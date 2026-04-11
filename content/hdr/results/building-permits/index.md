---
title: "34 Experiments, Zero Wins: Permit Delays Need Data, Not Models"
date: 2026-04-11
domain: "Urban Operations / Housing Policy"
blurb: "We ran 34 machine-learning experiments on 50,000 building permits from five US cities. None improved the baseline. Then Seattle's per-stage timestamps cut the prediction error fourfold -- not because the model got smarter, but because the data got better."
weight: 3
tags: ["urban-operations", "housing-policy", "negative-result", "process-mining", "open-data", "building-permits"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/building_permits/paper.md).*

## The Question

A duplex permit in Austin, Texas takes about 91 days. The same permit in San Francisco can take over 600 days. This order-of-magnitude gap has real consequences: every day a permit sits in a queue, the developer pays carrying costs on land and construction loans, the future tenant waits longer, and the housing shortage deepens.

Every major US city now publishes its permit records as open data. We pulled 50,000 small residential permit records from San Francisco, New York, Los Angeles, Chicago, and Austin and asked: can a machine-learning model predict how long a permit will take, and can it tell us where the time is going?

## What We Found

The model hit a wall. Our baseline predicted permit duration with an average error of about 89 days, and then nothing we tried made it meaningfully better. We pre-registered 120 hypotheses and ran 34 of them to completion on the cross-city sample -- calendar features, reform cutoffs, neighbourhood effects, rolling workload counts, hyperparameter sweeps, target transforms, and alternative model families. The remaining 86 were deferred due to schema mismatches or missing external data. Not a single completed experiment cleared the improvement threshold. The best one shaved a third of a day off the baseline.

- **34 experiments, zero winners.** The generic permit metadata that cities publish -- valuation, square footage, permit type, neighbourhood, filing date -- simply does not contain enough information to predict duration. The best tree-based model was only 11 percent better than a simple linear model, meaning there is no hidden non-linearity waiting to be unlocked.
- **Seattle's per-stage timestamps changed everything.** Seattle publishes how long each reviewer took and how long the applicant spent on corrections. Using just those two numbers, a simple model cut the within-Seattle error from 100 days to 25 days -- a fourfold improvement. Under temporal validation (train on 2015--2022, test on 2023+), the error was 28 days, confirming the result holds on unseen time periods.
- **New York City's four internal timestamps (filing, payment, approval, final permit) predicted duration to within 4 days** -- though this is a near-tautology, since the stages sum approximately to the total.
- **The improvement came entirely from data access, not from modelling sophistication.** The winning model used a shallower tree with fewer rounds than the baseline.

![The 34-experiment wall: every experiment reverted, then Seattle's stage data broke through](plots/headline_finding.png)

## Why That's Surprising

The machine-learning literature on process mining -- predicting how long a bureaucratic process will take -- has demonstrated strong results on Dutch building permits, hospital patient flows, and insurance claims. We expected the same approach to work here because the data looked similar: a start date, an end date, and a dozen metadata columns in between. The assumption was that somewhere in that metadata there would be a signal worth extracting.

There was not. A building permit is not a single process. It is a sequence of six to ten internal stages -- plan review, structural review, fire safety review, correction cycles, re-reviews -- each handled by a different reviewer with a different queue. The total duration is the sum of those stages plus the waiting time between them. The metadata every city publishes records only the first timestamp and the last. The decomposition in between is invisible. Predicting the total from the endpoints is like predicting how long a road trip will take when all you know is the departure city and the destination, but not the route, the stops, or the traffic.

The Seattle decomposition also inverted the folk wisdom. Permit applicants tend to assume the delays are their fault -- "the city is waiting for me to fix my corrections." In fact, city plan-review time explains 39 percent of the variance in total duration, more than double the 19 percent explained by applicant corrections. The biggest predictor of whether a given permit will be slow is how long the city's own reviewers have been working on it, with drainage and zoning reviews together accounting for over half the stage-level variance.

![Seattle's per-stage data reveals where the time goes](plots/seattle_stage_decomposition.png)

## What It Means

The highest-leverage intervention for reducing permit processing time in the United States may not be a better algorithm. It may be a transparency requirement: every city should publish per-stage timestamps showing how long each reviewer took, how many correction cycles occurred, and where the bottleneck sat. Seattle already does this. The data is machine-readable, freely available, and immediately useful. If other cities followed suit, researchers and policymakers could identify which stages are slow, which reviewers are overloaded, and which process reforms actually worked.

The dollar stakes are meaningful but uncertain. Under a sensitivity analysis varying the assumed per-day carrying cost from $100 to $500, halving applicant correction time in Seattle alone would save an estimated $11 million to $56 million per year (central estimate: $33 million at $300 per day). In New York City, where 55 percent of total elapsed time is the post-approval wait for the owner to collect the permit, halving that pickup delay is projected at $18 million to $88 million per year. These are upper-bound projections assuming one-for-one day savings; the true values are likely smaller but the order of magnitude is policy-relevant.

Three intake-channel effects were also striking: in New York City, permits filed under professional self-certification cleared in a median of 6 days versus 76 days through the standard queue (a 12.7-fold difference). In Los Angeles, plan check at counter was 4 times faster than the regular queue. In Chicago, express review was 7.5 times faster than standard review. These are unadjusted comparisons that likely overstate the true causal effect, but the magnitudes suggest that expanding eligibility for fast-track channels could substantially reduce wait times.

![Duration distributions vary enormously across cities](plots/duration_by_city.png)

## How We Did It

We assembled a stratified sample of 50,000 small residential permits from five US cities using the [Socrata open data feeds](https://data.seattle.gov/Permitting/Plan-Review/tqk8-y2z5) (including the [Seattle Plan Review dataset](https://data.seattle.gov/Permitting/Plan-Review/tqk8-y2z5), the only US municipal feed with per-reviewer-cycle timestamps), covering 2015 to 2026. We ran a five-family model tournament, then executed 34 single-change experiments from a pre-registered 120-hypothesis queue. All 34 reverted. We then ran a per-stage decomposition on the Seattle subset and validated the resulting two-feature model under both shuffled cross-validation and a temporal train/test split. The full [HDR methodology](https://github.com/colinjoc/hdr_autoresearch) drove the experiment loop, and all code, data loaders, and the experiment log are in the [project repository](https://github.com/colinjoc/hdr_autoresearch/tree/main/applications/building_permits).

## Further Reading

- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/building_permits/paper.md) -- methodology, all 34 experiments, variance decomposition, and dollar projections
- Gyourko J, Saiz A, Summers A. ["A New Measure of the Local Regulatory Environment for Housing Markets."](https://doi.org/10.1177/0042098007087341) *Urban Studies* (2008) -- the Wharton Residential Land Use Regulatory Index (WRLURI), used to measure permit friction nationally
- van Dongen B. ["BPI Challenge 2015."](https://doi.org/10.4121/uuid:31a308ef-c844-48da-948c-305d167a0ec1) *4TU.ResearchData* (2015) -- the Dutch building-permit process-mining benchmark that inspired this project

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
