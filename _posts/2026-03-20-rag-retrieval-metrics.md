---
layout: post
title: "RAG Retrieval Metrics You Should Actually Be Tracking"
date: 2026-03-20
description: Hit Rate@K, MRR, NDCG — what they measure, when each one matters, and how to implement them for your RAG system.
tags: [RAG, retrieval, metrics, LangSmith, Python]
categories: writing
related_posts: true
---

If you're building a RAG system and not tracking retrieval metrics, you're flying blind.

Most teams measure answer quality — they ask "does the LLM give a good response?" But answer quality is a lagging indicator. Retrieval quality is the leading indicator, and it's where the problems start.

Here are the three retrieval metrics I use on every RAG project, and what each one tells you.

## Hit Rate@K

**What it measures:** Does the correct document appear anywhere in the top-K retrieved results?

```python
def hit_rate_at_k(retrieved_docs, relevant_doc_id, k):
    top_k_ids = [doc.id for doc in retrieved_docs[:k]]
    return 1 if relevant_doc_id in top_k_ids else 0

# Average over your test set
hit_rate = sum(hit_rate_at_k(r, rel, k=5) 
               for r, rel in zip(results, relevant_ids)) / len(results)
```

**When it matters most:** When your LLM has a large context window and can synthesize across multiple retrieved chunks. If you're passing top-5 to the LLM, Hit Rate@5 is your primary metric.

**Typical target:** > 0.80 for a well-tuned system.

## MRR (Mean Reciprocal Rank)

**What it measures:** How high does the correct document rank? Being first is better than being fifth, even if both count as a "hit."

```python
def reciprocal_rank(retrieved_docs, relevant_doc_id):
    for rank, doc in enumerate(retrieved_docs, start=1):
        if doc.id == relevant_doc_id:
            return 1 / rank
    return 0

mrr = sum(reciprocal_rank(r, rel) 
          for r, rel in zip(results, relevant_ids)) / len(results)
```

**When it matters most:** When your LLM only uses the top-1 or top-2 results. If the correct document is ranked 5th, MRR penalizes that even if Hit Rate@5 counts it as a success.

## NDCG (Normalized Discounted Cumulative Gain)

**What it measures:** Ranking quality across multiple relevant documents, with higher-ranked documents weighted more.

```python
from sklearn.metrics import ndcg_score
import numpy as np

# relevance_scores: list of [1, 0, 1, 0, 0] for each retrieved doc
ndcg = ndcg_score(
    y_true=np.array([relevance_scores]),
    y_score=np.array([retrieval_scores])
)
```

**When it matters most:** When queries have multiple relevant documents (e.g., "summarize everything about X") and you need to know if the most relevant ones rank highest.

## Putting It Together in LangSmith

```python
from langsmith import Client
from langsmith.evaluation import evaluate

def retrieval_evaluator(run, example):
    retrieved = run.outputs["retrieved_docs"]
    relevant = example.outputs["relevant_doc_ids"]
    
    return {
        "hit_rate_5": hit_rate_at_k(retrieved, relevant[0], k=5),
        "mrr": reciprocal_rank(retrieved, relevant[0]),
    }

results = evaluate(
    retrieval_pipeline,
    data="my-rag-test-dataset",
    evaluators=[retrieval_evaluator],
)
```

Track these weekly. When Hit Rate@5 drops below 0.80, investigate: did your data change? Did query distribution shift? Did someone modify the chunking strategy?

Retrieval metrics give you the early warning system that answer quality alone can't.
