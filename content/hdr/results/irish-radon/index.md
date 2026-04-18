---
title: "Ireland's radon map misses the places it matters most"
date: 2026-04-11
domain: "Environmental Science / Public Health"
blurb: "Radon kills about 250 Irish people a year. Only three in a hundred homes have been tested. A model trained on geology alone cannot yet fix that."
weight: 24
tags: ["radon", "Ireland", "geology", "public-health", "spatial-prediction", "environmental-risk"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/irish_radon/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Radon is the second leading cause of lung cancer in Ireland, after smoking, and only three in every hundred homes have ever been tested. We trained a model on five geological datasets to predict which parts of the country are dangerous without needing to test every house. The model catches barely half the high-radon areas, and underestimates the very worst zones by 25 percentage points — exactly where accurate warnings matter most.

## The question

Radon is an invisible, odourless radioactive gas that seeps from the ground into buildings. It causes roughly 250 lung cancer deaths in Ireland every year. The Environmental Protection Agency designates "High Radon Areas" on a 10-kilometre grid, but only about 3 percent of Ireland's 2 million homes have actually been tested. We asked whether publicly available geological data — airborne radioactivity surveys, bedrock maps, glacial soil maps — could predict which grid squares are dangerous without testing every house.

## What we found

The model identifies real geological patterns. It is not accurate enough to use for public health screening on its own.

- The model misses 57 percent of actual High Radon Areas. It catches barely half the dangerous zones and flags a fair number of safe ones as dangerous.
- The failure is worst where it matters most. For the 32 grid squares where more than 30 percent of homes exceed the danger threshold — Ireland's most dangerous places — the model predicts an average of only 13 percent. It underpredicts by 25 percentage points in the areas where accurate warnings are most needed.
- The strongest geological predictors are geographic position, the ratio of uranium to thorium from airborne radioactivity surveys, and specific bedrock formations — particularly Carboniferous marine shelf limestone, which has moderate uranium but high permeability from ancient cave systems.
- Switching from a simple model to a more flexible one gets the biggest single gain — roughly 10 percent more accurate overall. Additional feature engineering adds only another 2 percent on top.
- Earlier Irish studies reported higher accuracy. When we replicate their evaluation method — picking test and training data randomly — we match their numbers. The gap comes entirely from how we evaluate: splitting the data by county, so the model cannot peek at geological neighbours it was trained on. The stricter evaluation reveals that the conventional approach overstates accuracy by about 10 percent.

## Why that matters

Conventional wisdom in radon mapping says the airborne uranium measurement is the single best predictor of indoor radon. Our analysis complicates that. Geographic position and the ratio of uranium to thorium outrank the raw uranium signal. But there is a twist — the airborne uranium data we had access to was extracted from colour-rendered map images rather than raw scientific measurements. That is like reading a thermometer from a photograph: the general trend is there but the precision at the extremes is lost. So the finding that rock type matters more than uranium intensity might be partly an artefact of degraded data, rather than a real geological hierarchy. Without access to the raw measurements, we cannot distinguish the two explanations.

The underprediction pattern is also striking. The model regresses so hard toward the average that for the most dangerous parts of Ireland, it predicts radon levels less than half the actual values. That is a known pathology of flexible models trained on heavily skewed data — most of Ireland has low radon, a small tail has very high radon, and the model learns to play it safe. Unfortunately, playing it safe fails exactly where failure has the highest public-health cost.

## What it means in practice

**For homeowners.** This model is not ready to tell you whether your house is at risk. The only reliable answer is a direct measurement — the EPA sells kits for about 30 euros. If you live in a county flagged as High Radon Area by the current EPA map, the case for testing is strong.

**For policymakers.** The model is not a substitute for direct measurement, but it does identify where direct measurement would be most valuable. The counties where the model is most uncertain — Sligo, Carlow, Louth, all at geological boundary zones — are ideal targets for focused measurement campaigns. Ireland's National Retrofit Plan aims to make 500,000 homes more energy-efficient by 2030, and sealing a house on uranium-rich bedrock can trap radon inside. The geological risk factors identified here — granite bedrock, granitic glacial soils, karstified limestone — could feed a retrofit risk-screening checklist even if the full model is not accurate enough to replace direct measurement.

**For researchers.** Two immediate improvements are available. First, obtain the raw airborne survey data in physical units from the Geological Survey Ireland, which would resolve the central ambiguity about uranium's predictive value. Second, evaluation methodology matters enormously — standard random splits overstate accuracy on spatial data by a clear margin, and future studies should default to spatial cross-validation.

## How we did it

We used five publicly available datasets: the [EPA radon grid map](https://www.epa.ie/environment-and-you/radon/radon-map/) (820 grid squares based on 63,914 home measurements), the [Geological Survey Ireland Tellus airborne radiometric survey](https://www.gsi.ie/en-ie/programmes-and-projects/tellus/Pages/Data-Downloads.aspx), the [all-island bedrock geology map](https://www.gsi.ie/en-ie/data-and-maps/Pages/Bedrock.aspx), the national subsoils map, and county boundaries. We engineered 53 geological features and evaluated four model families using spatial cross-validation grouped by county, which stops the model from using geologically-similar neighbours as training data for itself.

## Further reading

- Elio J. et al. (2022), "Estimation of residential radon in Ireland using geology, TELLUS radiometric data and indoor radon measurements", *Science of the Total Environment*. [doi:10.1016/j.scitotenv.2022.155677](https://doi.org/10.1016/j.scitotenv.2022.155677) — the current state of the art for Irish radon prediction.
- Roberts D.R. et al. (2017), "Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure", *Ecography* 40(8):913-929. [doi:10.1111/ecog.02881](https://doi.org/10.1111/ecog.02881) — why standard cross-validation overstates accuracy on spatial data.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/irish_radon/paper.md) — all experiments, feature importance analysis, and spatial diagnostic tables.
