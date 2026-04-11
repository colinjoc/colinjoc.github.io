---
title: "34 Experiments, Zero Wins: Why Building-Permit Delays Resist Machine Learning"
date: 2026-04-10
weight: 3
blurb: "We ran 34 machine-learning experiments on 50,000 building permits from five US cities. None improved the baseline. Then Seattle's per-stage timestamps cut the error fourfold -- not because the model got smarter, but because the data got better."
domain: "Urban Operations / Public Services"
tags: ["urban-operations", "public-services", "negative-result", "process-mining", "housing-policy", "open-data"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/master/applications/building_permits/paper.md).*

## The Question

If you want to build a duplex in Austin, Texas, you will wait about 48 days for a permit. File the same paperwork in San Francisco and you might wait over 600 days. This order-of-magnitude gap has real consequences: every day a permit sits in a queue, the developer pays carrying costs, the future tenant waits longer, and the housing shortage deepens.

Every major US city now publishes its permit records as open data. We pulled 50,000 records from San Francisco, New York, Los Angeles, Chicago, and Austin and asked: can a machine-learning model predict how long a small residential permit will take, and can it tell us where the time is going?

## What We Found

The model hit a wall. Our baseline predicted permit duration with a Mean Absolute Error (MAE) of about 89 days, and then nothing we tried made it better. We pre-registered 120 hypotheses and ran 34 of them to completion on the cross-city sample -- calendar features, reform cutoffs, neighbourhood effects, rolling workload counts, hyperparameter sweeps, target transforms, and alternative model families. The remaining 86 were deferred due to schema mismatches or missing external data. Not a single completed experiment cleared the improvement threshold. The best one shaved 0.36 days off the baseline. The error floor was structural, not methodological.

- All 34 completed experiments were reverted. The generic permit metadata that cities publish (valuation, square footage, permit type, neighbourhood, date) simply does not contain enough information to predict duration.
- Seattle publishes per-stage reviewer timestamps. Using just two features from that decomposition -- city plan-review time and applicant correction time -- a simple model cut the within-Seattle error from 100 days to 25 days, a fourfold improvement. Under temporal holdout (train on 2015--2022, test on 2023+), the MAE was 28 days, confirming the result is not an artefact of data leakage.
- New York City publishes four internal timestamps (filing, payment, approval, final permit). A model using those four stages predicted duration to within 4 days -- though this is a near-tautology, since the stages sum approximately to the target.
- The improvement came entirely from data access, not from modelling sophistication.

![The 34-experiment wall: every experiment reverted, then Seattle's stage data broke through](plots/headline_finding.png)

## Why That's Surprising

The machine-learning literature on process mining -- predicting how long a bureaucratic process will take -- has demonstrated strong results on Dutch building permits, hospital patient flows, and insurance claims. We expected the same approach to work here because the data looked similar: a start date, an end date, and a dozen metadata columns in between. The assumption was that somewhere in that metadata there would be a signal worth extracting.

There was not. A building permit is not a single process. It is a sequence of six to ten internal stages -- plan review, structural review, fire safety review, correction cycles, re-reviews -- each handled by a different reviewer with a different queue. The total duration is the sum of those stages plus the waiting time between them. The metadata every city publishes records only the first timestamp and the last. The decomposition in between is invisible. Predicting the total from the endpoints is like predicting how long a road trip will take when all you know is the departure city and the destination, but not which route, which stops, or how bad the traffic was.

The Seattle decomposition also inverted the folk wisdom. Permit applicants tend to assume "the city is waiting for me to fix my corrections." In fact, city plan-review time explains 39 percent of the variance in total duration -- more than double the 19 percent explained by applicant corrections. The single most informative predictor of whether a given permit will be slow is how long the city has been reviewing it.

![Seattle's per-stage data reveals where the time goes](plots/seattle_stage_decomposition.png)

## What It Means

The highest-leverage intervention for reducing permit processing time in the United States is not a better algorithm. It is a transparency requirement: every city should publish per-stage timestamps showing how long each reviewer took, how many correction cycles occurred, and where the bottleneck sat. Seattle already does this. The data is machine-readable, freely available, and immediately useful. If other cities followed suit, researchers and policymakers could identify which stages are slow, which reviewers are overloaded, and which process reforms actually worked -- instead of arguing about anecdotes.

The dollar stakes are meaningful but uncertain. Under a sensitivity analysis varying the assumed per-day carrying cost from $100 to $500, the top stage-time interventions identified in the Seattle data are worth $11 million to $55 million per year in that city alone (central estimate: $33 million at $300 per day). For New York City's post-approval pickup bottleneck -- where 55 percent of total elapsed time is just the owner coming to collect the approved permit -- the range is $18 million to $88 million per year. These are upper-bound projections assuming one-for-one day savings and no general-equilibrium effects. The true values are likely smaller but the order of magnitude is policy-relevant.

![Duration distributions vary enormously across cities](plots/duration_by_city.png)

## How We Did It

We assembled a stratified sample of 50,000 small residential permits from five US cities using the Socrata open data feeds, covering 2015 to 2026. We ran a four-family model tournament to select the best model family (Extreme Gradient Boosting), then executed 34 single-change experiments testing feature additions, target transforms, reform cutoffs, rolling workload indicators, hyperparameter sweeps, and model-family swaps. All 34 reverted. We then ran a per-stage decomposition on the Seattle subset -- the only US city in our sample that publishes per-(review-type, cycle) timestamps -- and quantified the improvement from data access alone. The Seattle model was validated under both shuffled cross-validation and a temporal train/test split. Full code, data loaders, and the experiment log are in the [project repository](https://github.com/colinjoc/hdr_autoresearch/tree/master/applications/building_permits).

## Further Reading

- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/master/applications/building_permits/paper.md) -- methodology, all 34 experiments, variance decomposition, and dollar projections
- Gyourko J, Saiz A, Summers A. "A New Measure of the Local Regulatory Environment for Housing Markets." *Urban Studies* (2008). [doi:10.1177/0042098007087341](https://doi.org/10.1177/0042098007087341) -- the Wharton Residential Land Use Regulatory Index used to measure permit friction nationally
- van Dongen B. "BPI Challenge 2015." *4TU.ResearchData* (2015). [doi:10.4121/uuid:31a308ef-c844-48da-948c-305d167a0ec1](https://doi.org/10.4121/uuid:31a308ef-c844-48da-948c-305d167a0ec1) -- the Dutch building-permit process-mining benchmark that inspired this project
- Glaeser E, Gyourko J. "The Economic Implications of Housing Supply." *Journal of Economic Perspectives* (2018). [doi:10.1257/jep.32.1.3](https://doi.org/10.1257/jep.32.1.3) -- the link between permit friction and housing costs
