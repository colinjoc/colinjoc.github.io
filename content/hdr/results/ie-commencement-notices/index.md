---
title: "How long does an Irish home really take to build?"
date: 2026-05-08
domain: "Housing policy / Construction economics"
blurb: "Ireland argues about housing supply using two charts that never meet. We rebuilt the link between them, project by project, and the answer is 32 months."
weight: 35
tags: ["housing-policy", "ireland", "construction", "survival-analysis", "open-data", "commencement-notices"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_commencement_notices/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** From the day a planning permission is granted to the day a Certificate of Completion and Compliance is filed, the typical Irish residential project takes about 32 months — eight months longer than the standard aggregate-statistics estimate. Almost no permissions are truly abandoned, but only a fraction of started homes ever get a completion certificate filed against them, and that gap is mostly a question of paperwork rather than vacant building sites.

## The question

Every quarter, two Irish charts get waved at each other in the housing debate. One shows planning permissions granted. The other shows new dwellings completed. The country has spent a decade trying to read the gap between them as a single number — how long, on average, does a permission take to become a finished home?

The honest answer was: nobody knew. The two series are national totals, smoothed across thousands of projects of wildly different sizes. You can slide one against the other and find the lag that lines them up best, but that lag cannot tell you whether the pipeline is short and leaky or long and patient. It produces the same answer either way.

The Building Control Management System changes that. Since 2014, every residential building project in Ireland has had to file a commencement notice before breaking ground and a Certificate of Completion and Compliance before being signed off. Each filing carries dates and an identifier linking it back to the original planning permission. We pulled the full public extract — n = 183,633 residential permissions granted between 2014 and 2025 — and rebuilt the pipeline one project at a time.

## What we found

<figure>
<img src="plots/baseline_survival.png" alt="Two survival curves. The left curve falls steeply and crosses the half-way line at 232 days; the right curve falls more slowly and never reaches half, plateauing above 50 percent un-certified.">
<figcaption>Left: time from permission granted to commencement on site, with the typical project starting at 232 days. Right: time from commencement to completion certificate. The right curve never crosses the half-way line because more than half of started projects have no completion certificate on file — a paperwork channel, not an abandonment rate.</figcaption>
</figure>

- The typical permission takes 232 days to start. From start to certified completion takes another 498 days. Stitched together for the projects we can follow end-to-end, the typical permission-to-certificate journey is 962 days — close to 32 months.
- The conventional aggregate-lag estimate, drawn from sliding national charts against each other, gives roughly 24 months. It under-states the real gap by about a third because it cannot see the long right tail.
- Hardly any permissions are dead on the page. Of permissions granted long enough ago to have been used, only about two-thirds of one percent never filed a commencement notice within six years. The "dark permission" panic that recurs in Irish housing commentary is, on a strict reading, almost nothing.
- But there is a far larger filing-discipline gap. Among started projects that are not exempt from the certificate process, around 39 percent never have a completion certificate filed at all. That number is sometimes paraded as evidence of abandoned developments. It is not. It is mostly the difference between a building being finished and the paperwork that says it is finished.
- Apartments take about 53 days longer than houses to go from on-site start to certificate. Schemes of 200 or more units take about 574 days just to start, against 160 days for one-off houses. Multi-phase developments are slowest of all.
- Dublin starts faster, not slower. Permissions in the four Dublin local authorities reach commencement 45 days quicker than the rest of Ireland. About two-thirds of that advantage is composition — Dublin has fewer slow-to-start one-off rural houses — but a real residual remains, driven by the largest schemes.
- The big strategic-housing-development era of 2017 to 2021, designed to fast-track large urban schemes, is associated with permission-to-start times about 70 days longer than the rest of the period. Faster planning consents produced slower starts, consistent with a pipeline of very large permissions tied up in judicial review.
- Approved housing bodies — the not-for-profit social-housing developers — reach the certificate stage at about 87 percent of the rate of private developers after controlling for project size and type. The raw 46-day gap shrinks once you adjust for the fact that approved housing bodies build larger, more apartment-heavy schemes, but it does not vanish.

## Why that matters

Ireland's housing-supply targets are set in completed-dwelling units, not permissions. The whole point of a Housing for All target is to know, at any moment, how much of the pipeline is real. If the cohort journey is 32 months and the Government's flagship aggregate-statistic produces 24, every five-year supply forecast is off by roughly a quarter of its time horizon. Permissions granted in 2026 will not become finished homes until the back half of 2028 at the earliest, and that is the median project — half are slower.

The dark-permission story matters too, in the opposite direction. Public commentary regularly cites large numbers of "permitted but unbuilt" homes. On the cleanest definition — did anyone ever turn up to file a commencement notice — that number is essentially zero. The big number is a different number: it counts started projects whose paperwork at the other end is missing. Treating those as abandoned is wrong, and using them to justify levies, claw-backs, or use-it-or-lose-it rules would be aimed at a problem that does not exist.

Finally, the local-authority league tables that get published off this data have a quiet flaw. Local authorities differ enormously in how strictly they chase up the final certificate — filing rates run from 11 to 69 percent. The headline rankings are partly a story about which councils are diligent paper-shufflers, not which areas deliver the most homes. Once you adjust for filing discipline, the top-performing combination is not Dublin commuter-belt at all. It is mid-sized dwelling schemes — 50 to 199 units — spread across Offaly, Leitrim, Clare, Kilkenny, Cork County, Wicklow, and Carlow.

## What it means in practice

**For homebuyers.** A permission granted today is, on the median, two-and-a-half years from being a finished house you can move into, and longer if it is an apartment in a large scheme. Press releases that count permissions as if they were keys-on-the-mat are misleading by about thirty months.

**For developers.** Scale costs you time. Going from a 10-49 unit scheme to a 200-plus scheme adds more than seven months to the time-to-start alone, before any of the build itself. Multi-phase delivery adds more again. The premium on large urban apartments is real and has not eased.

**For policymakers.** Two specific numbers to retire. First, the 24-month rule of thumb derived from sliding the planning and completion charts against each other — the cohort number is 32. Second, any "dark permission" figure pulled from completion-certificate filings — that statistic mixes filing discipline with construction outcomes and cannot bear the policy weight that has been placed on it. The honest dark-permission rate sits between two-thirds of one percent and 39 percent depending on which channel you mean. Picking either number alone is not defensible.

A direct policy lever falls out of this. If the country wants the league tables to mean something, mandate certificate filing the same way commencement notices are mandated, with a published deadline. The variation between local authorities collapses overnight, and the national completion series stops being a measurement of paperwork.

## How we did it

We built three project-level cohorts from the [Building Control Management System](https://data.nbco.gov.ie/) public extract: every residential permission granted from 2014 onward, every project that filed a commencement notice, and the subset where all three dates — grant, start, and completion certificate — are populated. We applied standard time-to-event statistics from medical survival analysis, treating "time to commencement" the way an oncologist treats "time to event," with right-censoring for projects that have not yet started. The headline numbers carry bootstrap confidence intervals; the medians above are tight to within a handful of days. We then ran the same models with covariates for scheme size, apartment-versus-house, Dublin, approved-housing-body status, and grant year, to separate composition from genuine effect. A gradient-boosted classifier trained to predict abandoned permissions looked impressive on data it had already seen and collapsed on data from later years; we report this as a caution rather than a forecasting tool.

## Further reading

- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_commencement_notices/paper.md) — methodology, model comparison, channel-bound analysis, and the channel-adjusted local-authority ranking.
- [BCMS open dataset](https://data.nbco.gov.ie/) — the underlying commencement-notice and certificate filings, published by the National Building Control Office.
- [CSO new dwelling completions (NDQ)](https://data.cso.ie/) — the aggregate completions series this work compares against.
- Harter J, Morris D. ["Measuring lags between permit and completion in US data."](https://www.census.gov/) US Census Bureau (2021) — the methodological precedent for cohort-level permit-to-completion latency in housing data.
- Saiz A. ["The Geographic Determinants of Housing Supply."](https://doi.org/10.1162/qjec.2010.125.3.1253) *Quarterly Journal of Economics* (2010) — the standard reference on regulatory friction and urban supply elasticity.
