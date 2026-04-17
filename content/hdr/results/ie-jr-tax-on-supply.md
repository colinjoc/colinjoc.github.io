---
title: "What Did Judicial Review Actually Cost Irish Housing?"
date: 2026-04-17
domain: "Irish Housing Policy"
blurb: "Between 2018 and 2021, court challenges to Irish fast-track housing approvals overturned roughly seven out of eight decisions that reached the High Court. We converted that cascade of legal losses into a concrete number: roughly 105,000 housing-unit-months of direct delay across 22 large schemes. That is the equivalent of about 7,000 to 12,500 homes held up for a year — large, but not large enough to explain Ireland's overall shortfall on its own."
weight: 11
tags: ["housing", "ireland", "judicial-review", "planning", "policy"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_jr_tax_on_supply/paper.md).*

## The Question

In 2017 Ireland set up a fast-track planning route for large housing developments, called Strategic Housing Development. The idea was to route schemes of 100 or more homes directly to the national planning appeals body, bypassing local councils, to speed delivery. Instead, the fast-track route became a magnet for court challenges. Community groups and environmental NGOs took nearly every major decision to judicial review, and the state lost the overwhelming majority of cases. The regime was scrapped at the end of 2021.

The legal fees are a matter of public record. What was not known is the housing cost. How many homes were delayed by the litigation cascade? For how long? And how much of Ireland's subsequent housing shortfall can be attributed to the courts versus other causes?

## What We Found

**The direct delay cost of judicial review on the fast-track housing regime was about 105,000 housing-unit-months — the equivalent of roughly 7,000 to 12,500 homes held up for a year.** The figure is based on 22 large schemes that went to the High Court between 2018 and 2022.

- Seven out of every eight fast-track decisions that reached the High Court were either quashed or conceded by the state. The legal strategy underpinning the regime was not sustainable.
- The five largest cases alone — including one affecting 741 apartments and another affecting 661 homes — accounted for nearly half of the total delay.
- Delays were heavily concentrated in Dublin: 18 of the 22 cases were Dublin schemes, covering about three-quarters of all delayed units.
- At a conservative estimate of land-finance holding cost, the direct delay represents about EUR 53 million in carrying costs borne by developers; at higher cost assumptions the figure reaches EUR 158 million.
- The national planning appeals body slowed dramatically across the same period. Its average decision time rose from 18 weeks in 2017 to 42 weeks by 2023, with on-time compliance falling from 69% to 25%.
- Some of that slowdown was caused by judicial review — the body became institutionally cautious and spent more time defending each decision. But it cannot be cleanly separated from other concurrent problems: a collapse in the number of filled board positions, a major IT transition, and growing case complexity.
- Under a counterfactual where the appeals body had maintained its pre-crisis turnaround time, an estimated 7,400 to 16,600 additional homes would have been delivered sooner, depending on whether the construction sector could have absorbed them.

## Why That's Surprising

The popular narrative in Irish housing debate frames judicial review as the dominant cause of the country's housing shortfall. The numbers here tell a more nuanced story. The direct cost is real and large — tens of thousands of housing-unit-months, concentrated in a handful of Dublin schemes — but it is not of the scale needed to explain the gap between Ireland's actual completions (roughly 34,000 in 2024) and its target of 50,500. At the higher end of the plausible range, the combined direct and indirect delay amounts to something like 10,000 to 16,000 homes of lost delivery over seven years. That is serious. It is not the whole story.

The other surprise is how hard it is to separate judicial-review damage from the planning appeals body's capacity crisis. Both started worsening around the same time, both produced slower decisions, and both responded to the same political environment. The honest statement is that judicial review contributed somewhere between zero and half of the overall appeals-body slowdown — but no data available can identify where within that range the truth lies.

A third surprise: the successor regime to the fast-track route, Large-scale Residential Development, has produced almost no substantive court decisions as of end-2024. The jury is literally out on whether the reforms worked.

## What It Means

For a developer considering a large Dublin scheme, the lesson is unambiguous: the cost of a judicial-review loss includes not just legal fees but one to two years of land-finance carry, and the probability of losing was near 90% under the old regime. That calculus has shaped, and continues to shape, whether large apartment schemes are viable at all.

For a policymaker, the numbers point to a three-pronged response. First, reform the costs regime that makes filing a judicial review cheap for objectors — a change the 2024 Planning and Development Act attempts. Second, speed up resolution of the reviews themselves, so that a challenged scheme is not held in limbo for two years. Third, sustain the recent investment in planning-appeals-body staffing, because the capacity crisis is a larger contributor to delay than judicial review itself. Removing judicial review entirely would not, on its own, rescue the housing target.

For a voter, the takeaway is that the reforms being debated are worth doing, but will produce low-thousands of additional homes per year, not tens of thousands. The structural gap is larger than litigation alone.

## How We Did It

We combined case-level data on 22 fast-track judicial reviews from the [Office of the Planning Regulator's public appendix](https://www.opr.ie/) with aggregate decision-time series from the national planning appeals body's annual reports and national completions data from the [Central Statistics Office](https://data.cso.ie/). For each case, we computed the number of homes affected, the months of delay from lodgement to decision, and an outcome weight reflecting whether the state won or lost. We then built a counterfactual completions scenario assuming the appeals body had maintained its pre-crisis turnaround, with sensitivity tests for construction-sector capacity constraints and for how much of the system-wide slowdown could be attributed to litigation.

## Further Reading

- [Office of the Planning Regulator](https://www.opr.ie/) — source for the judicial-review case appendix.
- [Central Statistics Office — housing completions](https://data.cso.ie/) — the national delivery series.
- [Simons, *Planning and Development Law* (3rd ed., 2019)](https://www.roundhall.ie/) — legal context for Irish planning judicial review.
- [Detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_jr_tax_on_supply/paper.md) — with the full case table, cost sensitivity analysis, and counterfactual bounds.

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
