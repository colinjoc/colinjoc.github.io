---
title: "How Far Is AI Training from the Laws of Physics?"
date: 2026-04-19
domain: "Physics / Machine Learning"
blurb: "We applied four branches of thermodynamics to GPU-based ML training. Current practice operates at least 10 billion times below the fundamental ceiling -- and the gap grows with model scale."
weight: 23
tags: ["thermodynamics", "machine-learning", "Landauer", "GPU", "energy-efficiency", "scaling-laws", "information-theory", "deep-learning"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/thermodynamic_ml_limits/paper.md) has the derivations and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Training a GPT-4-class model on 25,000 GPUs at 17.5 megawatts produces about 1.7 bits per second of functional information -- the useful knowledge encoded in the trained model. The thermodynamic ceiling, even after six engineering corrections, is at least 10<sup>20</sup> bits per second. Current ML training operates roughly 10<sup>20</sup> below the fundamental physical limit. The gap is not shrinking with scale; it is growing. Larger models are less thermodynamically efficient per unit of information gained.

## Why would physicists care about GPU electricity bills?

Every time a GPU flips a transistor, it dissipates heat. In 1961, Rolf Landauer proved that erasing one bit of information requires dissipating at least *k*<sub>B</sub>*T* ln 2 of heat -- about 3 x 10<sup>-21</sup> joules at GPU junction temperature (350 K). This is not an engineering limit. It is a consequence of the second law of thermodynamics.

An NVIDIA H100 GPU running at 700 watts can in principle process 2 x 10<sup>23</sup> bits per second at the Landauer limit. That number is absurdly generous -- nobody would claim a GPU gains 10<sup>23</sup> bits of useful knowledge per second during training. The question is: how generous exactly, and where does all the energy go?

## Six corrections that eat into the headroom

The bare Landauer bound assumes ideal conditions: infinitely slow operation, perfect utilisation, no wasted overhead. Real GPU training violates every one of those assumptions. We identified six multiplicative correction factors:

1. **Model FLOPS utilisation (MFU):** Only 30-60% of the GPU's peak throughput goes to useful computation. The rest is pipeline bubbles and communication stalls. Factor: 0.4x.

2. **Data movement overhead:** 60% of chip power goes to moving data between memory and compute units, not to arithmetic. Factor: 0.4x.

3. **Mixed precision:** Training at FP8 instead of FP32 erases 4x fewer bits per parameter update. Factor: 0.25x.

4. **Sparsity:** If 90% of weights are zero, only 10% need updating. Factor: 0.1x (when used).

5. **Static leakage:** About 25% of power at 4 nm is leakage current that does no computation at all. Factor: 0.75x.

6. **Finite-time switching:** Real transistors switch in nanoseconds, not infinitely slowly. The energy per bit at GHz clock speeds exceeds the Landauer minimum by a factor of 10<sup>6</sup> to 10<sup>9</sup>.

Stacking the first five factors tightens the bare Landauer bound by about 333x. Adding the sixth -- using measured energy-per-operation data from Horowitz (2014) rather than the theoretical Landauer minimum -- tightens by another factor of roughly 10<sup>6</sup>.

<figure>
  <img src="plots/plot2_hierarchy_headline.png" alt="Waterfall chart showing successive corrections tightening the Landauer bound from 10^27 bits/second down to 10^20 bits/second for a GPT-4 class cluster.">
  <figcaption><strong>Figure 1.</strong> The correction hierarchy for a 25,000-GPU cluster training a GPT-4-class model. The bare Landauer bound at the top (~10<sup>27</sup> bits/s) is tightened, correction by correction. The measured CMOS bound (~10<sup>20</sup> bits/s) is the most physically meaningful ceiling. The actual functional information gain rate (~1.7 bits/s) sits roughly 10<sup>20</sup> below.</figcaption>
</figure>

## Four independent thermodynamic frameworks agree

We did not rely on Landauer's principle alone. Four independent branches of physics each set an upper bound on how fast training can gain useful information:

1. **Landauer's principle** (corrected): the energy cost of irreversible bit erasure.
2. **The Crooks fluctuation theorem**, adapted to SGD: the additional entropy produced by gradient noise.
3. **The thermodynamic uncertainty relation (TUR)**, reformulated using the independently measurable Gradient Noise Scale from McCandlish et al. (2018): the precision-dissipation tradeoff for any noisy current.
4. **Quantum speed limits** (Margolus-Levitin): the maximum computation rate for a given energy. Irrelevant for classical hardware -- it exceeds Landauer by 10<sup>13</sup> -- but included for completeness.

<figure>
  <img src="plots/plot1_framework_comparison.png" alt="Bar chart comparing bounds from four thermodynamic frameworks, spanning from 10^16 to 10^41 bits per second.">
  <figcaption><strong>Figure 2.</strong> The hierarchy of thermodynamic bounds at the GPT-4 cluster operating point. The frameworks span 25 orders of magnitude. The corrected Landauer bound with measured CMOS energy is the tightest meaningful ceiling.</figcaption>
</figure>

All four frameworks agree: current ML training is nowhere near fundamental physical limits.

## The gap grows with scale

The most surprising finding is that larger models are less thermodynamically efficient, not more. Efficiency drops by roughly six orders of magnitude from XGBoost (10<sup>6</sup> parameters) to GPT-4 (10<sup>12</sup> parameters):

| Model | Parameters | Efficiency | Gap to limit |
|-------|-----------|-----------|-------------|
| XGBoost | 10<sup>6</sup> | 8 x 10<sup>-22</sup> | 10<sup>13</sup> |
| ResNet-50 | 26M | 2 x 10<sup>-23</sup> | 10<sup>16</sup> |
| GPT-3 | 175B | 3 x 10<sup>-27</sup> | 10<sup>18</sup> |
| GPT-4 | 1.8T | 3 x 10<sup>-28</sup> | 10<sup>20</sup> |

This happens because functional information -- the useful knowledge encoded in a model -- scales roughly as the square root of parameter count, while training energy scales superlinearly. Doubling the model buys you about 40% more knowledge but costs far more than double the energy.

## Biology does it better (per operation)

We applied the same thermodynamic framework to biological information processing, enabling a direct cross-substrate comparison.

The ribosome -- biology's protein-assembly machine -- operates at 11.5% of the Landauer limit during proofreading. It spends about 20 *k*<sub>B</sub>*T* per step to gain 3.3 bits of accuracy. The best CMOS transistor operation is 10<sup>6</sup> above Landauer.

<figure>
  <img src="plots/plot3_biology_vs_ml.png" alt="Log-scale comparison of thermodynamic efficiency across biological and ML systems, from ribosome (10^-1) to GPT-4 (10^-28).">
  <figcaption><strong>Figure 3.</strong> Thermodynamic efficiency across substrates, from the most efficient known biological system (ribosomal proofreading at 11.5% of Landauer) to the least efficient (GPT-4 training at 10<sup>-28</sup>). Both biology and ML devote the vast majority of their energy to housekeeping -- maintaining homeostasis for cells, moving data for GPUs.</figcaption>
</figure>

The parallel between the two substrates is structural. In both cases, the dominant energy cost is housekeeping -- maintaining the non-equilibrium state (alive for cells, powered-on for chips) -- rather than processing information. For biology, roughly 99% of metabolic power is homeostatic overhead. For GPUs, roughly 60-90% of chip power is data movement. The path to higher efficiency is the same in both domains: reduce the fraction of energy spent maintaining state.

Per watt of power consumed, biological evolution gains functional information about four million times more efficiently than GPT-4 training. But ML training is 10<sup>12</sup> times faster in absolute bit rate, because it can pour megawatts into the problem rather than picowatts.

## What the gap tells practitioners

The thermodynamic limit is not the binding constraint on ML training. Economics and engineering are. But the analysis reveals where the largest efficiency opportunities lie:

- **The information gap** (~10<sup>10</sup>+): Most FLOPs produce intermediate results that are immediately overwritten. The ratio of total computation to functional information gained is the single largest factor. Algorithmic improvements -- better optimisers, more efficient architectures, curriculum learning -- attack this gap directly.

- **The hardware gap** (~10<sup>6</sup>-10<sup>9</sup>): CMOS transistors dissipate 10<sup>6</sup> to 10<sup>9</sup> more energy per bit than the Landauer minimum. Neuromorphic hardware (TrueNorth, Loihi) is 100-1000x closer. Photonic accelerators are 10<sup>3</sup> above Landauer -- the closest of any substrate.

- **The overhead gap** (~10<sup>3</sup>): MFU, data movement, leakage, and precision together waste about 10<sup>3</sup> of the hardware's capacity. FlashAttention, kernel fusion, and processing-in-memory attack this gap.

At Koomey's law rate (doubling computations per joule every 2.6 years), CMOS hardware will approach the Landauer limit around 2100. Long before then, the algorithmic and overhead gaps offer orders of magnitude of low-hanging fruit.

## The transferable lesson

Speed limits are useful even when nobody is close to hitting them. The 10<sup>20</sup>-fold gap between the thermodynamic ceiling and GPT-4 training tells us definitively that energy efficiency is an engineering problem, not a physics problem. There is no fundamental barrier to training models that are 10<sup>5</sup> more energy-efficient than current practice -- the headroom is enormous. The constraint is not the laws of thermodynamics. It is the state of hardware design, the efficiency of optimisation algorithms, and the willingness to invest in both.

## How we did it

All bounds were derived analytically and evaluated at standardised operating points (H100 at 700 W / 350 K; 25,000-GPU cluster at 17.5 MW). Six multiplicative correction factors were applied independently and in combination, with sensitivity analysis across all parameters. The TUR bound was reformulated using the Gradient Noise Scale (McCandlish et al. 2018) to resolve a circular dependency in prior formulations. Functional information estimates use three independent methods (MDL compression, PAC-Bayes, Blier-Ollivier scaling) with 3.6 orders of magnitude of uncertainty, which propagates to all efficiency calculations.

## Further reading

- Landauer (1961), "Irreversibility and heat generation in the computing process" -- the original information-heat link.
- Horowitz (2014), "Computing's energy problem" -- measured CMOS energy per operation.
- Koomey et al. (2011), "Implications of historical trends in the electrical efficiency of computing" -- the trajectory toward Landauer.
- Goldt and Seifert (2017), "Stochastic thermodynamics of learning" -- the formal connection between thermodynamics and neural network training.
- McCandlish et al. (2018), "An empirical model of large-batch training" -- the Gradient Noise Scale used in the TUR bound.
- [Full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/thermodynamic_ml_limits/paper.md).
- [Companion biology project: How Fast Can Evolution Actually Go?](/hdr/results/thermodynamic-info-limits/)
