---
layout: post
title: "Say It Clearly, Own the Result: Communication and Ownership for Forward Deployed Engineers"
date: 2026-11-06
description: "The final part of the FDE skills series: written updates, demos and executive briefings that build trust, documentation that outlasts you, and the 'startup CTO inside the customer' mindset of owning outcomes, pricing by results and growing one engagement into the next."
tags: [ForwardDeployedEngineering, Communication, Leadership, Consulting, AIStrategy, AICareers]
categories: writing
related_posts: true
toc:
  beginning: true
---

> **Part 8, the last in the FDE skills series.** Everything in the first seven parts depends on two final skills. **Communication**, because value nobody understands is value nobody pays for. And **ownership**, because, as Aater Suleman said at the end of his Dallas talk, it's not enough to make yourself available. **You have to own something.**

## Part A: Communication

### 1. Why communication is a core FDE skill

Aater's central observation was that the wall between engineers and the business has come down. FDEs no longer talk engineer to engineer; they talk to CFOs, nurses, operations managers and compliance officers. That means translating constantly: technical risk into business risk, model metrics into KPIs, uncertainty into decisions someone can make.

Most FDE communication falls into four formats. Each has a different audience and a different job.

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 260" role="img" aria-label="Four communication formats: weekly written update for the owner, demo for users and sponsors, executive brief for leadership, documentation for whoever comes next" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">Four formats, four jobs</text>
  <rect x="20" y="55" width="160" height="170" rx="12" fill="#c9cfdb"/>
  <text x="100" y="92" font-size="16" font-weight="700" text-anchor="middle" fill="#1b2433">Weekly update</text>
  <text x="100" y="120" font-size="12" text-anchor="middle" fill="#1b2433">for the owner</text>
  <text x="100" y="160" font-size="11" text-anchor="middle" fill="#1b2433">keeps everyone</text>
  <text x="100" y="176" font-size="11" text-anchor="middle" fill="#1b2433">aligned</text>
  <rect x="195" y="55" width="160" height="170" rx="12" fill="#8aa6c8"/>
  <text x="275" y="92" font-size="16" font-weight="700" text-anchor="middle" fill="#1b2433">Demo</text>
  <text x="275" y="120" font-size="12" text-anchor="middle" fill="#1b2433">for users, sponsors</text>
  <text x="275" y="160" font-size="11" text-anchor="middle" fill="#1b2433">makes value</text>
  <text x="275" y="176" font-size="11" text-anchor="middle" fill="#1b2433">visible</text>
  <rect x="370" y="55" width="160" height="170" rx="12" fill="#e9a274"/>
  <text x="450" y="92" font-size="16" font-weight="700" text-anchor="middle" fill="#1b2433">Executive brief</text>
  <text x="450" y="120" font-size="12" text-anchor="middle" fill="#1b2433">for leadership</text>
  <text x="450" y="160" font-size="11" text-anchor="middle" fill="#1b2433">gets a</text>
  <text x="450" y="176" font-size="11" text-anchor="middle" fill="#1b2433">decision</text>
  <rect x="545" y="55" width="160" height="170" rx="12" fill="#e07b39"/>
  <text x="625" y="92" font-size="16" font-weight="700" text-anchor="middle" fill="#1b2433">Documentation</text>
  <text x="625" y="120" font-size="12" text-anchor="middle" fill="#1b2433">for whoever is next</text>
  <text x="625" y="160" font-size="11" text-anchor="middle" fill="#1b2433">makes it</text>
  <text x="625" y="176" font-size="11" text-anchor="middle" fill="#1b2433">last</text>
</svg>
</div>

### 2. The weekly written update

A short written update, sent on the same day every week, is the single highest-value communication habit I know. It forces clarity, creates a record and means nobody is ever surprised. Keep it to five sections:

1. **The number.** Where the KPI and leading indicators stand against the baseline.
2. **What we did.** Three bullets at most, in business terms.
3. **What we learned.** Including anything that surprised or worried you.
4. **What we need.** Decisions, access or people, with a date.
5. **What's next.** The plan for the coming week.

If the news is bad, put it at the top, using the structure from [Part 3](/writing/2026/fde-people-skills-techniques/): what we saw, what we think it means, what we recommend.

### 3. Demos that tell a story

A demo is not a tour of features. It's a short story about a user and a problem. A structure that works:

- **The person:** "This is how Maria in billing handles a flagged claim today." Show the current pain, ideally with real numbers.
- **The change:** walk through the same task with the system, in the tool Maria already uses.
- **The evidence:** what shadow mode or the pilot showed, compared with the baseline.
- **The honest limits:** what isn't done yet and what you're still measuring.
- **The ask:** the decision you need from the room.

Then, as [Part 1](/writing/2026/fde-think-like-a-product-manager/) recommends, hand over the controls. A user clicking through it themselves is more persuasive than anything you say.

### 4. The executive brief

Executives have minutes, not hours. Lead with the conclusion, then support it. This is Barbara Minto's pyramid principle, sometimes called "bottom line up front":

| Section           | Example                                                                       |
| ----------------- | ----------------------------------------------------------------------------- |
| **Bottom line**   | "The pilot met its target; we recommend expanding to two more sites in Q1."   |
| **Why**           | Three supporting points: the KPI result, adoption, and risk controls in place |
| **What it costs** | Budget, people and access needed                                              |
| **Risks**         | The top two, with how they're managed                                         |
| **Decision**      | Exactly what you need them to approve, and by when                            |

One page. No technical terms the reader would need to look up. If a chart helps, use one, and make sure its title states the conclusion ("Denial rate fell after go-live"), not just the topic ("Denial rate").

### 5. Documentation that outlasts you

FDEs move between engagements. What stays behind determines whether the value lasts. Leave behind:

- **The data dictionary** ([Part 4](/writing/2026/fde-integration-and-prototyping/))
- **Architecture and data-flow diagrams**, kept current ([Part 6](/writing/2026/fde-security-privacy-compliance/))
- **The metric card and gate decisions** ([Parts 2](/writing/2026/fde-business-metrics-to-ai-metrics/) and [5](/writing/2026/fde-evaluation-guardrails-observability/))
- **A runbook:** what to do when it breaks, who to call, how to roll back
- **A decision log:** what was decided, why, and by whom

The test: could someone who has never met you run and improve the system next month? If not, the job isn't done.

---

## Part B: Ownership

### 6. The startup CTO inside the customer

Palantir, which popularized the forward deployed title, has compared the role's responsibilities to those of a startup CTO ([via St-Hakky](https://book.st-hakky.com/en/news/ai-deployment-engineer-salary-188k)). That comparison captures the mindset: you're responsible for the whole outcome, from understanding the problem to keeping the system running, not just for the code you wrote.

In practice, ownership means:

- **Caring about the result more than the plan.** If the plan stops working, you change it, like the Dintash team did when the KPI plateaued.
- **Raising problems you weren't asked about.** A data quality issue, a risky workflow, an unhappy user group.
- **Closing loops.** Every question answered, every promise kept or explicitly renegotiated.
- **Staying until it works.** Not until the contract milestone is technically met.

When asked what he looks for in junior FDEs, Aater mentioned that even a failed startup is strong evidence, because building a company teaches everything this role needs. A founder can't say "that's not my job."

### 7. Thinking about value and pricing: the outcome chain

Aater built his first company on a simple idea: never bill by the hour. In his talk he described an **outcome chain**, a ladder of ways to be paid, from weakest to strongest link to real value:

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 300" role="img" aria-label="Outcome chain staircase from availability to hours, project delivered, usage, internal KPI, and revenue or cost saved" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">The outcome chain: climb as high as you can prove</text>
  <rect x="20" y="230" width="105" height="45" rx="6" fill="#e3e6ea"/><text x="72" y="257" font-size="12" font-weight="700" text-anchor="middle" fill="#1b2433">Availability</text>
  <rect x="135" y="200" width="105" height="75" rx="6" fill="#c9cfdb"/><text x="187" y="227" font-size="12" font-weight="700" text-anchor="middle" fill="#1b2433">Hours</text>
  <rect x="250" y="170" width="105" height="105" rx="6" fill="#aebfd6"/><text x="302" y="197" font-size="12" font-weight="700" text-anchor="middle" fill="#1b2433">Project done</text>
  <rect x="365" y="140" width="105" height="135" rx="6" fill="#8aa6c8"/><text x="417" y="167" font-size="12" font-weight="700" text-anchor="middle" fill="#1b2433">Usage</text>
  <rect x="480" y="110" width="105" height="165" rx="6" fill="#e9a274"/><text x="532" y="137" font-size="12" font-weight="700" text-anchor="middle" fill="#1b2433">KPI moved</text>
  <rect x="595" y="80" width="105" height="195" rx="6" fill="#e07b39"/><text x="647" y="107" font-size="12" font-weight="700" text-anchor="middle" fill="#1b2433">Revenue or</text><text x="647" y="123" font-size="12" font-weight="700" text-anchor="middle" fill="#1b2433">cost saved</text>
  <text x="20" y="295" font-size="12" fill="currentColor" opacity="0.7">Each rung is a leading indicator of the next (from Aater Suleman's talk)</text>
</svg>
</div>

Even if you're an employee, not a founder, this way of thinking shapes how you describe your work. "I built a model" sits near the bottom. "Our system is used by 40 coders every day" is in the middle. "Denials fell and the team saved hours a week" is near the top. Learn to describe your work at the highest rung you can honestly support.

For founders, Aater's advice was practical: you don't have to jump straight to revenue sharing, which is hard to measure and negotiate. Start by charging for delivered projects or usage, and climb as your measurement improves. AWS, he noted, never asked for a revenue share; it charged for use.

### 8. Growing one engagement into the next

Ownership doesn't end at delivery. The best FDE engagements expand because the customer trusts you with more. Aater's portfolio examples followed a consistent arc: earn trust with a small, read-only first step, prove value, then take on the next workflow.

Habits that make expansion natural:

- **Celebrate bright spots publicly** inside the customer, so other teams ask for the same thing.
- **Keep a running list of next opportunities** you noticed during discovery, ranked by value and feasibility ([Part 7](/writing/2026/fde-domain-expertise-and-scoping/)).
- **Hold a quarterly value review** with the sponsor: what moved, what it was worth, what's next.
- **Protect the relationship.** Admitting a mistake early does more for long-term trust than a perfect first quarter.

### 9. Owning your own growth

Aater was candid that the scarcity value of FDEs is high right now, but the industry always normalizes. The way to stay valuable is to keep owning something real: a domain, a type of problem, a set of outcomes you're known for. Write about your work, speak at meetups, mentor people behind you. That's how a reputation compounds, and it's why I'm writing this series in public.

---

## The complete FDE skill map

Across all eight parts, here's the full picture:

| Area                             | Core skills                                                          | Article                                                          |
| -------------------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Product thinking**             | Problem selection, hypotheses, prioritization, prototypes            | [Part 1](/writing/2026/fde-think-like-a-product-manager/)        |
| **Business metrics**             | KPIs, baselines, cost-weighted AI metrics, adoption, kill criteria   | [Part 2](/writing/2026/fde-business-metrics-to-ai-metrics/)      |
| **People skills**                | Listening, discovery, facilitation, trust, change, community         | [Part 3](/writing/2026/fde-people-skills-techniques/)            |
| **Integration and prototyping**  | Deployment shapes, connectors, messy data, prototypes in hours       | [Part 4](/writing/2026/fde-integration-and-prototyping/)         |
| **Evaluation and observability** | Golden sets, shadow mode, guardrails, monitoring, gates              | [Part 5](/writing/2026/fde-evaluation-guardrails-observability/) |
| **Security and compliance**      | Least privilege, data handling, AI threats, frameworks, reviews      | [Part 6](/writing/2026/fde-security-privacy-compliance/)         |
| **Domain and scoping**           | Domain sprints, expert partnerships, first slices, saying no         | [Part 7](/writing/2026/fde-domain-expertise-and-scoping/)        |
| **Communication and ownership**  | Updates, demos, executive briefs, documentation, outcomes, expansion | Part 8 (this article)                                            |

Nobody is strong in all eight on day one. That's exactly why Aater expects the role to evolve into pods. Pick the two areas where you're weakest, and start practicing this week.

---

## Let's talk

Thank you for reading the series. Which of the eight areas is your strongest, and which is your biggest gap? And thank you again to Aater Suleman for the talk that started it. Tell me on [LinkedIn](https://www.linkedin.com/in/mohcine-madkour-83a642b2) or at [mohcine@evaltrust.cloud](mailto:mohcine@evaltrust.cloud).

---

### The FDE skills series

1. [Think like a product manager](/writing/2026/fde-think-like-a-product-manager/)
2. [From business KPI to F1 score](/writing/2026/fde-business-metrics-to-ai-metrics/)
3. [The people stack](/writing/2026/fde-people-skills-techniques/)
4. [Integration and rapid prototyping](/writing/2026/fde-integration-and-prototyping/)
5. [Evaluation, guardrails and observability](/writing/2026/fde-evaluation-guardrails-observability/)
6. [Security, privacy and compliance](/writing/2026/fde-security-privacy-compliance/)
7. [Domain expertise and scoping](/writing/2026/fde-domain-expertise-and-scoping/)
8. **Communication and ownership** (this article)

### Sources and notes

- Aater Suleman, talk on forward deployed engineering, Dallas, November 5, 2026: the end of the wall between engineers and business, never billing by the hour, the outcome chain, AWS charging for use, failed startups as hiring evidence, the Dintash case, transient scarcity, and "you have to own something."
- Palantir's comparison of the role to a startup CTO, as reported by [St-Hakky](https://book.st-hakky.com/en/news/ai-deployment-engineer-salary-188k).
- Barbara Minto, _The Pyramid Principle_, on leading with the conclusion.
- The example billing scenario in the demo section is illustrative.
