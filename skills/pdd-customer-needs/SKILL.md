---
name: pdd-customer-needs
description: Identify customer needs with the voice-of-customer method - plan whom to interview (customer selection matrix, lead and extreme users), run interviews and observation with an interview guide, capture data in a customer data template, translate statements into well-formed need statements, cluster into a primary/secondary hierarchy, rate importance with a survey, and flag latent needs. Use for user research, discovery interviews, requirements gathering, jobs-to-be-done, understanding what users want, or turning interview notes into needs.
---

# Identifying Customer Needs

Part of the **product-design-development** suite (Ulrich, Eppinger & Yang, ch. 5). Input: mission statement (`pdd-product-planning`). Output: a hierarchical, weighted needs list feeding `pdd-product-specifications`, `pdd-concept-generation` and `pdd-concept-selection`.

**Philosophy:** build a high-quality information channel directly from customers to the people who design the details (engineers, designers). They must meet customers and experience the use environment themselves.

**Needs vs specs:** needs are solution-neutral (independent of any concept); specs depend on the chosen concept. "Need" covers wants, attributes, requirements.

**Latent needs** — real but not yet recognized by most customers or met by products (e.g., camera in phone, hands-free tailgate). Meeting them surprises and delights; once revealed they become must-haves. Finding them is a core capability.

Goals: focus on needs; find latent and explicit needs; create a fact base for specs; archive the needs work; miss nothing critical; build shared team understanding.

## Step 1 — Gather raw data

**Methods**
| Method | Notes |
|---|---|
| Interviews (recommended primary) | 1 customer, 1–2 h, in their environment; 2 interviewers (one asks, one notes) |
| Focus groups | 8–12 people, ~2 h, moderator; good for letting managers/team observe; one 2-h group ≈ two 1-h interviews in needs found |
| Observation of use | Passive or side-by-side; try the product or a surrogate task yourself; best for latent needs |
| Surveys | Not for initial discovery (miss use context and latent needs); use later for importance |

**How many:** <10 interviews is too few, ~50 too many for one segment; ~30 interviews found ~90% of needs in one study. Run sequentially and stop when no new needs appear. ≥10 per distinct segment. Split a large team into pairs to cover more.

**Whom — customer selection matrix**
```
| Segment \ Customer type | Lead users | Users | Buyers/retailers | Other stakeholders |
| Segment A (e.g., homeowner) | 5 | 5 | 5 | |
| Segment B (e.g., contractor) | 5 | 5 | | |
```
- **Lead users**: feel needs months/years before the market and benefit greatly from solutions; can articulate needs; may have built workarounds.
- **Extreme users**: unusual use or special needs (limited dexterity, very frequent use, very large/complex setups, unusual applications) — reveal latent needs useful to the mainstream.
- Always include end users; add purchasers and other stakeholders where important.
- Find them via sales force (beware bias), online search, communities/social networks, email.

**Interview guide** (after introductions and purpose):
- When and why do you use this type of product?
- Walk us through a typical session using the product.
- What do you like about existing products?
- What do you dislike about existing products?
- What issues do you consider when purchasing?
- What improvements would you make?

**Interviewing tips**: go with the flow (data over finishing the guide); use props — own, competitor and related products, maybe early concepts at the end; suppress your technology hypotheses — when customers propose a feature, probe for the underlying need; have them demonstrate the product/task; chase surprises (latent needs hide in jokes, offhand suggestions, frustrations); watch non-verbal cues (comfort, image, style); comply with data-privacy rules. For a revolutionary product, ask about the task/situation rather than the product.

**Documentation**: notes with verbatim quotes (transcribe/debrief right after); audio (easy, slow to transcribe, can intimidate); video (focus groups, use environment, onboarding new team members, management); still photos (unobtrusive, good quality, no dynamics). Send thank-you notes — you'll need these customers again.

**Customer data template** (fill right after each interview; >50 statements per interview is typical):
```
Customer: | Interviewer(s): | Date: | Currently uses: | Type of user: | Follow-up OK?:
| Question/Prompt | Customer statement / observation (verbatim) | Interpreted need | Latent? (!) |
| Typical uses | "I have to turn it on and off when it gets too hot" | The thermostat maintains a comfortable temperature without user action | |
| Dislikes | "I forget to turn it off when we leave" | The thermostat saves energy when no one is home | ! |
```

## Step 2 — Interpret raw data as need statements
Have more than one person translate (analysts differ). Five guidelines:

| Guideline | Customer statement | Right | Wrong |
|---|---|---|---|
| **What, not how** | "I'd like my phone to adjust my thermostat" | Can be controlled remotely without a special device | Comes with an iPhone app |
| **As specific as the raw data** | "I have separate heating and cooling systems" | Can control separate heating and cooling systems | Is versatile |
| **Positive, not negative** (unless awkward) | "Tired of standing in front of it to program it" | Can be programmed from a comfortable position | Does not require standing in front of it |
| **Attribute of the product** (or of the user if needed) | "I have to override it if I'm home unexpectedly" | Automatically responds to an occupant's presence | Occupant presence triggers mode change |
| **Avoid "must"/"should"** | "Worried about online security" | Controls are secure from unauthorized access | Must be secure… |

The list is the superset of all customers' needs. Record conflicting and infeasible needs too — resolve them later in specs and concepts.

## Step 3 — Organize into a hierarchy
Typically 50–300 statements → e.g., 8 primary / 41 secondary needs.
1. One need per card/sticky (customer quote in small print).
2. Merge exact duplicates only.
3. Group by similarity **as customers see it** (3–7 cards per group) — not by technology, components or materials. Some teams let customers do the grouping.
4. Label each group with a generalizing need statement (pick one or write one) → secondary needs under a primary.
5. If >20 groups, make supergroups → three levels (primary / secondary / tertiary).
6. Review; try alternative groupings; get another team's view.
**Multiple segments**: color-code cards by segment, or cluster each segment separately when segments differ a lot or one product may not serve both.

## Step 4 — Establish relative importance
Options: team consensus (fast) or customer survey (more accurate, ~a week — recommended; other work can proceed meanwhile). Survey ≤~50 needs: skip the obviously important and the easy-to-meet; focus on needs that drive difficult trade-offs or cost. Split long lists across respondents.

**Importance survey item**
```
For each feature, rate importance 1–5 and tick if unique/exciting/unexpected:
1 Undesirable – I would not consider a product with it
2 Not important, but I wouldn't mind having it
3 Nice to have, but not necessary
4 Highly desirable, but I'd consider a product without it
5 Critical – I would not consider a product without it
____ The thermostat does not require setting time or date   [ ] unique/exciting
```
Summarize by mean, standard deviation, distribution. Mark importance with * (one to three; *** critical) and latent with !. Critical needs are rarely latent — customers expect them.

## Step 5 — Reflect
- Have we reached all important customer types in the target market?
- Did we see beyond existing products to latent needs?
- What should we follow up on?
- Which customers should stay involved during development?
- What do we know now that we didn't; what surprised us?
- Did everyone in our organization who needs to understand the customer get involved?
- How do we improve the process next time?

## Output
```
Hierarchical needs list
| ID | Primary need | Secondary (tertiary) need | Importance (1–5 / *) | Latent (!) | Segment | Source quotes |

Summary
Critical needs: ...
Latent needs (drive concept creativity): ...
Open questions / follow-ups:
```

## Digital / AI adaptation
Observation = screen-share walkthroughs, session recordings, log/process mining, support tickets; extreme users = power users, admins, users with accessibility needs, edge-case workflows. For AI agents, capture needs about trust, explainability, control/override and error recovery — they are often latent.
