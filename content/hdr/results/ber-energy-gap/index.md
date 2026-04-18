---
title: "What Ireland's 1.3 million energy certificates reveal about retrofits"
date: 2026-04-11
domain: "Building Energy / Retrofit Policy"
blurb: "Ireland has committed to retrofitting half a million homes by 2030. The national energy certificate dataset quietly suggests the cheapest upgrade is one nobody is talking about."
weight: 28
tags: ["building-energy", "BER", "retrofit", "DEAP", "Ireland", "SEAI", "heat-loss", "housing-policy", "real-data"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ber_energy_gap/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** On Ireland's full national dataset of 1.33 million building energy certificates, the single most cost-effective retrofit the data points at is sealing open chimneys — a 200-euro intervention that the model predicts would save as much energy per square metre as wall insulations costing ten to fifty times more. It has never been tested in a controlled field trial. It should be.

## The question

Every home sold or rented in Ireland comes with a Building Energy Rating certificate, graded from A1 (best) to G (worst). The rating is not measured from your gas and electricity bills. It is calculated by a physics formula called DEAP — Dwelling Energy Assessment Procedure — that takes a building's dimensions, insulation, heating system, and ventilation details and spits out a number in kilowatt-hours per square metre per year.

Ireland has promised to retrofit 500,000 homes to a B2 rating or better by 2030. The certificate is the yardstick the whole policy is being judged against. We ran machine learning on the full national dataset — 1.33 million real certificates covering roughly two thirds of the country's housing stock — to ask three questions. Which building features does the formula actually weigh most heavily? Can a model approximate the rating from basic inputs? And what happens when you perturb features one at a time to see what matters most?

## What we found

The model hit a ceiling. Using building characteristics, it predicted the official rating with a typical error of 18 kilowatt-hours per square metre per year. The formula's own intermediate outputs, which are also in the public dataset, reconstruct the rating with a typical error of just 7. The machine-learning model is more than twice as far off as the formula it is approximating — a reminder that when a deterministic calculator already exists, a model trained on its outputs cannot beat it.

But the sensitivity analysis surfaced something policy-relevant.

- One composite measure — the Heat Loss Parameter, which captures how leaky a building is relative to its size — dominates the rating by more than two to one over any other feature.
- Open chimneys rank sixth overall. For the 42 percent of Irish homes that have at least one, the model predicts sealing them would save 21 kilowatt-hours per square metre per year, for roughly 200 euros of materials and labour.
- Homes built before 1930 use 8.5 times the calculated energy of homes built after 2021 — a direct reflection of successive waves of building regulation. The real-world gap is closer to two to one, because people in old, leaky houses under-heat and people in new, efficient houses crank up the comfort.
- A model trained on certificates from before 2020 lost more than half its accuracy on post-2020 certificates. The newer stock is dominated by heat pumps and near-zero-energy designs the training data had barely seen.
- Without features derived from the formula's own intermediate calculations, the honest model error is 19 rather than 18 — most of the apparent improvement from the research loop came from a single partially circular variable.

## Why that matters

Irish retrofit policy is focused on wall insulation, boiler upgrades, and heat pumps — interventions that cost several thousand euros per home. The sensitivity analysis points somewhere much cheaper. An open chimney is an uncontrolled ventilation path that bypasses every insulation improvement you could make; air leaves the house regardless of how well the walls are insulated. Two in five Irish homes have one, and sealing them costs on the order of a takeaway weekend.

Nobody has published before-and-after energy measurements for chimney sealing in Irish homes. The prediction is physically plausible and consistent with building-science literature on infiltration losses, but it is still a model prediction. That a 200-euro intervention could rival upgrades costing ten to fifty times more is exactly the kind of finding a field trial should settle.

## What it means in practice

**For homeowners with a disused fireplace.** The model says this should be the single highest-impact low-cost measure available to you. The physics is plausible and the cost low enough that the risk is minimal even before anyone confirms the magnitude in a trial.

**For policymakers.** The building energy certificate is a useful screening tool for identifying homes that need work. It should not be used as an energy-savings calculator. The well-documented performance gap means actual savings are typically 20 to 40 percent smaller than the certificate predicts. Retrofit targeting should use construction era rather than geography — a pre-1978 house in Dublin has the same profile as a pre-1978 house in Mayo, and county-level variation is almost entirely an age-of-stock artefact.

**For the Sustainable Energy Authority of Ireland.** A field trial of chimney sealing across a few hundred homes would cost very little and could either redirect a meaningful slice of retrofit funding or close the question.

## How we did it

We used the complete [Sustainable Energy Authority of Ireland public dataset](https://ndber.seai.ie/BERResearchTool/ber/search.aspx) of 1.33 million certificates, released under a Creative Commons licence. A model tournament selected a tree-based approach. Per-dwelling counterfactual perturbations — sealing one chimney, adding insulation, upgrading a boiler — replaced an earlier mean-dwelling approach after review revealed that the average dwelling has 0.52 chimneys, which makes subtracting one physically impossible and forces the model to extrapolate.

## Further reading

- Moran P et al. "Measured vs Calculated Energy Performance in Irish Residential Buildings." *Energy and Buildings* (2020). [doi:10.1016/j.enbuild.2020.110345](https://doi.org/10.1016/j.enbuild.2020.110345) — the Irish study quantifying the two-to-one measured gap versus the 8.5-to-one calculated gap.
- Sunikka-Blank M & Galvin R. "Introducing the Prebound Effect." *Building Research & Information* (2012). [doi:10.1080/09613218.2012.690952](https://doi.org/10.1080/09613218.2012.690952) — the landmark paper defining the gap between predicted and actual energy use.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ber_energy_gap/paper.md).
