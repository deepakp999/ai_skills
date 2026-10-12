---
name: pdd-process-and-organization
description: Design the product development process and team organization for a project - pick the process variant (market-pull, tech-push, platform, spiral/agile, complex system, etc.), define phases and stage gates, map functional responsibilities, and choose functional vs. matrix vs. project team structure. Use when setting up a new product program, a PD playbook, stage-gate reviews, or deciding how to staff and organize a product team.
---

# Product Development Process & Organization

Part of the **product-design-development** suite (Ulrich, Eppinger & Yang, ch. 2). Use it at the very start of a product effort, or when a team's way of working is the problem.

A product development process is the sequence of steps an organization uses to conceive, design and commercialize a product. A well-defined one gives you **quality assurance** (phases + checkpoints), **coordination** (who contributes when), **planning** (milestones anchor the schedule), **management** (a benchmark to compare actual progress to) and **improvement** (a documented process can be reviewed).

Three useful lenses on any process: it is (1) a funnel — many concepts narrowed to one fully specified product; (2) an information-processing system — inputs (strategy, technology, platforms) turned into the information production and sales need; (3) a risk-management system — risks identified early and retired phase by phase.

## Tool 1 — The generic six-phase process

| Phase | Purpose | Typical outputs | Gate at end |
|---|---|---|---|
| 0 Planning | Opportunity identification, strategy, tech & market assessment | Mission statement | Mission approval |
| 1 Concept development | Needs, concepts, selection, testing | Concept, specs, economics, plan (contract book) | Concept review |
| 2 System-level design | Architecture, subsystems & interfaces, supply-chain/assembly plan | Layout, subsystem functional specs, preliminary process flow | Preliminary design review |
| 3 Detail design | Geometry, materials, tolerances, standard parts, process plans, tooling | Control documentation | Critical design review |
| 4 Testing & refinement | Alpha (production-intent parts) and beta (production-process parts, customer-tested) prototypes | Validated design, engineering changes | Production approval |
| 5 Production ramp-up | Train workforce, fix process issues, early customers, launch | Launched product | Post-launch project review |

**Function × phase responsibility grid.** Build one for the project so each function knows when it is needed. Typical entries:

| | Planning | Concept dev. | System design | Detail design | Test & refine | Ramp-up |
|---|---|---|---|---|---|---|
| Marketing | Market opportunity, segments | Customer needs, lead users, benchmarks | Product options, family plan | Marketing plan | Promotion & launch materials, field tests | Early production to key customers |
| Design/Eng. | Platform & architecture, new tech | Feasibility, concepts, ID concepts, experimental prototypes | Architecture, subsystems & interfaces, refine ID | Part geometry, materials, tolerances, ID control docs | Test performance/reliability/durability, regulatory approvals, environmental impact, design changes | Evaluate early output |
| Manufacturing | Production constraints, supply-chain strategy | Cost estimate, production feasibility | Suppliers, make-buy, final assembly scheme | Piece-part processes, tooling, QA processes, long-lead tooling | Supplier ramp-up, refine processes, train workforce | Full production |
| Others | Research: tech demos; Finance: goals; PM: resources | Finance: economics; Legal: patents | Finance: make-buy; Service: issues | | Sales: sales plan | PM: post-project review |

**The front-end (concept development) activities**, roughly in order but overlapping and iterating: identify customer needs → establish target specs → generate concepts → select concept(s) → test concept(s) → set final specs → plan downstream development; running in parallel: economic analysis, competitive benchmarking, building/testing models & prototypes. The results go into a **contract book** (mission statement, needs, concept, specs, economics, schedule, staffing, budget) — the agreement between team and management.

Sister skills for each activity: `pdd-opportunity-identification`, `pdd-product-planning`, `pdd-customer-needs`, `pdd-product-specifications`, `pdd-concept-generation`, `pdd-concept-selection`, `pdd-concept-testing`, `pdd-product-architecture`, `pdd-industrial-design`, `pdd-design-for-environment`, `pdd-design-for-manufacturing`, `pdd-prototyping`, `pdd-robust-design`, `pdd-patents-ip`, `pdd-service-design`, `pdd-development-economics`, `pdd-project-management`.

## Tool 2 — Choose the process variant

| Variant | Use when | How the generic process changes | Examples |
|---|---|---|---|
| Market-pull (generic) | Start from a market need | Full six phases | Tools, furniture |
| Technology-push | Start from a proprietary technology | Planning = match technology to market; mission assumes the tech. Risky unless the tech gives clear advantage and is hard to copy — also evaluate concepts that don't use it | Gore-Tex |
| Platform | Building on an existing proven tech subsystem | Concept dev. assumes the platform | Electronics, printers |
| Process-intensive | Production process constrains product | Specify process from the start, or co-develop product & process | Food, chemicals, chips |
| Customized | Variants of standard configurations per order | Highly structured, often automated configuration process | Motors, batteries |
| High-risk | Big technical or market uncertainty | Attack biggest risks first: early concept tests with renderings/UI prototypes, early working models, parallel solution paths; design reviews must show risk falling | Pharma, space |
| Quick-build (spiral) | Prototyping is fast and cheap | After concept dev., split features into high/medium/low priority; repeat design-build-integrate-test cycles, highest priority first; ship when time/budget runs out | Clothing, electronics |
| Digital | Software, web, apps, AI | Spiral/agile: releases planned as milestones; system design = software architecture by function; discover needs by testing evolving product with users | Apps, SaaS, agents |
| Product-service system | Product + service delivered together | Design customer experience, touchpoints and process flow; match capacity to demand (see `pdd-service-design`) | Restaurants, rentals |
| Complex system | Many subsystems | Architecture is critical; parallel subsystem teams; integration teams; heavy system test & validation | Cars, aircraft |

**Process flow diagram.** Draw the chosen flow and the gates so everyone shares it:
- Stage-gate: Planning →(Mission approval)→ Concept dev →(Concept review)→ System design →(PDR)→ Detail →(CDR)→ Test →(Production approval)→ Ramp-up →(Project review)
- Spiral: Planning → Concept → System design → [Design → Build → Test] × N, each with a cycle review → Ramp-up
- Complex system: Concept → System design → parallel [Design ↔ Test] per subsystem → Integrate & test → Validate & ramp-up

Most firms tailor their own (e.g., a 9-gate process with a checklist per gate and "select a process variant" as an early deliverable). Write a one-line goal per phase and a gate checklist.

## Tool 3 — Choose the organization structure

Individuals are linked by **reporting relationships, financial arrangements and physical layout**. Links can align with functions, projects or both.

| | Functional | Lightweight project matrix | Heavyweight project matrix | Project (incl. start-up, tiger/scrum team) |
|---|---|---|---|---|
| Who has power | Functional managers | Functional managers; PM coordinates | PM: budget, evaluation, resources | PM / CEO |
| Strengths | Deep specialization | Explicit project coordination, keeps specialization | Integration and speed, retains some specialization | Resources optimized for project; fast trade-offs |
| Weaknesses | Slow, bureaucratic cross-function coordination | More managers/admin | More managers/admin | Functional expertise can erode |
| Typical | Customized products, slight variants | Derivative products in large firms | New platforms, dynamic markets | Start-ups, breakthroughs, skunkworks |
| Key issue | Integrating functions to business goals | Balancing function vs project; evaluating people on both | | Maintaining functional expertise; sharing learning across projects |

Questions that decide it:
1. How important is cross-functional integration? (high → project/heavyweight)
2. How critical is cutting-edge functional expertise retained over generations? (high → keep functional links)
3. Can specialists be fully used on one project for most of its duration? (no → share them functionally)
4. How important is speed? (high → project)

**Distributed teams**: justified by regional market knowledge, expertise, proximity to manufacturing/suppliers, cost, capacity. Expect more iterations and coordination cost, especially for new teams; co-location is still the most effective default. Mitigate with clear interfaces, overlap hours, and periodic co-located sessions.

## Steps to apply

1. Classify the product → pick the variant (Tool 2). Products can mix (e.g., a digital product-service system → spiral + service design).
2. Draw the process flow with named gates and a one-line purpose per phase.
3. Build the function × phase responsibility grid for this project.
4. Define gate criteria (what must be true to pass) and the contract-book contents.
5. Choose the org structure using the four questions; name the PM and their authority level.
6. Reflect: does the process attack the biggest risks early? Is anyone needed but unassigned? Is the gate load proportionate to project size?

## Output template

```
Project: 
Process variant(s): ... because ...
Phase plan:
| Phase | Goal | Key deliverables | Gate & pass criteria | Owner |
Responsibility grid: (function × phase)
Organization: functional / lightweight / heavyweight / project — rationale (4 questions)
PM authority: budget? evaluation? staffing?
Distributed? sites, reasons, coordination mechanisms
Biggest risks and the phase where each is retired
```

## Digital / AI adaptation
Use spiral releases (MVP → beta → GA) as the "testing & refinement" phases, keep a real concept phase up front, and treat model evaluation, data pipelines and guardrails as "production process" work that starts early. Small cross-functional squads (heavyweight/project style) usually fit best.
