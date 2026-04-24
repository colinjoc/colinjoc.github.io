---
title: "When does a language model become 'critical'? Pythia sits alone among transformers in already being there at random initialisation"
date: 2026-04-24
domain: "Computational Neuroscience"
blurb: "We measured a branching-ratio-style criticality signature across the full public Pythia pretraining ladder (70M → 1.4B parameters), then ran three controls: a three-seed random-initialisation baseline at each scale, a random-token-input control, and a cross-architecture replication on GPT-Neo-125M, Qwen2.5-0.5B, and Qwen2.5-1.5B. The original 410M 'emerges at step 16' finding turned out to hold nowhere else, but the reason is interesting: at small Pythia, the signature is already present at random init — numerically indistinguishable from trained values across three seeds. That is specific to Pythia: GPT-Neo-125M and two Qwen models never produce a measurable signature at random init, across three seeds each. 'Criticality emerges during pretraining' holds for every scale and architecture tested except small Pythia, where a specific init-scheme × corpus interaction places shallow MLP outputs in the near-critical band before training begins."
weight: 16
tags: ["language-models", "criticality", "pretraining", "pythia", "checkpoints", "scale-sweep", "random-init", "cross-architecture", "trajectory"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/criticality_llm_training/paper_submission_multiscale.md) has the 390-cell measurement grid, fifteen pre-registered predictions with verdicts, and the companion σ_MR-vs-α_full disagreement appendix. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** A year ago we reported that a criticality-like signature emerges in the first 16 optimiser updates of a single Pythia model (410M parameters). Over the course of five follow-up experiments — extending the Pythia scale ladder to 70M → 1.4B, adding a three-seed random-initialisation baseline at each size, swapping real text for uniformly random token IDs, and repeating the random-init protocol on three non-Pythia architectures — the picture simplifies substantially. At every scale above about 400M and at every non-Pythia model we tried, random-init MLP activations are too narrow to register a signature at all. Training genuinely has to inflate them, and when it does the onset is a sharp three-phase event rather than a smooth drift. At 70M and 160M Pythia something more unusual happens: the signature is already there at random initialisation. Across three random seeds, the mid-layer values at 160M fall inside a 0.008-wide band, numerically almost identical to the same layers after 143,000 steps of training. That signature does not replicate in GPT-Neo-125M or either Qwen2.5 model at any comparable scale, so it is specific to the Pythia (GPT-NeoX) initialisation scheme. The "emergence during pretraining" story therefore holds everywhere except inside small Pythia, where a specific init × corpus interaction places shallow MLP outputs above the measurement threshold before any gradient step has been taken.

## What we did

An adjacent [sibling study](/hdr/results/brain-llm-criticality/) ran the same avalanche-statistics measurement on three Allen mouse-brain recordings and six pretrained language models, and found that supervised fine-tuning did not measurably move the branching ratio between a Llama-3.2 base and its instruction-tuned variant. That implied the criticality signature was established during pretraining, not during later fine-tuning. We wanted to narrow "during pretraining" down.

Five experiments, all on public HuggingFace models:

- **Scale sweep (t01 + t02).** Nine log-spaced checkpoints (step 0 → 143,000) at each of five Pythia sizes: 70M, 160M, 410M, 1B, 1.4B. Five evenly-spaced MLP layers per model. 1,000 C4 documents per measurement.
- **Dense sampling (t03).** Step 256 and step 1000 added at 1B and 1.4B to resolve the transition window.
- **Three-seed random-init baseline (t04b).** Each Pythia size instantiated from its public config file with three distinct seeds, no trained weights loaded, same measurement pipeline.
- **Random-token-input control (t04c).** Each random-init Pythia fed uniformly-random token IDs in place of real text, at a single seed.
- **Non-Pythia replication (t07).** Three-seed random-init measurements on GPT-Neo-125M (EleutherAI), Qwen2.5-0.5B (Alibaba), Qwen2.5-1.5B (same family). Gemma-2-2B was attempted but its HuggingFace repository is gated, so it is recorded as a load failure.

We pre-registered fifteen predictions in the code before running anything. Seven of them were falsified.

## What we found

### 1. The step-16 onset result is scale-specific

Below 410M, the "by step 16" finding roughly holds — at 70M and 160M, four of five sampled layers already have a valid measurement by step 16 of training. At 410M, three of five do. At 1B and 1.4B, *zero* of five layers have enough measurable activity to produce a valid fit at step 16. The pre-registered prediction that at least one layer would be measurable by step 16 at every scale is falsified at the two largest scales.

### 2. At small Pythia, the signature is already there at random initialisation — reproducibly

This is the finding that reshaped the paper. We loaded each Pythia size from its public config file without fetching the trained weights, and ran the identical pipeline. Across three random seeds per scale:

- **Pythia-70M (4-5 of 5 layers measurable per seed):** branching ratio values between 0.88 and 0.96, with a systematic depth gradient — shallower layers closer to σ = 1, deeper layers closer to σ = 0.88. Cross-seed standard deviation across three seeds is 0.002–0.025.
- **Pythia-160M (3 of 5 layers per seed, same layers every seed):** mid-layer values all sit at σ ≈ 0.825, with a cross-seed standard deviation of just 0.004–0.008. Three independent random-number seeds produce three essentially identical numbers.
- **Pythia-410M:** one seed produces a single measurable layer at σ = 0.822; the other two produce none. The architecture is right at the measurement boundary.
- **Pythia-1B and 1.4B:** zero measurable layers at every seed. The random-init activations are several orders of magnitude below the measurement threshold.

Where we can compare the random-init value to the fully-trained value at the same scale and layer, the difference is often within measurement noise. Pythia-160M layer 11 measures 0.827 ± 0.004 at random init across three seeds, and 0.830 after 143,000 steps of training. The number of avalanches, by contrast, increases by one to two orders of magnitude from random init to step 143k at every matched cell. In other words: training multiplies how much activity crosses the measurement threshold, but it does not appreciably shift where the threshold-crossing activity sits in the critical-vs-subcritical landscape.

### 3. But this small-Pythia signature is GPT-NeoX-specific, not transformer-general

The previous finding was initially interpreted as "small transformers have architectural criticality at random init". That interpretation fails when we run the same protocol on three non-Pythia architectures:

- **GPT-Neo-125M** (EleutherAI, GPT-2-style dense transformer, nearly identical architectural shape to Pythia-160M — same 12 layers, same 768-dimensional hidden state): **zero measurable layers across three seeds**. The maximum avalanche count across all 15 cells (3 seeds × 5 layers) was 47, well below the fit-convergence threshold.
- **Qwen2.5-0.5B** (Alibaba, Llama-style: rotary embeddings, RMSNorm, SwiGLU MLPs, grouped-query attention): **zero measurable layers across three seeds**. Maximum avalanche count: 11.
- **Qwen2.5-1.5B** (same architectural family at larger scale): **zero measurable layers across three seeds**. Maximum avalanche count: 1 — essentially complete dark across all 15 cells.

Three architecturally distinct non-Pythia models, none of them replicating the small-Pythia finding. The distinguishing factor is the initialisation scheme: Pythia uses GPT-NeoX-style truncated normal initialisation with depth-dependent scaling; GPT-Neo uses older GPT-2-style initialisation; Qwen2.5 uses Llama-3-style initialisation. The σ ≈ 0.83 random-init signature is therefore specific to GPT-NeoX init on small-depth networks, not a property of transformers in general.

### 4. The small-Pythia signature further splits by input distribution

Replacing the C4 text corpus with uniformly-random token IDs, while holding the random-init weights fixed, gives two different answers:

- **At 70M**, the signature survives the swap. Four of five layers remain measurable, and the branching ratio values shift by no more than 0.09 from their real-text values. The 70M signature is therefore architecture-only — it does not need natural-language input statistics to appear.
- **At 160M**, the signature disappears entirely. All three of the C4-measurable layers fall below the measurement threshold when fed random tokens. The 160M signature is therefore not architecture-only; it is an interaction between the GPT-NeoX initialisation and the kind of structured temporal dependencies that real English prose provides.

So the architectural reframing has to be split further: at 70M the signature is architecture-only; at 160M the signature requires the architecture *and* natural-language input statistics; by 410M the signature is seed-marginal; by 1B it is absent regardless of input.

### 5. At 1B and 1.4B, emergence is genuine — and it has a three-phase shape

![Branching ratio σ_MR versus training step at Pythia-410M, one line per sampled layer. Random-init checkpoints are missing from the plot because they produced too few avalanches to fit. By step 16 every measurable layer is already near σ = 1. Later training fluctuates between 0.6 and 1.1. At 70M and 160M the same qualitative pattern appears; at 1B and 1.4B, every pre-step-128 point would be missing.](plots/fig1_sigma_trajectory.png)

Because 1B and 1.4B random-init are universally below the threshold on this set of seeds, training genuinely has to grow activations at those scales. We sampled the transition densely — adding checkpoints at step 256 and step 1000 on top of the base ladder — to see what the transition looks like. It has three distinct phases:

- **Phase I — deep-layer incubation.** At steps 128, 256, and 512, only the deepest sampled layer of Pythia-1.4B (layer 23 of 24) is measurable. Every other layer is below threshold.
- **Phase II — simultaneous ignition at step ≈ 1000.** At step 1000, four of five layers are jointly measurable with values tightly clustered in [0.857, 0.947]. The same happens at 1B step 1000 but with a much wider spread (0.55 to 1.05). The larger model's ignition is tighter than the smaller model's — the cross-layer spread is 0.09 at 1.4B versus 0.50 at 1B, suggesting depth rather than width is what synchronises the ignition.
- **Phase III — turbulent settling.** Between step 1000 and step 2000 at 1.4B, the count of measurable layers actually drops from 4 to 3 before rebounding to 5 by step 13,000. Individual layers cycle in and out of the measurable regime over a few hundred gradient steps. The pre-registered prediction that this count would be monotone non-decreasing after step 1000 is falsified.

By step 13,000 every scale has all sampled layers in the near-critical band.

### 6. The size-exponent result tells a different scale story

![Avalanche size exponent α_full versus training step at 410M, one line per layer. The shaded grey band is the pre-registered trained-language-model target of 1.12 to 1.37 that we carried over from the sibling study. Every layer's final value at 410M lands inside the band.](plots/fig2_alpha_trajectory.png)

The companion avalanche-size exponent narrows as models get larger. At 70M and 160M the final-checkpoint exponent sits at 1.3 to 1.44 — above the 1.12-to-1.37 band we inherited from the prior 410M work. At 410M, 1B, and 1.4B, every sampled layer's final value lands inside the band. The pre-registered prediction that at least 80 percent of layers per scale would fall inside the band passes at 410M / 1B / 1.4B and fails at 70M / 160M. This is a pre-registration failure at the small-model end that we report rather than rescue by widening the band; the widened [1.12, 1.45] band that captures every cell is flagged as a post-hoc observation for downstream studies, not as a substitute test.

### 7. Fifteen pre-registered predictions, seven falsifications, six confirmations, two partial

The full scoreboard is the paper's primary structural contribution. Confirmed: the deepest layer stays measurable throughout the transition at both 1B and 1.4B; the random-init avalanche count never exceeds the fully-trained avalanche count at matched layers; cross-seed branching-ratio variance at small Pythia falls within the pre-registered 0.05 ceiling; the 1B and 1.4B dark state replicates at every seed; every valid-fit cell stays within ±0.1 across the input-distribution swap or loses its fit entirely. Falsified: scale-invariance of step-16 onset; the α_full band at small scales; monotonicity of the large-scale transition; both of the random-init nulls at small Pythia; and the cross-architecture replication prediction. Partial: the step-16 cross-layer mean branching ratio holds where measurable but not universally; non-Pythia scale-dependence is only partially testable without the gated Gemma repository.

## Why that matters

**Initialisation schemes are not interchangeable at the measurement level we use.** GPT-NeoX-style initialisation on small-depth transformers produces MLP activations whose statistics are already inside a near-critical band at step 0. GPT-2 and Llama-3 initialisation on comparable architectures do not. This is a concrete, narrow, testable difference between init recipes that were previously treated as exchangeable in large parts of the criticality-in-neural-networks literature. It suggests that any future claim of "criticality in neural networks" needs to specify which init was used, because the answer is not architecture-family-general.

**"Emergence during pretraining" survives almost everywhere.** At 1B and 1.4B Pythia, and at every non-Pythia scale we tested, random-init is below threshold and training has real work to do. The deflationary reading ("σ_MR tracks activation magnitude, not critical dynamics") then applies to the *onset* of measurability — what "emerges" at whatever step crosses the threshold is the ability to take the measurement, not necessarily a critical regime. At the small-Pythia exception, that deflationary reading applies even to the random-init state: the threshold is already crossed, so there is no training-time onset to explain in the first place.

**Denser sampling near the large-scale transition is worth it.** The simultaneous-ignition event at step ≈ 1000 at 1.4B is invisible at standard log-spaced sampling and at two-point sampling. Anyone studying a transition of this type should include step 256, 512, 1000, and 2000 at minimum.

## Honest caveats

- **Three seeds.** The Pythia random-init result is now three-seed-confirmed (cross-seed branching-ratio standard deviation 0.002–0.025 at every reproducible layer). The non-Pythia dark result is also three-seed-confirmed. Both are substantially stronger than the previous single-seed version. But three seeds is still not a rigorous statistical sample — a formal study might want ten or more.
- **Three non-Pythia families.** GPT-Neo, Qwen2.5, and (intended) Gemma-2 cover a reasonable spread of modern-transformer init choices but are not exhaustive. OLMo, BLOOM, MPT, and Llama-3 are not tested here. The "GPT-NeoX-init-specific" claim is supported by three counter-examples, not by a proof across all transformer families.
- **Gemma-2-2B was not loadable.** The HuggingFace repository is gated and our sessions were un-authenticated. A future replication with a HuggingFace token would add a fourth non-Pythia architecture and a 2B parameter-count data point.
- **One threshold and one corpus.** Every measurement uses |z| > 2.5 on 1,000 C4 English documents, inherited from the sibling study. Threshold- and corpus-sensitivity at random init are natural next experiments.
- **Critical-band convention.** The "inside the critical band" language uses [0.7, 1.1] from the Wilting-Priesemann cortex literature. A different band gives different pass/fail counts on the random-init null.
- **Deepest-layer estimator failures.** At 1.4B and 410M layer 23, the branching-ratio estimator collapses to near zero at late training steps despite thousands of valid avalanches. A companion appendix catalogues 20 such cases across the 245-cell trained grid and attributes them to the estimator's exponential-autocorrelation-fit form hitting its asymptote. It is a known limitation of the metric, not a dynamical claim.
- **The single-seed 410M data in this study is consistent with the sibling study** but we note 410M is seed-marginal: a single different seed removes even the one measurable layer.
- **Consumer-hardware caveat.** All experiments ran on a single RTX 3060 12 GB with 15 GB of host RAM. The 1.4B sweep required a loader patch to avoid an out-of-memory kill. The patch is tested for bitwise numerical equivalence against the unfiltered loader on GPT-2 small.

## What it means in practice

**For criticality-in-neural-network researchers.** Random-init baselines at each scale, across multiple seeds, on multiple architectures, are now low-cost and diagnostic. Without them it is not possible to distinguish "training creates the signature" from "the specific init-architecture combination already has the signature". A one-line change to the loader — load from config, don't fetch the trained weights — is all it takes.

**For people working with the Pythia checkpoint ladder.** The transition window between step 128 and step 2000 at 1B+ is dense with structure. Two-point sampling misses the simultaneous-ignition event at step ≈ 1000 entirely. Include step 256, 512, 1000, and 2000.

**For people generalising from small Pythia.** Observations at Pythia-70M or Pythia-160M are not automatically statements about transformers in general. The GPT-NeoX init scheme's interaction with small depth and natural-language corpora produces behaviour that other init schemes do not. Before generalising, repeat on a non-GPT-NeoX architecture.

**For practitioners replicating on consumer hardware.** The full multi-scale + three-seed random-init + input-distribution + cross-architecture protocol runs in about six hours on a single RTX 3060 12 GB, not counting the roughly 50 GB of HuggingFace downloads for the 1B and 1.4B Pythia revisions. Each revision is deleted after its checkpoint completes, so peak disk use is about 6 GB.

## How we did it

We fetched nine Pythia checkpoints — step 0, 1, 16, 128, 512, 2000, 13000, 50000, and 143000 — for each of the five Pythia model sizes, plus step 256 and step 1000 at 1B and 1.4B. On each checkpoint we ran 1,000 C4 English documents through the model, attached a forward hook to each of five evenly-sampled MLP layers, and captured the post-MLP activations for tokens outside the padding mask. Each layer's activation matrix was z-scored column-wise, binarised at |z| > 2.5, and run through the same avalanche-extraction, power-law-fit, and branching-ratio-estimator pipeline as the sibling cortex-versus-LM study. The branching ratio came from the Wilting-Priesemann mrestimator package with its subsampling correction; the avalanche-size exponent was reported under both a tail-fit convention and the canonical x_min = 2 maximum-likelihood estimator.

For the random-init protocols (t04b, t04c, t07) we loaded each model from its public config file, seeded PyTorch with the chosen seed before model instantiation, and ran the identical downstream pipeline. For the random-token-input control (t04c), we replaced the tokenised C4 documents with uniformly-random token ID sequences drawn from each model's own vocabulary, using a separately-seeded PyTorch generator.

## Further reading

- [Pythia paper — Biderman et al. 2023](https://arxiv.org/abs/2304.01373). The Pythia checkpoint ladder and design rationale.
- [Pythia models on HuggingFace](https://huggingface.co/EleutherAI). Every intermediate checkpoint of every Pythia size.
- [Wilting and Priesemann 2018](https://www.nature.com/articles/s41467-018-04725-4). The branching-ratio estimator with subsampling correction.
- [Qwen2.5 technical report — Yang et al. 2025](https://arxiv.org/abs/2412.15115). The Llama-style architectural family used in the cross-architecture replication.
- [GPT-Neo — Black et al. 2021](https://zenodo.org/record/5297715). EleutherAI's earlier GPT-2-style model, included as the architecturally-closest non-Pythia comparison.
- [Schaeffer, Miranda, Koyejo 2023 — "Are emergent abilities of large language models a mirage?"](https://arxiv.org/abs/2304.15004). A related deflationary reading of "emergence" in large language models, resonant with our own.
- [Sibling study: brains versus language models](/hdr/results/brain-llm-criticality/). The target avalanche-exponent band and the protocol that this project inherited.
- [Full technical paper, appendix, TSV data](https://github.com/colinjoc/generalized_hdr_autoresearch/tree/main/applications/criticality_llm_training).
