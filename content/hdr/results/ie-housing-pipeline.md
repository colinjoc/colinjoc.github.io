---
title: "Where do Irish planning permissions actually go?"
date: 2026-04-17
domain: "Irish Housing Policy"
blurb: "Ireland approved roughly 267,000 new homes between 2019 and 2025. It built about 167,000. The gap is where every Irish housing argument lives."
weight: 13
tags: ["housing", "ireland", "planning-permissions", "housing-crisis"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_housing_pipeline/paper.md) has the lag-sensitivity tables and methodological caveats. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Between 2019 and 2025 Ireland granted planning permission for about 267,000 new homes and built roughly 167,000 of them. The rate at which approvals turn into houses has recovered from a pandemic-era low but has not exceeded pre-pandemic levels. Meanwhile the number of permissions being granted each year has not grown — the top of the pipeline is the part that has not moved.

## The question

Every month the press reports a new "housing permissions" number, usually compared against the government's target of 50,500 homes per year under Housing for All. But those two numbers mean different things. Permissions are what councils and the national planning appeals body say developers are allowed to build. Completions are what actually got built and occupied. Between the two sits finance, labour, materials, design revisions, and sometimes sheer developer delay.

Is the Irish system stockpiling approvals that never produce houses? Or is it converting approvals into homes roughly as fast as it should? And has that changed since the housing crisis deepened?

## What we found

Permissions have been flat. Completions have roughly doubled. Between 2019 and 2025 Ireland approved 32,000 to 43,000 units per year with no upward trend, while completions rose from 15,935 to 25,237. The construction sector is delivering substantially more homes than five years ago, but the approval pipeline above it is not widening.

- At a two-year lag, the aggregate conversion ratio climbed from 41 percent in 2019 to 65 percent in 2022 — a real improvement in throughput.
- But the 2019 starting point was a pandemic-era trough. Pre-2019 data from the same statistical agency show 2016 and 2017 conversions of 77 to 86 percent. The recent rise is a recovery, not a breakthrough.
- The approval ceiling is binding. Even at 100 percent conversion — every permission built, none wasted — the current rate of about 38,000 permissions per year cannot deliver 50,500 homes.
- The Strategic Housing Development fast-track scheme — the expedited planning regime that ran from late 2017 to late 2021 for large residential projects — produced a similar volume of permissions to the standard route over the same period. Whether it was actually faster on a per-scheme basis is not answerable from the public data.
- The ranking of years by conversion ratio is stable whether you use a one-year, two-year, or three-year lag. The ratio moves, but 2022 is always the peak and 2019 to 2020 is always the trough.

## Why that matters

The commonest explanation for Ireland's housing shortfall is that developers sit on approvals without building. The data do not support that as the dominant story. The conversion side of the funnel is now performing at roughly its pre-pandemic norm — not exceptionally, but not catastrophically either. What has not moved is the number of approvals the system is willing to issue each year. Policy debate has focused heavily on developer behaviour and planning appeal delays. Those matter, but the arithmetic ceiling sits upstream of both.

There is also a measurement twist. The conversion ratio measured here is not a true cohort-tracked rate — it compares completions in one year against permissions two years earlier, at the national level. Some 2019 approvals will complete in 2026 or 2027. Some 2021 completions came from permissions granted before the current data series begins. The ratio is a useful smoothed signal, not a precise yield. That caveat matters for policymaking: both the "genuine improvement" reading and the "post-pandemic catch-up" reading are compatible with the same numbers, and both lead to the same headline — the binding constraint is permission volume.

## What it means in practice

**For anyone watching the housing crisis from the outside.** The picture is cautiously encouraging on one axis and starkly unchanged on the other. More homes are being built each year, and the pipeline is converting approvals back toward pre-pandemic norms. But the top of the pipeline — how many approvals the system issues at all — has not grown with the target. The 50,500-home annual goal is not reachable at current approval volumes even under the most favourable conversion assumptions.

**For policymakers.** Proposals focused on pushing developers to build faster, or forcing them to use their existing permissions, are pushing on a mechanism that is already at or near its historical normal. Proposals focused on increasing the number of permissions — through zoning reform, faster local decisions, or more land coming forward — are pushing on the structural constraint.

## How we did it

We downloaded three public tables from the [Central Statistics Office](https://data.cso.ie/): BHQ15 (quarterly planning permissions from 2019 to 2025), NDA12 (annual new-dwelling completions by urban area from 2012 to 2025), and BHQ16 (permissions by region going back to 1975, for pre-2019 context). We aggregated permissions to annual totals, being careful not to double-count apartment units and house units, and computed conversion ratios at one-, two-, and three-year lags. This is a descriptive comparison of two end stages — there is no middle-stage tracking, because commencement-notice data are held by a different department and are not part of the public statistical release.

## Further reading

- [Central Statistics Office — Planning Permissions (BHQ15)](https://data.cso.ie/) — the official permissions series.
- [Central Statistics Office — New Dwelling Completions (NDA12)](https://data.cso.ie/) — the official completions series.
- [Housing for All (Government of Ireland, 2021)](https://www.gov.ie/en/publication/ef5ec-housing-for-all-a-new-housing-plan-for-ireland/) — the 50,500-home-per-year target.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_housing_pipeline/paper.md) — with the full lag-sensitivity tables and methodological caveats.
