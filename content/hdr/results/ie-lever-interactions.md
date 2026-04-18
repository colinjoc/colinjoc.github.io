---
title: "Why Stacking Housing Policies Does Not Multiply Their Effect"
date: 2026-04-18
domain: "Housing and Policy"
blurb: "Irish housing debate often assumes that combining several cost-cutting reforms — cheaper land, lower taxes, faster planning, modular building — would compound into a much larger effect than any single measure. A systematic analysis of ten such levers finds the opposite. Each new cost cut mostly generates demand that the construction industry cannot actually build, because the binding constraint is the number of available workers, not the price of a home."
weight: 10
tags: ["ireland", "housing", "policy", "construction", "workforce", "modelling"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_lever_interactions/paper.md).*

## The Question

Ireland's housing plan asks for 50,500 new homes each year. The country has been delivering around 35,000. The conventional wisdom in the policy debate is that closing the gap needs a mix of levers: faster planning, cheaper land through compulsory purchase, reduced value added tax, modular factory-built construction, lower finance costs, and several others. The unstated hope is that stacking these measures on top of one another will compound — that a combination of four or five will produce more homes than the sum of the individual effects.

We wanted to test that assumption directly. Taking ten of the most-discussed policy levers, we ran every combination of their settings — 104,976 in total — through a calibrated model of the Irish housing pipeline, and asked whether the levers really do reinforce one another, interfere with one another, or act independently.

## What We Found

The cost levers do not reinforce one another. They act almost purely additively on demand for new homes, and most of that demand runs into a wall.

- Cost-cutting measures, combined, do not produce more than the sum of their parts. They produce exactly the sum of their parts in terms of demand.
- The construction industry can currently build roughly 35,000 homes per year. Every lever that reduces the cost of a home pushes demand above that ceiling; the ceiling then truncates nearly all of the gain.
- The only combination that genuinely multiplies — where two levers together deliver much more than the sum of each alone — is any cost lever paired with expansion of the construction workforce.
- Workforce expansion on its own does nothing. The ceiling rises, but without cost reduction the extra capacity sits unused. Cost reduction on its own also does nothing, because there is nobody extra to build the homes that now make financial sense.
- The largest apparent "redundancy" in the analysis — land purchase reform combined with modular construction appearing to cancel each other out — is not an economic effect. It is a mathematical artifact of both levers independently pushing demand above an already-saturated capacity ceiling.
- Reaching 50,500 homes a year requires roughly 80,000 extra construction workers. At current training and immigration rates, that would take about 16 years. At an ambitious rate never achieved historically, it would take 4 years.

## Why That's Surprising

The expected answer — and the implicit logic behind most policy bundles being debated — is that cost cuts compound. If one reform makes a scheme 5 percent cheaper and a second reform makes it another 8 percent cheaper, the combined effect should make some previously unviable schemes viable that neither reform would have reached alone, producing an extra boost. The model does include that mechanism. But the extra demand this creates has nowhere to go. The industry's workforce, equipment, and site capacity cannot absorb more than about 35,000 homes a year at present, and every extra euro of viability simply increases the queue of permitted-but-unbuilt schemes.

The second surprise is how symmetric the finding is across all ten levers. It is not a quirk of a particular lever; every cost lever in the basket has the same property. Planning reform, modular construction, tax cuts, compulsory land purchase, developer-margin compression — all of them generate demand that exceeds capacity, and all of them fail to translate that demand into built homes without a complementary expansion of the workforce. The distinction usually drawn between "supply-side reforms" and "demand-side reforms" collapses: every cost lever is a demand-side reform in practice, because it increases demand for construction services from an industry that is already at capacity.

The third surprise concerns the demand response itself. The model assumes that as building becomes more viable, more projects come forward, in the same proportion as has been seen historically. That assumption is tested by shrinking the response as viability improves — because there is a finite number of sites, developers, and planners. Under a realistic degree of saturation, even the maximum policy package produces about 92,000 completions per year instead of 168,000; under strong saturation, only about 51,000, barely above the target. The precise headline number depends heavily on an assumption that has never been tested at high viability margins, so the most reliable way to read the analysis is qualitative: without more workers, no package delivers.

## What It Means

For anyone following housing policy, the most practical implication is that a single-lever approach — "cut value added tax on new homes" or "abolish Part V" — cannot by itself shift completions. Neither can a five-lever bundle without workforce expansion. The capacity constraint is where all cost-side policies converge and stall.

For policymakers designing plans, the analysis points to a specific structure. Every successful package needs one lever from the capacity side (workforce, and the training, immigration, and productivity arrangements behind it) and one or more from the cost side. The most cost-efficient three-lever combination identified in the analysis combines modular construction, land-cost reform, and workforce expansion. Plans that stack cost levers without touching capacity produce headlines but not homes.

For the public debate, a more uncomfortable implication follows. Reaching the target of 50,500 homes per year requires roughly 80,000 additional construction workers — a large fraction of the current workforce of 160,000. There is no combination of planning reform, tax cuts, or technology deployment that substitutes for that labour. The honest timeline is years, not months, and the honest lever is whichever combination of apprenticeship, immigration, productivity, and retention adds workers fastest.

## How We Did It

The analysis drew every input parameter from a chain of preceding empirical studies of the Irish housing system: pipeline duration, development-cost components, viability margins, planning-approval rates, build yields from granted permissions, and construction-sector capacity. We built a calibrated model of the pipeline from cost through viability through application through permission through completion, evaluated it across every combination of ten lever settings, propagated uncertainty through Monte Carlo simulation, and tested the results against two alternative model specifications — a hard capacity ceiling where completions simply stop at the workforce limit, and a soft ceiling where exceeding capacity raises costs. We then checked the sensitivity of the headline numbers to whether the demand response stays linear at high viability margins or saturates. All inputs are from public sources; no synthetic data was used.

## Further Reading

- [Central Statistics Office — New Dwelling Completions](https://data.cso.ie/) — the current completions series
- Department of Housing, Local Government and Heritage (2021). *Housing for All: A New Housing Plan for Ireland* — the 50,500 target
- SOLAS (2022). *Construction Skills Forecasting* — the workforce recruitment baseline used in the scenarios
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_lever_interactions/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
