---
title: "How Long Does an Irish Home Really Take to Build? About 32 Months"
date: 2026-04-17
domain: "Housing Policy"
blurb: "Tracking 183,633 Irish residential planning permissions from grant to certified completion, the median project takes 32 months end-to-end — eight months longer than the figure implied by the official aggregate series. Only about two-thirds of one percent of permissions never start at all, far below the folklore of widespread unbuilt permissions."
weight: 12
tags: ["ireland", "housing", "construction", "survival-analysis", "policy"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_commencement_notices/paper.md).*

## The Question

"We grant plenty of permissions, but nothing gets built." That sentence, or some version of it, is routine in Irish housing debate. The number of planning permissions granted each quarter is published, and so is the number of completions. The gap between the two is usually estimated by lining up the national totals and asking how far back you have to shift the permissions series to make it match the completions series — a statistical trick, not a measurement.

We wanted a real answer. For the actual individual projects that were granted permission since 2014, how long did they take to start, how long did they take to finish, and how many never began?

## What We Found

Starting from the building-control filings that every developer must submit, we followed each residential permission from grant to first shovel to final certificate. The medians are:

- From permission granted to a declared start on site: **232 days** — around seven and a half months.
- From declared start to certified completion: **498 days** — around sixteen and a half months.
- End-to-end, for projects we can track all the way through: **962 days, or 32 months**.
- Fewer than one in 150 permissions — **0.67 percent** — never results in a commencement notice inside six years. The "dark permissions" problem at the start of the pipeline is very small.
- The share of permissions whose *completion* certificate is never filed is much larger — up to 39 percent for schemes that are required to file one — but this is a filing-discipline issue, not a construction-abandonment issue.
- Apartments take **53 days longer** than conventional dwellings to go from start to certificate, a gap that has survived two decades of policy attention to apartment viability.

The end-to-end 32-month figure is about **eight months longer** than the 24-month lag implied by the traditional aggregate-series method.

## Why That's Surprising

The folk story of Irish housing features large numbers of "land-banked" permissions that are granted and sat on. The data do not support it, at least under the simplest definition. Only around 0.67 percent of residential permissions granted have no commencement notice at all after six years. The slow part of the pipeline is not developers refusing to start; it is projects that start and then take a very long time to finish.

The aggregate method also turns out to understate the real wait. Because national permission and completion totals are compared without weighting for project size or tail cases, the long right tail of slow projects goes undercounted. The cohort figure — 32 months median, with a long upper tail that reaches years — is the one a homebuyer or planner should actually use.

A third surprise is Dublin. The prior expectation was that Dublin's land costs and planning friction would make it the slowest market. It is the opposite: Dublin permissions start 45 days faster on average than elsewhere in Ireland, and about two-thirds of that advantage is because Dublin has far fewer one-off rural dwellings — the single slowest category in the whole dataset.

## What It Means

For a prospective homebuyer: once a scheme near you has planning permission, expect roughly two and a half years before the homes change hands. A development that was granted planning in early 2024 will, if typical, certify completion around mid-to-late 2026.

For a county-level housing target: the share of permissions that "go dark" is not a big lever. Most permissions do get built; they just get built slowly. Policy attention is better spent on the commencement-to-completion leg than on permission-refusal or developer land-banking.

For policy audit: league tables ranking counties by completion rates are partly ranking differences in how diligently counties file their completion paperwork. We published a channel-adjusted ranking that strips out this filing-rate effect. Under that adjustment, the mid-sized 50-to-199 unit dwelling schemes in a geographically diverse set of counties — Offaly, Leitrim, Clare, Kilkenny, Cork County, Wicklow, Dublin City — are the consistent delivery workhorses, not the high-density urban cohort the raw ranking favoured.

## How We Did It

We used the [Building Control Management System dataset](https://data.nbco.gov.ie/) maintained by the National Building Control Office, which records the grant date, commencement notice, and completion certificate for every building-regulations project in Ireland since 2014. We restricted the data to residential permissions (183,633 of them), then applied standard survival-analysis techniques to estimate how long projects take to reach each pipeline step, with bootstrap confidence intervals on the medians and stratification by scheme size, region, and tenure. Completion-rate league tables were adjusted for differences in filing discipline across the 31 building-control authorities.

## Further Reading

- [Building Control Management System dataset](https://data.nbco.gov.ie/) — the project-level source data
- [Central Statistics Office housing series (HSM13)](https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/HSM13/JSON-stat/2.0/en) — the aggregate completions series for cross-check
- Harter & Morris (2021). Measuring lags between permit and completion in US data. US Census Bureau — the methodological parallel
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_commencement_notices/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
