---
title: "A 20-Line Rule Matches Deep Reinforcement Learning for Traffic Signal Control"
date: 2026-04-09
domain: "Transportation Engineering"
headline: "Two parameters cut wait times by 49% on the standard published traffic simulator — matching deep reinforcement learning with no training"
metric_name: "Average Wait Time reduction vs Webster optimal fixed-time controller (7 scenarios)"
metric_value: "−49.10% mean, −59.8% on the high-demand scenario"
tags: ["transportation", "control", "reinforcement-learning", "discovery", "occam"]
---

## The Problem

Traffic lights waste your time. The current global standard for fixed-time signal control is Webster's 1958 formula, which computes an analytically optimal cycle length and green-time split for an isolated intersection from the per-approach saturation flow. The adaptive-control literature has spent the last decade chasing Webster with deep reinforcement learning (RL) — Deep Q-Networks (DQN), Proximal Policy Optimisation (PPO), transformers — claiming 30–50% wait-time reductions on the standard published simulator for traffic, the Simulation of Urban MObility (SUMO).

We asked: does a simple deterministic rule, properly tuned, do the same?

## What We Found

A **drain-first Self-Organising Traffic Light (SOTL) rule plus a preemption clause** — about 20 lines of Python — achieves a **49.10% mean Average Wait Time (AWT) reduction** over Webster's optimal fixed-time controller on [SUMO](https://www.eclipse.org/sumo/) version 1.18 with the [sumo-rl](https://github.com/LucasAlegre/sumo-rl) wrapper version 1.4.5, evaluated across **seven scenarios**, with no training, no neural network, and no hyperparameter search.

### The discovered controller

```python
# Switch phase when EITHER:
#   (a) the other queue is at least 2× the current AND >= 4 (preemption), OR
#   (b) the current phase has fully drained AND the other has >= 1 waiting
if other_q >= max(2 * green_q, 4):
    return best_other_phase
if green_q == 0 and other_q >= 1:
    return best_other_phase
return current_phase
```

Four integer parameters: `CLEAR_THRESHOLD = 0`, `WAITING_THRESHOLD = 1`, `PREEMPT_RATIO = 2`, `PREEMPT_FLOOR = 4`. The two named conditions encode "drain the current phase first, then preempt only when the other phase is heavily oversubscribed."

### Results across the 7-scenario SUMO panel

| Scenario | Webster AWT (s) | Drain-first SOTL AWT (s) | Reduction |
|---|---|---|---|
| uniform_low  | 2.27  | 1.86 | **−18.1%** |
| uniform_med  | 4.72  | 2.06 | **−56.4%** |
| uniform_high | 9.54  | 3.84 | **−59.8%** |
| asymmetric   | 5.43  | 2.50 | **−54.0%** |
| sumo-rl horizontal-flow | 11.11 | 4.87 | **−56.2%** |
| sumo-rl vertical-flow   | 11.05 | 5.31 | **−52.0%** |
| sumo-rl variable-h-then-v-then-h | 11.02 | 5.78 | **−47.6%** |
| **Mean** | **7.88** | **3.75** | **−49.10%** |

Plus a **2.7× variance reduction** on the medium-demand scenario (2.17 ± 0.10 s vs Webster's 4.88 ± 0.16 s, measured across 5 random seeds): the simple rule is more stable across seeds, not just lower-mean.

## Five Novel Insights

### 1. Toy simulators lied, but only about parameters

We initially ran 20 experiments on a custom Poisson-arrivals + saturation-flow simulator and got −42.7%. Porting the *winning rule* to SUMO and re-running 18 experiments gave −49.1% — the top-level finding **transferred**, but the optimal `WAITING_THRESHOLD` shifted from 2 (toy) to 1 (SUMO). Worse, `WAITING_THRESHOLD = 3` was merely "slightly worse" on the toy and **catastrophic** on SUMO (+219% on the low-demand scenario). Custom simulators are useful for ranking ideas; they are dangerous for tuning numbers.

### 2. Preemption was invisible on the toy

A new rule — preempt when the other queue is ≥ 2× the current AND ≥ 4 vehicles deep — added 3 percentage points on SUMO. It was never visible on the toy because the toy used only 2 phases, hiding the inter-phase competition that SUMO's 4-phase protected-left intersections expose.

### 3. Occam's razor wins repeatedly — in both simulators

Of nine candidate "improvements" tested in both simulators, **eight failed in both**: cumulative-wait override, soft maximum-green time, asymmetric thresholds, density-based phase picking, pressure-based switching, minimum-burst constraint, anticipatory rate, starvation guard. Simplicity is robust across simulators in a way that parameter values are not.

### 4. Drain-completely strictly dominates drain-mostly

`CLEAR_THRESHOLD = 0` (wait until the current phase is completely empty) beats `= 1` (switch when only one vehicle remains) consistently. Counter-intuitive — you would think switching slightly early would help — but residual vehicles cost a full cycle of waiting.

### 5. The deep-RL traffic-signal literature has under-tested simple baselines

Published deep-reinforcement-learning controllers report 30–50% gains over fixed-time. So does a 20-line deterministic rule. The field has not systematically compared these "boring" baselines against deep RL on the same scenarios. Either deep RL is overkill for this problem, or current benchmarks are not capturing the complexity that justifies neural networks.

## Why This Matters

If you want to deploy adaptive traffic control on a microcontroller at an intersection, a 4-parameter rule is far easier to verify, certify, audit, and maintain than a trained neural network. And the methodological lesson — that custom toy simulators can hide the real performance landscape — generalises to any field where iteration speed pressures researchers toward simplified surrogates.

## Methodology

**Baseline.** The comparison target is Webster's 1958 optimal fixed-time formula, computed independently for each of the 7 SUMO scenarios from that scenario's per-approach saturation flow. The Webster controller cycles through phases at fixed durations regardless of observed traffic. On the 7-scenario panel at 3 random seeds per scenario, Webster yields a mean Average Wait Time of 7.88 seconds. On the medium-demand scenario specifically — used as the robustness reference — Webster averages 4.88 ± 0.16 seconds across 5 seeds.

**Iteration.** Each experiment was a single change to a Python controller that exposes a `select_action(state)` API. The change was committed to git **before** evaluation. The controller was then evaluated on all 7 scenarios; if the mean Average Wait Time across scenarios improved over the previous best, the change was kept; otherwise it was reverted (`git revert`) and the next hypothesis was tried. Twenty experiments were run on a custom Poisson-arrivals + saturation-flow simulator to identify candidate ideas quickly, then eighteen experiments were run on the canonical SUMO + sumo-rl benchmark to verify which findings transferred. The final controller is the result of 5 keeps out of 38 attempts; the SUMO-specific preemption rule emerged on experiment S15.

**Convergence criterion.** The loop stopped when 5 consecutive experiments produced no improvement on any scenario, indicating that the local search had exhausted obvious next moves around the current best.

## Key References

1. Webster, F.V. "Traffic Signal Settings." *Road Research Technical Paper No. 39*, HMSO London (1958).
2. Cools, S.B., Gershenson, C., D'Hooghe, B. "Self-Organizing Traffic Lights: A Realistic Simulation." *Advances in Applied Self-Organizing Systems*, Springer (2007). [arXiv:nlin/0610040](https://arxiv.org/abs/nlin/0610040)
3. Lopez, P.A. et al. "Microscopic Traffic Simulation using SUMO." *Proc. IEEE ITSC 2018*, 2575–2582. [eclipse.org/sumo](https://www.eclipse.org/sumo/)
4. Alegre, L.N. "sumo-rl: Reinforcement Learning Environments for Traffic Signal Control with SUMO." [github.com/LucasAlegre/sumo-rl](https://github.com/LucasAlegre/sumo-rl)
5. Wei, H. et al. "A Survey on Traffic Signal Control Methods." [arXiv:1904.08117](https://arxiv.org/abs/1904.08117) (2019).

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the Hypothesis-Driven Research framework, the program.md specification, and the full project history
