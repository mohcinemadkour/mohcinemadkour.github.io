---
layout: page
title: Surgical Robot Fleet — Predictive Maintenance MLOps
description: End-to-end MLOps system for predictive maintenance of a global surgical robot fleet at Intuitive Surgical. Achieved 25% reduction in unplanned downtime and $700K+ in savings through CI/CD pipelines, automated model monitoring, and real-time alerting.
img: assets/img/projects/surgical_robot.png
importance: 1
category: mlops
tags: [MLOps, MLflow, CI/CD, Azure ML, Python, Predictive Maintenance]
---

## Overview

At **Intuitive Surgical**, I designed and deployed a production MLOps system for predictive maintenance of the da Vinci surgical robot fleet — a globally distributed set of high-value medical devices where unplanned downtime has direct patient care consequences.

## Business Impact

- **25% reduction in unplanned downtime** across the global surgical robot fleet
- **$700,000+ in annual cost savings** from prevented emergency service dispatches and extended component life
- Shifted maintenance posture from reactive → condition-based → predictive

## MLOps Architecture

### Data Pipeline

- Real-time telemetry ingestion from robot IoT sensors (vibration, temperature, motor current, error codes)
- PySpark-based feature engineering at scale
- Delta Lake on Azure for reliable data versioning

### Model Layer

- Failure prediction models: XGBoost, LSTM for temporal patterns
- Multi-label classification across failure modes (mechanical, electrical, software)
- MLflow experiment tracking, model registry, and artifact versioning

### CI/CD for ML

- GitHub Actions pipelines: data validation → training → evaluation → staging → production promotion
- Automated retraining triggers on data drift detection
- Quality gates: F1, AUC, and calibration thresholds enforced before any model promotion

### Monitoring

- **Evidently** for feature drift and data quality monitoring
- **Azure ML Monitor** for production model performance tracking
- PagerDuty alerting for threshold violations
- Weekly monitoring reports auto-generated and distributed to engineering leadership

## Tech Stack

`Python` · `PySpark` · `MLflow` · `Azure ML` · `Delta Lake` · `XGBoost` · `PyTorch/LSTM` · `Evidently` · `GitHub Actions` · `Docker`
