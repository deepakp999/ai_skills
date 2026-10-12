---
name: pdd-concept-testing
description: Test product concepts with real target customers and forecast demand - define the test purpose, choose survey population and sample size, pick a survey format, communicate the concept (verbal, sketch, rendering, storyboard, video, simulation, looks-like or works-like prototype), measure purchase intent on the 5-box scale, and forecast sales with Q = N x A x P using calibrated top-box scores, plus sensitivity and sanity checks. Use for concept validation, resonance tests, fake-door/landing-page tests, purchase-intent surveys, demand or adoption forecasting, and go/no-go decisions.
---

# Concept Testing

Part of the **product-design-development** suite (Ulrich, Eppinger & Yang, ch. 9). Follows `pdd-concept-selection` (test only a few concepts); uses prototypes (`pdd-prototyping`); the forecast feeds `pdd-development-economics`.

A concept test (or **resonance test**) gets a **direct response from potential customers in the target market** to a description of the concept — unlike selection, which relies on team judgment. Uses: choose between concepts, improve a concept, estimate sales, decide go/no-go. Also useful when first identifying the opportunity and before committing to production.

**Skip it** if testing takes long relative to product life cycles, or costs a lot relative to just launching and iterating (some internet software). Never skip when development is huge and failure disastrous. Most products fall in between.

## Step 1 — Define the purpose (write the questions down)
- Do customers like the concept?
- Does it address their needs?
- Which of several concepts should we pursue?
- How can it be improved?
- Approximately how many units will sell?
- Should development continue?

## Step 2 — Choose the survey population
- Mirror the target market; start the survey with **screener questions** to confirm fit.
- Sample each target segment (sampling only the biggest biases the market estimate).
- You may run several tests: a small qualitative one early (~a dozen) and a large quantitative purchase-intent survey later (~1,000) for forecasts and financing.

**Sample size factors**
| Favor smaller samples | Favor larger samples |
|---|---|
| Early in concept development | Later in concept development |
| Mainly qualitative data | Quantitative demand assessment |
| Surveying is costly/slow | Surveying is cheap/fast |
| Small investment to develop & launch | Large investment |
| Large fraction of market expected to value it | Small fraction values it (need many to estimate) |
Range: ~10 (specialist medical device) to ~1,000 (mass consumer appliance).

## Step 3 — Choose the survey format
Face-to-face (intercepts, prearranged interviews, trade-show booths, focus groups of 6–12), telephone, postal mail (rare now), email (only where respondents see benefit or a relationship exists), internet (online test site; recruit via email/social).
- Each format has sampling bias (online skews tech-savvy).
- **Early, exploratory** tests: open-ended, face-to-face, with developers doing interviews themselves.
- **Focused** questions: structured formats; can hire a market research firm.
- **Forecasting** data: use third-party interviewers to avoid **sympathy bias**.

## Step 4 — Communicate the concept
Present alternatives **identically** (same medium, same detail). More realistic representations get more favorable reactions. Options, in increasing richness:
1. **Verbal description** — short paragraph/bullets (what it is, key specs, how it's used).
2. **Sketch** — annotated line drawing.
3. **Photo / rendering** — near-photo-realistic CAD or marker rendering.
4. **Storyboard** — sequence of images showing use scenarios over time.
5. **Video** — form and use in motion.
6. **Simulation** — software mimicking function/interface.
7. **Interactive multimedia** — video + interactivity (costly).
8. **Physical appearance ("looks-like") model**.
9. **Working ("works-like") prototype** — risky: respondents equate it with the product; it may perform better (premium parts) or usually worse and look worse. Can pair separate looks-like and works-like models.

**Format × communication fit**
| | Telephone | Email | Postal | Internet | Face-to-face |
|---|---|---|---|---|---|
| Verbal | ✓ | ✓ | ✓ | ✓ | ✓ |
| Sketch / photo / storyboard | | ✓ | ✓ | ✓ | ✓ |
| Video, simulation, multimedia | | | | ✓ | ✓ |
| Appearance model, working prototype | | | | | ✓ |

**Promotion level** — mirror the information a buyer would see when deciding; label promotional material as a "sample advertisement".
**Price** — omit unless the price is unusually high or low (or the category is new and buyers lack expectations); instead ask "what would you expect to pay?". If expectations differ greatly from plan, adjust the concept or retest with price.
**Forced choice** — show the concept with the leading existing products (pictures/descriptions) to estimate share; works best in narrow categories with few products.

## Step 5 — Measure customer response
Early: choose among alternatives + why + how to improve. Always: **purchase intent**, typically 5 boxes:
- Definitely would buy / Probably would buy / Might or might not / Probably would not / Definitely would not
(7-point scales or stated probabilities are alternatives.) Ask intent "within the next year" for new categories.

**Interview guide skeleton**
```
Intro & consent
Screeners (segment fit; if no → thank and end)
Current behaviour questions (how do you do X today?)
Show concept (ad / description / video)  [price if included]
Purchase intent (5-box)
Hands-on with prototype (if any) → purchase intent again
Expected price (if price not shown)
Open-ended: likes, dislikes, improvements, comparison with current solution
```

## Step 6 — Interpret
**Comparing concepts**: if one clearly dominates and respondents understood the differences, choose it; if inconclusive, decide on cost/other factors or offer variants. Beware: without price info, respondents favor the costliest concept.

**Forecasting durables** (negligible repeat purchase; consumables need trial/repeat models):
**Q = N × A × P**
- **N** = potential purchases in the period. Existing category: annual category sales. New category: number of target-market customers (defined e.g. by people with the problem; use census/demographic data and category sales volumes to estimate).
- **A** = fraction aware of the product *and* able to get it (multiply if independent; driven by distribution and promotion plans).
- **P** = **C_def × F_def + C_prob × F_prob**, where F = fraction answering "definitely" (top box) and "probably" (second box). Calibration from past products; typical ranges 0.10 < C_def < 0.50, 0 < C_prob < 0.25; with no history use **C_def = 0.4, C_prob = 0.2** (corrects respondents' overstatement).

Examples: existing category N = 150,000/yr, A = 0.25, F_def = 0.30, F_prob = 0.20 → P = 0.16 → Q = 6,000/yr. New category N = 2,000,000, A = 0.30, F_def = 0.10, F_prob = 0.05 → P = 0.05 → Q = 30,000 in year 1.

Why actual sales differ from intent: word-of-mouth/social media (not captured), fidelity of the concept description vs actual product, price differences, level of promotion.

## Step 7 — Reflect
- The **qualitative insights** from open-ended discussion are often the most valuable output early on.
- **Sensitivity** on the three levers: market size N (alternative markets), availability/awareness A (distribution partners, promotion), purchase probability P (design and advertising) — e.g., "what if a retail partner raises A by 20%?"
- Was the concept communicated so responses reflect true intent (e.g., was aesthetics visible if it's a key benefit)?
- Is the forecast consistent with sales of similar products? (If a competitor sells 1,000/yr, why would we sell 30×?)
- Document results and reconcile later with actual sales to calibrate future C values.

## Output
```
Purpose/questions:
Population, segments, screeners, sample size (why):
Format & representation:
Price shown? Y/N (why):
Results: preference shares, F_def, F_prob, expected price, key qualitative themes
Forecast: N= , A= , C_def= , C_prob= , P= , Q=
Sensitivity table & sanity check vs comparable products
Decision: pursue / improve / test again / stop
```

## Digital / AI adaptation
Concept representations: clickable Figma prototype, landing page with sign-up or "fake door", explainer video, Wizard-of-Oz (human behind the AI), concierge MVP, limited beta. Measure intent with sign-ups, pre-orders, waitlist conversion or adoption commitment from internal users. For internal tools: N = eligible users, A = fraction reached by rollout/training, P = stated adoption likelihood (calibrated with past tool rollouts).
