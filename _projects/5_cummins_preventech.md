---
layout: page
title: Cummins PreventTech — Connected Diagnostics
description: Industrial IoT predictive diagnostics platform for connected engine fleets at Cummins. PySpark feature engineering at scale, Azure ML model training, and Databricks orchestration powering real-time fleet health scoring.
img: assets/img/projects/cummins.png
importance: 3
category: industrial-iot
tags: [PySpark, Azure ML, Databricks, IoT, Python]
---

## Overview

At **Cummins**, I contributed to the **PreventTech / Connected Diagnostics** platform — an industrial IoT system providing real-time health scoring and predictive diagnostics for connected engine fleets across global customers.

## Scale

- Millions of telemetry data points per day from connected diesel engines
- Fleet sizes ranging from a handful of vehicles to thousands of commercial trucks
- Real-time fault prediction and remaining useful life (RUL) estimation

## Technical Contributions

### Data Engineering
- **PySpark** feature engineering pipelines on Azure Databricks — processing raw CAN bus telemetry into ML-ready feature sets
- Streaming ingestion via Azure Event Hubs
- Data quality validation and schema enforcement at ingestion

### ML Platform
- **Azure ML** for model training, experiment tracking, and deployment
- Gradient boosting and LSTM models for fault code prediction and RUL estimation
- Model versioning and A/B testing framework

### Orchestration
- **Databricks** job orchestration for daily batch scoring across the full fleet
- Alerting pipeline: model output → fleet health dashboard → customer-facing recommendations

## Business Impact

- Enabled early fault detection days before engine failure events
- Reduced unplanned road breakdowns for commercial fleet customers
- Provided actionable maintenance recommendations through Connected Diagnostics dashboard

## Tech Stack

`PySpark` · `Azure ML` · `Databricks` · `Azure Event Hubs` · `XGBoost` · `PyTorch` · `Python` · `SQL`
