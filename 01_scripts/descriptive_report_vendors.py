"""
Vendor Landscape Descriptive Report Generator
Generates comprehensive descriptive tables for Long Biên vendor survey data

Output: 4 table types across 5 narrative sections
- Section 1: Who Are These Vendors?
- Section 2: Where They Operate (Locations)
- Section 3: What They Sell (Product Availability)
- Section 4: Vendor Characteristics (Business Model)
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
DATA_PATH = Path("/Users/emersonrburke/Desktop/working/working_thesis_211125/Resources/Datasets/DataLongBien2024/vendor_survey_LONG_BIEN_2024_ALL_merged.csv")
OUTPUT_DIR = Path("/Users/emersonrburke/Desktop/working/working_thesis_211125/WFL-Analysis/02_outputs/descriptive_report")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================================
# LOAD DATA
# ============================================================================

print("Loading vendor survey data...")
df = pd.read_csv(DATA_PATH)
print(f"Loaded {len(df)} vendors with {len(df.columns)} variables\n")

# ============================================================================
# SECTION 1: WHO ARE THESE VENDORS?
# ============================================================================

print("=" * 80)
print("SECTION 1: WHO ARE THESE VENDORS?")
print("=" * 80)

# Table V1A: Vendor Demographics
vendor_demo = {
    'Variable': [],
    'N': [],
    'Mean': [],
    'SD': [],
    'Min': [],
    'Median': [],
    'Max': []
}

# Age
if 'age' in df.columns:
    age_numeric = pd.to_numeric(df['age'], errors='coerce')
    vendor_demo['Variable'].append('Vendor Age (years)')
    vendor_demo['N'].append(age_numeric.notna().sum())
    vendor_demo['Mean'].append(age_numeric.mean())
    vendor_demo['SD'].append(age_numeric.std())
    vendor_demo['Min'].append(age_numeric.min())
    vendor_demo['Median'].append(age_numeric.median())
    vendor_demo['Max'].append(age_numeric.max())

# Staff
if 'staff' in df.columns:
    staff_numeric = pd.to_numeric(df['staff'], errors='coerce')
    vendor_demo['Variable'].append('Number of Staff')
    vendor_demo['N'].append(staff_numeric.notna().sum())
    vendor_demo['Mean'].append(staff_numeric.mean())
    vendor_demo['SD'].append(staff_numeric.std())
    vendor_demo['Min'].append(staff_numeric.min())
    vendor_demo['Median'].append(staff_numeric.median())
    vendor_demo['Max'].append(staff_numeric.max())

# Time at location
if 'locationtime' in df.columns:
    loc_time_numeric = pd.to_numeric(df['locationtime'], errors='coerce')
    vendor_demo['Variable'].append('Years at Current Location')
    vendor_demo['N'].append(loc_time_numeric.notna().sum())
    vendor_demo['Mean'].append(loc_time_numeric.mean())
    vendor_demo['SD'].append(loc_time_numeric.std())
    vendor_demo['Min'].append(loc_time_numeric.min())
    vendor_demo['Median'].append(loc_time_numeric.median())
    vendor_demo['Max'].append(loc_time_numeric.max())

table_v1a = pd.DataFrame(vendor_demo)
table_v1a.to_csv(OUTPUT_DIR / "Table_V1A_Vendor_Demographics_Continuous.csv", index=False)
print("\n✓ Table V1A: Vendor Demographics (Continuous Variables)")
print(table_v1a.to_string(index=False))

# Table V1B: Categorical Vendor Characteristics
categorical_stats = []

# Gender
if 'resp_gender' in df.columns:
    gender_counts = df['resp_gender'].value_counts()
    gender_pct = df['resp_gender'].value_counts(normalize=True) * 100
    for category in gender_counts.index:
        categorical_stats.append({
            'Variable': 'Vendor Gender',
            'Category': category,
            'N': gender_counts[category],
            'Percent': gender_pct[category]
        })

# Vendor Type
if 'vendortype' in df.columns:
    type_counts = df['vendortype'].value_counts()
    type_pct = df['vendortype'].value_counts(normalize=True) * 100
    for category in type_counts.index:
        categorical_stats.append({
            'Variable': 'Vendor Type',
            'Category': category,
            'N': type_counts[category],
            'Percent': type_pct[category]
        })

# Owner vs Not Owner
if 'resp_owner' in df.columns:
    owner_counts = df['resp_owner'].value_counts()
    owner_pct = df['resp_owner'].value_counts(normalize=True) * 100
    for category in owner_counts.index:
        categorical_stats.append({
            'Variable': 'Ownership Status',
            'Category': category,
            'N': owner_counts[category],
            'Percent': owner_pct[category]
        })

# Ethnicity
if 'resp_ethn' in df.columns:
    ethn_counts = df['resp_ethn'].value_counts()
    ethn_pct = df['resp_ethn'].value_counts(normalize=True) * 100
    for category in ethn_counts.index:
        categorical_stats.append({
            'Variable': 'Ethnicity',
            'Category': category,
            'N': ethn_counts[category],
            'Percent': ethn_pct[category]
        })

table_v1b = pd.DataFrame(categorical_stats)
table_v1b.to_csv(OUTPUT_DIR / "Table_V1B_Vendor_Demographics_Categorical.csv", index=False)
print("\n✓ Table V1B: Vendor Demographics (Categorical Variables)")
print(table_v1b.to_string(index=False))

# ============================================================================
# SECTION 2: WHERE THEY OPERATE
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 2: WHERE VENDORS OPERATE")
print("=" * 80)

# Table V2A: Geographic Distribution
location_stats = []

# Neighborhood
if 'neighborhood' in df.columns:
    neigh_counts = df['neighborhood'].value_counts().head(20)  # Top 20 neighborhoods
    neigh_pct = df['neighborhood'].value_counts(normalize=True).head(20) * 100
    for category in neigh_counts.index:
        location_stats.append({
            'Neighborhood': category,
            'N Vendors': neigh_counts[category],
            'Percent': neigh_pct[category]
        })

table_v2a = pd.DataFrame(location_stats)
table_v2a.to_csv(OUTPUT_DIR / "Table_V2A_Vendor_Geographic_Distribution.csv", index=False)
print("\n✓ Table V2A: Vendor Geographic Distribution (Top 20 Neighborhoods)")
print(table_v2a.to_string(index=False))

# ============================================================================
# SECTION 3: WHAT THEY SELL
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 3: WHAT VENDORS SELL (PRODUCT AVAILABILITY)")
print("=" * 80)

# Table V3A: Food Groups Sold
foodgroup_cols = [col for col in df.columns if col.startswith('foodgroups/')]

if foodgroup_cols:
    foodgroup_stats = []
    for col in foodgroup_cols:
        food_group = col.split('/')[-1]
        # Assuming binary (1 = sold, 0 = not sold)
        count = df[col].sum() if df[col].dtype in [int, float] else df[col].value_counts().get(1, 0)
        pct = (count / len(df)) * 100
        foodgroup_stats.append({
            'Food Group': food_group,
            'N Vendors Selling': count,
            'Percent': pct
        })

    table_v3a = pd.DataFrame(foodgroup_stats)
    table_v3a = table_v3a.sort_values('Percent', ascending=False)
    table_v3a.to_csv(OUTPUT_DIR / "Table_V3A_Food_Groups_Sold.csv", index=False)
    print("\n✓ Table V3A: Food Groups Sold (sorted by prevalence)")
    print(table_v3a.to_string(index=False))

# Table V3B: Product Diversity per Vendor
if foodgroup_cols:
    # Calculate product diversity as count of food groups sold per vendor
    df['product_diversity'] = df[foodgroup_cols].sum(axis=1)

    diversity_stats = pd.DataFrame({
        'Variable': ['Vendor Product Diversity (# of food groups)'],
        'N': [df['product_diversity'].notna().sum()],
        'Mean': [df['product_diversity'].mean()],
        'SD': [df['product_diversity'].std()],
        'Min': [df['product_diversity'].min()],
        'Median': [df['product_diversity'].median()],
        'Max': [df['product_diversity'].max()]
    })
    diversity_stats.to_csv(OUTPUT_DIR / "Table_V3B_Vendor_Product_Diversity.csv", index=False)
    print("\n✓ Table V3B: Vendor Product Diversity")
    print(diversity_stats.to_string(index=False))

# ============================================================================
# SECTION 4: VENDOR BUSINESS CHARACTERISTICS
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 4: VENDOR BUSINESS CHARACTERISTICS")
print("=" * 80)

# Table V4A: Whole vs Processed Foods
if 'wholeorprocessed' in df.columns:
    processed_counts = df['wholeorprocessed'].value_counts()
    processed_pct = df['wholeorprocessed'].value_counts(normalize=True) * 100

    processed_stats = []
    for category in processed_counts.index:
        processed_stats.append({
            'Product Type': category,
            'N Vendors': processed_counts[category],
            'Percent': processed_pct[category]
        })

    table_v4a = pd.DataFrame(processed_stats)
    table_v4a.to_csv(OUTPUT_DIR / "Table_V4A_Whole_vs_Processed_Foods.csv", index=False)
    print("\n✓ Table V4A: Whole vs Processed Foods")
    print(table_v4a.to_string(index=False))

# ============================================================================
# SECTION 5: INTEGRATED SUMMARY
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 5: INTEGRATED VENDOR SUMMARY")
print("=" * 80)

# Create comprehensive summary table
summary_data = {
    'Domain': [],
    'Indicator': [],
    'N': [],
    'Value': []
}

# Vendor Characteristics
summary_data['Domain'].append('Vendor Characteristics')
summary_data['Indicator'].append('Total Vendors Surveyed')
summary_data['N'].append(len(df))
summary_data['Value'].append(f"{len(df)} vendors")

if 'age' in df.columns:
    age_numeric = pd.to_numeric(df['age'], errors='coerce')
    summary_data['Domain'].append('Vendor Characteristics')
    summary_data['Indicator'].append('Mean Vendor Age')
    summary_data['N'].append(age_numeric.notna().sum())
    summary_data['Value'].append(f"{age_numeric.mean():.1f} ± {age_numeric.std():.1f} years")

# Geographic Distribution
if 'neighborhood' in df.columns:
    n_neighborhoods = df['neighborhood'].nunique()
    summary_data['Domain'].append('Geographic Distribution')
    summary_data['Indicator'].append('Number of Neighborhoods')
    summary_data['N'].append(len(df))
    summary_data['Value'].append(f"{n_neighborhoods} neighborhoods")

# Product Availability
if 'product_diversity' in df.columns:
    summary_data['Domain'].append('Product Availability')
    summary_data['Indicator'].append('Mean Product Diversity')
    summary_data['N'].append(df['product_diversity'].notna().sum())
    summary_data['Value'].append(f"{df['product_diversity'].mean():.2f} ± {df['product_diversity'].std():.2f} food groups")

# Vendor Type Distribution
if 'vendortype' in df.columns:
    modal_type = df['vendortype'].mode()[0] if len(df['vendortype'].mode()) > 0 else 'N/A'
    modal_pct = (df['vendortype'].value_counts().iloc[0] / len(df)) * 100 if len(df['vendortype'].value_counts()) > 0 else 0
    summary_data['Domain'].append('Business Model')
    summary_data['Indicator'].append('Most Common Vendor Type')
    summary_data['N'].append(len(df))
    summary_data['Value'].append(f"{modal_type} ({modal_pct:.1f}%)")

table_v5_summary = pd.DataFrame(summary_data)
table_v5_summary.to_csv(OUTPUT_DIR / "Table_V5_Vendor_Integrated_Summary.csv", index=False)
print("\n✓ Table V5: Vendor Integrated Summary")
print(table_v5_summary.to_string(index=False))

# ============================================================================
# COMPLETION
# ============================================================================

print("\n" + "=" * 80)
print("VENDOR LANDSCAPE REPORT GENERATION COMPLETE")
print("=" * 80)
print(f"\nAll tables saved to: {OUTPUT_DIR}")
print("\nGenerated tables:")
print("  - Table_V1A_Vendor_Demographics_Continuous.csv")
print("  - Table_V1B_Vendor_Demographics_Categorical.csv")
print("  - Table_V2A_Vendor_Geographic_Distribution.csv")
print("  - Table_V3A_Food_Groups_Sold.csv")
print("  - Table_V3B_Vendor_Product_Diversity.csv")
print("  - Table_V4A_Whole_vs_Processed_Foods.csv")
print("  - Table_V5_Vendor_Integrated_Summary.csv")
print("\n" + "=" * 80)
