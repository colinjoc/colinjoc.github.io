---
title: "Did Irish petrol stations profiteer during the 2022 energy crisis? No."
date: 2026-04-17
domain: "Energy Economics"
blurb: "When the Ukraine war sent fuel prices soaring, Irish drivers and politicians alike accused retailers of pocketing the shock. A careful reconstruction of the Irish pump-price stack finds the headline excess margin is real in arithmetic but disappears once Ireland is compared to its European peers. The Irish margin widened because every European margin widened."
weight: 35
tags: ["energy", "fuel-prices", "ireland", "competition-policy", "null-result"]
---

*This is a short summary. For the full technical write-up, see the [detailed paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/irish_fuel_profiteering/paper.md).*

## The Question

In March 2022, two weeks after the invasion of Ukraine, Irish fuel retailers raised pump prices by an amount the public considered far larger than the rise in crude oil could justify. The Taoiseach called them out by name. A parliamentary committee hauled them in. Fuels for Ireland, the trade body, pushed back. The Competition and Consumer Protection Commission investigated and reported, in November 2022, that it found no evidence of coordinated pricing — but no full public reconstruction of the pump price, showing what proportion of the increase was genuinely unexplained margin, had ever been published for Ireland.

We built one. Using eleven years of weekly prices — crude oil, the euro-dollar exchange rate, Irish excise schedules, the European Union's weekly oil bulletin — we tested four concrete definitions of "profiteering" against the Irish retail diesel and petrol series.

## What We Found

The naive answer says yes: after the shock, Irish diesel carried about seventeen cents per litre of margin that a simple cost-stack model could not explain. But every meaningful control makes that number shrink or disappear.

- Adding realistic dynamics to the price model — accepting that pump prices chase crude with a lag — collapses the unexplained margin to about three cents per litre on diesel and one cent on petrol.
- Comparing Ireland to a carefully constructed synthetic version of itself built from the European Union's other 27 member states shrinks the gap to under three cents per litre, which is not statistically different from zero against a placebo.
- The textbook "rockets and feathers" asymmetry — the claim that retailers raise prices fast but drop them slowly — is not robust in our data. It flips sign when the model is specified differently.
- The one interaction effect that looked like a smoking gun — a reduced pass-through of crude increases during Ireland's excise-cut window — reproduces in Germany at almost identical magnitude.
- The largest apparent structural break in Irish prices is within the range of breakpoints you would expect to find in the pre-shock era just by chance.

## Why That's Surprising

The Irish public story of 2022 was a classic "villain story": global shocks hit, local middlemen pocket a windfall. Our result is that the villain story, when you actually do the arithmetic against European peers, has almost nothing left in it. Irish diesel margins widened because European diesel margins widened — in Germany, in the Netherlands, in the Czech Republic, in Italy. What looked like Irish profiteering was European refining-and-retail margin widening, visible everywhere anyone cared to look.

This does not mean retailers behaved angelically. It means that the right null hypothesis for an Ireland-specific profiteering investigation is not the historical Irish price itself; it is the contemporaneous European peer. An investigation that skips that step will find a villain every time there is a common European shock.

## What It Means

For consumers, the frustrating news is that the "£17-cents-per-litre of rip-off" number that circulated in 2022 was not really measuring what people thought it was measuring. The cost of a tank of diesel rose for real reasons common to every European market.

For competition regulators and future price-gouging inquiries, there is a concrete design lesson. Watching your own country's prices against its own history will flag a false alarm whenever a continent-wide shock hits. A credible Ireland-specific monitor has to compare Ireland, in real time, to a synthetic Ireland built from its peers. Only when Ireland departs from that peer group is there a signal worth investigating. We propose exactly such a design for the ongoing Middle East tensions.

For economists, the paper reinforces the Competition and Consumer Protection Commission's November 2022 conclusion with a transparent, publicly reproducible dataset and a concrete methodology that future studies can adopt.

## How We Did It

We combined the [European Commission's Weekly Oil Bulletin](https://energy.ec.europa.eu/data-and-analysis/weekly-oil-bulletin_en) with [Brent crude prices](https://finance.yahoo.com/quote/BZ=F/) and Irish tax schedules from [Revenue.ie](https://www.revenue.ie/en/companies-and-charities/excise-and-licences/excise-duty-rates/energy-excise-duty-rates.aspx), reconstructed the pump-price stack week by week from 2015 to 2026, and then subjected the post-invasion residual to four independent tests: asymmetric pass-through analysis, a margin-versus-counterfactual comparison using a synthetic version of Ireland built from its European peers, an examination of the 2022 excise-cut episode, and a structural-break search with an honest noise-distribution null.

## Further Reading

- Competition and Consumer Protection Commission of Ireland (2022), fuel-market review
- Abadie, Diamond, and Hainmueller (2010), "Synthetic Control Methods" — *Journal of the American Statistical Association*
- Fuest, Neumeier, and Stöhlker (2024), pass-through of European fuel taxes
- UK Competition and Markets Authority (2023), road-fuel market study
- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/irish_fuel_profiteering/paper.md)

---

📂 **[HDR methodology](https://github.com/colinjoc/hdr_autoresearch)** — the framework and full project history
