---
title: "Low-carbon concrete design, with the training data as the limit"
date: 2026-04-10
domain: "Materials Engineering"
blurb: "A machine-learning loop optimised a concrete recipe and found a mathematical optimum that uses almost no cement. Should we trust it?"
weight: 35
tags: ["materials", "sustainability", "concrete", "reproduction", "multi-objective"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/master/applications/concrete/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Replacing two thirds of the cement in structural concrete with industrial byproducts cuts embodied carbon by 42 to 53 percent at equivalent strength. The recipe itself is from the 1990s. The contribution here is refusing to report the model's mathematical optimum — because it sits below any cement level the training data has ever seen, and an extrapolation is not a finding.

## The question

Concrete is the most consumed material on Earth — about 30 billion tonnes per year. Cement, the ingredient that makes concrete harden, produces roughly 8 percent of all human-caused carbon dioxide emissions. In a standard structural mix, cement alone accounts for 94 percent of the embodied carbon.

The most established decarbonisation strategy is to replace some of that cement with industrial byproducts: blast-furnace slag from steel production and fly ash from coal combustion. Both react slowly with water to form the same binding compounds, at a fraction of the carbon cost. The trade-off is time — these mixes take 56 to 90 days to reach full strength instead of the standard 28.

We ran an automated experiment loop on the standard 1,030-sample UCI Concrete dataset to see if a transparent, reproducible methodology could arrive at the known answer — and be honest about where the training data runs out.

## What we found

![The strength-versus-carbon trade-off for all candidate mixes. The discovered mix sits at the Pareto front's knee: further carbon cuts buy diminishing strength.](plots/headline_finding.png)

Screening 3,685 candidate mixes through a tree-based model surfaced a design sitting at the knee of the strength-versus-carbon trade-off: 120 kilograms of cement, 300 kilograms of slag, and 150 kilograms of fly ash per cubic metre, cured for 90 days. Predicted strength is 58.8 megapascals, 18 percent above the 50 megapascal structural target. The model's typical prediction error on a held-out test set was 2.15 megapascals — tight enough to trust near the operating point.

The carbon reduction depends on how you count the slag. Under the standard economic allocation used in most life-cycle assessments, the discovered mix produces 157 kilograms of carbon dioxide per cubic metre, a 53 percent reduction compared to the conventional 335. Under mass allocation — a legitimate alternative — the slag carries higher attributed emissions and the reduction drops to 42 percent. At the most conservative figure in the literature, it falls to 33 percent. Because the discovery mix uses 300 kilograms of slag, far more than a conventional mix, this accounting choice matters more here than in most concrete studies.

![How the headline carbon reduction shifts as the slag emission factor changes across allocation methods](plots/emission_sensitivity.png)

## Why that matters

The recipe itself is not new. Bilodeau and Malhotra published the foundational study on high-volume fly ash concrete in 2000. A 2025 study using a completely different optimisation method reported an essentially identical result.

What this project demonstrates is the discipline. Every experiment is pre-registered with a stated prior expectation and a fixed keep-or-revert decision. The model's mathematical optimum — which would use even less cement — sits below the training data minimum of 102 kilograms per cubic metre. It is explicitly rejected as an extrapolation rather than reported as a finding. The local prediction error at the discovery's operating point is actually tighter than the model's global average, despite the sparse data in that region — a reassuring sign that the prediction is not being held up by a single outlier.

The practical barrier is not chemistry or cost. It is regulatory. Whether a building code accepts 90-day strength testing instead of the standard 28-day test. Many European codes and an increasing number of American codes already allow this.

![Component-level carbon breakdown showing cement as the dominant contributor in conventional concrete](plots/co2_comparison.png)

## What it means in practice

**For structural engineers.** The 42 to 53 percent reduction is achievable today with commercially available materials. The main scheduling question is whether the project can wait 56 to 90 days for strength certification instead of 28. If the answer is yes, there is no materials-science reason not to use this family of mixes.

**For anyone running ML optimisation on materials.** Report the in-distribution Pareto front. Filter candidates to the training range. The gap between "53 percent" and "75 percent" in this project was the gap between honesty and overreach, and most papers in this area do not filter.

## How we did it

We used the UCI Concrete Compressive Strength dataset — 1,030 real lab-tested samples, freely available. A model tournament picked a tree-based family. The winning model uses the eight raw mix components plus water-to-binder ratio and supplementary materials percentage, with one monotonicity constraint enforcing that more cement cannot decrease strength. A design sweep screened 3,685 candidate mixes across 11 generation strategies. Emission-factor sensitivity, local-density analysis, holdout evaluation, and bootstrap confidence intervals were run as additional validation. The entire pipeline runs in two minutes on a laptop. Full code, data reference, and experiment log are in the [project repository](https://github.com/colinjoc/hdr_autoresearch/tree/master/applications/concrete).

## Further reading

- Yeh IC. "Modeling of Strength of High-Performance Concrete Using Artificial Neural Networks." *Cement and Concrete Research* (1998). [doi:10.1016/S0008-8846(98)00165-3](https://doi.org/10.1016/S0008-8846(98)00165-3) — the source of the standard dataset.
- Bilodeau A, Malhotra VM. "High-Volume Fly Ash System." *ACI Materials Journal* (2000) — the foundational paper establishing the high-volume fly ash concrete category.
- DeRousseau MA, Kasprzyk JR, Srubar WV. "Computational design optimization of concrete mixtures: A review." *Cement and Concrete Research* (2018). [doi:10.1016/j.cemconres.2018.04.007](https://doi.org/10.1016/j.cemconres.2018.04.007) — survey of ML-guided concrete design.
- Hammond GP, Jones CI. *Inventory of Carbon and Energy (ICE) Database.* Version 3.0, University of Bath (2019) — the source of emission factors used in this study.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/master/applications/concrete/paper.md).
