---
layout: page
title: RAG-Based Predictive Maintenance System
description: Production RAG pipeline for industrial predictive maintenance using ChromaDB, XGBoost, and a Claude-powered recommendation layer — built on the AI4I 2020 dataset.
img: assets/img/projects/rag_pm.png
importance: 1
category: mlops
tags: [RAG, ChromaDB, XGBoost, LangChain, MLflow, Python]
github: https://github.com/mohcinemadkour
---

## Overview

A full production-grade **RAG (Retrieval-Augmented Generation) pipeline** for predictive maintenance in industrial settings, built from scratch on the AI4I 2020 machine failure dataset.

The system combines classical ML (XGBoost failure prediction) with a vector retrieval layer (ChromaDB) and an LLM-powered recommendation engine (Claude) to deliver actionable maintenance alerts with contextual justification.

## Architecture

```
Sensor Data → Feature Engineering → XGBoost Failure Classifier
                                         ↓
                              ChromaDB Vector Store
                              (historical failure patterns)
                                         ↓
                           Claude Recommendation Layer
                                         ↓
                         Maintenance Alert + Justification
```

## Key Components

- **Ingestion pipeline** — batch simulation of sensor telemetry with realistic noise and drift
- **XGBoost classifier** — trained on AI4I 2020 dataset (tool wear, heat dissipation, torque, rotational speed features)
- **ChromaDB vector store** — embeds historical failure events for semantic retrieval
- **Claude recommendation layer** — synthesizes classifier output + retrieved context into natural-language maintenance recommendations
- **Retrieval evaluation module** — Hit Rate@K, MRR, and NDCG metrics to benchmark retrieval quality
- **MLflow tracking** — experiment logging, model registry, and artifact storage

## Results

- Retrieval Hit Rate@5: **0.87**
- XGBoost F1 (failure class): **0.91**
- End-to-end latency (recommendation): **< 2s**

## Tech Stack

`Python` · `LangChain` · `ChromaDB` · `XGBoost` · `MLflow` · `Pandas` · `Anthropic API` · `Streamlit`
