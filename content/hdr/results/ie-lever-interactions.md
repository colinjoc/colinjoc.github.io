---
title: "You cannot cost-cut your way to 50,500 Irish homes a year"
date: 2026-04-18
domain: "Housing and Policy"
blurb: "Cut the tax, cheapen the land, speed up planning, factory-build the walls. Stack all ten levers together — and Ireland still builds roughly the same number of homes."
weight: 10
tags: ["ireland", "housing", "policy", "construction", "workforce", "modelling"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_lever_interactions/paper.md) has the parameter table and the Monte Carlo sensitivity runs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Ireland's housing debate assumes that bundling together cheaper land, lower taxes, faster planning, and modular construction will compound into a large supply response. Tested across every combination of ten such levers, it does not. Every cost cut just generates demand the construction industry cannot actually build, because the binding constraint is workers, not price.

## The Question

Ireland's housing plan asks for 50,500 new homes each year. The country has been delivering around 35,000. The conventional wisdom is that closing the gap requires a mix of levers: faster planning, cheaper land through compulsory purchase, reduced value added tax, modular factory-built construction, lower finance costs. The unstated hope is that stacking these on top of one another will compound — that a combination of four or five will produce more homes than the sum of the individual effects.

We wanted to test that assumption directly. Taking ten of the most-discussed policy levers, we ran every combination of their settings — 104,976 in total — through a calibrated model of the Irish housing pipeline, and asked whether the levers really do reinforce one another, interfere with one another, or act independently.

## What we found

The cost levers do not reinforce each other. They act almost purely additively on demand for new homes, and most of that demand runs into a wall.

- Cost-cutting measures, combined, do not exceed the sum of their parts. They hit it exactly — on paper — and then the construction industry cannot absorb the demand.
- The industry can build roughly 35,000 homes a year at current capacity. Every lever that reduces the cost of a home pushes demand above that ceiling, and the ceiling truncates nearly all of the gain.
- The only combination that genuinely multiplies is any cost lever paired with expansion of the construction workforce. Cost cuts and workforce growth, together, build more homes than either alone.
- Workforce growth on its own does nothing. The ceiling rises, but without cost reduction the extra capacity sits unused. Cost reduction on its own also does nothing, because nobody extra is available to build the homes that now make financial sense.
- The biggest apparent "redundancy" — land purchase reform and modular construction appearing to cancel each other out — is not an economic effect. Both levers independently push demand above an already-saturated ceiling.
- Reaching 50,500 homes a year requires roughly 80,000 additional construction workers. At current training and immigration rates, that takes about 16 years. At an ambitious rate never achieved historically, about four.

## Why that matters

The expected answer — and the implicit logic behind most policy bundles being debated — is that cost cuts compound. If one reform makes a scheme 5 percent cheaper and a second makes it another 8 percent cheaper, the combined effect should make previously unviable schemes viable. The model does include that mechanism. But the extra demand has nowhere to go. The industry's workforce, equipment, and site capacity cannot absorb more than about 35,000 homes a year, and every extra euro of viability simply lengthens the queue of permitted-but-unbuilt schemes.

The second surprise is how symmetric the finding is across all ten levers. It is not a quirk of a particular one. Every cost lever in the basket has the same property. Planning reform, modular construction, tax cuts, compulsory land purchase, margin compression — all of them generate demand that exceeds capacity, and all of them fail to translate that demand into built homes without more workers. The usual distinction between "supply-side" and "demand-side" reforms collapses: every cost lever is a demand-side reform in practice, because it increases demand for construction services from an industry already at capacity.

The third surprise concerns the demand response itself. The model assumes that as building becomes more viable, more projects come forward, at roughly historical proportions. That assumption is tested by shrinking the response as viability improves, because there is a finite number of sites, developers, and planners. Under realistic saturation, even the maximum policy package produces about 92,000 completions per year instead of 168,000. Under strong saturation, only about 51,000, barely above the target. The precise headline number depends heavily on an assumption that has never been tested at high viability margins, so the reliable way to read the analysis is qualitative: without more workers, no package delivers.

## What it means in practice

**For anyone following housing policy.** A single-lever approach — "cut value added tax on new homes" or "abolish Part V" — cannot by itself shift completions. Neither can a five-lever bundle without workforce expansion. The capacity constraint is where all cost-side policies converge and stall.

**For policymakers designing plans.** Every successful package needs one lever from the capacity side — workforce, training, immigration, productivity — and one or more from the cost side. The most cost-efficient three-lever combination combines modular construction, land-cost reform, and workforce expansion. Plans that stack cost levers without touching capacity produce headlines, not homes.

**For the public debate.** Reaching the 50,500-home target requires roughly 80,000 additional construction workers — a large fraction of the current workforce of 160,000. There is no combination of planning reform, tax cuts, or technology that substitutes for that labour. The honest timeline is years, not months, and the honest lever is whichever combination of apprenticeship, immigration, productivity, and retention adds workers fastest.

## How we did it

We drew every input parameter from a chain of preceding empirical studies of the Irish housing system: pipeline duration, development-cost components, viability margins, approval rates, build yields, and construction-sector capacity. We built a calibrated model of the pipeline from cost through viability through application through permission through completion, evaluated it across every combination of ten lever settings, propagated uncertainty through Monte Carlo simulation, and tested the results against two alternative specifications — a hard capacity ceiling where completions simply stop at the workforce limit, and a soft ceiling where exceeding capacity raises costs. We then checked whether the headline numbers survive if the demand response saturates at high viability margins. All inputs come from public sources; no synthetic data was used.

## Further reading

- [Central Statistics Office — New Dwelling Completions](https://data.cso.ie/) — the current completions series.
- Department of Housing, Local Government and Heritage (2021). *Housing for All: A New Housing Plan for Ireland* — the 50,500 target.
- SOLAS (2022). *Construction Skills Forecasting* — the workforce recruitment baseline used in the scenarios.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_lever_interactions/paper.md).
