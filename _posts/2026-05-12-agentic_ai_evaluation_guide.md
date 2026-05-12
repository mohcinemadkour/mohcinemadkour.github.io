# Agentic AI Evaluation: From Development to Production
### A Practitioner's Guide for Engineers and Technical Leaders

> **Grounded in:** EquipmentIQ — a production multi-agent RAG system for CNC
> machinery predictive maintenance, built on 1,702 real vibration recordings
> from the Bosch CNC Machining Dataset (CC-BY-4.0). Every principle in this
> guide was learned from a real failure in a live system.

---

## Table of Contents

1. [Why Agentic AI Systems Require a Different Evaluation Model](#1-why-agentic-ai-systems-require-a-different-evaluation-model)
2. [The Evaluation Stack: Three Layers, Three Purposes](#2-the-evaluation-stack-three-layers-three-purposes)
3. [The Evaluation Lifecycle: Four Phases](#3-the-evaluation-lifecycle-four-phases)
   - [Phase 1 — Ground Truth Before Code](#phase-1--ground-truth-before-code)
   - [Phase 2 — Development Evaluation](#phase-2--development-evaluation)
   - [Phase 3 — Pre-Deployment Gates](#phase-3--pre-deployment-gates)
   - [Phase 4 — Continuous Production Monitoring](#phase-4--continuous-production-monitoring)
4. [The Metrics Reference](#4-the-metrics-reference)
5. [The Human Feedback Loop](#5-the-human-feedback-loop)
6. [Failure Mode Taxonomy](#6-failure-mode-taxonomy)
7. [The Live Debugging Cycle](#7-the-live-debugging-cycle)
8. [Domain Coverage Testing](#8-domain-coverage-testing)
9. [Key Principles for Technical Leaders](#9-key-principles-for-technical-leaders)
10. [Real-World Results: EquipmentIQ Benchmark](#10-real-world-results-equipmentiq-benchmark)

---

## 1. Why Agentic AI Systems Require a Different Evaluation Model

Traditional software systems are deterministic: a given input always produces
the same output. A sorting function returns the same sorted list every time.
A query against a relational database returns the same rows. Testing is
straightforward — write assertions, run them, read pass/fail.

Agentic AI systems break this contract at every layer.

### The Five Sources of Non-Determinism

| Source | Description | Impact on evaluation |
|---|---|---|
| **Intent classification** | The same query can be routed to different agents depending on model state, prompt phrasing, and context window content | Routing accuracy must be measured independently of retrieval quality |
| **Retrieval** | Vector similarity rankings shift when embeddings change, collections are updated, or the query distribution evolves | Retrieval metrics must be re-run after every knowledge base change |
| **Reranking** | Cross-encoder scores vary with model version, chunk boundaries, and co-occurring context | Reranker model versions must be pinned and change-controlled |
| **Generation** | LLM output is stochastic — the same prompt produces different answers across calls | Generation quality requires statistical sampling, not single-query testing |
| **Feedback loops** | The system changes over time as golden sets grow, prompts are tuned, and models are updated | Evaluation itself must be versioned and regression-tested |

### The Consequence for Engineering Teams

A system can produce plausible-looking answers while being fundamentally broken.
In the EquipmentIQ build, the orchestrator was returning answers within the
expected latency range with no errors — yet retrieval was returning 0.00 NDCG
across all collections. The answers were hallucinated. Without a structured
evaluation pipeline, this failure would have reached users.

> **The core principle:**
> Evaluation is not validation that the system works.
> It is the definition of what "working" means.

---

## 2. The Evaluation Stack: Three Layers, Three Purposes

Every agentic AI system must be evaluated at three distinct layers. These
layers are hierarchical — failures at Layer 1 make Layer 2 measurements
meaningless, and failures at Layer 2 make Layer 3 measurements misleading.

```
┌──────────────────────────────────────────────────────────────────┐
│  LAYER 3: System Health                                           │
│  Latency  ·  Token Cost  ·  Embedding Drift  ·  Feedback Rate   │
│  Measured: continuously in production                             │
├──────────────────────────────────────────────────────────────────┤
│  LAYER 2: Generation Quality                                      │
│  Faithfulness  ·  Answer Relevance  ·  LLM-as-Judge Score       │
│  Measured: on sampled production traffic and golden set           │
├──────────────────────────────────────────────────────────────────┤
│  LAYER 1: Retrieval Quality                                       │
│  NDCG@K  ·  Hit Rate@K  ·  MRR  ·  Routing Accuracy            │
│  Measured: against golden set before every deployment             │
└──────────────────────────────────────────────────────────────────┘
         Fix Layer 1 before measuring Layer 2.
         Fix Layer 2 before trusting Layer 3.
```

### Layer Interaction — Why Order Matters

| Scenario | Layer 1 state | Layer 2 state | What it means |
|---|---|---|---|
| Retrieval broken, generation good | NDCG = 0.00 | Faithfulness appears high | Faithfulness is measuring wrong context — false positive |
| Routing broken, retrieval correct | Hit Rate = 0.00 | Answers empty | Correct agent never runs — routing must be fixed first |
| Retrieval good, generation broken | NDCG = 1.00 | Faithfulness = 0.10 | Context not reaching synthesiser — code bug, not quality issue |
| All layers healthy | NDCG ≥ 0.70 | Faithfulness ≥ 0.80 | System is functioning correctly |

### What Each Layer Catches

**Layer 1** catches: wrong agent routing, empty retrieval, embedding
mismatches, golden set ID mismatches, similarity floor miscalibration.

**Layer 2** catches: hallucination, incomplete answers, ignored context,
synthesis prompt regressions, model degradation.

**Layer 3** catches: latency regressions, cost overruns, query distribution
drift, embedding space degradation, user satisfaction decline.

---

## 3. The Evaluation Lifecycle: Four Phases

Evaluation is not a one-time activity. It runs continuously across the full
system lifecycle, with different goals and methods at each phase.

```
PHASE 1              PHASE 2              PHASE 3              PHASE 4
Ground Truth    →    Development     →    Pre-Deploy      →    Production
                     Evaluation           Gates                Monitoring

Build golden         Unit tests           Numerical gates      Real-time traces
set before           Retrieval eval       CI/CD blocking       Sampled scoring
writing code         Routing checks       Load testing         Drift detection
                     Embed consistency    Regression suite     Feedback loop
```

---

### Phase 1 — Ground Truth Before Code

The most common and most damaging evaluation mistake is building the ground
truth test set after the system is already working. This creates circular
validation: the system is tuned until it passes tests written while observing
the system's output. The tests then measure the system's behaviour, not its
correctness.

**Ground truth must be built before the system runs.**

#### What the Golden Set Contains

A golden set is a curated collection of question-answer pairs where the correct
answer is known independently of what the system produces. For a multi-agent
RAG system, each entry specifies:

| Field | Description | Example |
|---|---|---|
| `query` | The natural language question | "What does error SPN-CR-001 mean?" |
| `agent` | Which agent should handle this query | `software` |
| `expected_doc_ids` | IDs of chunks that must appear in retrieval results | `["SPN-CR-001_chunk_0"]` |
| `ground_truth_answer` | The correct answer from authoritative source | "CRITICAL — spindle bearing failure..." |

#### Golden Set Sizing

| System size | Minimum entries | Entries per agent | Rationale |
|---|---|---|---|
| 1-agent system | 20 | 20 | Provides statistical stability for NDCG |
| 3-agent system | 30 | 10 per agent | One failure moves NDCG by 0.10 — detectable |
| 5-agent system | 50 | 10 per agent | Cross-domain pairs needed in addition |
| Production system | 90+ | 30 per agent | Organic growth from user feedback |

#### The Four Golden Set Rules

| Rule | Description | Risk if violated |
|---|---|---|
| **Use live collection IDs** | Extract expected_doc_ids by querying the live vector store — never write from memory | ID format mismatches produce NDCG = 0.00 regardless of retrieval quality |
| **Grow from failures** | Every production failure with a known correct answer becomes a new golden set entry | Test set becomes increasingly disconnected from real usage |
| **Version control** | Golden set changes require review — never update to make failing tests pass | Evaluation fraud: tests pass but system quality has not improved |
| **Minimum density** | At least 10 entries per agent | Fewer entries make metric noise indistinguishable from real signal |

---

### Phase 2 — Development Evaluation

During development, evaluation has a single goal: make retrieval and routing
deterministic before touching generation quality.

#### The Development Evaluation Loop

```
Write component
      ↓
Run unit tests (fast, mocked, every commit)
      ↓
Run retrieval evaluation (against live collections)
      ↓
         ┌─── NDCG ≥ 0.70? ───No──→ Diagnose layer 1 failure → Fix
         │
        Yes
         ↓
Run routing evaluation (40 labelled queries)
      ↓
         ┌─── Accuracy ≥ 95%? ──No──→ Fix intent classifier prompt → Retest
         │
        Yes
         ↓
Run generation evaluation (sampled)
      ↓
Commit
```

#### Unit Tests vs Evaluation Tests — Critical Distinction

| Dimension | Unit tests | Evaluation tests |
|---|---|---|
| **Purpose** | Verify code correctness | Measure system quality |
| **Output** | Binary pass/fail | Numerical score vs threshold |
| **Speed** | Milliseconds | Seconds to minutes |
| **Frequency** | Every commit | Scheduled or triggered |
| **Dependencies** | All mocked | Real collections and APIs |
| **Failure action** | Block commit | Diagnose and tune |
| **Example pass** | NDCG formula returns 0.0 when no match | NDCG ≥ 0.70 on 10 golden queries |
| **Example fail** | NDCG formula returns 1.28 (overflow bug) | NDCG = 0.27 on support collection |

Both are required. Neither replaces the other. In EquipmentIQ, 91 unit tests
ran in under 60 seconds with all external dependencies mocked. A separate
evaluation suite ran against live collections and real APIs. The unit tests
found the NDCG formula bug (returning 1.28). The evaluation suite found the
routing collapse (software domain scoring 30%).

#### The NDCG Formula — A Common Implementation Bug

NDCG is the industry standard retrieval quality metric. It rewards systems
that rank relevant documents at the top of the result list. The formula has
one common implementation error that produces values above 1.0 — a mathematical
impossibility that signals a bug in the evaluation code itself.

| Implementation | Formula | Result range | Correctness |
|---|---|---|---|
| **Incorrect** | relevance / (rank + 1) | [0, ∞) | ❌ Can exceed 1.0 |
| **Correct** | relevance / log₂(rank + 1) | [0, 1.0] | ✅ Mathematically bounded |

The correct NDCG computation:

```
For each retrieved document at rank r (starting at 1):
  DCG  += relevance(r) / log₂(r + 1)

For the ideal ranking of the same documents:
  IDCG += 1.0 / log₂(r + 1)   for each relevant doc in top-K positions

NDCG = DCG / IDCG   (clamped to [0.0, 1.0])
```

**Always add a hard clamp to [0.0, 1.0].** Any value above 1.0 is a formula
bug — not an exceptionally good retrieval result.

#### Routing Accuracy — The Overlooked Development Metric

In multi-agent systems, routing accuracy is as consequential as retrieval
quality. A query routed to the wrong agent produces a confidently-wrong answer —
often more harmful than an empty response, because it signals false certainty.

| Routing scenario | User experience | Risk level |
|---|---|---|
| Correct agent, relevant chunks | Accurate answer with citations | Low |
| Correct agent, irrelevant chunks | INSUFFICIENT_CONTEXT response | Medium — user knows to ask differently |
| Wrong agent, relevant chunks | Partial answer from wrong domain | High — misleading but not empty |
| Wrong agent, irrelevant chunks | INSUFFICIENT_CONTEXT from wrong domain | High — user has no path forward |
| Cross-domain when ambiguous | Parallel retrieval, merged context | Low — designed for ambiguity |

**Target: 95% routing accuracy on a labelled test set of 40 queries
(10 per domain).** This test must run after every change to the intent
classification prompt.

#### Embedding Consistency — The Silent Production Killer

The most architecturally damaging failure in EquipmentIQ was an embedding
dimension mismatch: documents were ingested using a 1536-dimensional embedding
model, but the retrieval layer was querying using a 384-dimensional model.
Every retrieval call silently returned empty results. The system appeared to
function — no errors, normal latency — but answers were hallucinated.

| Scenario | Symptom | Root cause |
|---|---|---|
| Dimension mismatch | Empty retrieval, random results | Different embedding model used for ingestion vs query |
| Model version mismatch | Declining NDCG after model update | Stored embeddings incompatible with new query embeddings |
| Distance metric mismatch | Scores outside expected range | Collection created with L2 distance, queried with cosine |

**The rule: one embedding model, one distance metric, specified in
configuration, referenced by every component that touches embeddings.**
Never hardcode embedding model names in individual scripts.

---

### Phase 3 — Pre-Deployment Gates

Every change that reaches production — new prompt, new chunk size, new
embedding model, new documents added, any code change — must pass a set of
numerical gates before deployment proceeds.

#### The Gate Framework

| Gate ID | Metric | Target | What it catches | Failure consequence |
|---|---|---|---|---|
| AC-001 | NDCG@5 per collection | ≥ 0.70 | Retrieval degradation from any cause | Deployment blocked |
| AC-002 | Hit Rate@5 per collection | ≥ 0.85 | Retrieval coverage loss | Deployment blocked |
| AC-003 | Generation Faithfulness | ≥ 0.80 | Synthesis hallucination regression | Deployment blocked |
| AC-004 | Routing accuracy | ≥ 95% on 40 queries | Intent classifier regression | Deployment blocked |
| AC-005 | P95 latency (single agent) | ≤ 10 seconds | Performance regression | Deployment blocked |
| AC-006 | P95 latency (cross-domain) | ≤ 20 seconds | Parallel retrieval overhead | Advisory |
| AC-007 | Domain Q&A coverage | ≥ 90% per domain | Knowledge base coverage gaps | Advisory, investigate |

#### Gate Calibration Strategy

Gates set too high block legitimate deployments. Gates set too low allow
regressions to reach production. The recommended calibration approach:

| System maturity | NDCG target | Faithfulness target | Routing target |
|---|---|---|---|
| Early development | ≥ 0.50 | ≥ 0.60 | ≥ 80% |
| Stable development | ≥ 0.70 | ≥ 0.80 | ≥ 95% |
| Production | ≥ 0.80 | ≥ 0.85 | ≥ 95% |
| Mature production | ≥ 0.90 | ≥ 0.90 | ≥ 97% |

Raise targets as the system matures. Do not start at maximum targets — this
creates evaluation debt where teams route around gates rather than fixing
underlying quality.

#### What Triggers a Gate Run

| Trigger | Gates that run | Rationale |
|---|---|---|
| Any prompt change | AC-001 to AC-004 | Prompts affect routing and synthesis quality |
| Chunk size / overlap change | AC-001, AC-002 | Chunking affects what retrieval can find |
| New documents added | AC-001, AC-002, AC-007 | New content may disturb existing retrieval |
| Embedding model change | AC-001 to AC-005 | Requires full collection rebuild |
| LLM model version change | AC-003, AC-004 | New models behave differently |
| Scheduled weekly | AC-001 to AC-007 | Catch silent degradation |

---

### Phase 4 — Continuous Production Monitoring

Production monitoring detects when a system that was working stops working,
before users notice. The challenge is cost: running full evaluation on every
production query is prohibitively expensive. The solution is tiered monitoring.

#### The Tiered Monitoring Architecture

| Tier | Trigger | What runs | LLM calls | Approx. cost/run |
|---|---|---|---|---|
| **Real-time** | Every query | Latency per node, routing domain, chunk count, similarity scores | 0 | $0.00 |
| **Sampled online** | 10–15% of traffic | Faithfulness, answer relevance, LLM-as-Judge | 2 | ~$0.004 |
| **Feedback-triggered** | Every user feedback submission | Failure mode classification, metric correlation | 1 | ~$0.001 |
| **Nightly batch** | Daily scheduled | Full NDCG/MRR across golden set, drift detection | 4–8 | ~$0.02 |
| **Weekly regression** | Weekly scheduled | Full golden set evaluation vs prior week baseline | 10–20 | ~$0.10 |
| **Deployment gate** | Every change | Full golden set + latency + routing accuracy | 15–25 | ~$0.10 |

At this cost structure, a mature system running 1,000 production queries per
day spends approximately $0.60–1.00 per day on evaluation infrastructure —
less than 0.1% of typical LLM API spend.

#### Embedding Drift Detection

Embedding drift occurs when the distribution of production queries diverges
from the distribution of indexed documents. This is not a code failure — it
is a natural consequence of a system being used in ways its designers did not
anticipate. If unchecked, it produces a gradual decline in NDCG that appears
in metrics weeks after the underlying cause.

```
DRIFT DETECTION MECHANISM

At collection creation:
  Compute mean embedding vector of all indexed documents (baseline centroid)
  Save baseline to file

Nightly:
  Compute current mean embedding vector of production query log
  Measure cosine distance between current and baseline centroids
  
  Distance < 0.10 → No action
  Distance 0.10–0.15 → Log and monitor
  Distance > 0.15 → Alert: review query distribution, consider re-indexing
```

#### Production Observability — What to Monitor

For each production query, a structured trace should capture the following
signals:

| Signal | Where captured | What it indicates when anomalous |
|---|---|---|
| Classification domain | Routing node | Shift toward cross_domain → prompt drift |
| Classification confidence | Routing node | Declining confidence → ambiguity in new query types |
| Chunks retrieved per agent | Agent nodes | Count dropping → embedding drift or collection issue |
| Top similarity score | Agent nodes | Score declining → query distribution shift |
| Synthesis latency | Synthesis node | Rising → context window growing, reduce top-K |
| Total tokens (in + out) | Synthesis node | Rising → cost management trigger |
| Citations in answer | Synthesis node | Declining → synthesis prompt regression |
| Answer length | Output | Declining sharply → INSUFFICIENT_CONTEXT pattern |

---

## 4. The Metrics Reference

### Retrieval Metrics

| Metric | Full name | Formula | Range | Interpretation |
|---|---|---|---|---|
| **NDCG@K** | Normalised Discounted Cumulative Gain | DCG / IDCG, where DCG = Σ rel(r) / log₂(r+1) | [0, 1] | Measures ranking quality — rewards relevant documents at top positions. 1.0 = perfect ranking. |
| **Hit Rate@K** | Hit Rate at K | 1 if any expected doc in top-K, else 0 | [0, 1] | Binary — did the system find at least one relevant document? |
| **MRR** | Mean Reciprocal Rank | Mean of 1/rank(first relevant doc) | [0, 1] | Measures how high the first correct answer appears. 1.0 = always rank 1. |
| **Routing Accuracy** | — | Correct routings / total queries | [0, 1] | Fraction of queries sent to the correct agent. |

### Generation Metrics

| Metric | What it measures | Interpretation |
|---|---|---|
| **Faithfulness** | Are factual claims in the answer grounded in retrieved context? | Low = hallucination risk. High = answer is evidence-based. |
| **Answer Relevance** | Does the answer directly address the question? | Low = topic drift or incomplete answers. |
| **LLM-as-Judge (1–5)** | Overall answer quality on a structured rubric | 4+ = acceptable for production. Below 3 = systematic prompt issue. |
| **Context Precision** | What fraction of retrieved chunks were used in the answer? | Low = retrieval returning noise. High = tight retrieval-synthesis alignment. |

### The Faithfulness Contradiction Pattern

A critical diagnostic signal: when faithfulness and LLM-as-Judge scores
contradict each other, the cause is almost always a bug in the evaluation
pipeline, not in the system.

| Faithfulness | LLM Judge | Diagnosis | Action |
|---|---|---|---|
| High (≥ 0.80) | High (≥ 4.0) | System working correctly | No action |
| Low (< 0.40) | High (≥ 4.0) | Context not reaching faithfulness scorer | Debug context passing in evaluation code |
| High (≥ 0.80) | Low (< 3.0) | Answer is grounded but incomplete or poorly structured | Improve synthesis prompt |
| Low (< 0.40) | Low (< 3.0) | Both retrieval and synthesis have issues | Fix retrieval first, then synthesis |

### System Health Metrics

| Metric | Normal range | Alert threshold | Response |
|---|---|---|---|
| **Embedding drift** (cosine distance) | 0.00 – 0.10 | > 0.15 | Review query distribution, update baselines |
| **P95 latency — single agent** | < 5 seconds | > 10 seconds | Reduce top-K, check collection size |
| **P95 latency — cross-domain** | < 10 seconds | > 20 seconds | Parallelism degraded, check async execution |
| **Routing accuracy** | > 97% | < 95% | Prompt regression, run routing test suite |
| **Discordant feedback rate** | < 10% | > 20% | Automated metrics miscalibrated |
| **INSUFFICIENT_CONTEXT rate** | < 5% | > 15% | Knowledge base coverage gap |

---

## 5. The Human Feedback Loop

Automated metrics scale to 100% of production traffic. They cannot capture
whether an answer was actually useful for a specific user's situation.
Human feedback provides the ground truth signal that calibrates whether
automated metrics are measuring the right things.

### The Four-Stage Feedback Pipeline

```
STAGE 1          STAGE 2          STAGE 3          STAGE 4
Capture     →    Extract     →    Correlate    →    Grow
                 Signal           with Metrics      Golden Set

Thumbs up/down   LLM classifies   Compare human    Negative feedback
+ free text      failure mode     vs automated     with known answer
                 from free text   scores           → new golden entry
```

### Stage 2 — Failure Mode Classification

Raw free-text feedback is noisy and inconsistent. Structuring it into
classified failure modes enables systematic diagnosis.

| Failure mode | Description | System implication |
|---|---|---|
| `wrong_answer` | Answer is factually incorrect | Retrieval returning wrong content, or synthesis hallucinating |
| `incomplete` | Answer addresses part of the question but misses key information | Context window too small, or relevant chunks below similarity floor |
| `hallucinated` | Answer contains information not in retrieved context | Synthesis prompt not enforcing grounding |
| `out_of_scope` | System answered a question it should have declined | Similarity floor too low, accepting irrelevant chunks |
| `correct` | Answer is accurate and complete | System functioning as intended |

### Stage 3 — Metric Calibration via Discordant Cases

| Human rating | Automated score | Label | Meaning |
|---|---|---|---|
| Positive | High faithfulness | Concordant positive | System working, metrics calibrated |
| Negative | Low faithfulness | Concordant negative | System failing, metrics correctly detecting |
| Negative | High faithfulness | **Discordant** | Metrics not measuring what matters to users |
| Positive | Low faithfulness | **Discordant** | Metrics measuring something wrong |

A discordant rate above 20% signals that automated metrics need recalibration.
The most common cause: faithfulness measures whether answers are grounded
in context, but users care whether answers are complete and actionable.
A grounded-but-incomplete answer scores high on faithfulness but low on
user satisfaction.

### The Feedback-Evaluation Relationship

> Human feedback calibrates automated metrics.
> Automated metrics scale human judgment.
> Neither replaces the other.

---

## 6. Failure Mode Taxonomy

This table documents every failure mode encountered in a production
multi-agent RAG system, its root cause, and the correct fix. The most
important column is "incorrect fix" — what teams do when they address
the symptom rather than the cause.

| Symptom | Root cause | Correct fix | Incorrect fix | Risk of incorrect fix |
|---|---|---|---|---|
| NDCG = 0.00 across all collections | Golden set IDs don't match live collection IDs | Rebuild golden set by querying live collections | Re-ingest all collections | Ingestion works fine — wasted effort, IDs still wrong |
| NDCG > 1.00 | DCG formula uses 1/(rank+1) instead of 1/log₂(rank+1) | Correct formula and add clamp | Lower evaluation targets | Metrics permanently untrustworthy |
| Faithfulness = 0.00, LLM Judge = 4+ | Context not passed to faithfulness scorer (code bug) | Debug context passing in evaluation pipeline | Tune synthesis prompt | Synthesis prompt is not the problem |
| Support queries route to cross_domain | Intent classifier has insufficient support-domain examples | Add examples + categorical rule to prompt | Lower confidence threshold | Ambiguous queries now route incorrectly to single agents |
| Software domain scores 30% on coverage test | Parameter/MID queries have vocabulary that sounds mechanical | Add software examples for parameter IDs, MID numbers | Increase top-K retrieval | Retrieval is not the problem — routing is |
| Empty retrieval despite populated collection | Embedding dimension mismatch (ingestion vs query) | Standardise embedding model across all components | Add more documents | More documents with same mismatch makes nothing better |
| Retrieval quality degrades after prompt update | New examples broke disambiguation of edge cases | Narrow example scope; add routing regression tests | Revert all prompt changes | Routing regression becomes permanent risk |
| Knowledge base content gap | Specific topic documented in source but not indexed | Add supplementary content file; re-ingest | Tune retrieval parameters | Parameters cannot retrieve content that was never ingested |
| Correct domain, INSUFFICIENT_CONTEXT answer | Query phrasing semantically distant from indexed text | Add synonymous phrasing to supplementary content | Lower similarity floor | Lower floor adds irrelevant chunks without helping |
| Good NDCG, poor user satisfaction | System answers question asked, not question intended | Review query intent; improve synthesis prompt | Tune retrieval | Retrieval is correct — intent interpretation is the issue |

---

## 7. The Live Debugging Cycle

When evaluation reveals a mismatch, the debugging process must follow a
strict order. Every step skipped creates new problems while appearing to
fix the current one.

### The Six-Step Cycle

| Step | Action | Output | Common mistake |
|---|---|---|---|
| **1. Observe** | Document exactly what the system did vs what it should have done | Precise, falsifiable problem statement | Jumping to a fix before fully characterising the problem |
| **2. Localise** | Test each layer independently to find where the failure originates | Layer identified: routing / retrieval / synthesis / evaluation | Testing the wrong layer and concluding no problem |
| **3. Fix** | Make exactly one change targeting the identified root cause | One changed file, one changed configuration value | Making multiple changes simultaneously |
| **4. Verify** | Run the specific failing query or test | Pass/fail on the originally failing case | Declaring success without running the specific case |
| **5. Regression** | Run the full golden set and coverage test | Confirmation that no previously-passing tests broke | Skipping regression and shipping a fix that breaks other tests |
| **6. Document** | Update golden set, change log, and repository history | Permanent record of root cause, fix, and verification | Undocumented fix that is silently broken six months later |

### Localisation: Testing Each Layer Independently

When an answer is wrong, the first task is identifying which layer produced
the failure. Each layer answers one specific diagnostic question:

| Layer | Diagnostic question | Evidence of layer failure |
|---|---|---|
| **Routing** | Was the query sent to the correct agent? | Wrong domain in routing output, or cross_domain with low confidence |
| **Retrieval** | Did the correct agent return relevant chunks? | Zero chunks, wrong source documents, or similarity scores below 0.15 |
| **Synthesis** | Did the LLM use the retrieved context faithfully? | Answer contains facts not in any retrieved chunk |
| **Evaluation** | Is the metric itself computing correctly? | NDCG > 1.0, faithfulness = 0.0 everywhere, golden set IDs mismatched |

This layered approach was critical in diagnosing the Zone C routing failure
in EquipmentIQ. The query "What error codes are triggered in Zone C?" routed
to the software agent at 85% confidence and returned INSUFFICIENT_CONTEXT.
Layer-by-layer diagnosis in 25 minutes:

| Step | Finding |
|---|---|
| Observe | Domain = software, confidence = 85%, answer = INSUFFICIENT_CONTEXT |
| Localise (routing) | Classifier reasoning: "query asks about error codes → software" — wrong |
| Localise (retrieval) | Software collection has no ISO zone documentation — retrieval correctly empty |
| Root cause | Vocabulary collision: "error codes" mapped to software, but ISO 10816-3 zones live in mechanical PDFs |
| Fix | Added 3 examples + 1 disambiguation rule to intent classification prompt |
| Verify | Query now routes to mechanical at 87% confidence with correct answer |
| Regression | All 30 golden set entries still passing — no regressions |

### The One-Change Rule

Making multiple changes in a single debugging cycle is the most common
cause of evaluation regressions that cannot be explained. When the next
evaluation run shows a different failure, there is no way to know which
change caused it.

| Scenario | What happened | Result |
|---|---|---|
| One change, problem fixed | Root cause identified and resolved | Trustworthy fix — can be documented and explained |
| One change, problem persists | Change did not address root cause | Clear signal to re-localise at the correct layer |
| Two changes, problem fixed | Either change A or B fixed it — unknown which | False confidence; the other change may have introduced a regression |
| Two changes, problem persists | Unknown interaction | Starting over from scratch is faster than debugging the combination |

---

## 8. Domain Coverage Testing

The golden set measures retrieval precision on specific known queries. It does
not measure whether the system can answer the full breadth of questions users
will actually ask. Domain coverage testing fills this gap.

### Golden Set vs Coverage Testing

| Dimension | Golden set evaluation | Domain coverage testing |
|---|---|---|
| **Purpose** | Verify retrieval quality on known queries | Verify the system handles the full query space |
| **Query source** | Carefully curated, verified ground truth | Representative sample of real user queries |
| **Pass criterion** | NDCG ≥ threshold | Answer contains expected key terms |
| **Frequency** | Every deployment (gate) | After major content or routing changes |
| **Failure action** | Block deployment | Diagnose failure type, fix root cause |
| **Scale** | 30–90 entries | 20+ per domain (80+ for 3-agent systems) |

A system can achieve NDCG = 1.00 on its golden set and still fail 30% of
domain coverage tests — because the golden set only covers the topics it
was designed around.

### The Four Coverage Failure Types

| Failure type | Description | How to diagnose | Fix |
|---|---|---|---|
| **Routing failure** | Query goes to wrong agent | Check routing output for correct domain | Add examples to intent classifier prompt |
| **Retrieval failure (empty)** | Correct agent, zero chunks returned | Inspect similarity scores; check embedding consistency | Fix embedding pipeline; lower similarity floor |
| **Content gap** | Query topic not in knowledge base | Check source documents for coverage | Add supplementary content; re-ingest |
| **Semantic mismatch** | Content exists but query phrasing doesn't match indexed text | Run direct collection query; compare phrasing | Add synonymous phrasing to supplementary content |

### EquipmentIQ Coverage Test Results

Two coverage tests were run against the EquipmentIQ system — a 20-query
mechanical domain test and an 80-query full-system test.

#### Test 1: 20-Query Mechanical Domain (DOC-EIQ-005 Vibration Monitoring)

| # | Query topic | Result | Failure type |
|---|---|---|---|
| 1 | Vibration classification standard | ✅ PASS | — |
| 2 | ISO 10816-3 machine group | ✅ PASS | — |
| 3 | Zone D RMS range and action | ✅ PASS | — |
| 4 | Error codes triggered in Zone C | ✅ PASS | — |
| 5 | Zone B vs Zone B Upper | ❌ FAIL | Content gap — "Zone B Upper" not explicitly documented |
| 6 | Statistical features per axis | ✅ PASS | — |
| 7 | Best early-fault indicator | ✅ PASS | — |
| 8 | Kurtosis alarm threshold | ✅ PASS | — |
| 9 | Crest Factor formula | ❌ FAIL | Semantic mismatch — formula exists but phrasing differs |
| 10 | Purpose of Mean feature | ✅ PASS | — |
| 11 | Fault category for tooth-pass frequency | ✅ PASS | — |
| 12 | Spindle bearing fault parameters | ✅ PASS | — |
| 13 | Operations affected by tool wear | ✅ PASS | — |
| 14 | Actuator fault indicators | ❌ FAIL | Routing failure — routed to cross_domain |
| 15 | Process anomaly signal | ✅ PASS | — |
| 16 | Normal range for P064 | ✅ PASS | — |
| 17 | VIB-SR-001 required action | ❌ FAIL | Missing data — error code not ingested |
| 18 | Critical range for P004 | ✅ PASS | — |
| 19 | Bosch dataset size | ❌ FAIL | Routing failure — dataset stats routed to cross_domain |
| 20 | Normal vs fault sample breakdown | ❌ FAIL | Routing failure — same cause as #19 |

**Initial score: 14/20 (70%).** After five targeted fixes: **20/20 (100%).**

#### Test 2: 80-Query Full-System Validation

| Domain | Initial score | After Tier 1 fixes | Target |
|---|---|---|---|
| Mechanical | 16/20 (80%) | 17/20 (85%) | ≥ 90% |
| Software | 6/20 (30%) | 14/20 (70%) | ≥ 90% |
| Support | 14/20 (70%) | 15/20 (75%) | ≥ 90% |
| Cross-domain | 20/20 (100%) | 20/20 (100%) | ≥ 95% |
| **Overall** | **56/80 (70%)** | **66/80 (83%)** | **≥ 90%** |

**Key diagnostic insight from the 80-query test:** Cross-domain (parallel
retrieval across all three agents) scored 100% while software single-agent
scored 30%. This pattern is diagnostic — it means the knowledge base contains
the right content, but the routing layer is preventing the software agent from
being called for software-domain queries. The fix is in the intent classifier,
not in retrieval or the knowledge base.

### The Coverage Test as a Living Asset

Coverage tests must be re-run after:

| Change | Why re-run |
|---|---|
| New documents added to any collection | New content may conflict with existing retrieval, or queries about new content may fail |
| Intent prompt updated | New examples may break disambiguation of previously-correct queries |
| Chunk size or overlap changed | Different chunking distributes content differently, affecting semantic matches |
| Similarity floor adjusted | Threshold changes affect which queries return chunks vs INSUFFICIENT_CONTEXT |
| New query patterns observed in production logs | Emerging usage patterns may reveal new coverage gaps |

---

## 9. Key Principles for Technical Leaders

These principles distil the lessons from building, breaking, and repairing a
production multi-agent RAG system. They are relevant for anyone making
architectural, resourcing, or quality decisions about agentic AI systems.

### Principle 1 — Evaluation Defines Correctness

You cannot verify a system works by looking at it. In agentic systems, a
system producing answers with normal latency and no errors can simultaneously
be returning hallucinated content with 0.00 retrieval quality. The only way
to know is to measure. Evaluation is not a testing activity — it is the
engineering definition of what the system is supposed to do.

### Principle 2 — Layer Order is Non-Negotiable

Always diagnose and fix in layer order: routing → retrieval → generation →
system health. Generation metrics are meaningless when retrieval is broken.
A team that tunes the synthesis prompt while NDCG is 0.00 is not making the
system better — it is adding noise on top of a broken foundation.

### Principle 3 — Ground Truth Must Be Independent of the System

A golden set built by observing the system's output is not ground truth — it
is a description of the system's current behaviour. True ground truth requires
knowing the correct answer from an authoritative source before the system runs.
Golden sets built after the fact measure conformance to past behaviour, not
correctness.

### Principle 4 — Automated Metrics and Human Feedback Serve Different Purposes

| Automated metrics | Human feedback |
|---|---|
| Scale to 100% of traffic | Capture real-world usefulness |
| Consistent and reproducible | Noisy but authentic |
| Fast and cheap | Slow and expensive |
| Measure proxy signals | Measure actual user value |
| Can be fooled by metric gaming | Cannot be fooled |
| Tell you what changed | Tell you what matters |

Run both. When they disagree, human feedback is right and the automated metric
needs recalibration.

### Principle 5 — The Confidence Threshold is Not a Quality Control

A routing confidence threshold determines how much ambiguity the system
tolerates before routing to parallel retrieval. It is not a mechanism for
correcting routing errors. Lowering the threshold to fix a routing failure
shifts ambiguous queries to arbitrary single agents — it does not fix the
classifier. Every routing fix must happen in the classifier examples, not
in the threshold parameter.

### Principle 6 — Evaluation Infrastructure is Production Code

Evaluation code has the same failure modes as system code. The NDCG formula
bug (returning 1.28) gave false confidence about retrieval quality for an
entire development sprint. Evaluation scripts need the same engineering rigour
as the system they evaluate: unit tests, version control, code review, and
change management.

### Principle 7 — Coverage Debt Accumulates Silently

A system with NDCG = 1.00 on its 30-entry golden set can have 30% of real
user queries failing — because the golden set was built around the topics
the team thought about, not the topics users actually ask about. Domain
coverage tests, run regularly and grown organically from production failures,
are the mechanism for keeping evaluation aligned with real usage.

---

## 10. Real-World Results: EquipmentIQ Benchmark

EquipmentIQ is a three-agent RAG system for CNC machinery predictive
maintenance. The following results reflect the system state at the close of
Sprint 3 (evaluation pipeline complete) and the subsequent coverage testing
phase.

### System Architecture

| Component | Specification |
|---|---|
| Orchestration | LangGraph StateGraph, 8 nodes, conditional routing |
| Agents | 3 specialised (mechanical, software/error codes, customer support) |
| Vector store | 3 isolated ChromaDB collections |
| Embedding model | OpenAI text-embedding-3-small (1536 dimensions, cosine distance) |
| Reranker | Cross-encoder/ms-marco-MiniLM-L-6-v2 (top-8 → top-5) |
| Synthesis model | Anthropic Claude (Haiku for evaluation, Sonnet for production) |
| Confidence threshold | 0.75 (cross-domain below this) |
| Similarity floor | 0.15 (chunks below this score rejected) |

### Knowledge Base

| Collection | Source | Documents | Content type |
|---|---|---|---|
| mechanical_collection | 6 technical PDFs + supplementary | 66 chunks | Machine specs, wiring, maintenance, ISO standards |
| software_collection | 96 error code JSON files | 96 documents | Error codes, severity levels, parameters, diagnostics |
| support_collection | 150 complaint records CSV | 150 documents | Phone notes, investigation notes, RMA data, remedies |

### Retrieval Evaluation Results (Sprint 3 Close)

| Collection | NDCG@5 | Hit Rate@5 | MRR | Gate |
|---|---|---|---|---|
| mechanical_collection | 1.00 | 1.00 | 1.00 | ✅ PASS (≥ 0.70) |
| software_collection | 1.00 | 1.00 | 1.00 | ✅ PASS (≥ 0.70) |
| support_collection | 1.00 | 1.00 | 1.00 | ✅ PASS (≥ 0.70) |
| Embedding drift | 0.00 (baseline) | — | — | ✅ OK (< 0.15) |

### Domain Coverage Test Results

| Domain | Queries tested | Initial pass | After fixes | Fix types applied |
|---|---|---|---|---|
| Mechanical | 20 | 14/20 (70%) | 20/20 (100%) | 3 routing, 1 content gap, 1 ingestion |
| Software | 20 | 6/20 (30%) | 14/20 (70%) | 6 routing, ongoing |
| Support | 20 | 14/20 (70%) | 15/20 (75%) | 2 routing, 4 transient errors |
| Cross-domain | 20 | 20/20 (100%) | 20/20 (100%) | None required |
| **Total** | **80** | **54/80 (67%)** | **69/80 (86%)** | |

### Issues Encountered and Resolved

| Issue | Symptom | Root cause | Resolution |
|---|---|---|---|
| NDCG = 0.00 everywhere | All golden set queries scored zero | Golden set used short IDs; collection stored full filename IDs | Rebuilt golden set by querying live collections |
| NDCG > 1.00 | Score of 1.28 returned | DCG formula used 1/(rank+1) instead of 1/log₂(rank+1) | Corrected formula, added clamp |
| Faithfulness = 0.015 | Near-zero despite accurate answers | Faithfulness scorer received empty context list | Fixed context extraction in evaluation pipeline |
| Embedding mismatch | Empty retrieval across all collections | Ingestion used 1536-dim model; retrieval defaulted to 384-dim | Standardised embedding client across all components |
| Support NDCG = 0.27 | Support queries retrieving wrong content | Support queries routed to cross_domain (confidence 0.65–0.72) | Added complaint-specific examples to intent classifier |
| Software coverage 30% | Parameter/MID queries routed to mechanical | Classifier lacked software examples for these query patterns | Added 9 software examples + disambiguation rule |
| Zone C routing failure | "Error codes in Zone C" → software agent | "error codes" keyword overrode vibration context | Added mechanical examples for ISO zone queries |
| Zone B Upper content gap | No chunks matched Zone B Upper threshold | Specific sub-zone not explicitly named in source PDFs | Created supplementary content file with explicit zone table |

### Test Infrastructure

| Component | Count | Coverage |
|---|---|---|
| Unit tests | 91 | Config, ingestion, agents, orchestrator, evaluation, feedback |
| Integration tests | 12 | End-to-end with live API calls |
| Golden set entries | 37 | 10+ per agent, grown from failures |
| Coverage test queries | 80 | 20 per domain |
| Evaluation tiers | 6 | Real-time through weekly regression |

---

## Appendix A — Metric Quick Reference

| Metric | Layer | Formula summary | Target | Alert threshold |
|---|---|---|---|---|
| NDCG@5 | Retrieval | Σ rel(r)/log₂(r+1) normalised | ≥ 0.70 | < 0.50 |
| Hit Rate@5 | Retrieval | Any relevant in top-5 | ≥ 0.85 | < 0.70 |
| MRR | Retrieval | Mean 1/rank(first relevant) | ≥ 0.60 | < 0.40 |
| Routing accuracy | Retrieval | Correct routings / total | ≥ 95% | < 90% |
| Faithfulness | Generation | Claims grounded in context | ≥ 0.80 | < 0.60 |
| Answer relevance | Generation | Answer addresses question | ≥ 0.75 | < 0.55 |
| LLM Judge | Generation | 1–5 rubric score | ≥ 3.5/5 | < 2.5/5 |
| Embedding drift | System | Cosine distance vs baseline | < 0.10 | > 0.15 |
| P95 latency (single) | System | 95th percentile ms | < 10,000 ms | > 15,000 ms |
| Domain coverage | Coverage | Pass rate on domain Q&A test | ≥ 90% | < 75% |
| Discordant rate | Feedback | Human-metric disagreement % | < 10% | > 20% |

## Appendix B — Diagnostic Decision Tree

```
WRONG OR EMPTY ANSWER
│
├─── Step 1: Was the query routed to the correct agent?
│    │
│    ├─── NO → Routing failure
│    │         Fix: Add examples to intent classifier prompt
│    │         Do NOT: Lower confidence threshold
│    │
│    └─── YES → Continue to Step 2
│
├─── Step 2: Did the correct agent retrieve relevant chunks?
│    │
│    ├─── ZERO CHUNKS → Check embedding consistency and similarity floor
│    │                  Check embedding dimensions match (ingestion vs query)
│    │
│    ├─── WRONG CHUNKS → Check golden set IDs match live collection
│    │                   Check if content exists in knowledge base at all
│    │
│    └─── RIGHT CHUNKS → Continue to Step 3
│
├─── Step 3: Did synthesis use the retrieved context?
│    │
│    ├─── CONTEXT IGNORED → Tighten synthesis prompt grounding instruction
│    │
│    ├─── HALLUCINATED → Verify context is passed correctly to synthesiser
│    │
│    └─── INSUFFICIENT_CONTEXT → Content gap: add supplementary content
│
└─── Step 4: Is the evaluation metric itself correct?
     │
     ├─── NDCG > 1.0 → Formula bug: use log₂(rank+1) not (rank+1)
     │
     ├─── Faithfulness = 0.0 everywhere → Debug context argument to scorer
     │
     └─── All metrics pass but answers wrong → Fix golden set IDs
```

---

*Mohcine Madkour, PhD — Senior AI/ML Engineer & Architect*
*EquipmentIQ Project — Multi-Agent RAG for Industrial Predictive Maintenance*
*Bosch CNC Machining Dataset (CC-BY-4.0) — Tnani et al. Procedia CIRP 2022, 107, 131–136*
