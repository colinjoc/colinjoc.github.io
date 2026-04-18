---
title: "Did Irish fuel retailers profiteer in 2022? No."
date: 2026-04-19
domain: "Energy Economics"
blurb: "When Russia invaded Ukraine and pump prices exploded, everyone assumed Irish retailers were cashing in. We tested it properly."
weight: 21
tags: ["energy-economics", "fuel-prices", "ireland", "competition-policy", "null-result"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/irish_fuel_profiteering/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Irish pump prices did jump by more than the crude oil cost could explain after February 2022. But every other European country's prices jumped by the same amount at the same time. The 17-cents-per-litre "rip-off" that circulated in Irish headlines was a Europe-wide refining-margin widening, not an Irish retail conspiracy.

## The question

When Russia invaded Ukraine in February 2022, oil prices exploded and Irish pump prices followed within days. The Taoiseach hinted at "morally reprehensible" price-fixing. Politicians demanded action. The Competition and Consumer Protection Commission opened a review. The government cut excise duty by 20 cents per litre on petrol and 15 on diesel — the largest single-move tax cut in modern Irish history.

The question everyone wanted answered was simple. Did Irish fuel retailers use the chaos to widen their margins? We built a transparent, reproducible pump-price reconstruction and tested four concrete definitions of "profiteering" against the data.

## What we found

The naive answer says yes. If you predict Irish diesel prices from only two ingredients — the world price of crude and the euro-dollar rate — and you train on years of pre-war data, then ask what prices "should have been" after the invasion, Irish diesel ran about **17 cents per litre higher** than the simple model predicted, for years afterwards. That looked like a clear profiteering scandal.

![Irish diesel pre-tax price minus the simple model's prediction. Before 2022 the gap fluctuates around zero. After the invasion it sits stubbornly above the pre-shock band.](plots/baseline_residual_diesel.png)

Every meaningful control then shrinks or kills that number.

- Accept that pump prices lag crude with a delay, and the unexplained margin collapses to about 3 cents per litre on diesel and 1 cent on petrol.
- Build a "synthetic Ireland" from a weighted average of other European countries' diesel prices — Italy, the Czech Republic, Slovenia, Spain, and Bulgaria did most of the matching — and track it through the war. Real Ireland and synthetic Ireland move together. The remaining gap is about 3 cents per litre, and when we rerun the same test pretending each other European country was the one being investigated, we see gaps of similar or larger size in roughly a quarter of cases.
- The textbook "rockets and feathers" pattern — retailers raising prices fast but dropping them slowly — is not robust in our data. It flips sign under reasonable specification changes.
- The one statistic that looked like a smoking gun — a slower pass-through of crude price increases during the excise-cut window — reproduces in Germany at almost identical size. Germany never had the Irish excise cut. If the effect were Irish profiteering, Germany should show nothing.

![Real Ireland (black) versus synthetic Ireland built from European peers (red dashed). The two track each other closely all the way through the 2022 shock and beyond.](plots/e21_synthetic_control.png)

## Why that matters

The Irish public story of 2022 was a classic villain narrative. A global shock hits, local middlemen pocket a windfall. Our result is that the villain narrative, when you actually do the arithmetic against European peers, has almost nothing left in it. Irish diesel margins widened because European diesel margins widened — in Germany, the Netherlands, the Czech Republic, and Italy. What looked Irish was European, visible everywhere anyone cared to look.

This does not mean retailers behaved angelically. It means the right comparison is not "Ireland versus its own calm past". It is "Ireland versus its neighbours during the same weeks". An investigation that skips that step will find a villain every time there is a common European shock. The Competition and Consumer Protection Commission reached the same conclusion in November 2022 and was criticised for moving too quickly. The data says they were right.

## What it means in practice

**For Irish drivers and voters.** The 17-cents-per-litre rip-off figure that circulated during the crisis was not measuring what people thought it was measuring. The cost of a tank of diesel rose for reasons common to every European market. Frustrating, but not local wrongdoing.

**For competition regulators.** A credible profiteering monitor has to compare a country, in real time, to a synthetic version built from its European peers. We built exactly such a dashboard and it raises an alarm only when Ireland departs persistently from its cohort. As of this week, Ireland is sitting about 0.6 cents per litre above its European peers — well within normal variation.

![Live detector. Top panel: Ireland (black) versus its European-peer synthetic (red dashed). Middle panel: the gap between them. Bottom panel: a running tally that triggers an alarm when Ireland departs persistently from its peers.](plots/iran_detector_dashboard.png)

**For policymakers facing the next oil shock.** The Irish state has real levers if a fresh Middle East shock develops. A repeat of the March 2022 excise cut (20 cents per litre on petrol, 15 on diesel) would cost roughly 35 million euro a month at cut rates and — based on our analysis — would reach drivers rather than being captured by retailers. Pausing the annual carbon-component escalator saves about 2 cents per litre. Cutting the NORA strategic-reserve levy saves another 2 cents. EU law forbids VAT cuts on motor fuels, so that lever is off the table without a derogation. If the aim is to target the actual windfall beneficiaries, a coordinated EU refining-margin windfall tax (as implemented in Council Regulation 2022/1854) is the mechanism that matches what the data says is actually happening.

## How we did it

We combined the [European Commission's Weekly Oil Bulletin](https://energy.ec.europa.eu/data-and-analysis/weekly-oil-bulletin_en) with [Brent crude prices](https://finance.yahoo.com/quote/BZ=F/) and Irish tax schedules from [Revenue.ie](https://www.revenue.ie/en/companies-and-charities/excise-and-licences/excise-duty-rates/energy-excise-duty-rates.aspx), reconstructed the pump-price stack week by week from 2015 through early 2026, and subjected the post-invasion residual to four independent tests — asymmetric pass-through analysis, a synthetic-control comparison to European peers, a Germany placebo on the excise-cut window, and a structural-break search against an honest noise-distribution null.

## Further reading

- Competition and Consumer Protection Commission of Ireland (2022), fuel-market review — the contemporaneous official investigation.
- Abadie, Diamond, and Hainmueller (2010), "Synthetic Control Methods", *Journal of the American Statistical Association* — the peer-comparison method we used.
- UK Competition and Markets Authority (2023), road-fuel market study — the parallel investigation that documented Europe-wide refining-margin widening.
- [Full technical paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/irish_fuel_profiteering/paper.md) — all experiments, the live monitor specification, and the full Irish fuel-tax policy analysis.
