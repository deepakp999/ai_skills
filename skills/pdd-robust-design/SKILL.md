---
name: pdd-robust-design
description: Make a product perform well despite variation using robust design / Taguchi-style design of experiments - parameter (P) diagram of control factors, noise factors and performance metrics, objective functions (larger/smaller/target-is-best, signal-to-noise), experimental plans (full and fractional factorial, L4/L8/L9 orthogonal arrays, one-factor-at-a-time), handling noise (inner/outer arrays, replicates, compounded noise), randomization, analysis of means and factor effects charts, selecting and confirming setpoints. Use for DOE, parameter tuning, A/B/multivariate test design, reliability under real conditions, tolerance and setpoint decisions.
---

# Robust Design (Design of Experiments)

Part of the **product-design-development** suite (Ulrich, Eppinger & Yang, ch. 15). Can refine specs in concept development; used most in detail design ("parameter design"). Experiments run on physical or analytical prototypes (`pdd-prototyping`); metrics come from `pdd-product-specifications`.

A **robust product** performs as intended under non-ideal conditions. **Noise** = uncontrolled variation (manufacturing variation, material properties, operating conditions and user scenarios, deterioration, misuse). **Robust design** improves performance while minimizing noise effects by finding **robust setpoints** — design-parameter values where performance is good and *insensitive* to variation.

**Key idea:** exploit non-linearity. Many setpoint combinations give the same mean; choose the one where the response curve is flat for the noisy factors (e.g., choose B where sensitivity to B is low, and adjust the mean with a linear factor A).

DOE complements, not replaces, technical knowledge: use understanding to pick factors, use results to improve models. Advanced DOE/ANOVA benefits from a statistician.

## Seven steps
### 1. Identify control factors, noise factors, performance metrics → P-diagram
```
Control factors (design variables we set)  →  [ System / process ]  →  Performance metrics
                                     ↑
                  Noise factors (can't control in production/use)
```
- **Control factors**: tested at 2–3 discrete levels (materials, dimensions, tolerances, stiffness, friction, processes, operating instructions).
- **Noise factors**: if controllable in the lab, vary deliberately; otherwise let them vary naturally.
- **Performance metrics**: 1–2 key specs where robustness matters.
Many candidate factors? Narrow with analytical models or a 2-level **screening experiment**, then a finer experiment on the vital few.

### 2. Formulate an objective function (η)
| Type | Use when | Common forms |
|---|---|---|
| Larger-is-better (maximize) | Strength, max load | η = μ or μ² |
| Smaller-is-better (minimize) | Error, displacement | η = μ or σ²; or maximize 1/μ, 1/σ² |
| Target-is-best | Hit a nominal value | maximize η = 1/(μ − t)² |
| Signal-to-noise (Taguchi) | Robustness: mean vs variance | maximize η = 10·log₁₀(μ²/σ²) |
μ = mean of observations for a test condition, σ² = variance across noise. Changing the mean is usually easy; reducing variance is hard — so track variance explicitly. Many practitioners use two objectives (e.g., mean and range across noise conditions) rather than one combined S/N ratio, for more control over the trade-off.

### 3. Develop the experimental plan
Trade cost per trial vs information:
- **Full factorial** — all combinations, nᵏ trials (2⁷ = 128); all interactions; practical for ≤4–5 factors or cheap simulations.
- **Fractional factorial** (½, ¼, ⅛…) — balanced subset; interactions confounded with each other/main effects.
- **Orthogonal arrays** (L4, L8, L9, L16, L18, L27…) — smallest balanced fractional plans that still give main effects (confounded with interactions); very efficient.
- **One factor at a time** — 1 + k(n−1) trials; unbalanced, generally poor; but an **adaptive** one-at-a-time version can beat orthogonal arrays when interactions are strong.

**L4 (3 factors, 2 levels)**
| Run | A | B | C |
|---|---|---|---|
| 1 | 1 | 1 | 1 |
| 2 | 1 | 2 | 2 |
| 3 | 2 | 1 | 2 |
| 4 | 2 | 2 | 1 |

**L8 (up to 7 factors, 2 levels)**
| Run | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 |
| 3 | 1 | 2 | 2 | 1 | 1 | 2 | 2 |
| 4 | 1 | 2 | 2 | 2 | 2 | 1 | 1 |
| 5 | 2 | 1 | 2 | 1 | 2 | 1 | 2 |
| 6 | 2 | 1 | 2 | 2 | 1 | 2 | 1 |
| 7 | 2 | 2 | 1 | 1 | 2 | 2 | 1 |
| 8 | 2 | 2 | 1 | 2 | 1 | 1 | 2 |

**L9 (up to 4 factors, 3 levels)**
| Run | A | B | C | D |
|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 2 | 2 | 2 |
| 3 | 1 | 3 | 3 | 3 |
| 4 | 2 | 1 | 2 | 3 |
| 5 | 2 | 2 | 3 | 1 |
| 6 | 2 | 3 | 1 | 2 |
| 7 | 3 | 1 | 3 | 2 |
| 8 | 3 | 2 | 1 | 3 |
| 9 | 3 | 3 | 2 | 1 |

**Testing noise factors**
- Assign noise factors to extra columns of the array (treat as variables).
- **Outer array**: for each inner-array row, test combinations of noise factors (e.g., an L4 outer array → 4 replicates per row).
- **Replicates** with natural noise (randomize order!).
- **Compounded noise**: combine noise factors into a few representative or extreme conditions (e.g., N− best case, N+ worst case) → 2 replicates per row (L8 × 2 = 16 runs).

### 4. Run the experiment
**Randomize run order** so drifts over time don't masquerade as factor effects (a factor whose column changes halfway through would absorb any drift). If some factors are hard to change, partially randomize and rely on confirmation runs.

### 5. Analyze — analysis of means & factor effects charts
1. Compute the objective(s) per row (e.g., average and range across N−/N+).
2. **Factor effect** of a level = mean of the objective over all rows at that level (L8: A1 = rows 1–4; E2 = rows 2, 4, 5, 7).
3. Plot **factor effects charts** — one line per factor, levels on x, objective on y — one chart per objective (mean; variance/range or S/N).
4. Classify: **robustness factors** (strongly affect variance) and **scaling/adjustment factors** (affect mean, little effect on variance); factors with no effect → set by cost.
ANOVA tests statistical significance relative to experimental error (more assumptions; get expert help).

### 6. Select and confirm setpoints
Choose levels that minimize variance using robustness factors, then tune the mean with scaling factors; resolve trade-offs where a factor's best mean level differs from its best variance level. The chosen combination is usually not a tested row → **run a confirmation test** (also checks the no-interaction assumption).

### 7. Reflect and repeat
Reconsider trade-off factors; explore interactions (assign interaction columns, larger fractional factorial, adaptive OFAT); fine-tune between/beyond tested levels; add omitted control or noise factors. Did we run the right experiments? Is the result acceptable? Could another round pay off?

## Caveats
Analysis of means assumes additive, independent factor effects; real systems have interactions (usually smaller than main effects) — hence confirmation runs. Simulations calibrated with physical data can stand in for expensive tests (e.g., crash simulation).

## Output
```
P-diagram (control / noise / metrics; chosen subset)
Objective function(s)
Design: array, factor-level assignment, noise strategy, # runs, randomized order
Results table: | Run | factors… | N− | N+ | mean | range/S/N |
Factor effects (per objective) and classification
Selected setpoint + confirmation result
Next round plan
```

## Digital / AI adaptation
Control factors: model choice, temperature, prompt variants, retrieval top-k, chunk size, timeouts, cache settings, UI variants. Noise factors: input phrasing/language, data quality, load, user segments, upstream API latency. Metrics: task success, accuracy, latency, cost. Run orthogonal arrays over configurations against an eval set with noise conditions (clean vs messy inputs) to find robust configurations; use multivariate test designs instead of one-change-at-a-time A/B tests.
