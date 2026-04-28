---
layout: page
title: MySurgeryRisk — Clinical AI Platform
description: Clinical risk prediction platform at UF Health/UF Shands Hospital. Predicts post-surgical complications using HL7 FHIR pipelines, Mirth Connect integration, and ensemble ML models (AUC 0.82–0.94).
img: assets/img/projects/mysurgeryrisk.png
importance: 2
category: healthcare-ai
tags: [HL7, FHIR, Mirth Connect, Clinical AI, Python, PostgreSQL]
---

## Overview

**MySurgeryRisk** is a clinical decision support platform deployed at UF Health / UF Shands Hospital, providing real-time surgical risk prediction for clinical staff and surgeons. Built during my postdoctoral fellowship in Biomedical Informatics at the University of Florida.

The system ingests live patient data from the Epic EHR via HL7 v2 and FHIR R4 feeds, processes it through a clinical feature engineering pipeline, and serves risk scores to clinical staff in real time.

## Clinical Impact

- **AUC 0.82–0.94** across multiple surgical complication endpoints (mortality, ICU admission, prolonged LOS)
- Integrated into pre-operative workflow at UF Shands Hospital
- Powers clinical staff decision-making for high-risk patient identification

## Technical Architecture

### EHR Integration

- **Mirth Connect** (certified) for bidirectional HL7 v2 message processing — ADT, ORU, ORM message types
- **FHIR R4 APIs** for patient demographics, encounters, observations, and care plans
- Real-time feed from Epic with interface specifications co-designed with Epic analysts

### ML Pipeline

- Ensemble model stack: Logistic Regression, Random Forest, Gradient Boosting
- Feature engineering from ICD codes, lab values, vitals, medication history, and surgical history
- PostgreSQL backend with HIPAA-compliant audit logging and encryption at rest/in transit

### Compliance

- HIPAA-compliant data handling throughout (encryption in transit, audit logging, RBAC, minimum necessary access)
- Clinical staff training and ongoing monitoring post-deployment

## Publications

This work generated multiple peer-reviewed publications in clinical informatics and biomedical AI.

## Tech Stack

`Python` · `Mirth Connect` · `HL7 v2/FHIR R4` · `Epic EHR` · `PostgreSQL` · `scikit-learn` · `Flask` · `Linux`
