---
layout: post
title: "Proof, Not Promises: Evaluation, Guardrails and Observability for Forward Deployed Engineers"
date: 2026-11-06
description: "The technical side of 'earning the right to write': golden test sets, shadow mode, quality gates, guardrails and production monitoring, and how an FDE uses them to turn a customer's 'no' into a 'yes'."
tags: [ForwardDeployedEngineering, LLM-Evaluation, Observability, Guardrails, AgenticAI, AIGovernance]
categories: writing
related_posts: true
toc:
  beginning: true
---

> **Part 5 of the FDE skills series.** Aater Suleman's third pattern, **earn the right to write**, has a people side, covered in [Part 3](/writing/2026/fde-people-skills-techniques/), and a technical side, covered here. The people side gets you a fair hearing. The technical side gives you the evidence. This is the area I work in every day through [EvalTrust](https://evaltrust.cloud), so this article is the most personal in the series.

## 1. Why evaluation is an FDE skill, not a specialist's job

In his talk, Aater listed **poor risk controls** among the main reasons AI pilots fail, and pointed out that an agent going wrong in production can cost millions. His answer to the access problem was not to argue harder. It was to **show proof**: run the system read-only, show what it _would_ have done next to what people actually did, and let the evidence make the case.

That proof doesn't produce itself. Someone has to design the tests, define what "good" means with the customer, run the comparisons, watch the system in production and explain the results in business terms. On an FDE team, that someone is often you.

There's also a simple reason it matters more for agents than for older software: **agents fail quietly.** A traditional application that breaks throws an error. An agent that breaks usually returns a fluent, confident, wrong answer, and no alert fires. I wrote about this in detail in my [leader's guide to agent readiness](/writing/2026/ai-agent-readiness-leaders-guide/).

---

## 2. The four controls: observe, evaluate, guard, gate

I organize this work into four controls. Each answers a different question a customer will ask.

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 260" role="img" aria-label="Four controls in a row: observe (what did it do?), evaluate (was it right?), guard (can it do harm?), gate (is it ready for the next step?)" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">Four controls that earn the right to write</text>
  <rect x="20" y="55" width="160" height="170" rx="12" fill="#c9cfdb"/>
  <text x="100" y="95" font-size="18" font-weight="700" text-anchor="middle" fill="#1b2433">Observe</text>
  <text x="100" y="125" font-size="12" text-anchor="middle" fill="#1b2433">"What did it do?"</text>
  <text x="100" y="160" font-size="11" text-anchor="middle" fill="#1b2433">traces, tool calls,</text>
  <text x="100" y="176" font-size="11" text-anchor="middle" fill="#1b2433">cost, latency</text>
  <rect x="195" y="55" width="160" height="170" rx="12" fill="#8aa6c8"/>
  <text x="275" y="95" font-size="18" font-weight="700" text-anchor="middle" fill="#1b2433">Evaluate</text>
  <text x="275" y="125" font-size="12" text-anchor="middle" fill="#1b2433">"Was it right?"</text>
  <text x="275" y="160" font-size="11" text-anchor="middle" fill="#1b2433">golden sets, judges,</text>
  <text x="275" y="176" font-size="11" text-anchor="middle" fill="#1b2433">human review</text>
  <rect x="370" y="55" width="160" height="170" rx="12" fill="#e9a274"/>
  <text x="450" y="95" font-size="18" font-weight="700" text-anchor="middle" fill="#1b2433">Guard</text>
  <text x="450" y="125" font-size="12" text-anchor="middle" fill="#1b2433">"Can it do harm?"</text>
  <text x="450" y="160" font-size="11" text-anchor="middle" fill="#1b2433">input and output checks,</text>
  <text x="450" y="176" font-size="11" text-anchor="middle" fill="#1b2433">limits, approvals</text>
  <rect x="545" y="55" width="160" height="170" rx="12" fill="#e07b39"/>
  <text x="625" y="95" font-size="18" font-weight="700" text-anchor="middle" fill="#1b2433">Gate</text>
  <text x="625" y="125" font-size="12" text-anchor="middle" fill="#1b2433">"Is it ready?"</text>
  <text x="625" y="160" font-size="11" text-anchor="middle" fill="#1b2433">agreed thresholds</text>
  <text x="625" y="176" font-size="11" text-anchor="middle" fill="#1b2433">before each step</text>
  <text x="20" y="250" font-size="12" fill="currentColor" opacity="0.7">Most teams have the first control. Far fewer have all four.</text>
</svg>
</div>

---

## 3. Evaluate: building a golden set with the customer

Every evaluation starts with ground truth: a set of real cases where the right answer is known and agreed. This is the **golden set**, and building it is as much a people task as a technical one.

**How to build one in an engagement:**

1. **Sample real cases.** A few hundred, drawn from actual historical work, deliberately including the hard and unusual ones, not just the easy majority.
2. **Have the customer's experts label them.** What should the system have flagged, answered or done? Use their definitions of "correct," not yours.
3. **Measure expert agreement.** Have two experts label the same subset. If they only agree 85% of the time, a system that matches them 85% of the time is performing at human level, and a 99% target is unrealistic.
4. **Write down the edge cases.** Every disagreement is a policy question the business needs to answer. Bring them to the owner.
5. **Version it.** The golden set becomes the reference for every model change, prompt change and vendor switch. Keep it under version control like code.

**What to measure** depends on the system. A quick map:

| System type                | Core metrics                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------------ |
| Classification or flagging | Precision, recall, cost-weighted value at the chosen threshold                             |
| RAG and question answering | Retrieval recall, answer correctness, groundedness (faithfulness)                          |
| Drafting and summarization | Factual accuracy, completeness, human acceptance and edit rate                             |
| Agents taking actions      | Task success, tool-call accuracy, escalation correctness, safety violations, cost per task |

[Part 2](/writing/2026/fde-business-metrics-to-ai-metrics/) explains how to connect each of these to the business KPI, and why the threshold with the best F1 score is often not the best business decision. For a deeper technical treatment, see my [practitioner's guide to evaluating agentic AI](/writing/2026/agentic-ai-evaluation-guide/).

**A note on LLM judges.** Using a language model to grade outputs scales evaluation enormously, but a judge is itself a model that can be wrong. Calibrate it against expert labels on part of the golden set before you trust it, and keep humans reviewing a sample over time.

---

## 4. Shadow mode: the safest experiment you'll ever run

Shadow mode is Aater's "show them A versus B" made concrete. The AI runs on real, live work, but its outputs go only to a log, never to the real system. You then compare what it would have done with what people actually did.

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 270" role="img" aria-label="Shadow mode diagram: real work goes to both the human process, which updates the system of record, and the AI, whose output goes only to a comparison log. The comparison produces an evidence report" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">Shadow mode: same input, two paths, one comparison</text>
  <rect x="20" y="110" width="130" height="56" rx="10" fill="#c9cfdb"/>
  <text x="85" y="143" font-size="14" font-weight="700" text-anchor="middle" fill="#1b2433">Real work</text>
  <line x1="150" y1="128" x2="220" y2="85" stroke="currentColor" opacity="0.5" stroke-width="2"/>
  <line x1="150" y1="148" x2="220" y2="190" stroke="currentColor" opacity="0.5" stroke-width="2"/>
  <rect x="220" y="55" width="170" height="56" rx="10" fill="#8aa6c8"/>
  <text x="305" y="88" font-size="14" font-weight="700" text-anchor="middle" fill="#1b2433">Human process</text>
  <rect x="220" y="165" width="170" height="56" rx="10" fill="#e9a274"/>
  <text x="305" y="198" font-size="14" font-weight="700" text-anchor="middle" fill="#1b2433">AI (shadow)</text>
  <line x1="390" y1="83" x2="460" y2="83" stroke="currentColor" opacity="0.5" stroke-width="2"/>
  <rect x="460" y="55" width="160" height="56" rx="10" fill="none" stroke="#8aa6c8" stroke-width="2"/>
  <text x="540" y="88" font-size="13" text-anchor="middle" fill="currentColor">System of record</text>
  <line x1="390" y1="193" x2="460" y2="193" stroke="currentColor" opacity="0.5" stroke-width="2" stroke-dasharray="5 4"/>
  <rect x="460" y="165" width="160" height="56" rx="10" fill="none" stroke="#e07b39" stroke-width="2"/>
  <text x="540" y="198" font-size="13" text-anchor="middle" fill="currentColor">Comparison log only</text>
  <line x1="540" y1="111" x2="540" y2="165" stroke="#e07b39" stroke-width="2"/>
  <text x="640" y="143" font-size="13" font-weight="700" fill="#e07b39">Evidence</text>
  <text x="640" y="160" font-size="13" font-weight="700" fill="#e07b39">report</text>
</svg>
</div>

What a good shadow-mode report shows the customer:

- **Agreement rate** with human decisions, broken down by case type
- **Where the AI was right and the human wasn't**, and the reverse; both matter
- **Severity of disagreements:** a wrong low-risk suggestion isn't the same as a wrong high-risk one
- **Safety and policy violations**, which should be zero
- **Cost and speed** compared with the current process

Run it long enough to cover normal variation: busy weeks, quiet weeks, month-end. Then let the business owner decide whether the evidence justifies the next step.

---

## 5. Guard: designing guardrails that fit the risk

Guardrails are the controls that stop the system from doing harm even when it's wrong. Match them to the risk of each action.

| Layer              | Examples                                                                                |
| ------------------ | --------------------------------------------------------------------------------------- |
| **Input checks**   | Detect prompt injection, out-of-scope requests and sensitive data entering the system   |
| **Output checks**  | Groundedness checks, format and policy validation, blocking sensitive data from leaving |
| **Action limits**  | Allowed tools only, value caps, rate limits, read-only by default                       |
| **Human approval** | Required for high-impact or irreversible actions, with a clear review screen            |
| **Escalation**     | Hand off to a person when confidence is low or the case is unusual                      |
| **Reversibility**  | Every write can be traced and undone                                                    |

A practical rule: **the more irreversible the action, the more layers it needs.** Drafting an email needs light checks. Changing a patient record, issuing a payment or modifying production infrastructure needs approval, limits and a full audit trail.

---

## 6. Observe: monitoring in production

Passing an evaluation once proves nothing about next month. Data changes, users change, vendors update models, and quality drifts without anyone noticing. Production monitoring for AI should track three kinds of signal:

1. **System health:** errors, latency, cost per task, tool failures. The traditional monitoring most teams already have.
2. **Quality:** ongoing evaluation on a sample of live traffic, user acceptance and edit rates, escalation rates, groundedness scores.
3. **Business outcome:** the KPI from the metric card, compared with the baseline.

Instrument agents with traces that capture every step (model calls, retrieved documents, tool calls and their results) so that when something goes wrong you can see exactly why. Open standards like OpenTelemetry make this portable across tools; I walked through a working setup in my [article on agent observability with OpenTelemetry](/writing/2026/agent-observability-opentelemetry/).

Set alerts on quality, not just uptime. "Evaluation pass rate dropped below the agreed threshold" should page someone just like "service is down" does.

---

## 7. Gate: thresholds agreed before each step

A gate is a decision point with criteria agreed in advance. Gates connect all of the above to the right-to-write ladder from Aater's talk.

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 230" role="img" aria-label="Gates between steps: read-only to shadow, shadow to human in the loop, human in the loop to autonomous. Each gate lists example criteria" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">Gates on the right-to-write ladder (example criteria)</text>
  <rect x="20" y="60" width="140" height="50" rx="8" fill="#c9cfdb"/><text x="90" y="90" font-size="14" font-weight="700" text-anchor="middle" fill="#1b2433">Read-only</text>
  <rect x="200" y="60" width="140" height="50" rx="8" fill="#8aa6c8"/><text x="270" y="90" font-size="14" font-weight="700" text-anchor="middle" fill="#1b2433">Shadow</text>
  <rect x="380" y="60" width="140" height="50" rx="8" fill="#e9a274"/><text x="450" y="90" font-size="14" font-weight="700" text-anchor="middle" fill="#1b2433">Human in loop</text>
  <rect x="560" y="60" width="140" height="50" rx="8" fill="#e07b39"/><text x="630" y="90" font-size="14" font-weight="700" text-anchor="middle" fill="#1b2433">Autonomous</text>
  <g font-size="22" fill="#e07b39" text-anchor="middle"><text x="180" y="93">▶</text><text x="360" y="93">▶</text><text x="540" y="93">▶</text></g>
  <g font-size="11" fill="currentColor" text-anchor="middle">
    <text x="180" y="140">Golden-set score</text><text x="180" y="156">meets target</text>
    <text x="360" y="140">Agreement with experts,</text><text x="360" y="156">zero safety violations</text>
    <text x="540" y="140">Acceptance rate high,</text><text x="540" y="156">overrides understood</text>
  </g>
  <text x="20" y="205" font-size="12" fill="currentColor" opacity="0.7">The business owner, not the engineer, signs off on each gate.</text>
</svg>
</div>

The most important word in this section is **before**. If you set the threshold after seeing the results, you'll be tempted to move it. Agree on it with the owner, write it down, and treat it like a contract. That discipline is what makes a customer believe your next report.

Gates also run in the delivery pipeline. Every change to a prompt, model or tool should rerun the golden set automatically and block the release if quality drops, just as failing unit tests block a code deploy.

---

## 8. How to build these skills

- **Build a golden set for something you already made.** Even 100 hand-labeled cases will change how you think about quality.
- **Run a shadow comparison.** Take any process with historical decisions, run a model against it and write a one-page evidence report as if for a customer.
- **Add traces to an agent** and practice debugging a wrong answer from the trace alone.
- **Write a gate document:** the criteria, who signs off, and what happens if the system fails it.
- **Read the frameworks** customers will ask about, such as the NIST AI Risk Management Framework, so you can map your evidence to their language.

---

## Let's talk

How do you prove an AI system is ready to act on real data? What evidence has worked for you with skeptical stakeholders? Tell me on [LinkedIn](https://www.linkedin.com/in/mohcine-madkour-83a642b2) or at [mohcine@evaltrust.cloud](mailto:mohcine@evaltrust.cloud).

---

### The FDE skills series

1. [Think like a product manager](/writing/2026/fde-think-like-a-product-manager/)
2. [From business KPI to F1 score](/writing/2026/fde-business-metrics-to-ai-metrics/)
3. [The people stack](/writing/2026/fde-people-skills-techniques/)
4. [Integration and rapid prototyping](/writing/2026/fde-integration-and-prototyping/)
5. **Evaluation, guardrails and observability** (this article)
6. [Security, privacy and compliance](/writing/2026/fde-security-privacy-compliance/)
7. [Domain expertise and scoping](/writing/2026/fde-domain-expertise-and-scoping/)
8. [Communication and ownership](/writing/2026/fde-communication-and-ownership/)

### Sources and notes

- Aater Suleman, talk on forward deployed engineering, Dallas, November 5, 2026: poor risk controls as a cause of failed pilots, "earn the right to write," and showing A-versus-B evidence instead of arguing for access.
- Example gate criteria are illustrative; real thresholds must be agreed with each customer.
