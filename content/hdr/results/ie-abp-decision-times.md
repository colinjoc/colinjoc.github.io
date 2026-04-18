---
title: "How Ireland's 18-week planning-appeal target became a 42-week wait"
date: 2026-04-17
domain: "Public Administration"
blurb: "A statutory deadline that used to be hit two times out of three collapsed to one in four. Then, quietly, the queue started draining again."
weight: 14
tags: ["ireland", "planning", "public-services", "queueing", "policy"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_abp_decision_times/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** An Bord Pleanála — Ireland's national planning-appeals body — saw a typical appeal stretch from 18 weeks in 2017 to 42 weeks by 2023. The collapse was not a gentle slide; it was a cliff edge in a single year. And by late 2025 the queue was clearing faster than new cases were arriving.

## The question

An Bord Pleanála decides appeals against local-authority planning decisions — from a neighbour's extension up to nationally significant housing and infrastructure schemes. Since 1992 it has had a statutory target to decide most appeals in 18 weeks. Through the mid-2010s it met that target for roughly 70 to 80 percent of cases. Slow, but predictable.

Then it stopped being predictable. By 2023 compliance had fallen to 28 percent and a typical case took 42 weeks. Developers, homeowners, and councils all began planning around a system where a "normal appeal" could easily take ten months instead of four. We asked a simple question: what actually happened, when did it happen, and is the apparent 2025 recovery real?

## What we found

The compliance collapse was not a slow slide. It was a single-year break between 2022 and 2023, on top of a smaller 2018 step-up.

- A typical appeal took 18 weeks in 2017, 23 weeks in 2018, 26 weeks in 2022, and 42 weeks in both 2023 and 2024.
- The share of cases meeting the 18-week target fell from 64 percent in 2017 to 25 percent in 2024.
- In 2022 the Board received about 1.45 cases for every one it closed — a clear tipping point. By 2024 that ratio had dropped to 0.74, meaning the queue was finally draining.
- Monthly compliance in 2025 rose steadily from 37 percent in January to 77 percent in September, the clearest recovery signal in the record.
- Strategic Housing Development appeals — the fast-track regime for large schemes — averaged 124 weeks in 2024, while the newer Large-scale Residential Development appeals cycled through in 13 weeks. A nearly tenfold spread across case types.

## Why that matters

The popular explanation was "the backlog". But a backlog is an outcome, not a cause — and the arithmetic showed the break was almost entirely within case types, not a shift in which kinds of cases were coming in. Cases of every kind got slower. The mix did not move much.

The shape of the break is also unusual. Most capacity crises in public bodies look like gentle drift. This one looked like a cliff: a flat 2018 to 2021, a small step-up in 2022, and then a near-doubling in a single year. That single-year character points at specific institutional shocks — gaps on the Board itself, a 2018 computer-system transition, and court rulings that lengthened the reasoning the Board must attach to each decision — rather than gradual erosion.

The final surprise is how far the 2025 recovery outran our forecasts. A queueing model fit to the crisis years predicted third-quarter compliance of around 26 percent. The actual figure was 77 percent. The Board was clearing cases roughly 40 percent faster per member than the year before — something no pre-2025 calibration could have anticipated.

## What it means in practice

**For anyone waiting on a planning appeal.** The picture is brighter than the 2023 and 2024 headlines suggested. The queue is genuinely shrinking and recent months show pre-crisis throughput. But the 18-week target is a political marker, not a legal deadline, and whether it is met depends heavily on having enough Board members in seat.

**For policymakers.** Capacity shocks at specialist tribunals cascade fast. The system spent most of 2023 and 2024 at a 40-week wait not because the underlying volume was unmanageable, but because a one-year intake-versus-disposal imbalance in 2022 created a queue that took two years to drain. Forward projections to 2028 depend on assumptions the data cannot yet pin down — confident numerical forecasts of the post-reform era should be read as scenario bookkeeping, not predictions.

## How we did it

We built a year-by-year series of decision times and compliance rates from the [An Bord Pleanála quarterly casework statistics](https://www.pleanala.ie/en-ie/statistics/quarterly-statistics) for 2018 through 2025, fit a family of simple time-series and queueing models to the ten-year record, and decomposed the change into within-case-type and case-mix components. We validated the 2025 projection against the actual monthly compliance figures as they came in.

## Further reading

- [An Bord Pleanála quarterly planning casework statistics](https://www.pleanala.ie/en-ie/statistics/quarterly-statistics) — the official source for compliance rates.
- Kingman, J. F. C. (1961). The single server queue in heavy traffic. *Proceedings of the Cambridge Philosophical Society* 57(4) — the queueing-theory backbone.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_abp_decision_times/paper.md).
