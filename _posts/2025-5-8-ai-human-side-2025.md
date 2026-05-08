# The Human Side of AI: What the Data Reveals — and What Businesses Are Getting Wrong

*By Mohcine Madkour, PhD | Senior AI/ML Engineer & Architect*

---

The 2025 AI Impact Report from House 337 and Savanta surveyed over 6,000 people across the US, UK, Canada, and the Netherlands. The headline findings are worth reading slowly, because they cut through a lot of noise: **87% of people have heard of Generative AI, but only 36% have knowingly used it.** And of those using it at work, 62% say their employer expects them to figure it out on their own.

That gap — between awareness and real adoption, between leadership enthusiasm and ground-level support — is exactly where I spend my working days. Let me share what I think this report actually means for businesses trying to build AI that works.

---

## Problem 1: High Visibility, Low Literacy — and a Trust Crisis Waiting to Happen

The report surfaces something subtle but critical: people interact with AI constantly without knowing it. Recommendation engines, customer support bots, fraud detection — it's everywhere, invisible. But when you ask people if they've *knowingly* used Generative AI, the number drops sharply.

This creates a dangerous asymmetry. Businesses are deploying AI across customer touchpoints while their users don't understand what they're interacting with. The report finds that **75% of people want to know when content is AI-generated** — not obsessively, but meaningfully, especially when stakes are high.

**What this means for your business:** If your AI-powered product doesn't disclose its nature at the right moments, you're not just missing a transparency opportunity — you're accumulating a trust debt. When something eventually goes wrong (and it will), users who didn't know they were interacting with AI will feel deceived, not just disappointed.

The fix isn't slapping a disclaimer on everything. It's designing AI disclosure as a product feature, not a legal obligation. I've seen this done well at the system architecture level: confidence-tiered outputs that automatically escalate to human review or flag uncertainty, rather than confidently serving a wrong answer to a customer.

---

## Problem 2: The Workplace AI Divide Is a Productivity Leak

Here's a number that should alarm every executive: **only a third of employees report receiving training** on the AI tools their company is deploying, yet 76% say those tools improve their productivity once they actually use them.

The report is clear — writing (47%), editing (47%), and data analysis (40%) are already embedded in core workflows. But most people got there on their own, through trial and error, YouTube videos, and peer advice. The ROI on structured AI enablement is sitting there, unextracted.

Meanwhile, the gap widens by age. Younger adults (18–34) are using AI across a much broader range of tasks. Older workers, who often hold institutional knowledge and senior judgment, are the most cautious group — and the least supported. **63% of people 55+ believe AI should not be relied upon to make decisions.** That's not Luddism; that's wisdom applied to tools they don't yet understand well enough to trust. And companies are leaving them without the context they need to calibrate that judgment.

**What this means for your business:** Your AI strategy isn't just a technology investment — it's a change management problem. If you deploy a new LLM-powered workflow tool and call it done, you've bought a Ferrari and handed the keys to someone who learned to drive on a tractor. The performance gap you're measuring isn't the AI's fault; it's the adoption gap.

I've built AI systems for surgical robotics teams, industrial fleet diagnostics, and clinical decision support. In every case, the technical architecture was 40% of the challenge. The other 60% was designing the human interaction layer: how do users build appropriate trust, how do they know when to override the system, how does the system communicate its own uncertainty?

---

## Problem 3: People Are Still in "Knowing" Mode — Not "Doing" Mode

The report draws a sharp distinction between knowledge-driven AI tasks (search, research, learning) and action-driven tasks (scheduling, purchasing, executing). Search dominates at 62%. Purchasing sits at 24%. The gap signals something important: **we are still in an early integration phase**, and most users haven't built enough trust to hand consequential actions over to AI.

This maps directly onto what I see in enterprise deployments. Organizations rush to automate decisions — flagging fraud, routing support tickets, prioritizing surgical maintenance alerts — before users have developed enough experience with the system to know when to trust it and when to push back. The result is either over-reliance (users rubber-stamp AI outputs without scrutiny) or under-reliance (users ignore the system entirely because they had one bad experience).

**What this means for your business:** If you're building agentic AI — systems that take real-world actions on behalf of users — you need to design the trust-building arc, not just the capability. That means starting with read-only recommendations before you move to autonomous execution. It means making the AI's reasoning legible, not just its outputs. It means building in graceful degradation when the system is uncertain.

The shift from "AI tells me things" to "AI does things for me" is the next major adoption frontier. The businesses that design for that transition thoughtfully will capture enormous competitive advantage. The ones that just flip the automation switch will generate a wave of incidents that set their AI programs back two years.

---

## Problem 4: Concern Is Consistent Across All Age Groups — But the Conversation Isn't

One finding I keep returning to: ethical concern about AI is **consistent across all ages** — 51% of 18–34 year-olds, 52% of 35–54 year-olds, and 56% of over-55s report ethical concerns that discourage AI use. It's not just older users who are worried. Younger users are worried too; they're just less likely to let it stop them.

The top concerns: data collection and ownership (54%), security and manipulation risk (47%), algorithmic accuracy and bias (45%), lack of transparency (39%), and misalignment with human values (45%).

These aren't abstract philosophical worries. They're concrete, operational concerns — and most of them are addressable with good engineering and honest communication.

**What this means for your business:** Your AI governance conversation needs to happen in the open, not just in the boardroom. Users want to know not just *that* your AI is safe, but *how* you've thought about fairness, what happens when it's wrong, and who is accountable when it causes harm. The companies that treat AI ethics as a marketing checkbox will be exposed. The ones that build it into their product architecture — explainability, bias monitoring, human oversight loops — will earn durable trust.

---

## What I Can Help You With

These problems are solvable. I've spent 16 years building production AI systems at the intersection of high-stakes domains — surgical robotics at Intuitive Surgical, connected fleet diagnostics at Cummins, clinical risk prediction at UF Health. The patterns repeat across industries: the gap between AI potential and AI reality almost always comes down to trust architecture, adoption design, and evaluation rigor.

If your organization is navigating any of the following, I'd welcome a conversation:

- **AI strategy and architecture** — how to design systems your users will actually trust and use
- **Agentic AI evaluation** — how to measure whether your AI agents are doing what you think they're doing
- **RAG and knowledge systems** — building retrieval-augmented systems that are accurate, auditable, and production-ready
- **Predictive maintenance and industrial AI** — applying ML to equipment health, fleet diagnostics, and operational reliability
- **AI enablement** — helping your teams develop the literacy to work effectively alongside AI systems

---

## Let's Connect

I'm always interested in conversations with leaders and builders who are thinking seriously about the human side of AI — not just the technology, but what it takes to make it actually work for real people in real organizations.

- **LinkedIn:** [linkedin.com/in/mohcinemadkour](https://www.linkedin.com/in/mohcinemadkour)
- **GitHub:** [github.com/mohcinemadkour](https://github.com/mohcinemadkour)
- **Website:** [mohcinemadkour.github.io](https://mohcinemadkour.github.io)

If you're working on a problem where AI could make a real difference — or where an AI deployment isn't delivering what was promised — reach out. The most interesting work I do starts with someone who already tried the obvious answer and found it wasn't enough.

---

*Mohcine Madkour, PhD, is a Senior AI/ML Engineer and Architect with 16+ years of experience building production AI systems in surgical robotics, industrial IoT, and clinical healthcare. He is based in the Dallas–Fort Worth area and available for consulting, fractional AI leadership, and advisory engagements.*
