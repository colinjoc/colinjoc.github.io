---
title: "What Actually Drives Irish Construction Costs: A Decade Decomposed"
date: 2026-04-18
domain: "Construction Economics"
blurb: "Irish residential construction costs rose about four percent per year between 2015 and 2024, and the headline number hides a 16-fold gap between the fastest and slowest-rising materials. When the totals are split apart, labour and materials grew at almost identical rates — overturning the popular claim that materials are the main cost problem — and Ireland's tougher energy-performance building rules do not appear to have pushed up the prices of the materials they regulate."
weight: 16
tags: ["ireland", "construction", "housing", "materials", "prices", "regulation"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_construction_cost_decomp/paper.md).*

## The Question

Ireland is building roughly one home for every three it needs. Every conversation about why eventually lands on cost: new homes are expensive to build, and the cost keeps rising. The usual short answer is "materials" — timber during the pandemic, steel and cement after the invasion of Ukraine, and stricter energy-efficiency rules on top. Each of those stories is plausible on its own, but together they leave the basic question unanswered: over a full decade, which bits of construction cost actually grew fastest, and which of the usual suspects really mattered?

We took the Central Statistics Office's monthly price index for forty building materials, plus its quarterly series on construction wages, and pulled the aggregate apart to see which components drove the 4 percent-a-year headline.

## What We Found

The single-number story — "construction costs rose four percent a year" — is close to right on average, and almost useless in practice. Underneath the average, materials behaved wildly differently from one another, and labour kept pace with materials almost to the decimal point.

- Structural steel rose 7.8 percent per year. Glass rose 0.5 percent per year. These are materials in the same buildings, over the same decade.
- Labour and materials grew at virtually the same rate over the full ten years (about 4.0 percent per year each). The gap between them was four hundredths of a percentage point.
- Of the 40 material price series, just three underlying factors explain 90 percent of the movement — essentially a common inflation tide, a minerals-versus-organics split, and a manufactured-goods-versus-bulk-commodities split.
- The structural frame — steel, cement, precast concrete — is the single largest contributor to annual cost growth, because it combines a big share of the bill with above-average inflation.
- Ireland's tougher energy-performance building rules, phased in from November 2019, did not visibly push up the prices of the materials they regulate. Materials outside the rules' scope inflated more than the regulated ones over the same period.

## Why That's Surprising

The widely repeated line is that materials costs are the problem, and that the pandemic and the war in Ukraine broke the construction-material supply chain in a lasting way. The data show something more specific. The pandemic really did double the price of timber for a while. The Ukraine shock really did push steel and cement up by a third. But over the full decade, wages in construction rose just as fast as the weighted basket of materials — and wage increases are smooth and persistent, while the material spikes have partly reverted. The materials narrative is the story of the two most dramatic years, not the story of the decade.

The result that was not expected at all concerns Ireland's Nearly Zero Energy Building standard, the regulation that from late 2019 required thicker insulation, triple glazing, and heat pumps in new homes. The intuitive expectation is that a regulatory demand shift would lift the prices of the affected materials. A simple before-and-after comparison appears to confirm this: insulation, glass, electrical fittings, and heating equipment all inflated faster after 2019 than before. But when compared against a control group of unregulated materials — cement, structural steel, plaster — the unregulated materials inflated even more. Once the pandemic and Ukraine effects are separated from the regulatory effect, the regulation itself does not show up as a price driver. Glass, the material with a triple-glazing mandate hanging over it, had the lowest inflation rate of any material in the basket.

## What It Means

If you are a homebuyer in Ireland, the most practical takeaway is that construction-cost inflation is not primarily a material-price problem that supply-chain normalisation will solve on its own. Roughly half of it is wages, driven by a persistent shortage of construction labour, and wage increases do not revert. The other half is dominated by the structural frame — steel and cement — where Irish builders are price-takers in global and domestic markets with limited short-run substitutes.

For policymakers, the analysis suggests two practical shifts. First, the debate about new energy-efficiency standards should probably focus on how much extra material each new home requires (thicker walls, a heat pump, triple-glazed windows) rather than on whether those materials became more expensive per unit — because the per-unit price effect appears to be absent. Second, any serious plan to bend the cost curve has to engage with labour supply and with the structural frame specifically; tweaking peripheral trades cannot move a number that is being driven by steel, concrete, and wages.

## How We Did It

We used the [Central Statistics Office Wholesale Price Index for Building and Construction Materials (WPM28)](https://data.cso.ie/table/WPM28), a monthly panel covering 40 material categories from January 2015 to September 2024, together with the [Central Statistics Office Earnings, Hours and Employment Costs Survey (EHQ03)](https://data.cso.ie/table/EHQ03) for construction-sector wages, and the Society of Chartered Surveyors Ireland's published cost-share weights that assign each material category a share of total hard cost. The analysis combined growth-rate rankings, a factor-structure analysis of the full price panel, a weighted-contribution calculation that multiplied each category's cost share by its inflation rate, formal tests for structural breaks at the pandemic and the Ukraine invasion, and a difference-in-differences comparison of regulated against unregulated materials around the 2019 rule change. All inputs are real public data — no synthetic series were used.

## Further Reading

- [Central Statistics Office Wholesale Price Index WPM28](https://data.cso.ie/table/WPM28) — the primary 40-material monthly index
- [Central Statistics Office Earnings Survey EHQ03](https://data.cso.ie/table/EHQ03) — the construction-sector wage series
- Rogan F et al (2021). *Impact assessment of Part L NZEB on construction costs*. Sustainable Energy Authority of Ireland — the official cost-uplift estimate for the energy-performance standard
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_construction_cost_decomp/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
