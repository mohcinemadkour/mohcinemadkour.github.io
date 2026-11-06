---
layout: post
title: "Think Like a Product Manager, Ship Like an Engineer: The Real Path to Becoming a Forward Deployed Engineer"
date: 2026-11-05
description: "Lessons from Aater Suleman's Dallas talk on forward deployed engineering, and why product-management thinking, not more code, is the skill that separates the engineers who get these roles. Charts, data, a skills map and a practical plan."
tags: [ForwardDeployedEngineering, ProductManagement, AICareers, AIStrategy, AIAdoption, Leadership]
categories: writing
related_posts: true
toc:
  beginning: true
---

> **Who this is for.** Engineers who want to become forward deployed engineers (FDEs), product managers wondering whether the role fits them, and founders building AI services companies. It summarizes a talk by **Aater Suleman** in Dallas on November 5, 2026, adds market data, and gives my own perspective as a PhD, a long-time AI engineer and the founder of [EvalTrust](https://evaltrust.cloud). The ideas credited to Aater are his; the commentary and the plan at the end are mine.

## TL;DR

- **The FDE role is exploding.** Indeed counted 5,330 FDE postings in April 2026, up from 643 a year earlier. Supply is not keeping up.
- **FDEs fill the gap** between what an AI platform provides and what a customer actually needs, and they are judged on outcomes, not hours.
- **The hidden core of the role is product management.** When AI makes building cheap, the scarce skill is deciding _what_ to build, for _whom_, and _how you will know it worked_.
- **You can learn it.** Five habits (discover first, prototype fast, earn trust step by step, meet people where they work, think in outcomes) are the curriculum. A 90-day plan is at the end.

---

## 1. The moment: why everyone is suddenly hiring FDEs

Aater opened with a confession: ten years ago he built a cloud services company in Dallas that never billed a single hour. It sold productized packages and was paid for results. Most of the large Dallas companies were clients, and the company was later acquired by NTT Data. The problem was that _nobody had a name for what they were doing_. Today we do: **forward deployed engineering**. Since then, his accelerator has worked with 35 companies that together have sold roughly 100 million dollars in AI-native services, and most of the lessons below come from that portfolio.

The market numbers explain why the name suddenly matters.

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 340" role="img" aria-label="Bar chart: FDE job postings on Indeed, April 2025: 643; April 2026: 5,330" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">FDE job postings on Indeed</text>
  <text x="20" y="50" font-size="13" fill="currentColor" opacity="0.7">April 2025 vs April 2026 (+729% year over year)</text>
  <line x1="120" y1="290" x2="690" y2="290" stroke="currentColor" opacity="0.3"/>
  <rect x="160" y="263" width="160" height="27" rx="4" fill="#8aa6c8"/>
  <text x="240" y="253" font-size="16" font-weight="700" text-anchor="middle" fill="currentColor">643</text>
  <text x="240" y="314" font-size="14" text-anchor="middle" fill="currentColor">April 2025</text>
  <rect x="440" y="70" width="160" height="220" rx="4" fill="#e07b39"/>
  <text x="520" y="60" font-size="16" font-weight="700" text-anchor="middle" fill="currentColor">5,330</text>
  <text x="520" y="314" font-size="14" text-anchor="middle" fill="currentColor">April 2026</text>
</svg>
<p style="font-size:0.85rem;opacity:0.75;">Source: Indeed data reported by Business Insider, via <a href="https://www.scaler.com/topics/forward-deployed-engineer-jobs-grew-1165-percent/">Scaler</a>.</p>
</div>

Other signals point the same way:

- **Big money is moving into deployment.** Accenture agreed in January 2026 to buy UK applied-AI firm Faculty in a deal valued at about 1 billion dollars ([Consultancy.uk](https://www.consultancy.uk/news/42712/accenture-swoops-for-uk-start-up-faculty-amid-ai-services-pivot)). Aater cited roughly **7.5 billion dollars** committed to AI deployment by Anthropic, OpenAI, AWS, Google and Microsoft.
- **Demand is broad.** Aater said 9 to 17 companies that have never hired an FDE post their first FDE role every week. In Dallas alone, banks and insurers are posting.
- **The pay reflects the scarcity.** Bloomberry's review of 1,000 FDE postings found a median base salary of about **173,816 dollars** ([Paraform](https://www.paraform.com/insights/how-to-hire-a-forward-deployed-engineer)).
- **The talent is thin.** By the figure Aater cited, only about **1 in 8** engineers qualifies for the role today.

That last number is the interesting one. If the demand is there, why can't companies fill the roles? Because the missing skill is not technical.

---

## 2. What an FDE actually does

Aater's definition is simple. A big vendor provides a platform: Claude, AWS, SAP. A customer has a real workflow and a business problem. **There is a gap in between, and someone has to fill it.** That someone is the forward deployed engineer.

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 200" role="img" aria-label="Diagram: Platform, then the gap filled by the FDE, then the customer's workflow and KPI" style="width:100%;height:auto;font-family:inherit;">
  <rect x="10" y="40" width="190" height="120" rx="12" fill="none" stroke="#8aa6c8" stroke-width="2"/>
  <text x="105" y="85" font-size="17" font-weight="700" text-anchor="middle" fill="currentColor">Platform</text>
  <text x="105" y="110" font-size="13" text-anchor="middle" fill="currentColor" opacity="0.8">Claude, AWS, SAP</text>
  <text x="105" y="130" font-size="13" text-anchor="middle" fill="currentColor" opacity="0.8">core technology</text>
  <text x="230" y="108" font-size="28" text-anchor="middle" fill="#e07b39">→</text>
  <rect x="260" y="25" width="200" height="150" rx="12" fill="#e07b39"/>
  <text x="360" y="70" font-size="17" font-weight="700" text-anchor="middle" fill="#1b2433">The gap = FDE</text>
  <text x="360" y="98" font-size="13" text-anchor="middle" fill="#1b2433">discovery · prototypes</text>
  <text x="360" y="118" font-size="13" text-anchor="middle" fill="#1b2433">integration · evaluation</text>
  <text x="360" y="138" font-size="13" text-anchor="middle" fill="#1b2433">change management</text>
  <text x="490" y="108" font-size="28" text-anchor="middle" fill="#e07b39">→</text>
  <rect x="520" y="40" width="190" height="120" rx="12" fill="none" stroke="#8aa6c8" stroke-width="2"/>
  <text x="615" y="85" font-size="17" font-weight="700" text-anchor="middle" fill="currentColor">Customer</text>
  <text x="615" y="110" font-size="13" text-anchor="middle" fill="currentColor" opacity="0.8">a real workflow</text>
  <text x="615" y="130" font-size="13" text-anchor="middle" fill="currentColor" opacity="0.8">one KPI that matters</text>
</svg>
</div>

He described the role as having several facets, each added on top of the last:

1. **Bridge the technology gap** between platform and need.
2. **Connect the work to business value**, not to "doing AI."
3. **Have the people skills** to work directly with business users, not just other engineers.
4. **Do product management**: choose the right thing to do, roadmap it, and sequence it so value shows up fast.

He called this the **hard stack** and the **soft stack**. Most engineering programs teach the first. The second is why only about one engineer in eight is ready.

### Why the wall came down

Aater framed the FDE as the end of a long trend. Before Agile, a 300-page requirements document was thrown over a wall to developers. Scrum brought a product owner onto the team. DevOps and DevSecOps brought operations and security closer. Now AI changes _how the work itself is done_, so the last wall between engineers and the business is gone. In the cloud era, his engineers talked to the customer's engineers. **FDEs talk to the business**, and that is a different conversation entirely.

---

## 3. The hidden core of the role: product management

This is the part of the talk I want every aspiring FDE to read twice.

### Building got cheap, so deciding got expensive

Aater compared two eras of his own work. In the cloud-migration years, a project was roughly one week of assessment, 8 to 20 weeks of implementation, and a week of re-syncing with the customer. With AI, implementation has shrunk dramatically, and **about 70% of the effort now goes into planning**, because the work reaches parts of the company that have never dealt with engineering.

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 230" role="img" aria-label="Stacked bars: in the cloud era, planning was a small share and building most of the effort; in the AI era, planning is about 70% of the effort" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">Where the effort goes</text>
  <text x="20" y="50" font-size="13" fill="currentColor" opacity="0.7">Illustrative, based on the timelines Aater described</text>
  <text x="20" y="98" font-size="14" fill="currentColor">Cloud era</text>
  <rect x="130" y="78" width="45" height="32" fill="#e07b39"/>
  <rect x="175" y="78" width="470" height="32" fill="#8aa6c8"/>
  <rect x="645" y="78" width="45" height="32" fill="#c9cfdb"/>
  <text x="410" y="99" font-size="13" text-anchor="middle" fill="#1b2433">Building: 8–20 weeks</text>
  <text x="20" y="158" font-size="14" fill="currentColor">AI era</text>
  <rect x="130" y="138" width="392" height="32" fill="#e07b39"/>
  <rect x="522" y="138" width="112" height="32" fill="#8aa6c8"/>
  <rect x="634" y="138" width="56" height="32" fill="#c9cfdb"/>
  <text x="326" y="159" font-size="13" text-anchor="middle" fill="#1b2433">Discovery and planning: ~70%</text>
  <rect x="130" y="196" width="14" height="14" fill="#e07b39"/><text x="150" y="208" font-size="12" fill="currentColor">Planning</text>
  <rect x="230" y="196" width="14" height="14" fill="#8aa6c8"/><text x="250" y="208" font-size="12" fill="currentColor">Building</text>
  <rect x="330" y="196" width="14" height="14" fill="#c9cfdb"/><text x="350" y="208" font-size="12" fill="currentColor">Re-sync and adoption</text>
</svg>
</div>

When code is cheap, the expensive mistake is building the wrong thing well. That is a product-management problem, not an engineering one.

### The product-manager ratio is collapsing

Aater shared a striking data point. In his old company, one product owner served about three teams, roughly **one PM per 20 engineers**. One OpenAI partner he has advised is now talking about **one PM per engineer**. His metaphor: coding with AI and no product manager is like driving 90 miles an hour without GPS.

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 220" role="img" aria-label="Comparison: traditionally 1 product manager per 20 engineers; emerging AI teams 1 product manager per engineer" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">Product managers per engineer</text>
  <text x="20" y="70" font-size="14" fill="currentColor">Traditional team</text>
  <circle cx="190" cy="65" r="9" fill="#e07b39"/>
  <g fill="#8aa6c8">
    <circle cx="215" cy="65" r="7"/><circle cx="235" cy="65" r="7"/><circle cx="255" cy="65" r="7"/><circle cx="275" cy="65" r="7"/><circle cx="295" cy="65" r="7"/>
    <circle cx="315" cy="65" r="7"/><circle cx="335" cy="65" r="7"/><circle cx="355" cy="65" r="7"/><circle cx="375" cy="65" r="7"/><circle cx="395" cy="65" r="7"/>
    <circle cx="415" cy="65" r="7"/><circle cx="435" cy="65" r="7"/><circle cx="455" cy="65" r="7"/><circle cx="475" cy="65" r="7"/><circle cx="495" cy="65" r="7"/>
    <circle cx="515" cy="65" r="7"/><circle cx="535" cy="65" r="7"/><circle cx="555" cy="65" r="7"/><circle cx="575" cy="65" r="7"/><circle cx="595" cy="65" r="7"/>
  </g>
  <text x="620" y="70" font-size="15" font-weight="700" fill="currentColor">1 : 20</text>
  <text x="20" y="130" font-size="14" fill="currentColor">Emerging AI team</text>
  <circle cx="190" cy="125" r="9" fill="#e07b39"/><circle cx="215" cy="125" r="7" fill="#8aa6c8"/>
  <text x="620" y="130" font-size="15" font-weight="700" fill="currentColor">1 : 1</text>
  <circle cx="195" cy="180" r="9" fill="#e07b39"/><text x="210" y="185" font-size="12" fill="currentColor">Product manager</text>
  <circle cx="335" cy="180" r="7" fill="#8aa6c8"/><text x="348" y="185" font-size="12" fill="currentColor">Engineer</text>
  <text x="20" y="210" font-size="12" fill="currentColor" opacity="0.7">As described by Aater Suleman; one advisee's plan, not an industry average.</text>
</svg>
</div>

He predicted strong demand for product management as a skill, and noted that most services companies, and most companies that don't build products, don't have it in-house.

### A case that proves it: usage is not value

The story that stuck with me was from **Dintash**, one of Aater's portfolio companies. A client had a top-down AI mandate. The team built a working automation in two weeks, and **nobody used it**. So they did what Aater called the hardest thing an engineer does: they talked to people. The real problem was one layer up. Fixing it moved the cost metric 15%, and then the number stopped moving, even as AI usage kept climbing. They went back and interviewed about 50 business users, found more workflows worth automating, and kept iterating. The KPI eventually moved **40%**.

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 280" role="img" aria-label="Line chart: KPI improvement at Dintash. After the first build: 0%. After fixing the real problem: 15%, which plateaued. After interviewing about 50 users: 40%" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">Dintash: KPI improvement as discovery deepened</text>
  <line x1="80" y1="230" x2="690" y2="230" stroke="currentColor" opacity="0.3"/>
  <line x1="80" y1="60" x2="80" y2="230" stroke="currentColor" opacity="0.3"/>
  <text x="70" y="234" font-size="12" text-anchor="end" fill="currentColor">0%</text>
  <text x="70" y="166" font-size="12" text-anchor="end" fill="currentColor">20%</text>
  <text x="70" y="98" font-size="12" text-anchor="end" fill="currentColor">40%</text>
  <polyline points="130,230 300,179 470,179 640,94" fill="none" stroke="#e07b39" stroke-width="4"/>
  <circle cx="130" cy="230" r="7" fill="#8aa6c8"/>
  <circle cx="300" cy="179" r="7" fill="#e07b39"/>
  <circle cx="470" cy="179" r="7" fill="#e07b39"/>
  <circle cx="640" cy="94" r="8" fill="#e07b39"/>
  <text x="300" y="165" font-size="13" font-weight="700" text-anchor="middle" fill="currentColor">15%</text>
  <text x="470" y="165" font-size="13" text-anchor="middle" fill="currentColor">plateau: more AI, same KPI</text>
  <text x="640" y="80" font-size="13" font-weight="700" text-anchor="middle" fill="currentColor">40%</text>
  <text x="130" y="254" font-size="12" text-anchor="middle" fill="currentColor">Built to mandate</text>
  <text x="300" y="254" font-size="12" text-anchor="middle" fill="currentColor">Real problem found</text>
  <text x="470" y="254" font-size="12" text-anchor="middle" fill="currentColor">More AI added</text>
  <text x="640" y="254" font-size="12" text-anchor="middle" fill="currentColor">~50 users interviewed</text>
</svg>
</div>

Notice that every jump in the curve came from a product decision, not a technical breakthrough.

---

## 4. The five product habits every FDE needs

Aater distilled his portfolio's experience into five lessons. Read them as a product-management curriculum.

| Habit                              | What it means                                                                                           | Product skill underneath            |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **1. Discover before you build**   | Spend most of the time understanding the workflow, the owner and the real pain.                         | User research, problem framing      |
| **2. Show it before they commit**  | Bring a working prototype to the first call, using mock or read-only data. Show three options, not one. | Rapid prototyping, option framing   |
| **3. Earn the right to write**     | Start read-only. Prove safety with evidence before asking to change real data.                          | Roadmapping, risk sequencing        |
| **4. Meet people where they work** | No new platform, no migration. Fit into the tools and habits people already have.                       | Adoption and change design          |
| **5. Think in outcomes**           | Measure the KPI moved, not hours spent. Drop a workflow that isn't delivering.                          | Hypotheses, metrics, prioritization |

Two of these deserve a closer look.

### Prototypes in hours, not weeks

Someone in the audience asked how long a prototype should take. Aater's answer: in 2026, measure it in **hours, maybe days, never weeks**. If it takes weeks even with today's coding tools, "you're taking a bite that's too big," and that is a product-management failure. You don't need customer data either; synthetic data is enough for the first round.

### The right-to-write ladder

For anyone working in regulated industries, this was the most important idea of the night. Customers won't let your AI write to their databases, records or production systems on day one, and they shouldn't. So you plan the work as a ladder and climb it with evidence.

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 270" role="img" aria-label="Staircase: 1 mock data, 2 read-only on real data, 3 shadow mode, 4 human in the loop, 5 autonomous writes" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">Earn the right to write</text>
  <rect x="20" y="200" width="130" height="50" rx="6" fill="#c9cfdb"/>
  <text x="85" y="222" font-size="13" font-weight="700" text-anchor="middle" fill="#1b2433">1. Mock data</text>
  <text x="85" y="240" font-size="11" text-anchor="middle" fill="#1b2433">synthetic prototype</text>
  <rect x="160" y="160" width="130" height="90" rx="6" fill="#aebfd6"/>
  <text x="225" y="182" font-size="13" font-weight="700" text-anchor="middle" fill="#1b2433">2. Read-only</text>
  <text x="225" y="200" font-size="11" text-anchor="middle" fill="#1b2433">real data, answers</text>
  <rect x="300" y="120" width="130" height="130" rx="6" fill="#8aa6c8"/>
  <text x="365" y="142" font-size="13" font-weight="700" text-anchor="middle" fill="#1b2433">3. Shadow</text>
  <text x="365" y="160" font-size="11" text-anchor="middle" fill="#1b2433">"what it would do"</text>
  <rect x="440" y="80" width="130" height="170" rx="6" fill="#e9a274"/>
  <text x="505" y="102" font-size="13" font-weight="700" text-anchor="middle" fill="#1b2433">4. Human in loop</text>
  <text x="505" y="120" font-size="11" text-anchor="middle" fill="#1b2433">AI proposes, people approve</text>
  <rect x="580" y="40" width="130" height="210" rx="6" fill="#e07b39"/>
  <text x="645" y="62" font-size="13" font-weight="700" text-anchor="middle" fill="#1b2433">5. Autonomous</text>
  <text x="645" y="80" font-size="11" text-anchor="middle" fill="#1b2433">proven tasks only</text>
</svg>
</div>

Aater's advice was to stop arguing about access and start showing proof: "here's what the system _would_ have done" next to what people actually did. Choosing that sequence is a product decision. **Producing the evidence for each step is evaluation**, which is exactly why I care so much about this idea. It's the problem we work on at EvalTrust.

### The outcome chain

On pricing and value, Aater described an **outcome chain**: getting paid for availability is the bottom rung; then hours; then a delivered project; then usage; then movement on an internal KPI; and at the top, revenue earned or cost saved. Each rung is a leading indicator of the next. The goal is not to jump to revenue sharing on day one but to keep climbing. His blunt advice for anyone stuck: **don't be a workflow hugger.** If a workflow isn't showing value within a month, move on to one that will.

---

## 5. Thinking like a product manager: the mental shift

I have spent more than 13 years building AI in clinical research, surgical robotics and industrial IoT, and I hold a PhD in computer science. Here's my honest observation: technical training rewards you for answering the question you were given. Product thinking asks whether it was the right question.

These are the five shifts I believe matter most:

1. **From "how do I build it?" to "who is it for and what changes if it works?"** Start every engagement by naming the workflow, the owner and the one metric.
2. **From specifications to hypotheses.** Write it as a bet: _"If we automate X, metric Y moves by Z within N weeks."_ Then go test it.
3. **From finished software to fast evidence.** A rough prototype shown today beats a polished system shown next quarter.
4. **From "they won't give us access" to "how do we earn it?"** Treat trust as a product feature you design, not an obstacle you complain about.
5. **From effort to outcomes.** Nobody cares how many days you worked. They care that the needle moved.

Aater had a line for product managers who worry they aren't technical enough: you don't need to be anymore. Anyone in the room can build a prototype with today's tools. **So the door swings both ways.** Engineers need to learn product thinking, and product managers need to learn to build the prototype. Whoever closes their gap first is the FDE.

### Where the role is heading: pods, not unicorns

Aater was realistic about how rare the full package is. One person who is an excellent engineer, product manager, domain expert and strategist is a unicorn, and you can't hire 300,000 unicorns. His prediction is that the role will spread across **forward deployed pods**: a domain expert, a product manager, an AI strategist and an engineer working as one unit. He pointed out that this has happened in every tech shift: everyone starts full-stack, roles split, then recombine as tools improve.

That's good news for career-changers. You don't have to be everything. You need to be strong in one seat and fluent enough in the others to work as part of the pod.

---

## 6. How to build the skills: a 90-day plan

This plan is mine, built from Aater's lessons and what I've seen work.

**Days 1–30: Learn to discover**

- Pick one real workflow, at work, in a nonprofit or at a local business, and interview five people who live it.
- For each, write down: the owner, the pain, the metric that would prove it got better.
- Read one book on change. Aater recommended _Switch_ and its idea of "bright spots": small, visible wins that spread.

**Days 31–60: Learn to prototype and frame options**

- For the best problem you found, build **three** rough prototypes in a day each, using synthetic data.
- Show them to the people you interviewed. Ask, "Which is closest to what you need?" Write down what changed in their thinking.
- Write a one-line hypothesis and a simple read-only plan for the winner.

**Days 61–90: Learn to deliver outcomes**

- Run the winning prototype in read-only or shadow mode on real (permitted) data.
- Measure the metric. If it doesn't move, drop it and pick the next workflow. Practice not being a workflow hugger.
- Write it up publicly as a case study: problem, hypothesis, prototype, evidence, result.

That case study is your portfolio. When Aater was asked what he looks for when hiring a junior FDE, he said: proof you can work with people, such as building a community, volunteering, or even running a failed startup, because building a company teaches everything this role needs.

### Score yourself

| Question                                                              | Yes / Not yet |
| --------------------------------------------------------------------- | ------------- |
| Can I name the one KPI my current project moves, and who owns it?     |               |
| Have I shown a working prototype to a non-technical user this month?  |               |
| Do I have a plan to earn trust step by step, starting read-only?      |               |
| Does my solution fit into tools people already use?                   |               |
| Would I drop my favorite workflow if the data said it wasn't working? |               |

Three or more "not yet" answers? That's not a verdict, it's your curriculum.

---

## 7. The window is open, but not forever

Aater closed with a point for builders and founders. Right now the big AI labs are focused on large enterprises, so the **mid-market is wide open** for forward deployed companies. If you're building one, **go narrow and go deep**: a firm that has done 20 hospital revenue-cycle projects understands that business better than any single hospital's IT team. And own an outcome; don't just make yourself available.

He also warned that our industry always normalizes. The scarcity value of FDEs is enormous today, and it won't last forever. **The best time to build product judgment is now**, while it's still the rarest skill in the room.

---

## Let's talk

I'd love to hear where you stand:

- If you're an engineer: which of the five habits is hardest for you?
- If you're a product manager: what's stopping you from building the prototype yourself?
- If you're a founder: would you let an AI agent write to your systems, and what evidence would you need first?

Reach out on [LinkedIn](https://www.linkedin.com/in/mohcine-madkour-83a642b2) or at [mohcine@evaltrust.cloud](mailto:mohcine@evaltrust.cloud). And thank you to Aater Suleman for one of the most useful talks I've attended this year.

---

### Sources

- Aater Suleman, talk on forward deployed engineering, Dallas, November 5, 2026. Figures attributed to him (the 7.5-billion-dollar commitment, the 300,000 FDE estimate, 9–17 new hiring companies per week, the 1-in-8 ratio, the Dintash case and the PM ratios) are as he presented them.
- [Scaler: Forward Deployed Engineer Jobs Grew 1,165%](https://www.scaler.com/topics/forward-deployed-engineer-jobs-grew-1165-percent/) (Indeed data via Business Insider; Bloomberry analysis)
- [Paraform: How to hire a forward deployed engineer in 2026](https://www.paraform.com/insights/how-to-hire-a-forward-deployed-engineer)
- [Consultancy.uk: Accenture swoops for UK start-up Faculty](https://www.consultancy.uk/news/42712/accenture-swoops-for-uk-start-up-faculty-amid-ai-services-pivot)
