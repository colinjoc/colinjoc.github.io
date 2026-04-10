---
title: "Ireland's Cheapest Home Retrofit Is the One Nobody Talks About"
date: 2026-04-09
weight: 8
blurb: "Ireland plans to retrofit half a million homes by 2030. We analysed 1.33 million real energy certificates and found that the most cost-effective single measure is not insulation, not a heat pump, and not new windows. It is sealing the chimney."
domain: "Building Energy / Retrofit Policy"
tags: ["building-energy", "BER", "retrofit", "energy-performance-gap", "Ireland", "SEAI", "heat-loss", "housing-policy", "real-data"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/master/applications/ber_energy_gap/paper.md).*

## The Question

Every home sold or rented in Ireland must have a Building Energy Rating certificate, graded from A1 (best) to G (worst). An A-rated home is supposed to use eight times less energy than a G-rated one. But when researchers compared these certificates against actual gas and electricity bills, the real ratio was closer to two to one. People in draughty old houses wear jumpers and heat one room; people in well-insulated new builds crank up the thermostat because it is cheap. The academic literature calls this the "prebound and rebound effect," and it means the rating system overstates the gap between best and worst homes by about fourfold.

Ireland has committed to retrofitting 500,000 homes to a B2 rating or better by 2030. The energy certificate is the yardstick for that target. We asked: what building characteristics actually drive the score, and which retrofits look best on paper -- even knowing that the real savings will be smaller?

## What We Found

We analysed the full national dataset -- 1.33 million real energy certificates covering roughly two thirds of Ireland's housing stock. The model predicts the energy rating with 95 percent accuracy, and the most important finding is about what drives that score.

- The single most important factor is the overall quality of the building's thermal envelope -- how well insulated the walls, roof, floor, and windows are relative to the building's size. This one measure has more than double the influence of any other feature.
- Heating system type is second. The jump from a conventional boiler to a heat pump changes the predicted rating more than any other single component swap.
- Open chimneys are dramatically undervalued as a retrofit target. Sealing an open chimney is the most cost-effective single measure at roughly 8 euros per unit of rating improvement -- an order of magnitude cheaper than any other intervention.
- Wall insulation shows near-zero marginal benefit for the average Irish dwelling, because the majority of homes in the dataset already have reasonable walls. For a pre-1978 home with uninsulated walls, the story is very different.
- Heat pumps provide the second-largest absolute improvement, but they work best in homes that are already well insulated. The correct sequence is fabric first, then heat pump.

![The distribution of energy ratings by band shows substantial overlap between adjacent categories](plots/headline_finding.png)

## Why That's Surprising

Irish retrofit policy and public discussion focus overwhelmingly on wall insulation and heat pumps. Chimney sealing barely appears in the guidance. Yet open chimneys in older Irish homes create uncontrolled ventilation paths that bypass every insulation improvement you make. You can insulate the walls, upgrade the roof, and install triple glazing -- and the warm air still pours out through the open fireplace. A draught excluder or a chimney seal costs about 200 euros and is immediately effective.

The other surprise is the sheer size of the energy performance gap. The certificate system predicts an 8.5-to-1 ratio between the worst and best homes. In reality it is about 2-to-1. This means every retrofit saving estimated from the certificates should be discounted by 20 to 40 percent to reflect what actually happens in practice. Ireland's 2030 retrofit target will deliver less energy saving than the headline numbers suggest.

![The heat loss parameter dominates all other predictors by more than two to one](plots/feature_importance.png)

## What It Means

For a homeowner deciding what to do first: if your house has an open chimney or disused fireplace, seal it before doing anything else. It is the single highest-return investment in the dataset. After that, the correct sequence depends on your starting point. For a pre-1978 house with poor insulation, address the building fabric before installing a heat pump. For a post-2006 house with good walls but a conventional boiler, a heat pump alone provides a large improvement.

For policymakers, the finding about the energy performance gap matters most. If Ireland targets 500,000 retrofits by 2030, the actual energy and carbon savings will be substantially less than the certificate improvements suggest. The certificates are useful as a screening tool for identifying which homes need work, but they should not be used as a savings calculator.

## How We Did It

We used the complete Sustainable Energy Authority of Ireland public dataset of 1.33 million Building Energy Rating certificates, released under a Creative Commons licence. Each certificate contains 211 fields describing the building envelope, heating system, ventilation, and lighting. We ran a four-family model tournament and an 11-experiment single-change loop, producing a gradient-boosting model with four physics-informed features. Counterfactual retrofit analysis was performed by perturbing individual features for the average dwelling and re-predicting. All results describe what the national calculation method predicts, not what households actually consume. Full details and code are in the [project repository](https://github.com/colinjoc/hdr_autoresearch/tree/master/applications/ber_energy_gap).

## Further Reading

- Moran P et al. "Measured vs Calculated Energy Performance in Irish Residential Buildings." *Energy and Buildings* (2020). [doi:10.1016/j.enbuild.2020.110206](https://doi.org/10.1016/j.enbuild.2020.110206) -- the Irish study quantifying the 2:1 actual energy gap versus the 8:1 calculated gap.
- Sunikka-Blank M, Galvin R. "Introducing the Prebound Effect." *Building Research and Information* (2012). [doi:10.1080/09613218.2012.690952](https://doi.org/10.1080/09613218.2012.690952) -- the landmark paper defining the gap between predicted and actual energy use.
- SEAI. "National BER Research Tool." [seai.ie](https://www.seai.ie/) -- the public dataset used in this analysis.

---
📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)**
