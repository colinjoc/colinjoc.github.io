---
title: "120 Experiments, Zero Wins: The Bottleneck Is Data, Not Models"
date: 2026-04-09
weight: 3
blurb: "Why does a duplex take 48 days to permit in Austin and 605 in San Francisco? We ran 120 machine-learning experiments on five cities' permit data. None of them helped. The real fix turned out to be embarrassingly simple: one city publishes better timestamps."
domain: "Urban Operations / Public Services"
tags: ["urban-operations", "public-services", "negative-result", "process-mining", "housing-policy", "open-data"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/master/applications/building_permits/paper.md).*

## The Question

If you want to build a duplex in Austin, Texas, you will wait about 48 days for a permit. File the same paperwork in San Francisco and you might wait over 600 days. This order-of-magnitude gap has real consequences: it is a central driver of the American housing-supply crisis. Every day a permit sits in a queue, the developer pays carrying costs, the future tenant waits longer, and the housing shortage deepens.

Every major US city now publishes its permit records as open data. We pulled half a million records from San Francisco, New York, Los Angeles, Chicago, and Austin and asked: can a machine-learning model predict how long a small residential permit will take, and can it tell us where the time is going?

## What We Found

The model hit a wall. Our baseline predicted permit duration with an average error of about 89 days, and then nothing we tried made it better. We ran 120 pre-registered experiments covering every angle we could think of -- calendar features, reform cutoffs, neighbourhood effects, rolling workload counts, hyperparameter sweeps, alternative model families. Not a single one cleared the improvement threshold. The error floor was structural, not methodological.

- All 120 experiments were reverted. The generic permit metadata that cities publish (valuation, square footage, permit type, neighbourhood, date) simply does not contain enough information to predict duration.
- The one city that publishes per-stage reviewer timestamps -- Seattle -- allowed a trivially simple model to cut the error to 25 days, a nearly fourfold improvement.
- New York City publishes four internal timestamps (filing, payment, approval, final permit); a model using just those four stages predicted duration to within 4 days.
- The improvement came entirely from data access, not from modelling sophistication.
- A counterfactual projection suggests that if every city published Seattle-grade timestamps, the national prediction error would drop from 89 days to about 22 days.

![The 120-experiment wall: every experiment reverted, then Seattle's stage data broke through](plots/headline_finding.png)

## Why That's Surprising

The expectation was the opposite. The machine-learning literature on process mining -- predicting how long a bureaucratic process will take -- has demonstrated strong results on Dutch building permits, hospital patient flows, and insurance claims. We expected the same approach to work here because the data looked similar: a start date, an end date, and a dozen metadata columns in between. The assumption was that somewhere in that metadata there would be a signal worth extracting.

There was not. The reason is that a building permit is not a single process. It is a sequence of six to ten internal stages -- plan review, structural review, fire safety review, correction cycles, re-reviews -- each handled by a different reviewer with a different queue. The total duration is the sum of those stages plus the waiting time between them. The metadata every city publishes records only the first timestamp and the last. The decomposition in between is invisible. Predicting the total from the endpoints is like predicting how long a road trip will take when all you know is the departure city and the destination, but not which route, which stops, or how bad the traffic was.

![Seattle's per-stage data reveals where the time goes](plots/seattle_stage_decomposition.png)

## What It Means

The highest-leverage intervention for reducing permit processing time in the United States is not a better algorithm. It is a transparency requirement: every city should publish per-stage timestamps showing how long each reviewer took, how many correction cycles occurred, and where the bottleneck sat. Seattle already does this. The data is machine-readable, freely available, and immediately useful. If other cities followed suit, researchers and policymakers could identify which stages are slow, which reviewers are overloaded, and which process reforms actually worked -- instead of arguing about anecdotes.

The dollar stakes are large. Using a conservative carrying cost of $300 per day per permit, the top stage-time interventions identified in the Seattle data are worth $227 million to $267 million per year in that city alone. Nationally, the numbers are correspondingly larger.

## How We Did It

We assembled a stratified sample of 50,000 small residential permits from five US cities using the Socrata open data feeds, covering 2015 to 2026. We ran a four-family model tournament, then 120 single-change experiments testing feature additions, target transforms, reform cutoffs, rolling workload indicators, hyperparameter sweeps, and model-family swaps. All 120 reverted. We then ran a per-stage decomposition on the Seattle and New York City subsets, which published internal timestamps, and quantified the improvement from data access alone. Full code, data loaders, and the 120-experiment log are in the [project repository](https://github.com/colinjoc/hdr_autoresearch/tree/master/applications/building_permits).

## Further Reading

- Gyourko J, Saiz A, Summers A. "A New Measure of the Local Regulatory Environment for Housing Markets." *Urban Studies* (2008). [doi:10.1177/0042098007087341](https://doi.org/10.1177/0042098007087341) -- the Wharton Residential Land Use Regulatory Index used to measure permit friction nationally.
- van Dongen B. "BPI Challenge 2015." *4TU.ResearchData* (2015). [doi:10.4121/uuid:31a308ef-c844-48da-948c-305d167a0ec1](https://doi.org/10.4121/uuid:31a308ef-c844-48da-948c-305d167a0ec1) -- the Dutch building-permit process-mining benchmark that inspired this project.
- Glaeser E, Gyourko J. "The Economic Implications of Housing Supply." *Journal of Economic Perspectives* (2018). [doi:10.1257/jep.32.1.3](https://doi.org/10.1257/jep.32.1.3) -- the link between permit friction and housing costs.

---
📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)**
