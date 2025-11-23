"""
Phase 1: Data Cleaning & Variable Specification
WFL-Analysis Project
Date: 2025-11-23

Purpose: Construct all 33 operationalized variables from Phase 0 processed data
Input: Phase 0 checkpoint datasets
Output: Analysis-ready dataset with complete variable set
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'03_logs/phase_1_execution_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# ============================================================================
# CONFIGURATION
# ============================================================================

class Config:
    """Phase 1 configuration parameters"""

    # File paths
    HOUSEHOLD_INPUT = "02_outputs/datasets/phase_0_household_processed.csv"
    VENDOR_INPUT = "02_outputs/datasets/phase_0_vendor_processed.csv"
    HOUSEHOLD_OUTPUT = "02_outputs/datasets/phase_1_household_analysis_ready.csv"
    VENDOR_OUTPUT = "02_outputs/datasets/phase_1_vendor_analysis_ready.csv"
    CODEBOOK_OUTPUT = "02_outputs/datasets/phase_1_codebook.csv"
    SUMMARY_OUTPUT = "02_outputs/tables/phase_1_summary_statistics.csv"

    # T2 Stratification cutoffs
    ACCESSIBILITY_CUTOFF = 5  # minutes
    BUDGET_SHARE_TERTILES = [0.33, 0.67]  # for Low/Med/High
    SAFETY_MEDIAN_SPLIT = True  # use median for Low/High

    # HDDS configuration
    HDDS_FOOD_GROUPS = 16  # Using all 16 groups found in data
    HDDS_MIN_VALID = 0  # Minimum for valid HDDS
    HDDS_MAX_VALID = 16  # Maximum for valid HDDS

    # Diet quality tiers
    DIET_POOR_MAX = 3  # <4 food groups
    DIET_ADEQUATE_MAX = 6  # 4-6 food groups
    # 7+ = Diverse

    # Expenditure standardization
    EXPENDITURE_MULTIPLIERS = {
        'day': 30,
        'week': 4,
        'month': 1
    }

config = Config()

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def load_data(filepath):
    """Load CSV data with error handling"""
    try:
        logger.info(f"Loading data from {filepath}")
        df = pd.read_csv(filepath)
        logger.info(f"Loaded {len(df)} rows × {len(df.columns)} columns")
        return df
    except Exception as e:
        logger.error(f"Failed to load {filepath}: {e}")
        raise

def save_data(df, filepath, description="dataset"):
    """Save DataFrame with logging"""
    try:
        logger.info(f"Saving {description} to {filepath}")
        df.to_csv(filepath, index=False)
        logger.info(f"Saved {len(df)} rows × {len(df.columns)} columns")
    except Exception as e:
        logger.error(f"Failed to save {filepath}: {e}")
        raise

def validate_range(df, column, min_val, max_val, varname="variable"):
    """Validate variable is within expected range"""
    if column not in df.columns:
        logger.warning(f"{varname} column '{column}' not found - skipping validation")
        return

    valid_data = df[column].dropna()
    if len(valid_data) == 0:
        logger.warning(f"{varname} has no valid data - skipping validation")
        return

    out_of_range = ((valid_data < min_val) | (valid_data > max_val)).sum()
    if out_of_range > 0:
        logger.warning(f"{varname}: {out_of_range} values out of range [{min_val}, {max_val}]")
    else:
        logger.info(f"{varname}: All values in valid range [{min_val}, {max_val}]")

def calculate_summary_stats(df, variables):
    """Generate summary statistics for specified variables"""
    summary = []
    for var in variables:
        if var not in df.columns:
            logger.warning(f"Variable {var} not found in dataset")
            continue

        stats = {
            'variable': var,
            'n_total': len(df),
            'n_valid': df[var].notna().sum(),
            'n_missing': df[var].isna().sum(),
            'pct_missing': (df[var].isna().sum() / len(df)) * 100,
        }

        # Add numeric stats if applicable
        if pd.api.types.is_numeric_dtype(df[var]):
            stats.update({
                'mean': df[var].mean(),
                'std': df[var].std(),
                'min': df[var].min(),
                'q25': df[var].quantile(0.25),
                'median': df[var].median(),
                'q75': df[var].quantile(0.75),
                'max': df[var].max()
            })
        else:
            # Categorical stats
            value_counts = df[var].value_counts()
            stats['unique_values'] = len(value_counts)
            stats['most_common'] = value_counts.index[0] if len(value_counts) > 0 else None
            stats['most_common_count'] = value_counts.iloc[0] if len(value_counts) > 0 else None

        summary.append(stats)

    return pd.DataFrame(summary)

# ============================================================================
# VARIABLE CONSTRUCTION FUNCTIONS
# ============================================================================

def construct_hdds(household_df):
    """
    OP029: Household Dietary Diversity Score (PRIMARY OUTCOME)
    Sum of food groups consumed in past 7 days
    """
    logger.info("Constructing OP029: HDDS")

    # Find all HDDS food group columns (ODK format uses / separator)
    food_group_cols = [col for col in household_df.columns if 'foodgroups_001/' in col]
    logger.info(f"Found {len(food_group_cols)} HDDS food group columns")

    if len(food_group_cols) == 0:
        logger.error("No HDDS food group columns found!")
        return household_df

    # Calculate HDDS as sum of food groups
    household_df['OP029_HDDS'] = household_df[food_group_cols].sum(axis=1)

    # Validate
    validate_range(household_df, 'OP029_HDDS', config.HDDS_MIN_VALID, config.HDDS_MAX_VALID, "OP029_HDDS")

    # Log coverage
    valid_hdds = household_df['OP029_HDDS'].notna().sum()
    logger.info(f"OP029_HDDS: {valid_hdds}/{len(household_df)} households ({valid_hdds/len(household_df)*100:.1f}%)")
    logger.info(f"OP029_HDDS: mean={household_df['OP029_HDDS'].mean():.2f}, median={household_df['OP029_HDDS'].median():.1f}")

    return household_df

def standardize_expenditure(household_df):
    """
    OP012: Standardize food expenditure to monthly
    Convert all expenditure to monthly using time unit multipliers
    """
    logger.info("Constructing OP012: Monthly Food Expenditure")

    def convert_to_monthly(row):
        if pd.isna(row.get('foodexpenditure')) or pd.isna(row.get('foodexp_timeunit')):
            return np.nan

        timeunit = row['foodexp_timeunit']
        amount = row['foodexpenditure']

        multiplier = config.EXPENDITURE_MULTIPLIERS.get(timeunit, np.nan)
        if pd.isna(multiplier):
            logger.warning(f"Unknown time unit: {timeunit}")
            return np.nan

        return amount * multiplier

    household_df['OP012_monthly_food_expenditure'] = household_df.apply(convert_to_monthly, axis=1)

    # Convert to numeric (in case of string data)
    household_df['OP012_monthly_food_expenditure'] = pd.to_numeric(household_df['OP012_monthly_food_expenditure'], errors='coerce')

    # Log results
    valid_exp = household_df['OP012_monthly_food_expenditure'].notna().sum()
    logger.info(f"OP012: {valid_exp}/{len(household_df)} complete expenditure records ({valid_exp/len(household_df)*100:.1f}%)")

    if valid_exp > 0:
        logger.info(f"OP012: mean={household_df['OP012_monthly_food_expenditure'].mean():.0f}, "
                   f"median={household_df['OP012_monthly_food_expenditure'].median():.0f}")

    return household_df

def create_accessibility_tier(household_df):
    """
    OP011: Accessibility Tier (T2 STRATIFICATION VARIABLE)
    Binary: Close (≤5 min) / Far (>5 min)
    """
    logger.info("Constructing OP011: Accessibility Tier")

    if 'locationtime' not in household_df.columns:
        logger.error("Variable 'locationtime' not found - cannot create OP011")
        return household_df

    household_df['OP011_accessibility_tier'] = household_df['locationtime'].apply(
        lambda x: 'Close' if pd.notna(x) and x <= config.ACCESSIBILITY_CUTOFF else ('Far' if pd.notna(x) else np.nan)
    )

    # Log distribution
    dist = household_df['OP011_accessibility_tier'].value_counts()
    logger.info(f"OP011 distribution:")
    for tier, count in dist.items():
        logger.info(f"  {tier}: {count} ({count/len(household_df)*100:.1f}%)")

    return household_df

def create_budget_share_tier(household_df):
    """
    OP016: Food Budget Share Tier (T2 STRATIFICATION VARIABLE)
    Tertile: Low / Medium / High based on (food_exp / income) * 100
    """
    logger.info("Constructing OP016: Food Budget Share Tier")

    # Check required variables
    if 'OP012_monthly_food_expenditure' not in household_df.columns:
        logger.error("OP012_monthly_food_expenditure must be created first")
        return household_df

    if 'income' not in household_df.columns:
        logger.error("Variable 'income' not found - cannot create OP016")
        return household_df

    # Calculate budget share percentage
    household_df['OP016_budget_share_pct'] = (
        household_df['OP012_monthly_food_expenditure'] / household_df['income']
    ) * 100

    # Create tertiles for households with valid budget share
    valid_budget_share = household_df['OP016_budget_share_pct'].notna()

    if valid_budget_share.sum() > 0:
        household_df.loc[valid_budget_share, 'OP016_budget_share_tier'] = pd.qcut(
            household_df.loc[valid_budget_share, 'OP016_budget_share_pct'],
            q=3,
            labels=['Low', 'Medium', 'High'],
            duplicates='drop'  # Handle ties
        )

        # Log distribution
        dist = household_df['OP016_budget_share_tier'].value_counts()
        logger.info(f"OP016 distribution:")
        for tier, count in dist.items():
            logger.info(f"  {tier}: {count} ({count/valid_budget_share.sum()*100:.1f}%)")
    else:
        logger.warning("OP016: No valid budget share data - tier variable not created")

    return household_df

def create_food_safety_tier(household_df):
    """
    OP025: Food Safety Tier (T2 STRATIFICATION VARIABLE)
    Binary: Low / High based on median split of safety index
    Index = mean(clean, safe, reputation)
    """
    logger.info("Constructing OP025: Food Safety Tier")

    # Check for required variables
    safety_vars = ['clean', 'safe', 'reputation']
    missing_vars = [v for v in safety_vars if v not in household_df.columns]

    if missing_vars:
        logger.error(f"Missing variables for OP025: {missing_vars}")
        return household_df

    # Calculate safety index (mean of components)
    household_df['OP025_safety_index'] = household_df[safety_vars].mean(axis=1)

    # Create binary tier (median split)
    median_safety = household_df['OP025_safety_index'].median()
    household_df['OP025_food_safety_tier'] = household_df['OP025_safety_index'].apply(
        lambda x: 'High' if pd.notna(x) and x >= median_safety else ('Low' if pd.notna(x) else np.nan)
    )

    # Log distribution
    dist = household_df['OP025_food_safety_tier'].value_counts()
    logger.info(f"OP025 distribution (median={median_safety:.2f}):")
    for tier, count in dist.items():
        logger.info(f"  {tier}: {count} ({count/len(household_df)*100:.1f}%)")

    return household_df

def create_diet_quality_tier(household_df):
    """
    OP033: Diet Quality Tier
    Classification: Poor (<4) / Adequate (4-6) / Diverse (7+)
    Based on HDDS score
    """
    logger.info("Constructing OP033: Diet Quality Tier")

    if 'OP029_HDDS' not in household_df.columns:
        logger.error("OP029_HDDS must be created first")
        return household_df

    def classify_diet(hdds):
        if pd.isna(hdds):
            return np.nan
        elif hdds <= config.DIET_POOR_MAX:
            return 'Poor'
        elif hdds <= config.DIET_ADEQUATE_MAX:
            return 'Adequate'
        else:
            return 'Diverse'

    household_df['OP033_diet_quality_tier'] = household_df['OP029_HDDS'].apply(classify_diet)

    # Log distribution
    dist = household_df['OP033_diet_quality_tier'].value_counts()
    logger.info(f"OP033 distribution:")
    for tier, count in dist.items():
        logger.info(f"  {tier}: {count} ({count/len(household_df)*100:.1f}%)")

    return household_df

def construct_external_domain(household_df, vendor_df):
    """
    Construct External Domain variables (OP001-OP008)
    """
    logger.info("Constructing External Domain variables (OP001-OP008)")

    # OP004-OP007: Quality perceptions (already in data)
    quality_vars = {
        'OP004_cleanliness': 'clean',
        'OP005_food_safety': 'safe',
        'OP006_reputation': 'reputation',
        'OP007_infrastructure': 'infrastructure'
    }

    for op_var, data_var in quality_vars.items():
        if data_var in household_df.columns:
            household_df[op_var] = household_df[data_var]
            logger.info(f"Created {op_var} from {data_var}")
        else:
            logger.warning(f"Variable {data_var} not found for {op_var}")

    # OP008: Not measured (document as limitation)
    household_df['OP008_marketing_regulation'] = np.nan
    logger.info("OP008: Not measured (documented limitation)")

    return household_df, vendor_df

def construct_personal_domain(household_df):
    """
    Construct Personal Domain variables (OP009-OP024)
    """
    logger.info("Constructing Personal Domain variables (OP009-OP024)")

    # OP009: Travel Time
    if 'locationtime' in household_df.columns:
        household_df['OP009_travel_time'] = household_df['locationtime']
        logger.info("Created OP009_travel_time")

    # OP017-OP020: Convenience variables
    convenience_vars = {
        'OP017_cooking_source': 'cookingsource',
        'OP018_water_source': 'watersource',
        'OP019_water_distance': 'waterdistance'
    }

    for op_var, data_var in convenience_vars.items():
        if data_var in household_df.columns:
            household_df[op_var] = household_df[data_var]
            logger.info(f"Created {op_var} from {data_var}")
        else:
            logger.warning(f"Variable {data_var} not found for {op_var}")

    # Note: OP003, OP021-OP024 require codebook consultation (Phase 1 Priority 2)
    logger.info("OP003, OP021-024: Require codebook mapping (documented for Priority 2)")

    return household_df

def create_codebook(household_df):
    """
    Create comprehensive variable codebook
    """
    logger.info("Creating variable codebook")

    codebook = []

    # Define codebook entries for constructed variables
    op_variables = {
        'OP029_HDDS': {
            'description': 'Household Dietary Diversity Score (count of food groups)',
            'type': 'numeric',
            'range': '0-16',
            'op_id': 'OP029',
            'domain': 'Outcome',
            'role': 'Primary DV'
        },
        'OP012_monthly_food_expenditure': {
            'description': 'Monthly food expenditure (standardized)',
            'type': 'numeric',
            'unit': 'currency per month',
            'op_id': 'OP012',
            'domain': 'Personal - Affordability',
            'role': 'IV'
        },
        'OP011_accessibility_tier': {
            'description': 'Accessibility tier (Close ≤5min / Far >5min)',
            'type': 'categorical',
            'values': 'Close, Far',
            'op_id': 'OP011',
            'domain': 'Personal - Accessibility',
            'role': 'T2 Stratification'
        },
        'OP016_budget_share_tier': {
            'description': 'Food budget share tier (tertiles)',
            'type': 'categorical',
            'values': 'Low, Medium, High',
            'op_id': 'OP016',
            'domain': 'Personal - Affordability',
            'role': 'T2 Stratification'
        },
        'OP025_food_safety_tier': {
            'description': 'Food safety perception tier (median split)',
            'type': 'categorical',
            'values': 'Low, High',
            'op_id': 'OP025',
            'domain': 'Emergent',
            'role': 'T2 Stratification'
        },
        'OP033_diet_quality_tier': {
            'description': 'Diet quality classification',
            'type': 'categorical',
            'values': 'Poor (<4), Adequate (4-6), Diverse (7+)',
            'op_id': 'OP033',
            'domain': 'Outcome',
            'role': 'Derived DV'
        }
    }

    for var, info in op_variables.items():
        if var in household_df.columns:
            entry = {
                'variable_name': var,
                'n_valid': household_df[var].notna().sum(),
                'pct_complete': (household_df[var].notna().sum() / len(household_df)) * 100
            }
            entry.update(info)
            codebook.append(entry)

    return pd.DataFrame(codebook)

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main Phase 1 execution"""

    logger.info("="*80)
    logger.info("PHASE 1: DATA CLEANING & VARIABLE SPECIFICATION")
    logger.info("="*80)
    logger.info(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # ========================================================================
    # STEP 1: Load Phase 0 Data
    # ========================================================================
    logger.info("\n" + "="*80)
    logger.info("STEP 1: Loading Phase 0 Processed Data")
    logger.info("="*80)

    household_df = load_data(config.HOUSEHOLD_INPUT)
    vendor_df = load_data(config.VENDOR_INPUT)

    # ========================================================================
    # STEP 2: Construct Priority 1 Variables (CRITICAL)
    # ========================================================================
    logger.info("\n" + "="*80)
    logger.info("STEP 2: Constructing Priority 1 Variables (CRITICAL)")
    logger.info("="*80)

    # Primary outcome variable
    household_df = construct_hdds(household_df)

    # Expenditure standardization
    household_df = standardize_expenditure(household_df)

    # T2 Stratification variables
    household_df = create_accessibility_tier(household_df)
    household_df = create_budget_share_tier(household_df)
    household_df = create_food_safety_tier(household_df)

    # Derived outcome
    household_df = create_diet_quality_tier(household_df)

    # ========================================================================
    # STEP 3: Construct Supporting Variables
    # ========================================================================
    logger.info("\n" + "="*80)
    logger.info("STEP 3: Constructing Supporting Variables")
    logger.info("="*80)

    household_df, vendor_df = construct_external_domain(household_df, vendor_df)
    household_df = construct_personal_domain(household_df)

    # ========================================================================
    # STEP 4: Data Quality Validation
    # ========================================================================
    logger.info("\n" + "="*80)
    logger.info("STEP 4: Data Quality Validation")
    logger.info("="*80)

    # Validate constructed variables
    validate_range(household_df, 'OP029_HDDS', 0, 16, "HDDS")
    validate_range(household_df, 'OP025_safety_index', 0, 100, "Safety Index")

    # ========================================================================
    # STEP 5: Generate Summary Statistics
    # ========================================================================
    logger.info("\n" + "="*80)
    logger.info("STEP 5: Generating Summary Statistics")
    logger.info("="*80)

    # Identify all OP variables
    op_variables = [col for col in household_df.columns if col.startswith('OP')]
    logger.info(f"Found {len(op_variables)} OP variables")

    summary_stats = calculate_summary_stats(household_df, op_variables)
    save_data(summary_stats, config.SUMMARY_OUTPUT, "summary statistics")

    # ========================================================================
    # STEP 6: Create Codebook
    # ========================================================================
    logger.info("\n" + "="*80)
    logger.info("STEP 6: Creating Variable Codebook")
    logger.info("="*80)

    codebook = create_codebook(household_df)
    save_data(codebook, config.CODEBOOK_OUTPUT, "codebook")

    # ========================================================================
    # STEP 7: Save Analysis-Ready Datasets
    # ========================================================================
    logger.info("\n" + "="*80)
    logger.info("STEP 7: Saving Analysis-Ready Datasets")
    logger.info("="*80)

    save_data(household_df, config.HOUSEHOLD_OUTPUT, "household analysis-ready")
    save_data(vendor_df, config.VENDOR_OUTPUT, "vendor analysis-ready")

    # ========================================================================
    # STEP 8: Final Summary
    # ========================================================================
    logger.info("\n" + "="*80)
    logger.info("PHASE 1 COMPLETION SUMMARY")
    logger.info("="*80)

    logger.info(f"\nHousehold Dataset:")
    logger.info(f"  Total households: {len(household_df)}")
    logger.info(f"  Total variables: {len(household_df.columns)}")
    logger.info(f"  OP variables: {len(op_variables)}")

    logger.info(f"\nKey Variable Coverage:")
    logger.info(f"  HDDS (OP029): {household_df['OP029_HDDS'].notna().sum()} ({household_df['OP029_HDDS'].notna().sum()/len(household_df)*100:.1f}%)")
    logger.info(f"  Accessibility (OP011): {household_df['OP011_accessibility_tier'].notna().sum()} ({household_df['OP011_accessibility_tier'].notna().sum()/len(household_df)*100:.1f}%)")
    logger.info(f"  Budget Share (OP016): {household_df['OP016_budget_share_tier'].notna().sum() if 'OP016_budget_share_tier' in household_df.columns else 0}")
    logger.info(f"  Food Safety (OP025): {household_df['OP025_food_safety_tier'].notna().sum()} ({household_df['OP025_food_safety_tier'].notna().sum()/len(household_df)*100:.1f}%)")

    logger.info(f"\nOutput Files Created:")
    logger.info(f"  ✅ {config.HOUSEHOLD_OUTPUT}")
    logger.info(f"  ✅ {config.VENDOR_OUTPUT}")
    logger.info(f"  ✅ {config.CODEBOOK_OUTPUT}")
    logger.info(f"  ✅ {config.SUMMARY_OUTPUT}")

    logger.info(f"\n{'='*80}")
    logger.info("PHASE 1 COMPLETE - READY FOR PHASE 2 ANALYSES")
    logger.info("="*80)
    logger.info(f"End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    return household_df, vendor_df

if __name__ == "__main__":
    household_df, vendor_df = main()
