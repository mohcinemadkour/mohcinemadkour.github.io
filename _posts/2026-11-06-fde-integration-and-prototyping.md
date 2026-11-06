---
layout: post
title: "Bridging the Gap: Integration, Messy Data and Prototyping in Hours, the Hands-On Skills of a Forward Deployed Engineer"
date: 2026-11-06
description: "The technical core of the FDE role: connecting AI platforms to real customer systems, handling messy data and permissions, choosing a deployment shape, and going from first conversation to working prototype in hours."
tags: [ForwardDeployedEngineering, DataEngineering, Integration, Prototyping, AgenticAI, AICareers]
categories: writing
related_posts: true
toc:
  beginning: true
---

> **Part 4 of the FDE skills series.** The first three parts covered [product thinking](/writing/2026/fde-think-like-a-product-manager/), [business metrics](/writing/2026/fde-business-metrics-to-ai-metrics/) and [people skills](/writing/2026/fde-people-skills-techniques/). This part covers the hard-stack skill at the center of Aater Suleman's definition of the role: **bridging the gap** between what a platform provides and what a customer needs, and doing it fast enough to show a working prototype on the first call.

## 1. The gap is mostly integration

In his Dallas talk, Aater defined forward deployed engineering simply: a big vendor provides the core technology, a customer needs something, and there's a gap in between that somebody has to fill. In practice, most of that gap isn't the model. It's everything around it:

- Data spread across systems that were never designed to talk to each other
- Identity, permissions and network rules that block access for good reasons
- Legacy platforms with decades of customization
- Workflows that live in email, spreadsheets and people's heads

Aater gave a vivid example: before an AI project could touch one company's SAP environment, it took **two weeks of discovery just to map the custom objects**. He also described his own lesson from being acquired: moving a large company from one chat tool to another sounded simple until they discovered how many features and integrations the larger company relied on. Enterprise complexity is the reason FDEs exist. As he put it, you can't write a piece of software that walks into a 135-year-old company and finds its own way around.

---

## 2. Choosing a deployment shape

Before writing any integration code, decide _how_ the AI will live in the customer's world. Aater described three shapes, and each one implies very different integration work.

| Shape                 | What it looks like                                                             | Integration work                                         | Example from the talk                |
| --------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------- | ------------------------------------ |
| **AI employee**       | An AI persona with an email, chat account and desktop, trained like a new hire | Accounts, remote desktop, onboarding materials; few APIs | AI "contractors" for HVAC businesses |
| **Embedded agents**   | Agents built around the customer's own systems on a licensed platform          | APIs, connectors, data pipelines, identity, monitoring   | The classic FDE engagement           |
| **AI-native service** | Work goes in, results come back; the AI stays outside the company              | File exchange, secure portals, output formats            | Legal and accounting services        |

The lesson from the HVAC example is worth remembering: the company stopped asking small business owners for API keys, because that's where conversations stalled. They asked for what any contractor would get. **Choose the shape that creates the least friction for this customer, not the one that's most elegant for you.**

---

## 3. Integration patterns, from least to most invasive

A useful habit is to rank integration options by how much trust they require, and start at the bottom. This mirrors Aater's "earn the right to write."

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 330" role="img" aria-label="Integration ladder from least to most invasive: file exports, read-only API or connector, event stream or webhook, human-approved write, autonomous write" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">The integration ladder: start with the least trust required</text>
  <rect x="20" y="255" width="680" height="44" rx="8" fill="#c9cfdb"/>
  <text x="40" y="282" font-size="14" font-weight="700" fill="#1b2433">1. File exports and samples</text>
  <text x="680" y="282" font-size="12" text-anchor="end" fill="#1b2433">de-identified, one-off, zero system access</text>
  <rect x="60" y="205" width="640" height="44" rx="8" fill="#aebfd6"/>
  <text x="80" y="232" font-size="14" font-weight="700" fill="#1b2433">2. Read-only API or connector</text>
  <text x="680" y="232" font-size="12" text-anchor="end" fill="#1b2433">scoped service account, live but safe</text>
  <rect x="100" y="155" width="600" height="44" rx="8" fill="#8aa6c8"/>
  <text x="120" y="182" font-size="14" font-weight="700" fill="#1b2433">3. Event stream or webhook</text>
  <text x="680" y="182" font-size="12" text-anchor="end" fill="#1b2433">react in real time, still read-only</text>
  <rect x="140" y="105" width="560" height="44" rx="8" fill="#e9a274"/>
  <text x="160" y="132" font-size="14" font-weight="700" fill="#1b2433">4. Human-approved write</text>
  <text x="680" y="132" font-size="12" text-anchor="end" fill="#1b2433">AI drafts, a person commits</text>
  <rect x="180" y="55" width="520" height="44" rx="8" fill="#e07b39"/>
  <text x="200" y="82" font-size="14" font-weight="700" fill="#1b2433">5. Autonomous write</text>
  <text x="680" y="82" font-size="12" text-anchor="end" fill="#1b2433">proven tasks, monitored, reversible</text>
  <text x="20" y="320" font-size="12" fill="currentColor" opacity="0.7">Each step needs evidence from the one below it</text>
</svg>
</div>

Some practical rules for each step:

- **File exports** are the fastest way to start. Ask for a de-identified sample of real records on day one. It unblocks prototyping while access requests work through the system.
- **Read-only connectors** should use a dedicated, narrowly scoped service account, never a person's credentials. Log every call.
- **Events and webhooks** let the AI react to real work as it happens (a new claim, a new ticket) without changing anything.
- **Human-approved writes** are the workhorse of most enterprise AI: the AI prepares the update, a person reviews and commits it. Design the approval to fit inside the tool people already use.
- **Autonomous writes** come last, only for tasks with a proven track record, with monitoring, limits and a way to undo.

Standard protocols for connecting AI to tools, such as the Model Context Protocol (MCP), make many of these connections faster to build. They don't change the ladder. A connector that can write is still a write.

---

## 4. Messy data: what to expect and how to handle it

Aater named data quality as one of the main reasons AI pilots fail: train or ground a system on poor data and you get poor results. Every FDE engagement starts with a data reality check. These are the problems I meet most often, and how to handle each:

| Problem                        | What it looks like                                             | What to do                                                        |
| ------------------------------ | -------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Same thing, many names**     | A customer, part or patient appears differently across systems | Build a simple matching layer; ask the business which system wins |
| **Missing context**            | The key fact lives in free text, email or someone's memory     | Interview for it; extract it with an LLM, then validate a sample  |
| **Stale or inconsistent data** | Fields updated in one system but not another                   | Find the system of record for each field; timestamp everything    |
| **Undocumented meaning**       | Codes, flags and status values nobody can explain              | Build a data dictionary with the people who use the data          |
| **Bias and gaps**              | Some groups, sites or time periods barely represented          | Measure coverage before modeling; report it to stakeholders       |
| **Access lag**                 | Permissions take weeks                                         | Prototype on samples or synthetic data in the meantime            |

Two habits make a big difference:

1. **Profile before you promise.** Spend the first days measuring completeness, consistency and volume of the data you'll depend on. Share the results with the client. It sets realistic expectations and often reveals the real project.
2. **Keep a data dictionary from day one.** One shared page explaining every field, code and source. It becomes the most-used document in the engagement and a gift you leave behind.

---

## 5. Prototyping in hours

Asked how long a prototype should take, Aater said that in 2026 he wouldn't measure it in days at all, especially with newer models like Opus 5.5. His guidance: hours, maybe days, but definitely not weeks. And if it's taking weeks, the problem isn't your tools. **You've taken too big a bite.**

Here's a realistic same-day workflow:

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 230" role="img" aria-label="Timeline of a same-day prototype: hour 0 to 1 frame the problem, 1 to 2 data, 2 to 5 build three options, 5 to 6 test and polish the user flow, then demo" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">A same-day prototype (illustrative)</text>
  <line x1="40" y1="120" x2="690" y2="120" stroke="currentColor" opacity="0.3" stroke-width="2"/>
  <rect x="40" y="95" width="100" height="50" rx="6" fill="#c9cfdb"/>
  <text x="90" y="125" font-size="13" font-weight="700" text-anchor="middle" fill="#1b2433">Frame</text>
  <rect x="145" y="95" width="100" height="50" rx="6" fill="#aebfd6"/>
  <text x="195" y="125" font-size="13" font-weight="700" text-anchor="middle" fill="#1b2433">Data</text>
  <rect x="250" y="95" width="290" height="50" rx="6" fill="#e07b39"/>
  <text x="395" y="125" font-size="13" font-weight="700" text-anchor="middle" fill="#1b2433">Build three options</text>
  <rect x="545" y="95" width="100" height="50" rx="6" fill="#8aa6c8"/>
  <text x="595" y="125" font-size="13" font-weight="700" text-anchor="middle" fill="#1b2433">Test flow</text>
  <text x="670" y="125" font-size="20" fill="#e07b39">▶</text>
  <g font-size="11" fill="currentColor" opacity="0.8" text-anchor="middle">
    <text x="90" y="165">hour 0–1</text><text x="90" y="181">user, task, KPI</text>
    <text x="195" y="165">hour 1–2</text><text x="195" y="181">sample or synthetic</text>
    <text x="395" y="165">hours 2–5</text><text x="395" y="181">AI coding tools, real user flow</text>
    <text x="595" y="165">hour 5–6</text><text x="595" y="181">walk the path end to end</text>
    <text x="680" y="165">demo</text>
  </g>
</svg>
</div>

**Hour 0–1: frame it.** Write one sentence: _who_ uses it, for _which task_, and _which number_ should move. If you can't write it, go back to discovery.

**Hour 1–2: get data.** Use the de-identified sample, or generate synthetic data that mirrors the real structure. As Aater said in answer to an audience question, you don't need the customer's data for the first prototype.

**Hours 2–5: build three options.** Use AI coding tools (Aater mentioned Claude Code and hosting tools like Netlify) to build genuinely different approaches: maybe a chat assistant, a dashboard and an inbox-style triage queue. Focus on the user flow, not the infrastructure.

**Hour 5–6: walk the path.** Click through every step as the user would. It doesn't need to be debugged "to the nth degree," in Aater's words, but the flow must make sense.

What a good prototype has, and doesn't have:

| Include                                      | Skip for now                                |
| -------------------------------------------- | ------------------------------------------- |
| The real user flow, end to end               | Authentication, scaling, edge-case handling |
| Realistic data (sample or synthetic)         | Production infrastructure                   |
| The output in the format users actually need | Perfect accuracy                            |
| A visible note of what's simulated           | Anything that writes to real systems        |

---

## 6. From prototype to production: the honest gap

Aater's framing was clear: you build the application, but you don't take the prototype to production. Many projects die in the space between a demo that wowed everyone and a system that works every day. Being honest about that gap is part of the job. Before calling anything production-ready, check:

- **Integration:** real connectors, service accounts, error handling, retries
- **Data:** pipelines that refresh, with monitoring for missing or late data
- **Evaluation:** a golden test set and agreed quality thresholds (Part 5 covers this)
- **Security and compliance:** access reviews, logging, data handling approval (Part 6)
- **Operations:** who gets alerted when it breaks, and how to roll back
- **Adoption:** embedded in the users' tools, with a feedback loop

Tell the client which of these are done and which aren't, every time you demo. It keeps expectations honest and builds the trust you'll need for the next step.

---

## 7. How to build these skills

- **Practice integration on real systems.** Build a small project that pulls from two different sources (an API and a spreadsheet, say) and reconciles them. The reconciliation is the real lesson.
- **Get comfortable with one enterprise platform.** Salesforce, SAP, ServiceNow, Epic or Microsoft 365. Knowing how one of them models data and permissions makes the others easier to learn.
- **Time yourself.** Pick a real problem and build three prototype options in a single day. Do it monthly. Speed comes from repetition.
- **Learn to generate good synthetic data.** It unblocks you whenever access is slow, and it's essential in regulated industries.
- **Write the data dictionary**, even on personal projects. It trains you to ask "what does this field really mean?"

---

## Let's talk

What's the messiest integration you've had to make work? And how fast can you really go from conversation to prototype today? Tell me on [LinkedIn](https://www.linkedin.com/in/mohcine-madkour-83a642b2) or at [mohcine@evaltrust.cloud](mailto:mohcine@evaltrust.cloud).

---

### The FDE skills series

1. [Think like a product manager](/writing/2026/fde-think-like-a-product-manager/)
2. [From business KPI to F1 score](/writing/2026/fde-business-metrics-to-ai-metrics/)
3. [The people stack](/writing/2026/fde-people-skills-techniques/)
4. **Integration and rapid prototyping** (this article)
5. [Evaluation, guardrails and observability](/writing/2026/fde-evaluation-guardrails-observability/)
6. [Security, privacy and compliance](/writing/2026/fde-security-privacy-compliance/)
7. [Domain expertise and scoping](/writing/2026/fde-domain-expertise-and-scoping/)
8. [Communication and ownership](/writing/2026/fde-communication-and-ownership/)

### Sources and notes

- Aater Suleman, talk on forward deployed engineering, Dallas, November 5, 2026: the definition of the gap, the three deployment shapes, the HVAC and SAP examples, prototyping in hours, synthetic data, and not taking prototypes straight to production.
- The data problems table and the same-day timeline reflect the author's experience and are illustrative.
