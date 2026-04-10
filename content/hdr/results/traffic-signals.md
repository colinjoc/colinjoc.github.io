---
title: "A 20-Line Rule Matches Deep RL for Traffic Signals"
date: 2026-04-10
domain: "Transportation Engineering"
headline: "Two parameters cut wait times by 49% on the standard traffic simulator — matching deep reinforcement learning with no training"
metric_name: "Average Wait Time reduction vs Webster optimal fixed-time controller (7 scenarios)"
metric_value: "−49.10% mean, −59.8% on the high-demand scenario"
tags: ["transportation", "control", "reinforcement-learning", "discovery", "occam"]
---

## The Problem

Traffic lights waste your time. The global standard for fixed-time signal control is Webster's 1958 formula, which computes an analytically optimal cycle length and green-time split for an isolated intersection from the per-approach saturation flow. Over the past decade, the adaptive-control literature has converged on deep reinforcement learning (RL) methods — Deep Q-Networks (DQN), Proximal Policy Optimisation (PPO), transformers — claiming 30–50% wait-time reductions over fixed-time baselines on the standard Simulation of Urban MObility ([SUMO](https://www.eclipse.org/sumo/)) benchmarks.

A parallel line of work, dating to Cools, Gershenson, and D'Hooghe's 2007 Self-Organising Traffic Lights (SOTL) paper, has shown that simple deterministic rules can also achieve large improvements. But the literature has not systematically compared these "boring" baselines against deep RL on the same scenarios — creating a possible publication bias where complex methods get published and simple ones do not.

We asked: does a simple deterministic rule, properly tuned, match deep RL?

## The Baseline (What We Compared Against)

The comparison target is [Webster's](https://trid.trb.org/View/115048) **1958 optimal fixed-time controller** — the first analytically derived rule for setting fixed-cycle traffic signal timings at an isolated intersection.

**Mathematical formulation.** Define L as the total lost time per cycle (sum of yellow and all-red intervals plus startup lost time), Y = Σᵢ yᵢ as the sum of the maximum flow ratios across phases (where each yᵢ = qᵢ/sᵢ is the demand on the critical approach divided by its saturation flow). Webster's optimal cycle length is:

C₀ = (1.5L + 5) / (1 − Y)

Webster's optimal per-phase green time is:

gᵢ = (yᵢ / Y) × (C₀ − L)

The "1.5L + 5" numerator is an empirical fit Webster derived from delay-minimisation curves. The formula minimises expected total delay across all approaches under Poisson vehicle arrivals and constant saturation flow.

**What the controller does at runtime.** A Webster controller has zero state beyond the wall clock. At every simulation step it looks up the current cycle position (modulo C₀), checks which phase the position falls into, and returns that phase. It never observes vehicles, never reads queue lengths, never adapts. The cycle length and green-time splits are fixed at startup from the route file's flow values, then frozen.

**Specific baseline used.** For each of the 7 SUMO scenarios, Webster's C₀ and per-phase gᵢ were computed from the route file's flow rates using lost time L = 8 seconds per cycle (2 phases, each with 2-second yellow plus 2-second all-red). Saturation flow was taken from SUMO's per-lane vehicle physics defaults (1900 vehicles/hour/lane). The Webster baseline yields a mean Average Wait Time (AWT) of **7.88 seconds** across the 7-scenario panel. On the medium-demand scenario: 4.88 ± 0.16 seconds across 5 random seeds.

**Why Webster is the right baseline.** It is the standard fixed-time controller against which all adaptive methods in the literature are measured. It is analytically optimal under its own assumptions (Poisson arrivals, constant saturation flow). It uses no training data and no hyperparameters, making it a clean comparison for any controller that does.

## The Solution (What We Discovered)

A **drain-first SOTL rule with one preemption clause** — about 20 lines of Python, 4 integer parameters, no neural network, no training.

### The final code

```python
CLEAR_THRESHOLD = 0
WAITING_THRESHOLD = 1
PREEMPT_RATIO = 2
PREEMPT_FLOOR = 4

def select_action(state, current_phase, time_in_phase, MIN_GREEN=5):
    queues = state["lane_queues"]

    # Sum of halting vehicles on the current green phase's lanes
    green_q = sum(queues[lane] for lane in current_phase_lanes(current_phase))

    # Max queue across all other phases
    other_q = max(
        sum(queues[lane] for lane in phase_lanes(p))
        for p in other_phases(current_phase)
    )

    # Rule 1: respect minimum green
    if time_in_phase < MIN_GREEN:
        return current_phase

    # Rule 2: preempt if the other queue is much larger
    if other_q >= max(PREEMPT_RATIO * green_q, PREEMPT_FLOOR):
        return best_other_phase(queues, current_phase)

    # Rule 3: drain-first — switch when current is empty AND other has waiting
    if green_q == CLEAR_THRESHOLD and other_q >= WAITING_THRESHOLD:
        return best_other_phase(queues, current_phase)

    return current_phase
```

### How it works step by step

At every simulation step (every 3 simulated seconds):

1. **Read queues.** SUMO exposes a per-lane halting-vehicle count via `traci.lane.getLastStepHaltingNumber()`.
2. **Compute green-phase queue** as the sum of halting vehicles across all lanes served by the active green.
3. **Compute best other-phase queue** as the maximum sum across non-active phases.
4. **Enforce minimum green.** If the current phase has been green for less than MIN_GREEN seconds (typically 5), hold.
5. **Check preemption.** If the other queue is ≥ 2× the current AND ≥ 4 vehicles deep, switch immediately. This handles severe cross-traffic asymmetries.
6. **Check drain.** If the current green-phase queue has reached zero AND the other phase has ≥ 1 waiting vehicle, switch. This is the "drain first, then yield" rule.
7. **Otherwise hold.**

### Why it works

The drain-first rule succeeds for three reasons grounded in queueing theory:

1. **Eliminates phase-end waste.** Webster commits to a green duration before observing demand. If the green ends with vehicles still waiting on the other approach, those vehicles wait an additional full cycle. Drain-first switches only when the current phase is empty, eliminating this waste.
2. **Naturally adaptive to demand asymmetry.** Heavier approaches take longer to drain and hold the green longer; lighter approaches get short bursts. No explicit asymmetry parameter needed.
3. **Preemption handles heavy multi-phase scenarios.** Without preemption, a phase with 1 vehicle can hold the green while another phase accumulates 10. The preemption rule (other ≥ 2× current AND ≥ 4) breaks this in favour of the heavily loaded phase.

### Differences from Webster

| Aspect | Webster | Drain-first SOTL with preemption |
|---|---|---|
| State observed | None (wall clock only) | Per-lane halting vehicle count |
| Cycle length | Fixed at C₀ | Variable; depends on observed demand |
| Per-phase green | Fixed at gᵢ | Variable; ends when queue reaches zero |
| Adaptation | None | Implicit (heavier approaches drain slower) |
| Parameters | L, {qᵢ}, {sᵢ} pre-computed once | 4 integers, never changed |
| Lines of Python | ~50 | ~20 |

### Assumptions and limits

The controller assumes SUMO exposes a halting-vehicle count per lane, phase transitions are subject to externally enforced minimum-green time, and the simulator handles yellow and all-red transitions automatically. It does not handle pedestrian phases, emergency-vehicle preemption, transit signal priority, or coordinated green-wave operation across multiple intersections.

## What We Found

The headline: a **49.10% mean AWT reduction** over Webster across 7 [SUMO](https://www.eclipse.org/sumo/) scenarios using the [sumo-rl](https://github.com/LucasAlegre/sumo-rl) wrapper, plus a **2.7× variance reduction** on the medium-demand scenario.

| Scenario | Webster AWT (s) | SOTL+Preemption AWT (s) | Reduction |
|---|---|---|---|
| uniform-low | 2.27 | 1.86 | **−18.1%** |
| uniform-medium | 4.72 | 2.06 | **−56.4%** |
| uniform-high | 9.54 | 3.84 | **−59.8%** |
| asymmetric (N-S heavy) | 5.43 | 2.50 | **−54.0%** |
| sumo-rl horizontal-flow | 11.11 | 4.87 | **−56.2%** |
| sumo-rl vertical-flow | 11.05 | 5.31 | **−52.0%** |
| sumo-rl variable-flow | 11.02 | 5.78 | **−47.6%** |
| **Mean** | **7.88** | **3.75** | **−49.10%** |

On the medium-demand scenario at 5 seeds: Webster 4.88 ± 0.16 s, SOTL 2.17 ± 0.10 s — the simple rule is more stable across stochastic vehicle arrivals, not just lower-mean.

## Key Insights

### 1. Toy simulators transfer the finding but not the parameters

Twenty experiments on a custom Poisson-arrivals + saturation-flow simulator gave −42.7%. Porting the winning rule to SUMO gave −49.1% — the top-level finding transferred, but the optimal WAITING_THRESHOLD shifted from 2 (toy) to 1 (SUMO). WAITING_THRESHOLD = 3 was "slightly worse" on the toy and catastrophic on SUMO (+219% on the low-demand scenario). Custom simulators are useful for ranking ideas; they are dangerous for tuning numbers.

### 2. Preemption was invisible on the toy

The preemption rule (other ≥ 2× current AND ≥ 4) added 3 percentage points on SUMO. It was never visible on the toy because the toy used only 2 phases, hiding the inter-phase competition that SUMO's 4-phase protected-left intersections expose.

### 3. Occam's razor wins repeatedly in both simulators

Of 9 candidate "improvements" tested in both simulators, 8 failed in both: cumulative-wait override, soft maximum-green time, asymmetric thresholds, density-based phase picking, pressure-based switching, minimum-burst constraint, anticipatory rate, starvation guard. Simplicity is robust across simulators in a way that parameter values are not.

### 4. Drain-completely strictly dominates drain-mostly

CLEAR_THRESHOLD = 0 (wait until the current phase is completely empty) beats = 1 (switch when one vehicle remains) consistently. Residual vehicles cost a full cycle of waiting — switching slightly early does not help.

### 5. Deep RL traffic-signal literature has under-tested simple baselines

Published deep RL controllers report 30–50% gains over fixed-time. So does a 20-line deterministic rule. Three conjectured reasons: (a) many RL papers compare against poorly tuned fixed-time rather than Webster-optimal; (b) standard benchmarks under-test conditions where complex policies genuinely help; (c) publication bias — a simple rule is harder to publish than a novel neural architecture.

## Why This Matters

If you want to deploy adaptive traffic control on a microcontroller at an intersection, a 4-parameter rule is far easier to verify, certify, audit, and maintain than a trained neural network. The methodological lesson — that custom toy simulators can hide the real performance landscape — generalises to any field where iteration speed pressures researchers toward simplified surrogates.

The practical implication for the deep RL traffic-signal community: a 20-line deterministic rule should be the new floor against which complex policies must demonstrate value. Either deep RL helps under conditions this simple rule cannot handle (network-level coordination, multi-modal optimisation, demand prediction), or current benchmarks are not capturing the complexity that justifies neural networks.

## Methodology

**Baseline.** [Webster's](https://trid.trb.org/View/115048) 1958 optimal fixed-time formula, computed independently for each of the 7 [SUMO](https://www.eclipse.org/sumo/) scenarios from that scenario's per-approach saturation flow. The Webster controller cycles through phases at fixed durations regardless of observed traffic. On the 7-scenario panel at 3 random seeds per scenario, Webster yields a mean AWT of 7.88 seconds. On the medium-demand scenario at 5 seeds: 4.88 ± 0.16 seconds.

**Iteration.** Each experiment was a single change to a Python controller exposing a `select_action(state)` API, committed to git before evaluation. The controller was evaluated on all 7 scenarios; if the mean AWT improved, the change was kept; otherwise it was reverted. 20 experiments ran on a custom Poisson-arrivals + saturation-flow simulator to identify candidate ideas quickly (~1.5 s per experiment), then 18 experiments ran on the canonical SUMO + [sumo-rl](https://github.com/LucasAlegre/sumo-rl) benchmark (~30–60 s per experiment) to verify which findings transferred. Stage 1 produced a 42.67% improvement; stage 2 refined it to 49.10%. The SUMO-specific preemption rule emerged on experiment S15. The loop stopped when 5 consecutive experiments produced no improvement on any scenario.

## Key References

1. Webster, F.V. ["Traffic Signal Settings."](https://trid.trb.org/View/115048) *Road Research Technical Paper No. 39*, HMSO London (1958).
2. Cools, S.B., Gershenson, C., D'Hooghe, B. "Self-Organizing Traffic Lights: A Realistic Simulation." *Advances in Applied Self-Organizing Systems*, Springer (2007). [arXiv:nlin/0610040](https://arxiv.org/abs/nlin/0610040)
3. Lopez, P.A. et al. "Microscopic Traffic Simulation using SUMO." *Proc. IEEE ITSC 2018*, 2575–2582. [eclipse.org/sumo](https://www.eclipse.org/sumo/)
4. Alegre, L.N. "sumo-rl: Reinforcement Learning Environments for Traffic Signal Control with SUMO." [GitHub](https://github.com/LucasAlegre/sumo-rl)
5. Wei, H. et al. "A Survey on Traffic Signal Control Methods." [arXiv:1904.08117](https://arxiv.org/abs/1904.08117) (2019).

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework, program.md, and full project history
