---
layout: post
title: "MCP vs Tool Calling vs Skills — And Where RAG Fits In"
date: 2026-05-04
description: The three ways to extend an LLM aren't interchangeable — each solves a different problem at a different layer. Here's the mental model, with RAG as a fourth axis you can't ignore.
tags: [MCP, Tool Calling, Skills, RAG, LLM, Agentic AI, Architecture]
categories: writing
related_posts: true
---

Many builders treat Tool Calling, MCP, and Skills as alternatives. They're not. They're **layers** — and if you add RAG to the picture, you get a complete architecture for production agents.

Here's how they differ, when each one wins, and how they fit together.

---

## The Mental Model

| Layer | What it is | What it defines |
|---|---|---|
| **Tool Calling** | A function | *What* the model can do |
| **MCP** | A protocol | *Where* to find what it can do |
| **Skill** | A playbook | *How* to do it well |
| **RAG** | A memory layer | *What to know* before acting |

These aren't competitors. A production agent in 2026 uses all four.

---

## Tool Calling — The Primitive

Tool calling is the lowest layer. You define a function schema in JSON, pass it in the request, and the model decides when to call it. Your code executes the call, and the result flows back as the next message.

```json
{
  "name": "query_db",
  "description": "Run a SQL query against the analytics database",
  "input_schema": {
    "type": "object",
    "properties": {
      "sql": { "type": "string" }
    },
    "required": ["sql"]
  }
}
```

**What it solves:** Letting the model trigger deterministic code — APIs, calculators, databases, internal services.

**The cost:** Every tool schema lives in context on every turn. At 50 tools, you've burned thousands of tokens before the model says a word. No discovery — every integration is hardcoded.

**Best for:** 1–10 tools, a single application, full runtime control.

---

## MCP — The Protocol

MCP (Model Context Protocol) is a standard for how LLM clients talk to tool servers. Instead of embedding tool schemas in every prompt, you point a client at an MCP server and it discovers capabilities at runtime.

```
Client (Claude, Cursor, your agent)
        ↕  MCP
Server (tools, resources, prompts)
```

Servers expose tools, resources, and prompt templates. Transport is flexible: stdio, SSE, or streamable HTTP. The spec is open and multi-vendor.

**What it solves:** The M×N integration problem. Build a server once; every MCP-compatible client gets it. Tools become portable across Claude, Cursor, your IDE, and your agent framework. Auth and ops are centralized for an entire team.

**The cost:** Servers need to be hosted and secured. Tools still consume context once loaded. It's the wrong abstraction when your workflow is instruction-heavy rather than action-heavy.

**Best for:** External systems, cross-app reuse, team-wide integrations.

---

## Skills — The Playbook

A Skill is a folder: `SKILL.md` + scripts + reference material + examples. It bundles everything the model needs to do a complex task *well* — not just the ability to do it, but the expertise.

```
skills/
├── docx-creator/
│   ├── SKILL.md          ← instructions, gotchas, conventions
│   ├── templates/
│   └── scripts/
├── pdf-filler/
│   ├── SKILL.md
│   └── examples/
└── code-reviewer/
    ├── SKILL.md
    └── style-guide.md
```

The model reads `SKILL.md` first — triggered by task type — and pulls in the rest progressively as needed. Nothing loads until it's relevant.

**What it solves:** Token bloat from always-loaded instructions. Complex multi-step workflows (generate a Word doc, fill a PDF form, parse a spreadsheet). Encoded tribal knowledge — style guides, edge cases, conventions — that would otherwise live only in human heads.

**The cost:** Filesystem-dependent. Less cross-vendor portable than MCP today. The quality of behavior is directly tied to the quality of authoring — a bad `SKILL.md` means bad output.

**Best for:** Workflows where *how* matters as much as *what*. Any task with non-obvious conventions or multi-step execution logic.

---

## RAG — The Memory Layer

RAG (Retrieval-Augmented Generation) is the layer the other three don't cover: **grounding the model in relevant knowledge before it acts.**

Without RAG, the model reasons from parametric memory alone — frozen at training cutoff, unaware of your docs, your domain, your product. With RAG, it retrieves the right context at the right moment and reasons over it.

```
Query → Embed → Vector Search → Retrieved Chunks → LLM → Response
                     ↑
              Your knowledge base
         (docs, manuals, tickets, code)
```

**What it solves:** Knowledge staleness. Domain specificity. Hallucination on factual questions. Any task where the answer lives in a corpus, not in weights.

**How it combines with the others:**
- **RAG + Tool Calling:** The model retrieves context, then calls a tool to act on it. Example: retrieve a patient record, then call `schedule_appointment()`.
- **RAG + MCP:** A RAG server exposed as an MCP resource — any client can retrieve from your knowledge base without embedding the retrieval logic in each app.
- **RAG + Skills:** A Skill's `SKILL.md` can instruct the model to retrieve domain-specific references before executing. Example: retrieve the relevant regulatory guideline before filling a compliance form.

**The cost:** Retrieval quality is everything. Poor chunking, weak embeddings, or missing reranking will silently degrade every downstream response. You need evaluation — Hit Rate, MRR, NDCG — not just vibes.

**Best for:** Any agent that needs to *know things* it wasn't trained on. This is most production agents.

---

## How the Layers Stack

Here's how a production agentic system assembles them:

```
User query
    ↓
[RAG] Retrieve relevant context from knowledge base
    ↓
[Skill] Load task-specific playbook (SKILL.md triggered by task type)
    ↓
[MCP] Discover available tools from connected servers
    ↓
[Tool Calling] Execute deterministic actions (API calls, DB writes, calculations)
    ↓
Response
```

Each layer handles what it's good at. None of them handles everything.

---

## Picking the Right Layer

| Situation | Reach for |
|---|---|
| Need the model to call your API | Tool Calling |
| Need tools reusable across apps or teams | MCP |
| Complex task with non-obvious conventions | Skill |
| Model needs to know things beyond its training | RAG |
| Production agent | All four |

---

The mistake isn't picking the wrong one. It's treating them as mutually exclusive and forcing every problem into whichever one you learned first.

Tool = a function. MCP = a contract. Skill = a playbook. RAG = a memory.

Production agents in 2026 use all of them. They're layers, not alternatives.
