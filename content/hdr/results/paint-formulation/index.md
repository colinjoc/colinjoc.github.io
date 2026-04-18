---
title: "One model doesn't fit every paint property"
date: 2026-04-12
domain: "Coatings / Materials Science"
blurb: "Paint chemists want one machine-learning model that predicts every property at once. We checked whether that is actually the right approach."
weight: 33
tags: ["materials", "coatings", "small-data", "reproduction", "physics-informed"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/paint_formulation/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Gloss, hardness, hiding power and flexibility all respond to different physics. Matching a dedicated model to each property — and adding one carefully chosen physics-inspired feature per target — beats the published one-model-fits-all approach by between 13 and 28 percent on three of the four properties, with no expensive hyperparameter tuning.

## The Question

Developing a new industrial lacquer is slow and expensive. A formulation chemist adjusts four or more ingredients — crosslinker content, isocyanate type, matting agent, pigment loading — and every combination has to be tested for gloss, scratch resistance, hiding power, and flexibility. A single development cycle can chew through dozens of lab samples before landing on a satisfactory recipe.

In 2024, researchers at a German coatings institute published the first fully open dataset for this problem: 65 measured two-component polyurethane lacquer samples from six experimental campaigns, with all composition variables and four performance targets included. They trained a single statistical model on all four targets using 10,000 rounds of automated tuning and reported up to sixfold reductions in development time over conventional trial-and-error. We asked a simpler question. Does choosing the best model family and the most useful physics feature for each property independently beat the one-model-fits-all approach?

## What we found

It does. Matching each property to its own model and adding a single domain-specific feature per target cuts prediction error by 13 to 28 percent on three of the four properties.

- Scratch hardness is best predicted by a simple linear model with just one input: the binder-to-pigment ratio. Up to the critical pigment concentration, the relationship is nearly a straight line, and simplicity becomes an asset.
- Gloss needs a deeper, tree-based model, but only after adding the logarithm of film thickness and an interaction term between thickness and matting agent — which encode the known physics of surface roughness in drying coatings.
- Hiding power is best predicted by an ensemble model with a single engineered feature: the product of film thickness and pigment concentration, a direct translation of the century-old Kubelka-Munk light-scattering equation.
- Cupping depth — how much the coated metal can be stretched before it cracks — uses the same ensemble with an isocyanate-type interaction and a pigment volume proxy, capturing the combined stiffening effect of rigid chemistry and filler particles.
- Scratch hardness hits a hard ceiling at about one-fifth of its variance explained. No method does better. That is a data-scarcity limit, not a modelling failure.

![Per-target model selection beats the unified approach on three of four targets](plots/headline_finding.png)

## Why that matters

The published study invested 10,000 rounds of automated tuning into a single family of model. Our per-target approach uses essentially default settings for each model — the improvement comes entirely from two decisions: which kind of model to use, and which single physics-based feature to add. Domain knowledge encoded as a feature beat thousands of rounds of brute-force tuning.

The second surprise was what did not work. Log-ratio features, which textbook compositional-data theory says should help because the ingredients sum to a fixed total, failed on every target — the dataset's normalisation already removed the constraint those features are designed to fix. Hard monotonicity constraints (for example, forcing the model to learn that more matting agent always means less gloss) also hurt every target. At 65 samples, the real-world exceptions to these textbook rules are frequent enough that a hard constraint does worse than a learned pattern. And the popular gradient-boosting approach that dominates tabular machine learning competitions lost the initial family-of-model tournament on all four targets — it only recovered ground on gloss once physics features were added.

![Feature importance varies dramatically across the four paint properties](plots/feature_importance.png)

## What it means in practice

**For formulation chemists.** Do not force a single model to predict every property of a coating. Fit one model per target, and focus on the physics features every coating-science textbook already teaches: binder-to-pigment ratio for hardness, the thickness-times-pigment product for hiding power, the isocyanate-type interaction for flexibility. Using this approach, a discovery sweep identified a candidate predicted to hit 81 gloss units at about 106 grams per litre of volatile organic compound content — inside the low-emission regime defined by EU Directive 2004/42/EC for decorative coatings. The global low-VOC coatings market was worth 27.6 billion US dollars in 2024 and is projected to reach 40.1 billion by 2035, so small improvements in formulation efficiency compound commercially.

**For machine-learning researchers.** Cross-validation protocol matters enormously on small datasets. The published baseline used a single 55-versus-10 train-test split. Under five-fold cross-validation on the same data, the baseline looks meaningfully weaker, and a leave-one-campaign-out evaluation degrades performance by up to 14 percent further. Small-data coatings papers should report both random-split and structure-aware cross-validation to bound the optimism of their estimates.

![Predicted versus actual values for all four targets under 5-fold cross-validation](plots/pred_vs_actual_all.png)

## How we did it

We used the [published 65-sample two-component polyurethane lacquer dataset](https://doi.org/10.5281/zenodo.13742098) with four normalised composition variables, film thickness, and four performance targets. We reproduced the published baseline under five-fold cross-validation, ran a family-of-model tournament per target, then tested 22 physics-informed features derived from pigment volume concentration theory, Kubelka-Munk radiative transfer, and isocyanate chemistry. A discovery sweep screened 7,785 candidate formulations across five generation strategies, filtering to 4,765 after removing physically infeasible compositions.

## Further reading

- Borgert T et al. (2024). ["High-Throughput and Explainable Machine Learning for Lacquer Formulations"](https://www.sciencedirect.com/science/article/pii/S0300944025002140), *Progress in Organic Coatings* — the published baseline this study improves upon. Data at [Zenodo doi:10.5281/zenodo.13742098](https://doi.org/10.5281/zenodo.13742098).
- Wicks ZW et al. *Organic Coatings: Science and Technology* (Wiley, 2007) — the comprehensive coating-science textbook covering the physical mechanisms encoded in the kept features.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/paint_formulation/paper.md) — all experiments, ablations, and reproducible code.
