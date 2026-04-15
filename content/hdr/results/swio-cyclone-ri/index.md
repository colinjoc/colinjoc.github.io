---
title: "Predicting Which Indian Ocean Cyclones Will Suddenly Explode — Without Any Weather-Model Data"
date: 2026-04-15
domain: "Tropical Cyclones"
blurb: "Tropical cyclones in the South-West Indian Ocean — the basin that produced Idai, Eloise, Batsirai, Freddy, Gezani, Fytia — sometimes rapidly intensify in 24 hours, collapsing forecast lead time from days to hours. We tested how well you can predict which storms will do this using nothing but the public best-track archive: no satellite imagery, no weather-model output, just storm position, intensity, and motion. Result: a model that ranks storms about 88 percent correctly. The reason it works is older than it looks — what a storm has already done is the strongest predictor of what it is about to do."
weight: 3
tags: ["tropical-cyclones", "indian-ocean", "rapid-intensification", "forecasting", "madagascar"]
---

*Plain-language version. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/swio_cyclone_ri/paper.md).*

## The question

When a tropical cyclone rapidly intensifies — adding 35 miles per hour of wind speed in a single day — the forecast lead time for whoever is in its path collapses. A storm projected to reach Madagascar as a tropical storm can arrive as a Category 4. The 2019 Cyclone Idai killed over a thousand people in Mozambique partly because it intensified faster than the warning system could keep up. The same pattern repeated with Eloise (2021), Batsirai (2022), Freddy (2023), and most recently Gezani and Fytia in early 2025.

The South-West Indian Ocean — the basin that includes Madagascar, Mozambique, Mauritius, La Réunion, and the western Australian approaches — sees about ten named storms a year. Roughly four in ten of them will undergo at least one rapid intensification episode in their lifetime. The operational forecast question is: **which ones**?

The orthodox answer requires expensive inputs. National weather services run forecasts that ingest satellite imagery, ocean temperatures, atmospheric soundings from weather balloons, and the output of several global atmospheric models. We asked a deliberately bare-bones question: how well can you predict rapid intensification using nothing but the freely-downloadable historical best-track archive? Just position, intensity, and how the storm has been moving — no weather-model data, no satellite, no ocean.

## What we found

A simple machine-learning model trained on the South Indian best-track archive from 1980 to 2024 — about 50,000 six-hourly observations from 800 named storms — distinguishes storms that are about to rapidly intensify from those that aren't, with about 88 percent ranking accuracy. The exact number was 0.886 by the standard ROC-AUC metric, with a 95 percent confidence interval (computed by storm-cluster bootstrap) of 0.83 to 0.92.

That number is meaningfully above the 50 percent we'd get by random guessing, and it's a few points better than the published prior expectation for best-track-only models in this basin (around 0.72-0.78). When we added gradient-boosted decision trees instead of plain logistic regression, we crept up further to about 0.91.

The model survives the full battery of robustness checks an econometrician would demand:

- **Permutation null test**: scrambling the labels and re-running everything 200 times produces accuracies of 0.44 to 0.55. Our 0.88 is far outside that range. The signal is real.
- **Leave-one-season-out cross-validation**: hold out a different year each time and predict it from the rest; we get 0.879 instead of 0.886. Almost identical. The model generalises across years.
- **Storm-cluster bootstrap confidence intervals**: tightly bracketed around the point estimate.
- **Drop the most suspicious feature** (the storm's own intensification rate over the past 24 hours, which sounds like it might leak information about the next 24 hours): accuracy is unchanged. The model isn't cheating with autocorrelation.

Two important caveats came back from the same checks:

- **Pre-2000 data does not work**. When we trained and tested only on storms before 2000, the model collapsed to AUC=0.39 — worse than guessing. The pre-2000 best-track records for this basin have known intensity-quality issues that make rapid intensification ill-defined. The honest claim is for the satellite era only.
- **The model is a ranker, not a probability forecaster**. Its raw outputs are not well-calibrated probabilities even after standard recalibration. It tells you which storms are most likely to undergo rapid intensification *relative to others*. It does not give you "there is a 30 percent chance Cyclone Foo will rapid-intensify."

![Mean peak rapid-intensification risk per storm, by season. The trend is consistent with the known increase in Indian Ocean cyclone intensity through the satellite era.](plots/swio_seasonal_ri_risk.png)

## Why that's surprising

Tropical-cyclone forecasting is a multi-billion-euro industry. Operational systems use sophisticated environmental data — vertical wind shear from atmospheric reanalyses, sea-surface temperature from satellite-borne radiometers, deep-ocean heat content from drifting buoys, mid-tropospheric humidity from radio occultation. The published expectation is that a model without those features should not do well.

Our model has none of those. It has where the storm is, how strong it is, how strong it was 6, 12, and 24 hours ago, how far from land it is, and how its intensity has been changing. Six features. And it gets to 0.88 anyway.

The reason isn't mysterious. The strongest single predictor of what a tropical cyclone will do in the next 24 hours is what it has already done. A storm that was 30 knots stronger 24 hours ago than it was 24 hours before that has revealed something about its environment that the environmental data is also trying to measure. The track-only model is implicitly using the storm itself as a sensor for the conditions around it. This is the lesson the Atlantic-basin SHIPS-RII forecast system has been quietly demonstrating for two decades.

What the track-only model cannot do is tell you which side of that conditional probability distribution will dominate when the storm enters new territory. Once a storm crosses into a region with sharply different ocean temperatures or wind shear, its history is much less informative. That's where the environmental features earn their keep.

## What it means

For people in the path of Indian Ocean cyclones, the practical implication is that even very simple monitoring systems — the kind a small country with no national weather service of its own could run — can give meaningful pre-warning of rapid-intensification candidates. The data is free. The model fits in a laptop in a few seconds. The accuracy is about 88 percent at distinguishing rapid intensifiers from the rest.

What it cannot do is replace the operational systems run by Météo-France La Réunion (the regional warning centre for SWIO) and the Joint Typhoon Warning Center. Those systems do additional things our model does not — calibrated probability forecasts, integration with track-position uncertainty, and most importantly, the environmental-feature integration that pushes accuracy from 0.88 toward 0.95 or higher.

The forward step we did not take in this analysis is the obvious one: combine the best-track features with publicly available NOAA sea-surface-temperature data and ECMWF reanalysis wind shear. The published evidence suggests this would close most of the gap to operational performance. The technical specification is in the project's Phase B notes; the only blocker is the climate-data API that requires an academic registration we did not have time to set up in this analysis run.

## How we did it

We downloaded the IBTrACS South Indian best-track archive from NOAA, kept observations from 1980 onwards (when satellite-quality intensity becomes reliable), labelled each six-hourly observation with whether the storm's wind speed would increase by at least 30 knots over the following 24 hours, and trained a class-weighted logistic regression and gradient-boosted trees with storm-grouped 10-fold cross-validation throughout. The full code, robustness battery, reviewer-mandated experiments, and per-storm risk rankings are in the linked paper.
