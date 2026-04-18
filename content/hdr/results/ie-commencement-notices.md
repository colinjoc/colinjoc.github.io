---
title: "How long does an Irish home really take to build?"
date: 2026-04-17
domain: "Housing Policy"
blurb: "Everyone agrees Irish homes take too long to build. Almost nobody had followed individual projects through the system from paperwork to front door. We did."
weight: 12
tags: ["ireland", "housing", "construction", "survival-analysis", "policy"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_commencement_notices/paper.md) has the stratification tables and sensitivity analysis. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** From the day a council grants planning permission to the day the finished home is certified, a typical Irish residential project takes 32 months. That is about eight months longer than the figure implied by the official aggregate statistics — and the gap between the two numbers has quietly misdirected the policy debate.

## The question

"We grant plenty of permissions, but nothing gets built." Some version of that sentence is routine in Irish housing debate. The number of permissions granted each quarter is published, and so is the number of completions. The gap between the two is usually estimated by lining up the national totals and asking how far back you have to shift the permissions series to make it match — a statistical trick, not a measurement.

We wanted a real answer. For the individual projects granted permission since 2014, how long did they take to start, how long did they take to finish, and how many never began at all?

## What we found

Starting from the building-control filings every developer must submit, we followed each residential permission from grant to first shovel to final certificate.

- From permission granted to a declared start on site: **232 days** — around seven and a half months.
- From declared start to certified completion: **498 days** — around sixteen and a half months.
- End-to-end, for projects we can track all the way through: **962 days, or 32 months**.
- Fewer than one permission in 150 — 0.67 percent — never results in a commencement notice inside six years. The "dark permissions" problem at the start of the pipeline is very small.
- The share of permissions whose completion certificate is never filed is much larger — up to 39 percent for schemes required to file one — but this is a filing-discipline issue, not construction abandonment.
- Apartments take 53 days longer than conventional dwellings to go from start to certificate, a gap that has survived two decades of policy attention to apartment viability.

The 32-month end-to-end figure is about eight months longer than the 24-month lag implied by the traditional aggregate-series method.

## Why that matters

The folk story of Irish housing features large numbers of "land-banked" permissions that are granted and sat on. The data do not support that under the simplest definition. Only around 0.67 percent of residential permissions granted have no commencement notice at all after six years. The slow part of the pipeline is not developers refusing to start — it is projects that start and then take a very long time to finish.

The aggregate method also understates the real wait. National permission and completion totals are compared without weighting for project size or tail cases, so the long right tail of slow projects goes undercounted. The cohort figure — 32 months at the median, with an upper tail reaching years — is the one a homebuyer or planner should actually use.

A third surprise was Dublin. The prior expectation was that Dublin's land costs and planning friction would make it the slowest market. It is the opposite. Dublin permissions start 45 days faster on average than elsewhere, and about two-thirds of that advantage is because Dublin has far fewer one-off rural dwellings — the single slowest category in the whole dataset.

## What it means in practice

**For prospective homebuyers.** Once a scheme near you has planning permission, expect roughly two and a half years before the homes change hands. A development granted planning in early 2024 will, if typical, certify completion around mid to late 2026.

**For county-level housing targets.** The share of permissions that "go dark" is not a big lever. Most permissions do get built — they just get built slowly. Policy attention is better spent on the commencement-to-completion leg than on permission-refusal or developer land-banking.

**For policy auditors.** League tables ranking counties by completion rates are partly ranking differences in how diligently counties file their completion paperwork. Under a filing-discipline-adjusted ranking, the mid-sized 50-to-199 unit schemes in a geographically diverse set of counties — Offaly, Leitrim, Clare, Kilkenny, Cork County, Wicklow, Dublin City — are the consistent delivery workhorses, not the high-density urban cohort the raw ranking favours.

## How we did it

We used the [Building Control Management System dataset](https://data.nbco.gov.ie/), maintained by the National Building Control Office, which records the grant date, commencement notice, and completion certificate for every building-regulations project in Ireland since 2014. We restricted to residential permissions — 183,633 projects — and applied standard survival analysis to estimate how long projects take to reach each pipeline step, with bootstrap confidence intervals on the medians and stratification by scheme size, region, and tenure. Completion-rate league tables were adjusted for differences in filing discipline across the 31 building-control authorities.

## Further reading

- [Building Control Management System dataset](https://data.nbco.gov.ie/) — the project-level source data.
- [Central Statistics Office housing series (HSM13)](https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/HSM13/JSON-stat/2.0/en) — the aggregate completions series used as a cross-check.
- Harter & Morris (2021). Measuring lags between permit and completion in US data. US Census Bureau — the methodological parallel.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_commencement_notices/paper.md).
