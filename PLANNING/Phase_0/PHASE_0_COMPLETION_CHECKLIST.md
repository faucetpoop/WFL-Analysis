---
title: "Phase 0 Completion Checklist"
date: 2025-11-23
phase: 0
---

# Phase 0: Completion Checklist

Use this checklist to verify Phase 0 is complete before moving to Phase 1.

---

## Data Loading & Verification

### Household Survey
- [ ] File loaded: `household_survey_LONG_BIEN_2024_ALL_merged.csv`
- [ ] Sample size confirmed: 241 rows
- [ ] All expected columns present
- [ ] Data types appropriate (numeric vs character)
- [ ] No obvious data corruption

### Vendor Survey
- [ ] File loaded: `vendor_survey_LONG_BIEN_2024_ALL_merged.csv`
- [ ] Sample size confirmed: 284 rows
- [ ] All expected columns present
- [ ] Data types appropriate
- [ ] No obvious data corruption

---

## Critical: Variable Renaming

### Household Data Renaming
- [ ] **BEFORE**: Verify `foodgroups_001_*` columns exist in original data
- [ ] **BEFORE**: Verify `foodgroups` column exists in original data
- [ ] **RENAME**: `foodgroups_001_*` → `hh_consumption_*` (all 11 items)
- [ ] **RENAME**: `foodgroups` → `hh_sales_string`
- [ ] **AFTER**: No columns named `foodgroups_001_*` remain
- [ ] **AFTER**: Column `hh_sales_string` exists
- [ ] **AFTER**: Columns `hh_consumption_cereals`, `hh_consumption_legumes`, etc. exist

### Vendor Data
- [ ] Vendor data `foodgroups_001_*` columns **NOT renamed** (no conflict)
- [ ] These remain as-is for availability analysis

---

## Missing Data Assessment

### Household Data
- [ ] Missing data percentage calculated for all variables
- [ ] Variables with >10% missing documented
- [ ] Variables with >30% missing flagged for limitation discussion
- [ ] Missing data pattern identified (random vs systematic)
- [ ] Decision made: exclude variable vs impute vs handle in analysis

### Vendor Data
- [ ] Missing data percentage calculated for all variables
- [ ] Variables with >10% missing documented
- [ ] Variables with >30% missing flagged for limitation discussion

### High Missing Documentation
- [ ] Excel or CSV created listing all high-missing variables
- [ ] Percentage missing documented for each
- [ ] Impact on analysis discussed in log file

---

## Data Quality Checks

### Household Data Structure
- [ ] 241 rows (no data loss from original)
- [ ] Correct number of columns (original + renaming, no duplicates)
- [ ] No duplicate household IDs (if ID column exists)
- [ ] Date columns properly parsed (if any)
- [ ] Numeric columns contain numeric values (no text mixed in)

### Vendor Data Structure
- [ ] 284 rows (no data loss from original)
- [ ] Correct number of columns
- [ ] No duplicate vendor IDs (if ID column exists)
- [ ] Data types consistent

### Range Checks
- [ ] Time variables (e.g., `time_to_main_source`) are in reasonable range
- [ ] Expenditure variables are positive numbers
- [ ] Frequency counts are non-negative integers
- [ ] Perception/scale variables are in expected range (e.g., 1-5)

---

## Operationalization Verification

### Check Variables Against Operationalization Guide

| OP_ID | Variable | Data File | Status |
|-------|----------|-----------|--------|
| OP001-002 | Food availability | Vendor | ☐ Verified |
| OP003 | Price/affordability motive | Household | ☐ Verified |
| OP004-007 | Vendor quality (clean, safe, reputation, infrastructure) | Vendor | ☐ Verified |
| OP009-011 | Accessibility/travel time | Household | ☐ Verified |
| OP012-016 | Affordability/expenditure | Household | ☐ Verified |
| OP017-020 | Convenience (cooking, water) | Household | ☐ Verified |
| OP021-024 | Desirability (health, trust, preferences) | Household | ☐ Verified |
| OP025-028 | Emergent dimensions (safety index, trust, stability) | Both | ☐ Verified |
| OP029-033 | Outcome variables (HDDS, diet quality) | Household | ☐ Verified |

---

## Household Food Consumption Items (for HDDS)

Verify all 11 food groups renamed correctly:

- [ ] `hh_consumption_cereals` (was `foodgroups_001_cereals`)
- [ ] `hh_consumption_legumes`
- [ ] `hh_consumption_meat`
- [ ] `hh_consumption_poultry`
- [ ] `hh_consumption_fish`
- [ ] `hh_consumption_dairy`
- [ ] `hh_consumption_eggs`
- [ ] `hh_consumption_oilseeds`
- [ ] `hh_consumption_vegetables`
- [ ] `hh_consumption_fruits`
- [ ] `hh_consumption_other`

**Total**: 11 items, all present and properly renamed

---

## Key Variables by Domain

### External Domain Variables

**Availability (OP001-002)**
- [ ] Vendor `foodgroups_001_*` present (11 items)

**Prices (OP003)**
- [ ] Affordability shopping motive variable present

**Vendor/Product Properties (OP004-007)**
- [ ] `clean` - vendor cleanliness perception
- [ ] `safe` - food safety perception
- [ ] `reputation` - vendor reputation
- [ ] `infrastructure` - facilities/infrastructure

**Marketing & Regulation (OP008)**
- [ ] ⚠️ Not measured - document as limitation

### Personal Domain Variables

**Accessibility (OP009-011)**
- [ ] Travel time variable present
- [ ] Time unit identified (minutes? hours?)
- [ ] Range reasonable (0-60 minutes typical)

**Affordability (OP012-016)**
- [ ] `foodexpenditure` - spending amount
- [ ] `foodexp_timeunit` - time period (daily/weekly/monthly)
- [ ] Income proxy variables present
- [ ] Data sufficient for budget share calculation

**Convenience (OP017-020)**
- [ ] `cookingsource` - cooking facilities
- [ ] `watersource` - water source
- [ ] `waterdistance` - distance to water
- [ ] Visit frequency to different outlets

**Desirability (OP021-024)**
- [ ] Shopping motives (health, trust, preference)
- [ ] Reason/motivation variables present
- [ ] Perception of food safety/quality

### Emergent Dimension Variables

**Food Safety Index (OP025)**
- [ ] Component variables: `clean`, `safe`, `reputation`
- [ ] All three present for aggregation

**Social Forces (OP026-027)**
- [ ] Trust-based shopping indicator
- [ ] Decision-maker gender (if applicable)

**Stability (OP028)**
- [ ] Visit frequency variation data
- [ ] Multiple outlet types

### Outcome Variables

**HDDS (OP029)**
- [ ] All 11 consumption items present (as `hh_consumption_*`)
- [ ] Can be summed for HDDS calculation

**Diet Composition (OP030-032)**
- [ ] Nutrients/quality data present (if available)
- [ ] Classification into nutrient-dense vs processed

**Diet Tier (OP033)**
- [ ] Classification basis identified
- [ ] Categories clear

---

## File Management

### Input Files
- [ ] Original data files remain unchanged in `00_inputs/data/`
- [ ] No modifications to source files

### Output Files Created
- [ ] `01_scripts/Phase_0_household_processed.csv` - cleaned household data
- [ ] `01_scripts/Phase_0_vendor_processed.csv` - cleaned vendor data
- [ ] `01_scripts/Phase_0_summary.RDS` - summary statistics

### Documentation
- [ ] Phase 0 log created in `03_logs/Phase_0_DataConsolidation_Log.md`
- [ ] Issues encountered documented
- [ ] Solutions applied documented
- [ ] Timestamp recorded

---

## Sample Size Verification

**Before Any Analysis:**
- [ ] Household n = 241 confirmed in processed data
- [ ] Vendor n = 284 confirmed in processed data
- [ ] No data lost during processing
- [ ] All observations have ID (if ID required)

**Missing Cases:**
- [ ] Total count: _____ households with complete data
- [ ] Total count: _____ households with >30% missing
- [ ] Decision documented: exclude vs include

---

## Code Completion

### R Script
- [ ] Data loading code runs without errors
- [ ] Variable renaming code executes correctly
- [ ] Data verification code runs successfully
- [ ] Output files saved correctly
- [ ] Script saved in `01_scripts/Phase_0_Script.R`

### Python Script (Optional)
- [ ] If using Python, equivalent script created
- [ ] Script saved in `01_scripts/Phase_0_Script.py`

### Comments & Documentation
- [ ] Code is commented and readable
- [ ] Function names are descriptive
- [ ] Variable names follow naming conventions
- [ ] Future analyst could understand approach

---

## Error Resolution

### Data Loading Issues
- [ ] Encoding errors resolved (if any)
- [ ] Column delimiter correct
- [ ] Date format handled appropriately

### Variable Conflicts
- [ ] `foodgroups_001_*` vs `foodgroups` conflict resolved
- [ ] Renamed variables verified in dataset
- [ ] Old variable names confirmed deleted/not present

### Missing Data Handling
- [ ] Missing value codes identified (NA, -99, etc.)
- [ ] Consistent handling across dataset
- [ ] Documented in Phase 0 log

### Dimension Mismatches
- [ ] Expected rows match actual (241 households, 284 vendors)
- [ ] Unexpected variables documented
- [ ] Missing variables documented

---

## Documentation Review

### Phase 0 Log File (`03_logs/Phase_0_DataConsolidation_Log.md`)
Contains:
- [ ] Start time and completion time
- [ ] Data files loaded (names, paths)
- [ ] Sample sizes (before/after if applicable)
- [ ] Variables renamed with before/after names
- [ ] Missing data patterns described
- [ ] Any issues encountered
- [ ] How issues were resolved
- [ ] Variables available for analysis
- [ ] Variables NOT available (why)
- [ ] Next phase readiness statement

---

## Final Verification

### Before Moving to Phase 1

Complete this final checklist:

- [ ] All data loaded successfully
- [ ] Critical variable renaming completed
- [ ] No naming conflicts remain
- [ ] Missing data assessed
- [ ] Data quality verified
- [ ] Processed files saved
- [ ] Documentation complete
- [ ] No errors in code
- [ ] Phase 0 log written
- [ ] Ready for Phase 1? **YES / NO**

---

## Sign-Off

**Phase 0 Completion:**

```
Date Completed: _______________
Household n: 241 ✅ Confirmed
Vendor n: 284 ✅ Confirmed
Critical Renaming: ✅ Complete
Missing Data Assessment: ✅ Complete
Documentation: ✅ Complete

Ready for Phase 1? ☐ YES  ☐ NOT YET (document why below)

Notes:


```

---

## If Issues Remain

If Phase 0 is not complete, document:

1. **What's incomplete?**
   - [ ] Data loading issues
   - [ ] Variable renaming issues
   - [ ] Missing data assessment
   - [ ] Documentation missing
   - [ ] Other: _____________

2. **What needs to be fixed?**
   ```

   ```

3. **When will it be fixed?**
   ```

   ```

---

## Next Steps

✅ **Phase 0 Complete?** YES
→ Proceed to Phase 1: Data Cleaning & Variable Specification

❌ **Phase 0 Not Complete?**
→ Review this checklist and identify blockers
→ Fix issues before proceeding
→ Return here and mark complete

---

**Document Status**: Phase 0 Completion Checklist
**Last Updated**: 2025-11-23
