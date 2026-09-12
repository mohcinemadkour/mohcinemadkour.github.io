---
layout: page
title: "Agentic AI Evaluation: Production-Ready Systems"
permalink: /agentic-ai-evaluation-course/
description: Build automated evaluation pipelines for RAG and agentic AI systems using LangGraph, LangSmith, and RAGAS.
---

This course teaches engineers and data scientists how to build **production-ready evaluation pipelines** for agentic AI and RAG systems — moving beyond manual spot-testing to systematic, automated, deployment-gated measurement.

### Course Overview

Shipping an agentic AI system without evaluation infrastructure is like deploying a web service with no monitoring. You will not know when it breaks — until your users tell you. In this course, you will go from manual spot-testing to a fully automated evaluation pipeline — with retrieval metrics, LLM-as-Judge scoring, CI/CD gates, and drift detection running on every deployment.

- **Platform**: Udemy
- **Status**: In Development (Launching 2026)
- **Duration**: 50+ Hours of Content (10 Modules, 60+ Lessons, 15 Labs)
- **Tech Stack**: `LangGraph` · `LangSmith` · `RAGAS` · `LangChain` · `ChromaDB` · `Python` · `GitHub Actions` · `Anthropic API`
- **Waitlist/Registration**: [Join the Waitlist on Udemy](https://udemy.com)

---

### What You'll Learn

#### Track A — Core Curriculum (Modules 1–5)

- **M1: Why Evaluation Matters (~60 min)**
  - Silent production failures, the Evaluation Pyramid, defining "production-ready," and course roadmap.
- **M2: Metrics Demystified (~80 min)**
  - Retrieval vs. generation metrics, precision/recall/F1 for RAG, LangSmith setup, tracing, and your first experiment.
- **M3: Building Retrieval Evaluators (~100 min)**
  - Hit Rate@K, MRR implementation, NDCG from scratch, RAGAS context precision/recall, and golden dataset construction.
- **M4: Generation Quality & LLM-as-Judge (~110 min)**
  - RAGAS faithfulness, answer relevancy, automated quality scoring, bias mitigation, and human-in-the-loop calibration.
- **M5: CI/CD Quality Gates (~90 min)**
  - GitHub Actions evaluation pipelines, configuration thresholds, and blocking bad deployments.

#### Track B — Advanced Modules (Modules 6–10)

- **M6: Embedding Drift & Re-indexing (~90 min)**
  - Cosine centroid drift, Spearman correlation, chunk-level citation tracking, and re-indexing strategy.
- **M7: Latency & Cost Optimization (~80 min)**
  - Profiling, cost-per-query, tradeoff visualization, and caching.
- **M8: Multi-Agent Evaluation (~100 min)**
  - Trajectory evaluation, tool call correctness, consistency testing, and team debugging.
- **M9: Healthcare RAG Case Study (~90 min)**
  - Clinical safety rubric, catching hallucinations, patient safety, and regulatory framing.
- **M10: Capstone Project (~120 min)**
  - Build your own evaluation framework, 9-deliverable checking, CI gate deployment, and portfolio writeup.

---

### Seven Production Artifacts You Will Build

1. **Retrieval Evaluator**: Measure Hit Rate@K, MRR, and NDCG against a golden dataset and publish to LangSmith.
2. **LLM-as-Judge Pipeline**: Automated generation quality scorer calibrated against human labels.
3. **CI/CD Quality Gate**: GitHub Actions workflow that runs your eval suite and blocks bad deployments on PRs.
4. **Embedding Drift Detector**: Monitor cosine centroid shift and trigger re-indexing on threshold exceedance.
5. **Multi-Agent Evaluation**: LangGraph-native evaluator scoring tool-call correctness and step trajectory.
6. **Clinical Safety Rubric**: Domain-specific evaluation framework designed for healthcare clinical accuracy.
7. **Full Eval Framework**: Modular evaluation framework documented and packaged for any agentic AI system.

---

### Target Audience

This is a hands-on engineering course designed for:

- **ML Engineers & AI Architects** maintaining production RAG/Agentic pipelines who need systematic quality measurement.
- **Senior Developers & Data Scientists** who have shipped LLM-powered features and need instrumentation for drift, cost, and hallucination.
- **Healthcare & Clinical AI Engineers** who need domain-specific evaluation rubrics.
- **Platform & DevOps Engineers** designing CI/CD quality gates for enterprise AI applications.

---

### Instructor

**Mohcine Madkour, PhD**  
_Senior AI/ML Engineer & Architect · Biomedical Informatics_

I have spent a decade building AI systems that run on real data — from the Da Vinci surgical robotics RAG system at Intuitive Surgical, to predictive maintenance pipelines at Cummins ($700K annual savings), to surgical risk prediction at UF Shands (AUC 0.82–0.94). In every one of those systems, the hardest problems were evaluation problems: knowing when retrieval drifted, catching hallucinations before clinicians did, and proving to stakeholders that the system was improving, not just changing. This course is what I wish had existed when I was building those systems.
