---
title: "The Best AI-Discovered Gravitational-Wave Detector Is Not a Fabry-Perot at All"
date: 2026-04-09
domain: "Gravitational Wave Physics"
headline: "One artificial-intelligence-discovered design beats LIGO Voyager by 4.05× — and contains zero canonical Fabry-Perot input mirrors"
metric_name: "Strain sensitivity improvement over LIGO Voyager (post-merger band 800–3000 Hz, log-averaged)"
metric_value: "4.05× (sol00, the strongest of 25 type8 solutions)"
tags: ["physics", "interferometry", "ai-discovery", "decomposition", "ligo"]
---

## The Problem

A gravitational-wave (GW) interferometer measures the tiny distortion of space-time produced by a passing gravitational wave by comparing the round-trip times of laser light in two perpendicular kilometre-scale arms. The current best detectors — Advanced Laser Interferometer Gravitational-Wave Observatory (LIGO), Advanced Virgo, and KAGRA — are within roughly 2× of the standard quantum limit on strain sensitivity at their target frequencies. Improving them further requires either much larger detectors or fundamentally new optical topologies.

In 2025, the [Urania artificial-intelligence (AI) system](https://doi.org/10.1103/PhysRevX.15.021012) released 50 novel gravitational-wave detector topologies, all claimed to improve on the planned LIGO Voyager upgrade. Each topology is encoded as a Universal Interferometric Field Operator (UIFO) — an n×n grid of optical components (mirrors, beamsplitters, lasers, squeezers, photodetectors) connected by free-space edges. The 50 designs are catalogued in the public [GW Detector Zoo](https://github.com/artificial-scientist-lab/GWDetectorZoo). The headline number from the paper: "up to 50× more observable Universe volume" via the strongest AI-discovered topology.

The catch: nobody knows *why* the AI designs work, and the Zoo authors themselves note that "the experimental setup is not fully optimized and could be significantly simpler." We took them at their word and decomposed the entire 25-solution post-merger family from scratch.

## What We Found

We wrote a parser for the PyKat-format `.kat` configuration files that the Zoo distributes (the canonical PyKat library is broken on modern Python and there was no working alternative). Using the parser we extracted every component, parameter, and free-space connection from all 25 type8 (post-merger) solutions, and combined that structural data with the canonical strain spectra distributed alongside each solution.

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

Mean across the family: 1.43×. Median: 1.11×. Only sol00 and sol01 deliver substantial improvements; the bottom half is essentially break-even with Voyager.

### The Urania UIFO grids are grossly over-parameterised

The strongest solution, sol00, declares 57 mirrors and 13 beamsplitters. Of those:

| Component class | Count | At extreme values | Doing real work |
|---|---|---|---|
| Mirrors | 57 | **29** (51%) — pinned to reflectivity (R) ≈ 0 or R ≈ 1 | 28 |
| Beamsplitters | 13 | **11** (85%) — pinned at extremes | **2** |

Only **2 of the 13 declared beamsplitters** are actually performing meaningful beam splitting (one at R = 0.81 and one at R = 0.30). The other 11 either function as perfect mirrors or as transparent windows. Twenty mirrors are pinned to R < 0.001 (effectively transparent), and nine to R ≥ 0.999 (effectively perfect reflectors).

The Zoo authors' own statement that the design "could be significantly simpler" is **quantitatively confirmed**: the functional core of sol00 is roughly 40 components, against 70+ declared in the .kat file.

## Key Insights

### 0. Sol00 is NOT a Fabry-Perot interferometer

A Fabry-Perot cavity is the standard high-finesse optical element used in gravitational-wave detectors: two highly reflective mirrors face each other across a long arm, and the input mirror has a reflectivity in the canonical impedance-matched range R ∈ [0.99, 0.9999]. We tested whether sol00 contains any mirrors in that range. **The answer is zero.** Sol00 has 9 mirrors at R ≥ 0.999 (effectively perfect reflectors), 4 mirrors in the range 0.9 ≤ R < 0.99, and *none* in the 0.99–0.999 range. None of these are at the endpoints of any of the 6 arm-length spaces.

The implication: whatever mechanism gives sol00 its 4.05× improvement, it is not classical Fabry-Perot finesse engineering. This is the single most important open question the project raises.

### 1. Squeezers correlate NEGATIVELY with strain improvement

Squeezed-light injection is the standard quantum-noise-reduction technique in modern gravitational-wave detectors. We hypothesised that more squeezers in a Urania design would mean better strain. The data says the opposite. Across the 25-solution type8 family, the number of squeezer elements has Pearson correlation coefficient r = **−0.50** with the strain improvement factor. The two strongest solutions (sol00, sol01) carry **zero squeezers**. The weakest solutions carry 5 to 7. Possible explanations: the optimiser added squeezers as filler in solutions that had no other improvements available; or squeezer parameters live in noisier regions of the gradient landscape than mirror parameters; or the Urania objective function does not correctly weight the interaction between squeezers and the rest of the topology.

### 2. Aggressive transparency-pinning correlates POSITIVELY with improvement

The number of mirrors pinned to R ≈ 0 (i.e. components the optimiser effectively deleted from the topology) has Pearson correlation r = **+0.51** with strain improvement. Solutions where the optimiser more aggressively pruned its own UIFO grid are the better solutions. The best designs are not the ones with the most optical machinery — they are the ones with the cleanest light paths.

### 3. Sol00 has 6 arm cavities, not 2

A conventional Michelson interferometer has 2 perpendicular arms. Sol00 has 78 free spaces. Six of them are at 4-kilometre-class lengths (three at 3847 m, three at 3670 m). The geometry is multi-arm, not a simple Michelson with two arms. Prior artifact-derived descriptions of "two essential arm cavities" were wrong.

### 4. Sol00's mirror masses skew light, with median 88.6 kg vs Voyager's 200 kg

All 57 mirrors in sol00 carry an explicit mass attribute. The median is 88.6 kilograms, less than half of Voyager's 200 kg test mass. Eighteen mirrors are below 50 kg. The design distributes optomechanical effects across many lighter elements rather than concentrating them in two heavy end mirrors. Whether this is responsible for sol00's quantum-noise reduction (in the absence of any squeezers) requires component-level ablation that this study did not perform.

### 5. The "120 free parameters" claim in the Zoo's own README is wrong

The sol00 README claims 120 free parameters. The actual `.kat` file declares **108** as `const param0XXXX` lines (parameter identifiers 0000–0133, with 26 unused gaps). The discrepancy may reflect the optimisation having pinned 12 parameters to constants before saving. The .kat file is the source of truth for what gets simulated.

### 6. Sol00 has zero squeezers — the conventional quantum-noise story is wrong here

Sol00 is the strongest type8 solution and contains zero squeezer elements. Whatever quantum-noise reduction the design achieves comes from the cavity topology and mass distribution, not from external squeezed-light injection. The frequency-dependent squeezing pathway that LIGO Voyager uses is not the same pathway that the Urania optimiser found.

## Why This Matters

For practical detector design:

- **Target sol00 (or sol01)** for any actual implementation. The other 23 solutions in the family are not worth the engineering cost.
- **The 4.05× improvement is achievable with a simpler topology** than the 70-component UIFO declaration suggests. The functional core is closer to 40 components.
- **Squeezers can be removed from this solution family without loss** — and the empirical pattern suggests they would actually help.

For artificial-intelligence-for-science methodology more broadly:

- **AI-discovered designs need decomposition before publication.** The Zoo's 50 designs are a useful starting point, but the Krenn et al. 2025 paper's framing — "all 50 are improvements" — obscures the heavy skew. Only a few of them are actually useful, and even the useful ones contain a lot of optimiser filler.
- **Negative correlations between conventionally-good features and improvement** are diagnostic of optimiser failure modes. The squeezer-vs-improvement anti-correlation in this family is a flag that the optimisation landscape is doing something the field's theoretical priors did not predict.

## Methodology

**Baseline.** The comparison target is the planned [LIGO Voyager](https://doi.org/10.1088/1361-6382/aba26f) detector design — a power-recycled, signal-recycled Fabry-Perot Michelson interferometer with 200 kg crystalline silicon test masses at 123 K, a 2 µm laser, and 10 dB frequency-dependent squeezing. The Voyager strain noise spectrum used here is the `strain_baseline` column of the `strain.csv` files distributed with each Zoo solution; we independently verified this column against [Differometor](https://github.com/artificial-scientist-lab/Differometor)'s bundled `voyager()` setup, which reproduces the published Voyager minimum (3.76 × 10⁻²⁵ /√Hz at 168 Hz) to within 0.1%. The improvement factor for any candidate solution is the geometric mean of `voyager_strain / candidate_strain` across all 1002 frequency points in the post-merger band 800–3000 Hz.

**Iteration.** The decomposition runs in two stages. First, a cross-family pass: the parser extracts component counts, parameter distributions, and reflectivity histograms for all 25 type8 solutions, and combines them with each solution's `strain.csv` to produce a 25-row, 16-column structural-vs-improvement table. Second, a hypothesis-driven Decomposition Loop: 20 single-question experiments, each specified before measurement with a Bayesian prior, an articulated causal mechanism, and a pre-registered keep-or-revert decision. Each experiment tests one structural fact about sol00 or one cross-family pattern. The keep-vs-revert criterion is whether the result quantitatively matches the prior's predicted regime. Final score across the 20 experiments: **13 keeps, 7 reverts**. The seven reverts are the most informative results — they include the discovery that sol00 contains zero canonical Fabry-Perot input mirrors, falsifying the "critical cavity coupling" mechanism story.

**Cross-validation.** The kat parser is independently verified against the canonical PyKat library: both parsers agree exactly on the four base component counts in sol00 (57 mirrors, 13 beamsplitters, 78 spaces, 3 lasers).

## Key References

1. Krenn, M., Drori, Y., & Adhikari, R.X. "Digital Discovery of Interferometric Gravitational Wave Detectors." [*Physical Review X* **15**, 021012 (2025)](https://doi.org/10.1103/PhysRevX.15.021012) — the Urania system and the GW Detector Zoo.
2. [Differometor: A Differentiable Interferometer Simulator](https://github.com/artificial-scientist-lab/Differometor) (2026) — used as the independent cross-check on the Voyager baseline.
3. [GW Detector Zoo](https://github.com/artificial-scientist-lab/GWDetectorZoo) — the public dataset of 50 AI-discovered detector topologies analysed in this study.
4. Adhikari, R.X. et al. "A cryogenic silicon interferometer for gravitational-wave detection." [*Classical and Quantum Gravity* **37**, 165003 (2020)](https://doi.org/10.1088/1361-6382/aba26f) — the LIGO Voyager design used as the baseline for all improvement factors.
5. Caves, C.M. "Quantum-mechanical noise in an interferometer." [*Physical Review D* **23**, 1693 (1981)](https://doi.org/10.1103/PhysRevD.23.1693) — the foundational paper on quantum noise and the standard quantum limit.

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the Hypothesis-Driven Research framework, the program.md specification, and the full project history including the kat parser and analysis scripts in `applications/gw_detectors/`
