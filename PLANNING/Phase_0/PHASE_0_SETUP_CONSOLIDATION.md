---
title: "Phase 0: Setup & Data Consolidation"
date: 2025-11-23
phase: 0
status: "Ready to Execute"
---

# Phase 0: Setup & Data Consolidation

**Objective**: Consolidate raw datasets, verify data integrity, and prepare analysis environment
**Duration**: 2-3 hours
**Output**: Clean, merged household and vendor datasets ready for Phase 1

---

## Phase 0 Overview

### What You'll Do
1. Load household survey data (with/without food waste module)
2. Load vendor survey data
3. Handle variable naming conflicts
4. Stack/merge datasets appropriately
5. Verify sample sizes and missing data patterns
6. Save Phase 0 checkpoint datasets

### Why It Matters
- Ensures all data is loaded correctly before analysis
- Identifies and resolves data quality issues early
- Creates clean working datasets for downstream analysis
- Allows you to verify operationalizations against actual data

---

## Critical Data Information

### Household Survey Files

**Two separate datasets to consolidate:**
- `household_survey_LONG_BIEN_2024_ALL_withFoodWaste.xlsx` (n=102 households)
- `household_survey_LONG_BIEN_2024_ALL_withoutFoodWaste.xlsx` (n=139 households)
- **Merged result**: `household_survey_LONG_BIEN_2024_ALL_merged.csv` (n=241 total)

**Or load the merged CSV directly:**
- `household_survey_LONG_BIEN_2024_ALL_merged.csv` (all 241 households)

### Vendor Survey Files

**Single complete dataset:**
- `vendor_survey_LONG_BIEN_2024_ALL_merged.csv` (n=284 vendors)
- Also available in XLSX format for reference

### Location
All files in: `00_inputs/data/`

---

## ⚠️ CRITICAL: Variable Naming Conflict

**Problem**: Two different "foodgroups" variables with different meanings:

| Variable | Meaning | Usage |
|----------|---------|-------|
| `foodgroups_001_*` | Consumption items (food groups eaten by household) | For HDDS calculation (OP029) |
| `foodgroups` | String listing what household sells | For sales/vendor analysis |

**Impact**: If not renamed, these will conflict in analysis

**Solution**: Rename explicitly in Phase 0

```r
# Load household data
household_df <- read_csv("00_inputs/data/household_survey_LONG_BIEN_2024_ALL_merged.csv")

# CRITICAL RENAMING to avoid conflict:
household_df <- household_df %>%
  rename_with(~gsub("foodgroups_001_", "hh_consumption_", .x),
              starts_with("foodgroups_001_")) %>%
  rename(hh_sales_string = foodgroups)

# After renaming:
# - hh_consumption_cereals, hh_consumption_legumes, etc. (for HDDS)
# - hh_sales_string (for sales analysis)
```

---

## Phase 0 Execution Checklist

### Step 1: Load Data Files
- [ ] Load household survey (merged CSV or combine with/without food waste)
- [ ] Load vendor survey
- [ ] Verify all files loaded successfully (check row counts)
- [ ] List all columns to verify structure

**Expected Sample Sizes:**
- Households: 241 total
- Vendors: 284

### Step 2: Handle Variable Naming Conflict
- [ ] Rename `foodgroups_001_*` → `hh_consumption_*`
- [ ] Rename `foodgroups` → `hh_sales_string`
- [ ] Verify renamed columns exist
- [ ] Check no duplicate column names

### Step 3: Check Data Structure
- [ ] Household data: Expected columns present
- [ ] Vendor data: Expected columns present
- [ ] Data types correct (numeric vs character)
- [ ] Date columns properly parsed (if any)

### Step 4: Verify Survey Codebook Variables

**Household Survey - Key Variable Groups:**
- [ ] `foodgroups_001_*` (11 items) - Consumption diversity
- [ ] `reason_001_*` (5 items) - Shopping motives
- [ ] `clean`, `safe`, `reputation` (3 items) - Perception/quality
- [ ] `time_*` or `transportation_*` - Travel time to outlets
- [ ] `[outlet_type]_freq` - Visit frequency to different outlets
- [ ] `foodexpenditure` - Food spending amount
- [ ] `foodexp_timeunit` - Time unit for spending
- [ ] `cookingsource` - Where they cook
- [ ] `watersource` - Water access
- [ ] `waterdistance` - Distance to water

**Vendor Survey - Key Variable Groups:**
- [ ] `foodgroups_001_*` (11 items) - Availability of food groups
- [ ] `vendor_type` - Outlet classification
- [ ] `clean`, `safe`, `reputation` - Vendor characteristics
- [ ] `infrastructure` - Vendor-reported facilities

### Step 5: Check for Missing Data
- [ ] Calculate missingness for each variable
- [ ] Identify variables with >30% missing (flag for limitations)
- [ ] Document patterns (random vs systematic)
- [ ] Decide on handling strategy (exclude vs impute)

### Step 6: Verify Sample Sizes
- [ ] Household survey: n=241 confirmed
- [ ] Vendor survey: n=284 confirmed
- [ ] Check for duplicate IDs (if applicable)
- [ ] Confirm no data loss during load/rename process

### Step 7: Create Phase 0 Checkpoint

**Save processed datasets:**

```r
# Save household dataset
write_csv(household_df, "01_scripts/Phase_0_household_processed.csv")

# Save vendor dataset
write_csv(vendor_df, "01_scripts/Phase_0_vendor_processed.csv")

# Save summary statistics
summary_stats <- list(
  household_n = nrow(household_df),
  household_vars = ncol(household_df),
  vendor_n = nrow(vendor_df),
  vendor_vars = ncol(vendor_df),
  timestamp = Sys.time()
)
saveRDS(summary_stats, "01_scripts/Phase_0_summary.RDS")
```

### Step 8: Document Phase 0 Completion

Create a log file documenting:
- [ ] Data files loaded
- [ ] Variable renaming performed
- [ ] Sample sizes confirmed
- [ ] Missing data patterns documented
- [ ] Any issues encountered and how resolved
- [ ] Timestamp of completion

---

## R Code Template for Phase 0

```r
# ===== PHASE 0: SETUP & DATA CONSOLIDATION =====
# Date: [TODAY'S DATE]
# Author: [YOUR NAME]
# Purpose: Load, verify, and consolidate survey data

library(dplyr)
library(readr)
library(tidyr)

# Set working directory to WFL-Analysis
setwd("/Users/emersonrburke/Desktop/working/working_thesis_211125/WFL-Analysis")

# ===== LOAD HOUSEHOLD SURVEY DATA =====
cat("Loading household survey data...\n")

# Option 1: Load merged CSV directly
household_df <- read_csv("00_inputs/data/household_survey_LONG_BIEN_2024_ALL_merged.csv")

# Or Option 2: Load and combine separate files
# hh_with_fw <- read_excel("00_inputs/data/Household_survey_LONG_BIEN_2024_ALL_withFoodWaste.xlsx") %>%
#   mutate(food_waste_module = TRUE)
# hh_without_fw <- read_excel("00_inputs/data/Household_survey_LONG_BIEN_2024_ALL_withoutFoodWaste.xlsx") %>%
#   mutate(food_waste_module = FALSE)
# household_df <- bind_rows(hh_with_fw, hh_without_fw)

# ===== LOAD VENDOR SURVEY DATA =====
cat("Loading vendor survey data...\n")
vendor_df <- read_csv("00_inputs/data/vendor_survey_LONG_BIEN_2024_ALL_merged.csv")

# ===== CRITICAL: HANDLE VARIABLE NAMING CONFLICT =====
cat("Renaming conflicting variables...\n")

household_df <- household_df %>%
  # Rename consumption items: foodgroups_001_* -> hh_consumption_*
  rename_with(~gsub("foodgroups_001_", "hh_consumption_", .x),
              starts_with("foodgroups_001_")) %>%
  # Rename sales items: foodgroups -> hh_sales_string
  rename(hh_sales_string = foodgroups)

# ===== VERIFY DATA STRUCTURE =====
cat("Verifying data structure...\n")

# Check dimensions
cat(sprintf("Household data: %d rows, %d columns\n", nrow(household_df), ncol(household_df)))
cat(sprintf("Vendor data: %d rows, %d columns\n", nrow(vendor_df), ncol(vendor_df)))

# Check column names
cat("\nHousehold columns (first 20):\n")
print(names(household_df)[1:20])

cat("\nVendor columns (first 20):\n")
print(names(vendor_df)[1:20])

# ===== CHECK FOR MISSING DATA =====
cat("\nCalculating missingness...\n")

missing_household <- household_df %>%
  summarise(across(everything(), list(missing = ~sum(is.na(.)))))

missing_vendor <- vendor_df %>%
  summarise(across(everything(), list(missing = ~sum(is.na(.)))))

# Variables with >30% missing
high_missing_hh <- names(household_df)[colMeans(is.na(household_df)) > 0.3]
high_missing_vendor <- names(vendor_df)[colMeans(is.na(vendor_df)) > 0.3]

cat("\nHousehold variables with >30% missing:\n")
print(high_missing_hh)
cat("\nVendor variables with >30% missing:\n")
print(high_missing_vendor)

# ===== SAVE PHASE 0 CHECKPOINT =====
cat("\nSaving Phase 0 checkpoint datasets...\n")

write_csv(household_df, "01_scripts/Phase_0_household_processed.csv")
write_csv(vendor_df, "01_scripts/Phase_0_vendor_processed.csv")

# Save summary
phase_0_summary <- list(
  date = Sys.Date(),
  household_n = nrow(household_df),
  household_vars = ncol(household_df),
  vendor_n = nrow(vendor_df),
  vendor_vars = ncol(vendor_df),
  high_missing_household = high_missing_hh,
  high_missing_vendor = high_missing_vendor
)
saveRDS(phase_0_summary, "01_scripts/Phase_0_summary.RDS")

cat("\n✅ PHASE 0 COMPLETE\n")
cat("Saved files:\n")
cat("  - 01_scripts/Phase_0_household_processed.csv\n")
cat("  - 01_scripts/Phase_0_vendor_processed.csv\n")
cat("  - 01_scripts/Phase_0_summary.RDS\n")
```

---

## Python Template for Phase 0

```python
# ===== PHASE 0: SETUP & DATA CONSOLIDATION =====
# Date: [TODAY'S DATE]
# Author: [YOUR NAME]

import pandas as pd
import numpy as np
import yaml
import os

os.chdir("/Users/emersonrburke/Desktop/working/working_thesis_211125/WFL-Analysis")

# Load operationalization reference
with open("DOCUMENTATION/REFERENCE/operationalization_master.yaml", "r") as f:
    ops = yaml.safe_load(f)

# ===== LOAD HOUSEHOLD SURVEY DATA =====
print("Loading household survey data...")
household_df = pd.read_csv("00_inputs/data/household_survey_LONG_BIEN_2024_ALL_merged.csv")

# ===== LOAD VENDOR SURVEY DATA =====
print("Loading vendor survey data...")
vendor_df = pd.read_csv("00_inputs/data/vendor_survey_LONG_BIEN_2024_ALL_merged.csv")

# ===== CRITICAL: HANDLE VARIABLE NAMING CONFLICT =====
print("Renaming conflicting variables...")

# Rename consumption items
consumption_cols = [col for col in household_df.columns if col.startswith("foodgroups_001_")]
rename_dict = {col: col.replace("foodgroups_001_", "hh_consumption_") for col in consumption_cols}
rename_dict["foodgroups"] = "hh_sales_string"
household_df = household_df.rename(columns=rename_dict)

# ===== VERIFY DATA STRUCTURE =====
print(f"Household data: {household_df.shape[0]} rows, {household_df.shape[1]} columns")
print(f"Vendor data: {vendor_df.shape[0]} rows, {vendor_df.shape[1]} columns")

# ===== CHECK FOR MISSING DATA =====
print("\nCalculating missingness...")
missing_pct_hh = (household_df.isnull().sum() / len(household_df) * 100).sort_values(ascending=False)
missing_pct_vendor = (vendor_df.isnull().sum() / len(vendor_df) * 100).sort_values(ascending=False)

high_missing_hh = missing_pct_hh[missing_pct_hh > 30].index.tolist()
high_missing_vendor = missing_pct_vendor[missing_pct_vendor > 30].index.tolist()

print(f"\nHousehold variables with >30% missing: {high_missing_hh}")
print(f"Vendor variables with >30% missing: {high_missing_vendor}")

# ===== SAVE PHASE 0 CHECKPOINT =====
print("\nSaving Phase 0 checkpoint datasets...")
household_df.to_csv("01_scripts/Phase_0_household_processed.csv", index=False)
vendor_df.to_csv("01_scripts/Phase_0_vendor_processed.csv", index=False)

print("✅ PHASE 0 COMPLETE")
```

---

## Data Verification Checklist

### Household Data Variables

**Dietary Diversity (OP029 - Primary Outcome)**
- [ ] `hh_consumption_cereals` (after renaming)
- [ ] `hh_consumption_legumes`
- [ ] `hh_consumption_meat`
- [ ] All 11 food group items present
- [ ] No column named `foodgroups_001_*` remaining

**Accessibility (OP009-OP011)**
- [ ] `time_to_main_source` or similar (travel time)
- [ ] Time measured in minutes
- [ ] Binary classification: ≤5 min vs >5 min

**Affordability (OP012-OP016)**
- [ ] `foodexpenditure` (food spending amount)
- [ ] `foodexp_timeunit` (daily/weekly/monthly)
- [ ] Proxy income measures (land/assets)
- [ ] Sufficient data for budget share calculation

**Perceptions/Quality (OP004-OP007, OP021-OP025)**
- [ ] `clean` (vendor cleanliness perception)
- [ ] `safe` (food safety perception)
- [ ] `reputation` (vendor reputation)
- [ ] Shopping motives (reason_001, reason_002, etc.)

**Other Factors (OP017-OP020, OP026-OP028)**
- [ ] `cookingsource` (cooking facilities)
- [ ] `watersource` and `waterdistance` (water access)
- [ ] Visit frequency to different outlets
- [ ] Trust-based shopping indicators

### Vendor Data Variables

**Food Availability (OP001-OP002)**
- [ ] `foodgroups_001_*` (11 food groups - for vendors, NOT renamed)
- [ ] All food group items present

**Vendor Characteristics (OP004-OP007)**
- [ ] `clean` (vendor cleanliness)
- [ ] `safe` (food safety)
- [ ] `reputation` (vendor reputation)
- [ ] `infrastructure` (facilities/infrastructure)

**Vendor Classification**
- [ ] `vendor_type` (outlet classification)
- [ ] Types: market, supermarket, street vendor, etc.

---

## Common Issues & Solutions

### Issue 1: foodgroups variables not renamed
**Symptom**: Still have both `foodgroups_001_*` and `foodgroups` columns
**Solution**: Run renaming code before any analysis

### Issue 2: Missing data too high
**Symptom**: Variables with >50% missing values
**Solution**: Document as limitation, decide exclude vs impute case-by-case

### Issue 3: Data types incorrect
**Symptom**: Numeric columns loaded as character (due to special values)
**Solution**: Check for "NA", "-99", or other codes; recode appropriately

### Issue 4: Sample size mismatch
**Symptom**: Different n than expected (241 households, 284 vendors)
**Solution**: Check for duplicate IDs or filtering during import

---

## Phase 0 Output Files

After Phase 0 completes, you should have:

```
01_scripts/
├── Phase_0_household_processed.csv    (241 rows, all columns renamed)
├── Phase_0_vendor_processed.csv       (284 rows, ready for analysis)
└── Phase_0_summary.RDS               (summary statistics)

03_logs/
└── Phase_0_Completion_Log_[DATE].md  (your documentation)
```

---

## Phase 0 Completion Criteria

✅ **Data Loaded Successfully**
- Household data loaded: 241 rows
- Vendor data loaded: 284 rows
- No errors during load

✅ **Variables Renamed Correctly**
- No `foodgroups_001_*` columns remain (renamed to `hh_consumption_*`)
- `foodgroups` renamed to `hh_sales_string`
- Vendor `foodgroups_001_*` unchanged (no conflict there)

✅ **Data Quality Verified**
- Missing data patterns documented
- High-missing variables (>30%) identified
- Sample sizes confirmed

✅ **Checkpoint Datasets Created**
- `Phase_0_household_processed.csv` saved
- `Phase_0_vendor_processed.csv` saved
- Summary statistics saved

✅ **Documentation Complete**
- Phase 0 log created in `03_logs/`
- Variables verified against operationalization guide
- Any issues documented

---

## Next Phase

When Phase 0 is complete and verified, proceed to:
**Phase 1: Data Cleaning & Variable Specification**

See: `PLANNING/Phase_1/PHASE_1_DATA_CLEANING.md`

---

## Resources

- **Data Files**: `00_inputs/data/`
- **Codebooks**: `00_inputs/survey_instruments/`
- **Operationalization Reference**: `DOCUMENTATION/REFERENCE/operationalization_master.yaml`
- **Complete Workflow**: `DOCUMENTATION/GUIDES/Data_Analysis_Workflow_Complete.md`

---

**Phase 0 Status**: Ready to Execute
**Last Updated**: 2025-11-23
