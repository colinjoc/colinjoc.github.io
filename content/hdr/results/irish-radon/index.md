---
title: "Ireland's Radon Map Misses 57% of Dangerous Areas"
date: 2026-04-11
domain: "Environmental Science / Public Health"
blurb: "Radon kills about 250 Irish people a year, but only 3 percent of homes have been tested. We trained a model on five real geological datasets to predict which 10-kilometre grid squares are most dangerous. It identifies the right geological signals but misses 57 percent of actual High Radon Areas and underpredicts the worst zones by 25 percentage points."
weight: 24
tags: ["radon", "Ireland", "geology", "public-health", "spatial-prediction", "environmental-risk"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/irish_radon/paper.md).*

## The Question

Radon is an invisible, odourless radioactive gas that seeps from the ground into buildings. It causes about 250 lung cancer deaths in Ireland every year -- the second leading cause after smoking. The Irish Environmental Protection Agency (EPA) designates "High Radon Areas" on a 10-kilometre grid, but only about 3 percent of Ireland's roughly 2 million homes have ever been tested for radon.

We asked: can publicly available geological data -- airborne radioactivity surveys, bedrock maps, glacial soil maps -- predict which grid squares are dangerous without testing every house? And how much accuracy do you lose when you evaluate your model honestly, preventing it from peeking at neighbouring grid squares that share the same geology?

## What We Found

The model identifies real geological patterns, but it is not accurate enough to screen for radon risk on its own.

- The model misses 57 percent of actual High Radon Areas. It catches barely half the dangerous zones and flags a fair number of safe ones as dangerous.
- The failure is worst where it matters most. For the 32 grid squares where more than 30 percent of homes exceed the danger threshold -- the most dangerous areas in Ireland -- the model predicts a mean of only 13 percent. It underpredicts by 25 percentage points exactly where accurate warnings are most needed.
- The strongest geological predictors are geographic position (capturing unmeasured east-west geological trends), the uranium-to-thorium ratio from airborne surveys, and specific bedrock formations -- particularly Carboniferous marine shelf limestone, which has moderate uranium but high permeability from ancient cave systems.
- Switching from a linear model to a tree-based model produces the biggest single accuracy gain (10 percent). Additional feature engineering adds only a further 2 percent.
- Previous Irish studies reported higher accuracy (measured by the area under the classification curve). When we replicate their evaluation method -- standard random cross-validation -- we match their numbers. The gap comes entirely from evaluation methodology: our county-grouped spatial cross-validation is stricter and reveals a 10 percent inflation in the conventional approach.

## Why That's Surprising

The conventional wisdom in radon mapping is that airborne uranium measurements are the single best predictor of indoor radon. Our feature analysis complicates that picture: geographic position and the ratio of uranium to thorium outrank the raw uranium signal. But there is a twist -- the airborne uranium data we used was extracted from colour-rendered map images rather than raw scientific measurements. This is like reading a thermometer from a photograph: you get the general trend but lose the precision at the extremes. The apparent finding that rock type matters more than radioactivity intensity may be partly an artifact of this degraded data, not a genuine geological hierarchy. Without access to the raw measurements, we cannot tell which explanation is correct.

The underprediction pattern is also striking: the model regresses to the mean so severely that for the most dangerous areas in Ireland, it predicts radon levels less than half the actual values. This is not a quirk of one model family -- it is an inherent problem when tree-based models are trained on a heavily skewed target where most areas have low radon and a small tail has very high radon. The model learns to play it safe, and in doing so it fails exactly where failure has the highest public health cost.

## What It Means

This model is not ready to guide public health decisions. But the geological patterns it uncovers point toward three practical next steps.

First, the counties where the model is most uncertain -- Sligo, Carlow, and Louth, all at geological boundary zones where rock types change sharply within a single grid square -- are exactly where targeted radon measurement campaigns would be most valuable. Second, Ireland's National Retrofit Plan aims to make 500,000 homes more energy-efficient by 2030, but sealing up a house on uranium-rich bedrock can trap radon inside. The geological risk factors identified here -- granite bedrock, granitic glacial soils, karstified limestone -- could contribute to a retrofit risk-screening checklist even if the full model is not accurate enough to replace direct measurement. Third, the most impactful technical improvement would be obtaining the raw airborne survey data in physical units from the Geological Survey Ireland, which would resolve the central ambiguity in this analysis.

## How We Did It

We used five publicly available datasets: the [EPA radon grid map](https://www.epa.ie/environment-and-you/radon/radon-map/) (820 grid squares based on 63,914 home measurements), the [Geological Survey Ireland Tellus airborne radiometric survey](https://www.gsi.ie/en-ie/programmes-and-projects/tellus/Pages/Data-Downloads.aspx) (uranium, thorium, and potassium), the [all-island bedrock geology map](https://www.gsi.ie/en-ie/data-and-maps/Pages/Bedrock.aspx), the national subsoils map, and county boundaries. We engineered 53 features and evaluated four model families under spatial cross-validation grouped by county, using the [HDR methodology](https://github.com/colinjoc/hdr_autoresearch) loop to test feature additions one at a time. No synthetic data were used at any stage.

## Further Reading

- Elio J. et al. "Estimation of residential radon in Ireland using geology, TELLUS radiometric data and indoor radon measurements." *Science of the Total Environment* (2022). [doi:10.1016/j.scitotenv.2022.155677](https://doi.org/10.1016/j.scitotenv.2022.155677) -- the current state of the art for Irish radon prediction.
- Roberts D.R. et al. "Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure." *Ecography* 40(8):913-929 (2017). [doi:10.1111/ecog.02881](https://doi.org/10.1111/ecog.02881) -- why standard cross-validation gives misleading results for spatial data.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/irish_radon/paper.md) -- all experiments, feature importance analysis, and spatial diagnostic tables.

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
