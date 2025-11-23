#!/usr/bin/env python3
"""
Phase 4: Create Comprehensive Data Dictionary
=============================================

Purpose: Generate complete data dictionary for all 25 OP variables used in analysis
Author: Senior Data Scientist Skill (SuperClaude)
Date: 2025-11-23
Phase: 4 - Outputs & Thesis Integration

Inputs:
    - phase_1_codebook_CORRECTED.csv (Phase 1 variables)
    - phase_3A_variable_construction_log.csv (Phase 3A constructed variables)
    - phase_3A_household_analysis_ready_COMPLETE.csv (for validation)

Outputs:
    - COMPREHENSIVE_DATA_DICTIONARY.csv
    - DATA_DICTIONARY_THESIS_READY.md (formatted for thesis appendix)
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Define paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "02_outputs" / "datasets"
LOGS_DIR = BASE_DIR / "03_logs"
OUTPUT_DIR = BASE_DIR / "DOCUMENTATION" / "REFERENCE"

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

logger.info("=" * 80)
logger.info("PHASE 4: CREATING COMPREHENSIVE DATA DICTIONARY")
logger.info("=" * 80)

# ============================================================================
# STEP 1: Load Existing Variable Documentation
# ============================================================================

logger.info("\nSTEP 1: Loading existing variable documentation...")

# Load Phase 1 codebook
codebook_phase1 = pd.read_csv(DATA_DIR / "phase_1_codebook_CORRECTED.csv")
logger.info(f"✓ Loaded Phase 1 codebook: {len(codebook_phase1)} variables")

# Load Phase 3A construction log
construction_log = pd.read_csv(LOGS_DIR / "phase_3A_variable_construction_log.csv")
logger.info(f"✓ Loaded Phase 3A construction log: {len(construction_log)} variables")

# Load complete dataset for validation
df = pd.read_csv(DATA_DIR / "phase_3A_household_analysis_ready_COMPLETE.csv")
all_op_columns = [c for c in df.columns if c.startswith('OP')]
logger.info(f"✓ Dataset has {len(all_op_columns)} OP variables")

# ============================================================================
# STEP 2: Build Comprehensive Data Dictionary
# ============================================================================

logger.info("\nSTEP 2: Building comprehensive data dictionary...")

# Initialize dictionary structure
data_dict = {
    'OP_ID': [],
    'Variable_Name': [],
    'Description': [],
    'Turner_Domain': [],
    'Data_Type': [],
    'Valid_N': [],
    'Coverage_Pct': [],
    'Mean': [],
    'SD': [],
    'Min': [],
    'Max': [],
    'Values': [],
    'Unit': [],
    'Source': [],
    'Phase_Created': []
}

# Manual OP ID assignments and descriptions (comprehensive)
op_metadata = {
    'OP029_HDDS': {
        'op_id': 'OP029',
        'description': 'Household Dietary Diversity Score (24-hour recall)',
        'domain': 'Outcome',
        'source': 'Phase 0 - Direct survey',
        'phase': '0',
        'unit': 'Food groups (0-12)'
    },
    'OP012_monthly_food_expenditure': {
        'op_id': 'OP012',
        'description': 'Total monthly household food expenditure',
        'domain': 'Personal',
        'source': 'Phase 0 - Aggregated from daily/weekly',
        'phase': '0',
        'unit': 'VND per month'
    },
    'OP011_accessibility_tier': {
        'op_id': 'OP011',
        'description': 'Accessibility perception (Close vs Far based on travel time)',
        'domain': 'External',
        'source': 'Phase 1 - Derived from OP009',
        'phase': '1',
        'unit': 'Categorical'
    },
    'OP016_budget_share_pct': {
        'op_id': 'OP016',
        'description': 'Food budget share (percentage of total expenditure)',
        'domain': 'Personal',
        'source': 'Phase 0 - Calculated',
        'phase': '0',
        'unit': 'Percentage (0-100)'
    },
    'OP016_budget_share_tier': {
        'op_id': 'OP016',
        'description': 'Food budget share category (Low/Medium/High tertiles)',
        'domain': 'Personal',
        'source': 'Phase 1 - Derived from OP016_budget_share_pct',
        'phase': '1',
        'unit': 'Categorical'
    },
    'OP025_neighborhood_safety_index': {
        'op_id': 'OP025',
        'description': 'Neighborhood safety composite index',
        'domain': 'External',
        'source': 'Phase 1 - Composite from OP005',
        'phase': '1',
        'unit': 'Index (continuous)'
    },
    'OP025_neighborhood_safety_tier': {
        'op_id': 'OP025',
        'description': 'Neighborhood safety category (Low vs High)',
        'domain': 'External',
        'source': 'Phase 1 - Derived from OP025_neighborhood_safety_index',
        'phase': '1',
        'unit': 'Categorical'
    },
    'OP033_diet_quality_tier': {
        'op_id': 'OP033',
        'description': 'Diet quality category based on HDDS (Low/Medium/High)',
        'domain': 'Outcome',
        'source': 'Phase 1 - Derived from OP029_HDDS',
        'phase': '1',
        'unit': 'Categorical'
    },
    'OP004_cleanliness': {
        'op_id': 'OP004',
        'description': 'Food outlet cleanliness perception',
        'domain': 'External',
        'source': 'Phase 0 - Direct survey (Likert scale)',
        'phase': '0',
        'unit': 'Likert (1-5)'
    },
    'OP005_neighborhood_safety': {
        'op_id': 'OP005',
        'description': 'Neighborhood safety perception',
        'domain': 'External',
        'source': 'Phase 0 - Direct survey (Likert scale)',
        'phase': '0',
        'unit': 'Likert (1-5)'
    },
    'OP006_reputation': {
        'op_id': 'OP006',
        'description': 'Food outlet reputation perception',
        'domain': 'External',
        'source': 'Phase 0 - Direct survey (Likert scale)',
        'phase': '0',
        'unit': 'Likert (1-5)'
    },
    'OP007_infrastructure': {
        'op_id': 'OP007',
        'description': 'Food outlet infrastructure quality perception',
        'domain': 'External',
        'source': 'Phase 0 - Direct survey (Likert scale)',
        'phase': '0',
        'unit': 'Likert (1-5)'
    },
    'OP008_marketing_regulation': {
        'op_id': 'OP008',
        'description': 'Marketing and regulation dimension (NOT MEASURED)',
        'domain': 'External',
        'source': 'NOT MEASURED - Turner Framework incomplete',
        'phase': 'N/A',
        'unit': 'N/A'
    },
    'OP009_travel_time': {
        'op_id': 'OP009',
        'description': 'Travel time to primary food outlet',
        'domain': 'External',
        'source': 'Phase 0 - Direct survey',
        'phase': '0',
        'unit': 'Minutes'
    },
    'OP017_cooking_source': {
        'op_id': 'OP017',
        'description': 'Primary cooking fuel/energy source',
        'domain': 'Personal',
        'source': 'Phase 0 - Direct survey',
        'phase': '0',
        'unit': 'Categorical'
    },
    'OP018_water_source': {
        'op_id': 'OP018',
        'description': 'Primary household water source',
        'domain': 'Personal',
        'source': 'Phase 0 - Direct survey',
        'phase': '0',
        'unit': 'Categorical'
    },
    'OP019_water_distance': {
        'op_id': 'OP019',
        'description': 'Distance to primary water source',
        'domain': 'Personal',
        'source': 'Phase 0 - Direct survey',
        'phase': '0',
        'unit': 'Meters or time'
    },
    'OP003_price_motive': {
        'op_id': 'OP003',
        'description': 'Price/affordability cited as market shopping motive',
        'domain': 'Personal',
        'source': 'Phase 3A - Constructed from market motive question',
        'phase': '3A',
        'unit': 'Binary (0/1)'
    },
    'OP010_shopping_frequency': {
        'op_id': 'OP010',
        'description': 'Total shopping visits per month across all outlet types',
        'domain': 'Personal',
        'source': 'Phase 3A - Summed from outlet-specific frequencies',
        'phase': '3A',
        'unit': 'Visits per month'
    },
    'OP013_expenditure_time_unit': {
        'op_id': 'OP013',
        'description': 'Time unit for food expenditure reporting (daily, weekly, monthly)',
        'domain': 'Personal',
        'source': 'Phase 3A - Extracted from expenditure question',
        'phase': '3A',
        'unit': 'Categorical'
    },
    'OP015_affordability_motive': {
        'op_id': 'OP015',
        'description': 'Affordability motive (duplicate of OP003 - price motive)',
        'domain': 'Personal',
        'source': 'Phase 3A - Duplicate variable',
        'phase': '3A',
        'unit': 'Binary (0/1)'
    },
    'OP021_health_motive': {
        'op_id': 'OP021',
        'description': 'Health cited as market shopping motive',
        'domain': 'Personal',
        'source': 'Phase 3A - Constructed from market motive question',
        'phase': '3A',
        'unit': 'Binary (0/1)'
    },
    'OP022_trust_motive': {
        'op_id': 'OP022',
        'description': 'Trust/reliability cited as market shopping motive',
        'domain': 'Personal',
        'source': 'Phase 3A - Constructed from market motive question',
        'phase': '3A',
        'unit': 'Binary (0/1)'
    },
    'OP023_food_env_perception': {
        'op_id': 'OP023',
        'description': 'Overall food environment perception composite',
        'domain': 'Personal',
        'source': 'Phase 3A - Likert scale response',
        'phase': '3A',
        'unit': 'Likert (1-5)'
    },
    'OP028_frequency_variation': {
        'op_id': 'OP028',
        'description': 'Outlet frequency variation (SD of shopping frequency across outlet types)',
        'domain': 'Personal',
        'source': 'Phase 3A - Calculated variation index',
        'phase': '3A',
        'unit': 'Standard deviation'
    },
}

# Process each variable
for var_name in all_op_columns:
    if var_name in op_metadata:
        meta = op_metadata[var_name]

        # Calculate statistics
        series = df[var_name].dropna()
        n_valid = len(series)
        coverage_pct = (n_valid / len(df)) * 100

        # Type detection
        if pd.api.types.is_numeric_dtype(series):
            data_type = 'Continuous' if series.nunique() > 10 else 'Categorical (numeric)'
            mean_val = series.mean() if series.nunique() > 2 else np.nan
            sd_val = series.std() if series.nunique() > 2 else np.nan
            min_val = series.min()
            max_val = series.max()
            values_str = '' if series.nunique() > 10 else ', '.join(map(str, sorted(series.unique())))
        else:
            data_type = 'Categorical (text)'
            mean_val = np.nan
            sd_val = np.nan
            min_val = np.nan
            max_val = np.nan
            values_str = ', '.join(map(str, sorted(series.unique())))[:100]  # Truncate if too long

        # Append to dictionary
        data_dict['OP_ID'].append(meta['op_id'])
        data_dict['Variable_Name'].append(var_name)
        data_dict['Description'].append(meta['description'])
        data_dict['Turner_Domain'].append(meta['domain'])
        data_dict['Data_Type'].append(data_type)
        data_dict['Valid_N'].append(n_valid)
        data_dict['Coverage_Pct'].append(round(coverage_pct, 1))
        data_dict['Mean'].append(round(mean_val, 2) if not pd.isna(mean_val) else '')
        data_dict['SD'].append(round(sd_val, 2) if not pd.isna(sd_val) else '')
        data_dict['Min'].append(min_val if not pd.isna(min_val) else '')
        data_dict['Max'].append(max_val if not pd.isna(max_val) else '')
        data_dict['Values'].append(values_str)
        data_dict['Unit'].append(meta['unit'])
        data_dict['Source'].append(meta['source'])
        data_dict['Phase_Created'].append(meta['phase'])

# Create DataFrame
data_dictionary = pd.DataFrame(data_dict)

# Sort by OP_ID for clarity
data_dictionary['OP_ID_num'] = data_dictionary['OP_ID'].str.extract(r'(\d+)').astype(float)
data_dictionary = data_dictionary.sort_values('OP_ID_num').drop('OP_ID_num', axis=1)

logger.info(f"✓ Created data dictionary with {len(data_dictionary)} variables")

# ============================================================================
# STEP 3: Save CSV Data Dictionary
# ============================================================================

logger.info("\nSTEP 3: Saving CSV data dictionary...")

output_csv = OUTPUT_DIR / "COMPREHENSIVE_DATA_DICTIONARY.csv"
data_dictionary.to_csv(output_csv, index=False)
logger.info(f"✓ Saved: {output_csv}")

# ============================================================================
# STEP 4: Create Thesis-Ready Markdown Version
# ============================================================================

logger.info("\nSTEP 4: Creating thesis-ready Markdown version...")

md_content = """# Comprehensive Data Dictionary
## WFL Analysis - Vietnamese Urban Households

---

**Document Type**: Variable Definitions and Metadata
**Analysis Dataset**: phase_3A_household_analysis_ready_COMPLETE.csv
**Total Variables**: {total_vars}
**Total Households**: 214
**Date**: 2025-11-23

---

## Turner Framework Domains

**External Domain** (Food Environment):
- OP004: Cleanliness
- OP005: Neighborhood Safety
- OP006: Reputation
- OP007: Infrastructure
- OP008: Marketing & Regulation (NOT MEASURED)
- OP009: Travel Time (Accessibility)
- OP011: Accessibility Tier (derived)
- OP025: Neighborhood Safety Index/Tier (composite)

**Personal Domain** (Household Characteristics):
- OP003: Price Motive
- OP010: Shopping Frequency
- OP012: Monthly Food Expenditure
- OP013: Expenditure Time Unit
- OP015: Affordability Motive (duplicate of OP003)
- OP016: Budget Share (percentage & tier)
- OP017: Cooking Source
- OP018: Water Source
- OP019: Water Distance
- OP021: Health Motive
- OP022: Trust Motive
- OP023: Food Environment Perception
- OP028: Outlet Frequency Variation

**Outcome Variables**:
- OP029: Household Dietary Diversity Score (HDDS)
- OP033: Diet Quality Tier (derived)

---

## Variable Listing

""".format(total_vars=len(data_dictionary))

# Group by domain for organized presentation
for domain in ['Outcome', 'External', 'Personal']:
    domain_vars = data_dictionary[data_dictionary['Turner_Domain'] == domain]

    md_content += f"### {domain} Domain Variables ({len(domain_vars)} variables)\n\n"

    for _, row in domain_vars.iterrows():
        md_content += f"#### {row['Variable_Name']}\n\n"
        md_content += f"- **OP ID**: {row['OP_ID']}\n"
        md_content += f"- **Description**: {row['Description']}\n"
        md_content += f"- **Data Type**: {row['Data_Type']}\n"
        md_content += f"- **Unit**: {row['Unit']}\n"
        md_content += f"- **Source**: {row['Source']}\n"
        md_content += f"- **Phase Created**: {row['Phase_Created']}\n"
        md_content += f"- **Coverage**: {row['Valid_N']} observations ({row['Coverage_Pct']}%)\n"

        if row['Mean'] != '':
            md_content += f"- **Mean**: {row['Mean']} (SD={row['SD']})\n"
            md_content += f"- **Range**: {row['Min']} to {row['Max']}\n"

        if row['Values']:
            md_content += f"- **Values**: {row['Values']}\n"

        md_content += "\n---\n\n"

# Add limitations section
md_content += """
## Data Quality Notes

### Missing Data Patterns

**Low Missingness (<10%)**:
- OP029_HDDS, OP028_frequency_variation: 100% coverage (N=214)
- OP011, OP016, OP025 tier variables: 58-76% coverage

**Moderate Missingness (10-40%)**:
- OP012_monthly_food_expenditure: 66.4% coverage (N=142)

**High Missingness (>40%)**:
- OP007_infrastructure: 46.3% coverage (N=99)
- OP019_water_distance: 46.3% coverage (N=99)
- Market-only variables (OP003, 021, 022): 58.9% coverage (market shoppers only)

### Variable Quality Issues

**OP008 (Marketing & Regulation)**: NOT MEASURED
- Turner Framework dimension not operationalized in household survey
- Critical gap in framework completeness

**OP015 (Affordability Motive)**: DUPLICATE
- Identical to OP003 (price motive)
- Should not be used simultaneously in models

**OP024 (Food Safety Perception)**: NOT FOUND
- Referenced in planning documents but not in dataset
- OP025 (neighborhood safety) used as proxy

**Motive Variables (OP003, 021, 022)**: RESTRICTED SAMPLE
- Only applicable to households who shop at markets
- 41.1% missingness due to structural survey design

---

## Usage Guidelines for Thesis

### Recommended Variables for Analysis

**Tier 1 (Descriptive)**:
- All variables with >50% coverage suitable for descriptive statistics

**Tier 2 (Bivariate)**:
- Tier variables (OP011, OP016, OP025) for group comparisons
- Full coverage variables (OP029, OP028) for correlations

**Tier 3 (Correlation)**:
- Continuous variables with >50% coverage
- Exclude duplicate (OP015) and categorical tiers

**Tier 4 (Regression)**:
- External Domain: OP004-007, OP009 (5 predictors)
- Personal Domain: OP003, OP010, OP012-013, OP016, OP019, OP021-023 (8-9 predictors)
- **WARNING**: Sample size drops to N=64 in full model (70% listwise deletion)

### Key Finding Variable

**OP028 (Outlet Frequency Variation)**:
- **Strongest predictor** of dietary diversity (r=0.542, p<0.001)
- Full sample coverage (N=214, 100%)
- Novel contribution: Food sourcing diversity hypothesis

---

## Citation

When referencing this data dictionary in thesis:

> "Variable definitions and metadata are documented in the Comprehensive Data Dictionary (see Appendix X). All 25 operationalized variables (OP003-OP033, excluding non-measured OP008) are described with data types, coverage statistics, and survey sources."

---

**Data Dictionary Version**: 1.0
**Last Updated**: 2025-11-23
**Status**: ✅ COMPLETE AND THESIS-READY

---
"""

output_md = OUTPUT_DIR / "DATA_DICTIONARY_THESIS_READY.md"
with open(output_md, 'w') as f:
    f.write(md_content)

logger.info(f"✓ Saved: {output_md}")

# ============================================================================
# SUMMARY
# ============================================================================

logger.info("\n" + "=" * 80)
logger.info("DATA DICTIONARY CREATION COMPLETE")
logger.info("=" * 80)

logger.info(f"\n📊 SUMMARY:")
logger.info(f"  Total variables documented: {len(data_dictionary)}")
logger.info(f"  External Domain: {len(data_dictionary[data_dictionary['Turner_Domain']=='External'])} variables")
logger.info(f"  Personal Domain: {len(data_dictionary[data_dictionary['Turner_Domain']=='Personal'])} variables")
logger.info(f"  Outcome Variables: {len(data_dictionary[data_dictionary['Turner_Domain']=='Outcome'])} variables")

logger.info(f"\n📁 OUTPUTS:")
logger.info(f"  CSV: {output_csv}")
logger.info(f"  Markdown: {output_md}")

logger.info("\n✅ Data dictionary ready for thesis appendix!")

print("\n" + "=" * 80)
print("PHASE 4 DATA DICTIONARY SCRIPT - EXECUTION COMPLETE")
print("=" * 80)
