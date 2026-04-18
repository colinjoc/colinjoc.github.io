---
title: "From planning permission to front door: the Irish housing pipeline"
date: 2026-04-18
domain: "Irish Housing"
blurb: "Ireland grants planning permission for about 60,000 homes a year. Tracing each one through to an actual front door reveals why completions come in below that."
weight: 2
tags: ["housing", "ireland", "pipeline", "planning-permission", "commencement", "completion"]
---

*A plain-language summary. The [full technical paper set](https://github.com/colinjoc/generalized_hdr_autoresearch/tree/main/applications) — five linked studies — has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

*Part 2 of 4 in the Irish Housing series. Previous: [Part 1: Economics](/hdr/results/irish-housing-economics/) | Next: [Part 3: Planning and judicial review](/hdr/results/irish-planning-and-judicial-review/) | [Part 4: What would fix it](/hdr/results/irish-housing-bottleneck-and-levers/)*

**Bottom line.** Of every 100 Irish residential planning permissions granted, about 60 end up as actual built homes. Another 35 are built but never file a completion certificate because self-built homes are legally exempt from the filing requirement. The median permission-to-front-door journey takes 32 months. About 9.5 percent of permissions lapse without ever starting construction. At current yields, hitting the government's 50,500-homes-a-year target requires 85,000 permissions annually — more than double the current rate.

## The question

Ireland's annual housing completions number is a headline. But what is behind it? Every house that gets built has travelled through a pipeline — from a planning permission granted on paper, to ground being broken on site, to a completion certificate filed when the work is done. How much drop-off happens at each stage? How long does each leg take? And how many permissions does Ireland actually need to grant in order to hit its completion target?

## What we found

![Pipeline yield: the share of permissions that reach each stage, split by certificate-filed and actually-built.](plots/yield.png)

- Of 100 residential permissions granted in the 2014-2019 cohort, about 90 had construction commenced within the tracking window. The remaining 10 lapsed — permission granted but never used.
- Of those 90, roughly 35 went on to file a completion certificate. Another 25 or so were built but never filed, because self-built one-off homes are legally exempt from the filing requirement. So the "built" yield is around 60 per 100 permissions, even though the certificate-filed yield is only 35.
- The median journey from planning permission to completion certificate is 962 days — about 32 months. The first leg, permission to ground being broken, takes 232 days. The second leg, construction itself, takes 498 days.
- Apartment schemes take 53 days longer than one-off houses. Multi-phase developments add 288 days. Dublin is 45 days faster than average, mostly because Dublin has more small one-off projects that commence quickly.
- About 9.5 percent of permissions lapse without the builder ever breaking ground. Bigger schemes lapse more — 9 percent for single-unit permissions, 19 percent for schemes of 50 units or more. This is consistent with bigger developments having more exposure to market cycles.
- The Land Development Agency, the State's delivery arm, completed about 850 homes in 2023 — around 3 percent of the Housing for All target. All of that came through forward-purchasing privately-built homes rather than direct construction.
- At a build-yield of 60 percent, hitting the government's 50,500-completions target requires roughly 85,000 permissions granted per year. Ireland currently grants about 38,000. That is less than half what is needed.

## Why that matters

There is a persistent narrative that "Irish builders sit on permissions". The data does not support it at scale. Roughly nine in ten permissions do get used — construction commences — within the tracking window. The lapse rate is real but it is 10 percent, not the 27 percent figure that circulated in earlier analyses (which turned out to be an artefact of database ID-format mismatches, not a genuine signal).

More importantly, the pipeline is not where Ireland's housing shortage lives. Every step in the pipeline is running at broadly the rate you would expect. The shortage is upstream — in how many permissions get filed in the first place. At 38,000 permissions a year and a 60 percent build yield, the maximum achievable completions are around 23,000. The government's target is 50,500. The gap is not a pipeline problem; it is a permission-volume problem.

## What it means in practice

**For policymakers.** Pipeline fixes — faster planning appeals, fewer judicial reviews, lower lapse rates — each add real but small numbers of completions. The binding constraint is permission volume, which sits upstream of the pipeline entirely. Solving the pipeline without solving permission volume caps you at roughly 23,000 homes a year.

**For builders and developers.** The median permission-to-completion journey is under three years, with the construction leg dominating. Apartment and multi-phase schemes run appreciably longer. The one-off-dwelling path is the fastest — not coincidentally, it is also the path with the least filing burden.

**For buyers waiting on a new home.** The typical journey from the day a builder gets their permission to the day you can move in is about 32 months. Apartments run two months longer than houses. If you are watching a specific scheme progress, ground being broken is usually about eight months after permission is granted.

## How we did it

This synthesis consolidates five linked studies. The foundation is the [Building Control Management System register](https://www.localgov.ie/bcms), which tracks commencement notices and completion certificates across Ireland. We built a 183,633-row cohort dataset — the first publicly reproduced version of this for Ireland — linking planning permissions to commencement notices to completion certificates. We computed median durations at each stage with bootstrap confidence intervals, ran survival analysis on the 2017-2019 permissions cohort to estimate lapse rates, and cross-referenced Land Development Agency output against the national completions series.

## Further reading

- [Building Control Management System](https://www.localgov.ie/bcms) — the commencement and completion register used throughout.
- [Commencement cohort study](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_commencement_notices/paper.md).
- [Lapsed permissions study](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_lapsed_permissions/paper.md).
- [End-to-end pipeline yield](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_housing_pipeline_e2e/paper.md).
- [Land Development Agency delivery](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_lda_delivery/paper.md).
