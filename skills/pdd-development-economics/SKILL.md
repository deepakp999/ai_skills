---
name: pdd-development-economics
description: Economic analysis for product development decisions - build a base-case cash-flow model and NPV (development, tooling, ramp-up, launch, marketing/support, production, revenue through channel margins, associated consumables/services, cannibalization), sensitivity analysis for internal and external factors, best/worst cases and tornado chart, trade-off rules (NPV per month of delay, per $ of unit cost, per % sales), qualitative factors (firm, market, macro), sunk costs, discount rates, scenario decision trees and the value of testing before launch. Use for business cases, go/no-go gates, ROI, payback, pricing or schedule-vs-cost trade-offs.
---

# Product Development Economics

Part of the **product-design-development** suite (Ulrich, Eppinger & Yang, ch. 18). Used at every gate and for operational trade-offs. Inputs: volumes (`pdd-concept-testing`), unit cost (`pdd-design-for-manufacturing`), schedule and budget (`pdd-project-management`).

**When to use**: choosing a **business model** (low entry price + upgrades/consumables? sequence of high/mid/low models?), **go/no-go milestones** at each phase end, **operational decisions** ("spend $100k on an outside firm to save 2 months?", "launch now at $260 or next quarter at $240?"). Build the model once, then update it as an ongoing project information system. Anyone on the core team can build it (finance can help), but the core team must understand it.

Typical cash-flow shape: development, tooling, ramp-up and launch outflows first; then revenue inflows offset by production, marketing and support costs; cumulative cash dips, then (hopefully) turns positive.

## Four steps
### 1. Build the base-case financial model
**a) Estimate timing and magnitude of cash flows** — merge the project schedule (Gantt) with budget and forecasts, usually by **quarter**:
- Sales revenue (units × net price to you after channel margins)
- Development & testing cost
- Equipment & tooling
- Production & distribution ramp-up
- Launch, ongoing marketing, product support
- Production direct and indirect (overhead) costs
Refinements as needed: seasonal profile, volume growth and price erosion, development split (design/test/refine), direct vs overhead, marketing split (launch, promotion, sales, service), taxes/depreciation, **cannibalization**, salvage, opportunity costs, working capital. **Associated revenue** (consumables, accessories, software, services, warranty costs) can dominate — e.g., capsule sales made NPV ~10× the machine-only case, so the machine could even be sold at a loss.
**Sunk costs are irrelevant** — only future cash flows count.

**b) Compute NPV**: period cash flow = inflows − outflows; PV = C / (1 + r)ᵗ (quarterly r = annual/4 approx.); NPV = Σ PV. Positive NPV → returns exceed the cost of capital. Also report the **investment required** (sum of negative PVs until cash turns positive) and payback period.
**Discount rate** = opportunity cost of capital (firms commonly use ~5–15%/yr; big firms set a hurdle rate; small firms use WACC or investors' expected return). Account for **project-specific risk in the cash flows/scenarios, not by inflating the rate**; market-wide risk is in the rate.

```
Parameters: dev cost & duration | tooling | ramp-up | launch | marketing & support/yr | unit cost | overhead/yr | initial volume | seasonality | volume growth | retail price | price change | channel margin | discount rate | (consumables per unit, price, cost)
| Line item | Q1 | Q2 | ... |
| Volume | ... |
| Net unit revenue = retail × (1 − channel margin) |
| Revenue |
| Development | Tooling | Ramp-up | Marketing & support | Production |
| Total costs |
| Period cash flow |
| PV factor 1/(1+r)^t |
| Period PV |
| NPV = Σ |
```
A runnable template is in `scripts/npv_model.py` (base case, one-at-a-time sensitivities, tornado ranking, trade-off rules).

### 2. Sensitivity analysis
Change one input at a time and record ΔNPV ($ and %).
- **Internal factors** (team controls): development cost, development speed, production cost, product performance.
- **External factors**: price, sales volume, competitive environment, cost of capital (competition is explored via price/volume changes).
State assumptions explicitly (e.g., a delay shrinks a fixed sales window vs shifts it). Typical lesson: development **time** and **volume** often swamp development **cost** (e.g., −20% dev cost → +0.8% NPV; one quarter late → −12% NPV).
**Uncertainty ranges** — set worst/best values for each uncertain input, compute NPV for each, and plot a **tornado chart** (bars sorted by NPV range); focus refinement and risk reduction on the top bars.

### 3. Use sensitivities for trade-offs
Six interacting objectives: **development time, development cost, product (unit) cost, product performance/features, price, sales volume**. Break-even questions: "a 20% dev budget increase costs $0.96M NPV — what volume gain offsets it?" (here only +0.6%).
**Trade-off rules** (approximately linear) for day-to-day decisions:
```
| Factor | Rule | Note |
| Development cost | $X NPV per 10% change | worth the PV of the money |
| Development time | $X per quarter earlier / later | often nonlinear, assumption-dependent |
| Tooling/capex | $X per 10% change | |
| Unit production cost | $X per $1/unit | |
| Price | $X per $1 retail | your share after channel margin |
| Sales volume | $X per 1% | |
| Consumables/attach rate | $X per 1% | |
```
Example uses: should we add a feature costing +10% development and +$3/unit (needs +1.4% volume — but marketing says it won't move sales → no)? Is the project still attractive if competition forces a 10% price cut (−$8M, still strongly positive → yes)?

**Limitations**: only measurable things count (biases against intangible investments); precision ≠ accuracy (assumptions drive results); models are easy to game (all-best vs all-worst values can triple NPV or make it negative) — managers must understand and challenge assumptions; combine with qualitative analysis.

### 4. Qualitative factors (relax "ceteris paribus")
- **Project ↔ firm**: **externalities** (positive: learning reused by other projects; negative: cannibalization) and **strategic fit** (resources, objectives, technical excellence, brand; better NPV elsewhere in the portfolio?). Multi-project NPV or scenarios can help.
- **Project ↔ market**: competitors (direct and substitutes; e.g., a competitor's price cut after launch), customers (expectations, incomes, tastes), suppliers (their markets' pressures). Simulate market scenarios.
- **Project ↔ macro environment**: economic shifts (FX, materials, labor, incomes, investment, capital costs), regulation (can kill or create industries), social trends.
- **Option value of platforms**: a platform may be worth building even if the first product alone doesn't justify it.
Discuss these interactions as a team alongside the numbers to set the relative emphasis on speed, development cost, unit cost and performance. More structured tools: strategic analysis, game theory, Monte Carlo, scenario analysis.

## Scenario and decision-tree analysis
- **Discrete scenarios** (e.g., patent allowed 60%: PV $6.5M; not allowed 40%: PV $1.5M) → expected NPV = Σ pᵢ·PVᵢ = $4.5M.
- **Decision points / real options**: launch now (PV $2.0M) vs **test the market** first (−$1.0M; then 70% launch with PV $5.0M, 30% cancel and salvage $0.5M) → −1.0 + 0.7·5.0 + 0.3·0.5 = **$2.65M** > $2.0M → test first. Projects can be stopped or redirected at gates — that flexibility has value.
- **Monte Carlo**: assign distributions to uncertain inputs and simulate NPV distribution.

## Output
```
Base-case assumptions table + quarterly cash-flow table → NPV, investment, payback
Sensitivity tables (dev cost, dev time, volume, price, unit cost…)
Worst/best ranges + tornado chart
Trade-off rules sheet for the team
Qualitative factors: firm / market / macro, platform option value
Scenarios / decision tree if discrete uncertainties exist
Recommendation: go / no-go / redirect, and what to de-risk first
```
Offer to build it as a spreadsheet the team can update.

## Digital / AI adaptation
Model revenue as subscriptions (users × ARPU × retention), usage or transaction fees; costs as build team, infrastructure, inference, third-party APIs, support, sales/marketing (CAC). Associated revenue = upsells, add-ons, services. For internal tools, value = hours saved × loaded cost, error reduction, revenue uplift, avoided licences; compare to build + run cost. Time-to-market sensitivity is usually the largest lever.
