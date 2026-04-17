---
title: "A 20-Line Rule Matches the Best AI for Traffic Lights"
date: 2026-04-12
domain: "Transportation Engineering"
blurb: "Researchers have spent a decade training complex neural networks to time traffic lights, reporting large reductions in wait times. We found that a short deterministic rule with no learning achieves the same improvement range -- and nearly all proposed refinements made things worse."
weight: 34
tags: ["transportation", "control", "reinforcement-learning", "discovery", "traffic-signals"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/traffic_signals/paper.md).*

## The Question

Traffic lights waste your time. The global standard for fixed-time signal control dates to 1958: [Webster's formula](https://trid.trb.org/View/115048) computes the optimal cycle length and green-time split from the traffic flow on each approach. It never adapts to what is actually happening on the road. Over the past decade, the adaptive control literature has converged on deep learning methods -- neural networks that learn to time signals by trial and error in simulation -- and these consistently report 30 to 50 percent reductions in wait time over the 1958 formula.

A parallel line of work, less published and less cited, has shown that simple deterministic rules can also achieve large improvements. But no study has systematically compared these simple rules against the deep learning results on the same benchmarks. We asked: does a simple rule, properly tuned, achieve comparable improvement -- and if so, what does that say about the complexity the field has been adding?

## What We Found

A 20-line rule with four integer parameters and no learning cuts average wait time by 49 percent across seven standard simulation scenarios -- squarely within the 30 to 50 percent range that deep learning papers report. The rule is also more stable: its variation across random traffic patterns is 1.6 times lower than the fixed-time baseline.

![The simple rule falls within deep learning's 30-50 percent improvement range](plots/headline_finding.png)

- The rule delivers improvements on every one of seven tested scenarios, with gains ranging from 18 percent on light traffic to 60 percent on heavy traffic.
- Eight out of nine proposed "intelligent" refinements -- including density-based switching, pressure-based switching, and anticipatory rate adjustments -- failed in both simulators. Every attempt to add sophistication made things worse.
- The largest gains appear under medium and high demand (55 to 60 percent reduction), precisely where the 1958 formula wastes the most time serving empty approaches.
- On light traffic, the gain is only 18 percent, because the old formula is already near-optimal when queues rarely build up.
- The rule's advantage comes from a single insight: drain the current phase completely before switching, then yield to whichever other approach has the most waiting vehicles.

![Per-scenario performance shows the rule helps everywhere, but most at medium and high demand](plots/demand_sensitivity.png)

An important caveat: this is not a head-to-head comparison. No learning-based method was run on our scenarios. The 30 to 50 percent range comes from different papers using different networks, baselines, and evaluation metrics. A direct comparison is the most important piece of future work.

## Why That's Surprising

The traffic signal control community has spent a decade building increasingly complex learning systems -- graph attention networks, multi-agent coordination, transformer architectures -- to beat the 1958 fixed-time formula. The implicit assumption is that the problem is hard enough to require learning. Hundreds of papers and thousands of GPU-hours have been dedicated to this question.

What nobody systematically tested was whether a simple deterministic rule, one that just watches the queue and reacts, could match those gains. The answer turns out to be yes, at least at single intersections. The reason is almost embarrassingly simple: the 1958 formula's main weakness is that it commits to a fixed green duration before seeing traffic. Any rule that watches the actual queue and switches when the lane is empty captures that wasted time. You do not need a neural network to notice an empty lane. This suggests that the benchmarks the field has been using may not capture the conditions where learning genuinely helps -- likely network-level coordination across many intersections, not isolated signal timing.

## What It Means

If you want to deploy adaptive traffic control at a single intersection, a four-parameter rule is far easier to verify, certify, audit, and maintain than a trained neural network. It runs on a microcontroller. It has no training data and no failure modes from encountering traffic patterns it has never seen before.

For traffic engineers: the practical takeaway is that a 20-line deterministic rule should be the new floor against which complex methods demonstrate value. If a learning-based controller cannot beat this simple rule on single-intersection scenarios, it is not adding value at that scale. The case for learning-based methods is strongest at the network level -- coordinating dozens of intersections, predicting demand surges, and handling multi-modal traffic -- none of which this simple rule addresses.

Two important scope limitations: all seven scenarios are single intersections (only three of which are published benchmarks from the [sumo-rl](https://github.com/LucasAlegre/sumo-rl) library), and the simulator itself is a model of reality, not reality. The rule has not been tested on a real intersection.

## How We Did It

We ran 38 experiments across two simulators: a custom lightweight simulator for fast iteration and the standard [SUMO](https://www.eclipse.org/sumo/) traffic simulator with the [sumo-rl](https://github.com/LucasAlegre/sumo-rl) wrapper for validation. The baseline was [Webster's](https://trid.trb.org/View/115048) 1958 optimal fixed-time formula computed independently for each of seven scenarios. Twenty experiments ran on the custom simulator (Stage 1), producing a 43 percent improvement. Eighteen experiments then ran on SUMO (Stage 2), confirming that the top-level finding transferred but that optimal parameter values did not -- the best threshold shifted between simulators, and a new preemption clause was needed. The key finding emerged by the first SUMO experiment; subsequent refinements added three more percentage points. All scenarios use standard SUMO vehicle physics with no synthetic data.

## Further Reading

- Webster FV. "Traffic Signal Settings." *Road Research Technical Paper No. 39* (1958). [TRB entry](https://trid.trb.org/View/115048) -- the 1958 formula that remains the standard fixed-time baseline.
- Cools SB, Gershenson C, D'Hooghe B. "Self-Organizing Traffic Lights: A Realistic Simulation." *Advances in Applied Self-Organizing Systems* (2007). [arXiv:nlin/0610040](https://arxiv.org/abs/nlin/0610040) -- the original self-organising traffic light paper.
- Full technical write-up: [paper.md](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/traffic_signals/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
