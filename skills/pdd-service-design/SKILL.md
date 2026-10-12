---
name: pdd-service-design
description: Design services and product-service systems - recognize how services differ from products (customer involvement, touchpoints, timing, capacity-demand matching, modular process architecture, repeat use, customization), write a service concept and storyboard, generate concepts by decomposing the user-action sequence, draw a service process flow diagram (acquisition/relationship, transaction, physical flows; material and information flows; touchpoints), launch a minimum viable service, prototype and pilot services, split local vs shared infrastructure, scale region by region and improve continuously. Use for service design, customer journeys, SaaS/platform operations, subscription or rental models, and any offering mixing products and services.
---

# Service Design (Product-Service Systems)

Part of the **product-design-development** suite (Ulrich, Eppinger & Yang, ch. 17). Most other stages apply unchanged to services (opportunity identification, needs, specs, concept generation/selection/testing, economics, project management, planning); DFM applies least, DFE principles still apply to operations, patents are less central (though some famous patents are service patents).

## Products vs services
**Product-service systems** bundle tangible and intangible elements (mobile network: handsets + connectivity; printers + cartridge recycling; car rental: vehicles + reservation, insurance, maintenance, billing; restaurants: food + reservations, preparation, wait service, ambiance; airlines; healthcare). Distinctive features of services:
- **Customer involvement** — customers supply inputs, make choices, interact, consume during delivery; behaviour is unpredictable so services must adapt; many **touchpoints**, each a chance to succeed, fail or innovate.
- **Timing** — waiting, timing of touchpoints, total elapsed time matter.
- **Matching capacity and demand** — produced and consumed nearly simultaneously; little inventory buffer → match closely or hold excess capacity, else queues or lost customers.
- **Modular architecture** — sequential/parallel process steps map closely to features → easy to modify, refine, extend.
- **Repeated use cycles** — acquisition and relationship management are critical.
- **Customization** — modular processes + customer involvement make per-customer tailoring cheap.

## Tool 1 — Service concept (+ storyboard)
A concept for a service is a **short narrative of the big idea**: how the service works, the sequence of events and key features (a sketch of hardware is incomplete). E.g., "Members reserve a car online for 30 min–4 h, unlock it with a card at a nearby dedicated spot, drive, return it to the same spot; billing is automatic." Elaborate with a **storyboard** — a sequence of illustrations of key steps in the experience.

## Tool 2 — Generate service concepts by decomposition
Decompose by **sequence of user actions** (or by key functions, or key needs) and list alternatives per step; combine one or more per column into a service concept (a concept combination table, see `pdd-concept-generation`).
```
| Join | Reserve | Obtain | Use | Return | Pay |
| Register / pre-register / guest / social login / employer bulk | None (first-come) / app / web / call center; fixed or open-ended | Delivered / distributed spots / regional hub / partner stores | Self / with driver | Same spot / any location | Auto-billing / in-app checkout / onboard system / kiosk |
```

## Tool 3 — Minimum viable service
Services are easy to modify, so launch the **minimal version of each process flow** quickly, learn, and add features in iterations. Ask: which steps can we deliver with the least cost and time? Which features now vs later? Use manual workarounds first (e.g., members log mileage; staff collect logs monthly) before automation (wireless telematics).

## Tool 4 — Service process flow diagram (system-level design)
List process steps, then arrange them to show:
- **Process steps** (boxes)
- **Precedence** (regular arrows)
- **Material flows** (heavy arrows)
- **Information flows** (dashed arrows)
- **Customer touchpoints** (person icons)
Organize into swim lanes:
1. **Customer acquisition & relationship management** — recruit, apply, verify, issue access, update member database.
2. **Transaction processing** — search, reserve, check out, use, return, log, confirm, bill.
3. **Physical process flow** — procure, equip, deploy, clean, service, update asset database, retire/sell.
Because services are modular, the diagram is essentially the function diagram *and* nearly the full embodiment. Use it to find innovation opportunities, waits, failure points and capacity bottlenecks. (Add a front-stage/back-stage line if useful, as in service blueprints.)
```
Lane | Step | Touchpoint? | Inputs (material/info) | Outputs | Owner/system | Time/wait | Failure modes | Capacity driver
```

## Tool 5 — Architecture for scaling: local vs shared infrastructure
Decide which process elements are **local** per market (assets/fleet, sites/parking, maintenance staff, local management and sales, partner contracts — tailored to local conditions) and which are **shared** centrally (booking platform, apps, software, support, billing). Design shared parts once for multi-market rollout.

## Downstream development
- **Prototyping a service** — approximate the process: a website or app for online services; a pilot facility or temporary location for physical services; alpha/beta labels ("in beta") signal ongoing change. Use DOE (`pdd-robust-design`) for service experiments. Real-customer tests are most realistic but risky for established businesses; pilot environments reduce risk.
- **Pilot** — small scale (e.g., one asset, ~20 participants, two months) to observe every step (joining, reserving, access…) and catch real behaviour (lost/shared access cards, keys left in the wrong place → design fixes).
- **Growing services** — usually region by region; pick early expansion markets similar to the first; use new markets to test variants (e.g., dropping a deposit and comparing outcomes); rare events (accidents, fines, lost cards) become frequent at scale → build operational processes for them.
- **Continuous improvement** — customers and employees co-produce, so feedback is easy: have everyone handle customer contacts early on, encourage employees to use the service, keep adding features and refining operations.

## Reflect
Are touchpoints designed and measured? Are waits and capacity–demand mismatches handled? Which steps are still manual, and when to automate? Is the local/shared split right for scaling? What is the plan for customer acquisition and retention?

## Output
```
Service concept narrative + storyboard
User-action decomposition with alternatives → chosen concept
Minimum viable service scope (now vs later)
Service process flow diagram (3 lanes, flows, touchpoints)
Local vs shared infrastructure map
Pilot plan & learnings; rollout sequence; improvement backlog
```

## Digital / AI adaptation
SaaS, platforms and AI agents are product-service systems: onboarding/activation = acquisition lane; core workflows = transaction lane; infrastructure, data pipelines, model ops, human review/support = physical/back-stage lane. Human-in-the-loop steps are touchpoints with capacity limits — design queues and escalation. Concierge or Wizard-of-Oz versions are the minimum viable service before automation.
