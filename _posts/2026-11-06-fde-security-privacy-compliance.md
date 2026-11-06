---
layout: post
title: "Inside the Fence: Security, Privacy and Compliance Skills for Forward Deployed Engineers"
date: 2026-11-06
description: "How FDEs work inside regulated customers: getting through security reviews, handling sensitive data, designing least-privilege AI systems, defending against AI-specific threats, and speaking the language of HIPAA, NIST AI RMF and new state AI laws."
tags: [ForwardDeployedEngineering, AISecurity, Privacy, Compliance, HealthcareAI, AIGovernance]
categories: writing
related_posts: true
toc:
  beginning: true
---

> **Part 6 of the FDE skills series.** FDEs work inside the customer's walls. In healthcare, finance, pharma and defense, those walls are there for good reasons. This part covers the security, privacy and compliance skills that let you work inside them without slowing everything down. _Nothing here is legal advice; always confirm obligations with the customer's counsel and compliance team._

## 1. Why this is part of the FDE job

Aater Suleman made the point in his Dallas talk that the FDE role grows out of a simple fact: to deliver value, someone has to embed with the customer. In regulated industries, embedding means handling patient records, financial data or controlled information, working under the customer's security policies, and convincing people whose job is to say no.

Many promising AI projects don't die on accuracy. They die in the security review. An FDE who understands security and compliance can turn a months-long approval into weeks, because they design the system to pass review from the start instead of retrofitting controls at the end.

The good news: most of what reviewers want follows a small set of principles. Learn them once and you'll recognize them in every framework.

---

## 2. Five principles that satisfy most reviewers

| Principle                | What it means for an AI system                                                          |
| ------------------------ | --------------------------------------------------------------------------------------- |
| **Least privilege**      | The AI gets only the access it needs for this task, through a dedicated, scoped account |
| **Data minimization**    | Use the least sensitive data that works: de-identified, sampled, or synthetic first     |
| **Know where data goes** | Document every place data travels, including model providers and logs                   |
| **Traceability**         | Log every model call, tool call and data access; keep an audit trail                    |
| **Human accountability** | A named person approves high-impact actions and owns each decision                      |

These map directly to Aater's "earn the right to write." Starting read-only, with minimal data, under a scoped account, is not only good engineering. It's the fastest path through review.

---

## 3. Handling sensitive data

### Know your data classes

Before touching any data, ask the customer how it's classified. Typical classes include public, internal, confidential, and regulated data such as protected health information (PHI), payment card data or personal data covered by privacy laws. Each class comes with rules about where it can be stored, who can see it and whether it can leave the customer's environment.

### Healthcare: the HIPAA basics every FDE should know

If you work with US healthcare organizations, a few HIPAA concepts come up constantly:

- **Business Associate Agreement (BAA).** A vendor that handles PHI on behalf of a covered entity generally needs a BAA in place before touching the data. That includes your company, and often your cloud and model providers too.
- **Minimum necessary.** Use and disclose only the minimum PHI needed for the purpose. Design prompts, retrieval and logs with that in mind.
- **De-identification.** HIPAA describes two routes: the Safe Harbor method, which removes 18 specified types of identifiers, and Expert Determination by a qualified expert. De-identified data is far easier to work with during prototyping.

### Practical data-handling rules

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 280" role="img" aria-label="Data access ladder from least to most sensitive: synthetic data, de-identified sample, limited live read-only, full live data with approval" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">Use the least sensitive data that answers the question</text>
  <rect x="20" y="210" width="680" height="44" rx="8" fill="#c9cfdb"/>
  <text x="40" y="237" font-size="14" font-weight="700" fill="#1b2433">Synthetic data</text>
  <text x="680" y="237" font-size="12" text-anchor="end" fill="#1b2433">prototypes, demos, testing</text>
  <rect x="80" y="160" width="620" height="44" rx="8" fill="#aebfd6"/>
  <text x="100" y="187" font-size="14" font-weight="700" fill="#1b2433">De-identified sample</text>
  <text x="680" y="187" font-size="12" text-anchor="end" fill="#1b2433">realistic patterns, low risk</text>
  <rect x="140" y="110" width="560" height="44" rx="8" fill="#e9a274"/>
  <text x="160" y="137" font-size="14" font-weight="700" fill="#1b2433">Limited live data, read-only</text>
  <text x="680" y="137" font-size="12" text-anchor="end" fill="#1b2433">shadow mode, scoped fields</text>
  <rect x="200" y="60" width="500" height="44" rx="8" fill="#e07b39"/>
  <text x="220" y="87" font-size="14" font-weight="700" fill="#1b2433">Full live data</text>
  <text x="680" y="87" font-size="12" text-anchor="end" fill="#1b2433">approved, logged, contracted</text>
</svg>
</div>

- **Never paste real customer data into a personal or consumer AI tool.** Use only environments and providers approved by the customer.
- **Check what the model provider keeps.** Ask about data retention, training use and where processing happens. Many enterprise offerings support zero-data-retention options; confirm the terms in writing.
- **Treat logs as sensitive data.** Prompts, retrieved documents and outputs often contain the very information you were trying to protect. Apply the same retention and access rules.
- **Mask by default.** Strip or tokenize identifiers before they reach the model whenever the task allows.
- **Keep data where it lives when you can.** Deploying inside the customer's cloud account or network often removes whole categories of review questions.

---

## 4. AI-specific threats

AI systems add new ways to fail that traditional security reviews may not cover. The OWASP Top 10 for Large Language Model Applications is a good starting list; prompt injection sits at the top of it. The threats I see most often in agent projects:

| Threat                        | What happens                                                           | Defense                                                                                       |
| ----------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Prompt injection**          | Instructions hidden in an email, document or web page hijack the agent | Treat all retrieved content as untrusted; limit tools; require approval for sensitive actions |
| **Sensitive data disclosure** | The model reveals data the user shouldn't see                          | Enforce the user's permissions at retrieval time; output filtering                            |
| **Excessive agency**          | The agent has more tools or permissions than the task needs            | Least privilege per task; read-only by default; value and rate limits                         |
| **Insecure output handling**  | Model output is executed or inserted into systems without checks       | Validate and sanitize outputs like any untrusted input                                        |
| **Supply-chain risk**         | Third-party models, plugins or connectors introduce vulnerabilities    | Approved component list; version pinning; vendor review                                       |

A key design rule for retrieval systems: **the AI should never see more than the person it's acting for is allowed to see.** Enforce document permissions when you retrieve, not after the model has already read everything.

---

## 5. Speaking the compliance language

You don't need to be a lawyer, but you need to recognize the frameworks your customers use and map your evidence to them.

- **NIST AI Risk Management Framework.** A voluntary US framework organized around four functions: Govern, Map, Measure and Manage. The evaluation, monitoring and gating work in [Part 5](/writing/2026/fde-evaluation-guardrails-observability/) maps naturally to Measure and Manage.
- **Texas Responsible AI Governance Act (TRAIGA).** Took effect January 1, 2026, enforced by the Texas Attorney General, and points to the NIST AI RMF as a recognized route to good-faith compliance. Health care providers must also disclose AI use to patients. ([McDonald Hopkins](https://www.mcdonaldhopkins.com/insights/news/texas-enacts-broad-artificial-intelligence-regulations); [Spencer Fane](https://www.spencerfane.com/insight/texas-enacts-comprehensive-ai-governance-law-with-specific-requirements-for-health-care-service-providers-are-you-ready-for-traiga/))
- **Sector rules.** HIPAA in healthcare; financial regulators' model risk management expectations in banking; and, for customers operating in Europe, the EU AI Act's risk-based obligations.
- **Security attestations.** Customers will often ask for SOC 2 reports or ISO 27001 certification from vendors, and for your system to fit their existing controls.

A practical habit: keep a **control map**, a simple table linking each requirement the customer cares about to the specific control and evidence in your system. Reviewers love it, and it makes the next review much faster.

---

## 6. Getting through the security review

The security review is a negotiation with people who carry the risk if something goes wrong. Treat them as design partners, as described in [Part 3](/writing/2026/fde-people-skills-techniques/). A sequence that works:

1. **Engage early.** Ask the security and compliance teams what they'll need before you build, not after.
2. **Send an architecture and data-flow diagram.** Show every system, every data movement and every external service, including the model provider.
3. **Answer the standard questions up front:** where data is stored and processed, who can access it, how it's encrypted, what is logged and for how long, how access is revoked, what happens in an incident.
4. **Propose a phased scope.** "Phase 1 uses de-identified data, read-only, inside your cloud account" is far easier to approve than the full vision.
5. **Show the controls working.** A short demo of the audit log, permission enforcement and approval step does more than ten pages of policy.
6. **Keep a decision log** of what was approved, with which conditions, by whom.

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 200" role="img" aria-label="Comparison: retrofitting controls at the end leads to long review cycles; designing for review from the start leads to shorter, phased approvals" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">Retrofit vs designed-in (illustrative)</text>
  <text x="20" y="80" font-size="14" fill="currentColor">Retrofit</text>
  <rect x="150" y="62" width="200" height="28" fill="#8aa6c8"/><text x="250" y="81" font-size="12" text-anchor="middle" fill="#1b2433">Build</text>
  <rect x="350" y="62" width="340" height="28" fill="#c9cfdb"/><text x="520" y="81" font-size="12" text-anchor="middle" fill="#1b2433">Review, rework, review again</text>
  <text x="20" y="140" font-size="14" fill="currentColor">Designed-in</text>
  <rect x="150" y="122" width="70" height="28" fill="#e07b39"/><text x="185" y="141" font-size="12" text-anchor="middle" fill="#1b2433">Engage</text>
  <rect x="220" y="122" width="200" height="28" fill="#8aa6c8"/><text x="320" y="141" font-size="12" text-anchor="middle" fill="#1b2433">Build with controls</text>
  <rect x="420" y="122" width="90" height="28" fill="#c9cfdb"/><text x="465" y="141" font-size="12" text-anchor="middle" fill="#1b2433">Review</text>
  <text x="525" y="141" font-size="13" font-weight="700" fill="#e07b39">Live sooner</text>
  <text x="20" y="185" font-size="12" fill="currentColor" opacity="0.7">The shape is typical; actual timelines depend on the organization.</text>
</svg>
</div>

---

## 7. How to build these skills

- **Draw data-flow diagrams for your own projects.** Every arrow is a question a reviewer will ask.
- **Read one framework end to end.** The NIST AI RMF is free and readable, and it gives you the vocabulary customers use.
- **Learn the basics of your target industry's rules.** For healthcare, HIPAA's privacy and security rules; for finance, model risk management.
- **Practice threat modeling on an agent:** list its tools, data and permissions, then ask how each could be misused.
- **Fill out a real security questionnaire** for a personal project. It's tedious, and it's exactly what customers will send you.

---

## Let's talk

What's the hardest security or compliance review you've been through with an AI project, and what finally got it approved? Tell me on [LinkedIn](https://www.linkedin.com/in/mohcine-madkour-83a642b2) or at [mohcine@evaltrust.cloud](mailto:mohcine@evaltrust.cloud).

---

### The FDE skills series

1. [Think like a product manager](/writing/2026/fde-think-like-a-product-manager/)
2. [From business KPI to F1 score](/writing/2026/fde-business-metrics-to-ai-metrics/)
3. [The people stack](/writing/2026/fde-people-skills-techniques/)
4. [Integration and rapid prototyping](/writing/2026/fde-integration-and-prototyping/)
5. [Evaluation, guardrails and observability](/writing/2026/fde-evaluation-guardrails-observability/)
6. **Security, privacy and compliance** (this article)
7. [Domain expertise and scoping](/writing/2026/fde-domain-expertise-and-scoping/)
8. [Communication and ownership](/writing/2026/fde-communication-and-ownership/)

### Sources and notes

- Aater Suleman, talk on forward deployed engineering, Dallas, November 5, 2026.
- TRAIGA details from [McDonald Hopkins](https://www.mcdonaldhopkins.com/insights/news/texas-enacts-broad-artificial-intelligence-regulations) and [Spencer Fane](https://www.spencerfane.com/insight/texas-enacts-comprehensive-ai-governance-law-with-specific-requirements-for-health-care-service-providers-are-you-ready-for-traiga/).
- HIPAA concepts (business associate agreements, minimum necessary, Safe Harbor and Expert Determination de-identification) are summarized from HHS guidance; NIST AI RMF and the OWASP Top 10 for LLM Applications are referenced at a general level.
- This article is general information, not legal advice.
