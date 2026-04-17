---
title: "Avanti's Post-Pandemic Collapse: The Operator or the Network?"
date: 2026-04-17
domain: "Transport Economics"
blurb: "Avanti West Coast's punctuality dropped 9 percentage points between the months before the pandemic and the months since, the worst recovery of any UK rail operator. The obvious excuse is the West Coast Main Line itself. But on the parallel East Coast Main Line, the comparable operator actually recovered above its pre-pandemic performance. The gap between them is large, statistically clean, and not mostly a story about the track."
weight: 11
tags: ["transport", "uk", "rail", "public-services", "policy-evaluation"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/uk_rail_punctuality/paper.md).*

## The Question

UK rail punctuality has been a standing national grievance since the pandemic. Avanti West Coast, which runs the London-to-Glasgow intercity service, became the lightning rod — a government operator-of-last-resort review in late 2023, repeated select-committee appearances, and a steady drumbeat of cancelled and late trains in the press.

The analytical question underneath the headlines is simple: is Avanti's performance poor because it runs the West Coast Main Line, which has had well-publicised infrastructure problems, strike concentration, and the Euston station works — or because it is Avanti? This project uses the UK regulator's public operator-by-quarter punctuality data to try to bound the answer.

## What We Found

Avanti's fall is real and unusually large, and it cannot mostly be blamed on the route.

- Avanti's punctuality averaged 77.8 percent in the months before COVID and 68.5 percent in the months since — a 9.3 percentage point drop, the worst of any UK operator, with a confidence interval that clearly excludes zero.
- Six other operators recovered worse than they ran before the pandemic. But the obvious intercity peer for a comparison is London North Eastern Railway, which runs the parallel East Coast Main Line to Edinburgh. LNER is the only long-distance intercity operator that recovered above its pre-pandemic performance, up 3.1 points.
- The Avanti-minus-LNER difference comes to −12.4 percentage points, with a confidence interval that comfortably excludes zero. Under the common assumption that both operators face similar long-distance rail conditions, this is the portion of Avanti's decline that is not shared with the obvious peer.
- A statistical model of punctuality across all 24 operators and 27 quarters explains roughly 79 percent of the variation using only operator identity and quarter identity. Avanti's deficit is persistent across the whole window, not a one-off 2022-2023 quirk.
- Metro and commuter operators (London Overground, Merseyrail, c2c, Greater Anglia) sit 18 to 20 points above Avanti on the underlying operator effect. The other intercity operators (LNER, CrossCountry, East Midlands, Great Western) are 7 to 12 points above.

## Why That's Surprising

The dominant press narrative around Avanti has been an infrastructure-and-external-disruption story: Euston access works, concentrated strikes, rolling-stock reliability issues with the Class 390 and 805 fleets. All of those are real. What the comparison with LNER shows is that they cannot be the whole story, because another long-distance intercity operator facing broadly comparable pressures on a parallel main line recovered above pre-pandemic levels.

It is also worth noticing how much of UK rail punctuality variation is explained by just two things: which operator you are and which quarter it is. 79 percent of the variance collapses into those two labels. Route-specific, weather, and one-off disruptions together account for the remaining 21 percent. If you know the operator and the quarter, you have most of the predictive signal.

## What It Means

For passengers, the finding supports the intuition that changing operators matters. The public data cannot prove that moving the Avanti contract to a different operator would automatically deliver LNER-style recovery — the infrastructure genuinely is different and there are rolling-stock, timetabling, and industrial-relations factors the regulator's headline table does not capture. But it does say that the comparable intercity alternative on the East Coast has delivered, and that the route is not a determining constraint.

For policymakers, the result is a data point in the long-running debate over franchise versus concession versus public operation. The single counterfactual where a different operator runs a similar profile of long-distance intercity services produced a positive recovery, not a negative one. That does not close the debate, but it sharpens it.

Two caveats matter. First, the analysis uses punctuality alone; the regulator's cancellation-rate table would give a complementary view and is a priority follow-up. Second, the comparison between Avanti and LNER is not controlled for fleet, timetable density, industrial-action exposure, or passenger-kilometre mix — those would refine the estimate but, given the size of the gap, are unlikely to close it.

## How We Did It

The data is the [Office of Rail and Road's operator-level punctuality series (Table 3113)](https://dataportal.orr.gov.uk/), covering the first quarter of 2019 through the fourth quarter of 2025 for 24 passenger operators. The analysis compares each operator's pre-pandemic and post-recovery averages with bootstrap confidence intervals, fits a two-way fixed-effects model on the full 24-operator by 27-quarter panel, and runs a difference-in-differences estimate using LNER as the intercity counterfactual.

## Further Reading

- [Office of Rail and Road data portal](https://dataportal.orr.gov.uk/) — source of the operator punctuality series
- [ORR punctuality methodology](https://www.orr.gov.uk/monitoring-regulation/rail/performance) — what the Public Performance Measure does and does not capture
- [Full technical write-up](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/uk_rail_punctuality/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
