---
title: "Low-carbon concrete, honestly reproduced"
date: 2026-04-12
domain: "Materials Engineering"
blurb: "Cement is eight percent of global emissions. A recipe that cuts most of it has been sitting in textbooks for twenty-five years. So why isn't it everywhere?"
weight: 35
tags: ["materials", "sustainability", "concrete", "reproduction", "multi-objective"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/concrete/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Replacing two thirds of the cement in structural concrete with industrial byproducts cuts embodied carbon by 42 to 53 percent at equal strength. This is not news — the recipe has been in textbooks for decades. What is new here is a transparent methodology that explicitly refuses to report its own extrapolations as findings, which is why our headline number is smaller than a previous iteration of the same project claimed.

## The question

Concrete is the most consumed material on Earth, at roughly 30 billion tonnes per year. Cement production alone is responsible for about 8 percent of global carbon dioxide emissions, and within a typical structural concrete mix, cement accounts for 94 percent of the embodied carbon. The oldest and most established way to bring that down is to replace some of the cement with industrial byproducts — blast-furnace slag from steelmaking and fly ash from coal combustion — which react slowly with water to form the same binding compounds, but at a fraction of the carbon cost.

The question is not whether this works. It has been documented since the 1990s, is codified in highway administration guidance, and appears in standard textbooks. The question is whether an automated, hypothesis-driven research loop can independently reproduce the known result — and be honest about where its predictions stop being trustworthy.

## What we found

A mix using 120 kilograms of cement, 300 kilograms of slag, and 150 kilograms of fly ash per cubic metre, cured for 90 days instead of the standard 28, exceeds structural-grade strength while cutting embodied carbon dioxide by 42 to 53 percent compared to a conventional mix.

- Cement is reduced by two thirds, from 350 down to 120 kilograms per cubic metre, and replaced by slag and fly ash. The predicted strength exceeds the structural target by 18 percent.
- Of 23 single-change experiments, four improved the model. The winners were a water-to-binder ratio feature, a supplementary materials percentage feature, a physical constraint forcing the model to respect that more cement means more strength, and additional training iterations.
- The carbon reduction depends on how you allocate the steel industry's emissions to its slag byproduct: 53 percent under economic allocation, 42 percent under mass allocation, and anywhere from 33 to 58 percent across the full range of published accounting methods.
- A previous version of this project claimed a 75 percent carbon reduction. That claim is rejected here because it required the model to predict below its training-data minimum of 102 kilograms of cement per cubic metre — an extrapolation, not a prediction.
- The main practical barrier is not chemistry or cost but regulatory: whether local building codes accept 56-day or 90-day strength specifications instead of the standard 28-day test.

## Why that matters

It is not, in itself, surprising — and that is the point. The recipe falls squarely within the well-established category of high-volume fly ash concrete, formalised in the literature over 25 years ago. An independent 2025 study using a completely different optimisation method reported an essentially identical result: 51 to 80 megapascals of strength at roughly 62 percent less cement than conventional mixes. A 2024 life-cycle assessment found a 54 percent carbon reduction with 65 percent fly ash replacement — the same ballpark as this work.

What is genuinely unusual is the self-correction. The automated loop initially produced a mathematically optimal mix that would have delivered a 75 percent carbon reduction. Rather than report it, the methodology flagged that this mix required cement levels below anything in the training data and rejected it. Most published papers in this area report mathematical optima without checking whether their model has ever seen similar data. This paper runs 3,685 candidate mixes through the model, then filters every result to the range the model was actually trained on before making any claims. The practical difference between "53 percent" and "75 percent" is the difference between a prediction the data supports and one it does not.

## What it means in practice

**For structural engineers.** The 42 to 53 percent carbon reduction is achievable with standard, commercially available materials. No exotic chemistry, no proprietary processes. Slag and fly ash are industrial byproducts already used at scale. The main decision is whether a project can wait 56 to 90 days for strength testing instead of the standard 28. Many European codes and an increasing number of North American codes already permit this.

**For researchers using machine learning on materials.** The standard benchmark dataset used across hundreds of published concrete-prediction papers has a minimum cement content of 102 kilograms per cubic metre. Any mix design below that is an extrapolation. Reporting extrapolations as verified findings — which is common — overstates what the model actually knows. Filter to the training range before claiming anything.

## How we did it

We used the [UCI Concrete Compressive Strength](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength) dataset — 1,030 real lab-tested samples, freely available from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/). A model tournament picked a tree-based family, and the winning model uses the eight raw mix components plus two derived features (water-to-binder ratio and supplementary materials percentage) and one monotonicity constraint. A design sweep then screened 3,685 candidate mixes across 11 generation strategies, and every candidate was filtered to the training data range before any results were reported. The pipeline was built with [scikit-learn](https://scikit-learn.org/) utilities and runs in about two minutes on a laptop.

## Further reading

- Yeh IC. "Modeling of Strength of High-Performance Concrete Using Artificial Neural Networks." *Cement and Concrete Research* (1998). [doi:10.1016/S0008-8846(98)00165-3](https://doi.org/10.1016/S0008-8846(98)00165-3) — the source of the standard dataset used in this work and hundreds of subsequent studies.
- Bilodeau A, Malhotra VM. "High-Volume Fly Ash System." *ACI Materials Journal* (2000) — the foundational paper establishing the high-volume fly ash concrete category that this work reproduces.
- Panesar DK, Seto KE, Churchill CJ. "Environmental Impact of Concrete Containing High Volume Fly Ash and GGBS." *Journal of Cleaner Production* (2024) — a life-cycle assessment reporting a 54 percent carbon reduction with 65 percent fly ash, consistent with our findings.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/concrete/paper.md).
