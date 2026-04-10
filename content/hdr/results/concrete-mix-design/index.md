---
title: "Half the Carbon, Same Strength: A Known Concrete Recipe, Honestly Reproduced"
date: 2026-04-09
weight: 15
blurb: "Can you halve the carbon footprint of structural concrete and keep the strength? Yes, but this is not news -- it has been known for decades. We reproduced it transparently to show our methodology works, not to claim a discovery."
domain: "Materials Engineering"
tags: ["materials", "sustainability", "concrete", "reproduction", "multi-objective"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/master/applications/concrete/paper.md).*

## The Question

Concrete is the most consumed material on Earth -- about 30 billion tonnes per year -- and cement production accounts for roughly 8 percent of global carbon dioxide emissions. Cement alone is responsible for 94 percent of concrete's carbon footprint. The most established approach to reducing it is to partially replace cement with industrial byproducts: blast-furnace slag from steel production and fly ash from coal combustion. Both react slowly with water to form the same binding compounds that cement produces, but with a fraction of the embodied carbon.

The question we investigated is not whether this approach works -- it has been documented since the 1990s and is codified in highway administration guidance. The question is whether our automated research methodology can reproduce the known result transparently, with explicit honesty about where the model's training data runs out.

## What We Found

The methodology reproduced the established result. A concrete mix with 120 kilograms of cement, 200 kilograms of slag, and 100 kilograms of fly ash per cubic metre, cured for 90 days instead of the standard 28, is predicted to reach structural-grade strength at 53 percent lower embodied carbon than a conventional mix -- and at roughly the same cost.

- The discovered mix reduces cement by two thirds compared to the standard 350-kilogram formulation, substituting slag and fly ash. The predicted strength exceeds the target by 18 percent.
- The standard default model settings were almost already optimal. Of 20 single-change experiments, only four improved the model: a water-to-binder ratio feature, a supplementary materials percentage feature, a constraint forcing the model to respect the physical rule that more cement means more strength, and an increase in training iterations.
- The textbook logarithmic age feature was rejected. The model can already handle the age-versus-strength relationship without an explicit transformation, and adding a redundant feature increased noise more than it reduced error.
- A previous version of this project reported a 75 percent carbon reduction. The current analysis rejects that claim because it required extrapolating below the training data's minimum cement content. The verified in-distribution result is 53 percent, not 75 percent.
- The practical barrier is not chemistry or cost but regulatory: whether your local building code accepts 56-day or 90-day strength specifications instead of the standard 28-day test.

![The strength-versus-carbon-dioxide trade-off for candidate mixes, with the conventional baseline and the discovered winner](plots/headline_finding.png)

## Why That's Surprising

It is not -- and that is the point. The recipe sits comfortably within the well-established category of high-volume fly ash concrete, formalised in the 1990s. An independent 2025 study using a completely different method reported an essentially identical result. The contribution here is not the chemistry but the methodology: a fully reproducible, pre-registered experiment loop where every hypothesis has a stated prior and every failed experiment is recorded alongside the successful ones. Most published studies in this area report only the winning configuration.

The rejection of the 75 percent claim is itself instructive. A model trained on data where the lowest cement content is 102 kilograms per cubic metre should not be trusted to predict what happens at 80 kilograms. The mathematically optimal mix sits outside the training range. Reporting it as a verified finding -- as many published papers in this area do -- is an extrapolation, not a prediction.

![The relationship between cement content and carbon dioxide, showing the in-distribution boundary](plots/co2_comparison.png)

## What It Means

For a structural engineer: the 53 percent carbon reduction is achievable with standard materials and standard methods. No exotic chemistry, no proprietary processes. The main decision is whether your project can accept 56-day or 90-day strength testing instead of the standard 28-day test. Many European codes and an increasing number of American codes already allow this.

For the machine-learning-for-concrete community: be honest about your training data boundaries. The UCI Concrete Compressive Strength dataset -- used in hundreds of published papers -- has a minimum cement content of 102 kilograms per cubic metre. Any mix design below that value is an extrapolation. Report it as such, or do not report it at all.

## How We Did It

We used the standard UCI Concrete Compressive Strength dataset (1,030 samples, freely available), ran a three-family model tournament, 20 single-change experiments, and an eight-experiment compositional retest. The winning model uses the eight raw mix components plus two derived features and one monotonicity constraint. A design sweep screened 3,685 candidate mixes across 11 generation strategies covering 28-day, 56-day, and 90-day curing. All candidates were filtered to the training data range before reporting. The entire pipeline runs in two minutes on a laptop. Full code, data reference, and experiment log are in the [project repository](https://github.com/colinjoc/hdr_autoresearch/tree/master/applications/concrete).

## Further Reading

- Yeh IC. "Modeling of Strength of High-Performance Concrete Using Artificial Neural Networks." *Cement and Concrete Research* (1998). [doi:10.1016/S0008-8846(98)00165-3](https://doi.org/10.1016/S0008-8846(98)00165-3) -- the source of the standard dataset.
- Bilodeau A, Malhotra VM. "High-Volume Fly Ash System." *ACI Materials Journal* (2000). -- the foundational paper establishing the high-volume fly ash concrete category.
- Federal Highway Administration. "Supplementary Cementitious Materials." [FHWA-HIF-16-001](https://www.fhwa.dot.gov/) (2016). -- the regulatory framework permitting high slag and fly ash replacement ratios.

---
📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)**
