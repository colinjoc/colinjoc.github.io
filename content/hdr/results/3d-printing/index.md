---
title: "Fifty Experiments, One Survivor: 3D Printing's Small-Data Wall"
date: 2026-04-11
domain: "Additive Manufacturing"
blurb: "Can machine learning improve 3D-printing strength predictions on just 50 samples? Barely -- only one experiment out of fifty helped. But the trained model discovered a print recipe that is 59 percent stronger and twice as fast as the slicer default."
weight: 12
tags: ["additive-manufacturing", "small-data", "physics-informed", "discovery"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/3d_printing/paper.md).*

## The Question

Fused deposition modelling -- the technology behind most consumer and prototype 3D printers -- melts a plastic filament and deposits it layer by layer. The strength of the finished part depends on about ten print settings: nozzle temperature, print speed, layer height, infill density, infill pattern, wall thickness, bed temperature, fan speed, and material choice. The relationships are governed by coupled polymer rheology, heat transfer, and bonding kinetics, and they have resisted closed-form solutions for three decades. Published machine-learning papers routinely report very high accuracy on the standard public benchmark, a 50-sample dataset from an Ultimaker S5 printer.

We wanted to know two things. First, do those published accuracy claims survive honest cross-validation? Second, if the signal is genuinely there, which print recipe maximises strength while minimising print time and energy?

## What We Found

The published high-accuracy claims do not hold up. Under rigorous five-fold cross-validation, a simple linear model performs only 32 percent worse than the best tree-based model. At 50 samples, the underlying signal is mostly linear, and published results claiming otherwise are likely overfitting.

- Of 50 single-change experiments -- physics-informed features, hyperparameter sweeps, target transforms, monotonicity constraints -- exactly one survived. The dataset does not support aggressive modelling.
- The one surviving experiment added five physics-informed features (linear energy density, volumetric flow rate, inter-layer cooling time, infill contact area, and thermal margin above the material's glass transition temperature) and improved prediction accuracy by 3.4 percent.
- A 2,394-candidate design sweep found a print recipe that dominates the standard slicer default on all three objectives simultaneously: 59 percent stronger, 54 percent faster, and 51 percent less energy.
- The discovered recipe uses high speed (more than double the default) combined with 70 percent honeycomb infill and three perimeter walls -- contrary to the conventional "slow down for strength" wisdom.
- Monotonicity constraints, which helped on a 1,030-sample dataset in a sister project, hurt here. At 50 samples, the expressiveness cost of the constraint exceeds its regularisation benefit.

![Only one of fifty experiments cleared the improvement threshold, and the discovered recipe dominates the slicer default on strength, speed, and energy](plots/headline_finding.png)

## Why That's Surprising

The 3D-printing machine-learning literature is full of papers reporting accuracy above 90 percent on this exact dataset. The gap between those claims and our result comes down to evaluation methodology. Most published studies use a single train-test split rather than cross-validation and report results without controlling for hyperparameter selection. On 50 samples, a single lucky split can look much better than the model actually is.

The discovered print recipe is also counterintuitive. Conventional wisdom says slower printing gives stronger parts because the polymer has more time to bond between layers. The model found the opposite: at the highest speed in the dataset (120 millimetres per second), the combination of high infill density and extra walls puts enough material in the load path to more than compensate, while cutting print time in half. The finding is a surrogate prediction, not a physical measurement, but every parameter value in the recipe appears in the training data -- no extrapolation is required.

## What It Means

For anyone running a 3D print farm: the slicer defaults are not optimised for strength. They are tuned for safety -- settings that work reliably across a wide range of geometries, not settings that maximise any particular property. The discovered recipe needs physical validation on an actual printer, but it sits inside the training distribution and is printable on any Ultimaker S5 without adjustment.

For the machine-learning community: do not trust high accuracy claims on tiny datasets without cross-validation. A 50-sample dataset does not support the nonlinear claims that dominate the published literature. The tree-to-linear performance gap of just 1.32 times means that a simple linear model gets most of the way there, and neural networks are unlikely to help.

## How We Did It

We used the [Kaggle 3D Printer Dataset](https://www.kaggle.com/datasets/afumetto/3dprinter) (50 samples of polylactic acid and acrylonitrile butadiene styrene specimens printed on an Ultimaker S5, tested under the ASTM D638 tensile standard). We ran a five-model tournament, 50 single-change experiments, a nine-experiment compositional retest, and a 2,394-candidate design sweep across seven generation strategies covering high-strength, high-throughput, material-specific, and random regimes. The dataset is real measured data with no synthetic generation. The full [HDR methodology](https://github.com/colinjoc/hdr_autoresearch) drove every experiment, with pre-registered priors and a fixed keep-or-revert threshold.

## Further Reading

- Sun Q, Rizvi GM, Bellehumeur CT, Gu P. "Effect of Processing Conditions on the Bonding Quality of FDM Polymer Filaments." *Rapid Prototyping Journal* (2008). [doi:10.1108/13552540810862028](https://doi.org/10.1108/13552540810862028) -- the foundational model of thermal-history bond formation that inspired the physics-informed features used here.
- Dey A, Yodo N. "Optimization of Fused Deposition Modeling Process Parameters: A Review." *Journal of Manufacturing and Materials Processing* (2019). [doi:10.3390/jmmp3030064](https://doi.org/10.3390/jmmp3030064) -- a systematic review of parameter optimisation techniques and open questions.
- Fumetto A. "3D Printer Dataset for Mechanical Engineers." [Kaggle](https://www.kaggle.com/datasets/afumetto/3dprinter) -- the 50-sample benchmark dataset used in this study.

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
