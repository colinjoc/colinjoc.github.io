---
title: "NYC's Congestion Charge Worked -- the Feared Displacement Never Came"
date: 2026-04-12
domain: "Transport / Urban Policy"
blurb: "We checked whether Manhattan's new congestion charge just pushed cars to outer boroughs. Three independent public datasets covering 15 months say no: about 11% fewer vehicles enter the toll zone than projected, subway use jumped, and bridge traffic to other boroughs barely budged."
weight: 25
tags: ["transport", "congestion-pricing", "nyc", "policy-evaluation", "displacement", "open-data"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/nyc_congestion/paper.md).*

## The Question

When New York City began charging most drivers $9 to enter Manhattan below 60th Street in January 2025, skeptics raised a straightforward objection: are you actually reducing traffic, or just pushing it somewhere else? If drivers simply rerouted across the Triborough, Whitestone, or Verrazzano bridges to avoid the toll, the Bronx, Brooklyn, Queens, and Staten Island would absorb the problem Manhattan shed.

Early academic studies were encouraging -- road speeds inside the toll zone jumped, and air pollution dropped measurably. But no one had directly tested whether the outer boroughs were paying the price. The Metropolitan Transportation Authority's own forecasts had predicted increased traffic on outer-borough bridges. We set out to answer that displacement question using three independent, freely available public datasets covering 15 months after the charge launched.

## What We Found

After 15 months of data, the feared displacement has not materialized. The strongest evidence comes from the MTA's direct count of vehicles crossing the toll cordon: about 490,000 per day, roughly 11% fewer than the pre-toll projection of 550,000. These are trips that stopped happening, not trips that went somewhere else.

{{< figure src="plots/mta_ridership_trend.png" alt="MTA weekly ridership and bridge traffic around congestion charge launch" caption="Weekly subway ridership rose steadily after the charge launched in January 2025, while bridge and tunnel traffic remained flat -- no sign of drivers rerouting to avoid the toll." >}}

- **Bridge and tunnel traffic was flat.** Volumes rose just 0.2% year-over-year in the first quarter -- effectively zero. If drivers were rerouting, you would see a clear jump here.

- **Subway use jumped 9% and bus use jumped 13%** compared to the same quarter a year earlier. Some of this reflects ongoing post-pandemic recovery, but the growth rate was notably faster than the following year, suggesting the charge gave a genuine one-time bump.

- **Taxi and rideshare trips to the toll zone fell 4.4%**, while outer-borough pickups also declined (by 2.0%). If displacement were happening, outer-borough pickups should have risen. Instead, both dropped, with the toll zone falling faster.

- **Peak-hour driving patterns barely changed.** The share of Manhattan traffic during rush hours shifted less than one-tenth of a percentage point, because the toll's broad charging window (5 AM to 9 PM) leaves little incentive to reschedule.

- **The city's own fixed traffic counters were too patchy to use.** A predictive model trained on those counters explained only 6% of the variation in weekly volumes, confirming that this data source is unsuitable for fine-grained policy evaluation.

{{< figure src="plots/tlc_cbd_shift.png" alt="CBD trip share before and after congestion charge" caption="The share of taxi and rideshare trips starting in the Central Business District fell modestly (45.4% to 44.8%). Total trips declined overall, not just in the toll zone." >}}

## Why That's Surprising

The conventional fear -- shared by transit experts, local politicians, and the MTA's own traffic models -- was that a cordon charge would act like squeezing a balloon: push down on Manhattan and traffic bulges out everywhere else. Stockholm and London, the two most-studied cordon pricing programs, had shown displacement effects early on, and outer-borough communities in New York mobilized against the charge partly on this basis.

What actually happened was different. Instead of rerouting, people either switched to the subway or simply stopped making the trip. The bridge and tunnel data is especially telling because bridge traffic had already fully recovered to pre-pandemic levels by 2024 -- so the flat line is not masking a pandemic recovery effect. It is a genuine null result for displacement. The bus ridership surge turned out to be transient (it reversed a year later), but the subway shift and trip elimination appear durable through the available data window.

{{< figure src="plots/decomposition.png" alt="Decomposition of Manhattan traffic volume change" caption="Decomposition of observed changes: mode shift to transit and trip elimination are the detectable effects. Route displacement and time-of-day shifting are negligible." >}}

## What It Means

For anyone who commutes through New York, the practical takeaway is that the congestion charge appears to be doing what it was designed to do: fewer cars in lower Manhattan, more people on trains, and no measurable cost imposed on the outer boroughs. About 60,000 fewer vehicles per day enter the toll zone than officials originally projected, and that reduction is not showing up as extra traffic on the bridges.

The bigger caveat is attribution. The subway was already recovering from pandemic-era lows, and we cannot cleanly separate how much of the 9% ridership bump came from the charge versus the underlying trend. What we can say is that the displacement worry -- the central argument opponents used against the policy -- finds no support in 15 months of bridge crossing data, transit ridership figures, or 46.6 million taxi and rideshare trip records.

## How We Did It

We assembled three independent public datasets: [NYC DOT Automated Traffic Volume Counts](https://data.cityofnewyork.us/Transportation/Automated-Traffic-Volume-Counts/7ym2-wayt) (210,000+ hourly records from 2023 to 2026), [MTA daily ridership and Congestion Relief Zone entry data](https://data.ny.gov/Transportation/MTA-Daily-Ridership-Data-2020-2025/vxuj-8kew) (including 456 days of direct vehicle counts at the toll cordon), and [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) (46.6 million taxi and rideshare trips). We ran five model families on the traffic counter data, a difference-in-differences analysis comparing Manhattan to outer boroughs, and a multi-source decomposition that separated the observed changes into mode shift, route displacement, time-of-day shift, and trip elimination. The key finding -- no displacement -- emerged consistently across all three data sources.

## Further Reading

- Cook, C. et al. "The Short-Run Effects of Congestion Pricing in New York City." NBER Working Paper 33584 (2025). [Link](https://www.nber.org/papers/w33584) -- the first comprehensive academic evaluation, finding 15% speed gains in the Central Business District and $14.3 million per week in welfare benefits.
- Fraser, T. et al. "A first look into congestion pricing in the United States: PM2.5 impacts after six months of New York City cordon pricing." npj Clean Air (2025). [Link](https://www.nature.com/articles/s44407-025-00037-2) -- found a 22% reduction in fine particulate pollution inside the toll zone.
- Eliasson, J. "A cost-benefit analysis of the Stockholm congestion charging system." Transportation Research Part A (2009). [doi:10.1016/j.tra.2008.11.014](https://doi.org/10.1016/j.tra.2008.11.014) -- the reference study from Stockholm, which found similar patterns of trip reduction with limited displacement.
- [Detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/nyc_congestion/paper.md) -- the full technical write-up with all data tables and methodology details.

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
