---
title: "Most households ignored variable electricity pricing"
date: 2026-04-11
domain: "Energy / Demand Response"
blurb: "Every net-zero plan assumes people will move their electricity use to when renewable power is cheap. A 2013 London trial tested that assumption at scale."
weight: 30
tags: ["energy", "demand-response", "time-of-use", "electricity", "smart-meters", "London"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/tou_demand_response/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** When London households were offered electricity prices that swung from 4 pence to 67 pence per kilowatt-hour depending on the time of day, about 60 percent did not meaningfully shift their consumption. The households that did respond were mostly those whose routines already matched the cheap periods — not people who actively changed their behaviour.

## The Question

Every decarbonisation plan assumes that households will move their electricity use away from peak hours when given the right price signal. Time-of-use tariffs are the most common mechanism: charge more during the evening peak (when fossil gas plants fire up) and less overnight (when wind is abundant). Industry surveys consistently report that roughly 75 percent of customers on time-of-use rates do not actually shift their consumption. This matters — if demand response does not work at scale, the grid cannot absorb the variable renewable generation that climate targets require.

Using the largest publicly available smart meter trial with dynamic pricing, we asked two questions. What fraction of households genuinely shifted load? And can their pre-trial consumption patterns predict who will respond?

## What we found

Using half-hourly smart meter data from 1,117 households on a dynamic time-of-use tariff and 1,100 control households on a flat rate during the 2013 London Low Carbon London trial, the answers were sobering.

- Households on the variable tariff reduced their peak-period consumption share by 5.6 percent compared to the control group. The difference is statistically robust, but the effect is small.
- About three-in-five households — 60.1 percent, with a tight confidence band of 57.4 to 63.1 percent — did not meaningfully shift their consumption under our main definition of "shifting". That share is sensitive to how strictly you define the word: anywhere from 31 to 84 percent, depending on threshold.
- The strongest predictor of who shifts is the pre-trial evening peak ratio itself. Households whose evening consumption was already relatively flat before the trial were the ones most likely to be classified as shifters. That is the opposite of what grid planners expect.
- A simple statistical model achieves about 70 percent accuracy at predicting who will respond — better than random, but not accurate enough to guarantee individual outcomes.
- High-price events covered only 4.5 percent of the year (788 half-hours out of 17,520) at 67.2 pence per kilowatt-hour, versus the normal 11.76 pence. Households cannot realistically maintain vigilance for rare events.

![Distribution of peak-period consumption ratios for the variable-tariff group versus the flat-rate control group](plots/headline_finding.png)

## Why that matters

The headline — that most households do not shift — is not surprising. It matches the 75 percent non-response estimate from industry surveys and the broader behavioural-economics literature on the gap between price signals and real behaviour. What is surprising is the direction of the strongest predictor.

Households with a *lower* pre-trial evening peak were *more* likely to be classified as shifters. This is counterintuitive. You might expect that households with high evening peaks — big TVs, electric cooking, evening laundry — would have the most room to shift and the strongest incentive to do so. Instead, households whose consumption was already relatively flat, perhaps because they had irregular schedules or fewer fixed-time appliances, continued that flat pattern under the new tariff, and that continuation got labelled as "shifting".

This raises an uncomfortable possibility. What is being measured as load shifting may partly be pre-existing lifestyle patterns that happen to align with the tariff structure, rather than genuine behavioural change. The aggregate 5.6 percent reduction is real, but it is well below the 15 to 20 percent that grid planners sometimes assume when modelling future demand response.

## What it means in practice

**For grid planners and regulators.** Voluntary time-of-use tariffs are unlikely to deliver the flexibility that net-zero grids require. Even in a well-designed trial with a 17-to-1 price ratio and smart in-home displays, only about 40 percent of self-selected participants shifted meaningfully — and the general population would almost certainly do less. Plans that assume 15 to 20 percent peak reductions from time-of-use pricing alone are over-optimistic.

**For utilities.** Pre-trial consumption patterns contain useful but limited targeting information. They are accurate enough to choose which neighbourhoods to market a variable tariff to, but not accurate enough to promise any individual household a given result.

**For policymakers.** The rarity of the high-price events (about 4.5 percent of the year) may be the problem more than the tariff itself. If the price signal only fires a few dozen days a year, households cannot build habits around it. More frequent price variation, or automated load control (smart thermostats, hot water timers, EV smart-charging), is likely necessary for meaningful demand flexibility — leaving it to human attention and motivation is not enough.

![Sensitivity of shifter classification to threshold choice](plots/shifter_threshold_sensitivity.png)

## What could be different

We stress-tested the findings. A permutation test rules out chance. Pre-trial features are computed from 2012 data and post-trial labels from 2013, with no household crossing between train and test folds. Bootstrap confidence intervals are tight on the three central estimates. The self-selection caveat remains: ToU households volunteered for the trial and are probably more price-responsive than average, which means the 60 percent non-shifter estimate is a lower bound — the true share in the general population is likely higher, not lower.

## How we did it

We used the [Low Carbon London smart meter dataset](https://data.london.gov.uk/dataset/smartmeter-energy-use-data-in-london-households/) (5,566 households, half-hourly readings, November 2011 to February 2014) from UK Power Networks. The dynamic time-of-use tariff schedule came from the [Data_Low_Carbon_London repository](https://github.com/groupoasys/Data_Low_Carbon_London). We extracted 16 consumption features from the 2012 pre-trial period, merged them with the 2013 tariff schedule to compute peak-period consumption ratios, and classified households as "shifters" based on whether their peak ratio fell meaningfully below the control-group mean. A simple linear model was compared to tree-based alternatives under five-fold stratified cross-validation. No synthetic data were used.

## Further reading

- UK Power Networks (2014). *Low Carbon London Project Summary Report* — the source trial from which the data was collected.
- Schofield J. et al. (2014). *Residential consumer responsiveness to time-varying pricing*, UK Power Networks Low Carbon London Learning Report A3 — the official analysis of this trial dataset.
- Faruqui A, Sergici S. (2010). ["Household response to dynamic pricing of electricity: a survey of 15 experiments"](https://doi.org/10.1007/s11149-010-9127-y), *Journal of Regulatory Economics* — meta-analysis finding 3 to 6 percent peak reduction from time-of-use pricing alone.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/tou_demand_response/paper.md) — all diagnostics and robustness checks.
