---
name: pdd-industrial-design
description: Plan and assess industrial design / user experience for a product - rate how much a product depends on ID (user experience and aesthetic needs), weigh ID costs vs benefits, use ID for corporate identity and visual equity, run the ID process (needs, sketches, soft models, renderings and hard models, control drawings, coordination), time ID for technology-driven vs user-driven products, and score finished design quality on usability, emotional appeal, maintainability, resource use and differentiation. Use for UX/UI or physical design strategy, design reviews, design budgets, and brand-consistent product look and feel.
---

# Industrial Design (ID) & User Experience

Part of the **product-design-development** suite (Ulrich, Eppinger & Yang, ch. 11). Runs in parallel with the main process: needs (`pdd-customer-needs`), concepts (`pdd-concept-generation`/`-selection`), testing (`pdd-concept-testing`) and prototyping (`pdd-prototyping`).

ID designs the aspects of a product that relate to the user — **aesthetics** (how it looks, sounds, feels, smells) and **user experience/ergonomics** (how it is used). It is not "gift-wrapping" after engineering: technology alone rarely sustains advantage, and design-competent firms grow revenue and returns faster.

**Guiding ideas from design history** (useful as review lenses): form follows function; human-centred ergonomics ("design around the person"); **MAYA** — Most Advanced Yet Acceptable (novel enough to attract, familiar enough not to repel); simplicity and user-centred design; Dieter Rams' ten principles of good design — innovative, useful, aesthetic, understandable, unobtrusive, honest, long-lasting, thorough to the last detail, environmentally friendly, as little design as possible.

## Tool 1 — How important is ID to this product?
Rate each Low / Medium / High with a one-line explanation:

**User experience needs**
- **Usability** — how important is ease of use (frequent or rare-but-critical use, many features/modes)?
- **Ease of maintenance** — frequent service/repair (or better, eliminate it)? Do features communicate procedures?
- **Complexity of interactions** — how many interactions/functions?
- **Familiarity of interactions** — incremental vs novel interface needing research?
- **Safety** — how prominent are safety concerns?

**Aesthetic needs**
- **Visual product differentiation** — stable markets/technology or new-to-world products depend heavily on it.
- **Pride of ownership, image, style** — trend-setting, rugged, conservative…
- **Team motivation** — an early, attractive concept gives everyone a concrete vision.
```
| Need | Low | Med | High | Explanation |
```
The more seen/used by people, the more ID matters. Typical ID spend ranges from tens of thousands (industrial equipment) to millions (cars); as % of development budget from ~1% (aircraft) to ~20–30% (handheld devices, small appliances).

## Tool 2 — Is ID worth the investment?
**Costs**: direct (designer hours — roughly $100–400/h, models, materials); manufacturing (finishes, shapes, tooling — but early ID can also *reduce* cost with manufacturing engineers); time (more iterations may delay launch).
**Benefits**: product appeal, satisfaction, brand identity, differentiation → price premium and/or share. Evidence links aesthetics to price but not to manufacturing cost; most ID-consultant projects were profitable with sizable sales increases.
**Quick calculation**: price premium × lifetime volume, or extra units × margin, vs ID cost (use `pdd-development-economics` for the full model).

## Tool 3 — Corporate identity / visual equity
Consistent, recognizable form, color, materials, interaction patterns across products build **visual equity** that transfers reputation to new products (e.g., consistent button layout across a range; signature grips; clean minimal lines). Check every new design against the brand's visual language.

## Tool 4 — The ID process
1. **Investigate customer needs** — designers join interviews/observations; they excel at spotting interaction issues.
2. **Conceptualization** — many quick sketches of form and user interface, co-designed with engineers working on technical concepts; group and evaluate with the team on needs, feasibility, cost, manufacturing.
3. **Preliminary refinement** — full-scale **soft models** (foam, foam-core) of promising concepts; touch, feel, modify; involve marketing and sometimes customers. Build as many as budget allows; more for hard-to-visualize concepts.
4. **Further refinement & final concept selection** — **renderings** (2D/3D, color studies, in-use scenes, alternative layouts) and a few **hard models** (realistic look, feel, weight, finish; some working buttons/sliders; costly) for customer feedback, trade shows and management buy-in; test in use cases (e.g., balance, grip styles).
5. **Control drawings or models** — document functionality, features, sizes, colors, materials, finishes (CMF), key dimensions; hand to engineering for detail design.
6. **Coordinate** with engineering, manufacturing and vendors through to production.

## Tool 5 — Timing: technology-driven vs user-driven
Place the product on the continuum (hard disk → laptop → phone → coffeemaker → office chair). Classifications shift as markets mature (first EVs were tech-driven; later competition moved to design).
| Activity | Technology-driven | User-driven |
|---|---|---|
| Customer needs | Little early involvement; joins later | Works closely with marketing; joins interviews & observation |
| Concept generation & selection | Ensures human factors, UI, safety, maintenance | Generates multiple concepts via the ID process |
| Concept testing | Helps engineering build prototypes | Leads model creation for customer tests |
| System-level design | Little involvement | Narrows and refines concepts |
| Detail design & refinement | Packages the product after engineering details | Selects final concept, coordinates with engineering, manufacturing, marketing |
ID is a sub-process **in parallel**, not separate; for user-driven products it may dominate.

## Tool 6 — Assess ID quality (finished product or design review)
Rate Low/Medium/High with explanation in five categories:
1. **Usability** — do features communicate their operation? intuitive? all features safe? all users and uses considered? (+ product-specific: grip for hand sizes, reachable buttons, obvious on/off, screen tasks easy)
2. **Emotional appeal** — attractive, exciting, expresses quality, evokes good images, pride of ownership (users, team, sales)? (sound of a car door, solid feel of a tool, looks good on the counter)
3. **Ability to maintain and repair** — is maintenance obvious and easy; do features communicate disassembly/assembly? (clear a paper jam, clean a food processor, change batteries)
4. **Appropriate use of resources** — were resources well spent on real needs? right materials (cost/quality)? over- or under-designed? environmental factors considered?
5. **Product differentiation** — recognizable in store, memorable from ads, recognizable on the street, consistent with corporate identity?

## Output
```
ID importance assessment (Tool 1 table) → ID involvement level & timing
ID budget & expected benefit
Design language / visual-equity guidelines
Concept sketches → soft models → renderings/hard models → control drawings (status)
ID quality scorecard (Tool 6)
```

## Digital / AI adaptation
"ID" ≈ product/UX/UI design. Soft models = paper prototypes and wireframes; renderings = high-fidelity mockups; hard models = clickable prototypes; control drawings = design system specs (tokens, components, states). Maintenance = error recovery, settings, admin flows. For AI products add trust cues, explanation, undo/override and graceful failure to the usability review; MAYA applies strongly to novel AI interactions.
