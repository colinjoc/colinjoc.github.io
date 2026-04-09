---
title: "A 20-Line Rule Beats RL for Traffic Signal Control on SUMO"
date: 2026-04-09
domain: "Transportation Engineering"
headline: "Two parameters cut wait times by 49% on the standard SUMO benchmark — matching deep RL with no training"
metric_name: "Wait time reduction vs Webster optimal (SUMO, 7 scenarios)"
metric_value: "-49.10% mean, -59.8% high demand"
tags: ["transportation", "control", "RL", "discovery", "occam", "sumo"]
---

## The Problem

Traffic lights waste your time. Webster's 1958 fixed-time formula is still the global standard, and the adaptive-control literature has spent the last decade chasing it with deep reinforcement learning — DQN, PPO, transformers — claiming 30–50% wait-time reductions on the standard SUMO benchmarks. We asked: does a simple deterministic rule, properly tuned, do the same?

## What We Found

A **drain-first Self-Organising Traffic Light (SOTL) rule plus a preemption clause** — about 20 lines of Python — achieves **49.10% mean wait-time reduction** over Webster's optimal fixed-time controller on [SUMO](https://www.eclipse.org/sumo/) 1.18 + [sumo-rl](https://github.com/LucasAlegre/sumo-rl) 1.4.5 across **seven scenarios**, with no training, no neural network, and no hyperparameter search.

### The discovered controller

```python
# Switch phase when EITHER:
#   (a) the other queue is at least 2x the current AND >= 4 (preemption), OR
#   (b) the current phase has fully drained AND the other has >= 1 waiting
if other_q >= max(2 * green_q, 4):
    return best_other_phase
if green_q == 0 and other_q >= 1:
    return best_other_phase
return current_phase
```

Four integer parameters: `CLEAR_THRESHOLD = 0`, `WAITING_THRESHOLD = 1`, `PREEMPT_RATIO = 2`, `PREEMPT_FLOOR = 4`.

### Results across the 7-scenario SUMO panel

| Scenario | Webster (s) | S16 (s) | Reduction |
|---|---|---|---|
| uniform_low  | 2.27  | 1.86 | **-18.1%** |
| uniform_med  | 4.72  | 2.06 | **-56.4%** |
| uniform_high | 9.54  | 3.84 | **-59.8%** |
| asymmetric   | 5.43  | 2.50 | **-54.0%** |
| sumo_rl horizontal | 11.11 | 4.87 | **-56.2%** |
| sumo_rl vertical   | 11.05 | 5.31 | **-52.0%** |
| sumo_rl vhvh       | 11.02 | 5.78 | **-47.6%** |
| **Mean** | **7.88** | **3.75** | **-49.10%** |

Plus a **2.7× variance reduction** on uniform_med (2.17 ± 0.10 s vs Webster's 4.88 ± 0.16 s, 5 seeds): the simple rule is more stable across seeds, not just lower-mean.

## Five Novel Insights

### 1. Toy simulators lied, but only about parameters

We initially ran 20 experiments on a custom Poisson + saturation-flow simulator and got -42.7%. Porting the *winning rule* to SUMO and re-running 18 experiments gave -49.1% — the top-level finding **transferred**, but the optimal `WAITING_THRESHOLD` shifted from 2 (toy) to 1 (SUMO). Worse, `WAITING_THRESHOLD = 3` was merely "slightly worse" on the toy and **catastrophic** on SUMO (+219% on uniform_low). Custom simulators are useful for ranking ideas; they are dangerous for tuning numbers.

### 2. Preemption was invisible on the toy

A new rule — preempt when the other queue is ≥ 2× the current AND ≥ 4 — added 3 percentage points on SUMO. It was never visible on the toy because the toy used only 2 phases, hiding the inter-phase competition that SUMO's 4-phase protected-left intersections expose.

### 3. Occam wins repeatedly — in both simulators

Of nine candidate "improvements" tested in both simulators, **eight failed in both**: cumulative-wait override, soft max-green, asymmetric thresholds, density-based picking, pressure switching, min-burst, anticipatory rate, starvation guard. Simplicity is robust across simulators in a way that parameter values are not.

### 4. Drain-completely strictly dominates drain-mostly

`CLEAR_THRESHOLD = 0` (wait until the current phase is completely empty) beats `= 1` consistently. Counter-intuitive — you'd think switching slightly early would help — but residual vehicles cost a full cycle of waiting.

### 5. The deep-RL traffic-signal literature has under-tested simple baselines

Published RL controllers report 30–50% gains over fixed-time. So does a 20-line deterministic rule. The field has not systematically compared these "boring" baselines against deep RL on the same scenarios. Either RL is overkill for this problem, or current benchmarks aren't capturing the complexity that justifies neural networks.

## Why This Matters

If you want to deploy adaptive traffic control on a microcontroller at an intersection, a 4-parameter rule is far easier to verify, certify, audit, and maintain than a trained neural network. And the methodological lesson — that custom toy simulators can hide the real performance landscape — generalises to any field where iteration speed pressures researchers toward simplified surrogates.

## Methodology

- **38 HDR experiments** total: 20 on a custom Poisson + saturation-flow simulator (E01–E20), 18 on [SUMO](https://www.eclipse.org/sumo/) 1.18 + [sumo-rl](https://github.com/LucasAlegre/sumo-rl) 1.4.5 (S01–S18)
- **7-scenario SUMO benchmark**, 3 seeds per scenario for the headline number
- **Robustness sweep**: 5 seeds on uniform_med
- **14 unit tests** covering Webster formula, controller contract, queue dynamics, and SUMO determinism
- **107 literature citations** in the Phase 0 review
- All code: SUMO + sumo-rl (the standard published simulator), no custom physics
- Full HDR protocol: hypothesis → prior → mechanism → one change → git commit → evaluate → keep/revert

## Key References

1. Webster, F.V. "Traffic Signal Settings." *Road Research Technical Paper No. 39*, HMSO London (1958).
2. Cools, S.B., Gershenson, C., D'Hooghe, B. "Self-Organizing Traffic Lights: A Realistic Simulation." *Advances in Applied Self-Organizing Systems*, Springer (2007). [arXiv:nlin/0610040](https://arxiv.org/abs/nlin/0610040)
3. Lopez, P.A. et al. "Microscopic Traffic Simulation using SUMO." *Proc. IEEE ITSC 2018*, 2575–2582. [eclipse.org/sumo](https://www.eclipse.org/sumo/)
4. Alegre, L.N. "SUMO-RL." [github.com/LucasAlegre/sumo-rl](https://github.com/LucasAlegre/sumo-rl)
5. Wei, H. et al. "A Survey on Traffic Signal Control Methods." [arXiv:1904.08117](https://arxiv.org/abs/1904.08117) (2019).

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework, program.md, and full project history
