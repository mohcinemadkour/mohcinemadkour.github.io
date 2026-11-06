---
layout: post
title: "The People Stack: The Analytical People Skills Every Forward Deployed Engineer Needs, and the Techniques to Build Them"
date: 2026-11-05
description: "People skills are the scarcest part of the FDE role. A realistic, technique-by-technique guide to listening, stakeholder analysis, facilitation and trust-building, mapped to the five patterns from Aater Suleman's talk."
tags: [ForwardDeployedEngineering, PeopleSkills, Leadership, ChangeManagement, AICareers, Consulting]
categories: writing
related_posts: true
toc:
  beginning: true
---

> **Third in a series.** The [first article](/writing/2026/fde-think-like-a-product-manager/) covered why product thinking sits at the core of the forward deployed engineer (FDE) role. The [second](/writing/2026/fde-business-metrics-to-ai-metrics/) covered how to turn business goals into metrics. This one covers the skill that Aater Suleman, in his Dallas talk, kept returning to: **people skills**. Not as a personality trait, but as a set of techniques you can learn, practice and measure.

## 1. Why people skills are the real bottleneck

Aater made a claim that should worry every engineer: by the figure he cited, only about **1 in 8 engineers** qualifies to be an FDE today. The missing piece is rarely technical. He said that what is disappearing in this era is the wall between technologists and the business. In the cloud era, his engineers talked to the customer's engineers. **FDEs talk to the business**, and that requires a different kind of conversation.

He was blunt about it. In the Dintash story, the turning point came when the team did "one of the most difficult things an engineer has to do in their life: talk to human beings." When asked what he looks for in a junior FDE, he named an **engineer who knows how to talk** as the minimum baseline, and gave examples of the evidence he wants to see: being part of a community, volunteering, building a community, or even running a failed startup.

Here's the realistic part. Many strong engineers are introverts, and many were never taught any of this. The good news is that the people skills an FDE needs are **mostly analytical**. They are about observing carefully, asking structured questions, reading incentives, synthesizing what you heard and checking your understanding. If you can debug a distributed system, you can learn to debug a stakeholder conversation.

---

## 2. The analytical side of people skills

I find it useful to think of FDE people skills as four analyses you run continuously, the same way you'd monitor a production system.

### Lens 1: Who matters? (Stakeholder mapping)

Every AI project has more stakeholders than the person who signed the contract. Before any build, list everyone the system will touch and place them on a simple grid by **influence** over the project and **impact** the project will have on their daily work.

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 420" role="img" aria-label="Stakeholder grid with influence on the vertical axis and impact on daily work on the horizontal axis. Four quadrants: keep satisfied, partner closely, monitor, involve and listen" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">Stakeholder map: influence vs impact on daily work</text>
  <rect x="100" y="50" width="290" height="160" fill="#aebfd6"/>
  <rect x="400" y="50" width="290" height="160" fill="#e07b39"/>
  <rect x="100" y="220" width="290" height="160" fill="#e3e6ea"/>
  <rect x="400" y="220" width="290" height="160" fill="#e9a274"/>
  <text x="245" y="110" font-size="16" font-weight="700" text-anchor="middle" fill="#1b2433">Keep satisfied</text>
  <text x="245" y="135" font-size="12" text-anchor="middle" fill="#1b2433">CFO, CISO, compliance</text>
  <text x="245" y="155" font-size="12" text-anchor="middle" fill="#1b2433">Brief on outcomes and risk</text>
  <text x="545" y="110" font-size="16" font-weight="700" text-anchor="middle" fill="#1b2433">Partner closely</text>
  <text x="545" y="135" font-size="12" text-anchor="middle" fill="#1b2433">Workflow owner, team lead</text>
  <text x="545" y="155" font-size="12" text-anchor="middle" fill="#1b2433">Co-design, weekly reviews</text>
  <text x="245" y="280" font-size="16" font-weight="700" text-anchor="middle" fill="#1b2433">Monitor</text>
  <text x="245" y="305" font-size="12" text-anchor="middle" fill="#1b2433">Adjacent teams</text>
  <text x="245" y="325" font-size="12" text-anchor="middle" fill="#1b2433">Light updates</text>
  <text x="545" y="280" font-size="16" font-weight="700" text-anchor="middle" fill="#1b2433">Involve and listen</text>
  <text x="545" y="305" font-size="12" text-anchor="middle" fill="#1b2433">Front-line users</text>
  <text x="545" y="325" font-size="12" text-anchor="middle" fill="#1b2433">Interviews, shadowing, pilots</text>
  <text x="395" y="405" font-size="13" text-anchor="middle" fill="currentColor">Impact on their daily work →</text>
  <text x="60" y="215" font-size="13" text-anchor="middle" fill="currentColor" transform="rotate(-90 60 215)">Influence over the project →</text>
</svg>
</div>

The most common FDE mistake is to talk only to the top-left (the executives who issued the AI mandate) and ignore the bottom-right (the users who will decide whether the system is used). Aater's point about mandates coming from the boardroom makes this worse: the sponsor is excited, the users weren't asked.

### Lens 2: What does each person want? (Incentive analysis)

For each key stakeholder, write down three things: what they are measured on, what they're afraid of, and what they'd lose if your project succeeded. A billing coder may fear that automation means fewer jobs. A compliance officer is measured on zero findings, not on speed. A sponsor may need a visible win before budget season. Resistance that looks irrational almost always makes sense once you see the incentives.

### Lens 3: How does the work really happen? (Workflow observation)

What people say they do and what they actually do are different. The only reliable way to find out is to watch. This is where the real problem usually hides, the way Dintash found theirs one layer above the one they were asked to solve.

### Lens 4: How much do they trust us? (Trust tracking)

Trust is observable. Signs it's rising: people bring you problems you didn't ask about, invite you to internal meetings, give you access without a fight, and defend the project when you're not in the room. Signs it's falling: meetings get shorter, data requests stall, feedback gets vague. Track these signals as deliberately as you track latency.

---

## 3. How people skills map to the five patterns

Aater's five patterns from his portfolio were: **discover before you build, show it before they commit, earn the right to write, meet people where they work,** and **think in outcomes.** Every one of them is a people problem disguised as a process. Here's how I map the core people skills to each pattern, from my own experience:

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 360" role="img" aria-label="Heatmap showing which people skills matter most for each of the five patterns. Listening is critical for discovery; facilitation for showing prototypes; transparency for earning the right to write; empathy for meeting people where they work; candor for thinking in outcomes" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">People skills × the five patterns</text>
  <text x="20" y="48" font-size="12" fill="currentColor" opacity="0.7">Darker = more critical (author's assessment)</text>
  <g font-size="12" fill="currentColor" text-anchor="middle">
    <text x="245" y="80">Discover</text>
    <text x="340" y="80">Show</text>
    <text x="435" y="80">Earn write</text>
    <text x="530" y="80">Meet where</text>
    <text x="625" y="80">Outcomes</text>
  </g>
  <g font-size="13" fill="currentColor">
    <text x="20" y="117">Active listening</text>
    <text x="20" y="157">Questioning</text>
    <text x="20" y="197">Facilitation</text>
    <text x="20" y="237">Empathy</text>
    <text x="20" y="277">Transparency</text>
    <text x="20" y="317">Candor</text>
  </g>
  <g>
    <rect x="200" y="95" width="90" height="34" fill="#e07b39"/><rect x="295" y="95" width="90" height="34" fill="#e9a274"/><rect x="390" y="95" width="90" height="34" fill="#aebfd6"/><rect x="485" y="95" width="90" height="34" fill="#e9a274"/><rect x="580" y="95" width="90" height="34" fill="#aebfd6"/>
    <rect x="200" y="135" width="90" height="34" fill="#e07b39"/><rect x="295" y="135" width="90" height="34" fill="#e9a274"/><rect x="390" y="135" width="90" height="34" fill="#aebfd6"/><rect x="485" y="135" width="90" height="34" fill="#aebfd6"/><rect x="580" y="135" width="90" height="34" fill="#e9a274"/>
    <rect x="200" y="175" width="90" height="34" fill="#aebfd6"/><rect x="295" y="175" width="90" height="34" fill="#e07b39"/><rect x="390" y="175" width="90" height="34" fill="#e9a274"/><rect x="485" y="175" width="90" height="34" fill="#e9a274"/><rect x="580" y="175" width="90" height="34" fill="#e9a274"/>
    <rect x="200" y="215" width="90" height="34" fill="#e9a274"/><rect x="295" y="215" width="90" height="34" fill="#aebfd6"/><rect x="390" y="215" width="90" height="34" fill="#e9a274"/><rect x="485" y="215" width="90" height="34" fill="#e07b39"/><rect x="580" y="215" width="90" height="34" fill="#aebfd6"/>
    <rect x="200" y="255" width="90" height="34" fill="#aebfd6"/><rect x="295" y="255" width="90" height="34" fill="#e9a274"/><rect x="390" y="255" width="90" height="34" fill="#e07b39"/><rect x="485" y="255" width="90" height="34" fill="#aebfd6"/><rect x="580" y="255" width="90" height="34" fill="#e9a274"/>
    <rect x="200" y="295" width="90" height="34" fill="#aebfd6"/><rect x="295" y="295" width="90" height="34" fill="#aebfd6"/><rect x="390" y="295" width="90" height="34" fill="#e9a274"/><rect x="485" y="295" width="90" height="34" fill="#aebfd6"/><rect x="580" y="295" width="90" height="34" fill="#e07b39"/>
  </g>
  <rect x="200" y="340" width="14" height="14" fill="#e07b39"/><text x="220" y="352" font-size="12" fill="currentColor">Critical</text>
  <rect x="300" y="340" width="14" height="14" fill="#e9a274"/><text x="320" y="352" font-size="12" fill="currentColor">Important</text>
  <rect x="410" y="340" width="14" height="14" fill="#aebfd6"/><text x="430" y="352" font-size="12" fill="currentColor">Supporting</text>
</svg>
</div>

Now, pattern by pattern, the techniques.

---

## 4. Pattern 1: Discover before you build

**The people challenge.** People can't tell you what they need, only what bothers them. And they'll often tell you what they think you want to hear. Aater said about 70% of an AI project's effort now goes into planning. Most of that planning is conversation.

### Technique: contextual inquiry (watch, then ask)

Don't start with a meeting room. Sit with the person while they do the work. Ask them to narrate what they're doing and why. Note every workaround, spreadsheet, sticky note and "I just know to check this." Those are your requirements.

### Technique: ask about the past, not the future

Hypothetical questions get hypothetical answers. Rob Fitzpatrick's book _The Mom Test_ makes this point well: ask about specific things people already did, not about what they would do.

| Instead of…                       | Ask…                                              |
| --------------------------------- | ------------------------------------------------- |
| "Would an AI assistant help you?" | "Walk me through the last time this went wrong."  |
| "What features do you want?"      | "What did you do about it? How long did it take?" |
| "Is this a big problem?"          | "What have you already tried? What did it cost?"  |
| "Would you use this?"             | "Who else deals with this? Can you introduce me?" |

### Technique: Five Whys

When someone names a problem, ask "why" until you reach a cause you can actually act on. "Claims get denied" → why? "Missing documentation" → why? "Doctors don't know what the payer requires" → why? "The rules change and nobody tells them." Now you know the real problem, and it might not even need a model.

### Technique: the active listening loop

Aater's line, "listen to understand, not to respond," is a technique, not a slogan. The loop is: **listen fully, paraphrase what you heard, ask whether you got it right, then probe deeper.**

<div style="margin:1.5rem 0;">
<svg viewBox="0 0 720 300" role="img" aria-label="Cycle diagram: listen, paraphrase, confirm, probe, then back to listen" style="width:100%;height:auto;font-family:inherit;">
  <text x="20" y="28" font-size="18" font-weight="700" fill="currentColor">The active listening loop</text>
  <circle cx="360" cy="165" r="95" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="2"/>
  <rect x="290" y="45" width="140" height="50" rx="25" fill="#e07b39"/>
  <text x="360" y="76" font-size="15" font-weight="700" text-anchor="middle" fill="#1b2433">1. Listen</text>
  <rect x="470" y="140" width="160" height="50" rx="25" fill="#e9a274"/>
  <text x="550" y="171" font-size="15" font-weight="700" text-anchor="middle" fill="#1b2433">2. Paraphrase</text>
  <rect x="290" y="235" width="140" height="50" rx="25" fill="#8aa6c8"/>
  <text x="360" y="266" font-size="15" font-weight="700" text-anchor="middle" fill="#1b2433">3. Confirm</text>
  <rect x="90" y="140" width="160" height="50" rx="25" fill="#aebfd6"/>
  <text x="170" y="171" font-size="15" font-weight="700" text-anchor="middle" fill="#1b2433">4. Probe deeper</text>
  <text x="640" y="110" font-size="12" text-anchor="end" fill="currentColor" opacity="0.8">"So what I'm hearing is…"</text>
  <text x="640" y="230" font-size="12" text-anchor="end" fill="currentColor" opacity="0.8">"Did I get that right?"</text>
  <text x="80" y="230" font-size="12" fill="currentColor" opacity="0.8">"Tell me more about…"</text>
  <text x="80" y="110" font-size="12" fill="currentColor" opacity="0.8">Don't plan your reply</text>
</svg>
</div>

Useful phrases:

- "So what I'm hearing is… Did I get that right?"
- "What would have to be true for this to be solved?"
- "It sounds like this is frustrating because…"
- "What's the part of this nobody talks about?"

Then **stay quiet**. Silence after a question feels awkward, and that awkwardness is where people tell you the real story.

### Technique: synthesize like an analyst

After five to ten interviews, write each observation on its own card and group them by theme (an affinity map). Count how many people raised each theme, note the exact words they used, and rank the pains by frequency and cost. Bring the synthesis back to the stakeholders: "Here's what eight of you told me. Did I miss anything?" That single meeting builds more trust than any demo.

**You know it's working when** people say "nobody has asked us this before," and you find the real problem one layer away from the one you were given.

---

## 5. Pattern 2: Show it before they commit

**The people challenge.** Non-technical people can't evaluate a requirements document, but they react instantly to something they can see and click. Aater credited one founder with opening his eyes to showing up at the first call with a prototype, and described a company that offers unlimited revisions, because every time a non-technical customer sees the product, their imagination adjusts a little.

### Technique: show three options, not one

One prototype invites a yes or no. Three invite comparison: "Which of these is closest to how you think about it?" People are much better at choosing than at specifying. Make the options genuinely different, not three shades of the same design.

### Technique: facilitate the demo, don't present it

- **Hand over the controls.** Let the user drive while you watch where they hesitate.
- **Ask for the failure case:** "What would make this useless to you?" It surfaces deal-breakers early.
- **Ask about Monday:** "If you had this tomorrow, what would you do differently?" If they can't answer, it doesn't fit their workflow yet.
- **Capture feedback live**, in their words, and read it back at the end.

### Technique: make change cheap and visible

Treat each piece of feedback as a gift, not a scope dispute. Show the updated version quickly, ideally in the next meeting. When people see their own words turn into the product, they become co-owners of it, which is the best adoption strategy there is.

**You know it's working when** stakeholders start correcting each other about how the work really happens, and ask when they can try it with real data.

---

## 6. Pattern 3: Earn the right to write

**The people challenge.** Letting AI change real records, accounts or production systems is a high-stakes decision, and the people who approve it are paid to say no. Aater's advice: change the mindset from "they won't give us permission" to "we have to earn it." By default, they won't trust you, and that's reasonable.

### Technique: treat the gatekeeper as a design partner

The CISO, compliance officer or system owner who blocks you knows exactly what could go wrong. Invite them in early: "You know the risks here better than anyone. What would you need to see before you'd be comfortable?" Their answer becomes your acceptance criteria. You've turned an opponent into a co-author.

### Technique: run a pre-mortem together

Ask the group: "Imagine it's six months from now and this project failed badly. What happened?" Write down every answer. People who would never raise a concern in a normal meeting will happily describe an imaginary disaster. Each answer becomes a risk you design against and a test you'll run.

### Technique: radical transparency

Share failures as quickly as successes. When the system gets something wrong in read-only or shadow mode, bring that case to the stakeholders yourself, with what you're doing about it. Nothing destroys trust faster than a gatekeeper discovering an error you didn't mention. Nothing builds it faster than you raising it first.

### Technique: let the evidence argue for you

Aater's approach was to avoid arguing about access at all: show what the system _would_ have done next to what people actually did, and let the comparison make the case. Agree on the thresholds up front, show progress against them in every review, and let the stakeholders decide when to move to the next step.

**You know it's working when** the gatekeeper starts presenting your evidence to their own leadership.

---

## 7. Pattern 4: Meet people where they work

**The people challenge.** People are busy, tired of new tools and often skeptical. Aater quoted a board member from the oil and gas industry: the last words they want to hear from a vendor are "platform" and "migration." He described a company selling AI "contractors" to HVAC businesses that stopped asking for API keys and asked for what contractors normally get: an email, a Slack seat and a desktop.

### Technique: shadow before you design

Spend real time in the users' environment and note which tools they keep open all day. The AI should appear there, not in a new tab they have to remember.

### Technique: treat resistance as data

When someone pushes back, ask "What worries you about this?" and listen properly. Resistance usually points to a real cost you haven't seen: extra clicks, a loss of control, a fear for their job. Write it down and address it in the design. Aater's line applies here too: listen to understand, not to respond.

### Technique: recruit champions

In every team, find one or two respected people who like to try new things. Involve them in the design, give them early access, and let them show their peers. People trust a colleague's "this saved me an hour" far more than an engineer's slide.

### Technique: use a change framework to diagnose where people are stuck

A simple model like Prosci's **ADKAR** helps you work out why adoption is stalling: do people have **Awareness** of why the change is happening, the **Desire** to take part, the **Knowledge** of how, the **Ability** to do it in their real day, and **Reinforcement** so it sticks? Each gap calls for a different fix: explanation, incentives, training, workflow redesign or recognition. Don't train people who don't yet see why it matters.

**You know it's working when** users stop calling it "the AI tool" and just call it part of how they work.

---

## 8. Pattern 5: Think in outcomes

**The people challenge.** Outcome thinking means saying hard things: "This isn't working," "Your metric didn't move," or "We should stop." Aater's advice, "don't be a workflow hugger," requires the social courage to walk away from your own work.

### Technique: the weekly value review

Hold a short, regular meeting with the workflow owner around one question: did the number move this week, and why? Keep it to the KPI, the leading indicators and the next action. Regular, boring honesty prevents dramatic surprises.

### Technique: deliver bad news early, with a plan

A simple structure: **what we saw, what we think it means, what we recommend.** For example: "Usage is up, but the cost metric has been flat for three weeks. We think we're automating the wrong step. We'd like to interview the billing team this week and decide by Friday whether to switch workflows." This is exactly what turned Dintash's 15% plateau into 40%.

### Technique: agree on the kill criterion before you start

It's far easier to stop a project when everyone agreed in advance what failure looks like. Write it on the first page: "If the leading indicators don't move in four weeks, we stop or switch." Then the conversation becomes a check against an agreement, not a personal judgment.

### Technique: celebrate bright spots publicly

Aater cited the book _Switch_ and its idea of bright spots: small successes that fuel larger change. When something works, make the people who did it visible to their leadership. Give the credit away. It's the cheapest, most powerful way to build momentum for the next workflow.

**You know it's working when** the client starts asking "what's the next workflow?" before you do.

---

## 9. Team player and community builder

### In the pod

Aater predicts the FDE role will spread across **pods**: a domain expert, a product manager, an AI strategist and an engineer. That makes being a team player a hard requirement, not a nice-to-have. In practice it means:

- **Make your thinking visible.** Write short notes on what you learned, decided and still don't know. A pod moves at the speed of its shared understanding.
- **Respect other kinds of expertise.** The domain expert's "that would never work here" is worth more than your best benchmark.
- **Hand off cleanly.** Leave every engagement documented well enough that someone else could pick it up tomorrow.

### In the community

Aater named community work among the clearest signals he looks for when hiring, and it makes sense: organizing a meetup, mentoring or volunteering is practice at everything above. You learn to listen to people who don't owe you their time, run a room, handle disagreement, and deliver something people actually show up for.

Practical ways to build that evidence:

- **Volunteer to run or speak at a local meetup.** I'm organizing an AI meetup community in Rabat for exactly this reason.
- **Mentor someone** a step or two behind you. Explaining clearly is a core FDE skill.
- **Write and teach in public**, like this series, and invite disagreement.
- **Join a nonprofit project** where you have to work with non-technical stakeholders on a real problem.

---

## 10. A realistic 30-day practice plan

None of this changes overnight, and none of it requires becoming an extrovert. It requires deliberate practice.

| Week  | Focus            | Practice                                                                                                                 |
| ----- | ---------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **1** | Listening        | Run three conversations using only the listening loop. Count how often you interrupted.                                  |
| **2** | Questioning      | Interview three people about a real work problem using past-behavior questions and Five Whys. Synthesize the themes.     |
| **3** | Facilitation     | Build three quick options for one problem and run a 20-minute session where the user drives.                             |
| **4** | Candor and trust | Run a pre-mortem on a current project, and give one piece of honest bad news using the "saw, mean, recommend" structure. |

### Score yourself

| Skill                                                                       | 1 (rarely) to 5 (always) |
| --------------------------------------------------------------------------- | ------------------------ |
| I can paraphrase what a stakeholder said to their satisfaction              |                          |
| I ask about past behavior, not hypothetical future use                      |                          |
| I know who the real gatekeepers are and what they fear                      |                          |
| I let users drive demos and watch where they struggle                       |                          |
| I raise bad news early, with a recommendation                               |                          |
| I give credit away and make others' wins visible                            |                          |
| I have recent evidence of community work: speaking, mentoring, volunteering |                          |

Low scores aren't a verdict. They're your roadmap.

---

## Let's talk

Aater's talk convinced me that the hardest part of deploying AI is not the AI. It's earning the trust of people whose work is about to change. I'd love to hear from you: which of these techniques do you already use, and which feels hardest? If you're an engineer moving toward an FDE role, what's holding you back on the people side?

Reach me on [LinkedIn](https://www.linkedin.com/in/mohcine-madkour-83a642b2) or at [mohcine@evaltrust.cloud](mailto:mohcine@evaltrust.cloud).

---

### Sources and notes

- Aater Suleman, talk on forward deployed engineering, Dallas, November 5, 2026: the 1-in-8 figure, the five patterns, the Dintash case, "listen to understand, not to respond," what he looks for in a junior FDE, forward deployed pods, and the references to _Switch_ and bright spots.
- Rob Fitzpatrick, _The Mom Test_ (2013), on asking about past behavior in customer interviews.
- Prosci's ADKAR model of individual change: Awareness, Desire, Knowledge, Ability, Reinforcement.
- The skills-by-pattern heatmap reflects the author's assessment, not survey data.
