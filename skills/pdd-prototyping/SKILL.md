---
name: pdd-prototyping
description: Plan prototypes that actually advance a product - classify prototypes (physical vs analytical, focused vs comprehensive, looks-like vs works-like), match them to purposes (learning, communication, integration, milestones), apply prototyping principles (flexibility of analytical models, physical surprises, risk-of-iteration math, expediting steps, removing tasks from the critical path), decide how many comprehensive prototypes using risk vs cost, plan each prototype with the four-step template, and schedule alpha/beta/pre-production milestones while avoiding the hardware swamp. Use for MVP/POC/spike planning, test rigs, pilots, beta programs and milestone demos.
---

# Prototyping

Part of the **product-design-development** suite (Ulrich, Eppinger & Yang, ch. 14). Used in every phase: concept testing (`pdd-concept-testing`), spec models (`pdd-product-specifications`), robustness experiments (`pdd-robust-design`), milestone planning (`pdd-project-management`).

**Prototype = an approximation of the product along one or more dimensions of interest.** This includes sketches, math models, simulations, test components and full pre-production units.

## Tool 1 — Types of prototypes (2×2)
| | Focused (one or a few attributes) | Comprehensive (most/all attributes) |
|---|---|---|
| **Physical** | Foam form model, wheel impact test, gripper coating pull test, hand-built circuit board | Alpha/beta/pre-production units, full-system field test |
| **Analytical** | Beam/spoke equations, FEA of one part, motor math model, CAD model, rendering | Full dynamic simulation (rarely fully possible for physical products) |
Hybrids exist (real UI hardware driving a simulation). Common pairing: a **looks-like** plus a **works-like** focused prototype to learn earlier than one integrated prototype would allow.

## Tool 2 — Purposes and the best type
| Purpose | Question | Best types |
|---|---|---|
| **Learning** | Will it work? How well does it meet needs? | Focused analytical & physical, comprehensive physical |
| **Communication** | Align management, vendors, partners, customers, investors | Physical (visual, tactile) — focused or comprehensive |
| **Integration** | Do parts/subsystems/functions work together? | Comprehensive physical (forces coordination; also integrates marketing, design, manufacturing views); software "daily build" + dogfooding |
| **Milestones** | Show functionality, enforce schedule, qualification tests | Comprehensive physical |

## Tool 3 — Principles
1. **Analytical prototypes are more flexible** — parameters vary easily and widely; use them first to narrow the range, then physical to fine-tune/confirm.
2. **Physical prototypes are needed to detect unanticipated phenomena** — all physics is present (e.g., grippy coatings that wear fast). Build at least one physical prototype.
3. **A prototype may reduce the risk of costly iteration.** Compare expected cost/time: e.g., build mold → test fit has 30% chance of re-doing the mold; building a prototype part first raises first-time success of the mold to 95%. Prototype if (prototype cost) < (reduction in iteration probability × cost of iteration).
4. **A prototype may expedite other steps** (a physical model of a complex part speeds mold design) — worth it if its time < time saved downstream.
5. **A prototype may restructure task dependencies** — e.g., a hand-built board lets software testing run in parallel with production board fabrication, removing a task from the critical path.

## Tool 4 — How many comprehensive prototypes? (risk × cost)
| | Low cost of comprehensive prototype | High cost |
|---|---|---|
| **High technical/market risk** | Many comprehensive prototypes (software, consumer products) | Analytical prototypes used extensively; carefully planned comprehensive prototypes (aircraft, satellites, cars) |
| **Low risk** | One may be built for verification (printed goods) | Few or none; sometimes the first unit built is sold (buildings, ships) |

**Enabling technologies**: CAD (3D visualization, photo-realistic renderings, mass properties, one canonical model; digital mock-up to find interferences, can eliminate full-scale physical models; basis for FEA, crash, kinematic/dynamic simulation) and **3D printing / rapid prototyping** (parts in days for visualization, working prototypes, or patterns for molds/castings).

## Tool 5 — Four-step plan for each prototype (avoid the "hardware swamp")
The swamp = building and debugging prototypes that don't advance the project. Define every prototype first:
1. **Define the purpose** — specific learning and communication needs, integration needs, milestone?
2. **Establish the level of approximation** — physical or analytical? The simplest prototype that serves the purpose; reuse earlier models/testbeds or prototypes built for other purposes; decide what must be accurate (e.g., geometry, materials, load) and what can be ignored (production method, color, attachments). Use analysis to choose what to build.
3. **Outline an experimental plan** — variables, test protocol, measurements, analysis plan; use DOE when many variables (`pdd-robust-design`); feed results back to improve analytical models (may eliminate future physical tests).
4. **Schedule procurement, construction and testing** — key dates: **"bucket of parts"** (parts ready to assemble), **"smoke test"** (first test/power-on), **test completion & results**.

```
Prototype: <name>
Purpose(s):
Level of approximation (accurate vs ignored):
Experimental plan: variables & levels, # units, fixture/rig, protocol, measurements, analysis
Schedule: design/select | build fixture | parts ready | assembly | smoke test | testing done | analysis done
```

## Tool 6 — Milestone prototypes
Plan in the overall project plan at the end of concept development. Base case: **alpha → beta → pre-production**, then consider removing or adding.
- **Alpha** — does it work as intended? Production-intent geometry and materials, made with prototype processes (e.g., machined instead of molded).
- **Beta** — reliability and remaining bugs; often customer-tested in real use; parts from production processes/intended suppliers, assembled in a prototype shop.
- **Pre-production (pilot)** — first units from the entire production process at limited volume; verify process capability; supply preferred customers.
- **Remove** alpha if the product is very similar to past ones or very simple. **Add** early **experimental/engineering prototypes** for new concepts or technologies (don't look like the product).
- Most engineered products need ≥2 milestone prototypes; many need 4+.
- Place milestones on the timeline working backward from launch. If one prototype's test overlaps the next one's design/build, learning can't transfer (worst form of the hardware swamp) → start earlier, delay launch, drop a milestone, or accelerate preceding work.

## Output
```
Prototype portfolio: | Name | Physical/analytical | Focused/comprehensive | Purpose | Key question | Owner | Dates |
Milestone plan: alpha / beta / pilot with entry & exit criteria
Risk-of-iteration calculations for major tooling or build decisions
```

## Digital / AI adaptation
Focused analytical = spreadsheet models, notebooks, offline evals on a test set; focused physical ≈ spike, single-feature proof of concept, Wizard-of-Oz; comprehensive = end-to-end MVP, staging environment, beta with real users; integration = CI/daily builds, dogfooding. Alpha = internal users; beta = selected customers with telemetry; pre-production = limited GA/canary. Risk-of-iteration logic applies to costly commitments (data platform choice, vendor contracts, model fine-tuning).
