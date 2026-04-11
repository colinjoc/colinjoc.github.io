---
title: "A 20-Line Rule Matches the Best AI for Traffic Lights"
date: 2026-04-11
weight: 14
blurb: "Researchers have spent a decade training complex neural networks to time traffic lights, reporting large reductions in wait times. We found that a short deterministic rule with no online learning achieves the same improvement range -- and nearly all proposed refinements made things worse."
domain: "Transportation Engineering"
tags: ["transportation", "control", "reinforcement-learning", "discovery", "traffic-signals"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/traffic_signals/paper.md).*

## The Question

Traffic lights waste your time. The global standard for fixed-time signal control dates to 1958: [Webster's formula](https://trid.trb.org/View/115048) computes the optimal cycle length and green-time split from the traffic flow on each approach. It never adapts to what is actually happening on the road. Over the past decade, the adaptive control literature has converged on deep learning methods -- neural networks that learn to time signals by trial and error in simulation -- and these consistently report 30 to 50 percent reductions in wait time over the 1958 formula.

A parallel line of work, less published and less cited, has shown that simple deterministic rules can also achieve large improvements. But no study has systematically compared these simple rules against the deep learning results on the same benchmarks. We asked: does a simple rule, properly tuned, achieve comparable improvement?

## What We Found

Yes. A 20-line rule with four integer parameters and no online learning cuts average wait time by 49 percent across seven standard simulation scenarios (three random seeds each) -- squarely within the 30 to 50 percent range that deep learning papers report. The rule is also more stable: its standard deviation across random traffic patterns is 1.6 times lower than the fixed-time baseline.

The rule works by draining the current phase completely before switching, then yielding to whichever other approach has the most waiting vehicles. A preemption clause handles cases where one approach accumulates a much larger queue than the currently active one. The four parameters are: drain the current phase to zero (CLEAR_THRESHOLD = 0), yield when at least one vehicle is waiting on the other side (WAITING_THRESHOLD = 1), preempt when the other queue exceeds twice the current queue (PREEMPT_RATIO = 2) and is at least four vehicles deep (PREEMPT_FLOOR = 4).

![The simple rule falls within deep learning's 30-50 percent improvement range](plots/headline_finding.png)

An important caveat: this is not a head-to-head comparison. No reinforcement learning method was run on our scenarios. The 30 to 50 percent range comes from different papers using different networks, baselines, and metrics. A direct comparison -- running an RL agent on the same seven scenarios with the same Webster baseline -- is the most important piece of future work.

## Where It Works and Where It Does Not

The rule delivers improvements on every scenario, but the gains vary. Medium and high uniform demand saw the largest reductions (55 to 60 percent), because those are the conditions where Webster's fixed cycle wastes the most time serving empty approaches. The smallest gain was on low demand (18 percent), where Webster is already near-optimal because queues rarely accumulate.

![Per-scenario performance shows the rule helps everywhere, but most at medium and high demand](plots/demand_sensitivity.png)

Eight out of nine proposed improvements -- cumulative wait overrides, soft maximum green times, asymmetric thresholds, density-based switching, pressure-based switching, minimum-burst constraints, anticipatory rates, and starvation guards -- failed in both a lightweight custom simulator and the standard [SUMO](https://www.eclipse.org/sumo/) traffic simulator. Every attempt to add intelligence made things worse. The rule that won is the simplest one that could possibly work.

## The Simulator Lesson

We initially developed the rule on a custom lightweight simulator for fast iteration (1.5 seconds per experiment versus 30 seconds on SUMO). The top-level finding transferred: the rule beats Webster by a similar margin on both simulators. But the optimal parameter values did not transfer. The best waiting threshold shifted from 2 (custom) to 1 (SUMO), and a new preemption clause was needed to handle demand patterns that the custom simulator did not produce.

The deeper issue: the custom simulator encoded the same mathematical assumptions as Webster's formula. Beating Webster on it was close to tautological. Only validation on SUMO -- the standard published tool with realistic car-following physics -- confirmed the result was meaningful.

## What It Means

If you want to deploy adaptive traffic control at a single intersection, a four-parameter rule is far easier to verify, certify, audit, and maintain than a trained neural network. It runs on a microcontroller. It has no training data and no failure modes from distribution shift.

The practical implication for the deep learning traffic signal community is that a 20-line deterministic rule should be the new floor against which complex methods demonstrate value. Either deep learning helps under conditions this rule cannot handle -- network-level coordination across many intersections, multi-modal optimisation, demand prediction over long horizons -- or the current benchmarks are not capturing the complexity that justifies neural networks.

Two important scope limitations: all seven scenarios are single intersections (four are custom routes, only three are published benchmarks), and the result says nothing about multi-intersection coordination, which is where reinforcement learning's advantage is most likely to appear.

## How We Did It

We ran 38 experiments across two simulators: a custom lightweight simulator for fast iteration and the standard [SUMO](https://www.eclipse.org/sumo/) simulator with the [sumo-rl](https://github.com/LucasAlegre/sumo-rl) wrapper for validation. The baseline was [Webster's](https://trid.trb.org/View/115048) 1958 optimal fixed-time formula computed independently for each of seven scenarios. Each experiment modified the controller by a single change, evaluated it on all scenarios, and kept the change only if every scenario improved. The loop stopped when five consecutive experiments produced no improvement. All scenarios use standard SUMO vehicle physics with no synthetic data. Full code and experiment log are in the [project repository](https://github.com/colinjoc/hdr_autoresearch/tree/main/applications/traffic_signals).

## Further Reading

- Webster FV. "Traffic Signal Settings." *Road Research Technical Paper No. 39* (1958). [TRB entry](https://trid.trb.org/View/115048) -- the 1958 formula that remains the standard fixed-time baseline.
- Cools SB, Gershenson C, D'Hooghe B. "Self-Organizing Traffic Lights: A Realistic Simulation." *Advances in Applied Self-Organizing Systems* (2007). [arXiv:nlin/0610040](https://arxiv.org/abs/nlin/0610040) -- the original self-organising traffic light paper.
- Wei H et al. "A Survey on Traffic Signal Control Methods." (2019). [arXiv:1904.08117](https://arxiv.org/abs/1904.08117) -- a comprehensive survey of the deep learning traffic signal literature.

---

[HDR methodology](https://github.com/colinjoc/hdr_autoresearch) -- the framework and full project history
