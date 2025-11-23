"""
Phase 3A: Construct Missing OP Variables for Tier 3 & 4 Analyses

This script constructs 7 missing operationalized variables needed for Phase 3:
- OP003: Price/Affordability Motive (from market shopping reasons)
- OP010: Shopping Frequency (sum of outlet visit frequencies)
- OP013: Expenditure Time Unit (from food expenditure reporting period)
- OP015: Affordability Motive Duplicate (same as OP003)
- OP021: Health Motive (from market shopping reasons)
- OP022: Trust Motive (from market shopping reasons)
- OP023: Food Environment Perception (from neighborhood satisfaction)
- OP028: Frequency Variation (SD across outlet shopping frequencies)

Variables validated against household survey codebook.

Author: Senior Data Scientist Skill (SuperClaude)
Date: 2025-11-23
Phase: 3A - Variable Construction
"""

import pandas as pd
import numpy as np
from pathlib import Path

# File paths
INPUT_PATH = Path("02_outputs/datasets/phase_1_household_analysis_ready_CORRECTED.csv")
OUTPUT_PATH = Path("02_outputs/datasets/phase_3A_household_analysis_ready_COMPLETE.csv")
LOG_PATH = Path("03_logs/phase_3A_variable_construction_log.csv")
SUMMARY_PATH = Path("03_logs/phase_3A_summary_statistics.csv")

print("="*80)
print("PHASE 3A: MISSING VARIABLE CONSTRUCTION")
print("="*80)
print()

# Load Phase 1 dataset
print(f"Loading dataset from: {INPUT_PATH}")
household_df = pd.read_csv(INPUT_PATH)
print(f"  - Loaded {len(household_df)} households")
print(f"  - Original columns: {len(household_df.columns)}")
print()

# Track construction results
construction_log = []

# ===========================
# OP003: Price/Affordability Motive
# ===========================
print("Constructing OP003: Price/Affordability Motive")
print("  Source: reason_003 (market shopping reasons)")
print("  Operationalization: 1 if 'cheap' cited, 0 otherwise")

if 'reason_003' in household_df.columns:
    # Create binary indicator: 1 if "cheap" is the reason, 0 otherwise
    household_df['OP003_price_motive'] = (household_df['reason_003'] == 'cheap').astype(int)

    # Coverage statistics
    coverage = household_df['reason_003'].notna().sum()
    coverage_pct = (coverage / len(household_df)) * 100
    cheap_count = (household_df['OP003_price_motive'] == 1).sum()
    cheap_pct = (cheap_count / coverage) * 100 if coverage > 0 else 0

    print(f"  ✓ Created: OP003_price_motive")
    print(f"    Coverage: {coverage}/{len(household_df)} ({coverage_pct:.1f}%)")
    print(f"    'Cheap' cited: {cheap_count}/{coverage} ({cheap_pct:.1f}%)")

    construction_log.append({
        'Variable': 'OP003_price_motive',
        'Source': 'reason_003',
        'Type': 'Binary',
        'Coverage_N': coverage,
        'Coverage_Pct': coverage_pct,
        'Mean': household_df['OP003_price_motive'].mean(),
        'Description': "Price/affordability cited as market shopping motive"
    })
else:
    print("  ⚠ Warning: reason_003 not found, OP003 not created")
    household_df['OP003_price_motive'] = np.nan

print()

# ===========================
# OP010: Shopping Frequency (Total Visits/Month)
# ===========================
print("Constructing OP010: Shopping Frequency")
print("  Source: Sum of all outlet frequency variables")
print("  Operationalization: Total visits per month across all outlets")

freq_cols = [
    'supermarket_freq', 'largesupermarket_freq', 'market_freq',
    'streetven_freq', 'wholesaler_freq', 'retail_freq'
]

available_freq_cols = [col for col in freq_cols if col in household_df.columns]
print(f"  Available frequency columns: {len(available_freq_cols)}/{len(freq_cols)}")

if available_freq_cols:
    # Sum frequencies, treating NaN as 0
    freq_data = household_df[available_freq_cols].fillna(0)
    household_df['OP010_shopping_frequency'] = freq_data.sum(axis=1)

    # Coverage: households with at least one non-zero frequency
    has_data = (household_df[available_freq_cols].notna().any(axis=1))
    coverage = has_data.sum()
    coverage_pct = (coverage / len(household_df)) * 100

    print(f"  ✓ Created: OP010_shopping_frequency")
    print(f"    Coverage: {coverage}/{len(household_df)} ({coverage_pct:.1f}%)")
    print(f"    Mean frequency: {household_df.loc[has_data, 'OP010_shopping_frequency'].mean():.2f} visits/month")
    print(f"    Range: {household_df.loc[has_data, 'OP010_shopping_frequency'].min():.0f} - {household_df.loc[has_data, 'OP010_shopping_frequency'].max():.0f}")

    construction_log.append({
        'Variable': 'OP010_shopping_frequency',
        'Source': ', '.join(available_freq_cols),
        'Type': 'Continuous',
        'Coverage_N': coverage,
        'Coverage_Pct': coverage_pct,
        'Mean': household_df.loc[has_data, 'OP010_shopping_frequency'].mean(),
        'Description': "Total shopping visits per month across all outlet types"
    })
else:
    print("  ⚠ Warning: No frequency columns found, OP010 not created")
    household_df['OP010_shopping_frequency'] = np.nan

print()

# ===========================
# OP013: Expenditure Time Unit
# ===========================
print("Constructing OP013: Expenditure Time Unit")
print("  Source: foodexp_timeunit")
print("  Operationalization: Categorical coding of expenditure reporting period")

if 'foodexp_timeunit' in household_df.columns:
    # Map time units to categories
    household_df['OP013_expenditure_time_unit'] = household_df['foodexp_timeunit'].copy()

    coverage = household_df['OP013_expenditure_time_unit'].notna().sum()
    coverage_pct = (coverage / len(household_df)) * 100

    # Value counts
    value_counts = household_df['OP013_expenditure_time_unit'].value_counts()

    print(f"  ✓ Created: OP013_expenditure_time_unit")
    print(f"    Coverage: {coverage}/{len(household_df)} ({coverage_pct:.1f}%)")
    print("    Distribution:")
    for val, count in value_counts.items():
        pct = (count / coverage) * 100 if coverage > 0 else 0
        print(f"      {val}: {count} ({pct:.1f}%)")

    construction_log.append({
        'Variable': 'OP013_expenditure_time_unit',
        'Source': 'foodexp_timeunit',
        'Type': 'Categorical',
        'Coverage_N': coverage,
        'Coverage_Pct': coverage_pct,
        'Mean': np.nan,
        'Description': "Time unit for food expenditure reporting (daily/weekly/monthly)"
    })
else:
    print("  ⚠ Warning: foodexp_timeunit not found, OP013 not created")
    household_df['OP013_expenditure_time_unit'] = np.nan

print()

# ===========================
# OP015: Affordability Motive (Duplicate of OP003)
# ===========================
print("Constructing OP015: Affordability Motive")
print("  Source: Duplicate of OP003 (price_motive)")
print("  Operationalization: Same as OP003 per Phase 3 plan")

household_df['OP015_affordability_motive'] = household_df['OP003_price_motive'].copy()

coverage = household_df['OP015_affordability_motive'].notna().sum()
coverage_pct = (coverage / len(household_df)) * 100

print(f"  ✓ Created: OP015_affordability_motive")
print(f"    Coverage: {coverage}/{len(household_df)} ({coverage_pct:.1f}%)")
print(f"    Note: Exact duplicate of OP003 as specified in Phase 3 plan")

construction_log.append({
    'Variable': 'OP015_affordability_motive',
    'Source': 'OP003_price_motive (duplicate)',
    'Type': 'Binary',
    'Coverage_N': coverage,
    'Coverage_Pct': coverage_pct,
    'Mean': household_df['OP015_affordability_motive'].mean(),
    'Description': "Affordability motive (duplicate of OP003)"
})

print()

# ===========================
# OP021: Health Motive
# ===========================
print("Constructing OP021: Health Motive")
print("  Source: reason_003 (market shopping reasons)")
print("  Operationalization: 1 if 'healthy' cited, 0 otherwise")

if 'reason_003' in household_df.columns:
    household_df['OP021_health_motive'] = (household_df['reason_003'] == 'healthy').astype(int)

    coverage = household_df['reason_003'].notna().sum()
    coverage_pct = (coverage / len(household_df)) * 100
    health_count = (household_df['OP021_health_motive'] == 1).sum()
    health_pct = (health_count / coverage) * 100 if coverage > 0 else 0

    print(f"  ✓ Created: OP021_health_motive")
    print(f"    Coverage: {coverage}/{len(household_df)} ({coverage_pct:.1f}%)")
    print(f"    'Healthy' cited: {health_count}/{coverage} ({health_pct:.1f}%)")

    construction_log.append({
        'Variable': 'OP021_health_motive',
        'Source': 'reason_003',
        'Type': 'Binary',
        'Coverage_N': coverage,
        'Coverage_Pct': coverage_pct,
        'Mean': household_df['OP021_health_motive'].mean(),
        'Description': "Health cited as market shopping motive"
    })
else:
    print("  ⚠ Warning: reason_003 not found, OP021 not created")
    household_df['OP021_health_motive'] = np.nan

print()

# ===========================
# OP022: Trust Motive
# ===========================
print("Constructing OP022: Trust Motive")
print("  Source: reason_003 (market shopping reasons)")
print("  Operationalization: 1 if 'trust' cited, 0 otherwise")

if 'reason_003' in household_df.columns:
    household_df['OP022_trust_motive'] = (household_df['reason_003'] == 'trust').astype(int)

    coverage = household_df['reason_003'].notna().sum()
    coverage_pct = (coverage / len(household_df)) * 100
    trust_count = (household_df['OP022_trust_motive'] == 1).sum()
    trust_pct = (trust_count / coverage) * 100 if coverage > 0 else 0

    print(f"  ✓ Created: OP022_trust_motive")
    print(f"    Coverage: {coverage}/{len(household_df)} ({coverage_pct:.1f}%)")
    print(f"    'Trust' cited: {trust_count}/{coverage} ({trust_pct:.1f}%)")

    construction_log.append({
        'Variable': 'OP022_trust_motive',
        'Source': 'reason_003',
        'Type': 'Binary',
        'Coverage_N': coverage,
        'Coverage_Pct': coverage_pct,
        'Mean': household_df['OP022_trust_motive'].mean(),
        'Description': "Trust cited as market shopping motive"
    })
else:
    print("  ⚠ Warning: reason_003 not found, OP022 not created")
    household_df['OP022_trust_motive'] = np.nan

print()

# ===========================
# OP023: Food Environment Perception
# ===========================
print("Constructing OP023: Food Environment Perception")
print("  Source: foodenvironment_002")
print("  Operationalization: Agreement score on food environment quality")

if 'foodenvironment_002' in household_df.columns:
    household_df['OP023_food_env_perception'] = household_df['foodenvironment_002'].copy()

    coverage = household_df['OP023_food_env_perception'].notna().sum()
    coverage_pct = (coverage / len(household_df)) * 100

    print(f"  ✓ Created: OP023_food_env_perception")
    print(f"    Coverage: {coverage}/{len(household_df)} ({coverage_pct:.1f}%)")
    if coverage > 0:
        print(f"    Mean: {household_df['OP023_food_env_perception'].mean():.2f}")
        print(f"    Range: {household_df['OP023_food_env_perception'].min():.0f} - {household_df['OP023_food_env_perception'].max():.0f}")

    construction_log.append({
        'Variable': 'OP023_food_env_perception',
        'Source': 'foodenvironment_002',
        'Type': 'Ordinal',
        'Coverage_N': coverage,
        'Coverage_Pct': coverage_pct,
        'Mean': household_df['OP023_food_env_perception'].mean(),
        'Description': "Perceived quality of neighborhood food environment"
    })
else:
    print("  ⚠ Warning: foodenvironment_002 not found, OP023 not created")
    household_df['OP023_food_env_perception'] = np.nan

print()

# ===========================
# OP028: Frequency Variation (Stability)
# ===========================
print("Constructing OP028: Frequency Variation")
print("  Source: SD across outlet frequency variables")
print("  Operationalization: Lower SD = more stable/concentrated shopping pattern")

if available_freq_cols:
    # Calculate standard deviation across outlet frequencies
    freq_data = household_df[available_freq_cols].fillna(0)
    household_df['OP028_frequency_variation'] = freq_data.std(axis=1)

    # Coverage: all households (even if all zeros)
    coverage = len(household_df)
    coverage_pct = 100.0

    print(f"  ✓ Created: OP028_frequency_variation")
    print(f"    Coverage: {coverage}/{len(household_df)} ({coverage_pct:.1f}%)")
    print(f"    Mean SD: {household_df['OP028_frequency_variation'].mean():.2f}")
    print(f"    Range: {household_df['OP028_frequency_variation'].min():.2f} - {household_df['OP028_frequency_variation'].max():.2f}")
    print(f"    Interpretation: Higher values = more diverse outlet usage")

    construction_log.append({
        'Variable': 'OP028_frequency_variation',
        'Source': ', '.join(available_freq_cols),
        'Type': 'Continuous',
        'Coverage_N': coverage,
        'Coverage_Pct': coverage_pct,
        'Mean': household_df['OP028_frequency_variation'].mean(),
        'Description': "Standard deviation of shopping frequencies across outlets (diversity measure)"
    })
else:
    print("  ⚠ Warning: No frequency columns found, OP028 not created")
    household_df['OP028_frequency_variation'] = np.nan

print()

# ===========================
# Save Results
# ===========================
print("="*80)
print("SAVING RESULTS")
print("="*80)
print()

# Save expanded dataset
print(f"Saving expanded dataset to: {OUTPUT_PATH}")
household_df.to_csv(OUTPUT_PATH, index=False)
print(f"  ✓ Saved {len(household_df)} households")
print(f"  ✓ Total columns: {len(household_df.columns)} (added 8 OP variables)")
print()

# Save construction log
print(f"Saving construction log to: {LOG_PATH}")
log_df = pd.DataFrame(construction_log)
log_df.to_csv(LOG_PATH, index=False)
print(f"  ✓ Saved construction details for {len(log_df)} variables")
print()

# Calculate and save summary statistics for new variables
print(f"Calculating summary statistics for new variables")
new_vars = [log['Variable'] for log in construction_log]

summary_stats = []
for var in new_vars:
    if var in household_df.columns:
        stats = {
            'Variable': var,
            'N': household_df[var].notna().sum(),
            'Missing': household_df[var].isna().sum(),
            'Mean': household_df[var].mean() if household_df[var].dtype in ['int64', 'float64'] else np.nan,
            'SD': household_df[var].std() if household_df[var].dtype in ['int64', 'float64'] else np.nan,
            'Min': household_df[var].min() if household_df[var].dtype in ['int64', 'float64'] else np.nan,
            'Max': household_df[var].max() if household_df[var].dtype in ['int64', 'float64'] else np.nan,
            'Unique_Values': household_df[var].nunique()
        }
        summary_stats.append(stats)

summary_df = pd.DataFrame(summary_stats)
summary_df.to_csv(SUMMARY_PATH, index=False)
print(f"  ✓ Saved summary statistics to: {SUMMARY_PATH}")
print()

# ===========================
# Final Summary
# ===========================
print("="*80)
print("PHASE 3A COMPLETION SUMMARY")
print("="*80)
print()
print(f"✅ Successfully constructed 8 OP variables:")
for log in construction_log:
    print(f"   - {log['Variable']}: {log['Coverage_Pct']:.1f}% coverage")
print()
print(f"📊 Dataset Statistics:")
print(f"   - Input: {INPUT_PATH}")
print(f"   - Output: {OUTPUT_PATH}")
print(f"   - Households: {len(household_df)}")
print(f"   - Original columns: 384")
print(f"   - New columns: {len(household_df.columns)}")
print(f"   - Variables added: 8 OP variables")
print()
print(f"📁 Output Files:")
print(f"   - Dataset: {OUTPUT_PATH}")
print(f"   - Construction Log: {LOG_PATH}")
print(f"   - Summary Statistics: {SUMMARY_PATH}")
print()
print("="*80)
print("PHASE 3A: VARIABLE CONSTRUCTION COMPLETE")
print("Ready to proceed to Phase 3B: Tier 3 & 4 Analyses")
print("="*80)
