---
name: product-design-development
description: Coordinator for end-to-end product development (Ulrich, Eppinger & Yang method) for any physical, digital, service or AI product - figures out where a project is in the journey, picks the process variant, routes to the right pdd-* stage skill (opportunity, planning, customer needs, specs, concept generation/selection/testing, architecture, industrial design, DFE, DFM, prototyping, robust design, IP, service design, economics, project management) and keeps the contract book. Use whenever someone has a product idea, wants to build or improve a product, or asks "where do I start / what's next".
---

# Product Design & Development — Coordinator

The coordinator of a suite of skills based on *Product Design and Development* (Ulrich, Eppinger & Yang). It works for physical products, software/digital products, AI agents, internal tools, services and product-service systems.

**Core belief:** most product failures are decided at the front end — wrong opportunity, misunderstood needs, vague specs, or a concept chosen by the loudest voice. The method front-loads structured thinking, keeps the customer's voice traceable from needs to specs to concept, and makes each big decision with an explicit, reviewable artifact (a list, a matrix, a model).

## How to run
1. **Locate the user in the journey.** Ask or infer: raw idea? known problem? concept chosen? building? launching? Jump to the open stage; quickly check upstream artifacts exist ("which customer needs drive these specs?") — missing upstream work is the most common root cause of downstream trouble; name it gently.
2. **Pick the process variant** (table below) — it changes which stages matter.
3. **Call the stage skill** for the current stage and follow its method and templates. Load only what is needed now; each stage skill is self-contained.
4. **Fill templates with the user's real content**; where data is missing, propose drafts marked `[assumption — validate]` rather than stalling.
5. **Gate check at the end of each stage** — what did we learn, what is still assumed, is it good enough to move on? Then suggest the next stage.
6. **Maintain the contract book** (below); offer to compile it into a document, spreadsheet or deck when several stages are done.
Right-size the rigor: a weekend project gets light versions (10 interviews, 1-page spec, a screening matrix); a capital-intensive program gets the full method. Say which you're doing.

## Stage map → skills
| Phase | Stage | Key question | Skill | Main artifacts |
|---|---|---|---|---|
| Setup | Process & organization | What process and team structure fit? | `pdd-process-and-organization` | Phase/gate plan, function×phase grid, org choice |
| 0 Planning | Opportunity identification | Which opportunity is worth pursuing? | `pdd-opportunity-identification` | Charter, opportunity log, Real-Win-Worth-it |
| 0 Planning | Product planning | Which projects, when, with what resources? | `pdd-product-planning` | Segment map, S-curves, roadmap, product-process matrix, aggregate resource plan, mission statement |
| 1 Concept | Customer needs | What must the product do for users? | `pdd-customer-needs` | Selection matrix, interview guide, data template, weighted need hierarchy, latent needs |
| 1 Concept | Target specifications | How will we measure success? | `pdd-product-specifications` | Metrics list, needs–metrics matrix, benchmarks, marginal/ideal values |
| 1 Concept | Concept generation | What are all the ways to do it? | `pdd-concept-generation` | Function diagram, search log, classification tree, combination table |
| 1 Concept | Concept selection | Which concept wins? | `pdd-concept-selection` | Screening (Pugh) and scoring matrices, sensitivity |
| 1 Concept | Concept testing | Do target customers want it? How many will buy? | `pdd-concept-testing` | Test plan, survey, Q = N×A×P forecast |
| 1 Concept | Final specifications | What can we actually achieve? | `pdd-product-specifications` (Part B) | Technical & cost models, target cost, trade-off maps, flow-down |
| 2 System design | Product architecture | How do functions map to chunks/modules? | `pdd-product-architecture` | Schematic, chunks, layout, interaction matrix, differentiation & commonality plans |
| 2–3 | Industrial design / UX | How will it look, feel and be used? | `pdd-industrial-design` | ID importance assessment, ID process, quality scorecard |
| 2–3 | Design for environment | How do we cut life-cycle impact? | `pdd-design-for-environment` | Impact chart, DFE guidelines, DFE score/LCA |
| 2–3 | Design for manufacturing & supply chain | How do we make it at target cost? | `pdd-design-for-manufacturing` | Sourcing plan, costed BOM, DFM/DFA actions, logistics |
| 3–4 | Prototyping | What must we learn by building? | `pdd-prototyping` | Prototype plans, milestone prototypes |
| 3–4 | Robust design | Will it work despite variation? | `pdd-robust-design` | P-diagram, orthogonal-array DOE, setpoints |
| Any | Patents & IP | What can and should we protect? | `pdd-patents-ip` | IP strategy, prior art, claims, disclosure |
| Any (services) | Service design | How does the service work end to end? | `pdd-service-design` | Service concept, process flow diagram, pilot |
| Throughout | Economics | Is it worth it; what are the levers? | `pdd-development-economics` | NPV model, sensitivities, tornado, trade-off rules |
| Throughout | Project management | How do we deliver on time? | `pdd-project-management` | Contract book, DSM, critical path, staffing, budget, risk plan |

Phases 4–5 (testing & refinement, production ramp-up/launch) execute the plan with `pdd-prototyping`, `pdd-robust-design` and `pdd-project-management`.

If a stage skill is not installed, apply the core method from memory: the stage's numbered steps and its main artifact listed above.

## Process variants
| Type | What changes |
|---|---|
| Market-pull (default) | Full process from market need |
| Technology-push | Find the market where the tech clearly wins; also evaluate non-tech concepts |
| Platform | Concepts assume the existing platform; architecture/reuse dominate |
| Process-intensive | Product and production process co-designed from the start |
| Customized | Structured configuration of standard designs |
| High-risk | Test biggest technical/market risks first; parallel paths |
| Quick-build / digital / AI | Spiral: prioritized features in repeated design-build-test cycles; still do needs, specs and selection up front |
| Product-service system | Add `pdd-service-design` |
| Complex system | Architecture, flow-down and integration dominate |

**Digital/AI vocabulary**: manufacturing cost → infra/inference/support cost per user; assembly → integration; chunks → services/modules/agents; physical prototype → clickable mock, Wizard-of-Oz, spike, beta; tooling → infrastructure and data pipelines.

## Contract book (running record)
Mission statement · customer needs · competitive analysis · specifications · concept sketches/description · concept test report · sales forecast · economic analysis · environmental assessment · manufacturing/operations plan · task list & DSM · staffing · schedule · budget · risk plan · performance measures · incentives. Track status per item (not started / draft / validated).

## Working norms
- **Traceability**: every spec traces to a need, every selection criterion to needs or business goals, every prototype to an open question. Point out disconnects.
- **Diverge, then converge**: no judging during generation; no picking without a matrix.
- **Separate evidence from assumption**.
- **Reflect at every gate** with 2–4 pointed questions.
- **Deliverables**: small artifacts inline as tables; for lasting ones offer a document, spreadsheet (needs–metrics, selection matrices, NPV) or deck.

## Entry examples
- "I have an app idea for truck drivers" → variant: digital, market-pull → `pdd-opportunity-identification` (quick RWW) → `pdd-product-planning` (mission) → `pdd-customer-needs` (interview guide).
- "Help me pick between these 3 designs" → confirm needs exist → `pdd-concept-selection`.
- "We built it but nobody uses it" → back to `pdd-customer-needs`, then `pdd-concept-testing` on a revised concept.
- "What should our unit cost be / is this worth funding?" → `pdd-product-specifications` (target costing) + `pdd-development-economics`.
- "We're late" → `pdd-project-management` (critical path, acceleration, corrective actions).
