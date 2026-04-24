---
title: "When does a language model become 'critical'? It depends on the scale — and at small scale the signature is there at random initialisation"
date: 2026-04-24
domain: "Computational Neuroscience"
blurb: "We measured a branching-ratio-style criticality signature across the full public Pythia pretraining ladder (70M → 1.4B parameters) at nine log-spaced checkpoints, plus a random-initialisation baseline at each scale. The earlier '410M's activation signature emerges in the first 16 optimiser steps' headline held only at 410M. At smaller scales the same number is already there at random init — training didn't create it. At larger scales the signature doesn't appear until several thousand gradient steps in, and when it does arrive it arrives through a three-phase transition, not a gradual drift. Five of nine pre-registered predictions were falsified; the data reframes what 'emergence during training' actually means."
weight: 16
tags: ["language-models", "criticality", "pretraining", "pythia", "checkpoints", "scale-sweep", "random-init", "trajectory"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/criticality_llm_training/paper_submission_multiscale.md) has the 245-cell measurement grid, the pre-registered pass/fail scorecard across nine predictions, and a companion appendix on where the two criticality metrics disagree. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** A prior version of this work (at a single scale, Pythia-410M) reported that the criticality signature "emerges" in the first 16 optimiser updates. We extended that to the full 70M → 1.4B Pythia ladder and added a random-initialisation baseline at each scale. The extension changed the story. At 70M and 160M the signature is already present at random init — with no training at all, three to four of the five sampled layers already sit inside the near-critical band, and training barely moves the value itself. At 1B and 1.4B the random-init activations are so narrow they don't cross our measurement threshold anywhere, and when training does bring them above the threshold it happens through a sharp three-phase transition — a deep-layer-only incubation, a narrow "simultaneous-ignition" event around step 1,000, then a few thousand turbulent steps of layers cycling in and out of the band before settling. The "emergence during pretraining" framing applies cleanly only at large scale; at small scale the right way to describe the data is "the architecture is critical at initialisation, and training just amplifies the activations enough to let us measure it."

## The question

An adjacent [sibling study of ours](/hdr/results/brain-llm-criticality/) ran the same avalanche-statistics measurement on three Allen mouse-brain recordings and on six pretrained language models, and found that supervised fine-tuning on a Llama-3.2-1B base/Instruct pair did not measurably change the branching ratio. That implied the criticality signature is established during pretraining, not during later fine-tuning. We wanted to narrow "during pretraining" down — and then, once the single-scale answer came out unexpectedly sharp, we wanted to check whether it held across model sizes and whether it held at *random initialisation* where there is no training at all.

Pythia (from EleutherAI) is the natural model for this. EleutherAI publishes every intermediate checkpoint — 154 of them — for every model size from 70M to 12B, all as named revisions on HuggingFace. You can load any model at any stage of its training life by asking for `revision="step128"`. You can also, using the public config, construct a randomly-initialised version of any scale without ever loading the trained weights — which is what we used for the null-baseline experiment.

Across three follow-on experiments we committed nine pre-registered predictions before running anything. Three concerned whether the step-16 onset finding would generalise across scale; three concerned the fine-grained shape of the transition at the two largest scales; three concerned what the measurements would look like on a randomly-initialised model.

## What we found

![Branching ratio σ_MR versus training step at Pythia-410M, one line per sampled layer. Random-init checkpoints are missing from the plot because they produced too few avalanches to fit. By step 16 every measurable layer is already near σ = 1. Later training fluctuates between 0.6 and 1.1. The same qualitative pattern appears at 70M and 160M; at 1B and 1.4B, every pre-step-128 point would be missing.](plots/fig1_sigma_trajectory.png)

### 1. The step-16 onset result is scale-specific

Below 410M, the "by step 16" finding roughly holds — four of five sampled layers already have a valid measurement by step 16 at 70M and 160M. At 410M, three of five layers do. At 1B and 1.4B, *zero* of five layers have enough measurable activity to produce a valid fit at step 16. The pre-registered prediction that at least one layer would be measurable by step 16 at every scale was falsified at the two largest scales.

### 2. On a *randomly initialised* model, the signature is already there at small scale

This was the decisive experiment. We instantiated each Pythia scale from its public config without loading any pretrained weights, ran the identical measurement, and asked whether the branching ratio at those layers is consistent with criticality. The fraction of sampled layers that produced a valid fit at random initialisation decreases monotonically with scale:

- **Pythia-70M: 4 of 5 layers** produce valid fits at random init, with branching ratio values between 0.88 and 0.95 — squarely inside the near-critical band.
- **Pythia-160M: 3 of 5 layers** produce valid fits, all three clustering tightly at ≈ 0.83.
- **Pythia-410M: 1 of 5 layers** produces a valid fit, at 0.82.
- **Pythia-1B and 1.4B: 0 of 5 layers** produce valid fits — the random-init activations are too narrow to register.

Where we can compare matched layers between random-init and fully-trained Pythia at the same scale, the values are often very close. Pythia-160M layer 11 measures 0.833 at random init and 0.830 at step 143,000. Pythia-70M layer 5 is 0.878 at random init and 0.894 trained. At other layers the gap is larger (70M layer 1 moves from 0.929 to 1.080), but the direction and character of the change is consistent: what training does at small scale is mostly *expand how much activity crosses the measurement threshold*, not move the branching-ratio value itself. The number of avalanches goes up by one to two orders of magnitude. The branching-ratio value barely moves on layers that were already above threshold.

This flatly falsifies the pre-registered null prediction that random-init models would *not* be in the critical band. It forces a reframing: at 70M and 160M, the near-critical signature is a property of the randomly-initialised GPT-NeoX architecture itself, not a thing that pretraining creates.

### 3. At 1B and 1.4B, emergence is genuine — and it has a three-phase shape

![Avalanche size exponent α_full versus training step at 410M, one line per layer. The shaded grey band is the pre-registered trained-language-model target of 1.12 to 1.37 that we carried over from the sibling study. At 410M every layer's final value lands inside the band. At 70M and 160M, several final values overshoot the band upward; at 1B and 1.4B, they all land squarely inside it.](plots/fig2_alpha_trajectory.png)

Because the 1B and 1.4B random-init baseline is below threshold everywhere, we cannot appeal to "it was there all along." At these scales training really is doing the work. We sampled the transition densely — adding checkpoints at step 256 and step 1000 on top of the base ladder — to see what the transition looks like. It has three distinct phases:

- **Phase I — deep-layer incubation.** At steps 128, 256, and 512, only the deepest sampled layer of Pythia-1.4B (layer 23 of 24) is measurable. Every other layer is below threshold. The picture is of a single layer "warming up" while the rest of the network stays dark.
- **Phase II — simultaneous ignition at step ≈ 1000.** At step 1000, four of five layers are measurable at once, with branching-ratio values tightly clustered in [0.86, 0.95]. The same happens at 1B step 1000 but with a much wider spread (0.55 to 1.05). The larger model's ignition is *tighter* than the smaller model's — at 1.4B the cross-layer spread of the ignition is 0.09; at 1B it is 0.50. Depth, not width, seems to be what synchronises the ignition.
- **Phase III — turbulent settling.** Between step 1000 and step 2000 at 1.4B, the count of measurable layers actually drops from 4 to 3 before rebounding to 5 by step 13,000. Individual layers cycle in and out of the measurable regime over a few hundred gradient steps. Our pre-registered prediction that this count would be monotone non-decreasing after step 1000 was falsified.

By step 13,000 every scale has all sampled layers inside the near-critical band, and the trajectory from there to the end of training is a noisy plateau.

![Cross-layer mean and standard deviation of σ_MR and α_full versus training step at 410M. The mean settles near σ ≈ 0.9 by step 128 and stays there; the cross-layer standard deviation grows slowly but steadily. α_full stabilises around 1.25 from step 128 onward. The analogous aggregate at 1B and 1.4B looks very different before step 1000, with most layers below threshold, and similar after step 13,000.](plots/fig3_trajectory_aggregate.png)

### 4. The avalanche-size exponent tells a different scale story

The companion "avalanche size exponent" measurement narrows with scale. At 70M and 160M the final-checkpoint exponent sits at 1.3 to 1.44 — above the 1.12-to-1.37 band we inherited from the prior 410M work. At 410M, 1B, and 1.4B, every sampled layer's final value lands *inside* the band. The pre-registered prediction that ≥ 80 % of layers per scale would fall inside the band passes at 410M / 1B / 1.4B and fails at 70M / 160M. This is a pre-registration failure at the small-model end that we report honestly rather than rescue by widening the band.

### 5. Five of nine pre-registered predictions were falsified

Across three experiments we had nine binary predictions committed in the code before we ran. The scoreboard: three predictions confirmed (the deepest layer stays critical throughout the transition at both 1B and 1.4B; the random-init avalanche count never exceeds the fully-trained avalanche count at the matched layer); one partial pass (the step-16 mean branching-ratio band holds where measurable but not everywhere); five falsified (scale-invariance of step-16 onset; the avalanche-exponent band; monotonicity of the large-scale transit; and both of the random-init null predictions). This scoreboard is the paper's primary scientific contribution.

## Why that matters

**The "emergence during training" framing needs a size qualifier.** At Pythia scales ≤ 410M, the near-critical branching ratio is a property of the randomly-initialised architecture. Training preserves the number while expanding how much activity crosses the measurement gate. That is a quantitatively different claim from "training self-organises the network to the edge of chaos."

**The activation magnitude doing the heavy lifting.** Under the deflationary reading, what "emerges" at step 16 at 410M is activation magnitude sufficient to cross a z = 2.5 threshold, not critical dynamics. Our own data now support this reading: at scales where the measurement works at step 0 (70M, 160M), the branching-ratio value *doesn't move much from step 0 to step 143,000.* The thing that moves is how many tokens cross the gate.

**At the large end, emergence is real and is structured.** At 1B and 1.4B, the random-init activations are not merely below the gate — they are far below. Training genuinely has to grow them, and it does so through a sharp three-phase transition that would be invisible to anyone sampling only at the start and end of training, or even at the standard log-spaced checkpoint grid. Denser sampling between step 128 and step 2000 is the right design for future studies of this class of phenomenon.

**Scale changes the observable, not just the answer.** The avalanche exponent α_full narrows as models get larger — from 1.3-to-1.44 at 70M down to 1.14-to-1.23 at 1.4B. Larger models do not just reach the same place "earlier" or "later"; they end up at a quantitatively different equilibrium. Any "scale-invariant criticality" claim in this family needs to disentangle which metric is being held invariant.

## Honest caveats

- **One random-init seed.** The random-init baseline was run on a single random-number seed at each scale. The three-layer 160M cluster at 0.83 is suspiciously tight and is plausibly a one-seed-one-corpus artefact. The paper's "architectural criticality at small scale" reframing is a single-seed demonstration; multi-seed repetition (at minimum three seeds per scale) is the highest-priority next experiment and is flagged in the paper's limitations.
- **One corpus, one threshold.** Every measurement uses 1,000 C4 English documents at |z| > 2.5. We inherited both choices from the sibling study. Threshold and corpus sensitivity are not tested here.
- **The "critical band" [0.7, 1.1] is a convention.** We justify it by reference to the Wilting-Priesemann corticis literature (cortical recordings classified as "reverberating" sit in this band). Different bands would give different pass/fail counts on the random-init null.
- **The deepest-layer estimator fails at large models in late training.** At 1.4B layer 23, the branching-ratio estimator collapses to near zero at step 50,000 and step 143,000 despite thousands of valid avalanches. The same failure was present in the 410M sibling study. A companion appendix catalogues 20 such metric-disagreement cells across the full 245-cell grid and attributes them to the estimator's autocorrelation-fit form hitting its asymptote. It is a known limitation, not a finding.
- **No causal intervention.** We observed the trajectory across published checkpoints. A shuffled-data control or frozen-weight comparison would strengthen any causal reading and is out of scope here.
- **The hardware caveat.** All experiments ran on a single RTX 3060 12 GB with 15 GB of host RAM. The 1.4B sweep required a loader patch — only hook the sampled layers, capture activations in half precision — to avoid an out-of-memory kill on the host. A 24 GB+ machine would not need the patch. The patch itself is tested for bitwise numerical equivalence against the unfiltered loader on GPT-2 small.

## What it means in practice

**For criticality-in-neural-network researchers.** Random-init baselines at each scale are essential. Without them, the "emergence during training" claim is not cleanly testable at model sizes where the random-init baseline is already inside the critical band. A one-line change to the loader — load from config, don't load the trained weights — is all it takes.

**For people working with the Pythia checkpoint ladder.** The transition window between step 128 and step 2000 is dense with structure, and two-point sampling (step 128 and step 512, or step 1000 and step 2000) will miss the simultaneous-ignition event entirely. The right log-spaced grid for studying large-model transitions includes step 256, step 512, step 1000, step 1500 or 2000.

**For practitioners replicating on consumer hardware.** The full multi-scale sweep plus random-init baseline runs in about three hours on a single RTX 3060 12 GB, not counting the roughly 50 GB of HuggingFace downloads for the 1B and 1.4B revisions. Each revision is deleted after its checkpoint completes, so peak disk use is about 6 GB.

## How we did it

We fetched nine Pythia checkpoints — step 0, 1, 16, 128, 512, 2000, 13000, 50000, and 143000 — for each of the five model sizes, from HuggingFace as named revisions. On each checkpoint we ran 1,000 C4 English documents through the model (max 64 tokens each), attached a forward hook to each of five evenly sampled MLP layers, and captured the post-MLP activations for tokens outside the padding mask. Each layer's activation matrix was z-scored column-wise, binarised at |z| > 2.5, and run through the same avalanche-extraction, power-law-fit, and branching-ratio-estimator pipeline as the sibling cortex-versus-language-model study. The branching ratio came from the Wilting-Priesemann `mrestimator` package with its subsampling correction; the avalanche-size exponent was reported under both a tail-fit convention and the canonical x_min = 2 maximum-likelihood estimator. For the random-initialisation baseline we loaded each model from its public configuration file without fetching any trained weights, seeded at 20260424, and ran the identical pipeline.

## Further reading

- [Pythia paper — Biderman et al. 2023](https://arxiv.org/abs/2304.01373). The training run, the 154-checkpoint ladder, the design rationale.
- [Pythia models on HuggingFace](https://huggingface.co/EleutherAI). Every intermediate checkpoint of every scale as a named git tag.
- [Wilting and Priesemann 2018](https://www.nature.com/articles/s41467-018-04725-4). The branching-ratio estimator with the subsampling correction.
- [Schaeffer, Miranda and Koyejo 2023 — "Are emergent abilities of large language models a mirage?"](https://arxiv.org/abs/2304.15004). A related deflationary reading of "emergence" in large language models, driven by the measurement instrument rather than the underlying dynamics.
- [Sibling study: brains versus language models](/hdr/results/brain-llm-criticality/). The primary numeric anchor for the target avalanche-exponent band and the protocol that this project inherited.
- [Full technical paper, appendix, TSV data](https://github.com/colinjoc/generalized_hdr_autoresearch/tree/main/applications/criticality_llm_training).
