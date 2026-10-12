---
name: pdd-project-management
description: Plan, accelerate and run a product development project - sequential/parallel/coupled tasks, design structure matrix (DSM) and sequencing, Gantt and PERT charts, critical path, the contract book, task list, team staffing criteria and staffing matrix, schedule, budget, risk plan, acceleration guidelines (scope control, overlap, pipelining, decoupling, critical chain buffers, set-based design), execution mechanisms (meetings, schedule owner, weekly status, incentives, Scrum, traffic lights, buffer reports), corrective actions and postmortem review. Use for project plans, schedules, critical path, risk registers, status reporting, speeding up a late project, or lessons-learned reviews.
---

# Project Management for Product Development

Part of the **product-design-development** suite (Ulrich, Eppinger & Yang, ch. 19). Planning peaks at the end of concept development (contract book); execution runs through launch. Pairs with `pdd-process-and-organization` (phases, org), `pdd-prototyping` (milestones), `pdd-development-economics` (value of time), `pdd-product-architecture` (interfaces that decouple tasks).

Project management = **planning** (tasks, schedule, resources) + **execution/control** (coordination, status, corrective action). Many teams fail by losing focus during execution, not planning.

## Part A — Understanding & representing tasks
**Dependencies** (mostly information transfer): a downstream task depends on an upstream task's output.
- **Sequential** — B needs A's output (B may start with partial information but can't finish before A).
- **Parallel** — depend on the same upstream task(s) but not on each other.
- **Coupled** — mutually dependent; do simultaneously with continual exchange, or iterate with tentative results until convergence.

**Tool 1 — Design Structure Matrix (DSM)**: same tasks as rows and columns in planned execution order; mark × in a task's **row** under each task (column) whose output it needs. Read across a row = inputs; down a column = who uses this task's output.
- **Sequence (partition)** the DSM to push marks below the diagonal.
- Marks just below the diagonal → sequential chain; no marks between tasks → parallel; marks **above** the diagonal that can't be removed by reordering → **coupled block** (box it; plan iteration/co-location).
- Captures more dependencies than a network diagram without clutter; also used for organization design and simulating schedule/cost risk.
```
            A B C D E
A Task A    A . . . .
B Task B    x B . . .
C Task C    x . C x .   ← above-diagonal x: C and D coupled
D Task D    . x x D .
E Task E    . . x x E
```
**Tool 2 — Gantt chart**: bars for start/end on a timeline, fill = % complete, vertical "today" line shows ahead/behind. Doesn't show dependencies (overlapping bars may be parallel, overlapped sequential, or coupled).
**Tool 3 — PERT chart (activity on node)**: tasks with durations, links left→right; no loops, so roll coupled blocks into one task; sized blocks double as a schedule.
**Critical path** = longest chain of dependent tasks → minimum project duration; any delay on it delays the project; other paths have slack. Software computes it.

## Part B — Baseline project plan (the contract book)
**Contract book** — the agreement between team and senior management (sometimes signed). Typical contents (1–5 pages each): mission statement; customer needs list; competitive analysis; product specifications; concept sketches; concept test report; sales forecast; economic analysis/business case; environmental impact assessment; manufacturing/operations plan; task/resource list; DSM; team staffing & organization; schedule (Gantt); budget; risk plan; project performance measurement plan; incentives.

**1. Task list** — 50–200 items at a level fitting the project (days per person for a small product; weeks for small groups on a medium product; months per subteam for a car — very large tasks become sub-projects). Build phase by phase (system design, detail design, test & refine, ramp-up); reuse a similar past project's list. For each task: predecessors (→ DSM/network) and **effort** (person-hours/days/weeks of actual working time) or required duration.
```
| ID | Task | Phase | Predecessors | Effort | Duration | Owner/skill |
```
**2. Team staffing & organization** — criteria for fast teams: ≤10 members; volunteers; on the team from concept to launch; full-time; report directly to the team leader; key functions included (at least marketing, design, manufacturing, product management); within conversational distance. Reality: specialists are scarce, people have other duties, workload rises toward ramp-up then falls → team grows and shrinks. Build a **staffing matrix** (people/roles × periods, fraction of full time; cap people at e.g. ~70% to allow for training, time off and interruptions).
**3. Schedule** — (1) use DSM/PERT for dependencies; (2) place **milestones** on a Gantt (design reviews/gates, alpha/beta prototypes, interfaces to other projects, fixed events like trade shows — powerful integrating anchors); (3) schedule tasks considering staffing and critical resources; (4) adjust milestones to fit. One credible schedule the team believes in.
**4. Budget** — staff (staffing plan × loaded rate: loaded salary ≈ 2–3× salary; typical $2k–5k per person-week), materials and services, project capital (facilities, equipment, tooling), outside development resources, operational costs (e.g., pilot production, approvals). Add **contingency**: early estimates may be ±30–50%, late ±5–10%.
**5. Risk plan** — ask what uncertainties could hurt technical, financial or schedule performance (task timing, technology, market acceptance, material costs, competition, regulation, suppliers). Rate likelihood and impact; plan actions; schedule actions for the biggest risks **early**. Fewer surprises for management.
```
| Risk | Likelihood | Impact | Actions to minimize | Owner | Trigger/date |
```
**6. Modify the baseline** — consciously trade development time, development cost, unit cost, performance and risk (use `pdd-development-economics` for the value of time); add contingency plans. The usual change is **schedule compression** →

## Part C — Accelerating projects (mostly decided during planning)
**Whole project**
- **Start early** — a month lost waiting for a kickoff/approval meeting costs the same as a month at the end.
- **Manage scope** — stop feature creep / "creeping elegance"; freeze the design; save ideas for the next generation.
- **Facilitate essential information exchange** — co-location, frequent meetings, collaboration tools; DSM coupled blocks show where.
**Critical path** (only shortening it shortens the project; worth a lot per week)
- **Complete critical tasks faster** — label them critical, start early, protect from interruption, spend more (path may shift).
- **Move tasks off the critical path** — redefine tasks or architecture to make sequential tasks parallel (e.g., site selection in parallel with device selection, managed by frequent talks).
- **Eliminate critical tasks** — reduce scope if acceleration value exceeds lost sales.
- **Aggregate safety time (Critical Chain)** — estimates often double nominal duration with hidden safety that gets consumed; strip it from critical tasks and put one **project buffer** at the end (~20–50% of the shortened critical path) plus **feeder buffers** where non-critical paths join.
- **Eliminate waiting for critical resources** — pay for priority, reserve supplier capacity, pre-order assortments, fix approval bottlenecks.
- **Overlap selected critical tasks** — pass partial information earlier/more often; freeze critical upstream information early.
- **Pipeline large tasks** — split into chunks passed on as finished (qualify vendors part by part as the BOM emerges).
- **Outsource some tasks** when resource-constrained.
**Coupled tasks**
- **Iterate faster** — more frequent, quicker exchanges (co-design sessions on shared CAD/screens).
- **Decouple** — define interfaces early so components proceed in parallel (`pdd-product-architecture`).
- **Set-based design** — exchange ranges/sets of values instead of point estimates to converge faster.

## Part D — Execution
**Coordination mechanisms**
- **Informal communication** — co-locate the core team; communication probability drops sharply beyond a few metres; electronic channels work best among people who already know each other.
- **Meetings** — regular time and place, at least weekly (2×/week or daily for some teams); short (stand-up, agenda, facilitator, before lunch/end of day); fewer needed when co-located.
- **Schedule display** — one owner (leader on small projects; a project analyst on larger ones) updating the Gantt/PERT weekly.
- **Weekly status memo** — 1–2 pages: last week's accomplishments, decisions, events; next week's key events; updated schedule.
- **Incentives** — project-based measures; both project and functional managers contribute to reviews, raises and bonuses.
- **Process documents/information systems** — each method's artifact (segment map, roadmap, needs list, function diagrams, selection matrices, needs–metrics matrix, schematic, differentiation/commonality plans, BOM, prototype plans, ID assessment, test reports, NPV model, contract book, DSM, Gantt, staffing matrix, backlog, buffer report, risk analysis, postmortem) both drives decisions and documents them.
- **Scrum** — daily stand-up (did / doing / blockers), scrum master removes impediments, prioritized **product backlog**, fixed-length **sprints** (e.g., 2 weeks) each ending in a reviewable deliverable; minimal upfront planning, dynamic correction. Usable beyond software.
**Assessing status**
- Leader's direct observation (works up to ~50 people); independent expert assessments.
- **Project/phase reviews** by senior managers or technical peers — useful closure points, but too many cost prep time, scheduling delays and meddling.
- **Buffer report** (Critical Chain) — if buffers are consumed faster than the critical path progresses, the end date is at risk.
- **Traffic lights** — green on track; yellow concern, needs help/resources; red known problem (behind, specs not met).
**Corrective actions** (usually to stop slippage)
- Change meeting timing/frequency (weekly → daily; Friday deadlines); video for remote members.
- Change staff — add if grossly understaffed, remove if overstaffed; adding people late to a late project can delay it further.
- Co-locate the team (or virtual co-location).
- Get more time/effort — relieve people of other projects; short bursts of extra hours are OK, sustained 60–70 h weeks cause burnout.
- Focus effort on critical tasks — temporarily drop non-critical work.
- Engage outside resources for well-defined, loosely coupled tasks.
- Change scope or schedule — when all else fails, narrow scope, change the goal or extend the schedule to keep the plan credible.

## Part E — Postmortem project evaluation
Open discussion (ideally facilitated by an uninvolved project leader/consultant; ~2 h with core team):
- Did we achieve the mission statement's strategic, technical and financial goals?
- Which aspects of performance (development time, development cost, quality, manufacturing cost, environmental impact) were most positive / most negative?
- Which tools, methods and practices helped / hurt?
- What problems did we hit?
- What specific actions should the organization take?
- What technical lessons should be shared, and how?
Write a **postmortem report**; with the contract book it gives "before and after" views and historical data for planning future projects.

## Output
```
Contract book outline (filled)
Task list + DSM (sequenced, coupled blocks marked) + PERT with critical path + Gantt with milestones
Staffing matrix, budget with contingency, risk plan
Acceleration options considered (with value of time)
Execution cadence: meetings, status memo, schedule owner, review gates, traffic-light/buffer reporting
Postmortem template
```

## Digital / AI adaptation
Combine milestone gates (concept approval, beta, GA) with Scrum sprints inside phases; keep a DSM of teams/services to see coupling; critical path often runs through data access, security/compliance approvals, vendor procurement and integration — start those first. Decouple with API contracts and mocks; pipeline by shipping vertical slices.
