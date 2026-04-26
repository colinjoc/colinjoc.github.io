---
title: "Can a per-generation 'criticality' signature predict whether a chatbot is hallucinating? A pre-registered tractability gate said no, before the experiment ran."
date: 2026-04-26
domain: "Computational Neuroscience"
blurb: "We pre-registered a head-to-head test of avalanche-criticality versus four published hallucination probes. The Phase 0.5 tractability gate failed under three protocol revisions. Honoring the pre-registration meant project KILL — and a useful negative result on what does not work."
weight: 16
tags: ["language-models", "criticality", "hallucination-detection", "negative-result", "pre-registration", "tractability-gate", "methods-note"]
---

*A plain-language summary. The [full technical note](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/criticality_capability_axis/paper_submission.md) and the [Phase 0.5 audit](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/criticality_capability_axis/phase_0_5_audit.md) document the three protocol attempts and their failure modes. See [About HDR](/hdr/) for how this work was produced and reviewed, including the two-REFRAME-cycle rule that triggered the early stop.*

**Bottom line.** A natural follow-up to our [base/instruct cross-family null](/hdr/results/sft-rlhf-criticality-distortion/) was to ask whether the same branching-ratio statistic, computed on activations *during* a chatbot's reply, predicts whether that specific reply is hallucinated. We pre-registered a 7-model × 2-benchmark × 4-baseline study and locked a tractability check before the headline experiment. The check failed in three ways: short generations are too short for the statistical machinery; sampled-resample fixes hit boundary saturation and length variance; forcing long generations makes the branching ratio cluster within a 0.03-wide band across all models, layers, and prompts — far too narrow to outperform published baselines. The autoregressive forward-pass structure pins the statistic near criticality regardless of content. Project killed early per the pre-registration; we ship the methods note and design a successor experiment with a different observable.

## The question

The avalanche branching ratio (call it σ for short) describes how many follow-up "spikes" of activity, on average, each spike triggers in a network. It is a long-standing diagnostic from neuroscience (Beggs and Plenz, 2003; Wilting and Priesemann, 2018) and recently applied to neural-network activations. In our [Pythia trajectory paper](/hdr/results/pythia-criticality-onset/) we mapped how σ converges to a settled value during pretraining; in our [base/instruct null](/hdr/results/sft-rlhf-criticality-distortion/) we showed instruction tuning leaves σ unchanged within seed noise across seven model families.

So far, σ has been measured at the *programme* level — averaged across thousands of forward passes on diverse text, treated as a property of the trained model itself. The natural next question: is σ also a *per-generation* observable? In other words, when a chatbot is replying to a single question, does its σ on that one reply predict whether the reply is correct or hallucinated? If yes, σ becomes a real-time "is the model speaking from knowledge or making things up?" detector — a deployment-relevant signal.

We pre-registered exactly that test, at cross-family scale, with sharp falsifiers. Seven instruction-tuned models. Two hallucination benchmarks (TruthfulQA, HaluEval). Four pre-registered baselines that σ would have to beat: token-loss entropy (the cheapest baseline), effective rank of activations (a static-spectral baseline), [semantic entropy](https://www.nature.com/articles/s41586-024-07421-0) from Farquhar and colleagues at Oxford (a *Nature* 2024 paper, currently the strongest black-box hallucination probe), and INSIDE/EigenScore from Chen and colleagues at ICLR 2024 (the closest published *internal-state* sibling to what we were proposing). The headline kill criterion required σ to win against *all four* baselines in at least 5 of 7 models, with bootstrap confidence intervals.

Two rounds of pre-registration scope-check tightened the design — drop a salami-sliced bundle, add the strongest internal-state baseline, lock difficulty stratification. Both rounds passed. The protocol then hit a pre-committed *tractability gate* before any hallucination labels were touched: can the σ statistic actually be measured reliably on individual chatbot generations, on each of the seven models?

## What the gate found

The gate failed three different ways, each pointing at a different aspect of the same underlying problem.

**Short generations are too short.** The pipeline for σ uses a "multistep regression" that needs a moderately long activity time series — typically hundreds of points — to fit cleanly. A 96-token chatbot reply gives you 96 points. The off-the-shelf statistical software emits warnings that its assumptions don't hold; the σ values it returns include impossible numbers like 2.7 (σ should be in [0, 1]).

**Multi-trial fixes hit boundary saturation and cross-family length variance.** The natural fix is to draw 10 alternative generations per prompt and feed them as parallel trials to the multistep regression. On the smallest model (Qwen-0.5B) this works at deeper layers — σ comes out in [0.69, 0.89], the right ballpark — but earlier layers saturate at the boundary value σ = 1, with a different warning indicating the assumption of weak stationarity is violated. Worse, on Llama-3.2-1B and Gemma-2-2B, the sampled resamples have wildly variable lengths because those models terminate replies early; the *minimum* length across 10 resamples falls below 30, leaving too few autocorrelation lags. The fix is not cross-family robust.

**Forcing long generations works statistically but kills the dynamic range.** A second fix: suppress the end-of-reply token for the first 200 generated tokens, force generations to 200–300 tokens, then run a single-trial fit. This removes the warnings: σ converges cleanly across all three model families. But every single σ value, across all model families, all five layer depths, and all tested prompts, lands in [0.97, 0.999]. A 0.03 total dynamic range. Whatever variation across hallucinated vs grounded generations exists has to fit inside that 0.03 band, most of which is presumably statistical noise from the regression itself.

For the headline to land, σ would need to support a rank-biserial correlation against hallucination labels of around 0.40 — comparable to what semantic entropy and EigenScore achieve in their published results. With a 0.03 dynamic range, almost certainly noise-dominated, that is not going to happen.

## Why σ saturates on autoregressive generations

The mechanism is the autoregressive forward pass itself. At every generation step, the next token is a deterministic-up-to-sampling function of the entire previous context, mediated through the cached attention key-value state. This bakes in very strong sequence-to-sequence autocorrelation by construction. The branching-ratio fit is exactly an autocorrelation-driven measurement — and on a sufficiently long autoregressive sequence, that autocorrelation is so strong that σ → 1 regardless of what content is being generated.

This is a structural fact about how transformers decode, not a fact about hallucination. The observation is in fact consistent with our prior cross-family null: the parent paper found σ ≈ 0.83 (settled-state, prompt-pooled) across models. Per-generation σ on long forced generations sits at the high end of that distribution, where a critical autoregressive system in steady state should be. The hypothesis that *per-generation deviations* from the settled state would track *per-generation reliability* turned out to require dynamic range that this observable, on this pipeline, does not have.

## Following the rule

The HDR programme rule we follow is: at most two REFRAME cycles per project before KILL. Phase −0.5 round 1 caught a salami-slice bundling problem (REFRAME 1, fixed). Phase 0.25 publishability review caught a missing strong baseline (REFRAME 2, INSIDE/EigenScore added). Phase 0.5 was the pre-committed tractability gate. With both REFRAME cycles consumed, a third gate fail meant project KILL — not because the question is uninteresting, but because no further protocol patching is permitted within the locked rule set.

Honoring the rule produced a short methods note instead of a long inconclusive paper, with three concrete failure modes documented. The alternative — quietly relaxing the gate or burning a third REFRAME — would have produced something less honest. We took the early stop.

## What's next

The negative result is constructive. It rules out *this* observable computed *this* way for *this* purpose. Several adjacent observables are not ruled out:

- The *fraction* of activation entries crossing a threshold, computed token by token, gives a per-token observable that does not require a long-time-series fit.
- *Cross-layer* coupling at fixed token position — a spatial rather than temporal correlation — is not affected by trial-length problems.
- *Attention-pattern entropy* is a per-token observable directly available from the attention weights, with no statistical-fit machinery in between.
- A *sliding-window σ* over the prompt-plus-generation context recovers length tractability at the cost of strict per-generation framing.

Each of these is its own pre-registration. We will not bundle them into a single paper.

## Reproducibility

The pre-registered proposal, two scope-check reviews, the publishability review, the 217-citation literature review, the Phase 0.5 audit log with all three protocol attempts, and the methods note are all in the project repository. The per-generation harvest module and the four baseline implementations have unit tests; the integration test passes on the smallest model end-to-end. The tractability gate failures are reproducible from the data and scripts.

This is the second project in this programme to ship a negative result honestly. The first was [the cross-family base/instruct null](/hdr/results/sft-rlhf-criticality-distortion/). Both followed the same rule: pre-register sharp falsifiers, run the experiment, ship the result the data supports. Sometimes the result is "this works, here's the effect"; sometimes it is "this does not work, here is why, here is what to try next."
