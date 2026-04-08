---
title: "Decomposing AI-Discovered Gravitational Wave Detector Topologies"
date: 2026-04-08
domain: "Gravitational Wave Physics"
headline: "A 120-parameter AI design reduces to 10 components. We explain why it works."
metric_name: "Improvement over LIGO Voyager"
metric_value: "3.62x (simplified design beats original)"
tags: ["physics", "interferometry", "AI-discovery", "ablation"]
---

## The Problem

The [Urania AI system](https://doi.org/10.1103/PhysRevX.15.021012) (Phys. Rev. X, 2025) discovered gravitational wave detector topologies that increase the observable Universe volume by up to **50-fold** over the planned LIGO Voyager upgrade. Fifty novel designs were compiled in a public ["Detector Zoo"](https://github.com/artificial-scientist-lab/GWDetectorZoo).

But the authors stated that **scientists don't understand why many of these designs work**.

## What We Found

Through 15 systematic ablation experiments using the [Differometor](https://github.com/artificial-scientist-lab/Differometor) differentiable simulator, we decomposed the best post-merger design (type8/sol00, 3.1x improvement over Voyager in the 800-3000 Hz band).

### The 120-parameter design is actually a 10-component interferometer

| Component Type | In Original | Essential | Redundant |
|---------------|-------------|-----------|-----------|
| Lasers | 3 | 1 | 2 |
| Squeezers | 4 | 0 | 4 |
| Arm cavities (4 km) | 13 | 2 | 11 |
| Beamsplitters | 13 | 1 | 12 |
| Filter cavities | 3 | 0 | 3 |

The simplified design retains **103% of the improvement** and with beamsplitter reoptimisation reaches **124%** (3.62x vs original 3.12x).

### Three mechanisms explain the improvement

| Mechanism | Contribution | What it does |
|-----------|-------------|-------------|
| **Critical cavity coupling** | 65% | Arm cavities at finesse ~6100 (vs Voyager's 3100) with precisely matched reflectivities |
| **Light test mass (7.3 kg)** | 35% | Creates optomechanical spring resonance in the 800-3000 Hz band |
| **Asymmetric beamsplitter (70:30)** | 10% | Balances signal pickup vs radiation pressure noise |

### Surprises

- **No squeezing needed.** All 4 squeezers have <0.5 dB — the quantum noise suppression comes from ponderomotive squeezing built into the cavity topology itself.
- **Multi-laser pumping is redundant.** Removing the second laser actually *improves* sensitivity by 3%.
- **Homodyne angle doesn't matter.** Only 1.4% sensitivity variation across 360° — no precision alignment needed.
- **Two distinct mechanism families** among the 25 type8 solutions: quantum noise suppression (dominant) and signal amplification (up to 13.7x signal gain).

### The Physical Picture

> The type8/sol00 design is an **asymmetric critically-coupled dual Fabry-Perot Michelson interferometer with one light test mass**. It extends the standard LIGO topology via (a) 2x higher arm finesse with impedance matching, (b) a 7.3 kg end mirror for optomechanical resonance, and (c) 70:30 beamsplitter splitting. No exotic features needed. The "complex" AI design is a natural extension of known physics, hidden beneath the UIFO grid parameterisation.

## Methodology

- **15 HDR experiments** over ~2 hours
- **110 literature citations** in Phase 0 review
- **28 hypotheses** tested across 6 priority tiers
- Simulation: Differometor (JAX, differentiable), ~1.1s per evaluation on GPU
- All code and data: [GWDetectorZoo](https://github.com/artificial-scientist-lab/GWDetectorZoo)

## Key References

1. Krenn, M., Drori, Y., and Adhikari, R.X. "Digital Discovery of Interferometric Gravitational Wave Detectors." *Phys. Rev. X* **15**, 021012 (2025).
2. Klimesch, J. et al. "Differometor: A Differentiable Interferometer Simulator." GitHub (2026).
3. Adhikari, R.X. et al. "A cryogenic silicon interferometer for gravitational-wave detection." *Class. Quantum Grav.* **37**, 165003 (2020).
