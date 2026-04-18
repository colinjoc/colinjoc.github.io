---
title: "What's actually blocking Irish housing — and what would fix it"
date: 2026-04-18
domain: "Irish Housing"
blurb: "Ireland needs to more than double its planning permissions to hit its housing target. Every other policy lever combined does not close the gap."
weight: 4
tags: ["housing", "ireland", "bottleneck-analysis", "policy", "synthesis", "flagship"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_housing_bottleneck/paper.md) and the [companion lever-interaction paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_lever_interactions/paper.md) have the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

*Part 4 of 4 in the Irish Housing series. Previous: [Part 1: Economics](/hdr/results/irish-housing-economics/) | [Part 2: Pipeline](/hdr/results/irish-housing-pipeline-complete/) | [Part 3: Planning and judicial review](/hdr/results/irish-planning-and-judicial-review/)*

**Bottom line.** Ireland grants about 38,000 residential planning permissions a year. It needs roughly 85,000 to hit its housing target. Every fix to every other step in the pipeline — faster planning appeals, fewer judicial reviews, lower lapse rates, better completion reporting — combined, closes less than a third of the gap. The binding constraint is permission volume, which is held down by development being economically unviable across most of the country. The honest achievable range, under a realistic policy package, is 42,000 to 49,000 completions a year.

## The question

Irish housing debate is a marketplace of hypothesised villains. Slow planning appeals. Judicial review. Lapsed permissions. Self-builders who never file completion certs. A supposedly under-powered national housing agency. Construction labour shortages. Each is said, somewhere, to be "the reason Ireland cannot build enough homes". So we asked: ranked by how many extra homes each fix would actually deliver, where does the constraint really sit?

## What we found

![Bottleneck ranking: extra homes delivered per year from each intervention.](plots/bottleneck_ranking.png)

- Granting 10,000 more planning permissions a year would add about 6,100 completions — roughly 37 percent of the 16,300-home annual shortfall. No other single lever comes close.
- Better completion-certificate filing would add about 3,270. Faster appeals at the planning board would add about 1,060. Removing judicial review entirely would add another 1,060. Halving the lapse rate would add about 700.
- Every efficiency fix combined adds roughly 5,000 completions a year, closing 31 percent of the gap. The remaining 69 percent requires more permissions and more construction capacity.
- Permission volume came out as the number-one constraint in every single one of 5,000 Monte Carlo simulations we ran to stress-test the ranking. It is not a borderline finding.
- The levers interact, but not the way intuition suggests. Cost-reduction levers — modular construction, value-added tax cuts, social-housing requirement reform — are purely additive among themselves. Their combined effect is exactly the sum of each alone.
- The real interaction is between cost reduction and workforce expansion. Cost levers generate demand for new building. Workforce expansion generates the capacity to build it. Neither works alone. Every combination that exceeds 50,000 completions a year includes workforce expansion.
- The best realistic combined package — modular construction, shorter build durations, a VAT reduction, reform of the social-housing requirement, and a 30 percent workforce expansion — gets Ireland from about 35,000 to roughly 45,000 to 47,000 completions a year. That is a 30-to-35 percent improvement. It is still short of the government's 50,500 target.

## Why that matters

The public debate about Irish housing lives almost entirely among the efficiency fixes. Planning appeals, judicial review, the housing agency's delivery record. These are real concerns and they do each add some completions. But even fixed together they do not close most of the gap. Ireland does not have a planning-processing problem so much as a permission-volume problem — and permissions are low because development is uneconomic across most of the country.

That reframes the question. It is not "how do we process applications faster". It is "why are so few applications filed in the first place?" The answer is that the numbers do not work outside Dublin. Construction costs, financing costs and developer margins, stacked together, exceed achievable sale prices in most of the country. Until the cost side of that equation moves — through modular construction, workforce expansion, or house prices simply rising faster than costs — no amount of planning-system reform will get Ireland to 50,500 homes a year.

## What it means in practice

**For policymakers.** Permission volume is the binding constraint. Interventions aimed at anything downstream of that are necessary but insufficient. The realistic near-term ceiling, even with a well-designed combined package, is 45,000 to 47,000 homes — probably not the 50,500 target. Setting expectations accordingly is itself an act of policy.

**For housing advocates.** The framing "judicial review is destroying housing supply" does not survive the numbers. Eliminating judicial review entirely would add about 1,060 completions a year, or 6.5 percent of the gap. Real, but modest.

**For developers and the construction industry.** Modular construction and workforce expansion are the two levers with the largest combined effect. Cost-reduction measures are genuinely additive — stacking them pays off linearly — but they do not work without a corresponding increase in capacity to actually build.

## How we did it

This synthesis consolidates findings from twenty predecessor studies covering pipeline yield, commencement rates, lapsed permissions, planning-board decision times, judicial-review rates under the Strategic Housing Development regime, delivery by the Land Development Agency, zoned-land conversion, development viability, infrastructure capacity, construction cost decomposition, policy-versus-market cost shares, and international cost comparison. We ranked every commonly-cited bottleneck by the marginal completions each fix would deliver, stress-tested the ranking with 5,000 Monte Carlo simulations, and ran 104,976 combinations of ten policy levers through a feedback model that passes cost reductions through to application rates, through permissions, through to completions.

## Further reading

- [Bottleneck ranking paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_housing_bottleneck/paper.md) — the formal ranking and sensitivity analysis.
- [Lever-interaction paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_lever_interactions/paper.md) — the 104,976-combination feedback model.
- The full twenty-study Irish Housing series is indexed on [GitHub](https://github.com/colinjoc/generalized_hdr_autoresearch/tree/main/applications).
