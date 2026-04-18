---
title: "Forecasting the Beast from the East from free weather data"
date: 2026-04-19
domain: "Atmospheric Science"
blurb: "When the polar vortex collapses, sometimes it freezes Texas and sometimes it stays aloft. Can free weather data tell you which is coming?"
weight: 22
tags: ["atmospheric-science", "polar-vortex", "stratosphere", "weather-forecasting", "null-result"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ssw_polar_vortex/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Using only the free weather indices anyone can download, a model that predicts which polar-vortex collapses will reach the ground is right about 65 percent of the time — better than a coin flip but nowhere near useful forecast skill. One specification looked like it reached 72 percent. Every robustness check took that apparent improvement apart. The real signal sits in stratospheric data that the public feeds do not include.

## The question

Every few winters, the ring of fast winds that circles the Arctic high in the stratosphere — the polar vortex — breaks down abruptly. Temperatures 30 kilometres up rise by 50 degrees Celsius in a few days. Sometimes the disturbance stays aloft and you never hear about it on the news. Sometimes it propagates down to the surface a few weeks later and delivers the kind of winter cold snap that shuts down cities: the Beast from the East that paralysed the United Kingdom in 2018, the Texas freeze of February 2021.

Roughly four in ten collapses reach the ground. Figuring out which ones is the holy grail of seasonal winter forecasting, and the lead time is real — forecasters can see the vortex weakening days before any cold air arrives. The published state of the art uses detailed atmospheric reanalysis data that is not easily accessible in every country. We asked whether you could get meaningful skill using only the free, well-known climate indices a curious amateur could download.

## What we found

On that question, the answer is essentially no.

- Using the best-known public indices — the Arctic Oscillation index, El Niño state, solar activity, and the shape of the disrupted vortex — a careful model reaches about 65 percent accuracy at separating surface-affecting collapses from those that stay aloft. Better than a coin flip (50 percent). Well short of useful forecast skill.
- One specification looked like it reached 72 percent. That felt like a finding.
- Every robustness check took it apart. The confidence interval on 72 percent stretched from 56 to 88 percent — wide enough to include chance performance.
- A permutation test that respected the multiple specifications we tried returned a borderline significance level, not a clean result.
- A single provisional event from February 2026 was doing most of the work. Remove it and the apparent improvement vanished back to 65 percent.
- Restricting to the satellite era (post-1979), where the underlying catalogue is most reliable, collapsed accuracy to 12.5 percent. The apparent signal lived in the older, less reliable pre-satellite half of the dataset.

![Calibration of the simple model. The dots show how often a predicted probability matched the observed outcome, binned by predicted probability. They sit reasonably close to the diagonal but well short of the precision a useful forecaster would need.](plots/baseline_calibration.png)

## Why that matters

The field has said for decades that the critical predictor of whether a vortex collapse reaches the surface is the persistence of the disturbance in the lower stratosphere, measured from detailed reanalysis of winds at specific altitudes. We do not have that measurement in our public panel. We tried to substitute surface signals and El Niño — which sit several causal steps away from the actual mechanism — and got exactly the performance the literature's prior would predict. Operational seasonal forecasts that do have the stratospheric data reach 85 to 95 percent on this same task. The gap between our 65 percent and their 85 percent is almost entirely the missing data.

The methodological lesson is more general. A finding that emerges from a single specification choice and falls apart under five independent robustness checks is not a finding. None of the checks are exotic — bootstrap a confidence interval, restrict to a temporal subset, drop the most leveraged observation, run a permutation null. All five killed our headline. Without them, a 72 percent accuracy claim would have been published that the data simply does not support.

## What it means in practice

**For meteorological agencies.** The result is a direct argument for continuing to make full-stratosphere reanalysis data freely accessible. That is where the real forecast skill lives, and excluding it from public feeds has a measurable cost for anyone outside the operational forecasting centres.

**For researchers building public benchmarks.** We establish an honest lower bound. Any claim that public indices alone can crack the downward-propagation problem should be tested against the five robustness checks we describe. Every "improvement" we found failed at least one.

**For curious outsiders following stratospheric forecasts online.** The hardest part of the problem — will this event actually reach the ground? — is currently unanswerable from the data feeds everyone is watching. If someone claims otherwise, ask them for the confidence interval.

## How we did it

We compiled a catalogue of 44 major stratospheric warming events from 1958 through early 2026 using the [NOAA stratospheric warming compendium](https://csl.noaa.gov/groups/csl8/sswcompendium/) and recent published events, fetched the [Climate Prediction Center's Arctic Oscillation index](https://www.cpc.ncep.noaa.gov/products/precip/CWlink/daily_ao_index/ao.shtml), the [Oceanic Niño Index](https://origin.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php), and the solar activity series, labelled each event for downward propagation, and trained a regularised classifier with leave-one-out cross-validation. We then ran a bootstrap confidence interval, a permutation null across feature sets, a leave-one-decade-out generalisation test, a leave-one-event-out sensitivity check, and an era-restricted rerun.

## Further reading

- Karpechko, Hitchcock, Peters, and Charlton-Perez (2017), "Predictability of downward-propagating stratospheric events", *Quarterly Journal of the Royal Meteorological Society* — the paper that defines what the field considers the relevant predictor.
- Domeisen et al. (2020), "The role of the stratosphere in subseasonal to seasonal prediction" — how operational forecasting systems use the full stratospheric column.
- Butler et al. (2017), "A sudden stratospheric warming compendium" — the event catalogue we built on.
- [Full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ssw_polar_vortex/paper.md) — all experiments, the full robustness battery, and the specification of the missing stratospheric feature.
