---
title: "Why Irish planning appeals slowed to a crawl, then started moving again"
date: 2026-05-08
domain: "Public administration / Planning policy"
blurb: "An Irish planning appeal took 18 weeks in 2017 and 42 weeks by 2023. Most of the slowdown landed in a single year — and the recovery is now visible."
weight: 35
tags: ["public-administration", "planning-policy", "ireland", "queueing", "open-data", "abp"]
---

*A plain-language summary. The [full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_abp_decision_times/paper.md) has the diagnostics and experiment logs. See [About HDR](/hdr/) for how this work was produced and reviewed.*

**Bottom line.** Ireland's national planning appeals body, An Bord Pleanála (ABP), saw average decision time more than double between 2017 and 2023, with most of the deterioration concentrated in a single year. By late 2025 the share of decisions delivered on time had climbed from a low of around one in four back to roughly three in four. The trajectory is robust; the standard explanation — overloaded capacity — fits the arithmetic but cannot, with only ten years of national data, be told apart from a handful of plausible alternatives.

## The question

An Bord Pleanála is the national board that decides planning appeals in Ireland. If your local council refuses your house extension, or approves a neighbour's apartment block over your objection, ABP is where the appeal is heard. Since 1992 it has worked to a Statutory Objective Period (SOP) — a target, not a legal deadline — of 18 weeks for most appeals. Through the mid-2010s the Board hit that target on roughly seven decisions in ten. By 2024 it was hitting it on one in four. The June 2025 reconstitution of the body as An Coimisiún Pleanála (ACP), under the Planning and Development Act 2024 (PDA-2024), inherited a backlog and a credibility problem at once.

Press coverage and political commentary blamed everything from missing Board members to judicial-review (JR) challenges to a 2018 IT transition. We pulled the Board's own annual reports back to 2015 and the 2024 and 2025 quarterly statistics, and asked: which of those stories does the actual numerical record support, and how confidently can we say so given that we only have one observation per year?

## What we found

![Mean weeks to dispose and on-time-decision share, ABP 2015–2024](plots/abp_decision_times.png)
<figcaption>Mean weeks to dispose of a planning case (left, blue) and the share of cases meeting the statutory objective (right, orange), ABP 2015–2024.</figcaption>

The mean time to dispose of a case rose from 18 weeks in 2017 to 26 weeks in 2022, then jumped to 42 weeks in 2023 and stayed there through 2024. The share of cases delivered within the statutory target fell from 64 percent in 2017 to 25 percent in 2024. The 2018–2021 period looks, on closer inspection, less like a rising trend than a one-off level shift after a 2018 step-up. The real collapse landed almost entirely in one year, 2022 to 2023.

The simplest accounting summary tracks a single ratio: cases coming in divided by cases going out. In 2022 ABP took in 1.45 cases for every one it disposed of. In 2023 the ratio was almost exactly one. In 2024 it fell to 0.74 — meaning the Board was, for the first time in three years, eating into its backlog faster than new cases arrived. The 2025 monthly statistics show the on-time share rising every month from January through September, climbing from around four cases in ten to closer to eight in ten.

That arithmetic is consistent with a queueing-theory description: when arrivals exceed service capacity, queues lengthen; when capacity catches up, queues drain. The harder question is whether capacity is what actually moved. With only ten years of national totals, the data cannot rule out two plausible alternatives. One is that a string of Supreme Court decisions in 2018 and 2019 — *Connelly v An Bord Pleanála* and *Balz v An Bord Pleanála* — required Board inspectors to write longer, more legally defensible reasons for each decision, slowing per-case throughput from inside the office. The other is that the cases themselves got harder, with a heavier mix of large infrastructure and Strategic Housing Development (SHD) files. A formal decomposition of the case mix between 2018 and 2024 attributes essentially all of the decision-time rise to within-case-type slowdowns and almost none to a shift in mix — which rules the third explanation out, but cannot separate the first two.

The case-type variation underneath the headline is enormous. In 2024 the small residual cohort of Strategic Housing Development cases — a fast-track regime for large apartment schemes that ran from 2017 to 2021 — averaged 124 weeks to dispose, with a typical (median) case nearer 79 weeks and a long upper tail running well past two years. The successor regime, Large-scale Residential Development (LRD), averaged 13 weeks. The SHD figure is constructed from a small cohort of 40 stragglers from a closed legislative regime; it should be read as "how long did the long-tail cases take to clear" rather than a generic SHD speed.

The 2025 recovery is real but the forward projection is fragile. We tested a simple capacity-based forecast against the actual 2025 first-quarter and third-quarter compliance figures. It got the first quarter roughly right and missed the third quarter by about 51 percentage points — under-predicting the recovery. The Board is now disposing of cases faster per staff member than the pre-crisis calibration assumed, probably because the freshly seated Board cohort has stabilised. Under a Monte Carlo sensitivity sweep across plausible parameter values, the projected 2028 on-time rate ranges from near zero to over 60 percent across all three policy scenarios we considered — status quo, a 20 percent staffing increase, and the new PDA-2024 statutory framework. None of the three scenarios' typical projections return ABP to its pre-2018 regime by 2028.

## Why that matters

Planning timelines have material consequences. A residential developer pays interest on land and construction loans for every week a permission is delayed; a community waits longer to know whether an objection has succeeded; an infrastructure project — a wind farm, a bus corridor, a desalination plant — sits in limbo. Ireland's housing crisis is bound up with planning throughput, and 2022 and 2023 saw the appeal stage become, briefly, the slowest part of the pipeline.

The political conversation around the slowdown has cycled through several explanations: missing Board members, the IT transition, governance failures uncovered by the 2022 Farrell preliminary report and the 2022 Indecon organisational capacity review, the rise of judicial review, the SHD fast-track regime, the courts' 2022 Planning and Environment List. The aggregate national record is consistent with all of these and inconsistent with none of them. It rules out only one story — that the case mix simply got harder — and it locates the deterioration tightly in time, in 2022 and 2023. Anything more granular requires case-level data the Board does not currently publish.

## What it means in practice

**For applicants.** The recovery is genuine and visible in the monthly numbers. The headline 124-week figure for SHD reflects a small cohort of legacy stragglers, not the speed of the current LRD pipeline, which is averaging 13 weeks. Standard appeals in 2024 averaged 41 weeks, against an 18-week target — still well behind objective, but visibly improving through 2025.

**For planning authorities.** The single most useful diagnostic the agency could publish is a case-level, per-stage timeline: when each file was assigned to an inspector, when the inspector's report was complete, when the Board considered it, when the decision issued. With only annual aggregates the public record cannot tell whether 2022's slowdown was a Board-capacity problem, a reasoning-burden problem, or a complexity problem. The decision is descriptively a queue; the queue's bottleneck is invisible from the outside.

**For policymakers.** None of the three forward scenarios — status quo, +20 percent staffing, or the new PDA-2024 framework — has a typical projection that returns the agency to its pre-2018 on-time regime by 2028, and the uncertainty bands are wide enough that the status-quo scenario beats the PDA-2024 scenario in roughly one Monte Carlo draw in five. The headline on-time rate will also rise mechanically once the new statutory timelines come into force, because some categories will shift to longer targets — that is a definition change, not a throughput improvement, and it is worth tracking the two separately.

## How we did it

We assembled a 2015 to 2024 annual series from An Bord Pleanála's Annual Report appendices, plus the 2024 and 2025 quarterly casework statistics, and hand-verified every numerical cell against the source PDFs (n = 10 annual observations for the headline series; the 2015 and 2016 figures are documented as chart read-offs from a single bar chart, with a sensitivity refit on 2017 to 2024 leaving the trajectory unchanged). Five model families were fit to the year-level mean-weeks series; an interrupted-time-series specification with breaks at 2018, 2022 and 2023 had the lowest in-sample and leave-one-year-out cross-validated error, though we report the cross-validated number alongside the in-sample one because the break years were chosen ex post from the narrative rather than discovered blind. A capacity-queueing forecast was tested out-of-sample against the 2025 first-quarter and third-quarter compliance figures; the under-prediction of the third-quarter recovery is reported plainly. A formal decomposition rules out case-type mix as the dominant driver of the 2018 to 2024 rise.

## Further reading

- [Full technical paper](https://github.com/colinjoc/hdr_autoresearch/blob/main/applications/ie_abp_decision_times/paper.md) — full series, model tournament, leave-one-year-out cross-validation, decomposition, Monte Carlo sensitivity, and out-of-sample 2025 validation.
- An Bord Pleanála Annual Reports 2018–2024 and Quarterly Planning Casework Statistics — primary source data, available at the [ABP statistics page](https://www.pleanala.ie/en-ie/statistics/quarterly-statistics).
- Simons G. *Planning and Development Law* (3rd ed., Round Hall, 2019) — the standard Irish reference on the statutory framework, including the legal status of the SOP target.
- Indecon. *Organisational Capacity Review of An Bord Pleanála* (2022) — independent review commissioned during the 2022 governance crisis.
