---
name: pdd-product-planning
description: Plan a product portfolio and launch projects with a mission statement - opportunity funnel, classify projects (platform, derivative, improvement, new), evaluate via competitive strategy, product segment maps, technology S-curves, platform plans and product-technology roadmaps, balance with the product-process change matrix and top-down budget split, check capacity with aggregate resource planning, sequence releases, and write the mission statement. Use for roadmaps, portfolio prioritization, "which projects should we fund", capacity planning across projects, or kicking off a project charter.
---

# Product Planning & Mission Statement

Part of the **product-design-development** suite (Ulrich, Eppinger & Yang, ch. 4). Follows `pdd-opportunity-identification`; its output (mission statement) feeds `pdd-customer-needs`.

Product planning decides **which projects, what mix (new / platform / derivative), how they relate, and their timing**, then gives each approved project a **mission statement**. It is periodic (annual or a few times a year), led by senior management, and updated as competition, technology and results change.

Symptoms of no planning: poor market coverage, badly timed launches, too many projects for capacity, over/under-staffed projects, cancelled ill-conceived projects, frequently changing direction.

## Four project types
| Type | Description |
|---|---|
| New product platform | New family built on a new common platform |
| Derivative of existing platform | Extends a platform to familiar/adjacent markets |
| Incremental improvement | Adds/modifies features to keep the line current |
| Fundamentally new product | Radically different product or production tech; new markets; highest risk and learning |

## Five steps
1. Identify opportunities → 2. Evaluate & prioritize projects → 3. Allocate resources & plan timing → 4. Complete pre-project planning → 5. Reflect. (Steps 2–3 iterate.)

### Step 1 — Opportunity funnel
Collect continuously from marketing, sales, research, customers, current teams, service, competitor benchmarks, and active generation (`pdd-opportunity-identification`). Store each as a one-sentence statement tagged with project type, e.g. "Develop a cordless upright vacuum for larger homes (new platform)". A spreadsheet is enough.

### Step 2 — Evaluate & prioritize (four perspectives + new-product criteria + balance)

**A. Competitive strategy** — which does the portfolio serve?
- Technology leadership → R&D, new tech deployment
- Cost leadership → production efficiency, DFM, process projects
- Customer focus → platforms enabling quick derivatives, broad variety
- Imitative → fast follower, needs a fast development process

**B. Market segmentation — product segment map.** Rows = segments (e.g., small area / multi-room / whole house, or SMB / mid-market / enterprise); x-axis = time of introduction; plot your and competitors' products with key specs and price (e.g., "runtime 40 min, $500"). Look for gaps in your line and weaknesses in competitors'; extrapolate spec/price trajectories to set targets.

**C. Technology trajectories — S-curve.** Plot performance (or performance/cost) of each technology vs time or cumulative effort: emergence → rapid improvement → maturity at a natural limit. Decide when to switch a product line to the next technology (e.g., NiMH → Li-ion). Hard to predict the limit — revisit regularly.

**D. Product platform planning.** A platform = assets shared across products (components, subassemblies, software, processes). Platform projects cost 2–10× a derivative, so not every project can be one. Decide derivative vs new platform for each project; release derivatives concurrently with the platform or sequentially after it. Consider network effects (customers committing to a standard; partners building accessories/complements) and design key interfaces for them. (See `pdd-product-architecture` for differentiation/commonality plans.)

**Product-technology roadmap.** Rows = key subsystems/functional elements; along a timeline, the generations of technology for each (e.g., Battery: 7-cell 2.5 Ah → cooled 8-cell 3 Ah → new chemistry); bottom row = the products/projects that will use them. Aligns technology development with product plans; best where critical functional elements are known in advance.

**E. Fundamentally new opportunities — criteria** (use in a screening matrix, see `pdd-concept-selection`): market size (units/yr × price), growth rate, competitive intensity, depth of our market knowledge, depth of our technology knowledge, fit with other products, fit with core assets/capabilities, potential for patents/trade secrets/barriers, existence of an internal product champion.

**F. Balance the portfolio — product-process change matrix.** x-axis: extent of production process change (none → incremental/tuning → single-department upgrade → next-generation process → new core process → R&D); y-axis: extent of product change (none → minor enhancement → addition to family → next-generation platform → new core product). Bubble size = project cost. Regions: current product/process support (bottom-left), derivative projects, platform projects, breakthrough projects (top-right), and R&D. Check for gaps (no breakthroughs? no improvements?) and consistency with strategy (low-cost → more process projects; high variety → many derivatives; tech leadership → more breakthroughs/R&D).

**Top-down portfolio budget.** Don't trade off incremental vs radical projects directly. First split the budget by category (e.g., new platforms 50% / derivatives 30% / updates 20%), then rank projects within each category using criteria suited to that category (strategic potential for breakthroughs, revenue/profit for existing-line projects, key customer concerns for updates).

### Step 3 — Allocate resources & plan timing

**Aggregate resource plan (spreadsheet).** Rows = projects; columns = resource types (industrial design, mechanical, electrical, software, tech development, manufacturing engineering, quality/test, marketing…) per period; cells = person-months (also critical facilities: prototype shop, test labs, pilot line).
```
| Project | Q1-ID | Q1-ME | Q1-EE | ... |
| Demand (sum) |
| Capacity |
| Utilization = demand / capacity |
```
Target **80–90% utilization**; flag cells >100% (or > target). Many firms over-commit by 50%+. Fixes: drop/defer lower-priority projects, outsource (design consultancies), shift people, reduce scope, reuse platforms, partner.

**Timing / pipeline management** — weigh: introduce early but not before quality is adequate (brand damage); technology readiness (proven tech integrates faster); market readiness (low-end vs high-end first; releasing too fast frustrates customers, too slow lags competitors); competitor launches.

**Product plan chart** — rows = product lines/categories, timeline, markers for new platform releases vs derivative releases. Update quarterly/annually.

### Step 4 — Pre-project planning (core team → mission statement)
A small cross-functional **core team** turns the opportunity into a **product vision statement** (one line) and then a **mission statement**:

```
Mission Statement: <project>
Product description: one sentence; basic function, avoid implying a concept
Benefit proposition: the critical few reasons a customer buys (hypothesis to validate)
Key business goals: launch timing, financial targets, share, quality (e.g., ratings), strategic goals
Primary market:
Secondary markets:
Assumptions & constraints: technology, platform, form factor, compatibility, manufacturing sites/suppliers, service goals, environmental policy, regulatory
Stakeholders: end users, buyers, retailers/channel, sales, service, production/supply chain, legal, partners
```
Include manufacturing, service and environmental strategy as constraints when they are decided at corporate level or the production system is itself a big project. Keep assumptions minimal — each one narrows the concept space. Also settle staffing (get leaders to "sign up") and budget; for fundamentally new products budget only the concept phase.

### Step 5 — Reflect
- Is the funnel collecting exciting, diverse opportunities?
- Does the plan support the competitive strategy and address the most important opportunities?
- Are total resources sufficient? Have platforms, joint ventures and supplier partnerships been used to leverage them?
- Does the core team accept the mission? Are its elements consistent?
- Are all assumptions necessary, or is the project over-constrained?
- How can planning improve?
The mission statement is the hand-off — do a reality check now; flaws get costlier later.

## Digital / AI adaptation
Platform = shared services, data platform, design system, agent framework; derivatives = new apps/agents on top. Resource types = data engineers, ML/AI engineers, frontend, backend, UX, product. S-curves apply to model generations and inference cost; roadmap rows = model, retrieval, orchestration, UI, integrations.
