---
title: "Different Paint Properties Need Different Models"
date: 2026-04-12
domain: "Coatings / Materials Science"
blurb: "A published study used one model for all four paint quality targets. We found that picking the right model for each property and adding a single physics-informed feature per target beats the published baseline on three of four targets by 13 to 28 percent -- and that some textbook-approved features actually hurt."
weight: 33
tags: ["materials", "coatings", "small-data", "reproduction", "physics-informed"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/paint_formulation/paper.md).*

## The Question

Developing a new industrial lacquer is slow and expensive. A formulation chemist adjusts four or more ingredients -- crosslinker content, isocyanate type, matting agent, pigment loading -- and each combination must be tested for gloss, scratch resistance, hiding power, and flexibility. A single development cycle can consume dozens of lab samples before landing on a satisfactory recipe.

In 2024, researchers at a German coatings institute published the first fully open dataset for this problem: 65 measured two-component polyurethane lacquer samples from six experimental campaigns, with all composition variables and four performance targets included. They trained a single statistical model on all four targets using 10,000 rounds of automated hyperparameter tuning and reported up to sixfold reductions in development time compared to conventional trial-and-error. We asked a simpler question: does choosing the best model family and the most useful physics feature for each property independently beat the one-model-fits-all approach?

## What We Found

It does. Matching each property to its own model and adding a single domain-specific feature per target cuts prediction error by 13 to 28 percent on three of the four properties.

- **Scratch hardness** responds best to a simple linear model using just the binder-to-pigment ratio -- the relationship is approximately straight-line up to the critical pigment concentration, making simplicity an asset.
- **Gloss** needs a deeper tree-based model, but only after adding the logarithm of film thickness and a thickness-times-matting-agent interaction term that encodes the known physics of surface roughness in drying coatings.
- **Hiding power** is best predicted by a randomised ensemble with a single feature: the product of film thickness and pigment concentration -- a direct translation of the century-old Kubelka-Munk light-scattering equation.
- **Cupping depth** (flexibility before cracking) uses the same ensemble approach with an isocyanate-type interaction and a pigment volume proxy, capturing the combined stiffening effect of rigid chemistry and filler particles.
- **Scratch hardness resists prediction by every method**, topping out at just 22 percent of variance explained -- a genuine data-scarcity ceiling, not a modelling failure.

![Per-target model selection beats the unified approach on three of four targets](plots/headline_finding.png)

## Why That's Surprising

The published study invested 10,000 rounds of automated hyperparameter tuning into a single model family. Our per-target approach uses essentially default settings for each model, with the improvement coming entirely from two decisions: which model family to use, and which single physics feature to add. Domain physics encoded as a feature outperformed thousands of rounds of brute-force tuning.

A second surprise was what did not work. Compositional log-ratio features -- which textbook theory says should help because the ingredients sum to a fixed total -- failed on every target. The published dataset's normalisation already removes the constraint they exist to fix. Monotonicity constraints (forcing physically correct relationships like "more matting agent means less gloss") also hurt every target. At 65 samples, the real-world exceptions to these textbook rules are frequent enough that a hard constraint does worse than a learned pattern. Meanwhile, the popular gradient-boosting approach that dominates tabular machine learning competitions lost the initial tournament on all four targets -- it only recovered for gloss after physics features were added.

![Feature importance varies dramatically across the four paint properties](plots/feature_importance.png)

## What It Means

For coating formulation chemists: when optimising a multi-target coating, fit one model per property rather than forcing a single model to do everything. The critical features are well-known coating science -- binder-to-pigment ratio for hardness, the thickness-times-pigment product for hiding power, and the isocyanate-type interaction for flexibility. Using this approach, a discovery sweep identified a predicted candidate achieving 81 gloss units at an estimated volatile organic compound (VOC) content of 106 grams per litre -- inside the low-emission regime defined by EU Directive 2004/42/EC for decorative coatings. The global low-VOC paints and coatings market was valued at 27.6 billion US dollars in 2024 and is projected to reach 40.1 billion by 2035, so even incremental improvements in formulation efficiency have significant commercial value.

For the machine learning community: cross-validation protocol matters enormously on small datasets. The published study used a single 55-versus-10 train-test split. Under five-fold cross-validation on the same data, the baseline looks meaningfully weaker, and a leave-one-campaign-out evaluation further degrades performance by up to 14 percent. Small-dataset papers should report both random-split and structure-aware cross-validation to bound the optimism of their estimates.

![Predicted versus actual values for all four targets under 5-fold cross-validation](plots/pred_vs_actual_all.png)

## How We Did It

We used the published [65-sample two-component polyurethane lacquer dataset](https://doi.org/10.5281/zenodo.13742098) with four normalised composition variables, film thickness, and four performance targets. We reproduced the published baseline under five-fold cross-validation, ran a four-family model tournament per target, then 204 single-change experiments testing 22 physics-informed features derived from pigment volume concentration theory, Kubelka-Munk radiative transfer, and isocyanate chemistry. Eleven experiments were kept across the four targets (5.5 percent keep rate). A discovery sweep screened 7,785 candidate formulations across five generation strategies, filtering to 4,765 after removing physically infeasible compositions. The key findings came from Phase 1 (model family tournament) and Phase 2 (single-change feature experiments).

## Further Reading

- Borgert T et al. "High-Throughput and Explainable Machine Learning for Lacquer Formulations." [*Progress in Organic Coatings* (2024)](https://www.sciencedirect.com/science/article/pii/S0300944025002140) -- the published baseline this study improves upon. Data at [Zenodo doi:10.5281/zenodo.13742098](https://doi.org/10.5281/zenodo.13742098).
- Wicks ZW et al. *Organic Coatings: Science and Technology* (Wiley, 2007) -- the comprehensive coating-science textbook covering the physical mechanisms encoded in the kept features.
- Full technical write-up: [paper.md](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/paint_formulation/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
