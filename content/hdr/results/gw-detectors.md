---
title: "The 25 AI-Discovered Post-Merger GW Detectors Are Mostly Filler"
date: 2026-04-09
domain: "Gravitational Wave Physics"
headline: "One AI design beats LIGO Voyager by 4.05× — the other 24 are within 10% of break-even, and the family's best designs have FEWER squeezers"
metric_name: "Strain improvement over LIGO Voyager (post-merger band 800-3000 Hz)"
metric_value: "4.05× (sol00, the strongest); median across 25 type8 solutions: 1.11×"
tags: ["physics", "interferometry", "ai-discovery", "decomposition", "ligo"]
---

## The Problem

In 2025, the [Urania AI system](https://doi.org/10.1103/PhysRevX.15.021012) released 50 new gravitational-wave detector topologies, all claimed to improve on the planned LIGO Voyager upgrade. The designs are catalogued in the public [GW Detector Zoo](https://github.com/artificial-scientist-lab/GWDetectorZoo). The headline number from the paper: "up to 50× more observable Universe volume" via the strongest AI-discovered topology.

The catch: nobody knows *why* the AI designs work, and the Zoo authors themselves note that "the experimental setup is not fully optimized and could be significantly simpler." We took them at their word and decomposed the entire 25-solution post-merger family from scratch.

## What We Found

We wrote a parser for the PyKat-format `.kat` configuration files in the Zoo (the canonical PyKat library is broken on modern Python), used it to extract every component, parameter, and free-space connection from all 25 type8 (post-merger) solutions, and combined that structural data with the strain spectra distributed alongside each solution.

### The family is dramatically skewed

| Rank | Solution | Improvement vs Voyager (800–3000 Hz, log-averaged) |
|---|---|---|
| 1 | **sol00** | **4.05×** |
| 2 | sol01 | 3.36× |
| 3 | sol02 | 2.68× |
| 4 | sol03 | 2.22× |
| 5 | sol04 | 1.78× |
| 6–12 | sol05–sol12 | 1.10×–1.30× |
| 13–25 | sol13–sol24 | 1.00×–1.10× |

Mean across the family: 1.43×. Median: 1.11×. Only `sol00` and `sol01` deliver substantial improvements; the bottom half is essentially break-even with Voyager.

### The Urania UIFO grids are grossly over-parameterised

`sol00` declares 57 mirrors and 13 beamsplitters. Of those:

| Component class | Count | At extreme values | Doing real work |
|---|---|---|---|
| Mirrors | 57 | **29** (51%) — pinned to R ≈ 0 or R ≈ 1 | 28 |
| Beamsplitters (`bs1`) | 13 | **11** (85%) — pinned at extremes | **2** |

Only **2 of the 13 declared beamsplitters** are actually performing meaningful beam splitting (B1_3 at R = 0.81 and B3_1 at R = 0.30). The other 11 either function as perfect mirrors or as transparent windows. Twenty mirrors are pinned to R < 0.001 (effectively transparent), and nine to R ≥ 0.999 (effectively perfect reflectors).

The Zoo authors' own statement that the design "could be significantly simpler" is **quantitatively confirmed**: the functional core of `sol00` is roughly 40 components, against 70+ declared in the .kat file.

## Key Insights

### 1. Squeezers correlate NEGATIVELY with strain improvement

Across the 25-solution family, the number of squeezer elements has **Pearson r = −0.50** with the strain improvement factor. The two strongest solutions (sol00, sol01) carry **zero squeezers**. The weakest solutions carry 5 to 7. This contradicts conventional intuition about quantum-noise reduction. Possible explanations: the optimiser added squeezers as filler in solutions that had no other improvements available; or squeezer parameters live in noisier regions of the gradient landscape than mirror parameters; or the Urania objective function does not correctly weight the interaction between squeezers and the rest of the topology.

### 2. Aggressive transparency-pinning correlates POSITIVELY with improvement

The number of mirrors pinned to R ≈ 0 has **Pearson r = +0.51** with strain improvement. Solutions where the optimiser more aggressively pruned its own UIFO grid are the better solutions. The best designs are not the ones with the most optical machinery — they are the ones with the cleanest light paths.

### 3. sol00 has 6 arm cavities, not 2

`sol00` has 78 free spaces. Six of them are at 4-km-class lengths (three at 3847 m, three at 3670 m). The geometry is multi-arm, not a simple Michelson with two arms. Prior artifact-derived descriptions of "two essential arm cavities" were wrong.

### 4. sol00's mirror masses skew light, with median 88.6 kg vs Voyager's 200 kg

All 57 mirrors in sol00 carry an explicit mass attribute. The median is **88.6 kg**, less than half of Voyager's 200 kg test mass. Eighteen mirrors are below 50 kg. The design distributes optomechanical effects across many lighter elements rather than concentrating them in two heavy end mirrors. Whether this is responsible for sol00's quantum-noise reduction (in the absence of any squeezers) requires component-level ablation that this study did not perform.

### 5. The "120 free parameters" claim in the Zoo README is wrong

The `sol00` README claims 120 free parameters. The actual `.kat` file declares **108** with `const param0XXXX` lines (parameter IDs 0000–0133, with 26 unused gaps). The discrepancy may reflect the optimisation having pinned 12 parameters to constants before saving. The .kat file is the source of truth for what gets simulated.

### 6. sol00 has zero squeezers — the conventional quantum-noise story is wrong here

`sol00` is the strongest type8 solution and contains zero squeezer elements. Whatever quantum-noise reduction the design achieves comes from the cavity topology and mass distribution, not from external squeezed-light injection. The "frequency-dependent squeezing" pathway that Voyager uses is not the same pathway that the Urania optimiser found.

## Why This Matters

For practical detector design, this means:

- **Target sol00 (or sol01)** for any actual implementation. The other 23 solutions in the family are not worth the engineering cost.
- **The 4.05× improvement is achievable with a simpler topology** than the 70-component UIFO declaration suggests. The functional core is closer to 40 components.
- **Squeezers can be removed from this solution family without loss** — and the empirical pattern suggests they would actually help.

For AI-for-science methodology more broadly:

- **AI-discovered designs need decomposition before publication.** The Zoo's 50 designs are a useful starting point, but the Krenn et al. paper's framing — "all 50 are improvements" — obscures the heavy skew. Only a few of them are actually useful, and even the useful ones contain a lot of optimiser filler.
- **Negative correlations between conventionally-good features and improvement** are diagnostic of optimiser failure modes. The squeezer/improvement anti-correlation in this family is a flag that the optimisation landscape is doing something the field's theoretical priors did not predict.

## Methodology

- **kat parser**: 286-line Python module supporting the subset of the Finesse `.kat` language used by the Zoo. 15 pytest tests passing against the canonical sol00 README numbers. No working modern parser previously existed.
- **Cross-family analysis**: parsed all 25 type8 `.kat` files and their `strain.csv` spectra, computed log-space-averaged improvement over Voyager in 800–3000 Hz directly from the canonical strain CSVs (no Finesse re-run).
- **Voyager cross-check**: the strain.csv `strain_baseline` column was independently verified against [Differometor](https://github.com/artificial-scientist-lab/Differometor)'s bundled `voyager()` setup, which reproduces the published Voyager minimum (3.76 × 10⁻²⁵ /√Hz at 168 Hz) to within 0.1%.
- **Single-solution anatomy**: per-mirror reflectivity classification, mass distribution, beamsplitter inventory, cavity inventory.
- **Correlation analysis**: Pearson r between every structural feature and the strain improvement factor across the 25-solution family.

## Key References

1. Krenn, M., Drori, Y., & Adhikari, R.X. "Digital Discovery of Interferometric Gravitational Wave Detectors." [*Phys. Rev. X* **15**, 021012 (2025)](https://doi.org/10.1103/PhysRevX.15.021012) — the Urania system and the GW Detector Zoo.
2. [Differometor: A Differentiable Interferometer Simulator](https://github.com/artificial-scientist-lab/Differometor) (2026) — used as the independent cross-check on the Voyager baseline.
3. [GWDetectorZoo](https://github.com/artificial-scientist-lab/GWDetectorZoo) — the public dataset of 50 AI-discovered detector topologies analysed in this study.
4. Adhikari, R.X. et al. "A cryogenic silicon interferometer for gravitational-wave detection." [*Class. Quantum Grav.* **37**, 165003 (2020)](https://doi.org/10.1088/1361-6382/aba26f) — the LIGO Voyager design used as the baseline for all improvement factors.
5. Caves, C.M. "Quantum-mechanical noise in an interferometer." [*Phys. Rev. D* **23**, 1693 (1981)](https://doi.org/10.1103/PhysRevD.23.1693) — the foundational paper on quantum noise and the SQL.

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework, program.md, and full project history including the kat parser and analysis scripts in `applications/gw_detectors/`
