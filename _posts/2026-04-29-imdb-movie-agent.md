---
layout: post
title: "Building a Conversational Voice Agent for IMDB Data with LangGraph, FAISS, and Streamlit"
description: "A deep dive into the architecture and design decisions behind a GenAI-powered movie assistant that combines structured pandas queries, semantic vector search, and LLM reasoning into a single voice-enabled chat interface."
tags: [LangGraph, RAG, FAISS, Streamlit, LLM, GenAI, Python, Voice-AI, Agentic-AI]
categories: writing
related_posts: true
---

Answering a question like _"Al Pacino movies grossing over $50M with an IMDB rating above 8"_ requires a very different execution path than _"comedy movies involving death or dead people."_ The first is a structured filter on tabular data; the second is a semantic concept search over plot summaries. A single query strategy cannot handle both well.

This post walks through how I built **IMDB Movie Agent** — a conversational voice assistant powered by GPT-4o, LangGraph, FAISS, and Streamlit — that routes each question to the right tool automatically, streams the answer token-by-token, and can both listen and speak.

**Live demo:** [imdb-movie-agent.onrender.com](https://imdb-movie-agent.onrender.com/)  
**Source:** [github.com/mohcinemadkour/IMDB_Movie_Agent](https://github.com/mohcinemadkour/IMDB_Movie_Agent)

---

## The Problem: One Dataset, Two Fundamentally Different Query Types

The IMDB Top 1000 dataset is a rich CSV with rating, gross revenue, genre, director, cast, runtime, and — crucially — a free-text `Overview` column containing plot summaries. Most applications would build either a filter UI or a semantic search box. Neither alone is enough.

| Query type  | Example                                       | Right approach                       |
| ----------- | --------------------------------------------- | ------------------------------------ |
| Structured  | "Top 5 horror movies of 2019 by meta score"   | pandas filter + sort                 |
| Semantic    | "Movies about police corruption in the 70s"   | vector similarity on plot text       |
| Hybrid      | "Spielberg sci-fi with IMDB ≥ 8"              | structured filter + semantic re-rank |
| Aggregation | "Directors with 2+ films grossing over $500M" | pandas groupby                       |

The architecture had to support all four patterns from a single natural-language input, without asking the user to choose.

---

## Architecture Overview

The system is organized into four layers:

```
Browser (User)
   │  chat input │ voice recorder │ sidebar settings
   │
app.py  (Streamlit)
   │  _speak() / OpenAI TTS / gTTS
   │  _transcribe_audio() / Whisper STT
   │  st.write_stream() / token streaming
   │
agent/agent.py  (LangGraph ReAct agent)
   │  build_agent_executor()  → LLM + tools + system prompt
   │  stream_agent()          → token-by-token generator
   │
   ├── structured_query    (pandas filters)
   ├── semantic_search     (FAISS + OpenAI embeddings)
   └── director_gross_summary  (pandas aggregation)
         │
   data/loader.py     (CSV cleaning, lru_cache)
   data/vectorstore.py (FAISS / Pinecone / ChromaDB)
         │
   imdb_top_1000.csv  +  data/faiss_index/
```

---

## Layer 1 — Presentation: Streamlit

Streamlit was chosen deliberately over Flask or FastAPI for the UI layer. Its reactive execution model means the entire script re-runs on each user interaction, which maps naturally to a chat interface where every new message updates state. Critically, two Streamlit primitives did the heavy lifting:

### `@st.cache_resource` for shared read-only objects

The IMDB DataFrame and the FAISS vector index are large objects — loading them on every rerun would be unacceptably slow. `@st.cache_resource` loads each exactly once per Streamlit worker process and shares them across all browser tabs:

```python
@st.cache_resource(show_spinner="📊 Loading IMDB dataset…")
def _load_shared_df():
    from data.loader import load_data
    return load_data()

@st.cache_resource(show_spinner="🔍 Loading vector index…")
def _load_shared_vectorstore():
    return get_vectorstore(_load_shared_df())
```

Because both objects are read-only after initialization, sharing them across sessions is safe. The agent executor — which holds per-session conversation history — lives in `st.session_state` so each browser tab gets its own isolated copy.

### `st.write_stream` for token-by-token streaming

Long LLM responses feel sluggish if rendered all at once. `st.write_stream()` accepts a generator and renders each yielded chunk as it arrives, giving users immediate feedback:

```python
response = st.write_stream(
    stream_agent(st.session_state.agent_executor, user_input, history)
)
```

This one line drives the entire streaming UI. The underlying `stream_agent()` generator is built on LangGraph's `stream_mode="messages"`, which yields tokens as the model produces them.

### Voice I/O

The sidebar hosts two optional voice capabilities:

- **Voice input**: `audio_recorder_streamlit` renders a microphone widget. On recording completion, raw audio bytes are sent to OpenAI's `whisper-1` model, which returns a transcript that is injected into the chat as a normal text query.
- **Voice output**: After each assistant response, `_speak()` calls OpenAI TTS (`tts-1`) to generate audio and renders an `st.audio()` player. If the OpenAI TTS call fails (e.g., rate limit), gTTS provides a free fallback for the first 500 characters.

The TTS engine and voice (nova, alloy, echo, fable, onyx, shimmer) are selectable per session from the sidebar, with no page reload required.

### Browser-session key entry

Rather than loading the API key from a `.env` file on disk, the app prompts each user to paste their own OpenAI API key directly into the browser. The key is stored only in `st.session_state` — it never touches disk, is not shared across sessions, and is cleared on page refresh. If a key turns out to be invalid, the app clears the session key and returns the user to the entry screen automatically.

---

## Layer 2 — Reasoning: LangGraph ReAct Agent

The core of the system is a **LangGraph ReAct agent** — a reasoning loop where the LLM alternates between thinking and acting (calling tools), until it has enough information to compose a final answer.

### Why LangGraph over bare LangChain?

LangChain's older `AgentExecutor` was serviceable but opaque. LangGraph models the agent as an explicit graph of nodes and edges, which gives three concrete benefits used here:

1. **Controllable recursion depth** — `MAX_AGENT_ITERATIONS = 10` caps the number of LLM + tool steps, preventing runaway API spend on pathological inputs.
2. **`stream_mode="messages"`** — yields prose tokens from the LLM node directly, separate from tool-dispatch JSON. The streaming layer filters out tool-call chunks so only the final narrative reaches the UI.
3. **Multi-tool chaining** — for hybrid queries, the agent calls both `structured_query` and `semantic_search` in a single reasoning pass, then synthesises the combined results.

### System prompt as routing logic

The agent's behavior is controlled almost entirely through the system prompt in `agent/prompts.py`. It encodes rules like:

- When a query mentions a director's name with numeric filters → prefer `structured_query`
- When a query references themes, plot elements, or vibes → prefer `semantic_search`
- "All" or "every" queries → set `limit: 500` to avoid silent truncation
- Count-only queries → set `count_only: true` to avoid transferring full row data
- After every answer → append 2–3 movie recommendations

This makes the routing declarative and auditable without touching code.

### LLM caching

Repeated identical queries — which are common for demo apps — hit a SQLite cache keyed on `(prompt, model)`:

```
LLM_CACHE=sqlite   → .cache/llm_cache.db  (default, persists across restarts)
LLM_CACHE=memory   → in-process, cleared on restart (used on Render free tier)
LLM_CACHE=none     → disabled
```

The free tier deployment on Render uses `LLM_CACHE=memory` because the free instance doesn't have persistent disk writes.

---

## Layer 3 — Tools: Three Strategies, One Interface

Each tool is a LangChain `@tool`-decorated function registered with the agent. The agent sees their docstrings as routing instructions.

### Tool 1: `structured_query` — pandas filters

Handles numeric comparisons, sorting, genre filtering, director/actor lookups, and count aggregations. The agent passes a JSON payload:

```json
{
  "genre": "Horror",
  "year_min": 2015,
  "imdb_min": 7.5,
  "sort_by": "IMDB_Rating",
  "limit": 10
}
```

The tool applies each present key as a pandas filter, sorts, limits, and returns a markdown table. Hard cap: 500 rows maximum regardless of what the LLM requests.

### Tool 2: `semantic_search` — FAISS + OpenAI embeddings

Handles conceptual queries against the `Overview` (plot summary) column. The agent passes a natural-language description:

```
"dark psychological thriller involving memory loss"
```

The tool calls `FAISS.similarity_search(query, k=10)` using OpenAI `text-embedding-3-small` embeddings (1536 dimensions). The pre-built FAISS index is committed to the repository at `data/faiss_index/`, so no re-embedding is required on first run or deployment — the app is ready instantly.

The choice of `text-embedding-3-small` over `text-embedding-ada-002` was deliberate: it is cheaper, faster, and scores higher on the MTEB leaderboard for retrieval tasks. The 1536-dimension output fits comfortably in FAISS's flat L2 index without quantization.

### Tool 3: `director_gross_summary` — pandas aggregation

Handles the class of queries like "directors who have made at least two films grossing over $500M." This pattern requires a multi-row groupby aggregation that neither a simple filter nor a vector search can express. The tool accepts a `gross_threshold` float, groups by director, counts qualifying films, and returns the ranked result.

---

## Layer 4 — Data: CSV Cleaning and Vector Store Dispatch

### `data/loader.py`

The raw CSV has several columns stored as strings with embedded commas and unit suffixes. The loader normalizes these once at startup and caches the result with `@lru_cache(maxsize=1)`:

| Column          | Raw format     | Clean type                       |
| --------------- | -------------- | -------------------------------- |
| `Runtime`       | `"142 min"`    | `int`                            |
| `Gross`         | `"67,172,125"` | `float`                          |
| `No_of_Votes`   | `"2,043,759"`  | `Int64` (nullable)               |
| `Released_Year` | mixed strings  | `int` (non-numeric rows dropped) |

### `data/vectorstore.py` — provider-agnostic dispatch

The vector store backend is selected at runtime via `VECTOR_STORE` env var, with no code changes:

| Backend             | Use case                                                         |
| ------------------- | ---------------------------------------------------------------- |
| **FAISS** (default) | Local, zero-ops, pre-built index committed to repo               |
| **Pinecone**        | Cloud-hosted, suitable for larger corpora or multi-tenant setups |
| **ChromaDB**        | Self-hosted alternative, supports persistent or HTTP modes       |

All three backends expose the same `.similarity_search(query, k)` interface, so the tool layer is completely insulated from the vector store choice.

---

## Data Flow: A Hybrid Query End-to-End

To make this concrete, here is what happens when a user asks:

> _"Top 5 horror movies of 2020 with a dark disturbing plot"_

```
1. app.py:        truncate to 2000 chars → append to messages → st.write_stream()

2. stream_agent(): format_chat_history() → build LangGraph input → executor.stream()

3. LangGraph ReAct loop:
   Step 1 — LLM reasons: this query needs both tools
   Step 2 — calls structured_query({"genre":"Horror","year_min":2020,"year_max":2020,"limit":5})
               → pandas filter → 5 rows → markdown table
   Step 3 — calls semantic_search("dark disturbing horror plot")
               → FAISS similarity_search(k=10) → 10 docs with metadata
   Step 4 — LLM synthesises both results → prose response + 2 recommendations

4. st.write_stream(): renders tokens progressively in the chat bubble

5. _speak():      OpenAI TTS tts-1 → st.audio() player below the response
```

The filtering in step 2 and the semantic retrieval in step 3 run as separate tool calls within the same agent reasoning pass, and the LLM merges the evidence in step 4.

---

## Infrastructure Choices

### Deployment: Render.com

The live demo runs on Render's free tier using the `render.yaml` configuration. Render was chosen over Heroku or Railway because it supports WebSocket connections natively, which Streamlit requires for its real-time UI updates. The free tier's ephemeral disk means `LLM_CACHE=memory` is used instead of SQLite.

### Docker: multi-stage build

The Dockerfile uses a two-stage build: a builder stage that installs all wheels into `/install`, and a minimal `python:3.11-slim` runtime stage that copies only the installed packages — no compilers, no build tools. The container runs as a non-root `appuser`, and a health check polls `/_stcore/health` every 30 seconds.

### CI/CD: GitHub Actions

Every push and pull request to `master` runs three checks in sequence:

```
ruff check agent/ data/ tests/ app.py
  └─ mypy agent/ data/
       └─ pytest tests/ -q  (114 tests)
```

The 114 tests cover data cleaning edge cases, all three tool implementations, vector store provider dispatch, agent streaming behavior, and LLM cache integration.

### Observability: LangSmith

When `LANGCHAIN_TRACING_V2=true` is set, every agent invocation is traced to LangSmith with the full reasoning chain, per-step latency, token counts, and input/output payloads — without any code changes.

---

## Key Design Decisions

| Decision                                               | Rationale                                                                              |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| **LangGraph ReAct** over bare LangChain AgentExecutor  | Controllable recursion, first-class streaming, explicit graph makes behavior auditable |
| **FAISS committed to repo**                            | Zero-config startup — no re-embedding on first run or deployment                       |
| **`@st.cache_resource` for DF + vector store**         | Single load per worker; all browser sessions share the same read-only objects          |
| **Per-session `agent_executor` in `st.session_state`** | Each browser tab gets isolated conversation history                                    |
| **`stream_mode="messages"` in LangGraph**              | Token-by-token streaming eliminates long blank waits                                   |
| **Tool-dispatch chunk filtering**                      | Function-call JSON tokens are suppressed; only prose reaches the UI                    |
| **SQLite LLM cache**                                   | Exact-match queries served instantly without API calls on repeat                       |
| **Provider-agnostic vector store**                     | Switch between FAISS, Pinecone, and ChromaDB via env var — no code change              |
| **`text-embedding-3-small`**                           | Lower cost, higher retrieval quality than ada-002 on standard benchmarks               |
| **Non-root Docker user**                               | Defence-in-depth; container cannot write to system paths even if exploited             |

---

## What I Would Do Differently at Scale

The current design is intentionally simple — the entire dataset fits in memory, and the FAISS index is a flat file. For a production system with a larger corpus, several things would change:

- **Pinecone or Weaviate** instead of local FAISS, to support index updates without a full rebuild and to enable metadata pre-filtering before vector search.
- **Structured output parsing** on the tool inputs — right now the agent produces JSON strings that the tool parses; a schema-validated Pydantic model would catch malformed LLM outputs earlier.
- **Rate limiting and user quotas** — the current app uses whatever key the user provides, which means API spend is entirely user-controlled. A production deployment would proxy requests through a backend with per-user limits.
- **Async LangGraph** — the current streaming uses a sync generator. LangGraph's async API would allow multiple concurrent users without thread starvation on a single Streamlit worker.

---

## Try It

The live demo is at [imdb-movie-agent.onrender.com](https://imdb-movie-agent.onrender.com/). Bring your own OpenAI API key — it is stored only in your browser session and never on disk.

Some questions worth trying to see the different tool paths activate:

- _"Top 7 comedy movies 2010–2020 by IMDB rating"_ → `structured_query`
- _"Comedy movies involving death or dead people"_ → `semantic_search`
- _"Horror movies with meta score > 85 and IMDB rating > 8"_ → `structured_query` with two numeric filters
- _"Directors with 2 or more movies grossing over $500M"_ → `director_gross_summary`
- _"Top 5 horror movies of 2020 with a dark disturbing plot"_ → both tools, synthesised

The source code is on GitHub at [github.com/mohcinemadkour/IMDB_Movie_Agent](https://github.com/mohcinemadkour/IMDB_Movie_Agent).
