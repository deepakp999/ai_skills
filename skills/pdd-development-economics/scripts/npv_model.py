#!/usr/bin/env python3
"""Quarterly NPV model for a product development project.

Defaults reproduce the coffee-maker example closely (NPV ~ $13M machines only; ~ $126M with
400 consumables per machine per year).

Usage:
    python npv_model.py                 # run with the example parameters below
    python npv_model.py params.json     # override any parameter from a JSON file

Prints the base-case cash-flow table, NPV, investment required, payback quarter,
one-at-a-time sensitivities (worst/best), a tornado ranking and trade-off rules.
Adjust PARAMS / RANGES to your project. Money in $M unless noted.
"""
import json
import sys
from copy import deepcopy

PARAMS = {
    "dev_cost": 5.0,             # total development cost, spread evenly over dev_quarters
    "dev_quarters": 4,           # remaining development time (quarters)
    "tooling": 4.0,              # equipment & tooling
    "ramp_up": 2.0,              # production ramp-up
    "launch": 10.0,              # market launch, last dev quarter + first sales quarter
    "marketing_per_year": 5.0,   # ongoing marketing & support after launch
    "unit_cost": 55.0,           # $/unit direct production cost
    "overhead_per_year": 1.0,    # production overhead
    "initial_volume": 200_000,   # units in first sales year
    "seasonality": [0.20, 0.25, 0.25, 0.30],
    "volume_growth": 0.15,       # per year after year 1
    "retail_price": 260.0,       # $/unit
    "price_change": -0.10,       # per year after year 1
    "channel_margin": 0.40,      # combined distributor + retailer margin
    "sales_quarters": 12,
    "fixed_end": True,           # True: sales window ends on a fixed date (delay shortens it)
    "base_horizon_quarters": 16, # total horizon when fixed_end is True
    "discount_rate": 0.07,       # per year
    # associated consumables / services (set attach_per_unit_year = 0 to ignore)
    "attach_per_unit_year": 0,   # consumable units per installed product per year
    "attach_price": 0.60,
    "attach_cost": 0.05,
    "attach_price_change": 0.05,
}

# worst / best values for the tornado chart
RANGES = {
    "dev_cost": (7.0, 4.0),
    "tooling": (5.0, 3.0),
    "launch": (15.0, 8.0),
    "marketing_per_year": (6.0, 4.0),
    "unit_cost": (60.0, 50.0),
    "initial_volume": (100_000, 250_000),
    "volume_growth": (-0.05, 0.25),
    "retail_price": (225.0, 295.0),
    "channel_margin": (0.50, 0.35),
    "dev_quarters": (5, 3),
}


def cash_flows(p):
    dq = int(p["dev_quarters"])
    horizon = p["base_horizon_quarters"] if p["fixed_end"] else dq + p["sales_quarters"]
    n_sales = horizon - dq
    rows = {k: [0.0] * horizon for k in
            ["volume", "revenue", "development", "tooling", "ramp_up", "marketing", "production", "attach_rev", "attach_cost"]}
    for q in range(dq):
        rows["development"][q] = p["dev_cost"] / dq
    for q in range(max(0, dq - 2), dq):
        rows["tooling"][q] = p["tooling"] / 2          # tooling: last two dev quarters
    for q in (dq - 1, dq):
        rows["ramp_up"][q] = p["ramp_up"] / 2          # ramp-up: last dev quarter + first sales quarter
    # launch spend split over the last dev quarter and first sales quarter; support starts with pre-launch
    rows["marketing"][dq - 1] += p["launch"] / 2 + p["marketing_per_year"] / 4
    installed = 0.0
    for s in range(n_sales):
        q = dq + s
        year, qi = divmod(s, 4)
        vol = p["initial_volume"] * (1 + p["volume_growth"]) ** year * p["seasonality"][qi]
        price = p["retail_price"] * (1 + p["price_change"]) ** year
        net_price = price * (1 - p["channel_margin"])
        rows["volume"][q] = vol
        rows["revenue"][q] = vol * net_price / 1e6
        rows["production"][q] = (vol * p["unit_cost"]) / 1e6 + p["overhead_per_year"] / 4
        rows["marketing"][q] += p["marketing_per_year"] / 4 + (p["launch"] / 2 if s == 0 else 0)
        installed += vol
        if p["attach_per_unit_year"]:
            a_units = installed * p["attach_per_unit_year"] / 4
            a_price = p["attach_price"] * (1 + p["attach_price_change"]) ** year * (1 - p["channel_margin"])
            rows["attach_rev"][q] = a_units * a_price / 1e6
            rows["attach_cost"][q] = a_units * p["attach_cost"] / 1e6
    rq = (1 + p["discount_rate"]) ** 0.25 - 1
    cf, pv = [], []
    for q in range(horizon):
        inflow = rows["revenue"][q] + rows["attach_rev"][q]
        outflow = sum(rows[k][q] for k in ["development", "tooling", "ramp_up", "marketing", "production", "attach_cost"])
        cf.append(inflow - outflow)
        pv.append(cf[-1] / (1 + rq) ** (q + 1))
    return rows, cf, pv


def npv(p):
    return sum(cash_flows(p)[2])


def report(p):
    rows, cf, pv = cash_flows(p)
    print("Quarter      " + " ".join(f"{q+1:>7}" for q in range(len(cf))))
    for k in ["revenue", "attach_rev", "development", "tooling", "ramp_up", "marketing", "production", "attach_cost"]:
        if any(rows[k]):
            print(f"{k:<12} " + " ".join(f"{v:7.2f}" for v in rows[k]))
    print(f"{'cash flow':<12} " + " ".join(f"{v:7.2f}" for v in cf))
    print(f"{'PV':<12} " + " ".join(f"{v:7.2f}" for v in pv))
    total = sum(pv)
    invest, cum, payback = 0.0, 0.0, None
    for q, v in enumerate(pv):
        cum += v
        if cum < invest:
            invest = cum
        if payback is None and q > 0 and cum >= 0:
            payback = q + 1
    print(f"\nNPV = ${total:,.2f}M | investment (max cumulative PV deficit) = ${-invest:,.2f}M | payback quarter = {payback}")
    return total


def sensitivities(p, base):
    print("\nOne-at-a-time sensitivities (worst / best):")
    out = []
    for k, (w, b) in RANGES.items():
        pw, pb = deepcopy(p), deepcopy(p)
        pw[k], pb[k] = w, b
        nw, nb = npv(pw), npv(pb)
        out.append((abs(nb - nw), k, w, nw, b, nb))
    for _, k, w, nw, b, nb in sorted(out, reverse=True):
        print(f"  {k:<20} worst {w!s:>9} -> {nw:8.2f} ({(nw-base)/abs(base)*100:+6.1f}%)   "
              f"best {b!s:>9} -> {nb:8.2f} ({(nb-base)/abs(base)*100:+6.1f}%)")
    print("  (sorted by range = tornado chart order)")


def tradeoff_rules(p, base):
    def delta(key, change, absolute=False):
        q = deepcopy(p)
        q[key] = q[key] + change if absolute else q[key] * (1 + change)
        return npv(q) - base
    print("\nTrade-off rules (change in NPV, $M):")
    print(f"  +10% development cost     : {delta('dev_cost', 0.10):+.2f}")
    print(f"  +1 quarter development    : {delta('dev_quarters', 1, True):+.2f}")
    print(f"  -1 quarter development    : {delta('dev_quarters', -1, True):+.2f}")
    print(f"  +10% tooling              : {delta('tooling', 0.10):+.2f}")
    print(f"  +$1/unit production cost  : {delta('unit_cost', 1, True):+.2f}")
    print(f"  +$1 retail price          : {delta('retail_price', 1, True):+.2f}")
    print(f"  +1% sales volume          : {delta('initial_volume', 0.01):+.2f}")


if __name__ == "__main__":
    params = deepcopy(PARAMS)
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            params.update(json.load(f))
    base = report(params)
    sensitivities(params, base)
    tradeoff_rules(params, base)
