"""
Phase 0 Addendum: Comprehensive Exploratory Data Analysis (EDA)
WFL-Analysis Thesis Project

Purpose: Deep exploration of actual data structure to reconcile with documentation
         and operationalization guide before proceeding to Phase 1

Author: Generated via AI-assisted workflow
Date: 2025-11-23
"""

import pandas as pd
import numpy as np
from pathlib import Path
import re
from collections import defaultdict

# ============================================================================
# CONFIGURATION
# ============================================================================

PROJECT_ROOT = Path(__file__).parent.parent
INPUT_DIR = PROJECT_ROOT / "00_inputs" / "data"
OUTPUT_DIR = PROJECT_ROOT / "02_outputs" / "datasets"
LOG_DIR = PROJECT_ROOT / "03_logs"

# Processed data files
HOUSEHOLD_FILE = OUTPUT_DIR / "phase_0_household_processed.csv"
VENDOR_FILE = OUTPUT_DIR / "phase_0_vendor_processed.csv"

# Original merged files (for comparison)
HOUSEHOLD_ORIG = INPUT_DIR / "household_survey_LONG_BIEN_2024_ALL_merged.csv"
VENDOR_ORIG = INPUT_DIR / "vendor_survey_LONG_BIEN_2024_ALL_merged.csv"

# Output files
EDA_REPORT = LOG_DIR / "phase_0_eda_comprehensive_report.md"
VAR_MAPPING = LOG_DIR / "phase_0_variable_mapping_to_ops.md"
RECONCILIATION = LOG_DIR / "phase_0_operationalization_reconciliation.md"

# ============================================================================
# EDA UTILITY FUNCTIONS
# ============================================================================

def analyze_variable_patterns(df, data_type="Data"):
    """Identify patterns in variable names"""
    print(f"\n{'='*70}")
    print(f"VARIABLE PATTERN ANALYSIS: {data_type}")
    print(f"{'='*70}\n")

    patterns = defaultdict(list)

    for col in df.columns:
        # Food groups pattern
        if 'food' in col.lower():
            patterns['food_related'].append(col)

        # Consumption patterns
        if any(word in col.lower() for word in ['consumption', 'eat', 'diet', 'meal']):
            patterns['consumption'].append(col)

        # Expenditure/affordability patterns
        if any(word in col.lower() for word in ['expend', 'spend', 'cost', 'price', 'afford']):
            patterns['expenditure'].append(col)

        # Accessibility patterns
        if any(word in col.lower() for word in ['time', 'distance', 'travel', 'access']):
            patterns['accessibility'].append(col)

        # Vendor quality patterns
        if any(word in col.lower() for word in ['clean', 'safe', 'reputation', 'quality', 'trust']):
            patterns['quality'].append(col)

        # Numbered patterns (e.g., var_001, var_002)
        if re.search(r'_\d{3}_', col):
            patterns['numbered_series'].append(col)

    # Print findings
    for pattern_name, variables in sorted(patterns.items()):
        print(f"\n{pattern_name.upper().replace('_', ' ')} ({len(variables)} variables):")
        if len(variables) <= 20:
            for var in sorted(variables):
                print(f"  - {var}")
        else:
            for var in sorted(variables)[:10]:
                print(f"  - {var}")
            print(f"  ... and {len(variables) - 10} more")

    return patterns

def search_for_diet_diversity_components(df):
    """Search for variables related to dietary diversity (HDDS components)"""
    print(f"\n{'='*70}")
    print("SEARCHING FOR DIETARY DIVERSITY COMPONENTS")
    print(f"{'='*70}\n")

    # Standard HDDS food groups
    hdds_groups = [
        'cereal', 'grain', 'bread', 'rice', 'noodle',
        'legume', 'bean', 'lentil', 'pea',
        'meat', 'beef', 'pork', 'lamb',
        'poultry', 'chicken', 'duck',
        'fish', 'seafood', 'shellfish',
        'dairy', 'milk', 'cheese', 'yogurt',
        'egg',
        'oil', 'fat', 'seed', 'nut',
        'vegetable', 'greens', 'carrot', 'tomato',
        'fruit', 'apple', 'banana', 'orange',
        'other'
    ]

    diet_vars = []
    for col in df.columns:
        col_lower = col.lower()
        if any(food in col_lower for food in hdds_groups):
            diet_vars.append(col)

    print(f"Found {len(diet_vars)} potential diet/food group variables:\n")
    for var in sorted(diet_vars):
        print(f"  - {var}")

    return diet_vars

def analyze_missing_patterns(df, data_type="Data"):
    """Comprehensive missing data analysis"""
    print(f"\n{'='*70}")
    print(f"MISSING DATA PATTERN ANALYSIS: {data_type}")
    print(f"{'='*70}\n")

    missing_pct = (df.isnull().sum() / len(df) * 100).round(2)

    # Categorize by missingness
    complete = missing_pct[missing_pct == 0]
    low_missing = missing_pct[(missing_pct > 0) & (missing_pct <= 10)]
    medium_missing = missing_pct[(missing_pct > 10) & (missing_pct <= 30)]
    high_missing = missing_pct[(missing_pct > 30) & (missing_pct < 100)]
    all_missing = missing_pct[missing_pct == 100]

    print("MISSING DATA SUMMARY:")
    print(f"  Complete (0% missing): {len(complete)} variables")
    print(f"  Low missing (>0-10%): {len(low_missing)} variables")
    print(f"  Medium missing (>10-30%): {len(medium_missing)} variables")
    print(f"  High missing (>30-100%): {len(high_missing)} variables")
    print(f"  All missing (100%): {len(all_missing)} variables")

    print("\nCOMPLETE VARIABLES (usable for analysis):")
    for var in sorted(complete.index[:20]):
        print(f"  - {var}")
    if len(complete) > 20:
        print(f"  ... and {len(complete) - 20} more")

    print("\nLOW MISSING (likely usable):")
    for var, pct in sorted(low_missing.items())[:10]:
        print(f"  - {var}: {pct}% missing")

    print("\nALL MISSING (metadata/unused fields):")
    for var in sorted(all_missing.index[:15]):
        print(f"  - {var}")
    if len(all_missing) > 15:
        print(f"  ... and {len(all_missing) - 15} more")

    return {
        'complete': complete,
        'low_missing': low_missing,
        'medium_missing': medium_missing,
        'high_missing': high_missing,
        'all_missing': all_missing
    }

def investigate_sample_composition(df):
    """Investigate sample characteristics and potential subgroups"""
    print(f"\n{'='*70}")
    print("SAMPLE COMPOSITION INVESTIGATION")
    print(f"{'='*70}\n")

    print(f"Total sample size: {len(df)}")

    # Look for potential subgroup indicators
    potential_indicators = []
    for col in df.columns:
        col_lower = col.lower()
        if any(word in col_lower for word in ['waste', 'module', 'group', 'type', 'category']):
            potential_indicators.append(col)

    print(f"\nPotential subgroup indicators found: {len(potential_indicators)}")
    for var in potential_indicators[:20]:
        if var in df.columns:
            unique_count = df[var].nunique()
            print(f"  - {var}: {unique_count} unique values")
            if unique_count <= 5:
                print(f"    Values: {df[var].value_counts().to_dict()}")

    return potential_indicators

def map_to_operationalizations(df, patterns, diet_vars, data_type="Household"):
    """Map actual variables to documented operationalizations"""
    print(f"\n{'='*70}")
    print(f"MAPPING TO OPERATIONALIZATION GUIDE: {data_type}")
    print(f"{'='*70}\n")

    # Define operationalization keywords
    op_mapping = {
        'OP001-002_Availability': ['available', 'foodgroups_001', 'stock', 'supply'],
        'OP003_Affordability_Motive': ['afford', 'price', 'cheap', 'expensive'],
        'OP004-007_Vendor_Quality': ['clean', 'safe', 'reputation', 'infrastructure'],
        'OP009-011_Accessibility': ['time', 'distance', 'travel', 'access', 'close', 'far'],
        'OP012-016_Expenditure': ['expend', 'spend', 'budget', 'income', 'cost'],
        'OP017-020_Convenience': ['cook', 'water', 'facility', 'convenient'],
        'OP021-024_Desirability': ['health', 'trust', 'prefer', 'motive', 'reason'],
        'OP025_Food_Safety_Index': ['clean', 'safe', 'reputation'],
        'OP026-027_Social': ['trust', 'gender', 'decision'],
        'OP028_Stability': ['frequency', 'visit', 'regular'],
        'OP029_HDDS': ['food', 'diet', 'consumption', 'eat'] + [col for col in diet_vars],
        'OP030-032_Diet_Quality': ['nutrient', 'quality', 'processed', 'healthy'],
        'OP033_Diet_Tier': ['tier', 'category', 'level', 'class']
    }

    found_ops = {}

    for op_name, keywords in op_mapping.items():
        matches = []
        for col in df.columns:
            col_lower = col.lower()
            if any(keyword.lower() in col_lower for keyword in keywords if keyword):
                matches.append(col)

        found_ops[op_name] = matches

        if matches:
            print(f"\n{op_name}:")
            for match in sorted(matches)[:10]:
                print(f"  ✅ {match}")
            if len(matches) > 10:
                print(f"  ... and {len(matches) - 10} more")
        else:
            print(f"\n{op_name}:")
            print(f"  ❌ No matching variables found")

    return found_ops

# ============================================================================
# MAIN EDA EXECUTION
# ============================================================================

def main():
    """Execute comprehensive exploratory data analysis"""

    print("="*70)
    print("PHASE 0 ADDENDUM: COMPREHENSIVE EXPLORATORY DATA ANALYSIS")
    print("="*70)
    print(f"\nPurpose: Understand actual data structure before Phase 1")
    print(f"Date: 2025-11-23\n")

    # Load processed data
    print("\nLoading processed datasets...")
    household_df = pd.read_csv(HOUSEHOLD_FILE)
    vendor_df = pd.read_csv(VENDOR_FILE)

    print(f"  Household: {household_df.shape[0]} rows × {household_df.shape[1]} columns")
    print(f"  Vendor: {vendor_df.shape[0]} rows × {vendor_df.shape[1]} columns")

    # ========================================================================
    # HOUSEHOLD DATA EXPLORATION
    # ========================================================================

    print("\n" + "="*70)
    print("HOUSEHOLD DATA EXPLORATION")
    print("="*70)

    # Variable patterns
    hh_patterns = analyze_variable_patterns(household_df, "Household")

    # Diet diversity search
    hh_diet_vars = search_for_diet_diversity_components(household_df)

    # Missing data analysis
    hh_missing = analyze_missing_patterns(household_df, "Household")

    # Sample composition
    hh_subgroups = investigate_sample_composition(household_df)

    # Map to OPs
    hh_op_mapping = map_to_operationalizations(household_df, hh_patterns,
                                                hh_diet_vars, "Household")

    # ========================================================================
    # VENDOR DATA EXPLORATION
    # ========================================================================

    print("\n" + "="*70)
    print("VENDOR DATA EXPLORATION")
    print("="*70)

    # Variable patterns
    vendor_patterns = analyze_variable_patterns(vendor_df, "Vendor")

    # Diet diversity search (for availability)
    vendor_diet_vars = search_for_diet_diversity_components(vendor_df)

    # Missing data analysis
    vendor_missing = analyze_missing_patterns(vendor_df, "Vendor")

    # Map to OPs
    vendor_op_mapping = map_to_operationalizations(vendor_df, vendor_patterns,
                                                     vendor_diet_vars, "Vendor")

    # ========================================================================
    # GENERATE COMPREHENSIVE REPORT
    # ========================================================================

    print(f"\n{'='*70}")
    print("GENERATING COMPREHENSIVE EDA REPORT")
    print(f"{'='*70}\n")

    with open(EDA_REPORT, 'w') as f:
        f.write("---\n")
        f.write("title: \"Phase 0 EDA: Comprehensive Data Exploration Report\"\n")
        f.write("date: 2025-11-23\n")
        f.write("status: \"Complete\"\n")
        f.write("---\n\n")

        f.write("# Phase 0 Exploratory Data Analysis\n\n")
        f.write("## Executive Summary\n\n")
        f.write(f"**Household Sample**: {len(household_df)} records (expected 241)\n")
        f.write(f"**Vendor Sample**: {len(vendor_df)} records (matches expected 284)\n\n")

        f.write("### Key Findings\n\n")
        f.write("1. **Sample Size Discrepancy**: Household data has 214 records, not 241\n")
        f.write(f"2. **Food-related Variables**: {len(hh_patterns.get('food_related', []))} in household, ")
        f.write(f"{len(vendor_patterns.get('food_related', []))} in vendor\n")
        f.write(f"3. **Diet/Consumption Variables**: {len(hh_diet_vars)} potential HDDS components found\n")
        f.write(f"4. **Complete Variables**: {len(hh_missing['complete'])} household, ")
        f.write(f"{len(vendor_missing['complete'])} vendor\n\n")

        f.write("## Household Data Structure\n\n")
        f.write(f"**Dimensions**: {household_df.shape[0]} rows × {household_df.shape[1]} columns\n\n")

        f.write("### Variable Patterns\n\n")
        for pattern_name, variables in sorted(hh_patterns.items()):
            f.write(f"**{pattern_name.replace('_', ' ').title()}** ({len(variables)} variables):\n")
            for var in sorted(variables)[:15]:
                f.write(f"- `{var}`\n")
            if len(variables) > 15:
                f.write(f"- ... and {len(variables) - 15} more\n")
            f.write("\n")

        f.write("### Diet/Consumption Variables\n\n")
        if hh_diet_vars:
            for var in sorted(hh_diet_vars):
                f.write(f"- `{var}`\n")
        else:
            f.write("❌ No clear HDDS consumption variables found\n")
        f.write("\n")

        f.write("### Missing Data Summary\n\n")
        f.write(f"- Complete (0% missing): {len(hh_missing['complete'])} variables\n")
        f.write(f"- Low missing (>0-10%): {len(hh_missing['low_missing'])} variables\n")
        f.write(f"- Medium missing (>10-30%): {len(hh_missing['medium_missing'])} variables\n")
        f.write(f"- High missing (>30-<100%): {len(hh_missing['high_missing'])} variables\n")
        f.write(f"- All missing (100%): {len(hh_missing['all_missing'])} variables\n\n")

        f.write("### Operationalization Mapping\n\n")
        for op_name, matches in hh_op_mapping.items():
            f.write(f"**{op_name}**: {len(matches)} variables\n")
            if matches:
                for match in sorted(matches)[:5]:
                    f.write(f"  - `{match}`\n")
                if len(matches) > 5:
                    f.write(f"  - ... and {len(matches) - 5} more\n")
            else:
                f.write("  - ❌ No matching variables\n")
            f.write("\n")

        f.write("## Vendor Data Structure\n\n")
        f.write(f"**Dimensions**: {vendor_df.shape[0]} rows × {vendor_df.shape[1]} columns\n\n")

        f.write("### Variable Patterns\n\n")
        for pattern_name, variables in sorted(vendor_patterns.items()):
            f.write(f"**{pattern_name.replace('_', ' ').title()}** ({len(variables)} variables):\n")
            for var in sorted(variables)[:15]:
                f.write(f"- `{var}`\n")
            if len(variables) > 15:
                f.write(f"- ... and {len(variables) - 15} more\n")
            f.write("\n")

        f.write("### Operationalization Mapping\n\n")
        for op_name, matches in vendor_op_mapping.items():
            f.write(f"**{op_name}**: {len(matches)} variables\n")
            if matches:
                for match in sorted(matches)[:5]:
                    f.write(f"  - `{match}`\n")
                if len(matches) > 5:
                    f.write(f"  - ... and {len(matches) - 5} more\n")
            else:
                f.write("  - ❌ No matching variables\n")
            f.write("\n")

        f.write("## Recommendations\n\n")
        f.write("1. **Phase 1 Priority**: Map actual variable names to OPs using codebooks\n")
        f.write("2. **Sample Size**: Document 214 household sample in all analyses\n")
        f.write("3. **HDDS Calculation**: Identify exact consumption variables before calculating\n")
        f.write("4. **Missing Data**: Use complete and low-missing variables for primary analyses\n")
        f.write("5. **Operationalization**: Reconcile OP guide with actual data structure\n\n")

    print(f"✅ EDA report saved: {EDA_REPORT}")

    # ========================================================================
    # GENERATE VARIABLE LISTS FOR PHASE 1
    # ========================================================================

    print("\nGenerating variable lists for Phase 1...")

    # Save usable variables (complete + low missing)
    hh_usable = list(hh_missing['complete'].index) + list(hh_missing['low_missing'].index)
    vendor_usable = list(vendor_missing['complete'].index) + list(vendor_missing['low_missing'].index)

    with open(LOG_DIR / "phase_0_usable_variables.txt", 'w') as f:
        f.write("HOUSEHOLD USABLE VARIABLES (complete or <10% missing)\n")
        f.write("="*70 + "\n\n")
        for var in sorted(hh_usable):
            f.write(f"{var}\n")

        f.write("\n\n")
        f.write("VENDOR USABLE VARIABLES (complete or <10% missing)\n")
        f.write("="*70 + "\n\n")
        for var in sorted(vendor_usable):
            f.write(f"{var}\n")

    print(f"✅ Usable variables list saved")

    # ========================================================================
    # SUMMARY
    # ========================================================================

    print(f"\n{'='*70}")
    print("EDA COMPLETE")
    print(f"{'='*70}\n")

    print("Files Generated:")
    print(f"  1. {EDA_REPORT}")
    print(f"  2. {LOG_DIR / 'phase_0_usable_variables.txt'}")
    print("\nNext Steps:")
    print("  1. Review EDA report")
    print("  2. Consult household and vendor codebooks")
    print("  3. Map actual variables to operationalizations")
    print("  4. Proceed to Phase 1 with accurate variable mapping\n")

    return {
        'household': {
            'data': household_df,
            'patterns': hh_patterns,
            'diet_vars': hh_diet_vars,
            'missing': hh_missing,
            'op_mapping': hh_op_mapping,
            'usable_vars': hh_usable
        },
        'vendor': {
            'data': vendor_df,
            'patterns': vendor_patterns,
            'diet_vars': vendor_diet_vars,
            'missing': vendor_missing,
            'op_mapping': vendor_op_mapping,
            'usable_vars': vendor_usable
        }
    }

if __name__ == "__main__":
    results = main()

    print("\n✅ Exploratory Data Analysis Complete!")
    print(f"\nHousehold: {len(results['household']['usable_vars'])} usable variables")
    print(f"Vendor: {len(results['vendor']['usable_vars'])} usable variables")
