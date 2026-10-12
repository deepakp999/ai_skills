# AI Skills

Agent skills for Claude (Claude.ai, Claude Code, Claude Agent SDK) and other agents that support the `SKILL.md` format.

## Product Design & Development suite

A coordinator skill plus 18 stage skills that take any product — physical, digital, service or AI — from opportunity to launch. Based on the method in *Product Design and Development* by Karl Ulrich, Steven Eppinger and Maria Yang (one skill per chapter). Each stage skill covers every tool from its chapter: when to use it, steps, templates, and a digital/AI adaptation.

| Skill | Use it for |
|---|---|
| [product-design-development](skills/product-design-development/SKILL.md) | **Start here.** Finds where you are, picks the process variant, routes to the stage skills, keeps the contract book |
| [pdd-process-and-organization](skills/pdd-process-and-organization/SKILL.md) | Phases and gates, process variants (stage-gate, spiral, complex system), functional vs matrix vs project teams |
| [pdd-opportunity-identification](skills/pdd-opportunity-identification/SKILL.md) | Innovation tournament, idea-generation techniques, multivoting, Real-Win-Worth-it |
| [pdd-product-planning](skills/pdd-product-planning/SKILL.md) | Portfolio, segment maps, S-curves, tech roadmaps, product-process matrix, capacity plan, mission statement |
| [pdd-customer-needs](skills/pdd-customer-needs/SKILL.md) | Interviews, lead/extreme users, need statements, need hierarchy, importance survey, latent needs |
| [pdd-product-specifications](skills/pdd-product-specifications/SKILL.md) | Metrics, needs–metrics matrix, benchmarking, target/final specs, target costing, trade-off maps, flow-down |
| [pdd-concept-generation](skills/pdd-concept-generation/SKILL.md) | Functional decomposition, external/internal search, SCAMPER, TRIZ, classification trees, combination tables |
| [pdd-concept-selection](skills/pdd-concept-selection/SKILL.md) | Pugh screening and weighted scoring matrices, sensitivity |
| [pdd-concept-testing](skills/pdd-concept-testing/SKILL.md) | Concept tests, survey design, purchase intent, Q = N × A × P demand forecast |
| [pdd-product-architecture](skills/pdd-product-architecture/SKILL.md) | Modular vs integral, chunks, interactions, postponement, differentiation/commonality platform plans |
| [pdd-industrial-design](skills/pdd-industrial-design/SKILL.md) | ID/UX importance, ID process, timing, design quality assessment |
| [pdd-design-for-environment](skills/pdd-design-for-environment/SKILL.md) | Life-cycle impacts, DFE guidelines by stage, DFE scoring, LCA |
| [pdd-design-for-manufacturing](skills/pdd-design-for-manufacturing/SKILL.md) | Sourcing, costed BOM, process cost structures, DFA, error-proofing, logistics |
| [pdd-prototyping](skills/pdd-prototyping/SKILL.md) | Prototype types and purposes, prototype planning, alpha/beta/pilot milestones |
| [pdd-robust-design](skills/pdd-robust-design/SKILL.md) | P-diagrams, orthogonal-array DOE, factor effects, robust setpoints |
| [pdd-patents-ip](skills/pdd-patents-ip/SKILL.md) | IP types, filing strategy, prior art, claims, invention disclosure (not legal advice) |
| [pdd-service-design](skills/pdd-service-design/SKILL.md) | Service concepts, process flow diagrams, minimum viable service, pilots, scaling |
| [pdd-development-economics](skills/pdd-development-economics/SKILL.md) | NPV model, sensitivities, tornado chart, trade-off rules, decision trees (includes `scripts/npv_model.py`) |
| [pdd-project-management](skills/pdd-project-management/SKILL.md) | Contract book, DSM, Gantt/PERT, critical path, staffing, budget, risk plan, acceleration, execution, postmortem |

## Marketing

| Skill | Use it for |
|---|---|
| [marketing-management](skills/marketing-management/SKILL.md) | Market & customer analysis, STP and positioning, brand equity, product/service/price/channel/communications strategy, sales force, loyalty & CLV, growth, marketing plan and metrics. Based on *Marketing Management* by Kotler & Keller. Pairs with the product design suite for go-to-market. |

## Installing

**Claude.ai / desktop app:** upload the zip of each skill folder you want (or the whole suite) under Settings → Capabilities → Skills. Install the coordinator plus whichever stage skills you need; the coordinator still works alone.

**Claude Code:** copy the folders into `~/.claude/skills/` (personal) or `.claude/skills/` in a project:

```bash
git clone https://github.com/deepakp999/ai_skills
cp -r ai_skills/skills/* ~/.claude/skills/
```

## Notes

Skill content summarises published methods in original wording; it does not reproduce the source books. Buy the books — they are worth it.
