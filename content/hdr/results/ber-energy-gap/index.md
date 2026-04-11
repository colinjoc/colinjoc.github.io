---
title: "Ireland's Energy Ratings: The Formula Beats the ML Model"
date: 2026-04-11
domain: "Building Energy / Retrofit Policy"
blurb: "We trained a machine learning model on 1.33 million Irish building energy certificates and it could not beat the government formula it was approximating. But the exercise revealed that open chimneys may be the most cost-effective retrofit target in older homes -- a prediction that has never been tested in the field."
weight: 8
tags: ["building-energy", "BER", "retrofit", "DEAP", "Ireland", "SEAI", "heat-loss", "housing-policy", "real-data"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ber_energy_gap/paper.md).*

## The Question

Every home sold or rented in Ireland must have a Building Energy Rating (BER) certificate, graded from A1 (best) to G (worst). The rating is not measured from gas and electricity bills. It is calculated by a physics formula called DEAP (Dwelling Energy Assessment Procedure), which takes the building's dimensions, insulation values, heating system, and ventilation details and produces a number in kilowatt-hours per square metre per year.

Ireland has committed to retrofitting 500,000 homes to a B2 rating or better by 2030. The energy certificate is the yardstick. We used machine learning on the full national dataset -- 1.33 million real certificates covering roughly two-thirds of the housing stock -- to ask three questions: which building characteristics does the formula weigh most heavily, can a model approximate the rating from basic building features, and what happens when you perturb individual features one at a time?

## What We Found

A tree-based model trained on building characteristics achieved a mean error of 18 kilowatt-hours per square metre per year. But the government formula's own intermediate outputs, already included in the public dataset, reconstruct the rating with a mean error of just 7. The model is 2.6 times worse than the formula it approximates.

- The Heat Loss Parameter -- a composite measure of insulation quality relative to building size -- dominates the formula's output by more than two to one over any other feature.
- Open chimneys rank sixth overall in importance, but for the 42 percent of homes that have them, the model predicts sealing them would save an average of 21 kilowatt-hours per square metre per year at a cost of roughly 200 euros.
- Homes built before 1930 consume 8.5 times the calculated energy of homes built after 2021, driven by successive waves of building regulation. But the real consumption gap is only about 2 to 1, because occupants of inefficient homes under-heat and occupants of efficient homes increase their comfort.
- The model trained on pre-2020 data lost 52 percent of its accuracy when tested on post-2020 certificates, because the newer building stock is dominated by heat pumps and near-zero-energy designs the model had barely seen.
- Without any features derived from the formula's intermediate calculations, the honest model error is 19, not 18 -- most of the improvement from the research loop came from a single partially circular variable.

## Why That's Surprising

The central surprise is that the chimney finding emerged at all. Retrofit policy in Ireland focuses heavily on wall insulation, boiler upgrades, and heat pumps -- measures costing thousands of euros per home. Yet the model's sensitivity analysis puts open chimney ventilation among the highest-impact features for older homes, at a fraction of the cost. An open chimney is an uncontrolled ventilation path that bypasses every insulation improvement, and 42 percent of Irish homes have at least one.

This has not been validated by a field trial. Nobody has published before-and-after energy measurements for chimney sealing in Irish homes. The prediction is physically plausible and consistent with building science literature on infiltration losses, but it remains a model hypothesis, not a measured effect. That a 200-euro intervention could rival the calculated impact of measures costing ten to fifty times more is exactly the kind of finding that warrants real-world testing.

## What It Means

For homeowners with an open chimney or disused fireplace, the model says sealing it should be the single highest-impact low-cost measure available. The physics is plausible and the cost low enough that the risk is minimal, even before field trials confirm the magnitude.

For policymakers, two messages emerge. First, the building energy certificate is useful as a screening tool for identifying which homes need work, but it should not be treated as an energy savings calculator -- the well-documented performance gap means actual savings from any intervention are 20 to 40 percent smaller than the certificate predicts. Second, retrofit targeting should focus on construction era rather than geography: a pre-1978 house in Dublin has similar characteristics to a pre-1978 house in Mayo, and the county-level variation in ratings is almost entirely explained by the age of the housing stock.

## How We Did It

We used the complete [Sustainable Energy Authority of Ireland (SEAI) public dataset](https://ndber.seai.ie/BERResearchTool/ber/search.aspx) of 1.33 million certificates, released under a Creative Commons licence. A four-family model tournament selected a tree-based gradient boosting model. An 11-experiment [HDR methodology](https://github.com/colinjoc/hdr_autoresearch) loop tested nine engineered features and two model configurations, keeping four features and reverting five. Per-dwelling counterfactual perturbations replaced the original mean-dwelling approach after review revealed that the average dwelling has 0.52 chimneys, making subtraction of one chimney physically impossible and forcing the model to extrapolate wildly.

## Further Reading

- Moran P et al. "Measured vs Calculated Energy Performance in Irish Residential Buildings." *Energy and Buildings* (2020). [doi:10.1016/j.enbuild.2020.110345](https://doi.org/10.1016/j.enbuild.2020.110345) -- the Irish study quantifying the 2:1 actual energy gap versus the 8.5:1 calculated gap.
- Sunikka-Blank M & Galvin R. "Introducing the Prebound Effect." *Building Research & Information* (2012). [doi:10.1080/09613218.2012.690952](https://doi.org/10.1080/09613218.2012.690952) -- the landmark paper defining the gap between predicted and actual energy use.
- Full technical paper: [paper.md](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ber_energy_gap/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
