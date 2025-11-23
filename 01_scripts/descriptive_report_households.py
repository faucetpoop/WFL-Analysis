"""
Household Descriptive Report Generator
Generates comprehensive descriptive tables for Long Biên household survey data

Output: 4 table types across 5 narrative sections
- Section 1: Demographics
- Section 2: Neighborhood Context
- Section 3: Food Shopping Behaviors
- Section 4: Dietary Patterns
- Section 5: Integrated Summary

Author: Claude Code
Date: 2025-11-23
"""

import pandas as pd
import numpy as np
from pathlib import Path

# ============================================================================
# CONFIGURATION
# ============================================================================

# Paths
DATA_PATH = Path("/Users/emersonrburke/Desktop/working/working_thesis_211125/Resources/Datasets/DataLongBien2024/household_survey_LONG_BIEN_2024_ALL_merged.csv")
OUTPUT_DIR = Path("/Users/emersonrburke/Desktop/working/working_thesis_211125/WFL-Analysis/02_outputs/descriptive_report")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================================
# LOAD DATA
# ============================================================================

print("Loading household survey data...")
df = pd.read_csv(DATA_PATH)
print(f"Loaded {len(df)} households with {len(df.columns)} variables\n")

# ============================================================================
# SECTION 1: WHO ARE THESE HOUSEHOLDS?
# ============================================================================

print("=" * 80)
print("SECTION 1: WHO ARE THESE HOUSEHOLDS?")
print("=" * 80)

# Table 1A: Demographic Profile
demographic_stats = {
    'Variable': [],
    'N': [],
    'Mean': [],
    'SD': [],
    'Min': [],
    'Median': [],
    'Max': []
}

# Household size components
if 'total' in df.columns:
    demographic_stats['Variable'].append('Household Size (total)')
    demographic_stats['N'].append(df['total'].notna().sum())
    demographic_stats['Mean'].append(df['total'].mean())
    demographic_stats['SD'].append(df['total'].std())
    demographic_stats['Min'].append(df['total'].min())
    demographic_stats['Median'].append(df['total'].median())
    demographic_stats['Max'].append(df['total'].max())

for var, label in [('men', 'Men'), ('women', 'Women'), ('children', 'Children')]:
    if var in df.columns:
        demographic_stats['Variable'].append(label)
        demographic_stats['N'].append(df[var].notna().sum())
        demographic_stats['Mean'].append(df[var].mean())
        demographic_stats['SD'].append(df[var].std())
        demographic_stats['Min'].append(df[var].min())
        demographic_stats['Median'].append(df[var].median())
        demographic_stats['Max'].append(df[var].max())

# Age (if available)
if 'locationtime_age' in df.columns:
    demographic_stats['Variable'].append('Respondent Age (years)')
    demographic_stats['N'].append(df['locationtime_age'].notna().sum())
    demographic_stats['Mean'].append(df['locationtime_age'].mean())
    demographic_stats['SD'].append(df['locationtime_age'].std())
    demographic_stats['Min'].append(df['locationtime_age'].min())
    demographic_stats['Median'].append(df['locationtime_age'].median())
    demographic_stats['Max'].append(df['locationtime_age'].max())

# Workers
if 'workers' in df.columns:
    demographic_stats['Variable'].append('Number of Workers')
    demographic_stats['N'].append(df['workers'].notna().sum())
    demographic_stats['Mean'].append(df['workers'].mean())
    demographic_stats['SD'].append(df['workers'].std())
    demographic_stats['Min'].append(df['workers'].min())
    demographic_stats['Median'].append(df['workers'].median())
    demographic_stats['Max'].append(df['workers'].max())

table_1a = pd.DataFrame(demographic_stats)
table_1a.to_csv(OUTPUT_DIR / "Table_1A_Demographics_Continuous.csv", index=False)
print("\n✓ Table 1A: Demographic Profile (Continuous Variables)")
print(table_1a.to_string(index=False))

# Table 1B: Categorical Demographics
categorical_stats = []

# Gender
if 'resp_gender' in df.columns:
    gender_counts = df['resp_gender'].value_counts()
    gender_pct = df['resp_gender'].value_counts(normalize=True) * 100
    for category in gender_counts.index:
        categorical_stats.append({
            'Variable': 'Respondent Gender',
            'Category': category,
            'N': gender_counts[category],
            'Percent': gender_pct[category]
        })

# Education
if 'resp_edu' in df.columns:
    edu_counts = df['resp_edu'].value_counts()
    edu_pct = df['resp_edu'].value_counts(normalize=True) * 100
    for category in edu_counts.index:
        categorical_stats.append({
            'Variable': 'Respondent Education',
            'Category': category,
            'N': edu_counts[category],
            'Percent': edu_pct[category]
        })

# Ethnicity
if 'resp_ethn' in df.columns:
    ethn_counts = df['resp_ethn'].value_counts()
    ethn_pct = df['resp_ethn'].value_counts(normalize=True) * 100
    for category in ethn_counts.index:
        categorical_stats.append({
            'Variable': 'Respondent Ethnicity',
            'Category': category,
            'N': ethn_counts[category],
            'Percent': ethn_pct[category]
        })

# Neighborhood
if 'neighborhood' in df.columns:
    neigh_counts = df['neighborhood'].value_counts()
    neigh_pct = df['neighborhood'].value_counts(normalize=True) * 100
    for category in neigh_counts.index:
        categorical_stats.append({
            'Variable': 'Neighborhood',
            'Category': category,
            'N': neigh_counts[category],
            'Percent': neigh_pct[category]
        })

table_1b = pd.DataFrame(categorical_stats)
table_1b.to_csv(OUTPUT_DIR / "Table_1B_Demographics_Categorical.csv", index=False)
print("\n✓ Table 1B: Demographic Profile (Categorical Variables)")
print(table_1b.to_string(index=False))

# ============================================================================
# SECTION 2: NEIGHBORHOOD CONTEXT
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 2: NEIGHBORHOOD CONTEXT")
print("=" * 80)

# Table 2A: Neighborhood Perceptions
neigh_perception = {
    'Variable': [],
    'N': [],
    'Mean': [],
    'SD': [],
    'Min': [],
    'Median': [],
    'Max': []
}

for var, label in [('clean', 'Neighborhood Cleanliness'),
                    ('safe', 'Neighborhood Safety'),
                    ('reputation', 'Neighborhood Reputation')]:
    if var in df.columns:
        neigh_perception['Variable'].append(label)
        neigh_perception['N'].append(df[var].notna().sum())
        neigh_perception['Mean'].append(df[var].mean())
        neigh_perception['SD'].append(df[var].std())
        neigh_perception['Min'].append(df[var].min())
        neigh_perception['Median'].append(df[var].median())
        neigh_perception['Max'].append(df[var].max())

table_2a = pd.DataFrame(neigh_perception)
table_2a.to_csv(OUTPUT_DIR / "Table_2A_Neighborhood_Perceptions.csv", index=False)
print("\n✓ Table 2A: Neighborhood Perceptions")
print(table_2a.to_string(index=False))

# Table 2B: Travel Times to Markets
travel_stats = {
    'Vendor Type': [],
    'N': [],
    'Mean (min)': [],
    'SD': [],
    'Min': [],
    'Median': [],
    'Max': []
}

# Assuming time_001 through time_007 are different vendor types
# We'll need to check the codebook for labels, but for now use generic names
time_vars = [f'time_{str(i).zfill(3)}' for i in range(1, 8)]
for i, var in enumerate(time_vars, 1):
    if var in df.columns:
        travel_stats['Vendor Type'].append(f'Vendor Type {i}')
        travel_stats['N'].append(df[var].notna().sum())
        travel_stats['Mean (min)'].append(df[var].mean())
        travel_stats['SD'].append(df[var].std())
        travel_stats['Min'].append(df[var].min())
        travel_stats['Median'].append(df[var].median())
        travel_stats['Max'].append(df[var].max())

table_2b = pd.DataFrame(travel_stats)
table_2b.to_csv(OUTPUT_DIR / "Table_2B_Travel_Times.csv", index=False)
print("\n✓ Table 2B: Travel Times to Markets")
print(table_2b.to_string(index=False))

# ============================================================================
# SECTION 3: FOOD SHOPPING BEHAVIORS
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 3: FOOD SHOPPING BEHAVIORS")
print("=" * 80)

# Table 3A: Food Expenditure
if 'foodexpenditure' in df.columns:
    # Convert to numeric, handling any non-numeric values
    food_exp = pd.to_numeric(df['foodexpenditure'], errors='coerce')
    exp_stats = pd.DataFrame({
        'Variable': ['Food Expenditure'],
        'N': [food_exp.notna().sum()],
        'Mean': [food_exp.mean()],
        'SD': [food_exp.std()],
        'Min': [food_exp.min()],
        'Q25': [food_exp.quantile(0.25)],
        'Median': [food_exp.median()],
        'Q75': [food_exp.quantile(0.75)],
        'Max': [food_exp.max()]
    })
    exp_stats.to_csv(OUTPUT_DIR / "Table_3A_Food_Expenditure.csv", index=False)
    print("\n✓ Table 3A: Food Expenditure")
    print(exp_stats.to_string(index=False))

# Table 3B: Food Sharing Activities
if 'foodsharing_activity' in df.columns:
    # Check for multi-select columns
    sharing_cols = [col for col in df.columns if col.startswith('foodsharing_activity/')]
    if sharing_cols:
        sharing_stats = []
        for col in sharing_cols:
            activity = col.split('/')[-1]
            count = df[col].sum() if df[col].dtype in [int, float] else df[col].value_counts().get(1, 0)
            pct = (count / len(df)) * 100
            sharing_stats.append({
                'Activity': activity,
                'N': count,
                'Percent': pct
            })
        table_3b = pd.DataFrame(sharing_stats)
        table_3b.to_csv(OUTPUT_DIR / "Table_3B_Food_Sharing.csv", index=False)
        print("\n✓ Table 3B: Food Sharing Activities")
        print(table_3b.to_string(index=False))

# ============================================================================
# SECTION 4: DIETARY PATTERNS
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 4: DIETARY PATTERNS")
print("=" * 80)

# Table 4A: Food Groups Consumed
# Looking for foodgroups variables
foodgroup_cols = [col for col in df.columns if col.startswith('foodgroups/')]

if foodgroup_cols:
    foodgroup_stats = []
    for col in foodgroup_cols:
        food_group = col.split('/')[-1]
        # Assuming binary (1 = consumed, 0 = not consumed)
        count = df[col].sum() if df[col].dtype in [int, float] else df[col].value_counts().get(1, 0)
        pct = (count / len(df)) * 100
        foodgroup_stats.append({
            'Food Group': food_group,
            'N Households': count,
            'Percent': pct
        })

    table_4a = pd.DataFrame(foodgroup_stats)
    table_4a = table_4a.sort_values('Percent', ascending=False)
    table_4a.to_csv(OUTPUT_DIR / "Table_4A_Food_Groups_Consumed.csv", index=False)
    print("\n✓ Table 4A: Food Groups Consumed (sorted by prevalence)")
    print(table_4a.to_string(index=False))

# Table 4B: Calculate HDDS if food groups present
if foodgroup_cols:
    # Calculate HDDS as sum of food groups consumed
    df['HDDS_calculated'] = df[foodgroup_cols].sum(axis=1)

    hdds_stats = pd.DataFrame({
        'Variable': ['Household Dietary Diversity Score (HDDS)'],
        'N': [df['HDDS_calculated'].notna().sum()],
        'Mean': [df['HDDS_calculated'].mean()],
        'SD': [df['HDDS_calculated'].std()],
        'Min': [df['HDDS_calculated'].min()],
        'Q25': [df['HDDS_calculated'].quantile(0.25)],
        'Median': [df['HDDS_calculated'].median()],
        'Q75': [df['HDDS_calculated'].quantile(0.75)],
        'Max': [df['HDDS_calculated'].max()]
    })
    hdds_stats.to_csv(OUTPUT_DIR / "Table_4B_HDDS_Distribution.csv", index=False)
    print("\n✓ Table 4B: HDDS Distribution")
    print(hdds_stats.to_string(index=False))

# ============================================================================
# SECTION 5: INTEGRATED SUMMARY
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 5: INTEGRATED SUMMARY TABLE")
print("=" * 80)

# Create comprehensive summary table
summary_data = {
    'Domain': [],
    'Indicator': [],
    'N': [],
    'Value': []
}

# Demographics
summary_data['Domain'].append('Demographics')
summary_data['Indicator'].append('Total Households')
summary_data['N'].append(len(df))
summary_data['Value'].append(f"{len(df)} households")

if 'total' in df.columns:
    summary_data['Domain'].append('Demographics')
    summary_data['Indicator'].append('Mean Household Size')
    summary_data['N'].append(df['total'].notna().sum())
    summary_data['Value'].append(f"{df['total'].mean():.1f} ± {df['total'].std():.1f}")

# Neighborhood
if 'safe' in df.columns:
    summary_data['Domain'].append('Neighborhood')
    summary_data['Indicator'].append('Safety Perception (mean score)')
    summary_data['N'].append(df['safe'].notna().sum())
    summary_data['Value'].append(f"{df['safe'].mean():.2f} ± {df['safe'].std():.2f}")

# Food Shopping
if 'foodexpenditure' in df.columns:
    food_exp = pd.to_numeric(df['foodexpenditure'], errors='coerce')
    summary_data['Domain'].append('Food Shopping')
    summary_data['Indicator'].append('Median Food Expenditure')
    summary_data['N'].append(food_exp.notna().sum())
    summary_data['Value'].append(f"{food_exp.median():.0f} (IQR: {food_exp.quantile(0.25):.0f}-{food_exp.quantile(0.75):.0f})")

# Dietary Diversity
if 'HDDS_calculated' in df.columns:
    summary_data['Domain'].append('Dietary Diversity')
    summary_data['Indicator'].append('Mean HDDS Score')
    summary_data['N'].append(df['HDDS_calculated'].notna().sum())
    summary_data['Value'].append(f"{df['HDDS_calculated'].mean():.2f} ± {df['HDDS_calculated'].std():.2f}")

table_5_summary = pd.DataFrame(summary_data)
table_5_summary.to_csv(OUTPUT_DIR / "Table_5_Integrated_Summary.csv", index=False)
print("\n✓ Table 5: Integrated Summary")
print(table_5_summary.to_string(index=False))

# ============================================================================
# COMPLETION
# ============================================================================

print("\n" + "=" * 80)
print("HOUSEHOLD DESCRIPTIVE REPORT GENERATION COMPLETE")
print("=" * 80)
print(f"\nAll tables saved to: {OUTPUT_DIR}")
print("\nGenerated tables:")
print("  - Table_1A_Demographics_Continuous.csv")
print("  - Table_1B_Demographics_Categorical.csv")
print("  - Table_2A_Neighborhood_Perceptions.csv")
print("  - Table_2B_Travel_Times.csv")
print("  - Table_3A_Food_Expenditure.csv")
print("  - Table_3B_Food_Sharing.csv")
print("  - Table_4A_Food_Groups_Consumed.csv")
print("  - Table_4B_HDDS_Distribution.csv")
print("  - Table_5_Integrated_Summary.csv")
print("\n" + "=" * 80)
