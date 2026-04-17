---
title: "How Much Zoned Land Is Blocked by Wastewater Capacity?"
date: 2026-04-17
domain: "Irish Housing"
blurb: "About a quarter of Ireland's 1,063 wastewater treatment plants are at or over capacity (15% RED, 10% AMBER). This translates to roughly 950-1,700 hectares of zoned residential land in constrained catchments — 12-22% of the national total. But wastewater is a secondary constraint: 83% of zoned land is already economically unviable (from the companion viability study), and about 1,265 hectares are 'double-stranded' — blocked by both infrastructure AND economics. The infrastructure constraint is real but smaller than the viability constraint."
weight: 6
tags: ["housing", "ireland", "infrastructure", "wastewater", "upper-funnel"]
---

*Plain-language summary. Full technical write-up in the [paper](https://github.com/colinjoc/generalized_hdr_autoresearch/blob/main/applications/ie_infra_capacity/paper.md).*

## The question

Even where land is zoned for housing and the numbers might work, you still can't build if there's no wastewater treatment capacity. Uisce Eireann (Irish Water) publishes capacity status for every treatment plant in the country. **How much zoned land is blocked by infrastructure?**

## What we found

### A quarter of treatment plants are constrained

Of 1,063 wastewater treatment plants nationwide:
- **GREEN** (spare capacity): 790 plants (74%)
- **AMBER** (potentially constrained): 109 plants (10%)
- **RED** (no spare capacity): 164 plants (15%)

### Roughly 950-1,700 hectares of zoned land sit in constrained catchments

Mapping RED/AMBER plant locations against county-level zoned-land estimates gives approximately **1,524 hectares** in constrained catchments (19% of the 7,911 ha national total). The range reflects sensitivity to how county-level data maps to individual catchments — rural RED plants are typically small and serve less zoned land than urban GREEN plants.

### Most RED plants have no upgrade planned

Of 164 RED plants, **122 (74%) have no upgrade project planned or underway.** These are mostly small rural facilities. The highest-priority investment targets — plants where an upgrade would unlock the most zoned land — are in Fingal, Louth, and Galway.

### Infrastructure is a secondary constraint — viability is bigger

The companion [viability study](/hdr/results/irish-viability-frontier/) found that 83% of zoned land is economically unviable. About **1,265 hectares are "double-stranded"** — blocked by both wastewater constraints AND development economics. Fixing the infrastructure alone wouldn't make these sites viable.

| Constraint | Hectares affected | % of 7,911 ha |
|:---|---:|---:|
| Economically unviable (U-2) | ~6,580 | 83% |
| Infrastructure constrained (U-3) | ~950-1,700 | 12-22% |
| Double-stranded (both) | ~1,265 | 16% |

### Dublin is GREEN at the treatment plant — but network capacity is unknown

Dublin's main treatment plant (Ringsend) is classified GREEN. But the capacity register only covers **treatment plants, not pipe networks**. Network constraints (inadequate sewers, pumping stations) are a separate and potentially significant barrier in Dublin that this data does not capture.

### One-off rural houses bypass the system entirely

About 24% of residential planning applications are for one-off houses using septic tanks. These are not dependent on WWTP capacity at all. The infrastructure constraint applies mainly to multi-unit schemes in towns and cities that need mains connections.

## What this does NOT establish

- **Not network capacity.** The register covers treatment-plant headroom only. Pipe/sewer network constraints are excluded and could be larger in urban areas.
- **Not parcel-level.** The hectare estimates use county-level ecological inference, not individual-site matching. The range (950-1,700 ha) reflects this uncertainty.
- **Not a time series.** We have one snapshot (2024 register). Historical capacity trends are not available.

## What it means

For policymakers: wastewater capacity is a real but secondary constraint. The bigger problems are upstream — not enough applications being filed (U-1) because development isn't economically viable (U-2). Fixing sewage for 164 RED plants would help but wouldn't solve the housing crisis on its own. The highest-leverage infrastructure investments are the 122 RED plants with no upgrade project — especially in the commuter belt where viability is closer to marginal.

## How we did it

Scraped Uisce Eireann's wastewater treatment capacity register (29 county pages, 1,063 plants, GREEN/AMBER/RED classification). Linked to county-level zoned-land estimates and viability margins from companion projects. Phase 2.75 blind reviewer caught the ecological-inference problem (county-level proportions applied to zoned land) and mandated a plant-size sensitivity range. CSS color classification spot-checked 5/5 correct. Full HDR pipeline with Phase 3.5 signoff.
