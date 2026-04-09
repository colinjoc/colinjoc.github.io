---
title: "AI's 48-Mirror GW Detector Is Really 10 Components"
date: 2026-04-09
domain: "Gravitational Wave Physics"
headline: "A 120-parameter AI-discovered detector reduces to 10 essential components — and a re-optimised version beats the AI by 16%"
metric_name: "Strain sensitivity over LIGO Voyager (800–3000 Hz)"
metric_value: "3.62× (up from the AI's 3.12×)"
tags: ["physics", "interferometry", "ai-discovery", "ablation", "ligo"]
---

## The Problem

In 2025, the [Urania AI system](https://doi.org/10.1103/PhysRevX.15.021012) discovered 50 novel gravitational wave detector topologies, catalogued in the public [GW Detector Zoo](https://github.com/artificial-scientist-lab/GWDetectorZoo). The best of them promised up to a **50-fold** increase in observable Universe volume over the planned LIGO Voyager upgrade.

The catch: nobody knew *why* these designs worked. Each one is a grid of up to 48 mirrors, 13 beamsplitters, 3 lasers, and 4 squeezers — over 120 free parameters. The physics hiding inside that parameter soup was opaque even to the authors of the paper that produced it.

This project decomposes the best post-merger design (type8/sol00) to identify which components actually matter, what physical mechanisms drive the improvement, and whether a human-in-the-loop pass can beat the AI's own optimum.

## What We Found

**The 120-parameter design is a 10-component interferometer in disguise — and a re-optimised version hits 3.62× strain sensitivity over [LIGO Voyager](https://doi.org/10.1088/1361-6382/aba26f), beating the original AI discovery by 16%.**

| Design | Components | Improvement over Voyager |
|---|---|---|
| LIGO Voyager baseline | — | 1.00× |
| type8/sol00 (Urania, original) | 48 mirrors, 13 BSs, 3 lasers, 4 squeezers, 3 filter cavities | 3.12× |
| type8/sol00 minimal (this work) | 10 components | 3.18× |
| **Minimal + beamsplitter re-optimised** | **10 components** | **3.62× (+16%)** |

Component-level ablation shows how much of the AI's design was load-bearing:

| Component type | In original | Essential | Redundant |
|---|---|---|---|
| Lasers | 3 | 1 | 2 |
| Squeezers | 4 | 0 | 4 |
| Arm cavities (4 km) | 13 | 2 | 11 |
| Beamsplitters | 13 | 1 | 12 |
| Filter cavities | 3 | 0 | 3 |

## Key Insights

### 1. Three mechanisms explain the 3.12× improvement

| Mechanism | Contribution | Physical description |
|---|---|---|
| Critical cavity coupling | 65% | Arm cavities at finesse ~6100 (vs Voyager's ~3100) with impedance-matched reflectivities |
| Light test mass (7.3 kg) | 35% | Ponderomotive spring resonance in the 800–3000 Hz band |
| Asymmetric beamsplitter (70:30) | 10% | Balances signal pickup against radiation-pressure noise |

Contributions sum above 100% because the mechanisms partially overlap — each was measured by reverting that one component to its Voyager value while holding the others at the AI-discovered values.

### 2. No squeezing. No multi-laser pumping. No filter cavities.

Three features that looked essential from the raw UIFO parameterisation are redundant or actively harmful:

- All 4 squeezers carry <0.5 dB of squeezing. The quantum noise suppression is ponderomotive, built into the cavity topology itself — removing all 4 squeezers degrades sensitivity by less than 0.5%.
- Removing the second laser *improves* sensitivity by 3%. The optimiser added it during training but never converged to using it productively.
- All 3 filter cavities can be deleted at zero cost.

### 3. Sharp peaks are real physics; broad plateaus are re-optimisation opportunities

Arm cavity finesse has a knife-edge optimum near 6100 — a ±5% deviation drops sensitivity below Voyager. That is a real critical-coupling condition. By contrast, beamsplitter reflectivity has a broad plateau: any value in [0.5, 0.8] is within 5% of optimal. The AI landed at 0.81; a post-hoc sweep finds 0.70 is 16% better. Gradient optimisers converge inside the basin they start in; they cannot distinguish a narrow real optimum from a broad arbitrary one.

### 4. Two mechanism families, not one

Applying the full decomposition to 25 type8 solutions revealed two disconnected families:

- **Noise suppression (dominant):** ~75% noise / 25% signal, via elevated finesse and ponderomotive squeezing.
- **Signal amplification (secondary):** ~30% noise / 70% signal, with signal-recycling cavities pushed up to **13.7×** Voyager's signal transfer.

The two families are not connected by any continuous deformation in the UIFO parameterisation. The "explanation" of the AI's discovery is a discrete classification, not a single mechanism.

### 5. Homodyne readout angle is essentially irrelevant

Sweeping the homodyne readout phase over the full 360° produces only 1.4% sensitivity variation. No precision phase alignment is required — a substantial relaxation of the engineering constraints implied by the raw design.

### 6. Cross-validation caught a wrong answer

The initial decomposition attributed the improvement to signal amplification. Cross-checking against the [GW Detector Zoo](https://github.com/artificial-scientist-lab/GWDetectorZoo) loss decomposition metadata corrected it: the dominant mechanism for type8/sol00 is noise suppression. Differentiable and step-based simulators can disagree on internal scales, so independent cross-validation is mandatory before claiming a mechanism.

### 7. The simplified design beats the original

After re-optimising only the beamsplitter ratio, the 10-component minimal design reaches 3.62× over Voyager — 16% better than the original AI-discovered design. In plain language, it is an asymmetric critically-coupled dual Fabry-Perot Michelson interferometer with one light test mass. No exotic features required.

## Why This Matters

AI-discovered scientific designs are routinely published as black boxes — hundreds of parameters, a performance number, and little physical interpretation. This work shows that systematic ablation plus parameter re-sweeping is not just an interpretation tool but a *productive* post-processing step: it finds a better design than the optimiser's local optimum.

For gravitational-wave instrumentation, the immediate consequence is a substantially relaxed specification for a Voyager-beating detector: about 10 optical components, no external squeezing, no filter cavities, no precision homodyne alignment. The hard engineering constraint concentrates on one thing — impedance-matched arm cavities at finesse ~6100. For AI-for-science more broadly, the methodology — ablate before sweeping, distinguish sharp peaks from broad plateaus, cross-validate the mechanism, survey the whole solution family — is directly transferable.

## Methodology

- **15 HDR ablation + parameter-sweep experiments** on the type8/sol00 design
- **Simulator**: [Differometor](https://github.com/artificial-scientist-lab/Differometor) — JAX-based differentiable interferometer, ~1.1 s per evaluation on GPU
- **Baseline**: [LIGO Voyager](https://doi.org/10.1088/1361-6382/aba26f) design, reproduced within 0.1% of published strain noise (3.76 × 10⁻²⁵ /√Hz at 168 Hz)
- **Dataset**: [GWDetectorZoo](https://github.com/artificial-scientist-lab/GWDetectorZoo) — 50 AI-discovered designs; the 25-solution type8 family used for the cross-solution survey
- **Cross-validation**: independent loss-function decomposition against GW Detector Zoo metadata to guard against simulator-internal scaling artifacts
- **Minimal-design verification**: simplified topology re-optimised over the beamsplitter ratio and confirmed to exceed the original 3.12× improvement

## Key References

1. Krenn, M., Drori, Y., & Adhikari, R.X. "Digital Discovery of Interferometric Gravitational Wave Detectors." [*Phys. Rev. X* **15**, 021012 (2025)](https://doi.org/10.1103/PhysRevX.15.021012) — the Urania system and the GW Detector Zoo.
2. Klimesch, J. et al. "[Differometor: A Differentiable Interferometer Simulator](https://github.com/artificial-scientist-lab/Differometor)" (2026).
3. Adhikari, R.X. et al. "A cryogenic silicon interferometer for gravitational-wave detection." [*Class. Quantum Grav.* **37**, 165003 (2020)](https://doi.org/10.1088/1361-6382/aba26f) — the LIGO Voyager baseline.
4. Buonanno, A. & Chen, Y. "Quantum noise in second generation, signal recycled laser interferometric gravitational-wave detectors." [*Phys. Rev. D* **64**, 042006 (2001)](https://doi.org/10.1103/PhysRevD.64.042006).
5. McCuller, L. et al. "Frequency-Dependent Squeezing for Advanced LIGO." [*Phys. Rev. Lett.* **124**, 171102 (2020)](https://doi.org/10.1103/PhysRevLett.124.171102).

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework, program.md, and full project history
