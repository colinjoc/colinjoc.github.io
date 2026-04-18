---
title: "Avanti's post-pandemic collapse: the operator or the network?"
date: 2026-04-19
domain: "Transport Economics"
blurb: "Avanti West Coast has the worst pandemic recovery of any UK rail operator. Its defenders blame the track. A parallel intercity line says otherwise."
weight: 11
tags: ["transport", "uk", "rail", "public-services", "policy-evaluation"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/uk_rail_punctuality/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Avanti West Coast's on-time rate fell 9 percentage points between the months before the pandemic and the months since, the worst recovery of any UK rail operator. The usual defence is that the West Coast Main Line itself is the problem. But the parallel East Coast Main Line, run by a broadly comparable intercity operator, actually recovered above its pre-pandemic level. About 12 percentage points of Avanti's gap is specific to Avanti, not shared with the closest intercity peer.

## The question

UK rail punctuality has been a national grievance since the pandemic. Avanti West Coast, which runs the London-to-Glasgow intercity service, became the lightning rod — a government operator-of-last-resort review in late 2023, repeated select-committee appearances, and a steady drumbeat of cancelled and late trains in the press.

The analytical question underneath the headlines is simple. Is Avanti's performance poor because it runs the West Coast Main Line, which has had well-publicised infrastructure problems, strike concentration, and the Euston station rebuild? Or because it is Avanti? This project uses the UK rail regulator's public operator-by-quarter punctuality data to try to bound the answer.

## What we found

Avanti's fall is real, unusually large, and cannot mostly be blamed on the route.

- Avanti's punctuality averaged 77.8 percent in the year before COVID and 68.5 percent in the post-recovery window — a 9.3 percentage-point drop, the worst of any UK operator, with a confidence interval clearly excluding zero.
- Six other operators recovered worse than they ran before the pandemic. But the most natural comparison is London North Eastern Railway, which runs the parallel East Coast Main Line to Edinburgh. LNER is the only long-distance intercity operator whose on-time rate is now above its pre-pandemic performance, up 3.1 points.
- The Avanti-minus-LNER difference comes to -12.4 percentage points, with a confidence interval that comfortably excludes zero. Under the common assumption that both operators face broadly similar long-distance rail conditions, this is the portion of Avanti's decline that is specific to Avanti and not shared with the closest intercity peer.
- A statistical model of punctuality across all 24 operators and 27 quarters explains about 79 percent of the variation using only operator identity and quarter identity. Avanti's operator effect is the lowest in the panel. This is not a 2023-2024 bad patch. It is a persistent six-year effect.
- Metro and commuter operators (London Overground, Merseyrail, c2c, Greater Anglia) sit 18 to 20 points above Avanti on the underlying operator effect. The other intercity operators (LNER, CrossCountry, East Midlands, Great Western) sit 7 to 12 points above.

![All the UK operators we flagged, quarterly on-time shares 2019 through 2025. The shaded band is the COVID period. LNER is at the top of the pack by 2025; Avanti is at the bottom.](plots/operator_trajectories.png)

## Why that matters

The dominant public narrative around Avanti has been an infrastructure-and-external-disruption story: Euston access works, concentrated strikes, rolling-stock reliability issues with the Class 390 and 805 fleets. All of those are real. What the LNER comparison shows is that they cannot be the whole story — because another long-distance intercity operator, facing broadly comparable pressures on a parallel main line, recovered above pre-pandemic levels. If the West Coast route were the binding constraint, no long-distance operator should have recovered. One did.

It is also worth noticing how much of UK rail punctuality variation collapses into just two things: which operator you are and which quarter it is. That pair of labels explains roughly four-fifths of the variance. Route-specific weather and one-off disruptions account for the rest. If you know the operator and the quarter, you have most of the predictive signal.

## What we cannot say

This is a measurement, not a prescription. The difference-in-differences identifies an Avanti-specific gap. It does not attribute that gap to any specific cause. Real infrastructure challenges, fleet reliability issues, and industrial-action concentration on Avanti routes could absorb part of the gap without requiring bad management. The Public Performance Measure also counts trains that arrived — it does not cleanly penalise trains that never ran, and the parallel cancellations table is the priority follow-up. Whether the gap justifies ending the contract depends on operator willingness to improve, alternative-operator capacity, and transition costs that are not in this data.

## What it means in practice

**For passengers on the West Coast.** The problem is more than just the line. LNER is a long-distance intercity operator on a parallel main line that has recovered above pre-pandemic performance. Avanti has not. The service genuinely is worse than it used to be, and the track is not the whole reason.

**For policymakers.** If the West Coast infrastructure were run by the team that delivered LNER's recovery, a reasonable expectation is around a 12-percentage-point improvement in punctuality, all else equal. That does not settle the franchise-versus-concession-versus-public-operation debate, but it sharpens it. The single available natural-experiment counterfactual — a comparable operator running a comparable profile of services on a parallel line — delivered a positive recovery, not a negative one.

**For regulators and researchers.** The Office of Rail and Road's cancellations table is the obvious next data source. If Avanti's cancellation rate is also elevated relative to LNER, the combined reliability picture is worse than the arrivals-only measure shows. A within-operator decomposition that controls for fleet, timetable density, and industrial-action exposure would refine the estimate further — but given the size of the gap, refinements are unlikely to close it.

## How we did it

We downloaded the [Office of Rail and Road's operator-level punctuality series](https://dataportal.orr.gov.uk/), covering the first quarter of 2019 through the fourth quarter of 2025 for 24 passenger operators across 27 quarters, and reshaped it into a 648-row panel. We then ran pre-COVID-versus-post-COVID pre/post differences with bootstrap confidence intervals, fit a two-way fixed-effects model on the full panel to extract each operator's underlying effect, and computed the Avanti-minus-LNER difference-in-differences with standard identifying assumptions stated.

## Further reading

- [Office of Rail and Road data portal](https://dataportal.orr.gov.uk/) — source of the operator punctuality series.
- [ORR punctuality methodology](https://www.orr.gov.uk/monitoring-regulation/rail/performance) — what the Public Performance Measure does and does not capture.
- [Full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/uk_rail_punctuality/paper.md) — all experiments, the full operator table, and the cancellations-data follow-up plan.
