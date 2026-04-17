---
title: "Irish Grocery Inflation: Sugar Up 51 Percent, Beef Up 48, Milk Up 39"
date: 2026-04-17
domain: "Consumer Economics"
blurb: "Across 74 Irish food categories, prices rose a median 19 percent between early 2022 and early 2026. The top of the distribution is much more extreme — sugar +51 percent, beef +48, chocolate +46, whole milk +39, butter +38 — and roughly half of those high-inflation categories are Irish-produced goods, not imports caught up in global commodity markets."
weight: 11
tags: ["ireland", "inflation", "food-prices", "cost-of-living", "consumer"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_grocery_drift/paper.md).*

## The Question

Irish households feel noticeably worse off at the checkout than they were four years ago. The official headline inflation rate tells part of the story, but it averages thousands of goods and hides which specific items moved most. Is it a broad rise, or is the pain concentrated in a handful of categories? And is this just global commodity inflation passing through Irish shelves, or is there something more local at work?

## What We Found

The rises are heavily concentrated, not evenly spread.

| Category | 2022 to 2026 price change | Real change after wages |
|---|---|---|
| Cane and beet sugar | **+51 percent** | +33 percent |
| Beef | +48 percent | +30 percent |
| Chocolate and cocoa | +46 percent | +28 percent |
| Whole milk | +39 percent | +21 percent |
| Butter | +38 percent | +20 percent |
| Fresh meat (all) | +36 percent | +18 percent |
| Bottled water | +36 percent | +18 percent |
| Soft drinks | +35 percent | +17 percent |
| Eggs | +33 percent | +15 percent |

Across the full set of 74 food and non-alcoholic-beverage subcategories, the typical item rose 19 percent in nominal terms. Irish average weekly earnings grew roughly 18 percent over the same window — so the *average* grocery basket is roughly treading water against wages, but the dispersion inside it is enormous. A household heavy on sugar, beef, chocolate, milk, butter, or bottled water is paying 15 to 33 percentage points more in real terms than wages delivered. A household heavy on fresh fruit or jams is approximately flat.

A second finding reframes the whole shock: in the four years *before* the crisis — 2016 to 2020 — sugar had *fallen* 15 percent, beef had fallen 6 percent, chocolate had fallen 16 percent, and bread, fresh meat, water, and eggs had all got cheaper. This is not a speed-up of a pre-existing trend. It is a clean break from what economists would have called the "cheap food decade".

## Why That's Surprising

The common explanation for Irish food inflation is imported commodity inflation: the 2022 invasion of Ukraine, the sugar-and-cocoa futures rallies, the energy spike. That story fits sugar and chocolate — both are globally-priced inputs, and their Irish shelf-price moves are roughly consistent with global futures.

It does not fit the rest of the list. **Whole milk, butter, bottled water, soft drinks, and eggs are not imported.** Irish milk is produced on Irish farms and bottled in Irish dairies. Irish bottled water comes from Irish springs. Yet these categories rose 33 to 39 percent — as much as the globally-determined ones. An imported-commodity-inflation story cannot account for the locally-produced half of the list.

There are plausible local explanations — energy pass-through into refrigeration and processing, a 30-percent rise in the statutory minimum wage over the same period, packaging costs, and the "sellers' inflation" hypothesis that firms widened margins under cover of cost shocks — but disentangling them would require factory-gate price data that the public series do not publish.

## What It Means

For an Irish household: aggregate food inflation looks roughly wage-matched, but the contents of the shopping trolley determine whether that average applies to you. A trolley that over-indexes on the nine categories above is delivering a double-digit *real* cost-of-living hit that wages have not compensated for. A trolley built around fresh fruit, jams, or seafood has been much closer to flat in real terms.

For a policy observer: the shock is not simply a Ukraine-and-energy story. Roughly half of the most-inflated categories are locally produced, and their rises are comparable to the globally-determined half. Policy discussion focused only on imported shocks is missing most of the picture.

For a retailer or supplier: the dispersion across categories is large enough that the "food inflation" aggregate is a poor guide to any specific product. Sugar, beef, and chocolate belong in one bucket; milk, butter, and water in a different bucket with a different causal story.

## How We Did It

We used [Consumer Price Index table CPM24](https://data.cso.ie/table/CPM24) from the Central Statistics Office, which publishes the Irish consumer price index at the 344-commodity subcategory level, monthly from 1996. We restricted to the 74 food and non-alcoholic-beverage subcategories, computed the four-year price change from January 2022 to January 2026, and tested its stability by sliding the start and end dates across a six-month window on each side. We compared against the equivalent 2016-to-2020 baseline period and deflated by approximate Central Statistics Office wage growth over the shock period. Categories were flagged as globally or locally determined based on whether they trade as world commodities.

## Further Reading

- [Central Statistics Office Consumer Price Index table CPM24](https://data.cso.ie/table/CPM24) — the 344-subcategory monthly index
- [Central Statistics Office Average Weekly Earnings series](https://www.cso.ie/en/statistics/earnings/earningsandlabourcostsquarterly/) — the wage-deflator source
- Weber and Wasner (2023). Sellers' Inflation, Profits and Conflict — the "sellers' inflation" hypothesis
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_grocery_drift/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
