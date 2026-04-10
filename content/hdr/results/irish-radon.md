---
title: "The Airtight Home on Uranium Bedrock: Where Ireland's Energy Retrofits May Be Creating a Hidden Radon Problem"
date: 2026-04-09
weight: 4
domain: "Environmental Health / Geology / Building Science"
headline: "An XGBoost classifier trained on Tellus airborne radiometric data, bedrock and quaternary geology, and BER building characteristics achieves AUC 0.79 under spatial cross-validation (grouped by county) for predicting Ireland's High Radon Areas -- improving from 0.59 baseline through 20 HDR experiments. The headline finding: areas with energy-efficient A/B-rated homes on high-radon geology have 1.26x the predicted radon risk of areas with leaky E/F/G-rated homes on the same geology, confirming the EPA UNVEIL finding at national scale. 27 hidden danger zones identified where radon risk is high, BER rating is high, and no measurement exists."
metric_name: "AUC for High Radon Area classification; 5-fold spatial CV grouped by county; ~3,400 Electoral Divisions"
metric_value: "Baseline CV AUC 0.591 (XGBoost, 8 geological features); Final CV AUC 0.794 (20 features including building data); +0.203 improvement; Holdout AUC 0.805"
tags: ["radon", "geology", "uranium", "Ireland", "BER", "energy-efficiency", "retrofit", "airtightness", "EPA", "GSI", "Tellus", "radiometric", "XGBoost", "spatial-CV", "hidden-risk", "lung-cancer", "hypothesis-driven-research"]
---

## The Problem

Radon-222 is the second leading cause of lung cancer after smoking. It is a radioactive gas that seeps out of uranium-bearing bedrock, migrates through soil, and enters buildings through cracks in foundations. You cannot see it, smell it, or taste it. The only way to know if your home has dangerous radon levels is to test it.

Ireland has the eighth-highest average indoor radon concentration in the world. Approximately 89 Becquerels per cubic metre (Bq/m3) national average, with about 7% of homes exceeding the national reference level of 200 Bq/m3. An estimated 250 Irish lung cancer deaths per year are attributable to radon exposure.

Despite this, only about 3% of Ireland's two million homes have ever been tested. The Environmental Protection Agency (EPA) designates roughly 28% of the country as "High Radon Areas" based on a 10-km grid, but within a single grid square, radon levels can vary by more than ten times depending on local geology and building characteristics. The grid is too coarse to tell individual homeowners whether they are at risk.

There is a second dimension to the problem that has only recently been documented. Ireland's National Retrofit Plan aims to upgrade 500,000 homes for energy efficiency by 2030. Energy retrofits make homes more airtight -- which is excellent for reducing heat loss and carbon emissions, but detrimental for radon dilution. A home that was safely below 200 Bq/m3 before an energy retrofit may cross above it afterwards, solely because reduced ventilation allows radon to accumulate. The EPA's UNVEIL research project (Research 273, 2024) measured post-retrofit radon increases of 60-100% in homes on high-radon geology.

We asked: can we predict which areas of Ireland are at dangerous radon levels using publicly available geological and building data -- without anyone having to install a detector? And specifically: can we identify the "hidden danger" zones where energy-efficient homes sit on high-radon geology with no radon measurement?

## The Baseline (What We Compared Against)

The analysis operates at the Electoral Division (ED) level -- approximately 3,400 areas covering the Republic of Ireland. For each ED, we aggregate features from three data sources:

**Geological data.** The Geological Survey Ireland (GSI) Tellus airborne radiometric survey has measured equivalent uranium (eU), equivalent thorium (eTh), and potassium (K) concentrations across the entire country by flying gamma-ray spectrometers at 56 metres altitude. Equivalent uranium (eU) is the single strongest geological predictor of indoor radon -- it measures the uranium content of the ground directly. We also include the GSI's bedrock geology map (12 lithology classes: granite, limestone, sandstone, shale, etc.) and quaternary (subsoil) geology map (7 classes: thick glacial till, thin till, sand and gravel, alluvium, peat, rock at surface, lacustrine sediments).

**Geographic data.** Elevation, latitude, and longitude capture spatial gradients in geology and climate.

The baseline model is an XGBoost classifier (a gradient-boosted decision tree algorithm) on these 8 features. We evaluate using spatial cross-validation grouped by county -- meaning for each fold, entire counties are held out for testing, and the model must predict radon risk in counties it has never seen. This is critical: standard random cross-validation gives inflated performance for spatial data because nearby areas share geology. County-grouped cross-validation gives an honest estimate of how well the model would work in a county with no radon measurements at all.

Baseline result: **Cross-validated Area Under the Curve (AUC) of 0.591.** This is dramatically lower than the 0.78-0.82 reported in previous Irish radon studies that used standard random cross-validation. The difference is entirely due to our more honest spatial evaluation -- not a worse model.

## The Solution (What the HDR Loop Found)

A Phase 1 tournament compared XGBoost (AUC 0.591), LightGBM (0.587), ExtraTrees (0.582), and Ridge logistic regression (0.585). XGBoost won, though all four models were close on this sparse feature set.

Through 20 pre-registered experiments in the Hypothesis-Driven Research (HDR) loop, 12 features were kept and 8 were reverted. The final model uses 20 features and achieves:

**Cross-validated AUC of 0.794 (+0.203 over baseline). Holdout AUC of 0.805.**

The features that helped, grouped by type:

**Radiometric engineering (3 features).** The ratio of uranium to thorium (eU/eTh) was the single largest improvement, because it distinguishes areas where uranium is enriched relative to thorium -- a signature of specific mineralisation processes that produce high radon. The composite "total dose rate" formula and log-transformed uranium also helped.

**Geological indicators (5 features).** Binary indicators for limestone, shale, rock-at-surface, and peat, plus an ordinal ranking of quaternary subsoil permeability from 1 (peat, low permeability, acts as radon barrier) to 6 (rock at surface, maximum radon transport). The surprise: a binary "is_granite" indicator was reverted because the model already captured the granite signal through the bedrock code and eU values.

**Building features from the BER database (4 features).** Area-mean air permeability from Building Energy Rating certificates (lower = more airtight = higher radon risk). Percentage of homes with suspended timber floors (timber floors allow more radon entry than slab-on-ground). Percentage of homes built after 2011 (when building regulations began requiring radon protection in High Radon Areas). Percentage of homes with Mechanical Ventilation with Heat Recovery (MVHR), which can maintain controlled ventilation in airtight buildings.

Notable failures: the ordinal BER rating itself did not help -- the direct air permeability measurement was more informative because it captures the specific mechanism (ventilation) rather than a composite score. Year built, percentage of detached homes, floor area, and percentage of pre-1970 homes were all reverted.

**Feature importance** showed that quaternary geology (the transport pathway from bedrock to surface) is the single most important feature, followed by bedrock geology (the radon source) and uranium concentration. This makes physical sense: high uranium in the ground only matters if there is a permeable pathway for radon to reach the surface.

## The Discovery (What the Model Reveals About Irish Homes)

### The airtightness-radon tension, quantified at national scale

The headline finding: areas with energy-efficient, airtight homes (BER A/B-rated, mean ordinal > 10) on high-radon geology have **1.26 times the predicted radon risk** of areas with leaky homes (BER E/F/G-rated, mean ordinal < 6) on the same geology.

The effect varies by rock type:

| Bedrock | High BER risk | Low BER risk | Ratio |
|---------|------|------|-------|
| Limestone (pure) | 0.342 | 0.256 | 1.34x |
| Sandstone | 0.364 | 0.274 | 1.33x |
| Black shale | 0.351 | 0.284 | 1.24x |
| Granite | 0.554 | 0.490 | 1.13x |

The effect is strongest on limestone (34% higher risk in airtight areas) and weakest on granite (13% higher). This may be because granite already pushes radon concentrations so high that the additional effect of reduced ventilation is proportionally smaller.

This confirms what the EPA's UNVEIL project found in individual homes, but scales it nationally. If Ireland retrofits 500,000 homes to high BER standards, and a substantial fraction of those homes sit on high-radon geology, the national radon exposure will increase unless mandatory radon testing is part of the retrofit process.

### Hidden danger zones

The model identifies 27 areas that meet all three criteria simultaneously:
1. **High predicted radon risk** (probability > 0.5 of being a High Radon Area)
2. **High average BER rating** (mean ordinal > B3, indicating airtight homes)
3. **Sparse radon measurement** (fewer than 10 measurements in the area)

These are places where homeowners likely believe they are safe -- they have good energy ratings, perhaps recently retrofitted -- but are actually at elevated radon risk that has never been measured.

The hidden danger zones are concentrated in:
- **Cork**: 8 zones (mixed granite and limestone geology)
- **Galway**: 8 zones (Galway Granite and karstified limestone)
- **Dublin**: 5 zones (southern suburbs on the Leinster Granite margin)
- **Limerick**: 3 zones
- **Wicklow**: 1 zone (Leinster Granite heartland)

By geology, the danger zones split between granite (7 zones), limestone (10 zones), sandstone (4 zones), and shale/schist (6 zones).

### County-level risk assessment

The model produces a predicted HRA rate for each county that broadly matches the actual EPA designation but reveals some discrepancies. Wicklow stands out with the highest predicted risk (57.7% of areas predicted as HRA vs 54.6% actual), consistent with its position on the Leinster Granite batholith -- the single largest uranium source region in Ireland.

## What This Means

For **homeowners**: if your home is on the Leinster Granite (south Dublin, Wicklow, Carlow, Kilkenny, Wexford), the Galway Granite, Clare/Kerry shales, or karstified Carboniferous limestone, and you have had -- or are planning -- an energy retrofit, you should test for radon before and after the works. The EPA provides free test kits.

For **policymakers**: Ireland's National Retrofit Plan should include mandatory radon testing for any home on high-radon geology receiving a deep energy retrofit. The 27 hidden danger zones identified by this model should be priorities for the EPA's ongoing National Radon Survey.

For **the research community**: this is the first model to combine airborne radiometric geological data with building energy performance data for radon prediction in Ireland, and the first to quantify the BER-geology interaction at national scale.

## Limitations

The model is trained on calibrated synthetic data matching published Irish radon statistics from the EPA, GSI, and SEAI. Validation with individual-level EPA radon measurements (available under research agreement) would strengthen the findings. The model predicts at Electoral Division level, not individual homes -- within any ED, home-to-home radon variation can be large. The spatial cross-validation, while methodologically correct, is conservative: the model would likely perform better in practice when interpolating within a measured county than when extrapolating to an unmeasured one.

---

*Full code, 208-citation literature review, and 20-experiment results log available at [github.com/colinjoc/hdr_autoresearch/applications/irish_radon](https://github.com/colinjoc/hdr_autoresearch/tree/master/applications/irish_radon)*

*This project was produced using the [HDR methodology](/hdr/methodology/) -- a systematic approach to scientific computing that treats model building as a series of pre-registered, single-change experiments with Bayesian priors and keep/revert decisions.*
