---
name: pdd-opportunity-identification
description: Find and pick product opportunities with an innovation tournament - write a charter, generate dozens to hundreds of opportunities (passions, bug lists, VRIN capabilities, customer ethnography, trends, imitate-but-better, lead users and other sources), screen by multivoting, develop the promising ones cheaply, and select with Real-Win-Worth-it. Use when someone wants new product or business ideas, asks "what should we build next", or needs to choose between several opportunities.
---

# Opportunity Identification (Innovation Tournament)

Part of the **product-design-development** suite (Ulrich, Eppinger & Yang, ch. 3). Comes before `pdd-product-planning`; its winner becomes a mission statement.

An **opportunity** is a hypothesis about how value might be created: an embryonic product description, a newly sensed need, a new technology, or a rough need–solution match. Write each in under a page: **title + short narrative (+ optional sketch)**.

## Core idea: run a tournament
Great opportunities are rare and uncertain, so generate many and filter hard (e.g., 50 raw → 7 with concept sketches → 3 with prototypes and packaging tests → 1 mission statement). Three levers raise the quality of the winner:
1. **More opportunities** — more candidates, more exceptional ones.
2. **Higher average quality** — better sources and methods.
3. **Higher variance** — wild ideas raise the odds of an outlier; don't over-filter early.

Opportunity identification aims to *kill* unworthy ideas cheaply; product development aims to make the chosen one as good as possible.

## Tool 1 — Opportunity horizon map
Two axes: knowledge of the **need/market** (existing served → adjacent → new) × knowledge of the **solution/technology** (current → existing but not ours → new).
- **Horizon 1**: improvements, extensions, variants, cost reductions for current markets — low risk.
- **Horizon 2**: next-generation products, adjacent markets, new approaches — medium risk.
- **Horizon 3**: new-to-the-world needs and solutions — highest risk.
Decide which horizons the charter allows (e.g., "launch within a year" → H1–H2).

## The six steps

### Step 1 — Establish a charter
State goals and boundaries. Example: "Create a physical product in category X that we can launch within ~a year through our existing retail channel." Make it a bit **broader than comfortable** — ideas are cheap; narrowing later is easy.

### Step 2 — Generate and sense many opportunities
About half of opportunities come from inside, half from outside (customers ~23%, competitive products ~11%, sales force, universities, inventors, partners, suppliers). Aim for dozens to hundreds. Seven techniques:
1. **Follow a personal passion** — list passions; ask how trends/tech/business models change them; what do you need?
2. **Bug lists** — record every annoyance for days/weeks (yours, customer complaints, immersion in users' world); pick the most universal and vexing; solve.
3. **Pull from capabilities (VRIN)** — inventory resources that are Valuable, Rare, Inimitable, Non-substitutable; turn each into a challenge ("where else could our X create advantage? what else could we offer our customer base?").
4. **Study customers** — ethnography/user anthropology; watch what people do, not what they say; surface latent needs.
5. **Implications of trends** — list social, environmental, technological, demographic, economic trends → imagine opportunities each enables.
6. **Imitate, but better** — scan competitors' launches, trade shows, patents (alternative solution for the same need, or alternative need for the same solution); **de-commoditize** a commodity (deluxe version); **drive down-market** (cheap version of a premium product); **import geographically isolated innovations**.
7. **Mine your sources** — lead users (advanced needs, often invent their own fixes), social networks and communities, universities & government labs (tech transfer), online idea submission from customers.

### Step 3 — Screen opportunities
Goal: drop the clearly weak, not pick the best. Use a **single holistic judgment**: "Is this worth a few days/weeks more investigation?" (multiple criteria bog things down).
- **Web survey**: anonymous list, yes/no or 1–10 votes; need ≥6, ideally >10 independent judges.
- **Workshop multivoting** (≤~50 ideas): one-minute, one-page pitch each; ideas posted and numbered; raters write numbers on dot stickers silently, then all place simultaneously (avoids herding).
- Advance top vote-getters **and** ideas with a few very enthusiastic supporters.

### Step 4 — Develop promising opportunities
Invest days to weeks in each of several survivors. Minimum: internet search for existing solutions + talk to a few potential customers. Also: interviews, test existing products, concept sketches, quick prototypes, market size/growth estimates, cursory patent search.
**Uncertainty-resolution table** — do the cheapest tasks that remove the most uncertainty first:
```
| Opportunity | Key uncertainty | Task to resolve | Cost/time | Result |
```

### Step 5 — Select exceptional opportunities (Real–Win–Worth it)
Answer each sub-question Yes/No/Unknown with evidence:

**1. Is it real? (real market, real product)**
- Is there a need? How is it satisfied today?
- Can the customer buy? (market size, buying process)
- Will the customer buy? (perceived risks/benefits, price & availability expectations)
- Is there (or can we develop) a viable concept?
- Acceptable within social, legal, environmental norms?
- Feasible — can it be made, is technology available, does it satisfy the need?
- Relative advantage over other products?
- Can it be produced at low cost?
- Are customer-perceived risks acceptable; what are adoption barriers?

**2. Can we win? (competitive product, competitive company)**
- Competitive advantage, and is it sustainable? (performance, patents, barriers, substitution, price)
- Is the timing right? Does it fit our brand?
- Will we beat competitors (their improvement, price trajectories, new entrants)?
- Superior resources (engineering, finance, marketing, production; core-competence fit)?
- Management that can win (experience, culture fit, commitment)?
- Do we know the market as well or better than competitors (behaviour, channels)?

**3. Is it worth doing? (return adequate, risk acceptable)**
- Will it make money? Do we have resources and cash?
- Are the risks acceptable (technical vs market, what could go wrong)?
- Does it fit our strategy (growth, brand, embedded options)?

Entrepreneurs may add/replace criteria: capital required, time to market, personal passion. For a more quantitative pick, use the screening/scoring matrices in `pdd-concept-selection` with opportunities as columns.

### Step 6 — Reflect
- Internal vs external share of opportunities?
- Did we consider dozens or hundreds?
- Was the charter too narrow?
- Were filters biased, or real estimates of success?
- Are the winners exciting to the team?

## Output templates
```
Charter: 
Horizon(s) allowed:

Opportunity log
| # | Title | One-line narrative | Source/technique | Horizon | Screen votes | Status |

RWW summary
| Opportunity | Real? | Win? | Worth it? | Key evidence | Biggest open risk | Decision |
```
Hand the winner to `pdd-product-planning` to write the mission statement.

## Digital / AI adaptation
Bug lists from support tickets, logs and process mining are rich sources; "can it be produced at low cost" = unit economics (infra/inference/support per user); patents are weaker moats — weigh data, distribution and integration advantages under "Can we win?".
