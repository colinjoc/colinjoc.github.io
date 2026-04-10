---
title: "HDR Methodology"
---

## Hypothesis-Driven Research

HDR is a systematic methodology for finding **novel solutions** to scientific and engineering problems. The search explores across the idea space, not just uphill from where it started. It applies to any domain where you can evaluate a hypothesis computationally — whether that's fitting a model to data or running a physics simulation.

### The Core Loop

Every experiment follows an 8-step cycle:

1. **Pick a hypothesis** from the research queue (highest-impact first)
2. **State a prior** — commit to a numerical probability before testing
3. **Articulate the mechanism** — WHY should this work? What's the causal story?
4. **Implement one change** — exactly one, isolated
5. **Evaluate** — run the simulation or model
6. **Record results** — every metric, no cherry-picking
7. **Update beliefs** — keep the change if it helped, revert if it didn't
8. **Update knowledge** — what did we learn? What new questions emerge?

### Why It Works

- **Literature review seeds many hypotheses** from different subfields — the search explores across the idea space, not just uphill from where it started
- **Negative results accumulate** — the knowledge base prevents retreading dead ends
- **Bayesian discipline** prevents both premature convergence and endless repetition
- **Isolation principle** identifies which ideas actually contribute

### Two Problem Types

**Dataset-based**: Train a predictor on known data, then use it for *discovery* — screening novel candidates, identifying non-obvious patterns. The model is infrastructure; the discovery is the result.

**Simulation-based**: Optimise designs via GPU-accelerated differentiable simulation. Find configurations that outperform published solutions under realistic physics constraints.

### The Key Principle

> **The goal is DISCOVERY, not model-fitting.** An R² of 0.95 on a known dataset is infrastructure. The novel result is what the model *finds*: new materials, new designs, new physical insights.

---

## Results

See the [Results Portfolio](/hdr/results/) for completed HDR projects.
