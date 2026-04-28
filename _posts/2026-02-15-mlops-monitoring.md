---
layout: post
title: "MLOps Monitoring: The Tools Actually Worth Using in 2026"
date: 2026-02-15
description: A practitioner's comparison of Evidently, Arize Phoenix, Azure ML Monitor, and LangSmith for production ML and LLM monitoring — based on real deployments.
tags: [MLOps, monitoring, Evidently, LangSmith, Arize, Azure ML]
categories: writing
related_posts: true
---

Production ML monitoring is crowded with tools that promise everything and deliver complexity. Here's what I've actually used across healthcare AI and industrial ML projects, and what each tool is genuinely good at.

## The Four Tools I Use

### Evidently — Best for Classic ML Drift

If you have a traditional ML model (classification, regression) in production, Evidently is the most practical starting point. It generates readable HTML reports on data drift, target drift, and data quality without much setup.

```python
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=train_df, current_data=production_df)
report.save_html("drift_report.html")
```

I've used this at Intuitive Surgical to monitor sensor feature distributions for the surgical robot predictive maintenance system. When a robot gets a firmware update that changes sensor calibration, Evidently catches the resulting distribution shift within days.

**Limitation:** Not built for LLMs or agentic systems. Text drift is possible but awkward.

### LangSmith — The Standard for LLM/RAG Monitoring

If you're building with LangChain or LangGraph, LangSmith is the obvious choice. It traces every step of your chain — retrieval, generation, tool calls — and stores structured run data that you can query and evaluate against.

What makes it worth using: the combination of **tracing + evaluation datasets + CI/CD integration**. You can define evaluation rubrics, run them against your traces, and set up automated testing pipelines.

I use LangSmith on every agentic AI project now. The ability to replay a failing trace and understand exactly which retrieval step went wrong is invaluable.

### Arize Phoenix — Best for Embedding Drift

When your vector store ages and queries stop matching well, the symptom is retrieval degradation. Arize Phoenix is the best tool I've found for visualizing embedding space drift and identifying which query clusters are underperforming.

It also has UMAP visualizations of your embeddings over time — genuinely useful for diagnosing retrieval regression when you re-index or change your embedding model.

### Azure ML Monitor — Production MLOps in Azure

If your stack is Azure (Azure ML, Databricks, Azure Event Hubs), Azure ML Monitor gives you model performance tracking and data drift monitoring that integrates natively with your deployment infrastructure. The dashboard is less polished than Evidently's reports, but the integration with Azure ML pipelines is seamless.

Used this at Cummins for fleet-level model health monitoring across thousands of connected engines.

## My Current Stack

| Use Case         | Tool             |
| ---------------- | ---------------- |
| Classic ML drift | Evidently        |
| LLM/RAG tracing  | LangSmith        |
| Embedding drift  | Arize Phoenix    |
| Azure production | Azure ML Monitor |

No single tool covers everything. The combination of Evidently (classical ML) + LangSmith (LLM layer) covers 90% of what most teams need.

## The Monitoring You Actually Need

Tooling aside, here's the minimum viable monitoring setup I recommend:

1. **Data drift alert** on your top 10 input features (Evidently)
2. **Retrieval Hit Rate@5** tracked weekly (LangSmith + custom evaluator)
3. **Faithfulness score** tracked on a sample of production queries (RAGAS via LangSmith)
4. **Latency p50/p99** for your full pipeline (any APM tool)
5. **Error rate** on LLM API calls and vector store queries

If those five metrics are green and trending right, your system is almost certainly behaving. If any one of them degrades, you have a signal to investigate before users notice.
