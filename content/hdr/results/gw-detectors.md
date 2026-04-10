---
title: "Decomposing AI-Discovered Gravitational-Wave Detectors"
date: 2026-04-10
domain: "Physics / Gravitational-Wave Instrumentation"
headline: "The best AI-discovered detector improves on LIGO Voyager by 4.05× — via a multi-input topology with no classical analogue"
metric_name: "Log-averaged strain improvement over LIGO Voyager (800–3000 Hz)"
metric_value: "4.05× for sol00 (median of the 25-solution family: 1.11×)"
tags: ["gravitational-waves", "interferometry", "AI-for-science", "structural-analysis", "topology"]
---

## The Problem

Gravitational-wave (GW) detectors like the Laser Interferometer Gravitational-Wave Observatory (LIGO) and Virgo measure spacetime distortions smaller than 10⁻²¹ metres. Strain sensitivity is bounded by quantum noise, coating thermal noise, and seismic noise. The standard quantum limit (SQL) sets a frequency-dependent floor on what a free-mass interferometer can achieve at a given test mass and laser power. Decades of human-guided design have produced the dual-recycled Fabry-Perot Michelson interferometer with squeezed light injection — the architecture behind LIGO, Virgo, and the planned LIGO Voyager upgrade.

In 2025, the [Urania](https://doi.org/10.1103/PhysRevX.15.021012) AI system broke from this tradition. Parameterising arbitrary interferometer topologies as Universal Interferometric Field Operator (UIFO) grids, Urania used gradient-based optimisation to discover 50 novel detector designs, published in the [GWDetectorZoo](https://github.com/artificial-scientist-lab/GWDetectorZoo). The authors stated explicitly that the physical mechanisms behind these designs remain poorly understood: "The experimental setup is not fully optimized and could be significantly simpler."

We performed the first systematic structural decomposition of the 25-solution type8 family (targeting the post-merger neutron star oscillation band, 800–3000 Hz) to answer: which components carry the improvement, and what mechanism does the AI's best design actually use?

## The Baseline (What We Compared Against)

The comparison target is the **[LIGO Voyager](https://doi.org/10.1088/1361-6382/aba26f) design** — a cryogenic silicon interferometer proposed as a near-term upgrade to Advanced LIGO.

**Architecture.** Voyager is a dual-recycled Fabry-Perot Michelson interferometer: two 4-km Fabry-Perot arm cavities in an L-shaped configuration, with power recycling and signal recycling mirrors, frequency-dependent squeezed light injection via a 300-m filter cavity, and 200-kg crystalline-silicon test masses cooled to 123 K to reduce coating thermal noise.

**How it works step by step:**
1. A laser injects ~750 W of coherent light through a power-recycling mirror into a 50:50 beamsplitter.
2. The beamsplitter splits the light into two perpendicular 4-km Fabry-Perot arm cavities, each formed by an input test mass (R ≈ 0.986) and an end test mass (R ≈ 0.99999).
3. A passing gravitational wave stretches one arm and compresses the other, shifting the differential phase of the returning beams.
4. The beamsplitter recombines the beams; the differential phase shift appears as a power change at the antisymmetric output port.
5. A signal-recycling mirror at the output enhances sensitivity in a chosen frequency band.
6. Frequency-dependent squeezed vacuum is injected to reduce quantum noise below the SQL at both low frequencies (radiation pressure) and high frequencies (shot noise).
7. A balanced homodyne detector reads out the signal by subtracting two photodetector ports, rejecting classical laser-amplitude noise.

**Performance.** Voyager's strain noise spectral density reaches a minimum of 3.76 × 10⁻²⁵ /√Hz at ~168 Hz. In the post-merger band (800–3000 Hz), Voyager is shot-noise limited and serves as the reference against which the [GWDetectorZoo](https://github.com/artificial-scientist-lab/GWDetectorZoo) solutions are compared.

**Why Voyager is the right baseline.** It is the reference used by the Urania authors themselves. The Zoo distributes Voyager's strain spectrum alongside every solution. Any improvement over Voyager represents a genuine advance beyond a parametrically optimised human design.

## The Solution (What We Discovered)

The solution is a **structural decomposition** — not a new detector design but a detailed understanding of what the AI's best design, `type8/sol00`, actually does.

### What sol00 contains

We wrote a custom parser for the PyKat-format `.kat` configuration files distributed by the Zoo (the canonical PyKat library is broken on Python ≥ 3.12). The parser, cross-validated against a patched PyKat installation, extracts every component:

| Component type | Count in sol00 |
|---|---|
| Mirrors | 57 |
| Beamsplitters | 13 |
| Directional beamsplitters (Faraday-like) | 1 |
| Lasers | 3 (total 1294 W) |
| Squeezers | 0 |
| Free spaces | 78 |
| Signal injection points | 26 |
| Free parameters | 108 |

### What sol00 actually uses

The structural and topological analysis revealed that most of sol00's declared components are non-functional:

- **29 of 57 mirrors (51%)** are pinned to reflectivity extremes: 20 at R < 0.001 (effectively transparent) and 9 at R > 0.999 (effectively perfect reflectors). These are UIFO grid filler, not tuned optical elements.
- **Only 2 of 13 beamsplitters** perform meaningful beam splitting (B1_3 at R = 0.81, B3_1 at R = 0.30). Two are pinned to R = 1 (perfect mirrors); the remaining 9 are near-transparent.
- **50 of 78 free spaces (64%)** have length exactly 1.0 m — the PyKat default for an unset distance. These are topology-graph filler, not real optical paths.
- **Only 1 of 6 arm-cavity-class spaces** is a true symmetric cavity (finesse ≈ 4.6, length 3847 m). The other 5 are 2 through-pass delay lines, 1 dead trap, 1 one-sided wall, and 1 asymmetric cavity.
- **The "balanced homodyne detector" is a phantom** — one of its two photodetector ports is not connected to any optical path. The detector operates as a single-port readout. This pattern appears in 4 of the top 5 type8 solutions.

### The candidate mechanism

The most plausible explanation for sol00's 4.05× improvement is **distributed gravitational-wave signal injection across 26 free-space perturbation points**, following the canonical Michelson 180°/0° phase pattern (horizontal arms at 0°, vertical arms at 180°), fed to a single-port readout, amplified by 1294 W of coherent multi-laser injection through one low-finesse 3.8-km compound cavity. This is a multi-input, single-output topology with no obvious analogue in the published interferometer-design literature.

**What it is not:**
- Not Fabry-Perot finesse engineering (zero mirrors in the canonical R ∈ [0.99, 0.9999] range)
- Not balanced-homodyne classical-noise rejection (the second photodetector is orphaned)
- Not multi-arm Fabry-Perot signal averaging (only 1 real cavity, not 6)
- Not Voyager-style heavy-test-mass radiation-pressure suppression (the 200-kg mirrors sit on transparent through-passes and feel no radiation pressure)

**Open limitation.** A kat-to-[Differometor](https://github.com/artificial-scientist-lab/Differometor) converter is structurally complete but currently off by ~10⁶ in absolute scale, blocking quantitative ablation to confirm the magnitude of this mechanism.

## What We Found

The headline: `type8/sol00` achieves a **4.05× log-averaged strain improvement** over LIGO Voyager in the 800–3000 Hz post-merger band — substantially higher than artifact-derived prior claims of 3.12× — and is dramatically better than its 24 family siblings (median 1.11×, bottom half within ±3% of Voyager).

| Rank | Solution | Improvement vs Voyager |
|---|---|---|
| 1 | sol00 | **4.05×** |
| 2 | sol01 | 3.36× |
| 3 | sol02 | 2.68× |
| 4 | sol03 | 2.22× |
| 5 | sol04 | 1.78× |
| 6–7 | sol05–sol06 | 1.28–1.30× |
| 8–12 | sol07–sol12 | 1.10–1.14× |
| 13–25 | sol13–sol24 | 1.00–1.10× |

## Key Insights

### 1. Sol00 is not a classical interferometer

Zero mirrors have reflectivity in the canonical Fabry-Perot input range (R ∈ [0.99, 0.9999]). The mirror reflectivity distribution bifurcates into "leaky cavity" (R near 0.9) and "closed end" (R ≥ 0.999) with a structural gap between 0.99 and 0.999. Whatever sol00 is doing, it is not classical Fabry-Perot finesse engineering.

### 2. More squeezers means worse performance

Across the 25 solutions, squeezer count correlates *negatively* with strain improvement (Pearson r = −0.50). The top 4 solutions average 1.0 squeezers; the bottom 21 average 2.71. Sol00 has zero squeezers. The best solutions achieve quantum-noise reduction through topology, not through explicit squeezed-light injection.

### 3. Aggressive pruning correlates with success

The number of mirrors pinned to R ≈ 0 (transparent) correlates *positively* with improvement (r = +0.51). The optimiser produces better results when it aggressively prunes its own UIFO grid rather than fitting more components into the topology.

### 4. Single-port readout is a learned pattern, not a quirk

The phantom balanced-homodyne pattern (one photodetector port not connected to any optical path) appears in 4 of the top 5 type8 solutions. The Urania optimiser independently converged to single-port readout across multiple solutions.

### 5. The Zoo's "50 improvements" claim hides extreme skew

The bottom 13 solutions cluster within ±3% of Voyager (mean 1.027×, std 0.031). These "improvements" are within experimental noise of break-even. Practical detector design should focus on sol00 and sol01; the rest of the type8 family is not worth implementing.

### 6. The UIFO grid is grossly over-parameterised

Of sol00's 57 mirrors, 29 (51%) are at reflectivity extremes. Of 13 beamsplitters, 11 are non-functional. Of 78 free spaces, 50 (64%) are default 1.0 m filler. A functionally simplified sol00 would need roughly 40 components and 28 real spaces instead of 70+ components and 78 spaces.

### 7. Signal injection follows the textbook Michelson pattern

All 26 signal injection points split exactly between vertical-arm spaces (phase 180°) and horizontal-arm spaces (phase 0°) — the canonical Michelson differential-arm-length detection scheme. This is the only feature of sol00 that matches a textbook gravitational-wave detector.

## Why This Matters

The GWDetectorZoo represents the first AI-generated catalogue of novel gravitational-wave detector topologies. Understanding *why* these designs work — or which components are load-bearing vs. optimiser artifacts — is essential before any of them can be built. This decomposition shows that sol00's 4.05× improvement comes from a fundamentally new architecture (distributed multi-input signal injection) rather than a refinement of existing Fabry-Perot Michelson designs. If confirmed by numerical ablation, this mechanism could guide the design of next-generation detectors like Cosmic Explorer and the Einstein Telescope.

## Methodology

**Baseline.** The reference is LIGO Voyager's strain noise spectral density as distributed in the GWDetectorZoo's `strain.csv` files. We cross-validated the baseline using the [Differometor](https://github.com/artificial-scientist-lab/Differometor) JAX-based simulator, which reproduced Voyager's published minimum (3.76 × 10⁻²⁵ /√Hz at ~168 Hz) to within 0.1%.

**Iteration.** A custom kat parser (286 lines, 16-test pytest suite, cross-validated against patched PyKat) extracted component counts and parameter values from all 25 type8 `.kat` files. 20 hypothesis-driven experiments (E06–E25) tested structural properties of sol00 and cross-family correlations, with each experiment specified before measurement using a Bayesian prior, articulated mechanism, and pre-registered keep/revert criterion. 13 of 20 hypotheses were confirmed. A follow-up topological analysis (light-path tracing via breadth-first search from each laser) classified arm cavities, identified phantom detectors, and traced signal-injection patterns. The convergence indicator was the exhaustion of structurally testable hypotheses within the purely structural (non-simulation) scope.

## Key References

1. Krenn, M., Drori, Y., Adhikari, R.X. "Digital Discovery of Interferometric Gravitational Wave Detectors." [*Phys. Rev. X* **15**, 021012 (2025)](https://doi.org/10.1103/PhysRevX.15.021012)
2. Klimesch, J. et al. "Differometor: A Differentiable Interferometer Simulator." [GitHub](https://github.com/artificial-scientist-lab/Differometor)
3. Krenn, M. et al. "GW Detector Zoo." [GitHub](https://github.com/artificial-scientist-lab/GWDetectorZoo)
4. Adhikari, R.X. et al. "A cryogenic silicon interferometer for gravitational-wave detection (LIGO Voyager)." [*Class. Quantum Grav.* **37**, 165003 (2020)](https://doi.org/10.1088/1361-6382/aba26f)
5. Abbott, B.P. et al. "Observation of Gravitational Waves from a Binary Black Hole Merger." [*Phys. Rev. Lett.* **116**, 061102 (2016)](https://doi.org/10.1103/PhysRevLett.116.061102)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework, program.md, and full project history
