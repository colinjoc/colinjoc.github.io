---
title: "How much does planning really cost Irish housing supply?"
date: 2026-04-18
domain: "Irish Housing"
blurb: "Planning appeal times doubled. Judicial reviews multiplied. Both are real problems. The question is whether either one is actually the binding constraint."
weight: 3
tags: ["housing", "ireland", "planning", "judicial-review", "ABP", "SHD", "LRD"]
---

*A plain-language summary. The [full technical paper set](https://github.com/colinjoc/generalized_hdr_autoresearch/tree/main/applications) — four linked studies — has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

*Part 3 of 4 in the Irish Housing series. Previous: [Part 1: Economics](/hdr/results/irish-housing-economics/) | [Part 2: Pipeline](/hdr/results/irish-housing-pipeline-complete/) | Next: [Part 4: What would fix it](/hdr/results/irish-housing-bottleneck-and-levers/)*

**Bottom line.** An Bord Pleanála — Ireland's planning appeals board — saw decision times nearly double from 23 weeks in 2018 to 42 weeks by 2024. Compliance with the 18-week statutory target collapsed from 69 percent to 25 percent. Twenty-two judicial reviews under the now-retired Strategic Housing Development regime directly held up about 7,000 homes for a combined 105,000 unit-months. Those are real costs. But translated into the national completions target, restoring the board to its statutory pace would add about 1,060 homes a year, and eliminating judicial review entirely would add another 1,060. That is real, and it is about 13 percent of the annual shortfall.

## The question

Two complaints dominate Irish housing debate. First, that An Bord Pleanála takes far too long to decide appeals. Second, that judicial review — the High Court procedure for challenging a planning decision — has ground the system to a halt. Both claims have a factual core. The question we wanted to answer is how much each actually costs Ireland in completed homes, compared to the other things that go wrong in the pipeline.

## What we found

![Planning board decision times and statutory-objective compliance over time.](plots/abp_decision_times.png)

- The mean time for An Bord Pleanála to decide a planning case rose from 23 weeks in 2018 to 42 weeks in 2023-2024. Only a quarter of cases met the 18-week statutory objective in 2024, down from 69 percent in 2019.
- At the peak, in 2022, the board was taking in cases 45 percent faster than it could clear them. That is an accounting relationship — several causes overlapped, including board-member resignations, pandemic disruption, a shift in case mix, and defensive processing under judicial-review pressure.
- There is early evidence of recovery. Quarterly 2025 data shows decision times back to around 25 to 30 weeks, with compliance at roughly 60 percent.
- Under the Strategic Housing Development regime — the fast-track apartment-scheme process that ran from 2017 to 2021 — the State lost 14 of 16 judicial reviews decided in 2018-2021. That is an 87.5 percent loss rate. Most were quashed for material contravention of a local development plan.
- The 2021 replacement regime, called Large-scale Residential Development, was partly intended to cut the judicial-review rate. Three years on, only two such judicial reviews have been decided, and the evidence is not yet there to say whether the reform worked. A clean comparison needs another two years of data.
- Totalling the direct judicial-review effect, 22 cases under the old regime held up about 7,000 homes for 105,000 unit-months combined — equivalent to 8,800 homes delayed by a year. Indirect effects (defensive processing spillovers) cannot be separated cleanly from the same aggregate data.
- Restoring the planning board to its 18-week statutory pace would add 1,060 completions a year. Eliminating judicial review entirely would add another 1,060. Against an annual shortfall of 16,300 homes, that is 13 percent.

## Why that matters

The "judicial review is destroying housing supply" framing is popular in the Irish debate. The data shows something more specific. Judicial review does cost homes — several thousand units directly, and more indirectly. But it is not the binding constraint on national output. Removing it entirely would add about 1,060 homes a year, or about 6.5 percent of the gap. The planning board's slowdown has a similar magnitude. Together, fully fixing the planning system closes around 13 percent of Ireland's housing shortfall.

The other 87 percent lives upstream — in the question of how many permissions developers actually file, which is governed by whether development is economically viable. The planning system is a cost. It is not the binding constraint.

## What it means in practice

**For policymakers.** Planning reforms are worth doing but will not, on their own, close the housing gap. The numbers are a couple of thousand homes a year, not fifteen thousand. Speeches framing planning reform as the primary solution should be discounted accordingly.

**For developers.** The planning board's recovery in 2025 is real. The judicial-review pipeline remains uncertain — the Large-scale Residential Development regime is not yet clearly safer than its predecessor. Budgeting for the possibility of a High Court challenge on larger schemes remains prudent.

**For housing advocates arguing that judicial review should be curtailed.** The direct cost is real, at 7,000 homes delayed for roughly a year apiece. The indirect cost is harder to pin down. But even the most aggressive plausible estimate puts the total at about 6.5 percent of the annual shortfall. It is a lever worth using; it is not the main lever.

## How we did it

This synthesis consolidates four linked studies. We used [An Bord Pleanála's published decision times](https://www.pleanala.ie/) to track the 2018-2024 slowdown and compliance with the 18-week objective. We catalogued every decided judicial review under the Strategic Housing Development regime from Courts Service records, coded the outcome and the number of units affected for each, and summed unit-months of delay. We ran a counterfactual simulation of what national completions would have looked like if the planning board had held its statutory pace throughout, capped at realistic construction-capacity ceilings.

## Further reading

- [An Bord Pleanála](https://www.pleanala.ie/) — the planning appeals board whose decision times are tracked here.
- [Planning board decision-time study](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_abp_decision_times/paper.md).
- [Strategic Housing Development judicial-review study](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_shd_judicial_review/paper.md).
- [Judicial-review cost on housing supply](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_jr_tax_on_supply/paper.md).
