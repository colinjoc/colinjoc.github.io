---
title: "New York's Congestion Charge Worked -- and the Feared Displacement Never Showed Up"
date: 2026-04-10
domain: "Transport / Urban Policy"
blurb: "We checked whether Manhattan's congestion charge just pushed cars to outer boroughs. Three independent public datasets say no: the toll zone sees about 11% fewer vehicles than projected, subway use jumped, and bridge traffic into other boroughs barely moved."
weight: 5
tags: ["transport", "congestion-pricing", "nyc", "policy-evaluation", "displacement", "open-data"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/nyc_congestion/paper.md).*

## The Question

When New York City began charging most drivers $9 to enter Manhattan below 60th Street in January 2025, the immediate question from skeptics was straightforward: are you actually reducing traffic, or just pushing it somewhere else?

Early studies from the National Bureau of Economic Research (NBER) showed that road speeds inside the toll zone jumped 11-15%, and a separate study found a 22% drop in a key air pollution measure. But critics worried the improvements inside the cordon could come at the cost of worsened conditions in the Bronx, Brooklyn, Queens, and Staten Island. The Metropolitan Transportation Authority's (MTA) own forecasts had predicted increased traffic on outer-borough bridges as drivers rerouted around the toll zone.

We wanted to know whether the displacement was happening, and if the toll was genuinely removing car trips or merely shuffling them to someone else's neighborhood.

## What We Found

After 15 months of data, the displacement has not materialized.

The strongest evidence comes from the MTA's own count of vehicles entering the Congestion Relief Zone. About 490,000 vehicles cross the cordon each day -- roughly 11% fewer than the pre-toll projections of 550,000. This is not traffic rerouting; these are trips that simply stopped driving into lower Manhattan.

{{< figure src="plots/mta_ridership_trend.png" alt="MTA weekly ridership and bridge traffic around congestion charge launch" caption="Weekly subway ridership rose steadily after the charge launched in January 2025, while bridge and tunnel traffic remained flat -- no sign of drivers rerouting to avoid the toll." >}}

Three lines of evidence point in the same direction:

- **Subway and bus ridership rose.** Subway use jumped 9% in the first quarter compared to the same period a year earlier. Bus ridership rose 13%. Part of this reflects the continuing post-pandemic recovery -- subway use was still only at 71% of pre-pandemic levels entering 2025 -- but the growth rate was notably faster than in the following year (subway growth decelerated to 4% in Q1 2026), suggesting the charge gave a genuine one-time bump.

- **Bridge and tunnel traffic was flat.** If drivers were rerouting around Manhattan, you would see more cars on the Triborough, Whitestone, and Verrazzano bridges. Instead, bridge and tunnel volumes rose just 0.2% year-over-year in Q1. Bridge traffic had already fully recovered to pre-pandemic levels by 2024, so this flatness is not masking pandemic recovery -- it is a genuine null result for displacement.

- **Taxi and rideshare trips to the Central Business District (CBD) fell.** Across all taxi and for-hire vehicle types, pickups in the CBD dropped 4.4%, while pickups in the outer boroughs also declined (by 2.0%). If displacement were happening, you would expect outer-borough pickups to increase while CBD pickups fell. Instead, both went down, with CBD falling faster.

{{< figure src="plots/tlc_cbd_shift.png" alt="CBD trip share before and after congestion charge" caption="The share of taxi and rideshare trips starting in the CBD fell modestly (45.4% to 44.8%). Total trips declined overall, not just in the toll zone." >}}

## What Did Not Work

We initially tried to measure the effect using the city's Automated Traffic Recorder data -- fixed vehicle counters scattered across all five boroughs. This turned out to be a dead end. The counters do not cover the same locations consistently across weeks, one borough had no post-charge data at all, and another showed a 340% jump that turned out to be a new counter installation rather than a genuine traffic surge. A predictive model trained on this data explained only 6% of the variation in weekly volumes. The lesson: New York's open traffic count data is useful for long-term trends but too patchy for fine-grained before-and-after policy evaluation.

## What It Means

For the practical question -- did the congestion charge just move the problem? -- the answer through 15 months of data is no. The toll zone sees measurably fewer vehicles, transit use is up, and the outer boroughs have not absorbed displaced traffic. The early fears about rerouting to surrounding communities appear not to have materialised, at least at the scale detectable in bridge crossing data and trip records.

{{< figure src="plots/decomposition.png" alt="Decomposition of Manhattan traffic volume change" caption="Decomposition of observed changes: mode shift to transit and trip elimination are the detectable effects. Route displacement and time-of-day shifting are negligible." >}}

The bigger caveat is about attribution. Some of the transit ridership increase was already happening before the charge launched -- the subway had been recovering steadily since the pandemic. We cannot cleanly separate how much of the 9% subway bump came from the congestion charge versus the underlying recovery trend. What we can say is that the bridge and tunnel data -- which had already fully recovered to pre-pandemic levels -- shows no displacement signal, and the CRZ vehicle counts confirm approximately 11% fewer daily entries than projected.

## How We Did It

We assembled three independent public datasets: [NYC DOT Automated Traffic Volume Counts](https://data.cityofnewyork.us/Transportation/Automated-Traffic-Volume-Counts/7ym2-wayt) (210,000+ hourly records, 2023-2026), [MTA daily ridership and Congestion Relief Zone entry data](https://data.ny.gov/Transportation/MTA-Daily-Ridership-Data-2020-2025/vxuj-8kew) (including 456 days of direct CRZ vehicle counts), and [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) (46.6 million taxi and rideshare trips). We trained five model families on the traffic count data (the best achieved R-squared of only 0.06, confirming its unsuitability), ran a difference-in-differences analysis (inconclusive due to data quality), and triangulated across all three sources for the decomposition.

## Further Reading

- Cook, C. et al. "The Short-Run Effects of Congestion Pricing in New York City." NBER Working Paper 33584 (2025). [Link](https://www.nber.org/papers/w33584) -- the first comprehensive academic evaluation, finding 15% CBD speed gains and $14.3M/week in welfare benefits.
- Fraser, T. et al. "A first look into congestion pricing in the United States: PM2.5 impacts after six months of New York City cordon pricing." npj Clean Air (2025). [Link](https://www.nature.com/articles/s44407-025-00037-2) -- found 22% reduction in PM2.5 inside the toll zone.
- Eliasson, J. "A cost-benefit analysis of the Stockholm congestion charging system." Transportation Research Part A (2009). [doi:10.1016/j.tra.2008.11.014](https://doi.org/10.1016/j.tra.2008.11.014) -- the reference study from Stockholm, which found similar patterns: genuine trip reduction with limited displacement.

---

[HDR methodology](https://github.com/colinjoc/hdr_autoresearch) -- the framework and full project history
