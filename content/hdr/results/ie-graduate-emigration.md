---
title: "The year Australia pulled level with the UK for Irish emigrants"
date: 2026-04-17
domain: "Migration"
blurb: "The UK has been Ireland's default emigration destination for a century. In 2025, for the first time on record, that quietly stopped being true."
weight: 16
tags: ["ireland", "migration", "emigration", "australia"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_graduate_emigration/paper.md) has the precision bands and policy-lever mapping. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Irish emigration rose 37 percent between 2020 and 2024 before easing slightly in 2025 — approaching, but not matching, the 2012 post-crash peak. And in 2025 Australia narrowly beat the United Kingdom as the top destination for the first time on record, though by a margin that sits inside the statistics' precision band. Meanwhile Ireland, on net, is still gaining people.

## The question

Every few years the Irish emigration story returns. The last major wave was the post-2008 financial crisis, when 83,000 people left in the year to April 2012. That wave receded, and by the late 2010s emigration had settled at 50,000 to 55,000 a year. Something changed in the 2020s. The question is by how much, where people are going, and whether Ireland is actually losing population as a result.

## What we found

Emigration is up sharply — but Ireland is still net-receiving people.

- Emigration rose from 50,900 in 2020 to 69,900 in 2024, a 37 percent increase, before easing to 65,600 in 2025.
- The 2024 peak is 84 percent of the 2012 crisis peak of 83,000 — approaching but not matching it.
- In every year from 2020 to 2025, immigration exceeded emigration. Net migration in 2025 was +59,700. In 2024 it was +79,300.
- The destination mix has shifted. Australia took 13,500 emigrants in 2025 versus 12,600 to the United Kingdom — the first time on record Australia has exceeded the UK.
- Australia has grown roughly fivefold since 2021, from 2,500 emigrants to 13,500.
- The 900-person gap between Australia and the UK sits inside the statistics' precision band of roughly two to three thousand, so the honest reading is "statistical tie at the top", not "structural shift".

## Why that matters

The UK was the default Irish emigration destination for most of a century. The proximity, the Common Travel Area, English as a shared language, and decades-deep diaspora networks all pointed to it as the natural first stop. For Australia to pull level — even narrowly, even for one year — is a reshaping of a migration pattern that had been remarkably stable since the 1950s.

The second surprise is the ongoing net-positive picture. Public narrative around the "new emigration wave" tends to assume Ireland is shrinking. It is not. The country added almost 80,000 people on net in 2024 and almost 60,000 in 2025. The outflow is real and comparable to the crisis years. The inflow is larger still.

The third surprise is how much of the Australia shift can be traced to specific policy levers rather than macro push factors. The Australian skilled-visa expansion of 2022, the Working Holiday programme's 2024 age extension, and a 2023 visa-threshold salary reset each coincide with year-on-year jumps in the Irish flow. This is not a story of Ireland pushing people out — it is at least partly a story of Australia pulling them in.

## What it means in practice

**For prospective emigrants.** Australia, the UK, and the pre-2004 EU grouping (Germany, France, the Netherlands and the rest) are effectively tied as the three most-chosen destinations, each receiving 12,000 to 13,000 Irish emigrants in 2025. Australia's pathway has become progressively more accessible since 2023 and is now as mainstream a choice as the UK.

**For policymakers.** The absolute outflow is serious but below 2012-crisis magnitude, and Ireland remains net-receiving. The diversification of destinations away from the UK default is genuine. The "Australia is number one" framing should be treated as provisional until a second year of data either confirms or reverses the 2025 crossover.

**For anyone reading the numbers.** The precision of the published destination series is about two to three thousand for small cells, so year-to-year rankings among the top three should be read as ranges rather than exact ordering.

## How we did it

The [Central Statistics Office PxStat table PEA18](https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/PEA18/JSON-stat/2.0/en) publishes annual April-to-April migration estimates by flow (immigration, emigration, net) and destination or origin region, covering 1987 to 2025. We downloaded the machine-readable version, built total-emigration and net-migration time series, and compared Australia against the UK year by year from 2023 to 2025. The cited precision band comes from the Central Statistics Office's own guidance on small-cell estimates in the PEA family.

The project directory name refers to "graduate" emigration because of the original framing; the actual data are all-ages. A graduate-specific breakdown would require the Higher Education Authority's Graduate Outcomes Survey and is a separate study.

## Further reading

- [Central Statistics Office PEA18 migration estimates](https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/PEA18/JSON-stat/2.0/en) — the primary source data.
- [Central Statistics Office Population and Migration Estimates](https://www.cso.ie/en/statistics/population/populationandmigrationestimates/) — the official release with narrative context.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_graduate_emigration/paper.md).
