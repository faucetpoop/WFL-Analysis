"""
Phase 0: Setup & Data Consolidation
WFL-Analysis Thesis Project

Purpose: Load, consolidate, and prepare raw household and vendor survey data
Duration: ~2-3 hours
Output: Clean checkpoint datasets ready for Phase 1 analysis

Author: Generated via AI-assisted workflow
Date: 2025-11-23
"""

import pandas as pd
import numpy as np
from pathlib import Path
import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
INPUT_DIR = PROJECT_ROOT / "00_inputs" / "data"
OUTPUT_DIR = PROJECT_ROOT / "02_outputs" / "datasets"
LOG_DIR = PROJECT_ROOT / "03_logs"

# Input files
HOUSEHOLD_FILE = INPUT_DIR / "household_survey_LONG_BIEN_2024_ALL_merged.csv"
VENDOR_FILE = INPUT_DIR / "vendor_survey_LONG_BIEN_2024_ALL_merged.csv"

# Output files
HOUSEHOLD_OUTPUT = OUTPUT_DIR / "phase_0_household_processed.csv"
VENDOR_OUTPUT = OUTPUT_DIR / "phase_0_vendor_processed.csv"
LOG_FILE = LOG_DIR / "phase_0_data_consolidation_log.md"

# Expected sample sizes
EXPECTED_HOUSEHOLD_N = 241
EXPECTED_VENDOR_N = 284

# ============================================================================
# LOGGING SETUP
# ============================================================================

class Logger:
    """Simple logger to track Phase 0 execution"""

    def __init__(self, log_path):
        self.log_path = log_path
        self.messages = []
        self.start_time = datetime.datetime.now()

    def log(self, message, level="INFO"):
        """Add message to log"""
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_line = f"[{timestamp}] {level}: {message}"
        self.messages.append(log_line)
        print(log_line)

    def save(self):
        """Save log to markdown file"""
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

        end_time = datetime.datetime.now()
        duration = (end_time - self.start_time).total_seconds()

        with open(self.log_path, 'w') as f:
            f.write("---\n")
            f.write("title: \"Phase 0: Data Consolidation Log\"\n")
            f.write(f"date: {self.start_time.strftime('%Y-%m-%d')}\n")
            f.write(f"duration: {duration:.1f} seconds\n")
            f.write("---\n\n")
            f.write("# Phase 0 Data Consolidation Log\n\n")
            f.write(f"**Start Time**: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**End Time**: {end_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Duration**: {duration:.1f} seconds\n\n")
            f.write("## Execution Log\n\n")
            f.write("```\n")
            for msg in self.messages:
                f.write(msg + "\n")
            f.write("```\n")

        print(f"\n✅ Log saved to: {self.log_path}")

# Initialize logger
logger = Logger(LOG_FILE)

# ============================================================================
# PHASE 0: DATA LOADING
# ============================================================================

def load_household_data():
    """Load household survey data with proper handling"""
    logger.log("Loading household survey data...")
    logger.log(f"   File: {HOUSEHOLD_FILE}")

    try:
        df = pd.read_csv(HOUSEHOLD_FILE, low_memory=False)
        logger.log(f"   ✅ Loaded {len(df)} rows, {len(df.columns)} columns")
        return df
    except FileNotFoundError:
        logger.log(f"   ❌ ERROR: File not found: {HOUSEHOLD_FILE}", "ERROR")
        raise
    except Exception as e:
        logger.log(f"   ❌ ERROR: {str(e)}", "ERROR")
        raise

def load_vendor_data():
    """Load vendor survey data"""
    logger.log("Loading vendor survey data...")
    logger.log(f"   File: {VENDOR_FILE}")

    try:
        df = pd.read_csv(VENDOR_FILE, low_memory=False)
        logger.log(f"   ✅ Loaded {len(df)} rows, {len(df.columns)} columns")
        return df
    except FileNotFoundError:
        logger.log(f"   ❌ ERROR: File not found: {VENDOR_FILE}", "ERROR")
        raise
    except Exception as e:
        logger.log(f"   ❌ ERROR: {str(e)}", "ERROR")
        raise

# ============================================================================
# PHASE 0: CRITICAL VARIABLE RENAMING
# ============================================================================

def rename_household_variables(df):
    """
    CRITICAL: Rename foodgroups variables to avoid naming conflicts

    Conflict:
        foodgroups_001_* = Consumption items (for HDDS calculation)
        foodgroups = Sales string (for vendor analysis)

    Solution:
        foodgroups_001_* → hh_consumption_*
        foodgroups → hh_sales_string
    """
    logger.log("🚨 CRITICAL: Renaming household variables to avoid conflicts...")

    # Find all foodgroups_001_* columns
    foodgroups_consumption_cols = [col for col in df.columns if col.startswith('foodgroups_001_')]
    logger.log(f"   Found {len(foodgroups_consumption_cols)} consumption columns to rename")

    # Check if plain 'foodgroups' exists
    has_sales_string = 'foodgroups' in df.columns
    logger.log(f"   'foodgroups' sales string present: {has_sales_string}")

    # Create renaming dictionary
    rename_dict = {}

    # Rename foodgroups_001_* → hh_consumption_*
    for col in foodgroups_consumption_cols:
        new_name = col.replace('foodgroups_001_', 'hh_consumption_')
        rename_dict[col] = new_name
        logger.log(f"      {col} → {new_name}")

    # Rename foodgroups → hh_sales_string
    if has_sales_string:
        rename_dict['foodgroups'] = 'hh_sales_string'
        logger.log(f"      foodgroups → hh_sales_string")

    # Execute renaming
    df_renamed = df.rename(columns=rename_dict)
    logger.log(f"   ✅ Renamed {len(rename_dict)} variables")

    # Verify no conflicts remain
    remaining_conflicts = [col for col in df_renamed.columns if col.startswith('foodgroups_001_')]
    if remaining_conflicts:
        logger.log(f"   ⚠️  WARNING: {len(remaining_conflicts)} conflicts remain!", "WARNING")
    else:
        logger.log("   ✅ No naming conflicts remain")

    return df_renamed

# ============================================================================
# PHASE 0: DATA QUALITY CHECKS
# ============================================================================

def verify_sample_size(df, expected_n, data_type="Data"):
    """Verify data has expected number of rows"""
    actual_n = len(df)
    if actual_n == expected_n:
        logger.log(f"   ✅ {data_type} sample size: {actual_n} (matches expected {expected_n})")
        return True
    else:
        logger.log(f"   ⚠️  {data_type} sample size: {actual_n} (expected {expected_n})", "WARNING")
        return False

def check_missing_data(df, data_type="Data"):
    """Assess missing data patterns"""
    logger.log(f"Assessing missing data for {data_type}...")

    # Calculate missing percentages
    missing_pct = (df.isnull().sum() / len(df) * 100).round(2)

    # Identify high-missing variables
    high_missing = missing_pct[missing_pct > 10].sort_values(ascending=False)

    if len(high_missing) > 0:
        logger.log(f"   ⚠️  {len(high_missing)} variables with >10% missing data")
        for var, pct in high_missing.head(10).items():
            logger.log(f"      {var}: {pct}%")
    else:
        logger.log(f"   ✅ No variables with >10% missing data")

    return missing_pct

def check_data_types(df, data_type="Data"):
    """Verify data types are appropriate"""
    logger.log(f"Checking data types for {data_type}...")

    dtype_summary = df.dtypes.value_counts()
    for dtype, count in dtype_summary.items():
        logger.log(f"   {dtype}: {count} columns")

    return True

def check_duplicates(df, id_col=None, data_type="Data"):
    """Check for duplicate rows or IDs"""
    logger.log(f"Checking for duplicates in {data_type}...")

    # Check for completely duplicate rows
    dup_rows = df.duplicated().sum()
    if dup_rows > 0:
        logger.log(f"   ⚠️  {dup_rows} duplicate rows found", "WARNING")
    else:
        logger.log(f"   ✅ No duplicate rows")

    # Check for duplicate IDs if ID column specified
    if id_col and id_col in df.columns:
        dup_ids = df[id_col].duplicated().sum()
        if dup_ids > 0:
            logger.log(f"   ⚠️  {dup_ids} duplicate {id_col} values found", "WARNING")
        else:
            logger.log(f"   ✅ No duplicate {id_col} values")

    return dup_rows == 0

# ============================================================================
# PHASE 0: SAVE PROCESSED DATA
# ============================================================================

def save_processed_data(df, output_path, data_type="Data"):
    """Save processed dataset to output directory"""
    logger.log(f"Saving processed {data_type}...")
    logger.log(f"   Output: {output_path}")

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save to CSV
    df.to_csv(output_path, index=False)
    logger.log(f"   ✅ Saved {len(df)} rows, {len(df.columns)} columns")

    # Verify file was created
    if output_path.exists():
        file_size = output_path.stat().st_size / 1024  # KB
        logger.log(f"   ✅ File size: {file_size:.1f} KB")
    else:
        logger.log(f"   ❌ ERROR: File not created", "ERROR")

# ============================================================================
# PHASE 0: MAIN EXECUTION
# ============================================================================

def main():
    """Execute Phase 0: Data Consolidation"""

    logger.log("=" * 70)
    logger.log("PHASE 0: SETUP & DATA CONSOLIDATION")
    logger.log("=" * 70)
    logger.log("")

    # ========================================================================
    # STEP 1: LOAD DATA
    # ========================================================================
    logger.log("STEP 1: Loading data files...")
    logger.log("")

    household_df = load_household_data()
    vendor_df = load_vendor_data()

    logger.log("")
    logger.log("✅ STEP 1 COMPLETE: Data loading successful")
    logger.log("")

    # ========================================================================
    # STEP 2: VERIFY SAMPLE SIZES
    # ========================================================================
    logger.log("STEP 2: Verifying sample sizes...")
    logger.log("")

    household_ok = verify_sample_size(household_df, EXPECTED_HOUSEHOLD_N, "Household")
    vendor_ok = verify_sample_size(vendor_df, EXPECTED_VENDOR_N, "Vendor")

    if not (household_ok and vendor_ok):
        logger.log("⚠️  WARNING: Sample size mismatch detected", "WARNING")

    logger.log("")
    logger.log("✅ STEP 2 COMPLETE: Sample size verification done")
    logger.log("")

    # ========================================================================
    # STEP 3: CRITICAL VARIABLE RENAMING (HOUSEHOLD ONLY)
    # ========================================================================
    logger.log("STEP 3: Critical variable renaming...")
    logger.log("")

    household_df_renamed = rename_household_variables(household_df)

    logger.log("")
    logger.log("✅ STEP 3 COMPLETE: Variable renaming successful")
    logger.log("")

    # ========================================================================
    # STEP 4: DATA QUALITY CHECKS
    # ========================================================================
    logger.log("STEP 4: Data quality assessment...")
    logger.log("")

    # Household data checks
    logger.log("--- Household Data Quality ---")
    household_missing = check_missing_data(household_df_renamed, "Household")
    check_data_types(household_df_renamed, "Household")
    check_duplicates(household_df_renamed, data_type="Household")

    logger.log("")

    # Vendor data checks
    logger.log("--- Vendor Data Quality ---")
    vendor_missing = check_missing_data(vendor_df, "Vendor")
    check_data_types(vendor_df, "Vendor")
    check_duplicates(vendor_df, data_type="Vendor")

    logger.log("")
    logger.log("✅ STEP 4 COMPLETE: Data quality assessment done")
    logger.log("")

    # ========================================================================
    # STEP 5: SAVE PROCESSED DATASETS
    # ========================================================================
    logger.log("STEP 5: Saving processed datasets...")
    logger.log("")

    save_processed_data(household_df_renamed, HOUSEHOLD_OUTPUT, "Household")
    save_processed_data(vendor_df, VENDOR_OUTPUT, "Vendor")

    logger.log("")
    logger.log("✅ STEP 5 COMPLETE: Processed datasets saved")
    logger.log("")

    # ========================================================================
    # PHASE 0 SUMMARY
    # ========================================================================
    logger.log("=" * 70)
    logger.log("PHASE 0 COMPLETE: DATA CONSOLIDATION SUCCESSFUL")
    logger.log("=" * 70)
    logger.log("")
    logger.log("Summary:")
    logger.log(f"  • Household records: {len(household_df_renamed)}")
    logger.log(f"  • Vendor records: {len(vendor_df)}")
    logger.log(f"  • Household variables: {len(household_df_renamed.columns)}")
    logger.log(f"  • Vendor variables: {len(vendor_df.columns)}")
    logger.log("")
    logger.log("Output Files:")
    logger.log(f"  • {HOUSEHOLD_OUTPUT}")
    logger.log(f"  • {VENDOR_OUTPUT}")
    logger.log("")
    logger.log("Next Steps:")
    logger.log("  1. Review Phase 0 log file")
    logger.log("  2. Verify processed datasets")
    logger.log("  3. Proceed to Phase 1: Data Cleaning & Variable Specification")
    logger.log("")

    # Save log
    logger.save()

    return household_df_renamed, vendor_df

# ============================================================================
# EXECUTE PHASE 0
# ============================================================================

if __name__ == "__main__":
    try:
        household_data, vendor_data = main()
        print("\n✅ Phase 0 execution complete!")
        print(f"\n📊 Quick check:")
        print(f"   Household shape: {household_data.shape}")
        print(f"   Vendor shape: {vendor_data.shape}")

    except Exception as e:
        logger.log(f"❌ FATAL ERROR: {str(e)}", "ERROR")
        logger.save()
        raise
