---
layout: post
title: "From Business KPI to F1 Score: How Forward Deployed Engineers Choose the Metrics That Matter"
date: 2026-11-05
description: "The skill that separates great FDEs: turning a vague business goal into a KPI, collecting the right data from the client, staying realistic, and translating it all into precision, recall, F1 and agentic AI metrics. With a worked example and charts."
tags: [ForwardDeployedEngineering, AIMetrics, LLM-Evaluation, AgenticAI, ProductManagement, ChangeManagement]
categories: writing
related_posts: true
toc:
  beginning: true
---

> **The short version.** A forward deployed engineer is not paid to ship a model. They are paid to move a number the business cares about. That means two things most technical training skips: **change management** (getting people to actually use the system) and **outcome thinking** (measuring whether it worked, and dropping it if it didn't). This article explains how to pick a business metric, collect the data to measure it, stay realistic, and translate it into the AI metrics you optimize every day: precision, recall, F1 and the newer metrics for agentic systems. It builds on my [previous article on FDEs and product thinking](/writing/2026/fde-think-like-a-product-manager/), inspired by Aater Suleman's Dallas talk.

## 1. The metric mindset

Here is the most common failure I see in AI projects, and the one Aater Suleman described in his talk: a team builds a technically good system, the dashboard shows rising usage, and the business number doesn't move. In the Dintash case he shared, more AI usage left the cost metric flat at 15% until the team went back and interviewed about 50 business users. Only then did the KPI climb to 40%.

The lesson is simple and uncomfortable: **usage is not value, and accuracy is not value either.** A model with a 0.92 F1 score can still be worthless if it optimizes the wrong thing, or if nobody trusts it enough to change how they work.

Great FDEs think in three layers at once:

1. **The business outcome.** What changes on the P&L, the risk register or the customer experience?
2. **The human behavior.** What do people need to do differently for that outcome to happen?
3. **The system behavior.** What must the AI do, and how well, for people to change their behavior?

Most engineers start at layer 3. FDEs start at layer 1 and work down. Goodhart's law is the warning label on this whole topic: _when a measure becomes a target, it ceases to be a good measure._ Your job is to choose measures that stay honest.

---

## 2. Change management is a metrics problem

Aater's advice to "meet people where they work" sounds like a soft skill. It's actually measurable. If you force a new platform on people, the adoption numbers will tell you so long before the KPI does.

Think of adoption as a funnel. Every stage is a leading indicator of the business outcome at the bottom:

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 330" role="img" aria-label="Adoption funnel: exposed, tried, used repeatedly, relied on, KPI moved. Each stage narrower than the last" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">The adoption funnel: leading indicators before the KPI moves</text>
  <polygon points="60,50 660,50 630,100 90,100" fill="#c9cfdb"/>
  <text x="360" y="81" font-size="14" font-weight="700" text-anchor="middle" fill="#1b2433">Exposed: users who can access it</text>
  <polygon points="95,105 625,105 595,155 125,155" fill="#aebfd6"/>
  <text x="360" y="136" font-size="14" font-weight="700" text-anchor="middle" fill="#1b2433">Tried: used it at least once</text>
  <polygon points="130,160 590,160 560,210 160,210" fill="#8aa6c8"/>
  <text x="360" y="191" font-size="14" font-weight="700" text-anchor="middle" fill="#1b2433">Repeat: weekly active in the workflow</text>
  <polygon points="165,215 555,215 525,265 195,265" fill="#e9a274"/>
  <text x="360" y="246" font-size="14" font-weight="700" text-anchor="middle" fill="#1b2433">Relied on: output accepted, not redone</text>
  <polygon points="200,270 520,270 490,320 230,320" fill="#e07b39"/>
  <text x="360" y="301" font-size="14" font-weight="700" text-anchor="middle" fill="#1b2433">KPI moved</text>
</svg>
</div>

What to measure at each stage:

| Stage         | Metric                                                      | What a drop-off tells you                           |
| ------------- | ----------------------------------------------------------- | --------------------------------------------------- |
| **Exposed**   | % of target users with access, in the tool they already use | Integration problem: you built a new place to go    |
| **Tried**     | % who used it once in the first two weeks                   | Awareness or trust problem: nobody explained why    |
| **Repeat**    | Weekly active users inside the workflow                     | Friction: it costs more effort than it saves        |
| **Relied on** | Acceptance rate: AI output used without being redone        | Quality problem: this is where your AI metrics live |
| **KPI moved** | The business metric, against the baseline                   | Wrong workflow, or a gap the AI can't close         |

Two practical rules come from this:

- **Embed, don't migrate.** If people live in Outlook, Slack, Epic or Salesforce, the AI shows up there. Aater's oil-and-gas board member put it bluntly: the last words they want from a vendor are "platform" and "migration." Every extra click shows up as a drop between _Tried_ and _Repeat_.
- **The acceptance rate is the bridge between adoption and model quality.** When users redo the AI's work, they are telling you its precision is too low for the cost of checking it. That is the first place your F1 score meets the real world.

---

## 3. How to pick a business metric that works

A client rarely hands you a metric. They hand you a frustration: "Our denials are out of control," or "The support team is drowning." Turning that into a metric is a five-step conversation.

**Step 1. Find the owner.** Ask who gets called when this number goes bad. If no one owns it, it won't be funded, and your project will die quietly. Aater's checklist starts here: pick a workflow, find the owner.

**Step 2. Map the workflow.** Sit with the people who do the work. Write down every step, every handoff, and where time, money or errors pile up. The real problem is often one layer away from the one you were told about, as Dintash discovered.

**Step 3. Pick one North Star KPI.** One number that the owner would put in their quarterly review. Not five. Examples: denial rate, cost per claim, average handle time, days to close, safety incidents.

**Step 4. Add guardrail metrics.** These are the numbers that must _not_ get worse while you push the North Star: patient safety, compliance violations, customer satisfaction, employee overtime. Guardrails are your defense against Goodhart's law.

**Step 5. Agree on baseline, target and time window, in writing.** "Reduce first-pass denial rate from the current baseline to X% within 8 weeks of go-live, with no increase in compliance findings." If the client won't commit to a target, they don't yet believe the problem is worth solving.

I recommend capturing this as a one-page **metric card** before any code is written:

| Field                  | Example (claims denial prevention)                                       |
| ---------------------- | ------------------------------------------------------------------------ |
| **Owner**              | Director of Revenue Cycle                                                |
| **North Star KPI**     | First-pass claim denial rate                                             |
| **Baseline**           | Measured over the last 3 months of claims data                           |
| **Target and window**  | Relative reduction agreed with the owner, measured 8 weeks after go-live |
| **Guardrails**         | Coder workload stays within capacity; no rise in compliance findings     |
| **Leading indicators** | Acceptance rate of flags; weekly active coders                           |
| **Kill criterion**     | No movement in the leading indicators after 4 weeks: rethink or drop     |

That last row is Aater's "don't be a workflow hugger," written down in advance so nobody has to argue about it later.

---

## 4. Collecting the data from the client

You can't measure what you can't see. In regulated industries you often can't see much at first, which is why Aater's "earn the right to write" applies to data access too: start with the least sensitive, most read-only access that answers the question.

A practical sequence I use:

1. **Interviews and shadowing.** Learn how the work happens and what people consider a good or bad outcome. This is where you discover the real definition of "correct." Ask for examples of the last ten cases that went wrong.
2. **System exports, read-only.** Pull historical records from the systems of record: tickets, claims, orders, logs. Ask for a de-identified sample first if the data is sensitive.
3. **A baseline period.** Measure the KPI and the workflow as they are today, before any AI touches them. Without a baseline, every later number is an opinion.
4. **A golden set labeled by experts.** Have the client's subject-matter experts label a few hundred real cases: "should have been flagged," "correct answer," "acceptable draft." This becomes the ground truth for every AI metric that follows. If two experts disagree often, measure that too: their agreement rate is the ceiling your model can realistically reach.
5. **The cost of each outcome.** Ask the finance or operations lead: what does a missed case cost? What does a false alarm cost in staff time? These two numbers drive almost every technical decision later.
6. **Ongoing feedback.** Design the workflow so users' accept, edit and reject actions are logged. That keeps your metrics alive after launch.

**A data request checklist for the first week:**

- Three to twelve months of historical outcomes for the workflow
- The current baseline value of the North Star KPI, and how it is calculated today
- Volume per day or month, and staff capacity to act on AI output
- The estimated cost of a miss and the cost of a false alarm
- Access to two or three experts for labeling and review
- The compliance constraints: what data can leave which system

---

## 5. Being realistic

Realism is what makes the business trust your numbers. Some habits that help:

- **Compare to humans, not to perfection.** If experienced staff are right 85% of the time, a model at 80% that works ten times faster may be very valuable. A 99% target set without a human baseline is a fantasy.
- **Respect the noise.** Weekly KPIs move on their own because of seasonality, volume swings and staffing. Know how much the number normally wobbles before you claim a win. If the expected effect is smaller than the normal variation, you need a longer window or a controlled comparison.
- **Use shadow mode as your experiment.** Run the AI alongside the current process, record what it _would_ have done, and compare. It's the safest A/B test you'll ever run, and it builds the evidence for the next step on the right-to-write ladder.
- **Time to value in weeks, not quarters.** Aater was clear: if a month passes without visible value, you're probably working on the wrong project.
- **Account for capacity.** A model that flags 2,000 cases a month for a team that can review 1,500 isn't a better model. It's a bottleneck. The worked example below shows why this matters so much.

---

## 6. The metric tree: connecting the boardroom to the confusion matrix

Once you have a North Star, you build down a tree. Each level explains the one above it.

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 380" role="img" aria-label="Metric tree: business KPI at top, then operational metrics, then model metrics, then agent metrics" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">The metric tree</text>
  <rect x="235" y="45" width="250" height="56" rx="10" fill="#e07b39"/>
  <text x="360" y="68" font-size="12" text-anchor="middle" fill="#1b2433">BUSINESS KPI (owner cares)</text>
  <text x="360" y="88" font-size="15" font-weight="700" text-anchor="middle" fill="#1b2433">First-pass denial rate</text>
  <line x1="360" y1="101" x2="180" y2="140" stroke="currentColor" opacity="0.4"/>
  <line x1="360" y1="101" x2="540" y2="140" stroke="currentColor" opacity="0.4"/>
  <rect x="60" y="140" width="240" height="56" rx="10" fill="#e9a274"/>
  <text x="180" y="163" font-size="12" text-anchor="middle" fill="#1b2433">OPERATIONAL</text>
  <text x="180" y="183" font-size="14" font-weight="700" text-anchor="middle" fill="#1b2433">Risky claims fixed before submission</text>
  <rect x="420" y="140" width="240" height="56" rx="10" fill="#e9a274"/>
  <text x="540" y="163" font-size="12" text-anchor="middle" fill="#1b2433">OPERATIONAL</text>
  <text x="540" y="183" font-size="14" font-weight="700" text-anchor="middle" fill="#1b2433">Coder review time per flag</text>
  <line x1="180" y1="196" x2="180" y2="235" stroke="currentColor" opacity="0.4"/>
  <line x1="540" y1="196" x2="540" y2="235" stroke="currentColor" opacity="0.4"/>
  <rect x="60" y="235" width="240" height="56" rx="10" fill="#8aa6c8"/>
  <text x="180" y="258" font-size="12" text-anchor="middle" fill="#1b2433">MODEL</text>
  <text x="180" y="278" font-size="14" font-weight="700" text-anchor="middle" fill="#1b2433">Recall on denied claims</text>
  <rect x="420" y="235" width="240" height="56" rx="10" fill="#8aa6c8"/>
  <text x="540" y="258" font-size="12" text-anchor="middle" fill="#1b2433">MODEL</text>
  <text x="540" y="278" font-size="14" font-weight="700" text-anchor="middle" fill="#1b2433">Precision of flags</text>
  <line x1="180" y1="291" x2="360" y2="315" stroke="currentColor" opacity="0.4"/>
  <line x1="540" y1="291" x2="360" y2="315" stroke="currentColor" opacity="0.4"/>
  <rect x="160" y="315" width="400" height="56" rx="10" fill="#c9cfdb"/>
  <text x="360" y="338" font-size="12" text-anchor="middle" fill="#1b2433">AGENT</text>
  <text x="360" y="358" font-size="14" font-weight="700" text-anchor="middle" fill="#1b2433">Correct reason cited · grounded · cost per claim</text>
</svg>
</div>

The tree does two jobs. Going **down**, it tells engineers what to optimize. Going **up**, it lets you explain to the owner why a change in recall matters to them. If a technical metric can't be connected to a branch of the tree, question why you're tracking it.

---

## 7. Translating business costs into precision, recall and F1

This is the heart of the skill. Every classification model produces four kinds of outcome. The FDE's job is to give each one a business meaning and, ideally, a cost.

| Model outcome           | In plain business terms (denial example)                    | Business effect            |
| ----------------------- | ----------------------------------------------------------- | -------------------------- |
| **True positive (TP)**  | Flagged a claim that really would be denied; coder fixes it | Rework avoided             |
| **False positive (FP)** | Flagged a clean claim; coder checks it for nothing          | Wasted staff time          |
| **False negative (FN)** | Missed a claim that gets denied                             | Same as today (lost value) |
| **True negative (TN)**  | Correctly left a clean claim alone                          | No cost                    |

From these come the familiar metrics, which you should always be able to say in business language:

- **Precision** = TP / (TP + FP). _"Of the claims we ask coders to review, how many actually needed it?"_ Low precision burns staff time and destroys trust, and it shows up in the adoption funnel as a falling acceptance rate.
- **Recall** = TP / (TP + FN). _"Of all the claims that would be denied, how many did we catch?"_ Low recall leaves value on the table.
- **F1** = the harmonic mean of the two. It's useful when a miss and a false alarm cost about the same. **In business, they rarely do.**

### A worked example: why the best F1 is not the best decision

_The numbers below are illustrative, to show the method. Use your client's real costs and volumes._

A hospital submits **10,000 claims a month**, and 8% (800) get denied. You build a model that flags risky claims for a coder to fix before submission. From the client conversations you learn:

- Fixing a flagged claim that would have been denied **saves about USD 112** net (avoided rework minus the review time).
- Reviewing a false alarm **costs about USD 6** of coder time.
- The coding team can review at most **1,500 flagged claims a month**.

So the monthly value is: **112 × TP − 6 × FP.** Here's how four decision thresholds compare:

| Threshold | Recall | Precision | Claims flagged | TP  | FP    | F1       | Net value per month        |
| --------- | ------ | --------- | -------------- | --- | ----- | -------- | -------------------------- |
| 0.2       | 0.90   | 0.30      | 2,400          | 720 | 1,680 | 0.45     | USD 70,560 (over capacity) |
| **0.4**   | 0.78   | 0.50      | 1,248          | 624 | 624   | 0.61     | **USD 66,144**             |
| 0.6       | 0.60   | 0.70      | 686            | 480 | 206   | **0.65** | USD 52,524                 |
| 0.8       | 0.35   | 0.85      | 329            | 280 | 49    | 0.50     | USD 31,066                 |

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 330" role="img" aria-label="Bar chart of monthly net value by threshold: 0.2 is 70,560 but exceeds review capacity; 0.4 is 66,144 and is the best feasible choice; 0.6 is 52,524 and has the highest F1; 0.8 is 31,066" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">Monthly net value by threshold (illustrative)</text>
  <text x="20" y="50" font-size="13" fill="currentColor" opacity="0.7">Highest F1 ≠ highest value; capacity rules out the lowest threshold</text>
  <line x1="80" y1="280" x2="690" y2="280" stroke="currentColor" opacity="0.3"/>
  <rect x="110" y="80" width="110" height="200" rx="4" fill="none" stroke="#8aa6c8" stroke-width="2" stroke-dasharray="6 4"/>
  <text x="165" y="70" font-size="13" font-weight="700" text-anchor="middle" fill="currentColor">70.6K</text>
  <text x="165" y="180" font-size="12" text-anchor="middle" fill="currentColor">over</text>
  <text x="165" y="196" font-size="12" text-anchor="middle" fill="currentColor">capacity</text>
  <rect x="260" y="93" width="110" height="187" rx="4" fill="#e07b39"/>
  <text x="315" y="83" font-size="13" font-weight="700" text-anchor="middle" fill="currentColor">66.1K</text>
  <text x="315" y="190" font-size="12" font-weight="700" text-anchor="middle" fill="#1b2433">best</text>
  <text x="315" y="206" font-size="12" font-weight="700" text-anchor="middle" fill="#1b2433">feasible</text>
  <rect x="410" y="131" width="110" height="149" rx="4" fill="#8aa6c8"/>
  <text x="465" y="121" font-size="13" font-weight="700" text-anchor="middle" fill="currentColor">52.5K</text>
  <text x="465" y="210" font-size="12" font-weight="700" text-anchor="middle" fill="#1b2433">best F1</text>
  <rect x="560" y="192" width="110" height="88" rx="4" fill="#c9cfdb"/>
  <text x="615" y="182" font-size="13" font-weight="700" text-anchor="middle" fill="currentColor">31.1K</text>
  <text x="165" y="302" font-size="13" text-anchor="middle" fill="currentColor">0.2</text>
  <text x="315" y="302" font-size="13" text-anchor="middle" fill="currentColor">0.4</text>
  <text x="465" y="302" font-size="13" text-anchor="middle" fill="currentColor">0.6</text>
  <text x="615" y="302" font-size="13" text-anchor="middle" fill="currentColor">0.8</text>
  <text x="390" y="324" font-size="12" text-anchor="middle" fill="currentColor" opacity="0.7">Decision threshold · net value in USD per month</text>
</svg>
</div>

Three lessons in one table:

1. **The highest F1 (0.6) is not the best business choice.** Because a catch is worth almost 20 times what a false alarm costs, the business wants more recall than F1 rewards.
2. **The highest raw value (0.2) is impossible.** It needs 2,400 reviews a month from a team that can do 1,500. Ignore capacity and the system creates a backlog, coders stop trusting the flags, and adoption collapses.
3. **The right answer (0.4) only appears when you combine the cost matrix with operational reality.** That combination is the FDE skill. No amount of model tuning finds it on its own.

When costs really are lopsided, tell the data scientists directly. Optimize a cost-weighted metric, or an F-beta score with beta above 1 to favor recall (below 1 to favor precision), and pick the threshold on business value, not on the default 0.5.

---

## 8. Metrics for agentic AI systems

Agents don't just classify. They plan, call tools, retrieve documents, write drafts and sometimes take actions. The same translation discipline applies, but the metric menu is larger. Suppose our denial agent also drafts appeal letters and updates the claim record.

| Agent metric                       | What it measures                                           | Business translation                                  |
| ---------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------- |
| **Task success rate**              | % of cases where the whole task was completed correctly    | Work the team no longer has to do                     |
| **Tool-call accuracy**             | Right tool, right arguments, right order                   | Fewer broken records and silent errors                |
| **Groundedness / faithfulness**    | Claims in the output are supported by the source documents | Compliance risk: no invented policy or clinical facts |
| **Retrieval precision and recall** | Did it find the right policy and patient documents?        | Quality of the evidence behind each decision          |
| **Human acceptance / edit rate**   | % of drafts sent as-is, lightly edited, or rewritten       | Real time saved, and trust                            |
| **Escalation rate**                | % of cases handed to a human, and whether that was correct | Safety valve working as designed                      |
| **Safety and policy violations**   | PHI leaks, out-of-scope actions, guardrail breaches        | Regulatory exposure; must stay at zero                |
| **Cost and latency per task**      | Tokens, tool calls and time per completed case             | Unit economics: does automation beat the human cost?  |

Two principles keep agentic metrics honest:

- **Measure the outcome, not the steps.** A beautiful reasoning trace that ends in a wrong claim update is a failure. Task success and human acceptance are your North Star at the system level. Step metrics, like tool-call accuracy and retrieval recall, are for diagnosing _why_.
- **Tie metrics to the right-to-write ladder.** Each step up needs a threshold the client agreed to in advance. For example: in shadow mode, the agent's recommended action matches the expert's in at least the agreed share of a few hundred golden cases, with zero safety violations. Only then does it move to human-in-the-loop. Then acceptance rate and override reasons become the gate for limited autonomy. The business owner, not the engineer, signs off on each threshold.

This is the part of the work I focus on with [EvalTrust](https://evaltrust.cloud): turning those thresholds into evaluation suites, monitoring and an audit trail that a regulated buyer will accept.

---

## 9. The skill itself: metric translation

So what is the skill? I'd call it **metric translation**: the ability to move fluently between the language of the business and the language of the model, in both directions. It combines:

1. **Business literacy.** Understanding how the client makes and loses money, and who owns which number.
2. **Workflow empathy.** Knowing what people actually do all day, so you can predict where adoption will break.
3. **Cost reasoning.** Putting a price, even a rough one, on each kind of error.
4. **Statistical judgment.** Baselines, noise, sample sizes, inter-rater agreement and the difference between a real effect and a lucky week.
5. **AI evaluation fluency.** Knowing which metric fits which system: precision and recall for detection, calibration for risk scores, groundedness for RAG, task success and tool accuracy for agents.
6. **The courage to kill.** Writing the kill criterion before you start, and honoring it.

How to practice it, even before your first FDE role:

- Take any model you've built and **rewrite its evaluation in business terms**: who is affected by each error type, and what does each cost?
- For every metric on your dashboard, ask "**so what?**" until you reach a number someone senior cares about. If you can't get there, drop the metric.
- Run the **threshold exercise** from section 7 on a real dataset with made-up but reasonable costs and a capacity limit. Notice how often the best F1 isn't the best choice.
- Interview someone in operations, finance or a clinical role about how they measure success. You'll learn more about metrics in an hour than in a week of tutorials.

---

## 10. A one-page checklist

**Before building**

- [ ] Owner identified and engaged
- [ ] Workflow mapped with the people who do it
- [ ] One North Star KPI, plus guardrail metrics
- [ ] Baseline measured; target and time window agreed in writing
- [ ] Cost of a miss and cost of a false alarm estimated
- [ ] Capacity limits known
- [ ] Kill criterion written down

**While building**

- [ ] Golden set labeled by client experts; their agreement measured
- [ ] Metric tree connects every model metric to the KPI
- [ ] Threshold chosen on business value and capacity, not default F1
- [ ] Shadow-mode comparison planned

**After launch**

- [ ] Adoption funnel tracked weekly, inside the tools people already use
- [ ] Acceptance, edit and override reasons logged
- [ ] KPI reviewed against the baseline at the agreed date
- [ ] Workflow dropped or doubled down on, based on evidence

---

## Let's talk

How do you choose metrics on your AI projects? Have you seen a high F1 score hide a system nobody used, or a business KPI that refused to move? I'd love to hear your stories. Reach me on [LinkedIn](https://www.linkedin.com/in/mohcine-madkour-83a642b2) or at [mohcine@evaltrust.cloud](mailto:mohcine@evaltrust.cloud).

---

### The FDE skills series

1. [Think like a product manager](/writing/2026/fde-think-like-a-product-manager/)
2. **From business KPI to F1 score** (this article)
3. [The people stack](/writing/2026/fde-people-skills-techniques/)
4. [Integration and rapid prototyping](/writing/2026/fde-integration-and-prototyping/)
5. [Evaluation, guardrails and observability](/writing/2026/fde-evaluation-guardrails-observability/)
6. [Security, privacy and compliance](/writing/2026/fde-security-privacy-compliance/)
7. [Domain expertise and scoping](/writing/2026/fde-domain-expertise-and-scoping/)
8. [Communication and ownership](/writing/2026/fde-communication-and-ownership/)

### Sources and notes

- Aater Suleman, talk on forward deployed engineering, Dallas, November 5, 2026: the Dintash case (15% to 40%), "meet people where they work," "don't be a workflow hugger," time to value in weeks, and "earn the right to write."
- The claims denial example, its costs and its thresholds are illustrative, constructed to demonstrate the method. They are not data from any client.
- Goodhart's law is paraphrased from economist Charles Goodhart, as popularized by anthropologist Marilyn Strathern.
