---
layout: post
title: "Go Narrow, Start Small: Domain Expertise and Scoping Under Ambiguity for Forward Deployed Engineers"
date: 2026-11-06
description: "Two skills that decide whether an FDE engagement succeeds: learning a customer's industry fast enough to be useful, and turning a vague 'we need to do something with AI' into a small first step that delivers value in weeks."
tags: [ForwardDeployedEngineering, DomainExpertise, Scoping, ProductManagement, AIStrategy, AICareers]
categories: writing
related_posts: true
toc:
  beginning: true
---

> **Part 7 of the FDE skills series.** Aater Suleman's advice to founders in his Dallas talk was to **go narrow and go deep**. His advice on prototypes was that if something takes too long, **you've taken too big a bite.** This part turns both into practical skills: learning a domain quickly, and scoping work when the request is vague.

## Part A: Domain expertise

### 1. Why depth beats breadth

Aater put it memorably: an IT team at a hospital only understands how _that_ hospital works. If you only work on revenue cycle management for US hospitals and you've done 20 of them, you'll know more about their business than they know about their own. That depth is what creates the value proposition.

His portfolio examples were all specialists: revenue cycle for hospitals, property valuation workflows for counties, administrative staff for HVAC companies, AI adoption for private-equity-backed firms. He also predicted that the FDE role will spread across **pods** that include a dedicated domain expert, and mentioned the rise of the "forward deployed expert" for exactly this reason.

Domain knowledge matters because nearly every judgment an FDE makes depends on it:

- Which problem is worth solving? (Requires knowing where the money and pain are)
- What counts as a correct answer? (Requires knowing the rules and exceptions)
- What will users accept? (Requires knowing their workflow and culture)
- What could go badly wrong? (Requires knowing the regulations and risks)

### 2. What "knowing a domain" actually means

Domain expertise isn't one thing. I break it into five layers, from quickest to slowest to learn:

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 300" role="img" aria-label="Five layers of domain knowledge, from fastest to learn to slowest: vocabulary, workflows, economics, regulation, judgment" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">Five layers of domain knowledge</text>
  <rect x="20" y="50" width="200" height="40" rx="6" fill="#c9cfdb"/><text x="35" y="76" font-size="14" font-weight="700" fill="#1b2433">Vocabulary</text>
  <text x="240" y="76" font-size="13" fill="currentColor">Terms, acronyms, codes · days</text>
  <rect x="20" y="98" width="290" height="40" rx="6" fill="#aebfd6"/><text x="35" y="124" font-size="14" font-weight="700" fill="#1b2433">Workflows</text>
  <text x="330" y="124" font-size="13" fill="currentColor">Who does what, in which system · weeks</text>
  <rect x="20" y="146" width="380" height="40" rx="6" fill="#8aa6c8"/><text x="35" y="172" font-size="14" font-weight="700" fill="#1b2433">Economics</text>
  <text x="420" y="172" font-size="13" fill="currentColor">How money is made and lost · weeks</text>
  <rect x="20" y="194" width="470" height="40" rx="6" fill="#e9a274"/><text x="35" y="220" font-size="14" font-weight="700" fill="#1b2433">Regulation and risk</text>
  <text x="510" y="220" font-size="13" fill="currentColor">Rules, audits · months</text>
  <rect x="20" y="242" width="560" height="40" rx="6" fill="#e07b39"/><text x="35" y="268" font-size="14" font-weight="700" fill="#1b2433">Judgment</text>
  <text x="600" y="268" font-size="13" fill="currentColor">Edge cases · years</text>
</svg>
</div>

You can't buy the top layer quickly. That's why the realistic strategy is to **learn the first three layers fast and partner for the last two**.

### 3. A two-week domain sprint

When I start in a new industry or a new customer, I run a deliberate learning sprint.

**Days 1–3: Vocabulary.** Build a glossary as you go: every acronym, code and term you hear, with a one-line definition confirmed by someone in the business. Read the trade press and the job descriptions of the people you'll work with; job postings are a surprisingly good map of what a role really does.

**Days 4–7: Workflows.** Shadow the people who do the work (see the techniques in [Part 3](/writing/2026/fde-people-skills-techniques/)). Draw the process end to end, including the systems, handoffs and spreadsheets in between.

**Days 8–10: Economics.** Follow the money. Ask: how does this organization earn revenue? Where does it lose it? What are the biggest cost lines? What metrics do executives watch? In healthcare revenue cycle, for example, that means understanding claims, denials, days in accounts receivable and the cost of rework.

**Days 11–14: Regulation and risk.** Find the rules that govern the workflow and the failures that would make the news. Ask the compliance team what keeps them up at night. ([Part 6](/writing/2026/fde-security-privacy-compliance/) covers the security and compliance side.)

At the end, write a two-page **domain brief**: glossary highlights, the workflow map, the money map, the key rules, and the questions you still can't answer. Ask a domain expert to correct it. Their corrections are the most valuable part.

### 4. Working with subject-matter experts

Even with a strong sprint, you'll depend on experts for judgment. Make that partnership productive:

- **Respect their time.** Bring specific questions and real examples, not "tell me about your job."
- **Use them for labeling and edge cases.** Their judgment defines the golden set ([Part 5](/writing/2026/fde-evaluation-guardrails-observability/)).
- **Make them visible.** Credit them in demos and reports. Experts who feel like co-owners become your champions.
- **Accept "that would never work here."** It's usually the most useful sentence you'll hear all week. Ask why.

### 5. Choosing your niche

Aater's advice to founders applies to individual careers too: compound your knowledge by repeating similar work. Good signals for a niche:

- You already have a head start there (prior job, degree, family business)
- The problems are expensive and frequent
- The work is complex enough that general software can't solve it alone
- The regulations create a barrier that rewards specialists

My own background in clinical informatics, surgical robotics and industrial IoT is why I focus EvalTrust on regulated industries, starting with healthcare. Depth in one area makes everything else in this series easier.

---

## Part B: Scoping under ambiguity

### 6. The vague request

Aater described the pattern well: a mandate comes from the top, someone is told to "do something with AI," and the team picks a use case because everyone needs to do _something_. That's how Dintash ended up with a working system nobody used.

The FDE's job is to turn ambiguity into a first step that is **small, valuable, measurable and safe**. Small enough to deliver in days or weeks; valuable enough that the owner cares; measurable against a baseline; safe enough to start read-only.

### 7. A scoping process that works

**Step 1. Collect candidates.** From discovery interviews, list every workflow where people mentioned pain. Aim for ten to twenty.

**Step 2. Score them.** For each, estimate value (how much the KPI could move), feasibility (data availability, integration difficulty, risk) and time to first value.

**Step 3. Plot and pick.** Choose a candidate with high value and high feasibility for the first slice. Park the big, hard, high-value ones for later, once you've earned trust.

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 400" role="img" aria-label="Value versus feasibility matrix with four quadrants: start here (high value, high feasibility), plan for later (high value, low feasibility), quick fixes (low value, high feasibility), avoid (low value, low feasibility)" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">Pick the first slice: value vs feasibility</text>
  <rect x="100" y="50" width="290" height="150" fill="#aebfd6"/>
  <rect x="400" y="50" width="290" height="150" fill="#e07b39"/>
  <rect x="100" y="210" width="290" height="150" fill="#e3e6ea"/>
  <rect x="400" y="210" width="290" height="150" fill="#c9cfdb"/>
  <text x="245" y="115" font-size="16" font-weight="700" text-anchor="middle" fill="#1b2433">Plan for later</text>
  <text x="245" y="140" font-size="12" text-anchor="middle" fill="#1b2433">big bets, after trust is earned</text>
  <text x="545" y="115" font-size="16" font-weight="700" text-anchor="middle" fill="#1b2433">Start here</text>
  <text x="545" y="140" font-size="12" text-anchor="middle" fill="#1b2433">first slice, the bright spot</text>
  <text x="245" y="275" font-size="16" font-weight="700" text-anchor="middle" fill="#1b2433">Avoid</text>
  <text x="245" y="300" font-size="12" text-anchor="middle" fill="#1b2433">hard and not worth it</text>
  <text x="545" y="275" font-size="16" font-weight="700" text-anchor="middle" fill="#1b2433">Quick fixes</text>
  <text x="545" y="300" font-size="12" text-anchor="middle" fill="#1b2433">may not need AI at all</text>
  <text x="395" y="385" font-size="13" text-anchor="middle" fill="currentColor">Feasibility (data, integration, risk) →</text>
  <text x="60" y="205" font-size="13" text-anchor="middle" fill="currentColor" transform="rotate(-90 60 205)">Business value →</text>
</svg>
</div>

**Step 4. Cut the slice thinner.** Take the chosen workflow and shrink it until you can show value quickly: one site instead of all, one document type instead of every type, one step of the process instead of the whole thing. Aater's test: if even the prototype takes weeks, the bite is too big.

**Step 5. Write a one-page scope.** Before building, agree on this with the owner:

| Section             | Contents                                                                                             |
| ------------------- | ---------------------------------------------------------------------------------------------------- |
| **Problem**         | The workflow and pain, in the users' words                                                           |
| **First slice**     | Exactly what's in, and explicitly what's out                                                         |
| **Success**         | The KPI, baseline, target and date (see [Part 2](/writing/2026/fde-business-metrics-to-ai-metrics/)) |
| **Data and access** | What you need, starting at the least sensitive level                                                 |
| **Risks**           | What could go wrong and how you'll know                                                              |
| **Kill criterion**  | When you'll stop or switch                                                                           |
| **Next slices**     | What comes after, if this works                                                                      |

### 8. Saying no (and "not yet")

Scoping means turning down good ideas. Aater named "unclear business value" as the biggest reason AI projects fail, and the worst answer to "why are we doing this?" is "because someone told us to." Some phrases that help:

- "That's a great idea for phase two. Can we earn the right to it with this smaller piece first?"
- "If we do both, we'll do neither well. Which matters more to your quarterly goals?"
- "I don't think this one needs AI. A rule or a report would solve it faster."
- "Before we add scope, can we see whether the first slice moved the number?"

Saying "this doesn't need AI" is one of the most trust-building things an FDE can do. It shows you're optimizing for their outcome, not your project.

### 9. Living with ambiguity

Even with good scoping, things will stay uncertain. Some habits that help:

- **Write down assumptions** and turn each into a question to test.
- **Prefer reversible decisions.** Choose approaches you can change cheaply as you learn.
- **Timebox exploration.** "We'll spend two days finding out whether the data supports this, then decide."
- **Share your uncertainty honestly.** "Here's what we know, what we don't, and how we'll find out" builds more credibility than false confidence.

---

## How to build these skills

- **Run a domain sprint on an industry you're curious about.** Build the glossary, workflow map and money map, then ask an expert to review it.
- **Practice scoping on public problems.** Take a vague prompt ("use AI to improve hospital operations") and write a one-page scope for a first slice.
- **Collect "doesn't need AI" examples.** It trains the judgment to recognize simpler solutions.
- **Pick a niche and repeat.** Each project in the same domain makes the next one faster and better.

---

## Let's talk

Which industry are you going deep in, and how did you learn it? What's the smallest first slice that ever won you a big project? Tell me on [LinkedIn](https://www.linkedin.com/in/mohcine-madkour-83a642b2) or at [mohcine@evaltrust.cloud](mailto:mohcine@evaltrust.cloud).

---

### The FDE skills series

1. [Think like a product manager](/writing/2026/fde-think-like-a-product-manager/)
2. [From business KPI to F1 score](/writing/2026/fde-business-metrics-to-ai-metrics/)
3. [The people stack](/writing/2026/fde-people-skills-techniques/)
4. [Integration and rapid prototyping](/writing/2026/fde-integration-and-prototyping/)
5. [Evaluation, guardrails and observability](/writing/2026/fde-evaluation-guardrails-observability/)
6. [Security, privacy and compliance](/writing/2026/fde-security-privacy-compliance/)
7. **Domain expertise and scoping** (this article)
8. [Communication and ownership](/writing/2026/fde-communication-and-ownership/)

### Sources and notes

- Aater Suleman, talk on forward deployed engineering, Dallas, November 5, 2026: "go narrow, go deep," the hospital revenue-cycle example, forward deployed pods and experts, the top-down mandate pattern, unclear business value, and "too big a bite."
- The domain-knowledge layers, sprint plan and scoping template reflect the author's practice.
