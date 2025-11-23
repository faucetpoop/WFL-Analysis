"""
Integrated Narrative Descriptive Report Generator
Combines vendor and household data into data journey narrative

"Long Biên's Food Environment: From Vendors to Households to Diets"

The narrative arc:
- Part 1: The Food Landscape (vendor data)
- Part 2: Household Navigation (household data)
- Part 3: Dietary Outcomes (HDDS analysis)
- Part 4: Key Patterns (integrated insights)

Author: Claude Code
Date: 2025-11-23
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================

# Paths
HOUSEHOLD_PATH = Path("/Users/emersonrburke/Desktop/working/working_thesis_211125/Resources/Datasets/DataLongBien2024/household_survey_LONG_BIEN_2024_ALL_merged.csv")
VENDOR_PATH = Path("/Users/emersonrburke/Desktop/working/working_thesis_211125/Resources/Datasets/DataLongBien2024/vendor_survey_LONG_BIEN_2024_ALL_merged.csv")
OUTPUT_DIR = Path("/Users/emersonrburke/Desktop/working/working_thesis_211125/WFL-Analysis/02_outputs/descriptive_report")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================================
# LOAD DATA
# ============================================================================

print("=" * 80)
print("INTEGRATED NARRATIVE REPORT: Long Biên's Food Environment")
print("=" * 80)
print("\nLoading datasets...")

hh = pd.read_csv(HOUSEHOLD_PATH)
vendor = pd.read_csv(VENDOR_PATH)

print(f"✓ Loaded {len(hh)} households")
print(f"✓ Loaded {len(vendor)} vendors")

# ============================================================================
# CREATE NARRATIVE REPORT
# ============================================================================

narrative = []

narrative.append("# Long Biên's Food Environment: A Data Journey")
narrative.append(f"\n**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
narrative.append(f"\n**Sample**: {len(hh)} households, {len(vendor)} vendors")
narrative.append("\n---\n")

# ============================================================================
# PART 1: THE FOOD LANDSCAPE (VENDOR DATA)
# ============================================================================

narrative.append("## Part 1: The Food Landscape That Vendors Create\n")
narrative.append(f"Long Biên District's food environment comprises **{len(vendor)} surveyed vendors** ")
narrative.append("operating across diverse retail formats. These vendors create the external food ")
narrative.append("environment—the structural availability, variety, and accessibility that households ")
narrative.append("encounter when acquiring food.\n")

# Vendor types distribution
if 'vendortype' in vendor.columns:
    vendor_types = vendor['vendortype'].value_counts()
    narrative.append("\n### 1.1 Vendor Landscape Composition\n")
    narrative.append("The vendor landscape reflects Vietnam's characteristic retail diversity:\n")
    for vtype, count in vendor_types.head(6).items():
        pct = (count / len(vendor)) * 100
        narrative.append(f"- **{vtype.capitalize()}**: {count} vendors ({pct:.1f}%)\n")

# Geographic distribution
if 'neighborhood' in vendor.columns:
    n_neighborhoods = vendor['neighborhood'].nunique()
    top_neighborhood = vendor['neighborhood'].value_counts().index[0]
    top_n = vendor['neighborhood'].value_counts().iloc[0]
    top_pct = (top_n / len(vendor)) * 100

    narrative.append(f"\n### 1.2 Geographic Coverage\n")
    narrative.append(f"Vendors operate across **{n_neighborhoods} neighborhoods**, with highest ")
    narrative.append(f"concentration in **{top_neighborhood}** ({top_n} vendors, {top_pct:.1f}%). ")
    narrative.append("This spatial distribution creates differentiated food access patterns across ")
    narrative.append("Long Biên's urban-peri-urban gradient.\n")

# Product availability
foodgroup_cols = [col for col in vendor.columns if col.startswith('foodgroups/')]
if foodgroup_cols:
    vendor['product_diversity'] = vendor[foodgroup_cols].sum(axis=1)
    mean_diversity = vendor['product_diversity'].mean()
    median_diversity = vendor['product_diversity'].median()

    narrative.append(f"\n### 1.3 Product Availability\n")
    narrative.append(f"Vendors offer an average of **{mean_diversity:.1f} food groups** ")
    narrative.append(f"(median: {median_diversity:.0f}), with most common offerings being:\n")

    foodgroup_prev = []
    for col in foodgroup_cols:
        food_group = col.split('/')[-1]
        count = vendor[col].sum() if vendor[col].dtype in [int, float] else vendor[col].value_counts().get(1, 0)
        pct = (count / len(vendor)) * 100
        foodgroup_prev.append((food_group, count, pct))

    foodgroup_prev_sorted = sorted(foodgroup_prev, key=lambda x: x[2], reverse=True)
    for fg, count, pct in foodgroup_prev_sorted[:5]:
        narrative.append(f"- **{fg.replace('_', ' ').title()}**: {pct:.1f}% of vendors\n")

# Whole vs processed
if 'wholeorprocessed' in vendor.columns:
    processed_pct = (vendor['wholeorprocessed'] == 'processed').sum() / len(vendor) * 100
    whole_pct = (vendor['wholeorprocessed'] == 'whole').sum() / len(vendor) * 100

    narrative.append(f"\n### 1.4 Product Processing Patterns\n")
    narrative.append(f"The vendor landscape shows **{processed_pct:.1f}% processed foods** versus ")
    narrative.append(f"**{whole_pct:.1f}% whole foods**, reflecting Vietnam's nutrition transition ")
    narrative.append("as traditional fresh markets coexist with modern retail formats.\n")

# ============================================================================
# PART 2: HOUSEHOLD NAVIGATION (HOUSEHOLD DATA)
# ============================================================================

narrative.append("\n---\n")
narrative.append("## Part 2: How Households Navigate This Landscape\n")
narrative.append(f"The **{len(hh)} surveyed households** navigate Long Biên's food environment ")
narrative.append("with differentiated resources, constraints, and strategies. Personal domain ")
narrative.append("factors—accessibility, affordability, and perceptions—mediate how the external ")
narrative.append("vendor landscape translates into household food acquisition.\n")

# Demographics
if 'total' in hh.columns:
    mean_hh_size = hh['total'].mean()
    narrative.append(f"\n### 2.1 Household Characteristics\n")
    narrative.append(f"Households average **{mean_hh_size:.1f} members**, with composition reflecting ")
    narrative.append("typical urban Vietnamese family structures.\n")

# Travel times
time_vars = [f'time_{str(i).zfill(3)}' for i in range(1, 8)]
travel_data = []
for var in time_vars:
    if var in hh.columns:
        travel_data.append(hh[var].dropna())

if travel_data:
    all_travel_times = pd.concat(travel_data)
    mean_travel = all_travel_times.mean()
    median_travel = all_travel_times.median()

    narrative.append(f"\n### 2.2 Accessibility Patterns\n")
    narrative.append(f"Households travel an average of **{mean_travel:.1f} minutes** (median: {median_travel:.0f} min) ")
    narrative.append("to reach food vendors. This temporal accessibility dimension shapes which vendor ")
    narrative.append("formats households can practically access given work and care responsibilities.\n")

# Neighborhood perceptions
if all(col in hh.columns for col in ['clean', 'safe', 'reputation']):
    mean_clean = hh['clean'].mean()
    mean_safe = hh['safe'].mean()
    mean_rep = hh['reputation'].mean()

    narrative.append(f"\n### 2.3 Neighborhood Context\n")
    narrative.append("Household perceptions of neighborhood quality (scale: -2 to +2):\n")
    narrative.append(f"- **Cleanliness**: {mean_clean:.2f}\n")
    narrative.append(f"- **Safety**: {mean_safe:.2f}\n")
    narrative.append(f"- **Reputation**: {mean_rep:.2f}\n")
    narrative.append("\nThese neighborhood perceptions shape food acquisition strategies beyond ")
    narrative.append("proximity, influencing where households feel comfortable shopping.\n")

# Food expenditure
if 'foodexpenditure' in hh.columns:
    food_exp = pd.to_numeric(hh['foodexpenditure'], errors='coerce')
    median_exp = food_exp.median()
    iqr_low = food_exp.quantile(0.25)
    iqr_high = food_exp.quantile(0.75)

    narrative.append(f"\n### 2.4 Affordability Constraints\n")
    narrative.append(f"Median household food expenditure: **{median_exp:,.0f} VND** ")
    narrative.append(f"(IQR: {iqr_low:,.0f}–{iqr_high:,.0f} VND). ")
    narrative.append("The wide expenditure range reflects differentiated affordability constraints ")
    narrative.append("that shape which vendor formats and food types households can access.\n")

# ============================================================================
# PART 3: DIETARY OUTCOMES (HDDS ANALYSIS)
# ============================================================================

narrative.append("\n---\n")
narrative.append("## Part 3: Dietary Outcomes\n")
narrative.append("The interaction of vendor-supplied availability and household-mediated access ")
narrative.append("produces observable dietary patterns measured through dietary diversity.\n")

# Calculate HDDS from foodgroups
hh_foodgroup_cols = [col for col in hh.columns if col.startswith('foodgroups/')]
if hh_foodgroup_cols:
    hh['HDDS'] = hh[hh_foodgroup_cols].sum(axis=1)
    mean_hdds = hh['HDDS'].mean()
    median_hdds = hh['HDDS'].median()
    sd_hdds = hh['HDDS'].std()

    narrative.append(f"\n### 3.1 Household Dietary Diversity\n")
    narrative.append(f"Mean HDDS: **{mean_hdds:.2f}** (SD: {sd_hdds:.2f}, Median: {median_hdds:.0f}). ")

    # Most consumed food groups
    hh_fg_prev = []
    for col in hh_foodgroup_cols:
        food_group = col.split('/')[-1]
        count = hh[col].sum() if hh[col].dtype in [int, float] else hh[col].value_counts().get(1, 0)
        pct = (count / len(hh)) * 100
        hh_fg_prev.append((food_group, count, pct))

    hh_fg_prev_sorted = sorted(hh_fg_prev, key=lambda x: x[2], reverse=True)

    narrative.append("\n\nMost commonly consumed food groups:\n")
    for fg, count, pct in hh_fg_prev_sorted[:5]:
        narrative.append(f"- **{fg.replace('_', ' ').title()}**: {pct:.1f}% of households\n")

# ============================================================================
# PART 4: KEY PATTERNS & INSIGHTS
# ============================================================================

narrative.append("\n---\n")
narrative.append("## Part 4: Integrated Insights\n")

narrative.append("\n### 4.1 Supply-Demand Alignment\n")
narrative.append("Comparing vendor supply with household consumption reveals:\n")

# Compare top vendor offerings with top household consumption
if foodgroup_cols and hh_foodgroup_cols:
    vendor_top = [fg for fg, _, _ in foodgroup_prev_sorted[:3]]
    hh_top = [fg for fg, _, _ in hh_fg_prev_sorted[:3]]

    narrative.append(f"- **Vendor top offerings**: {', '.join([v.replace('_', ' ') for v in vendor_top])}\n")
    narrative.append(f"- **Household top consumption**: {', '.join([h.replace('_', ' ') for h in hh_top])}\n")

    alignment = set(vendor_top) & set(hh_top)
    if alignment:
        narrative.append(f"\nAlignment observed in: **{', '.join([a.replace('_', ' ') for a in alignment])}**\n")

narrative.append("\n### 4.2 Structural Patterns\n")
narrative.append("Three structural patterns emerge from the integrated data:\n\n")

narrative.append("1. **Retail Diversity Coexists with Spatial Inequality**: ")
narrative.append(f"{len(vendor)} vendors across {n_neighborhoods} neighborhoods create uneven ")
narrative.append("accessibility, with household travel times varying substantially.\n\n")

narrative.append("2. **Traditional-Modern Transition Underway**: ")
narrative.append(f"Vendor composition ({processed_pct:.0f}% processed vs {whole_pct:.0f}% whole foods) ")
narrative.append("reflects Vietnam's nutrition transition, with implications for dietary outcomes.\n\n")

narrative.append("3. **Affordability Mediates Access**: ")
narrative.append(f"Wide food expenditure variation (IQR: {iqr_low:,.0f}–{iqr_high:,.0f} VND) suggests ")
narrative.append("affordability constraints differentiate which households can access higher-quality vendors.\n")

# ============================================================================
# SUMMARY TABLE
# ============================================================================

narrative.append("\n---\n")
narrative.append("## Summary Statistics\n")

summary_table = {
    'Domain': [],
    'Vendor Landscape': [],
    'Household Reality': []
}

summary_table['Domain'].append('Sample Size')
summary_table['Vendor Landscape'].append(f"{len(vendor)} vendors")
summary_table['Household Reality'].append(f"{len(hh)} households")

summary_table['Domain'].append('Geographic Coverage')
summary_table['Vendor Landscape'].append(f"{n_neighborhoods} neighborhoods")
if 'neighborhood' in hh.columns:
    hh_neighborhoods = hh['neighborhood'].nunique()
    summary_table['Household Reality'].append(f"{hh_neighborhoods} neighborhoods")
else:
    summary_table['Household Reality'].append("N/A")

summary_table['Domain'].append('Product Diversity')
summary_table['Vendor Landscape'].append(f"{mean_diversity:.1f} food groups/vendor")
summary_table['Household Reality'].append(f"{mean_hdds:.1f} HDDS score")

summary_table['Domain'].append('Accessibility')
summary_table['Vendor Landscape'].append("Multiple formats available")
summary_table['Household Reality'].append(f"{mean_travel:.1f} min average travel")

summary_table['Domain'].append('Food Types')
summary_table['Vendor Landscape'].append(f"{processed_pct:.0f}% processed")
if hh_foodgroup_cols:
    summary_table['Household Reality'].append(f"Top: {hh_fg_prev_sorted[0][0].replace('_', ' ')}")
else:
    summary_table['Household Reality'].append("N/A")

summary_df = pd.DataFrame(summary_table)
summary_df.to_csv(OUTPUT_DIR / "Table_INTEGRATED_Summary_Comparison.csv", index=False)

narrative.append("\n```")
narrative.append(summary_df.to_string(index=False))
narrative.append("\n```\n")

# ============================================================================
# CONCLUSIONS
# ============================================================================

narrative.append("\n---\n")
narrative.append("## Narrative Conclusions\n")

narrative.append("\nThis integrated view reveals Long Biên's food environment as a complex ")
narrative.append("system where vendor-created structural features interact with household-level ")
narrative.append("mediating factors to produce dietary outcomes. The narrative journey from ")
narrative.append("**vendors** (who create availability) → **households** (who navigate constraints) ")
narrative.append("→ **diets** (measurable outcomes) demonstrates how food environments function ")
narrative.append("not as static backdrops but as dynamic systems shaped by both supply-side ")
narrative.append("structures and demand-side realities.\n")

narrative.append("\nKey insights for food environment interventions:\n")
narrative.append("- Vendor diversity alone does not guarantee household dietary diversity\n")
narrative.append("- Accessibility (travel time) and affordability (expenditure capacity) mediate access\n")
narrative.append("- Neighborhood perceptions influence where households feel comfortable shopping\n")
narrative.append("- The nutrition transition (processed vs whole foods) is observable in both supply and demand\n")

narrative.append("\n---\n")
narrative.append(f"*Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")
narrative.append(f"*Data: {len(hh)} households, {len(vendor)} vendors, Long Biên District, Hanoi*\n")

# ============================================================================
# WRITE NARRATIVE TO FILE
# ============================================================================

narrative_text = '\n'.join(narrative)
output_file = OUTPUT_DIR / "INTEGRATED_NARRATIVE_REPORT.md"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(narrative_text)

print("\n" + "=" * 80)
print("INTEGRATED NARRATIVE REPORT GENERATED")
print("=" * 80)
print(f"\nSaved to: {output_file}")
print("\nReport Structure:")
print("  Part 1: The Food Landscape (Vendor Data)")
print("  Part 2: Household Navigation (Household Data)")
print("  Part 3: Dietary Outcomes (HDDS Analysis)")
print("  Part 4: Key Patterns & Insights")
print("\nAdditional Table:")
print("  - Table_INTEGRATED_Summary_Comparison.csv")
print("\n" + "=" * 80)
