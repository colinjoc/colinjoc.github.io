---
title: "Which Housing Policy Combinations Actually Work?"
date: 2026-04-18
domain: "Irish Housing"
blurb: "We tested 104,976 combinations of 10 housing-policy levers through a feedback model (cost reduction → viability → applications → permissions → completions). The core finding: cost-reduction levers and workforce expansion are complements, not substitutes. No cost reduction alone exceeds the 35,000/yr construction ceiling. No workforce expansion alone generates demand. The achievable range under realistic assumptions is 42,000-49,000 completions/yr — short of the 50,500 HFA target — because workforce expansion faces diminishing returns and the viability-to-application elasticity saturates at positive margins."
weight: 2
tags: ["housing", "ireland", "policy-interaction", "multiplier", "capstone", "synthesis"]
---

*Capstone synthesis across 19 predecessor projects. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_lever_interactions/paper.md).*

## The question

We've studied every stage of the Irish housing pipeline across 19 projects. Each found the individual effect of a single lever. But **do levers interact?** Is the combined effect of faster planning + modular construction + VAT reduction greater than the sum of each alone?

## The feedback loop

Every lever feeds through the same chain:

```
Cost reduction → Viability margin improves → More applications filed
→ More permissions granted → More completions (capped at capacity)
```

The key insight: cost levers generate demand; workforce expansion generates capacity. **Neither works alone.**

## What we found

### Cost-reduction levers are additive — no synergy, no redundancy

When we tested all 45 lever-pairs for interaction effects, the gross interaction between cost-reduction levers is **exactly zero**. Each lever improves the viability margin independently. What looked like "redundancy" in the draft (-14,588 units for modular × CPO) was entirely a ceiling artifact — two levers pushing demand past the same capacity limit.

### Workforce expansion is the necessary complement

Every combination that reaches 50,000+ completions includes workforce expansion. Without it, the ceiling stays at ~35,000 regardless of cost reduction. But workforce expansion alone does nothing — there's no demand without viable projects.

### The achievable range is 42,000-49,000, not 50,500

The draft claimed 52,500 was achievable. The Phase 2.75 reviewer caught three problems:

1. **Workforce expansion has diminishing returns** — training time, supervision needs, site congestion. A tanh capacity model caps effective expansion at ~49,289, below the HFA target.
2. **The viability-to-application elasticity saturates** — r=0.91 was measured at negative margins. At positive margins, applications saturate (finite buildable sites). A tanh elasticity drops the best package from 167,810 to 50,925-91,702.
3. **General equilibrium** — if supply doubles, prices fall, margins compress. Not modelled, but acknowledged as a further downward adjustment.

**Realistic achievable range: 42,000-49,000 completions/yr** — a 20-40% improvement over current 35,000, but probably short of the 50,500 target.

![Package comparison: individual levers vs combinations. The "everything" package under diminishing returns reaches ~49,000, just short of HFA.](plots/package_comparison.png)

### The best realistic package

| Lever | Setting | Individual effect |
|:---|:---|---:|
| Modular construction | -20% hard costs | +5,473/yr |
| Duration reduction | -33% (32→21 months) | +1,888/yr |
| VAT reduction | 13.5% → 9% | +1,962/yr |
| Part V reform | 20% → 10% | +878/yr |
| Workforce expansion | +30% (realistic ceiling) | Lifts capacity to ~45,500 |
| **Combined (with feedback)** | | **~45,000-47,000/yr** |

This is the "radical but achievable" package. It gets Ireland from 35,000 to roughly 45,000-47,000 completions per year — a genuine improvement, but not the full 50,500.

### What would actually hit 50,500?

Either: (a) 50% workforce expansion WITH diminishing returns eliminated (unlikely), or (b) a fundamental shift in construction technology that reduces hard costs by 30%+ (modular at Swedish/Dutch scale), or (c) the demand side — house prices rise enough to make more counties viable without any cost reduction (already happening at ~8%/yr nationally, which gradually improves margins).

## What this does NOT establish

- **Not a forecast.** This is a parameter-propagation model, not a general-equilibrium simulation. Real-world dynamics (price response, migration, wage bargaining) are not modelled.
- **Not an optimisation.** We test combinations, not sequences. The order in which levers are pulled matters for transition dynamics.
- **Not a policy recommendation.** "Modular construction -20%" is a number, not a policy. How to achieve it (regulation, procurement reform, factory investment) is a separate question.

## The 19 projects behind this

This capstone draws parameters from: [bottleneck ranking](/hdr/results/irish-housing-bottleneck/) | [pipeline yield](/hdr/results/irish-housing-pipeline-e2e/) | [JR tax](/hdr/results/irish-jr-tax-on-supply/) | [commencement cohort](/hdr/results/irish-commencement-cohort/) | [lapsed permissions](/hdr/results/irish-lapsed-permissions/) | [ABP decision times](/hdr/results/irish-abp-decision-times/) | [zoned land](/hdr/results/irish-zoned-land-conversion/) | [viability frontier](/hdr/results/irish-viability-frontier/) | [infrastructure](/hdr/results/irish-infra-capacity/) | [cost decomposition](/hdr/results/irish-construction-costs/) | [policy vs market](/hdr/results/irish-policy-vs-market-costs/) | [international comparison](/hdr/results/irish-intl-construction-costs/) | and 7 others

## How we did it

Full factorial over 104,976 combinations of 10 levers, with feedback loop (viability → applications → permissions → completions). Monte Carlo with 10,000 draws propagating all predecessor CIs. Phase 2.75 reviewer mandated tanh elasticity saturation, diminishing workforce returns, and gross-interaction decomposition — all of which reduced the achievable range. Linear estimates presented as upper bounds throughout. Phase 3.5 signoff cleared.
