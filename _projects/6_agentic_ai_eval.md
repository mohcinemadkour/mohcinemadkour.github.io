---
layout: page
title: Agentic AI Evaluation Framework
description: Production-ready evaluation framework for agentic AI systems using LangGraph orchestration and LangSmith tracing. Covers retrieval metrics (Hit Rate@K, MRR, NDCG), generation metrics (RAGAS, LLM-as-Judge), and CI/CD quality gates.
img: assets/img/projects/agentic_eval.png
importance: 1
category: agentic-ai
tags: [LangGraph, LangSmith, RAGAS, RAG, Python, CI/CD]
github: https://github.com/mohcinemadkour
---

## Overview

A comprehensive **evaluation framework for production agentic AI systems**, built around LangGraph for orchestration and LangSmith for tracing and observability. This system closes the gap between prototype RAG pipelines and production-ready systems that can be monitored, tested, and continuously improved.

This framework is also the foundation of my Udemy course: **"Agentic AI Evaluation: Production-Ready Systems with LangGraph and LangSmith."**

## What It Evaluates

### Retrieval Metrics

- **Hit Rate@K** — fraction of queries where the correct document appears in top-K results
- **MRR (Mean Reciprocal Rank)** — measures ranking quality
- **NDCG (Normalized Discounted Cumulative Gain)** — position-weighted relevance scoring
- **RAGAS retrieval metrics** — context precision and context recall

### Generation Metrics

- **RAGAS generation metrics** — faithfulness, answer relevancy, answer correctness
- **LLM-as-Judge pipeline** — automated quality scoring with bias mitigation
- **Hallucination detection** — citation tracking and factual grounding checks

### System-Level Metrics

- End-to-end latency profiling
- Cost-per-query tracking
- Embedding drift detection

## CI/CD Integration

```yaml
# GitHub Actions quality gate
- Run retrieval evaluation suite
- Assert Hit Rate@5 > 0.80
- Assert RAGAS Faithfulness > 0.85
- Block promotion if thresholds fail
```

## Tech Stack

`LangGraph` · `LangSmith` · `RAGAS` · `LangChain` · `ChromaDB` · `Python` · `GitHub Actions` · `Anthropic API`
