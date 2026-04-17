---
title: "Where Do Irish Planning Permissions Actually Go?"
date: 2026-04-17
domain: "Irish Housing Policy"
blurb: "Between 2019 and 2025, Irish planning authorities approved about 267,000 new homes and roughly 167,000 were actually built. We compared the two official series to see whether the system is converting approvals into houses. The conversion ratio has recovered from a pandemic-era low but not surpassed pre-pandemic levels, and the top of the pipeline — the number of permissions being granted — has not grown beyond its 2019 level."
weight: 13
tags: ["housing", "ireland", "planning-permissions", "housing-crisis"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_housing_pipeline/paper.md).*

## The Question

Every month the press reports a new "housing permissions" number, usually compared against the government's target of 50,500 homes per year under Housing for All. But these two numbers mean different things. Permissions are what councils and the national planning appeals body say developers are *allowed* to build. Completions are what actually got built and occupied. Between the two sits finance, labour, materials, design revisions, and sometimes sheer developer delay.

Is the Irish system stockpiling approvals that never produce houses? Or is it converting approvals into homes roughly as fast as it should? And has that changed since the housing crisis deepened?

## What We Found

**Permissions have been flat. Completions have roughly doubled.** Between 2019 and 2025 Ireland approved 32,000 to 43,000 units per year with no upward trend, while completions rose from 15,935 to 25,237. The construction sector is delivering substantially more homes than five years ago, but the approval pipeline above it is not widening.

- At a two-year lag, the aggregate conversion ratio climbed from 41% in 2019 to 65% in 2022 — a real improvement in throughput.
- But the 2019 starting point was a pandemic-era trough. Pre-2019 data from the same statistical agency show 2016-2017 conversions of 77-86%. The recent rise is a recovery, not a breakthrough.
- The approval ceiling is binding. Even at 100% conversion — every permission built, none wasted — the current rate of about 38,000 permissions per year cannot deliver 50,500 homes.
- The Strategic Housing Development fast-track scheme, which ran from late 2017 to late 2021, produced a similar volume of permissions to the standard route over the same period. Whether it was actually faster on a per-scheme basis is not answerable from the public data.
- The ranking of years by conversion ratio is stable whether you use a one-year, two-year, or three-year lag. The ratio moves, but 2022 is always the peak and 2019-2020 is always the trough.

## Why That's Surprising

The commonest explanation for Ireland's housing shortfall is that developers sit on approvals without building. The data do not support that as the dominant story. The conversion side of the funnel is now performing at roughly its pre-pandemic norm — not exceptionally, but not catastrophically either. What has *not* moved is the number of approvals the system is willing to issue each year. Policy debate has focused heavily on developer behaviour and planning appeal delays; those matter, but the arithmetic ceiling sits upstream of both.

There is also a measurement twist. The conversion ratio measured here is not a true cohort-tracked rate — it compares completions in one year against permissions two years earlier, at the national level. Some 2019 approvals will complete in 2026 or 2027; some 2021 completions came from permissions granted before the current data series begins. The ratio is a useful smoothed signal, not a precise yield. That caveat matters for policymaking: both the "genuine improvement" reading and the "post-pandemic catch-up" reading are compatible with the same numbers, and both lead to the same headline — the binding constraint is permission volume.

## What It Means

For someone watching the housing crisis from the outside, the picture is cautiously encouraging on one axis and starkly unchanged on the other. More homes are being built each year, and the pipeline is converting approvals back toward pre-pandemic norms. But the top of the pipeline — how many approvals the system issues at all — has not grown with the target. The 50,500-home annual goal is not reachable at current approval volumes even under the most favourable conversion assumptions.

For a policymaker, the implication is that proposals focused on pushing developers to build faster, or forcing them to use their existing permissions, are pushing on a mechanism that is already at or near its historical normal. Proposals focused on increasing the *number* of permissions — through zoning reform, faster local decisions, or more land coming forward — are pushing on the structural constraint.

## How We Did It

We downloaded three public tables from the [Central Statistics Office](https://data.cso.ie/): BHQ15 (quarterly planning permissions from 2019 to 2025), NDA12 (annual new-dwelling completions by urban area from 2012 to 2025), and BHQ16 (permissions by region going back to 1975, for pre-2019 context). We aggregated permissions to annual totals, being careful not to double-count apartment units and house units, and computed conversion ratios at one-, two-, and three-year lags between approvals and completions. This is a descriptive comparison of two end stages — there is no middle-stage tracking, because commencement-notice data are held by a different department and are not part of the public statistical release.

## Further Reading

- [Central Statistics Office — Planning Permissions (BHQ15)](https://data.cso.ie/) — the official permissions series.
- [Central Statistics Office — New Dwelling Completions (NDA12)](https://data.cso.ie/) — the official completions series.
- [Housing for All (Government of Ireland, 2021)](https://www.gov.ie/en/publication/ef5ec-housing-for-all-a-new-housing-plan-for-ireland/) — the 50,500-home-per-year target.
- [Detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_housing_pipeline/paper.md) — with the full lag-sensitivity tables and methodological caveats.

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
