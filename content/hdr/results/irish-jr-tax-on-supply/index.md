---
title: "The Judicial-Review Tax on Irish Housing Supply"
date: 2026-04-17
domain: "Irish Housing"
blurb: "Twenty-two Strategic Housing Development judicial reviews decided 2018-2022 directly delayed approximately 7,000 housing units for a combined 105,504 unit-months (sensitivity range 85k-150k). If An Bord Pleanála had maintained its 18-week statutory objective throughout, a counterfactual simulation suggests 7,421-16,638 additional completions over 2018-2024 — the range reflecting a construction-capacity ceiling that limits how fast delayed units can convert. The indirect channel (JR pressure → defensive ABP decision-making → slower all-case processing) cannot be point-identified from aggregate data; we report it as an attribution range, not an estimate."
weight: 19
tags: ["housing", "ireland", "judicial-review", "policy-evaluation", "counterfactual"]
---

*Plain-language summary. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_jr_tax_on_supply/paper.md). Synthesis of three predecessor projects: [SHD judicial review](/hdr/results/irish-shd-judicial-review/), [LRD vs SHD](/hdr/results/irish-lrd-vs-shd-jr/), [ABP decision times](/hdr/results/irish-abp-decision-times/).*

## The question

Judicial review of planning decisions is sometimes cited as a major drag on Irish housing delivery. But "major" needs a number. **How many housing units were actually delayed, and for how long?**

We distinguish two channels:
- **Direct**: schemes whose permissions were quashed or suspended by judicial review
- **Indirect**: all housing cases slowed because ABP decision times doubled from 23 to 42 weeks under JR pressure + capacity constraints

## What we found

### Direct JR delay: ~105,000 unit-months from 22 SHD-era cases

Across 22 SHD-era judicial reviews decided 2018-2022, approximately 7,000 housing units were directly affected. The five largest cases accounted for 45% of the total delay. 2020 was the peak year (10 JRs decided, ~59,000 unit-months). The sensitivity range — reflecting 13 of 22 cases requiring unit-count imputation — is 85,000-150,000 unit-months.

In holding-cost terms: EUR 52.8M at the lower bound (finance costs only), up to EUR 158M including construction-cost inflation during delay.

### Counterfactual completions gap: 7,421-16,638 units

If ABP had maintained 18-week statutory-objective compliance throughout 2018-2024, a counterfactual simulation estimates 7,421-16,638 more completions over the period. The upper bound (16,638) assumes no construction-capacity constraint; the lower bound (7,421) reflects a ~35,000/yr ceiling on Ireland's construction throughput — you cannot complete units faster than the sector can build them, regardless of how fast ABP decides.

![Left: direct JR delay by decision year — 2020 dominates (10 JRs decided that year). Right: counterfactual completions gap (shaded band) if ABP had maintained 18-week SOP.](plots/jr_tax.png)

### The indirect channel is real but unquantifiable from this data

ABP decision times doubled over exactly the period that JR pressure was highest (2020-2023). But three other factors overlapped: the board-member crisis (2022 resignations), COVID disruption (2020-2021), and IT-system transitions. At 10 annual observations with 4+ concurrent shocks, we cannot statistically separate the JR contribution.

We report the indirect channel as an **illustrative attribution range** (0%, 25%, 50% of ABP excess delay attributed to JR) — not a central estimate. The paper is explicit that 25% is a midpoint of ignorance, not a finding.

## What this does NOT establish

- **Not causation for the indirect channel.** The aggregate data cannot separate JR-induced defensive behaviour from board-capacity constraints and other concurrent shocks.
- **Not a "JR costs X homes" claim.** The counterfactual measures *delay*, not *prevention*. Most JR'd schemes eventually proceeded (some via re-application).
- **Not LRD-era.** Only 2 LRD-era JRs were decided by end-2024 (per the companion [LRD project](/hdr/results/irish-lrd-vs-shd-jr/)). The ongoing JR tax under LRD is below the detection floor.
- **Not endogenous.** The counterfactual assumes developers would have filed at the same rate under faster ABP processing; in reality faster processing might have induced more applications, narrowing the gap.

## What it means

For policymakers: the direct JR delay is concentrated in a small number of large Dublin schemes and the 2020 peak year. The "JR as housing blocker" narrative is directionally right but quantitatively modest — 105,000 unit-months is equivalent to about 8,800 units delayed for one year, against a national delivery of ~175,000 completions over 2018-2024. The indirect channel is probably larger but is not measurable from published data.

For reform design: the three highest-leverage interventions are (1) costs-rule reform (the one-way Aarhus costs rule makes JR filing near-free), (2) faster JR resolution via the Planning and Environment List, and (3) sustained ABP staffing to keep ρ below 1.0.

## How we did it

Linked OPR Appendix-2 case data (22 SHD-era JRs with unit counts and delay durations) to ABP annual reports (2018-2024 decision-time and SOP-compliance series). Counterfactual simulation calibrated to observed intake under maintained 18-week SOP, with construction-capacity ceiling from CSO completions data. Imputation sensitivity analysis (±25%) on the 13 cases without published unit counts. Full HDR pipeline with independent Phase 2.75 blind reviewer (7 mandated experiments, counterfactual halved by capacity ceiling, 6 numerical inconsistencies corrected) and Phase 3.5 signoff.
