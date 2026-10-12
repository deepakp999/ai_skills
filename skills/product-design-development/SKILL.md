---
name: product-design-development
description: End-to-end product development coach (Ulrich/Eppinger/Yang method) - opportunity, customer needs, specs, concept generation/selection/testing, architecture, prototyping, economics, project plan. Use for any physical, digital, service or AI product idea, even when the user just says "I have a product idea" or "help me pick a design".
---

# Product Design & Development

A structured, customer-first method for turning an idea or problem into a well-defined product, adapted from *Product Design and Development* (Ulrich, Eppinger & Yang, 7th ed.). It works for physical products, software/digital products, AI agents, internal tools, services and product-service systems.

The core belief behind the method: **most product failures are decided at the front end** — the wrong opportunity, misunderstood needs, vague specs, or a concept chosen by the loudest voice. So the method front-loads structured thinking, keeps the customer's voice traceable all the way to specs, and makes every big decision with an explicit, reviewable artifact (a list, a matrix, a model).

## How to run this skill

1. **Locate the user in the journey.** Ask (or infer) where they are: raw idea? known problem? concept already chosen? Don't restart a mature project at Phase 0 — jump to the stage that's actually open, but quickly check that upstream artifacts exist (e.g., "what customer needs drive these specs?"). Missing upstream work is the most common root cause of downstream trouble; name it gently.
2. **Classify the product type** (see "Process variants") — it changes which steps matter most.
3. **Work one stage at a time, producing its artifact.** Each stage below has a short method and a deliverable template. Fill templates with the user's real content; where you lack data, propose plausible draft entries clearly marked `[assumption — validate]` rather than stalling.
4. **Close each stage with a gate check** (the "Reflect" step the book ends every method with): What did we learn? What's still assumed? Is the output good enough to move on? Then suggest the next stage.
5. **Keep a running "contract book"** — the consolidated record of mission, needs, specs, chosen concept, test results, economics and plan. Offer to compile it into a document when the user has several stages done.

Be a sharp coach, not a form-filler: challenge solution-shaped "needs", too-narrow concept sets, and selections that ignore the matrix. Use tables generously — the method is matrix-driven.

## The journey at a glance

| Phase | Stage | Key question | Artifact |
|---|---|---|---|
| 0 Planning | 1. Opportunity identification | Which opportunity is worth pursuing? | Opportunity tournament + Real-Win-Worth-it screen |
| 0 Planning | 2. Product planning | Does it fit the portfolio; what's the scope? | Mission statement |
| 1 Concept dev. | 3. Customer needs | What must the product do for users? | Hierarchical, weighted needs list |
| 1 | 4. Target specifications | How will we measure success? | Needs–metrics matrix + benchmark + ideal/marginal values |
| 1 | 5. Concept generation | What are all the ways to do it? | Function decomposition, concept classification tree, combination table |
| 1 | 6. Concept selection | Which concept wins, objectively? | Screening matrix → scoring matrix |
| 1 | 7. Concept testing | Do real customers want it? | Test plan + purchase-intent forecast |
| 1 | 8. Final specifications | What can we actually achieve? | Trade-off-resolved spec sheet |
| 2 System design | 9. Product architecture | How do functions map to chunks/modules? | Schematic, clusters, interaction list |
| 2–3 | 10. Design-for-X | User experience, environment, manufacturing/cost | ID/UX plan, DFE, DFM/cost-of-goods |
| 3–4 | 11. Prototyping & robust design | What must we learn by building? | Prototype plan, robustness experiment |
| Throughout | 12. Economics | Is it worth it; what are the levers? | NPV model + sensitivities |
| Throughout | 13. Project plan & IP | How do we deliver; what to protect? | DSM / critical path, risk plan, IP strategy |

Phases 4–5 (testing & refinement, production ramp-up/launch) are execution of the plan; support them with prototyping, testing and project management stages.

---

## Process variants — pick before you start

| Type | What changes |
|---|---|
| **Market-pull** (default) | Start from market opportunity and needs; full process. |
| **Technology-push** | Start with a technology; spend extra effort finding the market where it truly beats alternatives. Verify needs before committing. |
| **Platform / derivative** | Architecture and reuse of an existing platform dominate; concept generation is narrower. |
| **Process-intensive** | Production process constrains product from day one. |
| **Customized** | Design is parameterized; the process becomes configuring variants. |
| **High-risk** | Identify biggest technical/market risks early; prototype and test them first. |
| **Quick-build / digital / software / AI** | Rapid build–test spirals: plan → design → build → test, repeated; release in increments. Still do needs + specs + concept selection up front — they're cheap and prevent building the wrong thing fast. |
| **Product-service system** | Design the service concept and process flow alongside the product (see Stage 10d). |
| **Complex systems** | Decompose into subsystems; architecture and interface management dominate. |

For digital/AI products translate physical vocabulary: "manufacturing cost" → cloud/inference/support cost per user; "assembly" → integration effort; "chunks" → services/modules/agents; "physical prototype" → clickable mock, Wizard-of-Oz, or working spike; "tooling" → infrastructure and data pipelines.

---

## Stage 1 — Opportunity identification

Treat it as a **tournament**: generate many raw opportunities, filter hard, develop the few survivors.

1. **Charter** — state the goal, the arena (markets, technologies, business model), and what's off-limits.
2. **Generate many** — sources: customer frustrations ("bug lists"), lead/extreme users, trends (social, technical, regulatory), capabilities you uniquely hold, imitate-and-improve elsewhere, mining existing data, cool new tech in search of a problem. Aim for dozens to hundreds.
3. **Screen** — quick, cheap cuts (multi-voting, simple criteria). Keep variety.
4. **Develop** — for the survivors, do a little research: market size, users, competitors, feasibility.
5. **Select with Real–Win–Worth it:**
   - *Is it real?* Real need, ability to pay, sufficient market, can the product be made?
   - *Can we win?* Competitive advantage (tech, IP, brand, distribution), can we beat competitors' timing, do we have the team/resources?
   - *Is it worth doing?* Expected return vs. risk, fit with strategy.
6. **Reflect.**

Template:
```
| Opportunity | Source | Real? | Win? | Worth it? | Verdict / next learning |
```
Categorize opportunities on a 2×2 of *solution knowledge* (known/new) × *need/market knowledge* (known/new): horizon 1 = incremental, 2 = new market or new solution, 3 = both new (exploratory, high risk). A healthy portfolio mixes them.

## Stage 2 — Product planning & mission statement

Evaluate candidate projects against: competitive strategy (tech leadership, cost leadership, customer focus, imitation), market segmentation, technology trajectory (S-curves — is the tech maturing?), and the product-platform plan. Balance the portfolio across breakthrough / new platform / derivative / support projects. Check aggregate capacity: don't start more than the team can staff.

**Mission statement** (the deliverable):
```
Product description: (one sentence)
Benefit proposition: (key reasons a customer buys/uses it)
Key business goals: (timing, cost, quality, share, adoption, revenue)
Primary market: 
Secondary markets:
Assumptions & constraints: (platform, technology, regulatory, budget)
Stakeholders: (buyers, users, ops, support, sales, suppliers, regulators, ...)
```

## Stage 3 — Identify customer needs

Goal: a high-quality information channel from customers straight to the people who design. Five steps:

1. **Gather raw data** — interviews (one-on-one, 60 min, in the use environment works best), focus groups, and above all **observing the product in use**. ~10–20 interviews usually surface 90%+ of needs for a segment; go to 30+ for a diverse market. Include **lead users** (ahead of the trend, invent workarounds) and **extreme users** (unusual conditions — reveal latent needs). Prompts: "When and why do you use…?", "Walk me through a typical use", "What do you like/dislike about current solutions?", "What would you improve?", watch for workarounds, hacks and complaints. Document verbatim statements, photos, video, notes.
2. **Interpret raw data into need statements.** Rules:
   - Express *what*, not *how* ("The screwdriver provides plenty of power" not "has a 6V motor").
   - As specific as the raw data.
   - Positive phrasing, not negative.
   - As an attribute of the product ("The app…", "The truck…").
   - Avoid "must" and "should" (importance comes later).
3. **Organize into a hierarchy** — write each need on a card, cluster by similarity (affinity), name each group with a primary need; members become secondary (and tertiary) needs. Don't force fixed categories in advance.
4. **Establish relative importance** — team consensus, or better, a customer survey (1–5 scale: undesirable … critical). Flag **latent needs** (customers would delight at but can't articulate) with `!` and **exceptionally important** with `*`.
5. **Reflect** — Did we reach all segment types? Lead users? What surprised us? Are there needs we can't yet address?

Template:
```
| # | Primary need | Secondary need statement | Source (quote/obs.) | Importance 1–5 | Latent? |
```
Push back when users give "needs" that are really features; ask "what would that let you do?"

## Stage 4 — Target specifications

A specification = **metric + value + unit** (e.g., "Average time to assemble < 75 s"; "P95 response latency < 2 s"). Specs translate the language of the customer into precise, measurable design targets. Set them twice: *target* now (aspirational), *final* after concept selection (Stage 8).

1. **List metrics** — each need gets ≥1 metric that ideally directly reflects how well it's satisfied. Metrics should be dependent variables (outcomes, not design choices), practical to measure, and include popular market criteria. Some needs can only be checked subjectively — use a "subjective" metric with a test panel.
2. **Needs–metrics matrix** — rows = needs, columns = metrics, mark relationships. Every need should be covered; every metric should trace to a need (this is the core of QFD/House of Quality).
3. **Competitive benchmarking** — measure competitors on each metric; also chart how competitors are *perceived* on each need. Gaps between perception and metric reveal errors or opportunities.
4. **Set ideal and marginally acceptable values** — expressed as: at least X, at most X, between X and Y, exactly X, or a set of discrete values. Use benchmarks to position.
5. **Reflect** — are we going to win on the dimensions customers care most about? Are specs gaming-proof?

Templates:
```
Metrics list:
| Metric # | Need #s | Metric | Importance | Unit |

Benchmark:
| Metric | Unit | Competitor A | Competitor B | Our current | Marginal | Ideal |
```

## Stage 5 — Concept generation

A concept = approximate description of technology, working principle and form. Generate **many** (dozens to hundreds); expect 5–20 to merit serious selection.

1. **Clarify the problem** — black-box function diagram (inputs/outputs of energy, material, signal/data), then **functional decomposition** into sub-functions. Identify the *critical subproblems* to focus on first. Alternatives: decompose by user action sequence (great for digital/service products) or by key customer needs.
2. **Search externally** — interview lead users, consult experts, search patents, literature, open-source projects, and benchmark related products (including from other industries solving analogous sub-functions).
3. **Search internally** — individual then group brainstorming. Rules: suspend judgment, go for quantity, welcome wild ideas, build on others, use sketches/mockups. Hints: make analogies ("what else does this?"), wish and wonder ("what if…"), use related stimuli, use unrelated stimuli, set quantitative goals, use the gallery method, try TRIZ-style contradiction thinking.
4. **Explore systematically**
   - **Concept classification tree**: split the solution space for a sub-function into distinct branches (e.g., energy source: electrical / chemical / mechanical / human). Lets you prune unpromising branches, spot neglected ones, and allocate effort deliberately.
   - **Concept combination table**: columns = sub-functions, rows = solution fragments; combine one per column into whole concepts. Not every combination is feasible — it's a prompt for creative synthesis.
5. **Reflect** — Have we explored the whole space? Are there alternative decompositions? Did we fully use outside sources? Did everyone's ideas get in?

Template:
```
Combination table
| Sub-function 1 | Sub-function 2 | Sub-function 3 |
| option a       | option x       | option p       |
| option b       | option y       | option q       |
→ Concept C1 = a+y+p : description / sketch
```

## Stage 6 — Concept selection

Two-stage, matrix-driven. Selection criteria come from the customer needs (plus business criteria like cost, risk, time-to-market).

**A. Concept screening (Pugh method)** — coarse narrowing
1. Prepare the matrix: criteria rows, concept columns, choose a **reference** concept (industry standard or a strong straightforward option).
2. Rate each concept vs. the reference on each criterion: `+` better, `0` same, `–` worse.
3. Sum +, 0, –; net score; rank.
4. **Combine and improve** — can a bad feature of a good concept be fixed by borrowing from another? Merge complementary concepts.
5. Select concepts to advance (often several).
6. Reflect.

**B. Concept scoring** — finer, weighted
1. Weight each criterion (sum 100%); break broad criteria into sub-criteria when needed.
2. Rate 1–5 relative to a reference point (may differ per criterion; 3 = same as reference).
3. Weighted score = Σ (rating × weight); rank.
4. Combine/improve again; select; check sensitivity — would small weight/rating changes flip the winner? If so, the decision is uncertain; consider testing both.
5. Reflect: Is the team comfortable? If the winner "feels wrong", a criterion is missing — find it.

Templates:
```
Screening
| Criterion | Ref | C1 | C2 | C3 |
| Ease of use | 0 | + | 0 | – |
| Sum + / 0 / – | | | | |
| Net / Rank / Continue? | | | | |

Scoring
| Criterion | Weight | C1 rating | C1 weighted | C2 rating | C2 weighted |
| Total score / Rank / Continue? |
```

## Stage 7 — Concept testing

Get direct responses from target customers to a description of the concept.

1. **Define the purpose** — which concept to pursue? how to improve it? estimate sales? go/no-go?
2. **Choose the survey population** — reflects target market; size grows with the stakes and the uncertainty.
3. **Choose the format** — face-to-face, phone, online, intercept.
4. **Communicate the concept** — verbal description → sketch → photo/rendering → storyboard → video → simulation/interactive mock → working prototype. Match fidelity to purpose; avoid overselling.
5. **Measure response** — typically a 5-point purchase-intent scale ("definitely would / probably would / might or might not / probably not / definitely not"), plus reasons and comparisons.
6. **Interpret** — forecast: **Q = N × A × P**, where N = number of potential purchases (or adoptions) per period, A = fraction aware and able to get it, P = probability of purchase given awareness = C_def × F_def + C_prob × F_prob (F = survey fractions; calibration C commonly ~0.1–0.5 for "definitely" and ~0–0.25 for "probably"; tune to your domain). For internal tools, read N as eligible users and P as adoption likelihood.
7. **Reflect** — consider why respondents might over/under-state intent; what would change the forecast most?

## Stage 8 — Final specifications

Now that a concept exists, refine targets into achievable finals:
1. Build technical models (analytical, simulation, quick physical/functional prototypes) of the concept to predict metric values for design variables.
2. Develop a preliminary cost model (bill of materials or, for digital, cost-per-user/transaction).
3. Refine specs, making trade-offs — plot competitive maps (metric A vs. metric B with competitors and technical feasibility frontier).
4. Flow specs down to subsystems where needed.
5. Reflect.

Template: `| Metric | Unit | Target (marginal/ideal) | Final value | Trade-off rationale |`

## Stage 9 — Product architecture

How functional elements map onto physical (or software) **chunks**, and how chunks interact. The key choice: **modular** (each chunk implements a few functions, well-defined interfaces — slot, bus, or sectional modular) vs. **integral** (functions spread across chunks, tight coupling, optimized performance).

Implications: modular eases product change, variety, component standardization, parallel development and postponement; integral can win on performance, size, cost at scale.

Method:
1. **Schematic** — functional and physical elements and their flows (energy, material, signal/data).
2. **Cluster into chunks** — considerations: geometric integration and precision, function sharing, supplier/team capabilities, similarity of production technology, localization of change, accommodating variety, enabling standardization, portability of interfaces.
3. **Rough geometric layout** (or deployment/component diagram for software).
4. **Identify fundamental and incidental interactions** between chunks; manage them with interface specs and a DSM.

Also address: **delayed differentiation** (put variety-driving elements in a few chunks, near the end of the supply chain/pipeline), and **platform planning** — a differentiation plan (how variants differ on attributes customers care about) vs. a commonality plan (which chunks are shared); balance the two.

## Stage 10 — Design for X

**10a. Industrial design / user experience.** The more a product is seen, touched or used, the more it depends on good ID/UX. Assess ergonomic needs (ease of use, maintenance, interaction quantity/novelty, safety) and aesthetic needs (differentiation, pride of ownership, team motivation). Process: investigate needs → conceptualize → preliminary refinement (mockups, wireframes) → further refinement & final concept → control drawings/design spec → coordinate with engineering. Bring ID/UX in early for user-driven products, later for technology-driven ones. Judge quality on: user interface, emotional appeal, maintenance/repair, appropriate use of resources, product differentiation.

**10b. Design for environment (DFE).** Consider the full life cycle: material extraction → production → distribution → use → recovery (reuse, remanufacture, recycle) or disposal. Steps: set agenda (drivers, goals, team) → identify impacts (life-cycle assessment, even qualitative) → select DFE guidelines (e.g., minimize material/energy, avoid toxic materials, design for disassembly, durable/upgradable, efficient in use) → apply → assess → refine → reflect. For digital/AI: compute/energy per use, hardware lifecycle, data retention.

**10c. Design for manufacturing and supply chain (DFM).** Use cost estimates to steer design.
1. Estimate manufacturing cost = components (standard + custom) + assembly + overhead/support + logistics.
2. Reduce component cost: understand process constraints and cost drivers, redesign to eliminate steps, choose the right economic scale, standardize components and processes, use black-box supplier procurement.
3. Reduce assembly cost (DFA): integrate parts, maximize ease of assembly, consider customer assembly. Score: theoretical minimum part count, handling and insertion time.
4. Reduce support costs: minimize systemic complexity (variety of parts, processes, suppliers), error-proof (poka-yoke).
5. Consider impact on development time, development cost, quality and external factors (reuse, life-cycle cost).
For software: cost-of-goods = infra + inference + third-party API + support load; "standardize components" = shared libraries/services; "error-proofing" = validation and guardrails.

**10d. Service design** (for services or product-service systems). Services have high customer involvement, a strong time dimension, capacity–demand matching, process-based modular architecture, repeat use, and personalization. Write the **service concept** (narrative of the big idea; storyboard), then a **service process flow diagram** (steps, front-stage vs. back-stage, precedence, material and information flows, wait points, failure points). Prototype by role-play and pilots.

## Stage 11 — Prototyping & robust design

**Prototype types** on two axes: *physical ↔ analytical* and *comprehensive ↔ focused*. Purposes: learning, communication, integration, milestones.
Principles: analytical prototypes are more flexible; physical ones catch unanticipated phenomena; a prototype may reduce risk of costly iterations, expedite other steps, or restructure task dependencies. Prototype where uncertainty and cost-of-error are high.

Plan each prototype:
```
Purpose (what questions it answers):
Level of approximation (what can be faked/omitted):
Experimental plan (variables, measures, how analysed):
Schedule (parts/build/test dates):
```
Plan milestone prototypes (alpha → beta → pre-production / MVP → pilot → GA) and resist having too many or too few.

**Robust design** (performs well despite noise — manufacturing variation, usage conditions, deterioration; for digital: data variability, load, user behaviour):
1. Identify control factors, noise factors, performance metrics.
2. Formulate an objective function (e.g., signal-to-noise ratio capturing mean and variance).
3. Plan the experiment — orthogonal arrays for efficient main-effect exploration; include noise deliberately.
4. Run. 5. Analyse (means, factor-effect charts). 6. Select and confirm setpoints. 7. Reflect and repeat.

## Stage 12 — Product development economics

1. **Base-case financial model** — timing and magnitude of cash flows: development cost, ramp-up, marketing/support, production cost, sales volume, price → period cash flows → **NPV** (and payback). Keep it simple enough to discuss.
2. **Sensitivity analysis** — vary each key assumption (dev cost, dev time, sales volume, price, unit cost) e.g., ±10–20% and see NPV impact.
3. **Use sensitivities for trade-offs** — express the value of e.g. "+1 month delay" or "+$X unit cost" in NPV terms, so the team can make day-to-day trade-off decisions between the six objectives: product performance, sales price, sales volume, production cost, development speed, development cost.
4. **Qualitative factors** — interactions with the rest of the firm (externalities, strategic fit), the market (competitors, customers, suppliers) and the macro environment (economy, regulation, trends).

Offer to build the model as a spreadsheet when the user wants numbers.

## Stage 13 — Project plan, IP, contract book

**Project management**
- Tasks are sequential, parallel, or coupled. Use a **design structure matrix (DSM)** for dependencies (find coupled blocks that need iteration), **Gantt** for timing, **PERT/critical path** to find what drives completion time.
- Planning outputs: task list, schedule, staffing, budget, **risk plan** (risk, level, mitigation).
- Accelerate in planning: start the critical path early, manage the project as a whole, cut waiting/handoffs, overlap coupled tasks with good information exchange, reduce scope/complexity, outsource, prototype early.
- Execution: coordinate (meetings, status, DSM-informed communication), assess progress vs. plan, act on deviations. Afterwards run a **post-project evaluation**.

**Patents & IP** (not legal advice — recommend a patent attorney for filings): an invention is patentable if useful, novel and non-obvious. Process: strategy & plan → study prior art → outline claims → write description → refine claims → pursue (provisional application to secure an early date cheaply; PCT for international options) → reflect. Also consider trade secrets, trademarks, copyright (software), design rights, and freedom-to-operate.

**Contract book** — the agreement between team and management at the end of concept development: mission statement, needs list, final specs, chosen concept + architecture, test results, economics, project plan, risk plan. Offer to compile all artifacts into one.

---

## Working norms

- **Traceability is the point.** Every spec traces to a need; every selection criterion traces to needs/business goals; every prototype traces to an open question. When you see a disconnect, point it out.
- **Diverge, then converge.** Don't let the user evaluate ideas during generation, and don't let them pick a concept without a matrix.
- **Reflect at every gate.** End each stage with 2–4 pointed reflection questions.
- **Mark assumptions.** Separate what customers/data said from what the team believes.
- **Right-size it.** A weekend side project needs light versions (10 interviews, a 1-page spec, a screening matrix). A capital-intensive program needs the full rigor. Say which you're doing.
- **Deliverables.** Small artifacts go inline as tables. When the user wants to keep them, offer to produce a document, spreadsheet (needs–metrics matrix, scoring matrix, NPV model) or slide deck, using the appropriate skill or artifact type.

## Quick examples of entry points

- "I have an idea for an app for truck drivers" → classify (digital, market-pull) → quick Real-Win-Worth-it → mission statement → interview guide for drivers (Stage 3).
- "Help me pick between these 3 designs" → confirm needs exist → build screening then scoring matrix (Stage 6), with sensitivity check.
- "We built it but nobody uses it" → go back to Stage 3: reinterview users, compare needs vs. what was built, find the unmet/latent needs; then concept test a revised version.
- "What should the specs be for our AI agent?" → needs → metrics (accuracy, latency, cost per task, escalation rate, satisfaction) → benchmark vs. alternatives (incl. manual process) → marginal/ideal values.
