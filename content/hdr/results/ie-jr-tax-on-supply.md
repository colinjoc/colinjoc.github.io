---
title: "Did the courts really break Irish housing? The arithmetic says no"
date: 2026-04-17
domain: "Irish Housing Policy"
blurb: "For half a decade, judges overturned almost every big Irish housing approval that reached them. Everyone agrees it was a scandal. Was it also the housing crisis?"
weight: 11
tags: ["housing", "ireland", "judicial-review", "planning", "policy"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_jr_tax_on_supply/paper.md) has the case table and the counterfactual bounds. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Court challenges to Ireland's fast-track housing approvals delayed somewhere between 7,000 and 12,500 homes by about a year. That is a real, large cost. It is not, on its own, big enough to explain why the country is roughly 16,000 homes short of its target every year.

## The Question

In 2017 Ireland set up a fast-track planning route for big housing developments, called Strategic Housing Development — SHD for short. Schemes of 100 or more homes were routed directly to the national planning appeals body, An Bord Pleanála — ABP, the country's planning regulator — bypassing local councils. The stated goal was speed.

Instead, the route became a magnet for court challenges. Community groups and environmental bodies took nearly every major decision to judicial review. The state lost almost all of them. The regime was scrapped at the end of 2021.

The legal bills are a matter of public record. The housing bill is not. How many homes were delayed, for how long, and how much of the national shortfall can honestly be pinned on the courts rather than on everything else?

## What we found

Across 22 large schemes that went to the High Court between 2018 and 2022, the direct delay added up to roughly 105,000 housing-unit-months. That is the equivalent of 7,000 to 12,500 homes held up for a year.

- Seven out of every eight fast-track decisions that reached the High Court were either quashed by a judge or conceded by the planning board before a hearing. The legal strategy underpinning the regime was not sustainable.
- Five cases alone — including one affecting 741 apartments and another 661 homes — accounted for nearly half the total delay.
- Eighteen of the 22 challenges were Dublin schemes, covering about three-quarters of the delayed homes.
- At a conservative estimate of the cost of holding land while a case runs, the direct delay cost developers about EUR 53 million in carrying costs. At a high-end estimate, closer to EUR 158 million.
- The planning board itself slowed dramatically over the same period. Average decision time rose from 18 weeks in 2017 to 42 weeks by 2023, with on-time compliance falling from 69 percent to 25 percent.
- Some of that slowdown was caused by the litigation — the board became cautious and spent longer defending each decision — but it cannot be cleanly separated from a collapse in the number of filled board positions, a major IT transition, and rising case complexity all landing at the same time.
- If the board had held its pre-crisis turnaround, an estimated 7,400 to 16,600 additional homes would have been delivered sooner.

## Why that matters

The popular framing of the Irish housing debate puts judicial review at the centre of the shortfall. The arithmetic is more awkward. The direct cost is real and large — tens of thousands of housing-unit-months concentrated in a handful of Dublin schemes — but it is not of the scale needed to close the gap between 34,000 completions and a 50,500-home target. Even at the high end of the plausible range, the combined direct and indirect damage over seven years amounts to something like 10,000 to 16,000 homes. That is serious. It is not the whole story.

The second awkwardness is that the damage from judicial review cannot be cleanly pulled apart from the damage from the planning board's own capacity crisis. Both started worsening at the same time. Both produced slower decisions. The honest range for how much of the board's slowdown to blame on litigation is anywhere between zero and half — and no public data can narrow that.

A third point worth noting: the successor regime, Large-scale Residential Development (LRD), has produced almost no substantive court decisions as of the end of 2024. Whether the reforms worked is a question the data cannot yet answer.

## What it means in practice

**For developers weighing a big Dublin scheme.** The cost of losing a judicial review under the old regime included legal fees, one to two years of land-finance carry, and a near-90 percent probability of losing. That calculus still shapes which apartment schemes are viable at all.

**For policymakers.** The numbers point to a three-pronged response. Reform the costs regime that makes filing a judicial review cheap for objectors — the 2024 Planning and Development Act attempts this. Speed up resolution of the reviews themselves, so a challenged scheme is not in limbo for two years. Sustain recent investment in planning-board staffing, because the capacity crisis is a larger contributor to delay than litigation itself. Removing judicial review entirely would not, on its own, rescue the housing target.

**For voters and journalists.** Reforms under debate are worth doing, and will produce low-thousands of additional homes per year. Not tens of thousands. The structural gap is larger than the courts.

## How we did it

We combined case-level data on 22 fast-track judicial reviews from the [Office of the Planning Regulator's public appendix](https://www.opr.ie/) with aggregate decision-time series from the planning appeals body's annual reports and national completions data from the [Central Statistics Office](https://data.cso.ie/). For each case, we computed the number of homes affected, the months of delay from lodgement to decision, and an outcome weight reflecting whether the state won or lost. We then built a counterfactual scenario in which the appeals body had held its pre-crisis turnaround, with sensitivity tests for construction-sector capacity and for how much of the system-wide slowdown could plausibly be blamed on litigation.

## Further reading

- [Office of the Planning Regulator](https://www.opr.ie/) — source for the judicial-review case appendix.
- [Central Statistics Office — housing completions](https://data.cso.ie/) — the national delivery series.
- Simons (2019). *Planning and Development Law* (3rd ed.) — legal context for Irish planning judicial review.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_jr_tax_on_supply/paper.md).
