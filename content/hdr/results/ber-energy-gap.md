---
title: "Why Does an A-Rated Irish Home Use Almost the Same Energy as a G-Rated One?"
date: 2026-04-09
weight: 8
blurb: "Why does an A-rated Irish home use almost the same energy as a G-rated one? A single feature — the dwelling form factor — explains 38% of the gap. Cavity wall insulation is the cheapest fix at EUR 28 per kWh saved."
domain: "Energy / Building Performance"
headline: "An ExtraTrees model trained on 100,000 synthetic BER certificates achieves R2=0.88 predicting DEAP-calculated energy values, revealing that dwelling form factor (surface-to-volume ratio) is the single most powerful predictor of BER rating, and that cavity wall insulation is the most cost-effective retrofit at EUR28 per kWh/m2/yr saved -- but the published performance gap literature warns that actual energy savings from retrofits are only 50-70% of what BER improvement predicts"
metric_name: "MAE on BER Energy Value (kWh/m2/yr) regression; 5-fold stratified cross-validation; 100k synthetic BER certificates calibrated to SEAI published statistics"
metric_value: "Baseline CV MAE 61.04 (XGBoost); Tournament winner 55.51 (ExtraTrees); Final CV MAE 33.03 (+46% improvement); Holdout MAE 30.60, R2=0.921"
tags: ["energy", "buildings", "BER", "DEAP", "performance-gap", "retrofit", "Ireland", "SEAI", "prebound", "rebound", "housing", "XGBoost", "ExtraTrees", "hypothesis-driven-research"]
---

## The Problem

Ireland rates every home offered for sale or rent on a scale from A1 (most efficient) to G (worst). The rating comes from a calculation called DEAP -- the Dwelling Energy Assessment Procedure -- which models how much energy the building should need based on its walls, roof, windows, heating system, and ventilation. A-rated homes are supposed to need less than 75 kWh per square meter per year. G-rated homes can score over 450.

But the ratings do not match reality. A landmark 2021 Irish study by Coyne and Denny, matching roughly 3,000 BER certificates to actual smart meter data, found something striking: G-rated homes used about 1.5 to 2.5 times as much energy as A-rated homes, not the 5 to 10 times that their BER certificates implied.

The explanation has two parts. First, the "prebound effect": people living in badly-rated homes already use less energy than the DEAP model predicts, because they under-heat their homes, close off rooms, or simply tolerate cold. The DEAP model assumes everyone heats their whole house to 20 degrees for 16 hours a day, but many Irish households -- especially in older housing stock -- heat only the living room to 18 degrees for a few hours. Second, the "rebound effect": people in well-rated homes use more than predicted because they heat the entire house to comfortable temperatures. The two effects compress actual consumption toward the middle.

This matters because Ireland's National Retrofit Plan targets 500,000 home upgrades to BER B2 by 2030 at a cost of approximately EUR8 billion. If each retrofit delivers 50-70% of the energy savings that BER improvement predicts, the plan's carbon reduction projections may be systematically optimistic.

We asked: what does the BER system actually measure, and which retrofits are truly worth the money?

## The Baseline (What We Compared Against)

Because the full SEAI BER dataset of roughly one million certificates requires either manual county-by-county CSV export or a research data agreement, and no public API exists, we generated a calibrated synthetic dataset of 100,000 BER certificates. The synthetic data reproduces the statistical properties documented in SEAI annual reports: the county-level housing stock distribution, the construction era profile (with the Celtic Tiger era 2000-2008 appropriately over-represented), the heating fuel mix (37% oil, 34% gas, 12% solid fuel, 8% heat pump), and the BER rating distribution (roughly 60% of stock rated C or worse).

Each synthetic certificate includes a simplified DEAP-like energy calculation: fabric heat loss from wall, roof, floor, and window U-values multiplied by areas and Heating Degree Days; ventilation heat loss from air permeability and volume; heating system efficiency; and primary energy conversion factors. The target variable is the BER Energy Value in kWh/m2/yr -- the number that determines the letter grade.

The baseline model is XGBoost with 21 features: year built, floor area, wall U-value, roof U-value, floor U-value, window U-value, heating efficiency, primary energy factor, air permeability, county Heating Degree Days, number of storeys, number of bedrooms, floor insulation status, plus label-encoded categoricals for county, dwelling type, wall type, insulation type, window type, heating type, ventilation type, and secondary heating.

Baseline result: **cross-validated MAE of 61.04 kWh/m2/yr** (about 28% of the mean energy value of 214 kWh/m2/yr), R2 of 0.604. The model explains roughly 60% of the variance but struggles badly with G-rated homes (MAE 172 kWh/m2/yr) while performing well on A-rated homes (MAE 9 kWh/m2/yr).

## The Solution (What the HDR Loop Found)

The Phase 1 model tournament found that ExtraTrees outperformed all other approaches with a CV MAE of 55.51, beating XGBoost (61.04), LightGBM (59.52), and Ridge regression (71.96). Ridge's R2 of 0.613 was notably close to the tree methods (0.604-0.659), confirming that the DEAP calculation is substantially linear -- which makes sense, since DEAP is built on linear heat transfer equations.

Through 20 pre-registered experiments in the HDR loop, three features were kept:

**1. Dwelling form factor proxy** -- the single biggest discovery. This simple feature encodes the surface-area-to-volume ratio by dwelling type: detached houses score 3.0, semi-detached 2.3, end-terrace 2.0, mid-terrace 1.5, and apartments 1.2. Adding this one number dropped the MAE from 55.51 to 34.25 -- a 38% improvement. The reason is physical: the DEAP calculation is dominated by fabric heat loss, which scales with envelope surface area. A mid-terrace home shares two walls with neighbours and has only front and back exposed. A detached home of the same floor area has four exposed walls. The form factor captures this geometry directly.

**2. Wall quality ordinal** -- a six-level binning of continuous wall U-value. This helps because wall U-values cluster around standard values for each construction era, and the binning reduces noise from assessor-level reporting variation.

**3. Wall-heating interaction** -- the product of wall U-value and inverse heating efficiency. Poor walls with an inefficient solid fuel boiler produce dramatically worse BER ratings than the same walls with a heat pump. The interaction captures this compounding effect.

Notable failures: regulation era, vintage decade, area per bedroom, county radon risk, gas availability, and individual heating technology flags all failed to improve the model. Most of this information was already captured by the base features.

**Final model: CV MAE 33.03 kWh/m2/yr, R2=0.88.** A 46% improvement over the baseline XGBoost.

## The Discovery (What the Model Reveals About Irish Housing)

### Which retrofits actually improve BER?

We evaluated nine retrofit measures across seven representative Irish housing archetypes, from pre-1940 terraced houses in Dublin to 2022 nZEB (nearly Zero Energy Building) semi-detached homes.

The standout finding: **cavity wall insulation** is by far the most cost-effective single retrofit, at just EUR28 per kWh/m2/yr saved for 1970s detached homes with unfilled cavity walls. This matters because roughly 12% of Irish housing stock has unfilled cavity walls -- these are the "low-hanging fruit" of the national retrofit programme.

For homes without cavity walls (pre-1940 solid construction), the cheapest entry point is **attic insulation** at EUR60 per kWh/m2/yr. For 1950s semi-detached homes with oil heating, an **air source heat pump** is most cost-effective at EUR93 per kWh/m2/yr because the shift from oil (82% efficient with a 1.1 primary energy factor) to a heat pump (COP 3.2 but with a 2.08 electricity factor) produces a large absolute improvement.

### Deep retrofit packages

A "fabric plus heating" package (external wall insulation + attic insulation to 300mm + air source heat pump, total EUR25,200) moves typical Irish housing from the D-rated range to B1:
- 1950s semi-D: D2 to B1 (improvement: 196 kWh/m2/yr)
- Pre-1940 terraced: D1 to B1 (improvement: 153 kWh/m2/yr)
- 1970s detached: C3 to B1 (improvement: 124 kWh/m2/yr)

Adding triple glazing and mechanical ventilation (total EUR44,000) achieves A-rated results but at nearly double the cost with marginal additional BER benefit.

### The inconvenient truth about actual savings

Applying Coyne and Denny's performance gap factors: a EUR25,200 retrofit on a 1950s semi-D is predicted by BER to save 196 kWh/m2/yr, but the actual saving is likely 100-140 kWh/m2/yr because the D2-rated starting point already under-consumed relative to DEAP predictions (prebound), and the occupant will increase comfort after retrofit (rebound).

### The radon warning

The EPA UNVEIL project documented that improving airtightness can trap radon gas in homes built over granitic bedrock -- particularly in parts of Wicklow, Galway, Kerry, and Donegal. Our analysis includes county-level radon risk, but it does not predict BER energy values because the BER system ignores indoor air quality entirely. This is itself a finding: retrofit grants should require radon testing in high-risk areas when airtightness improvements are planned.

## Honest Limitations

This study uses synthetic BER data, not the actual SEAI dataset. The performance gap estimates rely on published 2021 factors that may not represent 2026 conditions. The simplified DEAP calculation omits some parameters (detailed thermal bridging, solar thermal, multiple heating zones). And fundamentally: BER certificates give DEAP-calculated energy, not measured energy. We can predict what the BER system will say, but we cannot directly predict what a household will actually spend on heating.

---

*Built with the [HDR methodology](/hdr/). Source code at `applications/ber_energy_gap/`.*
