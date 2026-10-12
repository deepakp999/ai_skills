---
name: pdd-design-for-manufacturing
description: Design for manufacturing and supply chain (DFM/DFA) - strategic sourcing (make-buy, contract manufacturing, ODM, production location, duties), estimate cost of goods with a costed bill of materials (standard and custom components, tooling amortization, assembly time, overhead burden rates, freight and duties), then reduce component, assembly, production-support and logistics costs, and check impacts on development time, cost, quality and the wider enterprise. Use for unit cost / COGS estimates, BOM costing, should-cost, supplier and process selection, design-for-assembly reviews, packaging/freight reduction, or cutting product cost.
---

# Design for Manufacturing & Supply Chain (DFM)

Part of the **product-design-development** suite (Ulrich, Eppinger & Yang, ch. 13). Starts in concept development (cost as a selection criterion; BOM in `pdd-product-specifications`), shapes architecture (`pdd-product-architecture`), dominates detail design. Pairs with `pdd-design-for-environment`; cost feeds `pdd-development-economics`.

DFM reduces cost **while improving (or not inappropriately compromising) quality, development time and development cost**. It is cross-functional (designers, manufacturing engineers, supply chain, cost accounting, production, suppliers) — often run as workshops — and iterative: estimate, improve, re-estimate dozens of times until the design is frozen/released.

## The method (7 steps + iterate)
Proposed design → 1 strategic sourcing → 2 estimate costs → 3 components / 4 assembly / 5 production support / 6 logistics → 7 impact on other factors → recompute cost → good enough? (no → iterate).

### Step 1 — Strategic sourcing decisions
**Make vs buy** (degree of vertical integration). Keep in-house only what is a distinctive competitive advantage (e.g., trade-secret processes). Supplier arrangements:
| Arrangement | Brand owner does |
|---|---|
| Full vertical integration | Components and assembly internally |
| Final assembly only | Assembles; suppliers make components |
| Orchestration of suppliers | Coordinates separate component and assembly suppliers |
| Contract manufacturing (CM) | One supplier makes components (via its suppliers), assembles, packs |
| ODM | Supplier also does detailed design from a functional spec (mature categories) |
The more established the category, the more can be outsourced; truly novel products may force integration.
**Location drivers**: factor prices (labor, materials, energy), capabilities & ecosystem (clusters of skills, tooling, suppliers), duties/tariffs (by origin, via HTS codes), transport costs (ocean vs nearby truck/rail), other (geopolitical risk, "made in" preference, government incentives). Prefer near the market, all else equal.

### Step 2 — Estimate manufacturing costs
**Cost of goods (COGS)** = factory costs + logistics costs.
- **Components** — standard (purchased: batteries, motors, chips, fasteners) and custom (raw material + processing + tooling).
- **Assembly** — labor (+ equipment & tooling).
- **Overhead** — support costs (materials handling, QA, purchasing, shipping/receiving, facilities, tooling maintenance — design-dependent) and indirect allocations (not design-dependent, ignore for DFM); plus **supplier profit** (~10–30%) if outsourced.
- **Logistics** — freight + duties.
**Fixed vs variable**: fixed (tooling, setup, assembly-line setup) don't vary with volume within a stated range and horizon; variable (materials, processing, often labor) scale with units.

**Costed bill of materials** (indented by subassembly):
```
| Part # | Description | Rev | Process | Material | Unit variable cost | Tooling cost | Tooling life (units) | Unit fixed cost | Unit total | Qty | Total |
```
Unit fixed cost = tooling ÷ amortization quantity (the lesser of tool life and expected lifetime volume). Show a shared tool once and amortize over combined volume.

**Standard components** — compare to similar parts already bought at similar volume, or get quotes (volume matters hugely: 10× price difference between a dozen and 10,000/month). At high volume (~100k/yr) suppliers may customize "standard" parts cheaply.

**Custom components** (best: supplier quote; early: build up)
- Raw material = part mass × (1 + scrap allowance: ~5–50% molding, ~25–100% sheet metal) × $/kg (steels ~$0.5–5/kg, aluminum ~$2–10, plastics ~$1–10, titanium/composites higher).
- Processing = cycle time × machine rate (~$25/h simple press to ~$75/h CNC mill, incl. labor and depreciation).
- Tooling = molds/dies/fixtures ($5k–$500k for injection molds; good molds/dies last millions of cycles) ÷ volume.
- Supplier overhead & profit ≈ 20–40% of material + processing.
- Example (thermoformed hopper): material 0.9 kg × $4 = $3.60; forming 30/h @ $40 = $1.33; CNC trim 20/h @ $50 = $2.50 → variable $7.43; +30% = $2.23; tooling $3,000 / 2,000 units = $1.50 → **$11.16**.
**Process cost structures** (typical patterns): CNC machining — low fixed (setup, programming), high variable (tens of $ per part, minutes–hours each), unit cost falls modestly with volume; injection molding — high fixed ($10k–80k+ molds, cavities, actions/retracting pins add cost), cents to a few $ per part at high volume; progressive die stamping — high fixed ($10k–200k dies), very low variable at 100k–10M; sand casting — low tooling, moderate variable, needs machining; investment casting — moderate tooling, slow and costly per part, complex shapes. Unit cost = (setup + tooling)/volume + variable.

**Assembly** — mostly manual below several hundred thousand units/yr (circuit boards are automated). Sum operation times (≈4–60 s each; e.g., screw ~7.5–13 s, snap-fit ~3.5–8 s, pin ~3–10 s, spring ~2.6–14 s) × labor rate (<$1/h low-wage countries; ~$15–30/h developed economies incl. benefits; higher in auto/aero). Small products: ~2–14 s per part, total of a few minutes for dozens of parts. DFA software databases (e.g., Boothroyd Dewhurst) give handling/insertion times.

**Overhead** — burden rates on cost drivers, e.g., 10% of purchased materials + 80% of assembly labor (traditional) or activity-based: rates per machine hour, setup hour, production order, material-handling load, shipment, new part number introduced. Burden rates are convenient but distort true support cost.

**Logistics** — ocean container ~70 m³ for ~$5k Asia→US incl. fees (~$70/m³); domestic truck ~$0.10–1/kg; air ~$2–5/kg. Low-density goods pay dimensional weight (~100–200 kg/m³ minimum density). Duties: % of value by HTS code and origin (apparel/footwear often 10–20%; some tariffs ≥25%).

Look at the breakdown to see which category (components, assembly, support, logistics) to attack first.

### Step 3 — Reduce component costs
- **Understand process constraints and cost drivers** — avoid features needing expensive extra processes (tiny internal radii → EDM), excessive tolerances; codify **design rules** (materials, thicknesses, max size, min slot, accuracy); know cost-driver formulas (e.g., welding ∝ number of welds and weld length); work with process experts.
- **Redesign to eliminate processing steps** — drop unneeded finishing (unpainted hidden aluminum); use **net-shape / near-net-shape** processes (molding, casting, forging, extrusion) needing only minor secondary ops.
- **Choose the right economic scale** — low-fixed/high-variable processes (machining, 3D printing) for low volume; high-fixed/low-variable (molding, stamping) for high volume; compute the crossover (e.g., machining $10/unit + $1k fixture vs molding $1/unit + $10k mold → break-even ~1,000 units); multi-cavity molds at higher volume; newer additive processes can compete up to ~10k units.
- **Standardize components** — same part used repeatedly within and across products (e.g., one extrusion profile for all frame members, even with a few unneeded features) → volume, cost, quality.
- **Black-box (functional-spec) procurement** — give suppliers what the component must do and its interfaces, not how; they optimize cost and do the engineering. Needs clear system-level interfaces.

### Step 4 — Reduce assembly costs (DFA)
- **Integrate parts** — combine adjacent parts that needn't move relative to each other or be different materials; molded/stamped parts absorb features at little cost; fewer assemblies, often cheaper tooling, better dimensional control. (Theoretical minimum part count test: does it move, need a different material, or need to be separate for assembly/service?)
- **Maximize ease of assembly** — ideal part: inserted from the top (z-axis assembly); self-aligning (chamfers); needs no orientation (symmetry) or obvious orientation; one hand; no tools; single linear motion (push-in fasteners vs screws); secured immediately on insertion. Sometimes *adding* parts reduces time (gaskets instead of sealants with long cure times).
- **Consider customer assembly** — acceptable if it brings benefits (smaller box); must be foolproof for people who ignore instructions.
Rules of thumb: minimize part count, modular assembly, stack assemblies, eliminate adjustments, eliminate cables, self-fastening and self-locating parts, eliminate reorientation, ease handling, specify standard parts.

### Step 5 — Reduce production-support costs
- **Minimize systemic complexity** — variety in suppliers, parts, people, products and processes all drive tracking, inspection, handling and inventory cost; much is set by design.
- **Error-proofing (poka-yoke)** — anticipate production failure modes: asymmetric features so parts fit only one way; eliminate near-identical parts (thread pitch, left/right hand, mirror images, material grades) or exaggerate differences (color coding).

### Step 6 — Reduce logistics costs
Duties are mostly fixed by Step 1 location. Freight is driven by volume (ocean, rail) and weight/dimensional weight (truck, air). Reduce volume via: partial disassembly, folding or compression (detachable legs/handles, roll-packed mattresses); minimum carton size (tight inserts); limited or no packaging (hang tags); **delayed final packaging** (ship bare/nested in bulk, pack at destination); nest parts and assemble near market (e.g., nested hoppers cut shipping volume ~6×). Air freight only when value/size is very high.

### Step 7 — Impacts on other factors
- **Development time** — can be worth far more than unit savings (e.g., $1/unit saved rarely justifies a month's delay in autos).
- **Development cost** — teams that pursue DFM aggressively generally don't take longer or spend more.
- **Product quality** — ideally improves (simpler assemblies); check cheaper materials; test alternatives when significant.
- **Larger enterprise (externalities)** — component reuse by other teams, life-cycle costs (service, warranty, disposal of toxics — see DFE), supply-chain responsiveness (distant factories need more inventory).

## Results to expect
Mature DFM programs report COGS reductions up to ~50%: fewer parts, new materials, more integrated custom parts, higher-volume standard parts, simpler assembly. Track design iterations with part count, fixed cost and unit cost per version.

## Output
```
Sourcing plan: make/buy, arrangement, locations, duties
Costed BOM with fixed/variable split, assumptions (volumes, rates)
COGS breakdown: components / assembly / overhead / logistics
DFM/DFA improvement log: | Idea | Cost impact | Quality/time impact | Decision |
Design iteration comparison: | Version | Part count | Fixed cost | Unit cost |
```

## Digital / AI adaptation
COGS = hosting + inference/tokens + third-party APIs + data/storage + support & operations per user/transaction. Make-buy = build vs SaaS/API vs managed platform; location = cloud region (latency, data residency, price). Component cost reduction = cheaper models for easy tasks, caching, batching, prompt/token budgets; standardize components = shared services/libraries; black-box procurement = vendor APIs against an interface spec; assembly ≈ integration effort; error-proofing = schema validation, typed interfaces, guardrails; support complexity = number of variants, tenants and configurations.
