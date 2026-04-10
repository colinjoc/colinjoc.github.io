---
title: "Ireland's Building Energy Gap: Why Your BER Rating Does Not Match Your Bills"
date: 2026-04-10
weight: 8
blurb: "An A-rated Irish home is supposed to use eight times less energy than a G-rated one. In reality, the gap is more like two to one. We trained a model on 1.33 million real BER certificates to find out what drives the rating -- and which retrofits actually make a difference on paper."
domain: "Building Energy / Retrofit Policy"
headline: "LightGBM trained on 1.33 million real SEAI Building Energy Rating certificates achieves MAE 18.05 kWh/m2/yr (R2 0.951) -- a 44% improvement over the linear baseline -- with the Heat Loss Parameter dominating by SHAP analysis; counterfactual retrofit analysis finds chimney sealing is 30 times more cost-effective per calculated kWh saved than wall insulation; all results are DEAP-calculated not measured and the literature shows real savings are 20-40% smaller"
metric_name: "Mean Absolute Error on 5-fold cross-validation of BER kWh/m2/yr prediction (1.33M real certificates)"
metric_value: "MAE 18.05 kWh/m2/yr (R2 0.951), 44% reduction from Ridge baseline MAE 32.28; chimney sealing is most cost-effective retrofit at 8 EUR per kWh/m2/yr saved"
tags: ["building-energy", "BER", "DEAP", "retrofit", "energy-performance-gap", "Ireland", "SEAI", "heat-loss", "heat-pump", "housing-policy", "gradient-boosting", "SHAP", "real-data"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/master/applications/ber_energy_gap/paper.md).*

## The Problem

Every home sold or rented in Ireland must have a Building Energy Rating (BER) certificate. The rating, from A1 (excellent) to G (worst), is calculated using the Dwelling Energy Assessment Procedure (DEAP) -- Ireland's implementation of the European standard for modelling building energy performance. An A-rated home is supposed to use under 25 kWh per square metre per year. A G-rated home supposedly uses over 450. That is an eight-to-one ratio.

But when researchers compared the BER certificates against actual gas and electricity bills, the real ratio was closer to two to one. People in draughty old houses do not actually heat every room to 21 degrees all day -- they wear jumpers, heat one room, and tolerate the cold. Meanwhile, people in well-insulated new builds crank up the thermostat because heating is cheap. The academic term for this is the "prebound and rebound effect," and it has been documented across Europe.

Ireland plans to retrofit 500,000 homes to BER B2 or better by 2030. The BER system is the yardstick for that target. So we asked: what building characteristics actually drive the BER score, and which retrofits look best on paper -- even knowing that the real savings will be smaller?

## The Data

We used the full SEAI Building Energy Rating public search dataset: 1.33 million real certificates covering roughly two-thirds of Ireland's housing stock. Each certificate contains 211 fields describing the building envelope (wall, roof, floor, and window insulation levels), heating system type and efficiency, ventilation method, lighting, and the complete energy breakdown by end-use. The data is freely available under a Creative Commons licence.

This is not synthetic data. Every record is a real BER assessment conducted by a certified assessor on a real dwelling.

## The Baseline

The starting point was a Ridge linear regression (a standard regularised linear model) on 77 features extracted from the certificates: envelope U-values, areas, construction year, heating system efficiency, ventilation type, fuel type, and several derived features including the Heat Loss Parameter (total fabric heat loss divided by floor area).

The linear model achieved a Mean Absolute Error (MAE) of 32.28 kWh/m2/yr with R-squared of 0.862. This is already surprisingly good -- it means 86% of the variation in BER scores is explained by a simple linear combination of building characteristics. The BER system itself is fundamentally a physics-based linear calculation (heat loss equals thermal transmittance times area times temperature difference), so a linear model captures most of the structure.

## What Improved It

We ran a model tournament (Ridge, ExtraTrees, XGBoost, LightGBM) and then a Hypothesis-Driven Research loop testing nine engineered features and two model configurations.

**Tournament results on 200,000-record subsample:**

| Model | MAE (kWh/m2/yr) | R-squared |
|-------|-----------------|-----------|
| Ridge linear | 32.28 | 0.862 |
| ExtraTrees | 20.51 | 0.934 |
| XGBoost | 19.26 | 0.943 |
| LightGBM | 19.54 | 0.943 |

Tree-based models reduce the error by 40% compared to the linear baseline. The nonlinear gain comes primarily from two sources: the heat pump discontinuity (efficiency jumps from 85% for a gas boiler to 350% for a heat pump) and the stepwise effect of building regulation eras.

**HDR loop: what worked and what did not.** We tested nine feature engineering ideas individually. Four were kept:

- **Space heating fraction** (heating as a share of total energy): the strongest single addition, reducing MAE from 19.54 to 18.47 -- a 5.5% improvement. Buildings where heating dominates total energy use are those with the worst fabric.
- **Primary energy factor** (fuel-specific conversion: electricity 2.08, gas 1.1): makes the fuel penalty explicit.
- **Compactness ratio** (envelope area divided by floor area): captures the apartment-versus-detached effect.
- **Ventilation heat loss proxy** (chimney count plus weighted flue count plus permeability): combines multiple infiltration indicators.

Five features were tested and reverted because they did not help: wall-era interaction, heating-fabric interaction, roof-to-floor ratio, log floor area, and total wall heat loss. These are cases where the tree model was already capturing the effect through splits.

**Final composition** (LightGBM with tuned hyperparameters plus all four kept features) on the full 1.33 million records: **MAE 18.05 kWh/m2/yr, R-squared 0.951**. That is a 44% reduction from the linear baseline.

## What Drives the BER Score

SHAP analysis (SHapley Additive exPlanations) decomposes each prediction into per-feature contributions. The top features by mean absolute SHAP value:

| Feature | Mean absolute SHAP (kWh/m2/yr) |
|---------|-------------------------------|
| Heat Loss Parameter (fabric quality) | 55.4 |
| Heating system efficiency | 23.7 |
| Primary energy factor (fuel type) | 14.5 |
| Window area | 9.9 |
| Window U-value | 9.4 |
| Number of chimneys | 8.4 |
| Space heating fraction | 7.7 |
| Year built | 7.0 |

The Heat Loss Parameter -- total fabric heat loss per square metre of floor area -- dominates with more than double the impact of any other feature. This is the standard physics metric for building fabric quality, and it confirms that DEAP primarily measures how well insulated the building envelope is.

Heating system efficiency is second, driven largely by the binary distinction between conventional boilers and heat pumps. A heat pump with a coefficient of performance of 3.5 delivers 3.5 units of heat for every unit of electricity, compared to 0.9 units of heat per unit of gas for a condensing boiler. The effect is further amplified by Ireland's high electricity primary energy factor (2.08), which penalises electric resistance heating but is more than offset by heat pump efficiency.

## Which Retrofits Look Best on Paper

We applied counterfactual perturbations to the average Irish dwelling (predicted BER 171 kWh/m2/yr, roughly C1 band) to estimate how much each single-measure retrofit would improve the DEAP score:

| Retrofit | Predicted saving (kWh/m2/yr) | Approximate cost (EUR) | Cost per kWh/m2/yr saved |
|----------|------------------------------|------------------------|--------------------------|
| Chimney sealing | 25.1 | 200 | 8 |
| LED lighting | 8.5 | 500 | 59 |
| Roof insulation | 5.4 | 2,500 | 463 |
| Boiler upgrade | 8.0 | 4,000 | 501 |
| Heat pump | 15.5 | 10,000 | 644 |
| Triple glazing | 4.7 | 12,000 | 2,569 |

**Chimney sealing is dramatically undervalued.** At 8 EUR per kWh/m2/yr saved, it is an order of magnitude more cost-effective than any other single measure. Open chimneys in older Irish homes provide uncontrolled ventilation that bypasses all insulation improvements. Fitting a draught excluder or sealing a disused chimney is cheap and immediately effective.

**Heat pumps provide the second-largest absolute saving** but are not always the most cost-effective first step. For homes with poor fabric (pre-1978 uninsulated), insulation should come first -- a heat pump works best when the heat it produces stays inside the building.

**Wall insulation shows near-zero marginal effect on the average dwelling.** This is because the average dwelling in the dataset already has reasonable walls (the post-2006 majority pulls the average down). For a pre-1978 house with uninsulated cavity walls, the saving would be much larger.

## Ireland's Housing Stock by the Numbers

**By construction era** (mean BER in kWh/m2/yr):

| Era | Mean BER | Certificates |
|-----|----------|-------------|
| Pre-1930 | 339 | 114,506 |
| 1930-1977 | 271 | 272,816 |
| 1978-2005 | 199 | 630,487 |
| 2006-2011 | 146 | 93,065 |
| 2012-2020 | 54 | 112,069 |
| 2021+ (nZEB) | 40 | 107,079 |

The step-function improvements align with building regulation milestones. The 1978 regulations first required insulation. The 2012 and 2019 nearly-zero energy building requirements brought mean ratings below 55. Heat pump adoption went from under 1% pre-2012 to over 80% in 2021+.

**By county** (worst to best mean BER): Leitrim (239), Roscommon (231), Tipperary (230), Mayo (229) at the top. Meath (160) and Kildare (160) at the bottom. The western rural counties have older housing stock; the Dublin commuter-belt counties have more recent suburban development.

## The Fundamental Caveat

Everything in this analysis describes what the DEAP model *calculates*, not what households actually consume. The performance gap is real and large. A-rated homes use roughly 30% more energy than DEAP predicts (rebound effect). G-rated homes use roughly 40% less (prebound effect). Any retrofit saving we estimate here should be discounted by 20-40% to reflect real-world conditions.

This matters enormously for policy. If Ireland targets 500,000 BER B2 retrofits by 2030, the actual energy and carbon savings will be substantially less than the BER improvement suggests. Policymakers should use DEAP ratings as a screening tool, not a savings calculator.

## Technical Details

- **Data**: 1,330,022 records from the SEAI BER Public Search dataset (CC BY 4.0)
- **Best model**: LightGBM (600 trees, learning rate 0.05, max depth 10, L2 regularisation)
- **Features**: 81 (77 baseline + 4 from HDR loop)
- **Cross-validation**: 5-fold, stratified random split
- **Final metrics**: MAE 18.05 kWh/m2/yr, RMSE 26.77, R-squared 0.951
- **HDR loop**: 11 hypotheses tested, 6 kept, 5 reverted
- **Improvement**: 44% MAE reduction from Ridge baseline to final composition

Note: these results describe DEAP-calculated energy performance, not measured consumption. The performance gap between calculated and actual energy use is well-documented in the literature and means real savings from any retrofit are 20-40% smaller than the model predicts.
