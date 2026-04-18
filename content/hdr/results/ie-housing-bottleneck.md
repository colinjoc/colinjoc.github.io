---
title: "Ireland's housing bottleneck is at the top of the pipeline"
date: 2026-04-17
domain: "Irish Housing Policy"
blurb: "Ireland's housing debate is mostly about the middle of the pipeline — appeals, objectors, developer delay. Rank all ten candidate chokepoints and the binding one is none of those."
weight: 8
tags: ["housing", "ireland", "policy", "theory-of-constraints", "bottleneck-analysis"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_housing_bottleneck/paper.md) has the Monte Carlo ranking and the ten-chokepoint waterfall. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Ireland wants 50,500 new homes a year. It built 34,177 in 2024. The public debate is dominated by fixes to the middle of the pipeline — judicial reviews, anti-hoarding measures, faster appeals. The arithmetic says none of those is the binding constraint. Ireland is not primarily stuck in the middle. It is starved at the top. Permissions have been flat since 2019, and no combination of efficiency fixes can close the gap.

## The question

Ireland has a well-known housing shortfall. The government's Housing for All plan targets 50,500 new homes per year; actual completions hit 34,177 in 2024, leaving a gap of roughly sixteen thousand homes. Public debate cycles through suspects — lengthy planning appeals, judicial reviews by objectors, developers hoarding approvals without building, a slow certification regime. Each has its own advocates and its own proposed fix.

We asked a more basic question. Of the ten candidate chokepoints in Ireland's permission-to-completion pipeline, which one is actually binding? Which single fix — if applied today — would deliver the most additional homes per year?

## What we found

The binding constraint is the number of planning permissions being granted. Ireland has issued roughly 38,000 permissions per year since 2019, flat with no upward trend. Every other chokepoint is a second-order problem.

- Even if permissions were converted to built homes at 100 percent yield — a physical impossibility — the current 38,000-per-year ceiling still cannot reach 50,500 completions.
- Construction-sector capacity is the second constraint, at roughly 35,000 homes per year in 2024. If permissions rose sharply, the building industry would run out of workers before the target was met.
- Halving the lapse rate, raising certification compliance by ten points, and restoring planning-appeal turnaround to its pre-crisis standard — combined — add only about 5,000 homes a year. That closes about a third of the gap, and no more.
- The widely quoted 35 percent pipeline yield figure is largely an accounting artefact. About a third of homes are built by self-builders who are legally exempt from filing a completion certificate. They are occupied, connected to the electricity grid, and lived in — but invisible to the certification system.
- Once that measurement gap is corrected, Ireland's effective pipeline yield is about 61 percent, comparable to the UK (60 percent). The pipeline is not unusually leaky by international standards.
- A Monte Carlo analysis drew 5,000 parameter sets from the full uncertainty ranges in the source data. Permission volume was the top-ranked bottleneck in 100 percent of those draws.

## Why that matters

The entire Irish housing-policy conversation over the past five years has been dominated by proposals to fix the middle of the pipeline. Anti-hoarding measures would penalise developers who let permissions lapse. Judicial-review reform would stop environmental groups from blocking large schemes in court. Faster planning-appeal decisions would unblock projects in the queue. Each has political champions and each addresses a real problem.

The arithmetic is unforgiving. In a steady-state pipeline, friction parameters like delay and lapse affect when homes get built, not how many get built per year. Only two things change the annual flow: how many permissions enter at the top, and how many the construction sector can deliver at the bottom. Every other intervention is pushing on something that is not the constraint — and the Theory of Constraints, developed in manufacturing in the 1980s, predicts that pushing on non-constraints yields zero additional output. That prediction held here.

## What it means in practice

**For voters.** The most politically visible proposals — judicial-review reform, anti-hoarding penalties, faster appeals — are worth doing but cannot close the gap on their own. They add a few thousand homes a year, not tens of thousands.

**For policymakers.** The diagnosis points to a two-pronged strategy. First, dramatically increase the number of planning permissions granted — through zoning reform, public-land release, and easier routes to approval for dense housing. Second, invest in construction-sector capacity, because permissions without builders hit the capacity ceiling well before they hit the target. The Housing for All target is not reachable by tweaking the middle of the pipeline. It requires opening the top and the bottom at once.

**For developers and self-builders.** The one-off self-build route, which is regulatorily exempt from the certification paperwork, accounts for about a third of all housing actually delivered in Ireland. The official statistics understate its contribution.

## How we did it

This is a synthesis study, pulling together thirteen predecessor analyses of different stages of the Irish housing pipeline — [planning permissions](https://data.cso.ie/), completion statistics, commencement-notice timing, lapse rates, planning-appeal durations, judicial-review costs, and the Land Development Agency's delivery record. We combined the measured parameters from those studies into a single waterfall model, then applied five complementary approaches — a simple stage-by-stage accounting, a sensitivity ranking, a Theory of Constraints identification, a structural path model, and a Monte Carlo simulation that propagated every parameter's uncertainty. All five agreed on the same answer.

## Further reading

- [Central Statistics Office — New Dwelling Completions (NDA12)](https://data.cso.ie/) — the national completions series.
- [Housing for All (Government of Ireland, 2021)](https://www.gov.ie/en/publication/ef5ec-housing-for-all-a-new-housing-plan-for-ireland/) — the 50,500-home-per-year target.
- [Housing Commission Final Report (2024)](https://www.gov.ie/en/publication/e8145-report-of-the-housing-commission/) — the policy backdrop.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_housing_bottleneck/paper.md) — the full meta-analysis, with sensitivity sweeps and the bottleneck ranking table.
