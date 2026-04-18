---
title: "New York's congestion charge — where did the traffic go?"
date: 2026-04-12
domain: "Transport / Urban Policy"
blurb: "Critics said Manhattan's congestion charge would just push traffic to the outer boroughs. Fifteen months of data are now in."
weight: 25
tags: ["transport", "congestion-pricing", "nyc", "policy-evaluation", "displacement", "open-data"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/nyc_congestion/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Three independent public datasets covering the first 15 months of the Manhattan congestion charge all tell the same story. About 11 percent fewer vehicles enter the toll zone than the city had projected, subway use jumped, and bridge traffic to the outer boroughs barely moved. The feared displacement did not arrive.

## The Question

When New York City began charging most drivers nine dollars to enter Manhattan below 60th Street in January 2025, the sceptics' line was straightforward. Are you really reducing traffic, or just pushing it somewhere else? If drivers simply rerouted across the Triborough, Whitestone, or Verrazzano bridges, the Bronx, Brooklyn, Queens, and Staten Island would absorb whatever Manhattan shed.

Early evaluations were encouraging — road speeds inside the toll zone jumped, and air pollution dropped measurably. But nobody had directly tested whether the outer boroughs were paying the price. The Metropolitan Transportation Authority's own forecasts had predicted more traffic on outer-borough bridges. We set out to answer the displacement question using three independent, freely available public datasets covering 15 months after the charge launched.

## What we found

The feared spillover has not materialised. The cleanest evidence is the MTA's direct count at the toll cordon itself: about 490,000 vehicles a day, roughly 11 percent below the pre-toll projection of 550,000. Those are trips that stopped happening, not trips that went somewhere else.

{{< figure src="plots/mta_ridership_trend.png" alt="MTA weekly ridership and bridge traffic around congestion charge launch" caption="Weekly subway ridership rose steadily after the charge launched in January 2025, while bridge and tunnel traffic remained flat — no sign of drivers rerouting to avoid the toll." >}}

- Outer-borough bridge and tunnel volumes rose just 0.2 percent year-on-year in the first quarter — effectively zero. If drivers were rerouting, this is where it would show up.
- Subway use jumped 9 percent and bus use jumped 13 percent over the same quarter a year earlier. Some of this is pandemic recovery, but the growth rate was faster than the following year, suggesting the charge gave a genuine one-time bump.
- Taxi and rideshare trips into the toll zone fell 4.4 percent — and outer-borough pickups also dropped, by 2 percent. If displacement were happening, outer-borough pickups would have risen. Instead, both dropped, with the toll zone falling faster.
- Peak-hour patterns inside Manhattan barely shifted. The charging window runs from 5 in the morning to 9 at night, which leaves little incentive to reschedule.
- The city's own fixed traffic counters turned out to be too patchy to use. A model trained on them explained only 6 percent of weekly volume — confirming that this particular data source is unsuitable for fine-grained evaluation.

{{< figure src="plots/tlc_cbd_shift.png" alt="CBD trip share before and after congestion charge" caption="The share of taxi and rideshare trips starting in the Central Business District fell modestly. Total trips declined overall, not just in the toll zone." >}}

## Why that matters

The conventional fear — shared by transit experts, local politicians, and the MTA's own traffic models — was that a cordon charge would behave like a squeezed balloon. Push down on Manhattan, traffic bulges out everywhere else. Stockholm and London had shown early displacement effects, and outer-borough New York had mobilised against the charge partly on that basis.

What actually happened was different. Instead of rerouting, people either switched to the subway or simply stopped making the trip. The bridge data is especially telling because outer-borough bridge traffic had already fully recovered to pre-pandemic levels by 2024 — so the flat line is not masking a pandemic recovery. It is a genuine null result for displacement. The bus ridership surge proved transient (it reversed a year later), but the subway shift and the trip elimination appear durable through the available data window.

{{< figure src="plots/decomposition.png" alt="Decomposition of Manhattan traffic volume change" caption="Decomposition of observed changes: mode shift to transit and trip elimination are the detectable effects. Route displacement and time-of-day shifting are negligible." >}}

## What it means in practice

**For New York commuters and residents.** The congestion charge is doing what it was designed to do: fewer cars in lower Manhattan, more people on trains, and no measurable cost imposed on the outer boroughs. About 60,000 fewer vehicles per day enter the toll zone than officials originally projected, and those missing vehicles are not showing up on the bridges.

**For policymakers in other cities.** The central argument opponents used against the policy — the displacement claim — finds no support in 15 months of bridge crossing data, transit ridership figures, or 46.6 million taxi and rideshare trip records. Stockholm and London patterns replicate in a much denser, more car-dependent North American context.

**For evaluators and journalists.** Be careful with attribution. The subway was already recovering from pandemic-era lows, and the 9 percent ridership bump cannot be cleanly split into "charge effect" versus "underlying trend". What is clean is the null: across three independent data sources, the displacement worry does not appear.

## How we did it

We assembled three independent public datasets: [NYC DOT Automated Traffic Volume Counts](https://data.cityofnewyork.us/Transportation/Automated-Traffic-Volume-Counts/7ym2-wayt) (more than 210,000 hourly records from 2023 to 2026); [MTA daily ridership and Congestion Relief Zone entry data](https://data.ny.gov/Transportation/MTA-Daily-Ridership-Data-2020-2025/vxuj-8kew) (including 456 days of direct vehicle counts at the toll cordon); and [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) (46.6 million taxi and rideshare trips). We ran a difference-in-differences comparison between Manhattan and the outer boroughs, and a multi-source decomposition separating the observed changes into mode shift, route displacement, time-of-day shift, and trip elimination. The no-displacement finding emerged consistently across all three sources.

## Further reading

- Cook, C. et al. (2025). ["The Short-Run Effects of Congestion Pricing in New York City"](https://www.nber.org/papers/w33584), NBER Working Paper 33584 — the first comprehensive academic evaluation, finding 15 percent speed gains in the Central Business District.
- Fraser, T. et al. (2025). ["A first look into congestion pricing in the United States: PM2.5 impacts after six months of New York City cordon pricing"](https://www.nature.com/articles/s44407-025-00037-2), *npj Clean Air* — found a 22 percent reduction in fine particulate pollution inside the toll zone.
- Eliasson, J. (2009). ["A cost-benefit analysis of the Stockholm congestion charging system"](https://doi.org/10.1016/j.tra.2008.11.014), *Transportation Research Part A* — the reference Stockholm study, which found similar patterns of trip reduction with limited displacement.
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/nyc_congestion/paper.md) — all data tables and methodology.
