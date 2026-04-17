---
title: "Forecasting the 'Beast from the East' from free weather data: not yet"
date: 2026-04-17
domain: "Atmospheric Science"
blurb: "When the polar vortex collapses high in the stratosphere, the consequences can reach the ground as brutal winter cold snaps. But only some collapses make it down. We tested whether you could tell which ones from public weather indices alone — and found that the honest answer requires data most researchers can only get through restricted channels."
weight: 50
tags: ["climate", "weather-forecasting", "stratosphere", "polar-vortex", "null-result"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ssw_polar_vortex/paper.md).*

## The Question

Every few winters, the band of fast winds that circles the Arctic high in the stratosphere — the polar vortex — breaks down abruptly. When this happens, temperatures at forty kilometres altitude can jump by fifty degrees in a few days. Sometimes this disturbance stays aloft and you never hear about it on the news. Other times it propagates down to the surface weeks later, driving the kind of winter cold snap that shuts down cities: the "Beast from the East" that paralysed the United Kingdom in 2018, the Texas freeze of February 2021.

Figuring out which of these stratospheric events will actually reach the ground is the holy grail of seasonal winter forecasting. Roughly four in ten do. The published state of the art uses detailed, often restricted-access reanalysis data of winds and temperatures throughout the atmosphere. We asked whether you could get meaningful skill using only the free, well-known climate indices that a curious amateur could download.

## What We Found

On this question, the answer is essentially no.

- Using the best-known public indices — the Arctic Oscillation, the El Niño / La Niña state, solar activity, and the shape of the disrupted vortex — a careful model gets about 65% accuracy at separating downward-propagating events from those that stay aloft.
- One specification looked like it reached 72%, a meaningful jump. But every robustness check we ran dismantled that result.
- A single, provisional event from February 2026 was doing most of the work. Remove it, and the apparent improvement vanishes.
- Restricting the analysis to the modern satellite era — the period where the underlying data is most reliable — reversed the apparent gain entirely.
- Our confidence interval around the 72% number was wide enough to include chance performance.

## Why That's Surprising

There is a real temptation to believe that enough cleverness with free data can substitute for better data. Our result pushes back on that temptation hard. The literature has said for decades that the critical predictor is the persistence of the disturbance low in the stratosphere, measured from detailed reanalysis of winds at specific altitudes. We do not have that measurement in our public panel. We tried to substitute for it with the surface signals that everyone has, and we got exactly the performance that the literature's prior would predict: no better than the published ceiling on surface-index-only forecasting.

The surprise, in other words, is how little surprise there was. The data the field says matters really does matter, and an honest public-data benchmark tells you the gap between "what amateurs can do" and "what operational forecasters can do" is not a research-methodology gap. It is a data-access gap.

## What It Means

For meteorological agencies, it is a direct argument for continuing to make full-stratosphere reanalysis data freely accessible — that is where the real forecast skill lives, and excluding it from public forecasts has a measurable cost.

For researchers building public benchmarks, we establish an honest lower bound. Any claim that public indices alone can crack the downward-propagation problem should be tested against the five specific robustness checks described in our paper; every single "improvement" we found failed at least one.

For curious outsiders following stratospheric forecasts on Twitter or YouTube, it is a reminder that the hardest part of the problem — will this event actually reach the ground? — is currently unanswerable from the data feeds everyone is watching. If someone claims otherwise, ask them about their confidence interval.

## How We Did It

We built a catalogue of 44 major stratospheric warming events from 1958 to 2026 using the [NOAA Climate Science Lab's published compilation](https://csl.noaa.gov/groups/csl8/sswcompendium/) and combined it with the [Climate Prediction Center's Arctic Oscillation index](https://www.cpc.ncep.noaa.gov/products/precip/CWlink/daily_ao_index/ao.shtml) and the [Oceanic Niño Index](https://origin.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php). We then trained a regularised classifier to predict whether each event propagated downward to influence surface weather, using leave-one-out cross-validation and a battery of robustness checks including a bootstrap confidence interval, a permutation null across feature sets, a leave-one-decade-out generalisation test, and era-restricted reruns.

## Further Reading

- Karpechko, Hitchcock, Peters, and Charlton-Perez (2017), "Predictability of downward-propagating stratospheric events" — *Quarterly Journal of the Royal Meteorological Society*
- Domeisen et al. (2020), "The role of the stratosphere in subseasonal to seasonal prediction"
- Butler et al. (2017), "A sudden stratospheric warming compendium"
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ssw_polar_vortex/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
