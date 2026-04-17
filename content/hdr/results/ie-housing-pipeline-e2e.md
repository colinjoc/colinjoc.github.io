---
title: "For Every 100 Irish Permissions, How Many Become Homes?"
date: 2026-04-17
domain: "Irish Housing Policy"
blurb: "Ireland's planning system is often accused of producing paper houses — approvals that never turn into bricks. We traced the path from permission to completion for 85,565 residential projects granted between 2014 and 2019 and found that about 35 out of every 100 permissions produce a certified home on paper, but about 60 out of 100 actually become real, occupied homes. The difference is a measurement gap, not a failure rate."
weight: 10
tags: ["housing", "ireland", "planning-permissions", "pipeline-analysis"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_housing_pipeline_e2e/paper.md).*

## The Question

Ireland's housing crisis has been narrated for a decade in aggregate numbers — permissions granted in year X, completions recorded in year Y, a gap between them that everyone agrees is too large. But nobody had actually traced permissions *through* the pipeline: of all the permissions a council grants today, how many become homes someone lives in? And where, along the way, are they lost?

We built the first end-to-end pipeline yield estimate for Irish residential housing, following a cohort of 85,565 projects from the moment permission was granted to the moment a completion certificate was filed.

## What We Found

**For every 100 residential planning permissions granted in Ireland, about 35 produce a certified home — but about 60 produce a home that is actually built and lived in.** The difference is the most important number in this study.

- About 9 or 10 out of every 100 permissions never produce a commencement notice at all. These are genuine lapses, where the developer walked away.
- Of the remaining 90, only about 41 end up filing a completion certificate. That sounds like a disaster. It isn't.
- Roughly a third of all commenced projects are one-off self-builds, which are legally exempt from filing a completion certificate under the 2014 Building Control regulations. Those homes are built, connected to the electricity grid, and occupied — they just never appear in the certification database.
- Once that exemption is accounted for, the effective build-yield rises to about 60%, in line with the UK and within the normal range for comparable countries.
- The median time from permission to certified completion is 1,096 days — three years — with substantial variation: a quarter of projects complete in under two years, a quarter take more than four and a half.
- Scheme size matters enormously. Single-unit projects file certificates 12% of the time (because they are mostly self-builds); multi-unit schemes file 68% to 89% of the time, depending on size.
- Housing Associations file certificates at 72%, versus 40% for private developers. Multi-phase schemes file at 85%, versus 27% for single-phase.

## Why That's Surprising

The common reading of Irish housing statistics — "the system loses two-thirds of its permissions" — turns out to be largely a measurement artefact. About half of the apparent loss is regulatory paperwork that was never required in the first place, not homes that were never built. This changes the policy diagnosis dramatically.

The surprise goes in both directions. Optimistically, the Irish pipeline is not uniquely broken compared to peer countries. Pessimistically, even at the favourable 60% build-yield, Ireland would need about 85,000 planning permissions per year to deliver the Housing for All target of 50,500 homes — more than double the current volume of roughly 38,000. At the stricter certification-based yield, the figure rises to 144,000. Either number is far out of reach under current approval rates. The binding constraint is the number of permissions being granted, not the efficiency with which they are converted.

A second surprise: among the models tested, a sophisticated survival analysis performed no better than random at predicting which permissions would eventually complete. With the administrative fields available, individual project outcomes are genuinely hard to forecast. The pipeline yield emerges only at the population level.

## What It Means

For a homeowner or would-be buyer, the realistic picture is that about 60 out of every 100 approved homes will actually be built and occupied — not the 35 suggested by the certification statistics. The housing pipeline is leaky, but much less leaky than the headline numbers imply.

For a policymaker, the implication shifts focus. Tightening the certification regime or chasing lapsed permissions can each add a few thousand homes per year. But even combined, they cannot close the gap to the national target. Only increasing the number of permissions granted, in concert with expanding construction-sector capacity, can reach 50,500 per year. A secondary recommendation flows from the measurement gap itself: extending completion-certificate requirements to self-builds would close the gap between the administrative and physical pictures, giving everyone a clearer view of what is actually happening.

For a self-builder, the finding is reassuring in one way: people who commence one-off homes overwhelmingly finish them, even though the paperwork trail vanishes.

## How We Did It

We combined four data sources: the [Building Control Management System](https://nbco.localgov.ie/) (which records commencement and completion filings for all regulated building work), the National Planning Application register, the [Central Statistics Office](https://data.cso.ie/) aggregate permissions and completions series, and the Land Development Agency's published delivery figures. For the residential cohort with permissions granted between 2014 and 2019 — giving at least six years of follow-up time — we estimated each stage of the pipeline independently (permission-to-commencement, commencement-to-certificate, certificate-to-occupied home) and combined them multiplicatively. The same yield was then estimated with a Markov transition model, a survival model, a discrete-event simulation, and a logistic regression as cross-checks.

## Further Reading

- [Central Statistics Office — Housing statistics](https://data.cso.ie/) — the aggregate permissions and completions series.
- [National Building Control Office](https://nbco.localgov.ie/) — the building-control data source.
- [Housing for All (Government of Ireland, 2021)](https://www.gov.ie/en/publication/ef5ec-housing-for-all-a-new-housing-plan-for-ireland/) — the national target.
- [Detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_housing_pipeline_e2e/paper.md) — with the full stratification tables and sensitivity analysis.

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
