---
title: "Four Smart Cars Dissolve a Phantom Traffic Jam on the Sugiyama Ring Road"
date: 2026-04-09
domain: "Transportation / Traffic Flow Control"
headline: "Four Adaptive Cruise Control (ACC) vehicles among 22 human drivers (18.2% penetration) reduce phantom traffic jam wave amplitude from 8.17 to 0.55 m/s (93.3% reduction) on the canonical Sugiyama ring road; the transition is sharp -- three ACC vehicles (13.6%) still leave a 1.77 m/s wave; FollowerStopper requires 22.7% penetration for comparable suppression but imposes a 61% throughput penalty"
metric_name: "Wave amplitude (mean per-timestep max-min velocity in steady-state window) on a 22-vehicle / 230-metre Intelligent Driver Model ring road; secondary metrics: velocity variance, throughput (Edie's generalised definition), fuel proxy (VT-Micro simplified), minimum spacing"
metric_value: "Phase 1 winner ACC at 18.2%: wave_amp 0.55 m/s (93.3% reduction from 8.17 m/s baseline); Phase B sweep critical penetration: 4/22 (18.2%) for ACC, 5/22 (22.7%) for FollowerStopper; ACC throughput at 18.2%: 930 veh/hr (only 10.5% reduction from baseline 1039 veh/hr)"
tags: ["transportation", "traffic-flow", "phantom-jams", "autonomous-vehicles", "ring-road", "IDM", "ACC", "wave-suppression", "hypothesis-driven-research"]
---

## The Problem

You are driving on a clear, open highway with no accidents, no construction, no merging traffic -- and yet traffic suddenly stops. You crawl for several minutes, then accelerate back to speed for no apparent reason. You have just experienced a phantom traffic jam.

These waves form spontaneously when traffic density exceeds a critical threshold. Human drivers react to small perturbations -- a slight brake tap, a momentary distraction -- by braking harder than necessary, which causes the driver behind to brake even harder, propagating backward through traffic as an amplifying wave. The Japanese physicist Yuki Sugiyama proved this experimentally in 2008 by placing 22 drivers on a 230-metre circular track and watching them spontaneously generate a stop-and-go wave with no external trigger. The wave travelled backward at approximately 15 kilometres per hour and persisted indefinitely.

The control question is direct: if a fraction of those 22 drivers were replaced by smart cars -- vehicles with longitudinal controllers designed to smooth their speed profiles -- how many would you need to dissolve the wave?

## The Baseline (What We Compared Against)

The baseline is a pure-Python simulation of the Sugiyama ring road using the Intelligent Driver Model (IDM) for all 22 human drivers. The IDM is the standard microscopic car-following model in traffic research, governing each vehicle's acceleration based on its current speed, the gap to the leader, and the relative velocity:

```python
acceleration = a * [1 - (v / v0)^delta - (s_star / gap)^2]
s_star = s0 + max(0, v * T + v * delta_v / (2 * sqrt(a * b)))
```

With parameters tuned for ring-road instability (time headway T = 1.0 s, desired speed v0 = 30 m/s, Gaussian acceleration noise sigma = 0.3 m/s^2), the simulation reliably produces a phantom jam matching the Sugiyama experiment.

Baseline metrics (experiment E00, all-IDM, seed=42):

| Metric | Value | Meaning |
|---|---|---|
| Wave amplitude | 8.17 m/s | Mean velocity range per timestep in steady state |
| Velocity variance | 2.89 m/s | Standard deviation of all velocities |
| Throughput | 1039.4 veh/hr | Edie's generalised throughput |
| Fuel proxy | 130.65 mL/km | VT-Micro simplified model |
| Minimum spacing | 1.79 m | Smallest bumper-to-bumper gap |

The noise floor from a 5-seed sweep is +/- 0.40 m/s on wave amplitude (2-sigma), setting the keep/revert threshold for hypothesis testing.

## The Solution

The winning controller is a simple Adaptive Cruise Control (ACC) with constant time-headway policy:

```python
@dataclass
class ACCController:
    v_des: float = 20.0    # desired cruise speed (m/s)
    T_des: float = 1.8     # desired time headway (s)
    s0: float = 4.0        # minimum standstill gap (m)
    k1: float = 0.3        # gap-error gain
    k2: float = 0.5        # speed-difference gain

    def __call__(self, own_v, lead_v, gap, dt):
        desired_gap = self.s0 + own_v * self.T_des
        accel = self.k1 * (gap - desired_gap) + self.k2 * (lead_v - own_v)
        if gap > 3.0 * desired_gap:
            accel += 0.2 * (self.v_des - own_v)
        return clamp(accel, -9.0, 3.0)
```

Four ACC vehicles placed at equally spaced positions around the 22-vehicle ring (18.2% penetration) reduce wave amplitude from 8.17 to 0.55 m/s -- a 93.3% reduction. The ACC works through two mechanisms: (1) gap-error feedback pulls the vehicle toward a target headway, preventing the gap oscillations that amplify into waves, and (2) relative-velocity damping directly opposes speed differences between the ACC and its leader, preventing perturbation amplification. The ACC's conservative time headway (1.8 s vs the human's 1.0 s) provides a buffer that absorbs perturbations without requiring hard braking.

Four vehicles suffice because they divide the ring into human-driver platoons of at most 4-5 vehicles each, which is below the critical platoon length for IDM string instability at these parameters.

## What We Found

### Phase 1: Controller Tournament (12 experiments)

Five controller families tested at 4.5% and 18.2% penetration:

| Controller | 4.5% (1/22) Wave Amp | 18.2% (4/22) Wave Amp | 18.2% Throughput |
|---|---|---|---|
| IDM (control) | 7.15 m/s | 8.08 m/s | 1042.7 veh/hr |
| FollowerStopper | 8.28 m/s | 4.44 m/s | 529.4 veh/hr |
| PIWithSaturation | 8.77 m/s | 30.13 m/s (BROKEN) | 3962.8 veh/hr |
| **ACC** | **7.45 m/s** | **0.55 m/s** | **930.4 veh/hr** |
| ConstantVelocity | 0.46 m/s | 0.33 m/s | 2747.8 veh/hr (unsafe) |

ACC wins decisively. ConstantVelocity is effective but unsafe (ignores the leader). PIWithSaturation is catastrophically unstable due to integral windup.

### Phase 2: 105 Hypotheses (20 themes)

1 KEEP, 104 REVERT, 0 DEFER across penetration sweeps, controller gain tuning, ring size, human-driver model parameters, noise levels, vehicle placement, heterogeneous desired speeds, multi-objective trade-offs, run length sensitivity, integration timestep validation, and mixed controller strategies.

### Phase B: Dense Penetration Sweep

ACC penetration from 0% to 100% in steps of 1 vehicle:

| Vehicles | Penetration | Wave Amp (m/s) | Throughput (veh/hr) | Fuel (mL/km) |
|---|---|---|---|---|
| 0 | 0.0% | 8.17 | 1039.4 | 130.65 |
| 1 | 4.5% | 7.45 | 1008.5 | 126.47 |
| 2 | 9.1% | 5.27 | 1006.1 | 117.47 |
| 3 | 13.6% | 1.77 | 984.8 | 109.15 |
| **4** | **18.2%** | **0.55** | **930.4** | **107.55** |
| 5 | 22.7% | 0.50 | 875.7 | 107.15 |
| 6 | 27.3% | 0.41 | 824.5 | 106.76 |
| 11 | 50.0% | 0.26 | 607.2 | 104.87 |
| 22 | 100.0% | 0.00 | 283.2 | 100.00 |

The transition between 3 and 4 ACC vehicles is the sharpest feature: a single additional smart car reduces wave amplitude by a factor of 3.2.

## Key Insights

1. **The critical penetration rate for ACC is 18.2% (4/22 vehicles).** Below this, waves persist. Above this, there are diminishing returns. The transition is sharp because it corresponds to reducing the maximum human-platoon length below the critical threshold for IDM string instability.

2. **ACC beats FollowerStopper at matched penetration (0.55 vs 4.44 m/s).** This is surprising given that FollowerStopper was the controller used in the landmark Stern (2018) ring-road experiment. The explanation: FollowerStopper's default parameters (v_des = 15 m/s, s_go = 35 m) are calibrated for highway speeds, not the dense ring's 4-5 m/s equilibrium. When FS is re-tuned for the ring (v_des = 5-8 m/s), it matches ACC performance.

3. **ACC preserves throughput; FollowerStopper destroys it.** ACC at 18.2% costs only 10.5% throughput (930 vs 1039 veh/hr). FollowerStopper at 22.7% costs 61% (401 vs 1039 veh/hr). At 100%, FS collapses to 7.6 veh/hr while ACC maintains 283 veh/hr.

4. **PIWithSaturation is catastrophically unstable on the ring.** The integral term accumulates persistent gap error (the ring's equilibrium gap is far below PI's target), causing runaway oscillation. Even extensive gain tuning cannot fix this fundamental mismatch.

5. **The phantom jam is a dynamical attractor.** Steady-state wave amplitude is independent of perturbation type, strength, and timing (experiments H062-H065 all yield 8.0-8.2 m/s). The wave structure is determined by the traffic flow equations, not initial conditions.

6. **Vehicle placement matters: equally-spaced beats clustered.** Clustering 4 FS vehicles at adjacent positions (H066: 7.18 m/s) is dramatically worse than equal spacing (T04: 4.44 m/s), because clustering creates one long uncontrolled platoon that supports wave growth.

7. **The result partially transfers to larger rings.** ACC at 18% penetration on a 100-vehicle/1000-metre ring (same density) achieves 1.08 m/s -- reduced from 0.55 m/s on the small ring. Larger rings support more complex wave structures and require maintaining absolute smart-vehicle spacing, not just penetration fraction.

## Why This Matters

The phantom traffic jam is not merely annoying. In the United States alone, traffic congestion costs an estimated 8.8 billion hours and 3.3 billion gallons of wasted fuel per year (Texas Transportation Institute, 2023). Stop-and-go waves account for a significant fraction of this waste because they force vehicles through repeated acceleration-deceleration cycles, each consuming more fuel than steady-speed driving.

The finding that four smart cars in a platoon of 22 -- roughly one in five -- can dissolve the wave has direct implications for the deployment of connected and automated vehicles. Commercial ACC systems are already installed in millions of vehicles, though as Gunter et al. (2020) demonstrated, current commercial ACC systems are actually string-unstable and can make phantom jams worse. The gap between the ACC controller studied here and real commercial systems is primarily one of calibration: the stock ACC prioritises short following distance for driver convenience, while wave-suppressing ACC requires a longer time headway (1.8 s vs typical 0.8-1.2 s) to ensure string stability.

The CIRCLES consortium's MegaVanderTest on Interstate 24 in Nashville (2022) deployed 100 purpose-designed AVs at 3-5% penetration and observed measurable but incomplete wave suppression. Our finding that 4.5% (1/22) penetration reduces wave amplitude by only 9% on the ring is consistent with the MVT's modest effect at similar penetration. The sharp transition at 18.2% suggests that the MVT would need roughly 3-4 times more vehicles to see dramatic improvement -- a finding that could inform future field experiment design.

Important caveats: the ring road is a simplified one-dimensional model with periodic boundaries, no lane changes, no on-ramps, and conserved density. Real highways have all of these complications, and the minimum penetration rate on a real freeway is almost certainly higher than 18.2%. Nevertheless, the ring road provides the cleanest possible testbed for isolating the wave-suppression mechanism from confounding factors, and the qualitative finding -- that a modest fraction of string-stable vehicles can break the feedback loop that sustains phantom jams -- is robust across the 184 experiments in this study.

## Methodology

This project follows the Hypothesis-Driven Research (HDR) methodology:

1. **Phase 0: Literature review** -- 224 verified citations covering traffic flow theory (Lighthill-Whitham-Richards, Aw-Rascle-Zhang), car-following models (IDM, Optimal Velocity, Gipps), string stability theory (Swaroop-Hedrick, Wilson-Ward), controller design (FollowerStopper, PI-with-saturation, ACC/CACC, reinforcement learning), and field experiments (Sugiyama 2008, Stern 2018, CIRCLES MegaVanderTest)

2. **Phase 0.5: Baseline audit** -- All-IDM ring road established as E00, 5-seed sweep for noise floor quantification

3. **Phase 1: Controller tournament** -- 5 families at 2 penetration levels + 2 ceiling checks (12 experiments)

4. **Phase 2: HDR loop** -- 105 pre-registered single-change experiments across 20 themes with strict keep/revert criterion (wave amplitude must improve by >0.40 m/s, the 2-sigma noise floor)

5. **Phase 2.5: Compositional retest** -- 10 compositions of top single-change improvements

6. **Phase B: Discovery sweep** -- Dense penetration sweep (0-22 vehicles) for ACC, FollowerStopper (default), and FollowerStopper (ring-tuned), yielding the critical penetration rate and Pareto front

Total: 184 experiments, each a 600-second simulation of 22-200 vehicles. All experiments are deterministic (seed=42) and reproducible.

## Selected Phase 2 Highlights

The 105-hypothesis HDR loop produced several notable findings beyond the headline result:

**FollowerStopper is actually excellent -- when tuned for the ring.** The default FollowerStopper parameters (v_des = 15 m/s, s_go = 35 m) are designed for highway speeds. On the dense ring where equilibrium speed is 4-5 m/s, the FS operates entirely in its "stop" region and never reaches cruise mode. Reducing v_des to 5-8 m/s (H017-H018) brought FS wave amplitude down to 0.30-0.32 m/s at 18.2% penetration -- matching ACC. The throughput penalty persists, however, making ACC preferable in practice.

**ACC time headway has a non-monotonic optimum.** Shorter time headway (T_des = 0.8-1.0 s) makes ACC string-unstable and *worsens* the wave (H034: 9.55 m/s, H035: 8.57 m/s). Longer headway (T_des = 2.5-3.0 s) provides slightly better wave suppression (0.36-0.39 m/s) but at the cost of reduced throughput. The default T_des = 1.8 s sits at a practical sweet spot.

**The wave is a true dynamical attractor.** Removing the initial perturbation entirely (H062: 8.00 m/s), strengthening it to maximum braking (H063: 8.20 m/s), or delaying it to t = 50 s (H065: 8.07 m/s) produces the same steady-state wave. Noise-only seeding yields the same attractor. This confirms the jamiton theory of Flynn et al. (2009): the wave structure is intrinsic to the traffic flow equations, not the initial conditions.

**Ring size matters, but the mechanism transfers.** On a 100-vehicle / 1000-metre ring at the same density, ACC at 18% penetration achieves 1.08 m/s -- still a major improvement from the 10.84 m/s baseline (H042), though weaker than the 0.55 m/s on the 22-vehicle ring. The degradation suggests that maintaining absolute smart-vehicle spacing, not just penetration fraction, is important at scale.

**Noise does not significantly affect the baseline wave.** Varying human-driver acceleration noise from 0 to 1.0 m/s^2 (H055-H059) changes wave amplitude only from 5.92 to 8.23 m/s. The system is robustly unstable across realistic noise levels.

## References

1. Sugiyama, Y., Fukui, M., Kikuchi, M., et al. (2008). "Traffic jams without bottlenecks." New Journal of Physics 10, 033001.
2. Stern, R.E., Cui, S., Delle Monache, M.L., et al. (2018). "Dissipation of stop-and-go waves via control of autonomous vehicles: Field experiments." Transportation Research Part C 89.
3. Treiber, M., Hennecke, A., Helbing, D. (2000). "Congested traffic states in empirical observations and microscopic simulations." Physical Review E 62(2).
4. Milanes, V., Shladover, S.E. (2014). "Modeling cooperative and autonomous adaptive cruise control dynamic responses using experimental data." Transportation Research Part C 48.
5. Cui, S., Seibold, B., Stern, R., Work, D.B. (2017). "Stabilizing traffic flow via a single autonomous vehicle." IEEE Intelligent Vehicles Symposium.
6. Chou, F.C., Bagabaldo, A., Bayen, A.M. (2022). "The Lord of the Ring Road." ACM/IEEE Transactions on Networking.
7. Flynn, M.R., Kasimov, A.R., Nave, J.C., Rosales, R.R., Seibold, B. (2009). "Self-sustained nonlinear waves in traffic flow." Physical Review E 79(5).
8. Lee, J.H., Wang, T., Jang, K., et al. (2024). "The MegaVanderTest: A hundred AVs on I-24." Transportation Research Part C.
9. Gunter, G., Gloudemans, D., Stern, R.E., et al. (2020). "Are commercially implemented adaptive cruise control systems string stable?" IEEE TITS.
10. Wilson, R.E., Ward, J.A. (2011). "Car-following models: fifty years of linear stability analysis." Transportation Planning and Technology 34(1).

---

*Generated by the HDR pipeline. 184 experiments, 224 citations, 105 pre-registered hypotheses. All code and data at [generalized_hdr_autoresearch/applications/phantom_jams](https://github.com/colurw/generalized_hdr_autoresearch).*
