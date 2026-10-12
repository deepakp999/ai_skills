---
name: pdd-product-architecture
description: Define product architecture - map functional elements to physical (or software) chunks, choose modular (slot, bus, sectional) vs integral, using the four-step method (schematic, cluster into chunks, rough geometric layout, fundamental and incidental interactions graph/matrix), plus delayed differentiation (postponement), platform planning with differentiation and commonality plans, secondary systems and interface specifications. Use for system architecture, module boundaries, platform/product-family design, variant strategy, microservice or agent decomposition, and assigning work to teams or suppliers.
---

# Product Architecture

Part of the **product-design-development** suite (Ulrich, Eppinger & Yang, ch. 10). Emerges in concept development; settled early in system-level design. Feeds `pdd-design-for-manufacturing`, `pdd-project-management` (team/supplier assignment) and `pdd-product-planning` (platforms).

**Product architecture = the scheme by which functional elements are arranged into physical chunks, and by which the chunks interact.**
- Functional elements: operations/transformations that make up performance ("store paper", "communicate with host").
- Physical elements: parts, components, subassemblies — grouped into **chunks** (major building blocks).

## Modular vs integral
| Modular | Integral |
|---|---|
| Each chunk implements one or a few functional elements entirely | Functional elements spread over several chunks, or one chunk implements many |
| Interactions between chunks well defined and fundamental | Interactions ill-defined, often incidental |
| Change one chunk without changing others; design chunks independently | Optimized holistic performance; changes ripple widely |
Modularity is relative ("more modular than…").

**Three modular types**
- **Slot-modular** — each interface is different; chunks not interchangeable (car radio vs speedometer). Most common.
- **Bus-modular** — common bus, all chunks attach with the same interface (PC expansion cards, track lighting, shelving rails, roof racks).
- **Sectional-modular** — all interfaces identical, no central element; chunks connect to each other (pipes, sectional sofas, office partitions).
Bus/sectional suit products needing widely varying configurations with standard power/fluid/structure/signal connections.

**When defined:** incremental products — architecture is part of the concept; first-of-kind — concept focuses on working principles, architecture becomes the first task of system design.

## Implications to weigh
- **Product change** (modular localizes change): upgrade, add-ons (incl. third-party), adaptation to environments (voltage, fuel), wear (replaceable parts), consumption (refills/cartridges), flexibility in use (user-configurable), reuse in later products.
- **Product variety** — modular chunks combine into many variants cheaply (watch faces, hands, straps on few movements).
- **Component standardization** — same chunk across products → volume, cost, quality (also via common suppliers).
- **Product performance** — integral enables **function sharing** (one element doing several functions, e.g., transmission case as frame) and geometric nesting → lower size, mass, material, drag, noise.
- **Manufacturability** — part-count reduction by integration is only easy *within* chunks; so DFM starts during architecture.
- **Development management** — modular: careful system-level planning, then teams/suppliers work in parallel against chunk specs (good for outsourcing/distributed teams). Integral: less upfront spec, much more integration and coordination during detail design.

## Four-step method (cross-functional)
### 1. Create a schematic
Diagram of the product's elements — physical concepts/critical components already chosen plus still-functional elements — connected by flows of **force/energy**, **material** and **signal/data**. Aim for **< 30 elements**; group minor ones (handled later as secondary systems). The schematic is not unique (e.g., centralized vs distributed control) — sketch alternatives that open different architectures.

### 2. Cluster elements into chunks
Start with every element as its own chunk, then cluster where advantageous. Clustering factors:
- **Geometric integration and precision** — elements needing precise relative location in one chunk.
- **Function sharing** — one component can do several functions (display + controls).
- **Capabilities of vendors** — group what a trusted supplier is expert in.
- **Similarity of design or production technology** — e.g., all electronics on one board.
- **Localization of change** — isolate elements expected to change (e.g., enclosure styling).
- **Accommodating variety** — isolate elements that vary by market (regional power supply).
- **Enabling standardization** — group elements reusable across products (existing cartridge).
- **Portability of interfaces** — electrical/data signals travel easily (can be separated); mechanical forces/motions constrain placement; fluids in between.

### 3. Rough geometric layout
2D/3D drawings, CAD or cardboard/foam models positioning the chunks. Checks feasibility of geometric interfaces and key dimensional trade-offs (e.g., paper capacity vs machine height). Generate several layouts; re-cluster if infeasible; coordinate with industrial design when form and interface matter.

### 4. Identify fundamental and incidental interactions
- **Fundamental** — the planned flows on the schematic between chunks.
- **Incidental** — side effects of physical implementation or arrangement (vibration, heat/thermal distortion, RF interference, styling coupling).
- Record with an **interaction graph** (< ~10 chunks) or an **interaction matrix / DSM** (larger systems; can also drive clustering by interaction strength).
- Use it to organize the work: strongly interacting chunks → teams with strong communication; independent chunks → loosely coupled teams. Fully specified interfaces let interacting chunks be built independently (easy for fundamental, hard for incidental).
```
Chunk list
| Chunk | Functional elements | Owner/team/vendor | Key interfaces |
Interaction matrix (chunks × chunks): F = fundamental (type), I = incidental (type)
```

## Delayed differentiation (postponement)
Make variants as late as possible in the supply chain (e.g., partial assembly → ship → add region-specific chunk → package). Demand for the common base is far less random than for individual variants, so inventory and cost drop. Two necessary conditions:
1. **Differentiating attributes concentrated in one or a few chunks** (power cord + external power brick, not power components spread across cord, enclosure, chassis, board).
2. **Product and process designed so those chunks can be added near the end** (e.g., ship bare units on pallets so localized cartons are added at the distribution center).

## Platform planning — differentiation vs commonality
**Differentiation plan** — rows = differentiating attributes (in spec language), columns = product versions/segments:
```
| Attribute | Family | Student | Small office |
| Print speed | 6 ppm | 8 ppm | 10 ppm |
| Footprint | ... |
```
**Commonality plan** — rows = chunks, column for number of distinct types, then the version of each chunk used in each product:
```
| Chunk | # types | Family | Student | Small office |
| Print mechanism | 2 | Std | Narrow | Std |
```
Unconstrained, marketing maximizes differentiation and manufacturing maximizes commonality. Guidelines:
- Use **quantitative** cost/revenue estimates — e.g., profit from +1 point of market share vs added manufacturing, tooling and supply-chain cost of another chunk version (and whether its differentiation can be postponed).
- **Iterate** quickly with approximate data rather than agonizing.
- **Architecture sets the trade-off** — if differentiation and commonality conflict, try another architecture (more modular) that improves both.

## Related system-level issues
- **Secondary systems** (safety, power distribution, monitoring, structure) cut across chunks; usually flexible connections; assign a dedicated owner/sub-team.
- **Architecture of the chunks** — complex chunks need their own architecture (same method, one level down).
- **Detailed interface specifications** — the "contract" between chunks: each line/signal/flow with name and properties (voltages, currents, logic levels, data formats, mechanical datums).

## Reflect
Does the architecture support planned variety, change and reuse? Are incidental interactions understood and owned? Can chunks be assigned to teams/suppliers cleanly? Is DFM considered within chunks? Would another architecture give better differentiation *and* commonality?

## Digital / AI adaptation
Chunks = services, modules, agents, data stores, UI apps. Slot-modular = bespoke integrations; bus-modular = event bus/API gateway/MCP-style tool interface/plugin system; sectional = composable pipelines. Clustering factors map directly (team ownership ≈ vendor capability; localization of change ≈ isolate volatile components like the LLM provider or prompts; portability = network APIs). Incidental interactions: shared database contention, latency coupling, cost spikes, security boundaries. Postponement = configuration/feature flags and tenant-specific layers applied at deploy time. Interface spec = API contracts/schemas.
