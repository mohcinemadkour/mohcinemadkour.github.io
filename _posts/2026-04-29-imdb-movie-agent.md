---
layout: post
title: "Building a Conversational Voice Agent for IMDB Data with LangGraph, FAISS, and Streamlit"
description: "A deep dive into the architecture and design decisions behind a GenAI-powered movie assistant that combines structured pandas queries, semantic vector search, and LLM reasoning into a single voice-enabled chat interface."
tags: [LangGraph, RAG, FAISS, Streamlit, LLM, GenAI, Python, Voice-AI, Agentic-AI]
categories: writing
related_posts: true
---

Movie data is a surprisingly rich playground for GenAI engineering. Questions range from exact lookups ("When did The Matrix release?") to fuzzy conceptual searches ("Horror movies with a dark, psychological plot") to multi-hop aggregations ("Directors with two or more films grossing over $500M"). No single retrieval strategy handles all of them well — and that tension is what makes the problem interesting.

This post walks through the architecture of [IMDB Movie Agent](https://github.com/mohcinemadkour/IMDB_Movie_Agent), a conversational voice agent built on the IMDB Top 1000 dataset. The system combines a **LangGraph ReAct agent**, **FAISS semantic search**, **pandas-based structured queries**, and **Streamlit** with optional voice I/O powered by OpenAI Whisper and TTS.

---

## The Core Problem: One Query Type Is Never Enough

A purely structured approach — SQL-style filters over a DataFrame — handles numeric queries and exact lookups precisely, but fails on plot-level concepts. A purely semantic approach — vector similarity over plot summaries — excels at "movies involving grief or loss" but can't reliably sort by IMDB rating or filter by decade. The solution is a **routing agent** that decides, query by query, which tool (or combination of tools) to invoke.

LangGraph's ReAct (Reason + Act) loop is a natural fit here: the LLM reasons about the query, picks tools, inspects results, and synthesizes a final answer — all within a controllable, inspectable graph.

---

## Architecture Overview

The system is organized into four layers:

```
Browser (voice/text input)
        │
        ▼
app.py  — Streamlit UI, voice I/O, streaming renderer
        │
        ▼
agent/  — LangGraph ReAct agent, LLM, prompt, caching
        │
   ┌────┴────────────────────────┐
   ▼                             ▼
structured_query            semantic_search
(pandas filters)            (FAISS + embeddings)
   │                             │
   └────────────┬────────────────┘
                ▼
        data/loader.py + data/vectorstore.py
                ▼
        imdb_top_1000.csv  +  data/faiss_index/
```

### Presentation Layer — `app.py`

The Streamlit frontend handles more than layout. Its key responsibilities:

- **Shared resource caching** via `@st.cache_resource` — the DataFrame and FAISS index are loaded once per worker process and shared across all browser tabs, avoiding redundant I/O.
- **Per-session isolation** — `agent_executor` lives in `st.session_state`, so each browser tab maintains its own independent conversation history.
- **Streaming UI** — `st.write_stream(stream_agent(...))` renders LLM tokens progressively as they arrive, eliminating the blank-wait problem common in chat interfaces.
- **Voice pipeline** — an `audio_recorder` widget captures microphone input, which is transcribed via OpenAI Whisper, injected as `pending_input`, and triggers a `st.rerun()`. On the output side, `_speak()` calls OpenAI TTS (`tts-1`) or gTTS as a free fallback, rendering audio inline with `st.audio()`.
- **Input guard** — messages are capped at 2,000 characters before reaching the agent, preventing prompt injection via oversized inputs.

### Agent Layer — `agent/`

The agent is built with `create_agent()` from LangGraph and compiled into a graph with a recursion limit of 10 steps (`MAX_AGENT_ITERATIONS`), which prevents runaway API spend on pathological queries.

**Tool routing** is governed by `agent/prompts.py`, which encodes decision rules in the system prompt:

- Route to `structured_query` for any numeric filter, sort, genre, director, or actor lookup.
- Route to `semantic_search` when the query references plot elements, themes, or concepts not captured in structured columns.
- Use `director_gross_summary` for blockbuster aggregation queries ("directors with 2+ films over $500M").
- For count-only queries, pass `count_only: true` to avoid fetching full result rows.
- For "all / every" queries, set `limit: 500` rather than defaulting to a small page size.

`stream_agent()` uses `stream_mode="messages"` in LangGraph to yield prose tokens as they generate, while filtering out tool-dispatch JSON chunks that should never reach the UI.

### Data Layer — `data/`

**`data/loader.py`** applies targeted cleaning to the raw CSV:

| Column          | Transform                                |
| --------------- | ---------------------------------------- |
| `Runtime`       | Strip `" min"`, cast to `int`            |
| `Gross`         | Remove commas, cast to `float`           |
| `No_of_Votes`   | Remove commas, cast to `Int64`           |
| `Released_Year` | Coerce to numeric, drop non-integer rows |

Results are cached with `@lru_cache(maxsize=1)` — the clean DataFrame is computed exactly once per process lifetime.

**`data/vectorstore.py`** abstracts over three vector backends: FAISS (default, local), Pinecone (cloud, managed), and ChromaDB (local or remote). All three embed the `Overview` (plot summary) column using OpenAI `text-embedding-3-small` (1536 dimensions) and expose a `.similarity_search(query, k=10)` interface, so the agent's tools are backend-agnostic.

The FAISS index is pre-built and committed to the repository. This is a deliberate design decision: zero-config startup, no re-embedding on first run or cold deployment.

---

## A Query End-to-End

Consider the query: _"Top 5 horror movies of 2020 with a dark plot."_

1. **app.py** truncates the input to 2,000 characters, appends it to the session message list, and calls `st.write_stream(stream_agent(...))`.
2. **stream_agent()** formats the conversation history into `HumanMessage` / `AIMessage` objects and passes them to the compiled LangGraph executor.
3. **LangGraph ReAct loop, Step 1**: The LLM reasons that both tools are useful — `structured_query` to filter by genre and year, `semantic_search` to surface plot similarity.
4. **Step 2**: `structured_query({"genre": "Horror", "year_min": 2020, "year_max": 2020, "limit": 5})` runs a pandas filter and returns 5 rows as a formatted table string.
5. **Step 3**: `semantic_search("dark disturbing horror plot")` runs a FAISS similarity search and returns 10 docs with metadata.
6. **Step 4**: The LLM synthesizes both result sets into a coherent prose response, respecting the system prompt's formatting rules (monetary values, numbered lists, mandatory 2–3 movie recommendations).
7. **st.write_stream()** renders tokens progressively. If voice output is enabled, `_speak()` fires after the full response is assembled.

---

## Key Design Decisions

**LangGraph over vanilla function calling.** LangGraph's graph abstraction makes multi-tool chaining, multi-turn memory, and recursion limits first-class features rather than bolted-on logic. The compiled graph is also straightforwardly observable via LangSmith tracing.

**FAISS index committed to the repo.** Committing the pre-built index trades repo size for zero-friction deployment. Any developer or CI runner can clone and run the app without an embedding API call. Rebuilding is a single function call when the dataset changes.

**SQLite LLM cache.** Exact-match queries — title lookups, count queries, rating filters — are served from cache on repeat without touching the OpenAI API. The cache survives restarts and is transparent to the agent.

**Non-root Docker user + multi-stage build.** The runtime image contains no compilers or build tools. The app runs as `appuser`, not root. These are small additions that meaningfully reduce the attack surface of a publicly hosted app.

**Tool-dispatch chunk filtering in `stream_agent()`.** LangGraph's `stream_mode="messages"` emits both tool-call JSON and prose tokens. Filtering out function-call chunks before yielding to the Streamlit renderer ensures users never see raw JSON mid-response.

---

## Observability

LangChain and LangGraph emit traces automatically when `LANGCHAIN_TRACING_V2=true` and a `LANGSMITH_API_KEY` are set in `.env`. No code changes are required. Every agent invocation appears in the LangSmith UI with the full reasoning chain, per-step latency, token counts, and input/output payloads — which makes debugging tool routing decisions considerably faster than log parsing.

Structured JSON logging (`python-json-logger`) covers every tool call and agent invocation with fields like `query`, `latency_ms`, and `rows_returned`, written to stdout and a rotating file (`logs/app.log`, 10 MB × 5 files).

---

## Testing

The test suite covers 114 tests across four modules:

| Module                | Tests | Focus                                  |
| --------------------- | ----- | -------------------------------------- |
| `test_loader.py`      | 27    | Cleaning rules, data types, edge cases |
| `test_tools.py`       | 36    | All three agent tools                  |
| `test_vectorstore.py` | 12    | Backend dispatch, force rebuild        |
| `test_agent.py`       | 39    | Agent scenarios, streaming, LLM cache  |

A GitHub Actions pipeline runs `ruff check → mypy → pytest` on every push and pull request to `master`.

---

## What This Pattern Generalizes To

The architecture here — a ReAct agent routing between a structured query tool and a semantic search tool over a fixed dataset — generalizes to any domain where queries span both exact lookup and conceptual similarity:

- **Medical literature**: filter by year, journal, study type (structured) + semantic search over abstracts (FAISS).
- **Legal documents**: filter by jurisdiction, date, case type (structured) + semantic search over case summaries.
- **Product catalogs**: filter by price, category, rating (structured) + semantic search over descriptions.

The key insight is that the routing logic lives in the system prompt, not in handcrafted classifier code. Updating tool-selection behavior is a prompt edit, not a code change — which dramatically lowers the iteration cost.

---

## Running It Yourself

```bash
git clone https://github.com/mohcinemadkour/IMDB_Movie_Agent.git
cd IMDB_Movie_Agent
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add your OPENAI_API_KEY
streamlit run app.py
```

Docker Compose is also available for a one-command local deployment with log persistence and volume-mounted index files.

The full architecture documentation, environment variable reference, and CI/CD setup are in the repository README and `architecture.md`.
