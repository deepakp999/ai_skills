---
name: pdd-concept-selection
description: Select the best concept with a structured, team-based decision - concept screening (Pugh matrix with +/0/- against a reference), combine and improve concepts, then concept scoring with weighted, hierarchical criteria on a 1-5 scale with per-criterion reference points, weighted totals, sensitivity analysis and segment-specific matrices. Use whenever choosing between design options, architectures, vendors, features, opportunities or any alternatives where a defensible, documented decision is needed.
---

# Concept Selection

Part of the **product-design-development** suite (Ulrich, Eppinger & Yang, ch. 8). Inputs: concepts (`pdd-concept-generation`) and criteria from needs/specs. Output: 1–2 concepts for `pdd-concept-testing`. The method is reusable at every level — overall approach, subsystems, components, materials, colors, production processes, even opportunities and vendors.

Concept selection is **convergent but iterative**: the set narrows, temporarily widens as concepts are combined/improved, and narrows again.

**Methods teams actually use** (implicitly or explicitly): external decision (client picks), product champion, intuition, multivoting, online survey/crowdsourcing, pros & cons, prototype and test, **decision matrices** (this method).

**Why a structured method:** customer-focused product; competitive design (benchmarked against existing designs); better product–process coordination (manufacturing criteria included); faster (common language, fewer false starts); objective group decisions; documented rationale for new members and changes.

Two stages, each with the same six steps: **1 prepare matrix → 2 rate → 3 rank → 4 combine & improve → 5 select → 6 reflect.** Scoring can be skipped if screening yields a dominant concept.

---

## Stage A — Concept screening (Pugh method)

**1. Prepare the matrix**
- Medium: paper/whiteboard for small groups, spreadsheet for many concepts (then put concepts as rows, criteria as columns).
- Concepts across the top, each with a one-page sketch + short description, **all at the same level of detail**.
- >~12 concepts? Multivote first (each member puts 3–5 dots on favorites) to pick ~a dozen.
- **Criteria** down the side: 5–10 high-level criteria from customer needs plus enterprise needs (manufacturing cost, liability risk…). Choose criteria that differentiate; avoid many unimportant ones (all are equally weighted here).
- **Reference concept**: industry standard, best-in-class benchmark, previous generation, one of the concepts, or a composite of best features — something the team knows well.

**2. Rate** each cell vs the reference: **+** better, **0** same, **–** worse. Rate all concepts on one criterion before moving on (or concept-by-concept if very many). Use objective proxies when available (part count ≈ assembly cost; number of operations ≈ ease of use; spec metrics). Otherwise consensus or secret ballot. Note criteria needing more analysis.

**3. Rank** — sum +, 0, –; net score = (+) − (–); rank. Spot the one or two criteria that really differentiate.

**4. Combine & improve**
- Is a generally good concept degraded by one bad feature? Can a small change fix it while keeping it distinct?
- Can two concepts combine to keep the +'s and cancel the –'s?
Add new/revised concepts (e.g., "D+F", "G+") and rate them.

**5. Select** concepts to carry forward (limited by people, money, time); list issues to investigate; decide on another screening round or scoring.

**6. Reflect** — everyone should be comfortable; disagreement signals a missing criterion or unclear rating.

```
| Criterion | A | B | C | D (Ref) | E | F | G |
| Ease of handling | 0 | 0 | – | 0 | 0 | – | – |
| Ease of use | 0 | – | – | 0 | 0 | + | 0 |
| ... |
| Sum + | Sum 0 | Sum – |
| Net score |
| Rank |
| Continue? (Yes / No / Combine / Revise) |
```

---

## Stage B — Concept scoring

**1. Prepare the matrix** (spreadsheet, for sensitivity analysis)
- Concepts (now more refined) across the top.
- Criteria can be broken down **hierarchically** when broad ones don't discriminate (e.g., Ease of use → ease of injection, cleaning, loading). Secondary/tertiary customer needs make good sub-criteria.
- **Weights**: allocate 100% (or 1–5 importance), by team consensus or from customer importance data. For hierarchies, weight groups then split within groups.

**2. Rate** on a finer scale:
| Relative performance | Rating |
|---|---|
| Much worse than reference | 1 |
| Worse than reference | 2 |
| Same as reference | 3 |
| Better than reference | 4 |
| Much better than reference | 5 |
(1–9 scales are possible but cost more time.)
Avoid **scale compression**: if the overall reference is best (or worst) on a criterion, everything else squeezes into 1–3. Use **different reference points per criterion** — another concept, a benchmark product, or the spec target values. You can still keep one overall reference for competitiveness. Alternatively, rate all concepts per criterion relative to each other on a 1–9 scale without explicit references.

**3. Rank** — weighted score per concept: **Sⱼ = Σ rᵢⱼ × wᵢ**; rank by total.

**4. Combine & improve** — some of the best refinements happen now as strengths/weaknesses become clear. Write notes in cells about outstanding features to transplant.

**5. Select — with sensitivity analysis**
- Vary weights and uncertain ratings: does the winner change? A lower-scoring concept with little uncertainty may beat a higher-scoring risky one.
- Small score differences are not significant at this resolution.
- Build separate matrices with segment-specific weights to see if one concept dominates across segments.
- Carry the top 1–2 into prototyping and `pdd-concept-testing`.

**6. Reflect** — this is near the "point of no return". Review every eliminated concept: if anyone thinks a dropped concept is better than a kept one, find the missing/mis-weighted/inconsistent criterion. Also ask: how did the method help the decision; how can it be improved?

```
| Criterion | Weight | A rating | A wtd | DF rating | DF wtd | E rating | E wtd |
| Ease of handling | 5% | 3 | 0.15 | 3 | 0.15 | 4 | 0.20 |
| Dose accuracy | 25% | 3 | 0.75 | 3 | 0.75 | 2 | 0.50 |
| ... |
| Total score | | | 2.75 | | 3.45 | | 3.10 |
| Rank / Continue? |
```

---

## Caveats
- **Decomposition of quality** — the method assumes overall quality = sum of independent criteria. For products whose appeal arises from complex interactions (e.g., a racquet's feel), use prototypes/tests; see multi-attribute decision theory for non-linear cases.
- **Subjective criteria (aesthetics)** — team judgment is weak here; narrow to 3–4 and get target customers' reactions with mock-ups (`pdd-concept-testing`).
- **Notes in cells** — record outstanding positives/negatives to drive combination.
- **Include cost** — manufacturing cost/ease isn't a customer need but drives economic success; include it, plus other stakeholder needs.
- **Aggregate concepts** — if all concepts share independent sub-choices (e.g., needle type), select those separately first.
- **Use throughout development** — from single-use vs reusable down to color and material.

## Digital / AI adaptation
Typical criteria: user value/fit to key needs, accuracy/quality, latency, unit cost (infra/inference), build effort/time-to-market, integration complexity, security/compliance, vendor lock-in, maintainability, risk. Use the current production system or the manual process as the reference. Run sensitivity on weights for "cost vs quality" and "speed vs robustness".
