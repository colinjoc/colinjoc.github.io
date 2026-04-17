---
title: "Which Indian Ocean cyclones will explode overnight? A public-data baseline"
date: 2026-04-17
domain: "Atmospheric Science"
blurb: "Some tropical cyclones double in strength in a day, leaving residents of Madagascar or Mozambique hours instead of days to prepare. We built the first public-data-only forecast model for rapid intensification in the South-West Indian Ocean — a reproducible baseline that meaningfully beats coin flipping, with honest limits on how far public data can take you."
weight: 45
tags: ["tropical-cyclones", "weather-forecasting", "indian-ocean", "disaster-preparedness", "prediction"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/swio_cyclone_ri/paper.md).*

## The Question

Tropical cyclones over the South-West Indian Ocean regularly devastate Madagascar, Mozambique, Mauritius, and La Réunion. Cyclones Idai (2019), Batsirai (2022), Freddy (2023), and Fytia (2025) are recent and grim examples. The nightmare case for forecasters and emergency managers alike is the storm that rapidly intensifies — one that picks up at least thirty knots of wind speed in twenty-four hours. When that happens, the warning window for coastal populations collapses from days to hours.

Operational rapid-intensification forecasts at the United States National Hurricane Center use detailed atmospheric and ocean reanalysis data that is not easily accessible in the developing-world nations most exposed to these storms. We asked a simpler and more practical question: how much of the forecast can you recover from the free, publicly available best-track cyclone archive alone, with no reanalysis data at all?

## What We Found

Surprisingly, quite a lot — but not enough to be operationally useful on its own, and with one critical caveat about reliability before the satellite era.

- A tree-based model trained only on the public cyclone archive correctly ranks rapidly-intensifying observations against non-intensifying ones about ninety percent of the time.
- That ranking skill survives every major robustness check: it is highly statistically significant against a permutation null, it holds up under leave-one-season-out validation, and its confidence interval is tight.
- The model rarely depends on any single feature as a shortcut: even without recent wind-change information, performance is essentially unchanged.
- Restricting to the era of reliable satellite-quality observations (post-2000), performance stays around ninety percent. Before that era, the underlying data is too noisy and the model breaks down entirely.
- The model is a good ranker but a poor probability forecaster. It can tell you which storms are most at risk, but its absolute probability outputs do not beat assuming the climatological base rate — calibration, not ranking, is the open problem.

## Why That's Surprising

The field's working assumption is that meaningful skill at rapid-intensification forecasting requires the full menu of atmospheric reanalysis features: ocean heat content, vertical wind shear, mid-tropospheric humidity, potential intensity headroom. Our result is that a substantial chunk of the ranking signal lives in the best-track data itself — the size, the location, the recent intensity trajectory — and is recoverable without any reanalysis access.

The surprise is not that this replaces operational forecasting. It does not. The surprise is how much it replaces for free. A country without a reanalysis-grade forecasting infrastructure, using nothing but a publicly available archive, can build a first-pass ranker that flags about one in every eleven genuine rapid-intensification events at a decision threshold that sounds a manageable number of false alarms.

## What It Means

For disaster-preparedness teams in South-West Indian Ocean nations, the practical implication is concrete. A transparent, reproducible, public-data-only cyclone-risk ranker is feasible today. It does not replace the regional meteorological centres — the centres have, and need, far richer data. But it is a real tool for prioritisation, and it is buildable from a laptop.

For climate-forecasting researchers, our model establishes a clear public-data baseline that any future study has to beat. The path forward — adding satellite-derived sea surface temperature, ocean heat potential, and shear products — is specified in the paper. The gap between our public-only baseline and operational rapid-intensification forecasts is not closed by more clever modelling; it is closed by better features.

For emergency managers everywhere, it is a reminder that the absolute probabilities these models report cannot be taken at face value. The useful output is the ranking — which storms to watch — not the specific "thirty percent" number. Calibration is a separate, unsolved problem.

## How We Did It

We trained a tree-based ranker on the [International Best Track Archive for Climate Stewardship](https://www.ncei.noaa.gov/products/international-best-track-archive) South Indian basin records from 1980 through 2024 — a panel of roughly fifty thousand six-hourly cyclone observations across eight hundred storms. We used storm-grouped cross-validation (whole storms stay in one fold, never split across folds) and subjected the result to a permutation null that respects storm groupings, a leave-one-season-out generalisation test, an era-matched resample comparing pre-2000 versus post-2000 performance, a calibration analysis against climatology, and a storm-cluster block bootstrap.

## Further Reading

- Kaplan and DeMaria (2003), "Large-scale characteristics of rapidly intensifying tropical cyclones in the North Atlantic basin"
- Leroux et al. (2018), rapid-intensification climatology in the South Indian Ocean
- [IBTrACS v04r00 archive](https://www.ncei.noaa.gov/products/international-best-track-archive)
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/swio_cyclone_ri/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
