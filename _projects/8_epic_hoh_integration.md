---
layout: page
title: Bidirectional Epic Integration for Hospital-at-Home
description: A working HL7 v2 + FHIR R4 integration engine connecting a Hospital-at-Home platform to Epic. Built, demoed live, and tested end-to-end.
img: assets/img/projects/epic_hoh.svg
importance: 1
category: portfolio
tags: [HL7 v2, FHIR R4, Mirth Connect, FastAPI, Python, Azure, HIPAA, Healthcare Interoperability]
---

<div class="row">
  <div class="col-sm-12">
    <span class="badge bg-secondary me-1">Healthcare Interoperability</span>
    <span class="badge bg-secondary me-1">Case Study</span>
  </div>
</div>

---

## Overview

A working **HL7 v2 + FHIR R4 integration engine** that moves admissions, diagnoses, and vitals in and out of Epic — built, demoed live, and tested end-to-end.

<div class="row my-4">
  <div class="col-6 col-md-3 text-center">
    <h3 class="fw-bold text-info">2</h3>
    <small class="text-muted">directions wired</small>
  </div>
  <div class="col-6 col-md-3 text-center">
    <h3 class="fw-bold text-info">5</h3>
    <small class="text-muted">FHIR resources</small>
  </div>
  <div class="col-6 col-md-3 text-center">
    <h3 class="fw-bold text-info">14</h3>
    <small class="text-muted">tests passing</small>
  </div>
  <div class="col-6 col-md-3 text-center">
    <h3 class="fw-bold text-info">0</h3>
    <small class="text-muted">messages dropped</small>
  </div>
</div>

<div class="row mt-3">
  <div class="col-sm-12">
    <a class="btn btn-sm btn-primary me-2" href="https://youtu.be/ApIp756c2C0" target="_blank" rel="noopener">▶ Watch the walkthrough</a>
    <a class="btn btn-sm btn-outline-secondary" href="https://github.com/mohcinemadkour" target="_blank" rel="noopener">View the code</a>
  </div>
</div>

---

## Video Walkthrough

{% include video.liquid path="https://www.youtube.com/embed/ApIp756c2C0" class="img-fluid rounded z-depth-1" %}

_Full guided tour — architecture, live inbound/outbound demos, reliability and HIPAA posture, and the path to a live Epic connection._

---

## The Problem

Every Hospital-at-Home platform stalls on the same thing: **Epic**.

A care platform can't admit a patient, show a vital sign, or bill until it exchanges data with each health system's Epic — in both directions, reliably, without dropping a message. That's hard for four reasons:

- It's **bidirectional** (admissions in, vitals out)
- It spans **two protocols** — HL7 v2 (legacy wire) and FHIR R4 (modern API)
- It carries **protected health information** under HIPAA
- Every Epic is **configured differently** per health system

This project is the layer that solves it — and proves it on a live stack rather than a slide.

---

## What I Built — Thin Transport, Fat Engine

**Mirth Connect** owns the wire: MLLP framing and the acknowledgment back to Epic. A **Python/FastAPI engine** owns everything clinical and stateful — parsing, FHIR mapping, idempotency, retries, the audit trail, and the care-coordination domain. It deploys as just another service in a Python/Azure stack.

```
┌─────────────────┐         ┌───────────────────────────────────────┐         ┌──────────────────┐
│   Epic  (EHR)   │  ⇄ ⇄ ⇄  │         Integration Engine            │  ⇄ ⇄ ⇄  │   HaH Platform   │
│                 │         │  Mirth Connect + Python/FastAPI        │         │                  │
│ HL7 v2 / MLLP  │         │  dedup · retry · dead-letter · audit   │         │ Care-coord API   │
│ FHIR R4 / OAuth │         │  PostgreSQL                            │         │ React clinician  │
└─────────────────┘         └───────────────────────────────────────┘         │ PostgreSQL/Azure │
                                                                               └──────────────────┘
```

---

## Outcomes — Demonstrated End-to-End on a Live Stack

| Metric                           | Result                                                   |
| -------------------------------- | -------------------------------------------------------- |
| Directions wired                 | Admissions in, vitals out                                |
| FHIR resources created & queried | 5 (Patient, Encounter, Condition, CarePlan, Observation) |
| Automated tests passing          | 14                                                       |
| Dropped or duplicated messages   | 0                                                        |

One admit message produces a fully cross-referenced clinical record — **Patient, Encounter, Condition, and CarePlan**. One vitals message writes four **LOINC-coded Observations** back, linked to that patient.

Reliability and HIPAA technical safeguards are built into the core. The engine was hardened against real-server failure modes a fake server hides.

---

## What It Unlocks — One Integration Layer, Many Clinical Products

- **Remote patient monitoring** — live vitals streaming from HaH devices into Epic
- **Care coordination & transitions** — automated admit/discharge notifications
- **Analytics & population health** — structured FHIR data feeds for dashboards
- **AI & agentic clinical workflows** — LLM agents grounded in real EHR context
- **Multi-EHR expansion** — architecture generalizes to Cerner, Meditech, and others

---

## Tech Stack

`HL7 v2` · `FHIR R4` · `Mirth Connect` · `SMART on FHIR` · `Python` · `FastAPI` · `PostgreSQL` · `Docker` · `HAPI FHIR` · `Prometheus` · `Azure` · `HIPAA / SOC 2-ready`

---

## Explore It

<div class="row mt-3">
  <div class="col-md-4 mb-3">
    <div class="card h-100">
      <div class="card-body">
        <h5 class="card-title">▶ Video Walkthrough</h5>
        <p class="card-text small text-muted">The full guided tour, with live HL7 and FHIR demos.</p>
        <a href="https://youtu.be/ApIp756c2C0" class="btn btn-sm btn-primary" target="_blank" rel="noopener">Watch on YouTube →</a>
      </div>
    </div>
  </div>
  <div class="col-md-4 mb-3">
    <div class="card h-100">
      <div class="card-body">
        <h5 class="card-title">◆ Source Code</h5>
        <p class="card-text small text-muted">The runnable engine, Mirth channel, tests, and Docker stack.</p>
        <a href="https://github.com/mohcinemadkour" class="btn btn-sm btn-outline-secondary" target="_blank" rel="noopener">Open the repo →</a>
      </div>
    </div>
  </div>
  <div class="col-md-4 mb-3">
    <div class="card h-100">
      <div class="card-body">
        <h5 class="card-title">▣ Presentation Deck</h5>
        <p class="card-text small text-muted">Architecture, data flows, and the path to a live Epic connection.</p>
        <a href="/assets/Epic_HoH_Integration.pptx" class="btn btn-sm btn-outline-secondary">Download slides →</a>
      </div>
    </div>
  </div>
</div>

---

## Share Feedback

I'm sharing this to get better — if you work in health IT, FHIR, clinical AI, or have shipped an Epic integration before, I'd value your candid take: what's missing, what you'd do differently, and where this would break at a real Epic go-live.

<a class="btn btn-sm btn-primary me-2" href="mailto:mohcine.madkour@gmail.com?subject=Feedback%20on%20your%20Epic%2FFHIR%20integration">Email me your thoughts</a>
<a class="btn btn-sm btn-outline-secondary me-2" href="https://www.youtube.com/watch?v=ApIp756c2C0" target="_blank" rel="noopener">Comment on the video</a>
<a class="btn btn-sm btn-outline-secondary" href="https://www.linkedin.com/in/mohcine-madkour-83a642b2" target="_blank" rel="noopener">Connect on LinkedIn</a>
