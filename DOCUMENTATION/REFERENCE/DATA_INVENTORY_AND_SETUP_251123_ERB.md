---
title: "WFL-Analysis: Data Inventory & Setup Documentation"
date: 2025-11-23
version: 1.0
status: "complete"
---

# Data Inventory & Analysis Setup

## ✅ Status: COMPLETE & READY FOR USE

Your WFL-Analysis directory is now **fully set up** with:
- ✅ Complete folder structure created (00_inputs, 01_scripts, 02_outputs, 03_logs)
- ✅ All datasets copied and organized
- ✅ Survey instruments and codebooks in place
- ✅ All workflow documentation files present
- ✅ Ready for immediate analysis work

**Setup Date**: 2025-11-23
**Total Size**: ~1.6 MB of data + ~130 KB of documentation
**Location**: `/Users/emersonrburke/Desktop/working/working_thesis_211125/WFL-Analysis/`

---

## 📁 Complete Directory Structure

```
WFL-Analysis/
├── 📄 Workflow Documentation (6 files, ~130 KB)
│   ├── Data_Analysis_Workflow_Complete.md
│   ├── OPERATIONALIZATION_MASTER_AI_OPTIMIZED_251123_ERB.md
│   ├── OPERATIONALIZATION_QUICK_REFERENCE_251123_ERB.md
│   ├── operationalization_master.yaml
│   ├── README_ANALYSIS_WORKFLOW_251123_ERB.md
│   ├── WORKFLOW_SETUP_SUMMARY_251123_ERB.md
│   └── DATA_INVENTORY_AND_SETUP_251123_ERB.md (this file)
│
├── 00_inputs/  ⭐ INPUT DATA & DOCUMENTATION
│   ├── data/
│   │   └── DataLongBien2024/  (All datasets)
│   │       ├── household_survey_LONG_BIEN_2024_ALL_merged.csv
│   │       ├── vendor_survey_LONG_BIEN_2024_ALL_merged.csv
│   │       ├── Household_survey_*.xlsx  (with & without food waste)
│   │       ├── Vendor_survey_*.xlsx      (with & without food waste)
│   │       ├── households_LongBien_2024_*.kml  (geospatial)
│   │       └── vendors_LongBien_2024_*.kml     (geospatial)
│   │
│   └── survey_instruments/  (Survey tools & documentation)
│       └── surveys/
│           ├── household-survey/
│           ├── vendor-survey/
│           ├── household-survey-codebook.md
│           └── vendor-survey-codebook.md
│
├── 01_scripts/  📝 YOUR ANALYSIS SCRIPTS GO HERE
│   ├── 01_load_and_consolidate.R (or .py)
│   ├── 02_cleaning_and_spec.R
│   ├── 03_tier1_tier2_analyses.R
│   ├── 04_tier3_tier4_analyses.R
│   └── README_scripts.md
│
├── 02_outputs/  📊 RESULTS & ANALYSIS OUTPUTS
│   ├── tables/
│   │   ├── Table_01_Descriptive_Statistics.csv
│   │   ├── Table_02_Bivariate_Tests.csv
│   │   ├── Table_03_Correlation_Matrix.csv
│   │   └── Table_04_Regression_Model.txt
│   ├── figures/
│   │   ├── Figure_01_Correlation_Heatmap.png
│   │   └── [other visualizations]
│   └── datasets/
│       ├── household_df_consolidated.csv
│       ├── vendor_df_consolidated.csv
│       └── [cleaned, analysis-ready datasets]
│
└── 03_logs/  📋 DOCUMENTATION & DECISION LOGS
    ├── methodology_summary.md
    ├── variable_mapping.md
    ├── cleaning_decisions.md
    ├── data_decisions.md
    ├── analysis_notes.md
    ├── progress_log.md
    └── output_mapping.md
```

---

## 📊 Data Files Inventory

### **Location**: `00_inputs/data/DataLongBien2024/`

#### **Household Survey Data**

| File | Size | Type | Purpose | Status |
|------|------|------|---------|--------|
| `household_survey_LONG_BIEN_2024_ALL_merged.csv` | 290 KB | CSV | Merged household data (both versions combined) | ✅ Ready |
| `Household_survey_LONG_BIEN_2024_ALL_withFoodWaste.xlsx` | 63 KB | Excel | Household survey WITH food waste module (n=102) | ✅ Ready |
| `Household_survey_LONG_BIEN_2024_ALL_withoutFoodWaste.xlsx` | 129 KB | Excel | Household survey WITHOUT food waste module (n=139) | ✅ Ready |

#### **Vendor Survey Data**

| File | Size | Type | Purpose | Status |
|------|------|------|---------|--------|
| `vendor_survey_LONG_BIEN_2024_ALL_merged.csv` | 228 KB | CSV | Merged vendor data (both versions combined) | ✅ Ready |
| `Vendor_survey_LONG_BIEN_2024_ALL_withFoodWaste.xlsx` | 40 KB | Excel | Vendor survey WITH food waste module | ✅ Ready |
| `Vendor_survey_LONG_BIEN_2024_ALL_withoutFoodWaste.xlsx` | 101 KB | Excel | Vendor survey WITHOUT food waste module | ✅ Ready |

#### **Geospatial Data (KML)**

| File | Size | Type | Purpose | Status |
|------|------|------|---------|--------|
| `households_LongBien_2024_ALL_withFoodWaste.kml` | 22 KB | KML | Household locations (with food waste module) | ✅ Ready |
| `households_LongBien_2024_ALL_withoutFoodWaste.kml` | 36 KB | KML | Household locations (without food waste module) | ✅ Ready |
| `vendors_LongBien_2024_ALL_withFoodWaste.kml` | 20 KB | KML | Vendor locations (with food waste module) | ✅ Ready |
| `vendors_LongBien_2024_ALL_withoutFoodWaste.kml` | 58 KB | KML | Vendor locations (without food waste module) | ✅ Ready |

**Total Data Size**: ~1.6 MB

---

## 📚 Survey Instruments & Documentation

### **Location**: `00_inputs/survey_instruments/surveys/`

#### **Household Survey**

| Item | Type | Purpose |
|------|------|---------|
| `household-survey/` | Directory | Complete household survey instrument (ODK format) |
| `household-survey-codebook.md` | Markdown | Variable definitions, codes, item text |

**Use**: Reference when understanding variable meanings and response formats

#### **Vendor Survey**

| Item | Type | Purpose |
|------|------|---------|
| `vendor-survey/` | Directory | Complete vendor survey instrument (ODK format) |
| `vendor-survey-codebook.md` | Markdown | Variable definitions, codes, item text |

**Use**: Reference when understanding vendor-level variables

#### **Codebooks**

Both codebooks are available in Markdown format for easy searching:
- `household-survey-codebook.md` (122 KB)
- `vendor-survey-codebook.md` (45 KB)

---

## 🚀 Getting Started: What to Do Now

### **Step 1: Explore Your Data** (30 minutes)

Open the CSV files to understand the structure:

```bash
# In R
household <- read.csv("00_inputs/data/DataLongBien2024/household_survey_LONG_BIEN_2024_ALL_merged.csv")
vendor <- read.csv("00_inputs/data/DataLongBien2024/vendor_survey_LONG_BIEN_2024_ALL_merged.csv")

head(household)
dim(household)
summary(household)
```

### **Step 2: Load Operationalization Reference** (5 minutes)

```r
# In R
library(yaml)
ops <- yaml::read_yaml("operationalization_master.yaml")

# List all T2 stratification variables
cat("T2 Stratification Variables:\n")
for (strata in ops$analysis_structure$tier_2_group_comparisons$stratification_variables) {
  cat(strata$op_id, "-", strata$name, "\n")
}
```

### **Step 3: Begin Phase 0** (1-2 hours)

Follow `Data_Analysis_Workflow_Complete.md` Phase 0:
1. Data consolidation (stack household files)
2. Variable renaming (critical: `foodgroups_*` distinction)
3. Load geospatial data
4. Create key identifiers

### **Step 4: Verify Variables Exist** (1 hour)

Use the **Data Verification Checklist** from Master operationalization MD:
- Confirm consumption items exist: `foodgroups_001_*`
- Confirm shopping motives exist: `reason_001` through `reason_005`
- Confirm perception items: `vendor_clean`, `vendor_safe`, `vendor_reputation`
- Confirm accessibility variables: `transportation_001` through `transportation_007`
- Document any missing variables

---

## 📋 Data Variables Quick Reference

### **Key Variables for Your Analysis**

#### **Outcome Variable**
- **OP029 (DDS)**: `foodgroups_001_*` (count of food groups consumed)
  - Location: Household survey
  - Items: 11-12 binary indicators
  - Range: 0-12 (count)

#### **T2 Stratification Variables**
- **OP011 (Accessibility)**: Derived from `time_to_[outlet_type]`
  - Household survey, transportation_* columns
  - Binary: ≤5 min (close) / >5 min (far)

- **OP016 (Affordability)**: Derived from `foodexpenditure` + `income`
  - Household survey
  - Continuous: % of income spent on food
  - Tertile split: Low / Medium / High

- **OP025 (Safety Index)**: Aggregate of `vendor_clean`, `vendor_safe`, `vendor_reputation`
  - Household survey, Likert perception items
  - Continuous: Mean of 3 items
  - Binary split: Low / High (median)

#### **External Domain Variables**
- **OP001-OP002**: Food group availability + outlet type (Vendor survey)
- **OP003**: Price motive (`reason_003`)
- **OP004-OP006**: Cleanliness, safety, reputation perception
- **OP007**: Vendor infrastructure (Vendor survey)

---

## 🔧 Data Setup Checklist

Before you start analysis, verify:

- [ ] **Can read household data**
  ```r
  household <- read.csv("00_inputs/data/DataLongBien2024/household_survey_LONG_BIEN_2024_ALL_merged.csv")
  ```

- [ ] **Can read vendor data**
  ```r
  vendor <- read.csv("00_inputs/data/DataLongBien2024/vendor_survey_LONG_BIEN_2024_ALL_merged.csv")
  ```

- [ ] **Can load operationalization YAML**
  ```r
  ops <- yaml::read_yaml("operationalization_master.yaml")
  ```

- [ ] **Data dimensions match expectations**
  - Household: n=241 (102 + 139)
  - Vendor: n=284
  - Document actual n values

- [ ] **Key variables exist** (use codebooks to verify)
  - `foodgroups_001_*` items
  - `reason_*` variables
  - `vendor_*` perception items
  - Accessibility variables
  - Affordability variables

- [ ] **Can load KML geospatial data** (if using R)
  ```r
  library(sf)
  households <- st_read("00_inputs/data/DataLongBien2024/households_LongBien_2024_ALL_withoutFoodWaste.kml")
  vendors <- st_read("00_inputs/data/DataLongBien2024/vendors_LongBien_2024_ALL_withoutFoodWaste.kml")
  ```

---

## 📖 Using the Codebooks

### **Household Survey Codebook**
**File**: `00_inputs/survey_instruments/surveys/household-survey-codebook.md`

Use to:
- Find exact variable names in data
- Understand response formats (Likert, binary, categorical)
- See original ODK item text
- Check skip patterns and dependencies

**Example**: Search codebook for "foodgroups" to find all food group variables and their coding

### **Vendor Survey Codebook**
**File**: `00_inputs/survey_instruments/surveys/vendor-survey-codebook.md`

Use to:
- Find vendor-specific variables
- Understand outlet type classifications
- See vendor infrastructure items
- Check vendor-reported data fields

---

## 📝 Important Data Notes

### **Household Survey Structure**

Two versions combined in merged CSV:
- **WITH Food Waste Module** (n=102)
  - Extra variables for food waste tracking
  - Use for affordability analysis if needed
  - Identified by presence of additional columns

- **WITHOUT Food Waste Module** (n=139)
  - Standard survey items only
  - Use for complete sample analyses
  - May have different field names for affordability

**Critical**: Check `has_foodwaste_module` variable or equivalent to identify which households have which module

### **Geospatial Data**

KML files contain point locations for:
- Household GPS coordinates
- Vendor GPS coordinates

**For use in**:
- Distance calculations (to nearest market, etc.)
- Neighborhood-level aggregations
- Spatial analysis

**Tool to use**:
- R: `sf` package with `st_read()`
- Python: `geopandas` with `read_file()`
- Desktop: QGIS (for exploration)

---

## 🔑 Critical Data Handling Notes

### **Variable Naming**

⚠️ **CRITICAL**: There are TWO "foodgroups" variables with different meanings:
1. **`foodgroups_001_*`** (with number prefix)
   - Items from consumption recall
   - Binary: what household consumed
   - Use for: OP029 (DDS outcome)
   - Rename to: `hh_consumption_*`

2. **`foodgroups`** (string, no number)
   - Text listing what household sells (if vendor)
   - Categorical/Text
   - Use for: OP041 (household sales diversity, if applicable)
   - Rename to: `hh_sales_string`

**In Phase 0**, rename these explicitly to avoid conflict:
```r
# Rename on load
data <- data %>%
  rename_with(~gsub("foodgroups_001_", "hh_consumption_", .x),
              starts_with("foodgroups_001_")) %>%
  rename(hh_sales_string = foodgroups)
```

### **Handling Missing Data**

Before analysis, document:
- [ ] % missing per variable
- [ ] Any variables with >30% missing
- [ ] Decision: listwise deletion, imputation, or exclusion

**Standard approach**:
- For HDDS (OP029): Listwise deletion (all items must be present)
- For perception items: Exclude individuals with missing values
- For income/affordability: Document separately for subset analyses

### **Sample Size Notes**

- **Total households**: 241 (102 with food waste, 139 without)
- **Total vendors**: 284
- **Analysis samples**:
  - Full household analysis: n=214+ (verify actual count)
  - Affordability subset: ~92 (with income data)
  - Food expenditure subset: ~64 (with complete data)

---

## 📊 Data Quality & Verification

### **Before Phase 1, Run These Checks**

```r
# Household data
household <- read.csv("00_inputs/data/DataLongBien2024/household_survey_LONG_BIEN_2024_ALL_merged.csv")

# Check dimensions
dim(household)  # Should be ~241 rows

# Check key variables exist
colnames(household)[grepl("foodgroups_001", colnames(household))]
colnames(household)[grepl("reason_", colnames(household))]
colnames(household)[grepl("time_", colnames(household))]

# Check data types
str(household[, 1:20])

# Check for impossible values
summary(household)

# Document findings
cat("Data verification complete. See 03_logs/data_decisions.md for details.\n")
```

### **Document Findings**

In `03_logs/data_decisions.md`, record:
- Sample sizes (n_household, n_vendor)
- Missing data patterns
- Data type checks
- Any data quality issues found
- Decisions made for handling issues

---

## 🚀 Ready to Begin Phase 0

Your data is now in place. Follow these steps:

1. **Read**: `Data_Analysis_Workflow_Complete.md` (Phase 0 section)
2. **Verify**: Data files exist and can be read
3. **Begin**: Phase 0 (Setup & Data Consolidation)
4. **Document**: All decisions in `03_logs/`

---

## 📞 Troubleshooting

### **"I can't find a specific variable"**
1. Search household codebook: `00_inputs/survey_instruments/surveys/household-survey-codebook.md`
2. Check for alternate names or skip patterns
3. Verify variable exists in your actual data
4. If missing, document and decide: exclude from analysis or find proxy

### **"The data structure doesn't match what I expected"**
1. Check if you loaded the correct file (merged CSV vs. XLSX)
2. Verify both versions (with/without food waste) are properly combined
3. Check variable naming after import (may need cleaning)
4. Reference codebooks to understand original ODK structure

### **"How do I handle the two 'foodgroups' variables?"**
→ Rename on load (see above): `foodgroups_001_*` → `hh_consumption_*` and `foodgroups` → `hh_sales_string`

### **"What if a variable is in the codebook but not in my data?"**
→ Check if it's conditionally included (ODK skip pattern)
→ Verify spelling and naming
→ Document as missing and decide: find proxy or exclude

---

## 📚 File Organization Summary

### **In 00_inputs/data/:**
- All raw CSV and XLSX files
- All KML geospatial files
- Organized by data type (household, vendor, geospatial)

### **In 00_inputs/survey_instruments/:**
- Survey instrument files (ODK format)
- Codebooks (Markdown) with variable documentation
- Use for reference while analyzing

### **In 01_scripts/:**
- Your analysis code goes here
- Use operationalization YAML for variable specifications
- Reference workflow document for code structure

### **In 02_outputs/:**
- tables/: Results from statistical tests (Table 1-4)
- figures/: Visualizations (Figure 1+)
- datasets/: Cleaned, consolidated datasets ready for analysis

### **In 03_logs/:**
- Document all decisions, issues, and findings
- Required files: variable_mapping.md, cleaning_decisions.md, progress_log.md

---

## ✅ Setup Complete Verification

Confirm all items:

- [ ] Data files are in `00_inputs/data/DataLongBien2024/`
- [ ] Survey instruments are in `00_inputs/survey_instruments/surveys/`
- [ ] Folder structure exists: 00_inputs, 01_scripts, 02_outputs, 03_logs
- [ ] All workflow markdown documents are in root WFL-Analysis/
- [ ] YAML operationalization file is in root WFL-Analysis/
- [ ] Can read: household CSV, vendor CSV, codebooks
- [ ] Understand: Two "foodgroups" variables, how to rename them
- [ ] Know: Sample sizes and T2 stratification approach

---

## 🎯 Next Action

**Open**: `Data_Analysis_Workflow_Complete.md`
**Read**: Phase 0 (Setup & Data Consolidation)
**Execute**: Follow Phase 0 step-by-step

Your analysis environment is now **fully set up and ready to use**.

---

**Setup Date**: 2025-11-23
**Status**: ✅ Complete
**Data Size**: ~1.6 MB
**Documentation**: ~130 KB
**Location**: `/WFL-Analysis/`

Ready to analyze! 🚀
