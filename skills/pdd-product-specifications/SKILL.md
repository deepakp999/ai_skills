---
name: pdd-product-specifications
description: Turn customer needs into measurable product specifications - list metrics, build the needs-metrics matrix (QFD/House of Quality core), benchmark competitors on metrics and on perceived need satisfaction, set marginal and ideal target values, then finalize specs after concept selection using technical models, a bill-of-materials cost model, target costing through channel margins, competitive trade-off maps, conjoint analysis and spec flow-down to subsystems. Use for requirements/PRD metrics, acceptance criteria, KPIs for a product, target cost, or resolving performance-vs-cost trade-offs.
---

# Product Specifications

Part of the **product-design-development** suite (Ulrich, Eppinger & Yang, ch. 6). Inputs: weighted needs list (`pdd-customer-needs`). Target specs feed `pdd-concept-generation` and `pdd-concept-selection`; final specs are set after `pdd-concept-testing` and go into the contract book.

**A specification = metric + value (+ unit).** "Average time to assemble fork to frame" (metric) "< 75 s" (value). Specs say *what* the product must achieve, unambiguously, not *how*. Values can be a number, range or inequality; always include units.

**Set specs twice:** *target specs* right after needs (aspirations, before knowing technology limits) and *final specs* after a concept is chosen (real constraints, hard trade-offs). Some firms revisit many times.

---

## Part A — Target specifications (4 steps)

### Step 1 — Prepare the list of metrics
For each need, ask: what precise, measurable characteristic shows how well the product satisfies this need? Ideally one metric per need; often several (e.g., "reduces vibration" → attenuation at 10 Hz + max g on a standard test).

Guidelines:
- **Complete** — together the metrics fully reflect each need.
- **Dependent, not independent variables** — performance outcomes (mass, latency), not design choices (material, framework). Leaves designers freedom.
- **Practical** — directly observable or analyzable by the team at reasonable cost.
- **Subjective needs** — restate the need as the spec, unit "Subj.", and define how it will be judged (e.g., customer panel score).
- **Include popular market comparison criteria** — tests and ratings used by reviewers, magazines, analyst firms, app-store ratings. If a review criterion maps to no need, check for a missed need.
- Units may be "List" (e.g., compatible accessories) or "Binary" (pass/fail standard test).
- **Importance of a metric** — derived from the needs it serves; set by team discussion (or conjoint analysis when few, critical specs).
- People setting specs should have been in the customer interviews (translation is imprecise).

```
| Metric # | Need #s | Metric | Imp. | Units |
| 1 | 1, 3 | Attenuation from dropout to handlebar at 10 Hz | 3 | dB |
| 9 | 7 | Total mass | 4 | kg |
| 17 | 12 | Instills pride | 5 | Subj. |
| 25 | 20 | Industry safety standard test | 5 | Binary |
```

**Needs–metrics matrix** — rows = needs, columns = metrics, • where performance on the metric affects satisfaction of the need. Checks coverage both ways; it is the core of the House of Quality (QFD). For simple mappings, the "Need #s" column suffices.

### Step 2 — Collect competitive benchmarking information
**Metric benchmark chart** — rows = metrics, columns = competing products (and your current one); enter measured values. Buy, test, tear down and cost the important competitors; verify catalog claims independently.
**Perceived-satisfaction chart** — rows = needs (with importance), columns = competitors, scores (e.g., 1–5 dots) from customer perception data. Discrepancies between the two charts are instructive (wrong metric, missed need, or perception gap to exploit). At minimum, build the metric chart.

### Step 3 — Set ideal and marginally acceptable values
- **Ideal** = best you could hope for. **Marginal** = just barely commercially viable.
- Five value forms: **at least X**; **at most X**; **between X and Y**; **exactly X** (avoid — usually really a range); **set of discrete values** (e.g., sizes supported). Relative specs ("tip stiffness ≤ 20% of brake-pivot stiffness") only in the final phase.
- Use the benchmark, likely future competitor performance, mission statement and target segment.
```
| # | Need #s | Metric | Imp. | Units | Marginal | Ideal |
| 3 | 1,3 | Max value on standard test | 5 | g | < 3.5 | < 3.2 |
| 18 | 13 | Unit manufacturing cost | 5 | $ | < 85 | < 65 |
```
These bounds define the competitively viable product space.

### Step 4 — Reflect
- Is anyone **gaming** (e.g., marketing demanding an aggressive value hoping to get more)?
- Should we offer multiple products/options for distinct segments instead of one "average" product?
- Are specs missing? Do they capture what will drive commercial success?

---

## Part B — Final specifications (5 steps, after concept selection)

### Step 1 — Technical models
Analytical (equations, spreadsheet, simulation) or physical (prototypes, test rigs) models that predict metric values from **independent design variables** (dimensions, materials, parameters). Several small independent models are easier than one big one. Use design of experiments to minimize physical tests (`pdd-robust-design`). Models are concept-specific. Use them to check whether a spec combination is technically feasible.
```
Design variables (inputs) → Model (analytical/physical) → Metrics (outputs)
```

### Step 2 — Cost model (bill of materials)
List expected components/subsystems with quantity, low and high unit cost, totals; add assembly (time × labor rate) and overhead (% of direct cost). High/low columns show uncertainty. Update often (even weekly). For complex products, bound major subsystems from experience/suppliers. Get purchasing and production engineers involved. (Detail: `pdd-design-for-manufacturing`.)
```
| Component | Qty | Low $/ea | High $/ea | Low total | High total |
| ... |
| Assembly @ $X/hr | | | | |
| Overhead @ Y% | | | | |
| Total | | | | $low | $high |
```

**Target costing** — work back from market price, not cost-plus:
- Stage margin M = (P − C) / P (note: 50% margin = 100% markup).
- Target unit cost **C = P × Π(1 − Mᵢ)** over every stage (your margin, distributor, retailer…).
- Example: end price $250, manufacturer 40%, distributor 20%, retailer 45% → C = 250 × 0.6 × 0.8 × 0.55 = **$66**. Direct sale → $150; via retailer only → $82.50.
- Typical gross margins (very approximate): manufacturers ~20–60% depending on category (software, packaged goods and medical devices high; automobiles low); distributors/wholesalers ~10–30%; retailers ~20–50% (auto dealers low, specialty and department stores high); sales reps paid by commission.

### Step 3 — Refine specs, making trade-offs
Trade-offs are inverse relationships inherent in the concept (stiffness vs mass; mass vs cost; performance vs development time/cost). In a group session, find feasible value combinations with the technical models, then their cost.
**Competitive (trade-off) map** — scatter plot of competitors on two critical metrics (e.g., manufacturing cost vs test score), shade marginal and ideal regions, and draw your concept's **trade-off curve** (performance across design-variable settings). Can you "beat the trade-off"? Make 3–4 maps for the critical metric pairs.
**Conjoint analysis** (mature categories with a few well-understood attributes): customers evaluate experimentally designed hypothetical products → infer attribute importance → predict choices and market share → choose spec values that maximize share (or profit).

### Step 4 — Flow down specs (complex products)
Translate product specs into subsystem specs so that meeting subsystem specs guarantees the system spec, and difficulty is balanced across subsystems.
- **Budget allocation** for additive metrics: cost, mass, power, (roughly) volume, latency budgets.
- **Model-based allocation** for non-additive metrics (e.g., fuel economy from mass, drag, rolling resistance, engine efficiency). This is systems engineering.

### Step 5 — Reflect
- Is the product a winner? If specs can't be set to meet needs and beat competitors → go back to concept generation/selection or stop.
- How uncertain are the technical and cost models for the metrics that decide success? Refine them if needed.
- Is the concept best suited to this market, or is it "too good" — better used in a more demanding, more profitable segment?
- Should the firm build better technical models for future projects?

## Final spec sheet
```
| # | Metric | Unit | Final value | Rationale / trade-off |
```

## Digital / AI adaptation
Typical metrics: task success rate, accuracy/F1 on an eval set, hallucination/error rate, P95 latency, cost per task/user/month, uptime, time-to-first-value, steps to complete a task, escalation-to-human rate, CSAT/subjective panel score, security/compliance (binary). Benchmark against competitors **and** the current manual process. Target cost = price × (1 − margin) for SaaS gross margin; the "BOM" is infra + model inference + third-party APIs + support. Flow down latency/cost budgets across retrieval, model, tools and UI.
