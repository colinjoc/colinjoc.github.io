---
title: "Ireland's Planning Appeals: How an 18-Week Target Became a 42-Week Wait"
date: 2026-04-17
domain: "Public Administration"
blurb: "Ireland's national planning-appeals body saw the time to decide a typical case rise from 18 weeks in 2017 to 42 weeks by 2023 and 2024, with the compliance rate against the statutory 18-week target collapsing from 64 percent to 25 percent. The collapse concentrated in a single year — 2022 to 2023 — and the visible recovery through late 2025 rested on the queue finally draining faster than new cases arrived."
weight: 14
tags: ["ireland", "planning", "public-services", "queueing", "policy"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_abp_decision_times/paper.md).*

## The Question

An Bord Pleanála is the body that decides appeals against Irish local-authority planning decisions, from objections to a neighbour's extension through to nationally significant housing and infrastructure schemes. Since 1992 it has had a statutory target to decide most appeals in 18 weeks. Through the mid-2010s it met that target for roughly 70 to 80 percent of cases — slow, but predictable.

Then it wasn't. By 2023 compliance had fallen to 28 percent and the typical case took 42 weeks. Developers, homeowners, and local authorities all began planning around a system where a "normal appeal" could easily take ten months instead of four. The question we set out to answer is simple: what actually happened, when did it happen, and is the 2025 recovery real?

## What We Found

The compliance collapse is not a slow slide. It is a single-year break between 2022 and 2023, on top of a smaller 2018 step-up.

- Decisions per year took 18 weeks in 2017, 23 weeks in 2018, 26 weeks in 2022, and 42 weeks in both 2023 and 2024.
- The share of cases meeting the 18-week target fell from 64 percent in 2017 to 25 percent in 2024.
- In 2022 the Board received about 1.45 cases for every case it disposed of — a clear tipping point. By 2024 that ratio had dropped to 0.74, meaning the queue was finally draining.
- Monthly compliance in 2025 rose steadily from 37 percent in January to 77 percent in September, the clearest recovery signal in the record.
- Within the overall number, Strategic Housing Development appeals averaged 124 weeks in 2024 while the newer Large-scale Residential Development appeals cycled through in 13 weeks — a nearly ten-fold spread across case types.

## Why That's Surprising

The popular explanation for the collapse was "the backlog". But a backlog is an outcome, not a cause — and the arithmetic showed the break was almost entirely within case types, not a shift in which kinds of cases were coming in. Cases of every type got slower; the mix of cases did not move much.

The shape of the break is also unusual. Most capacity crises in public bodies look like gentle drift. This one looks like a cliff: a flat-ish 2018 to 2021, a small step-up in 2022, and then a near-doubling in a single year. The single-year character points at specific institutional shocks — gaps on the Board itself, a 2018 computer-system transition, and court rulings that lengthened the reasons the Board must give for each decision — rather than a gradual erosion.

The final surprise is how much the 2025 recovery outran the forecasts. The model that fit the crisis years reasonably well predicted 2025 compliance of around 26 percent by the third quarter. The observed figure was 77 percent. The Board was clearing cases roughly 40 percent faster per staff member than it had the year before, something no pre-2025 calibration could have anticipated.

## What It Means

For someone waiting on a planning appeal today, the picture is brighter than the 2023 and 2024 headlines suggest: the queue is genuinely shrinking and recent months show pre-crisis throughput. But the data also show that the statutory 18-week target is a political marker rather than a legal deadline, and the level of compliance depends heavily on having enough Board members in seat and a stable case-mix.

For policy, the practical lesson is that capacity shocks at specialist tribunals cascade quickly. The system spent most of 2023 and 2024 at a 40-week wait not because the underlying case volume was unmanageable, but because a one-year intake-versus-disposal imbalance in 2022 created a queue that took two years to drain. Forward projections to 2028 depend heavily on assumptions that the data cannot yet pin down, so confident numerical forecasts of the post-reform era should be read as scenario bookkeeping, not predictions.

## How We Did It

We built a year-by-year series of decision times and compliance rates from the [An Bord Pleanála Annual Report Appendices](https://www.pleanala.ie/en-ie/statistics/quarterly-statistics) for 2018 to 2024, cross-checked against the quarterly casework statistics through 2025. The analysis fit a family of simple time-series and queueing models to the ten-year record, decomposed the change into within-case-type and case-mix components, and validated the 2025 projection against the actual 2025 monthly compliance figures.

## Further Reading

- [An Bord Pleanála quarterly planning casework statistics](https://www.pleanala.ie/en-ie/statistics/quarterly-statistics) — official source for compliance rates
- Kingman, J. F. C. (1961). The single server queue in heavy traffic. *Proceedings of the Cambridge Philosophical Society* 57(4) — the queueing-theory backbone
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_abp_decision_times/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
