---
title: "Cortex and language models share the same crackle"
date: 2026-05-08
domain: "Computational neuroscience and machine learning"
blurb: "Mouse visual cortex and two very different language models all sit on the same statistical knife-edge — and one of them only got there through training."
weight: 38
tags: ["criticality", "neuroscience", "language-models", "avalanches", "neuropixels", "mamba", "gpt-2"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/entropy_brain_homology/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** When the same analysis pipeline is pointed at mouse cortex, a transformer language model, and a state-space language model, all three show the same telltale "crackle" — bursts of activity whose sizes follow nearly identical statistics. But only one of the language models, the state-space architecture, has to be trained to get there; the transformer arrives close to that critical balance from the moment it is initialised.

## The question

For more than two decades, neuroscientists have argued that healthy cortex hovers at a special operating point — a "knife-edge" between silence and runaway activity — where information flows most efficiently. The signature is unmistakable: bursts of neural activity whose sizes range over many orders of magnitude, with a precise mathematical relationship between small and large bursts. A natural question is whether large language models, which now process text with eerie fluency, organise their internal activity in the same way.

Earlier studies have hinted at a yes, but each used a different recipe — a different way to spot a burst, a different way to fit the curve, and almost never a side-by-side biological comparison. We asked the simpler, harder question: if you run cortex and language models through one identical pipeline, with one set of choices, do they really produce the same statistical fingerprint? And does that fingerprint depend on what an architecture has *learned*, or is it baked in from the start?

## What we found

The bursts of activity in mouse visual cortex, in OpenAI's GPT-2-small, and in the newer state-space model Mamba-130m really do cluster together — not identical, but tightly grouped on the same shelf. The more striking result is what happens when you strip the training away and look at randomly initialised networks. One architecture barely flinches; the other falls off the knife-edge entirely.

- The "burst size" exponent — the slope that summarises how often big avalanches happen relative to small ones — sits in a narrow band across all three substrates, and the textbook value associated with the critical balance falls inside the cortex's range.
- A second criticality measure, the branching ratio, is just shy of one for cortex (about 0.996) and for both trained language models (about 0.95) — the canonical signature of near-critical dynamics.
- Strip the training out of Mamba and the branching ratio collapses to roughly 0.57 — clearly subcritical, the dynamical equivalent of a cold engine.
- Strip the training out of GPT-2-small and almost nothing happens: the branching ratio only slips to about 0.88, still close to critical.
- The well-known shape exponent on its own is *not* a reliable criticality test: scrambling the timing of each unit's firing barely budges it, even though the underlying dynamics are now obviously broken.

## Why that matters

The "edge of chaos" idea — that neural systems compute best when poised between order and randomness — has been argued about for decades, mostly with biological data. Showing that two very different artificial architectures end up in the same regime as cortex is not, on its own, proof that they are computing the same way. But it is a strong hint that whatever pressure shapes cortex into this regime is also acting, in some form, on networks that have been optimised to predict the next word.

The training-asymmetry result is the more provocative one. State-space models like Mamba have been touted as a fresher, more efficient alternative to transformers; here we find that they reach the cortex-like regime only by learning their way to it, while transformers seem to land there at birth. That distinction has not, to our knowledge, been reported before. It suggests that two architectures which behave similarly on benchmarks may be following very different routes to the same dynamical place — and that their failure modes during training may be very different too.

There is also a methodological pay-off. The fact that the size-exponent looks identical even when we deliberately destroy the underlying timing structure is a warning to a literature that has often quoted that single number as evidence of criticality. Future work — in either neuroscience or machine learning — should report the branching ratio alongside it.

## What it means in practice

**For machine-learning researchers.** Architecture matters for how a network *acquires* its dynamical regime, not just for the regime it ends up in. If you are training a state-space model and want to monitor its progress, the branching ratio is a low-cost signal that genuinely changes during training; for transformers it barely moves. Reporting it alongside loss curves may surface dynamics that loss alone hides.

**For neuroscientists.** A unified pipeline that runs on Allen Brain Observatory recordings and on Hugging Face checkpoints with the same code lowers the cost of cross-substrate comparison substantially. The narrow-but-not-zero gap between cortex and the language models — about 0.15 in the size exponent — is itself a quantitative target for future work, rather than something to hand-wave past.

**For the broader debate.** Claims that "language models are critical, just like brains" should be treated cautiously. The clustering is real and reproducible, but our analysis also shows a small, systematic offset between cortex and the language models, and the size exponent is too forgiving to carry the claim alone.

## How we did it

We pulled three sessions of spontaneous and visually evoked spiking activity from the publicly streamable [Allen Brain Observatory Visual Coding — Neuropixels](https://dandiarchive.org/dandiset/000021) archive, and ran GPT-2-small and Mamba-130m on a thousand documents from the [C4](https://huggingface.co/datasets/allenai/c4) English text corpus. For each substrate we identified "avalanches" — contiguous bursts of activity above a threshold — and fit two complementary statistical descriptions of their size distribution. We then estimated the branching ratio (a measure of how strongly each burst tends to spawn the next) using a published method that corrects for the fact that we only see a small fraction of the underlying network. The same code path was run on randomly initialised copies of both language models as the cleanest test of whether training itself is what drives the cortex-like regime, and on time-shuffled cortex data to check that our headline statistic was not just a property of firing rates.

## Further reading

- [Neuronal avalanches in neocortical circuits (Beggs and Plenz, 2003)](https://www.jneurosci.org/content/23/35/11167) — the foundational report of cortical avalanches with the canonical size exponent near 3/2.
- [Inferring collective dynamical states from widely unobserved systems (Wilting and Priesemann, 2018)](https://www.nature.com/articles/s41467-018-04725-4) — the multistep-regression method we use to estimate the branching ratio under heavy subsampling.
- [Allen Brain Observatory — Visual Coding Neuropixels (DANDI 000021)](https://dandiarchive.org/dandiset/000021) — the open neural recordings underlying the cortex side of the comparison.
- [Full technical paper on GitHub](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/entropy_brain_homology/paper.md) — methods, tables, all thresholds, and the synthetic-validator results.
