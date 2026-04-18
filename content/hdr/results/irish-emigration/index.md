---
title: "Australia quietly pulled level with the UK for Irish emigrants"
date: 2026-04-16
domain: "Irish Migration"
blurb: "For two centuries, leaving Ireland has meant leaving for Britain. In 2025, that stopped being true — or at least, stopped being obviously true."
weight: 12
tags: ["migration", "ireland", "emigration", "australia"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_graduate_emigration/analysis.py) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Irish emigration rose 37 percent between 2020 and 2024, topping out at 69,900 people before easing back to 65,600 in 2025. That is roughly five out of every six people who left in the 2012 crisis peak. But Ireland is still gaining more people than it loses — net migration was plus 59,700 in 2025. And for the first time on record, Australia received more Irish emigrants than the United Kingdom, though by a margin too thin to call structural.

## The question

Every few years the Irish emigration story comes back into the public conversation. The last big wave was the post-2008 financial crisis, which peaked at 83,000 people leaving in the year to April 2012. By the late 2010s, that had settled into the 50-to-55-thousand range. Something changed in the 2020s — housing got dramatically more expensive, wages stagnated in real terms, post-COVID lifestyle preferences shifted. We wanted to know by how much emigration has risen, where people are actually going, and — crucially — whether Ireland is losing population or still gaining it.

A scope note: the data source covers all ages. A graduate-specific analysis would need a separate higher-education survey and is not answered here.

## What we found

![Irish emigration 1987-2025 with destination breakdown 2010-2025. The 2012 historical peak is annotated; the current wave is approaching but not yet matching it.](plots/emigration_trajectories.png)

- Emigration rose 37 percent between 2020 and 2024, from 50,900 to 69,900, before easing back to 65,600 in 2025. The current wave is about 84 percent of the 2012 peak — closer to "crisis-adjacent" than to the financial crisis itself.
- Ireland remains net-receiving. In 2025, 125,300 people moved in and 65,600 moved out — a net gain of 59,700. The emigration story is about gross outflows, not population decline.
- Australia took in 13,500 Irish emigrants in 2025. The United Kingdom took in 12,600. That is the first time on record that Australia has been the number-one destination.
- The margin — 900 people — is inside the precision band of the underlying statistics, which carry roughly plus-or-minus 2,000 to 3,000 for small destinations. So "Australia ahead of the UK" is technically true but statistically a three-way tie at the top with the EU14 grouping (Germany, France, Netherlands and others) at 13,100.
- The trajectory is the real story. In 2023 the UK led Australia by about ten thousand people. By 2024 that was down to five thousand. In 2025 Australia crossed over. One more year of data will tell us whether this is a structural shift or a noisy single-year lead.
- Australia itself has grown from 2,500 Irish emigrants in 2021 to 13,500 in 2025 — more than fivefold in four years. Visa-route reforms on the Australian side, including an expanded skilled-worker programme and an age-extended working holiday agreement, are the widely-cited drivers.

## Why that matters

The "Ireland is emptying out" framing does not survive contact with the numbers. Ireland is growing through migration, not shrinking from it. The net picture has been unambiguously positive every year since 2020.

What has genuinely changed is the destination mix. For two centuries, leaving Ireland has meant, overwhelmingly, leaving for Britain. As recently as 2023, the UK took in more than double Australia's intake. In 2025, for the first time in the series that begins in 1987, that default broke. Whether it holds is an open question. The 2026 estimate will either confirm a structural shift away from the UK or show 2025 as a single-year blip.

## What it means in practice

**For prospective emigrants.** Australia, the UK and mainland Europe are effectively tied as the three most-chosen destinations, each receiving between 12,000 and 14,000 Irish arrivals in 2025. Australia's visa pathways have opened meaningfully since 2023 — the working holiday programme now runs to age 35, and the skilled-worker route has widened.

**For policymakers.** The absolute scale is serious but below 2012 crisis magnitude, and Ireland remains net-receiving. The destination mix is clearly diversifying away from the UK default, but the "Australia is now number one" framing should be treated as provisional until the 2026 numbers are in.

**For journalists.** "Exodus" language is not supported by the net-migration data. The honest frame is that gross emigration has risen sharply while immigration has risen faster, and that the historical pattern of Ireland-to-Britain is, perhaps, ending.

## How we did it

We used the Central Statistics Office's [Population and Migration Estimates table PEA18](https://data.cso.ie/table/PEA18), which records annual April-to-April migration by sex, flow direction and destination country from 1987 through 2025. We parsed the JSON-stat API response, computed total emigration and net migration series, compared Australia against the UK year by year for 2023-2025, and ranked 2025 destinations. The precision band on small-cell destination estimates comes from standard CSO guidance.

## Further reading

- [CSO Population and Migration Estimates (table PEA18)](https://data.cso.ie/table/PEA18) — the source dataset.
- [Full technical paper and code](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_graduate_emigration/analysis.py).
