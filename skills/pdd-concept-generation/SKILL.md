---
name: pdd-concept-generation
description: Generate product concepts systematically - clarify and decompose the problem (black-box function diagram, functional decomposition, user-action or needs decomposition), pick critical subproblems, search externally (lead users, experts, patents, literature, benchmarking related products), search internally (individual then group brainstorming, analogies, wish-and-wonder, SCAMPER, related/unrelated stimuli, gallery method, TRIZ contradictions), then explore with concept classification trees and concept combination tables. Use for ideation, brainstorming solutions, design alternatives, "how could we build this", or when a team is stuck on one idea.
---

# Concept Generation

Part of the **product-design-development** suite (Ulrich, Eppinger & Yang, ch. 7). Inputs: needs (`pdd-customer-needs`) and target specs (`pdd-product-specifications`). Output: 10–20 serious concepts (from hundreds of fragments) for `pdd-concept-selection`.

A **product concept** = approximate description of technology, working principles and form — how the product will satisfy the needs; usually a sketch or rough 3D model plus short text. A poor concept can rarely be rescued later, and concept generation is cheap (often <5% of budget, ~15% of time) — so be thorough.

**Dysfunctions to prevent:** only 1–2 alternatives (from the loudest people); ignoring concepts used by other firms and industries; only 1–2 people involved; poor integration of partial solutions; whole categories of solutions missed.

The method also applies to subsystems and components, not just whole products. It is iterative.

## Step 1 — Clarify the problem
- Make sure everyone knows the mission statement, needs and target specs; note the mission's assumptions (they bound the space — decide consciously how broad: "fasten roofing" vs "better handheld nailer" vs "faster pneumatic nailer").
- Quantify key needs (energy, speed, forces, volumes, latency…).

**Decompose into simpler subproblems**
- **Functional decomposition**: draw the product as one **black box** with input/output flows of **energy** (thin line), **material** (thick line) and **signal** (dashed). Then split into **3–10 subfunctions** connected by those flows, refining until each is simple. Phrase subfunctions solution-neutrally ("isolate nail", not "index coil into slot"). Getting started: diagram an existing product; diagram an arbitrary concept then generalize; follow one flow (e.g., material) and list the operations. Make several drafts; there is no single right diagram. If flows are hard to identify, a plain list of subfunctions is fine.
- **Decomposition by sequence of user actions** — for simple-technology, high-interaction products (move tool to area → position precisely → trigger).
- **Decomposition by key customer needs** — when form, not working principle, is the problem (toothbrush, containers).
- **Focus on critical subproblems** — those most critical to success and most likely to benefit from novel solutions; consciously defer the rest (e.g., solve energy storage/conversion first, user interface later).

## Step 2 — Search externally (expand, then focus)
Existing solutions are quicker and cheaper; spend creativity where no good solution exists. A conventional solution for one subproblem plus a novel one for another often wins.
1. **Lead users** — in the target market *and* in markets for products sharing subfunctions; they may have built solutions.
2. **Experts** — related-product firms, consultants, faculty, supplier technical reps (suppliers often help free if you may buy). Always ask "who else should I talk to?" — second-generation leads are often best.
3. **Patents** — rich technical detail; shows what is protected (avoid or license) and what's free (expired, or foreign without coverage). Use online keyword search. See `pdd-patents-ip`.
4. **Published literature** — journals, conference papers, trade magazines, government reports, product announcements, engineering handbooks. Manage keyword breadth vs result count.
5. **Benchmark related products** — direct competitors and products in other markets with related subfunctions (find what they're called and how cataloged; industrial directories). Buy and **tear down** to learn principles and suppliers.

## Step 3 — Search internally (brainstorming)
Five guidelines:
1. **Suspend judgment** — turn criticism into improvement suggestions or alternatives.
2. **Generate lots of ideas** — quantity lowers the bar and each idea stimulates others.
3. **Welcome seemingly infeasible ideas** — others can repair them; they stretch the space.
4. **Sketch a lot** — quality doesn't matter; add key dimensions.
5. **Build sketch models** — foam, clay, cardboard, 3D prints; low fidelity is faster and judged more novel; build several in parallel.

**Individual + group**: people working alone generate more and better concepts than the same people together; groups build consensus, share information and refine. Ideal: several hours alone (e.g., each person ≥10 concepts for 1–2 assigned subproblems), then a group session to discuss and extend. Scheduled group sessions guarantee the time gets spent.

**Hints**
- **Make analogies** — what else solves a related problem? natural/biological analogies? the same problem at much larger/smaller scale (pile driver → multi-blow nailer)?
- **Wish and wonder** — "I wish we could…", "I wonder what would happen if…"
- **Distort ideas (SCAMPER)** — Substitute, Combine, Adapt, Modify/Magnify/Minimize, Put to other uses, Eliminate, Reverse/Rearrange.
- **Related stimuli** — pass idea lists to a neighbour; use need statements and use-environment photos.
- **Unrelated stimuli** — random photos/objects (synectics), go out and photograph random things.
- **Quantitative goals** — e.g., 10–20 concepts each.
- **Gallery method** — one concept per sheet on the walls; circulate, explain, improve, spawn related ideas.
- **TRIZ** — state the contradiction (improving A worsens B, e.g., power vs weight); the 39×39 contradiction matrix suggests some of 40 inventive principles (e.g., periodic action: replace continuous action with impulses). Even without full TRIZ, "find the conflict and resolve it" is a strong heuristic.

**Fragment list per subproblem**
```
Subproblem: Store/accept energy → chemical reaction gas, gunpowder, fuel-air combustion, compressed air, CO2 tank, wall outlet, battery, fuel cell, flywheel, human power, solar...
Subproblem: Apply energy to nail → single impact, multiple impacts (tens), multiple (thousands), push, twist-push
```

## Step 4 — Explore systematically
Combining all fragments explodes (15×15×15 = 3,375), so use two tools:

**Concept classification tree** — split the solution space for one subproblem into distinct branches (e.g., energy source: chemical {fuel-air, explosive} / pneumatic / hydraulic / electrical {wall outlet, battery, fuel cell} / nuclear). Build it on the subproblem whose solution **most constrains the others**. Benefits:
1. **Prune** less promising branches (carefully).
2. **Identify independent approaches** — assign branches to sub-teams.
3. **Expose imbalance** — branches that got little thought.
4. **Refine the decomposition per branch** — e.g., electrical can't deliver the peak power directly → add "accumulate energy" subfunction.

**Concept combination table** — columns = subproblems (for one branch), rows = fragments; pick one per column (e.g., 4 × 2 × 3 = 24 combinations) and develop each promising combination into an integrated concept with sketches and creative thought (a combination is a prompt, not a solution).
```
| Convert energy | Accumulate energy | Apply to nail |
| Rotary motor + transmission | Spring | Single impact |
| Linear motor | Moving mass | Multiple impacts |
| Solenoid | | Push |
| Rail gun | | |
→ C1: solenoid + spring + multiple impacts — description/sketch
```
Tips: eliminate infeasible fragments first (cuts combinations); include only **coupled** subproblems (those evaluable only in combination); tables lose value beyond 3–4 columns. Expect several trees and tables, interleaved with more search and re-decomposition. Return later to the deferred subproblems (UI, form, configuration) for the narrowed set.

## Step 5 — Reflect (throughout)
- Are we confident the solution space has been fully explored?
- Are there alternative function diagrams? Alternative decompositions?
- Have external sources been thoroughly pursued?
- Have everyone's ideas been accepted and integrated?
- Did we spend too long on a branch we should have pruned earlier?

## Output
```
Problem statement & assumptions:
Function diagram (black box → subfunctions, flows):
Critical subproblems (now) / deferred subproblems:
External search log: | Source | Finding | Applies to subproblem |
Fragments per subproblem:
Classification tree(s): branches, pruned branches + reason
Combination table(s):
Concept set (10–20): | ID | Name | Working principle | Sketch/description | Key risks |
```

## Digital / AI adaptation
Flows become data, control/events and user input. Subfunctions e.g.: capture input → understand intent → retrieve knowledge → decide/act → present → learn from feedback. Classification tree candidates: interaction mode (chat, form, embedded, autonomous), automation level (assist / approve / autonomous), architecture (rules, classic ML, LLM + RAG, agentic). External search: GitHub, papers, product teardowns via free trials, app-store reviews, API marketplaces.
