---
title: "Phase 0 EDA: Comprehensive Data Exploration Report"
date: 2025-11-23
status: "Complete"
---

# Phase 0 Exploratory Data Analysis

## Executive Summary

**Household Sample**: 214 records (expected 241)
**Vendor Sample**: 284 records (matches expected 284)

### Key Findings

1. **Sample Size Discrepancy**: Household data has 214 records, not 241
2. **Food-related Variables**: 68 in household, 35 in vendor
3. **Diet/Consumption Variables**: 44 potential HDDS components found
4. **Complete Variables**: 12 household, 10 vendor

## Household Data Structure

**Dimensions**: 214 rows × 365 columns

### Variable Patterns

**Accessibility** (35 variables):
- `Time`
- `_submission_time`
- `accessuncertainty`
- `accessuncertaintyreason`
- `accessuncertaintyreason/evictions_govt`
- `accessuncertaintyreason/familyissues`
- `accessuncertaintyreason/flooding`
- `accessuncertaintyreason/landgrab_companies`
- `accessuncertaintyreason/landgrab_squatters`
- `accessuncertaintyreason/landlord`
- `accessuncertaintyreason/policy`
- `accessuncertaintyreason/squatter`
- `accessuncertaintyreason/urbangrowth_rent`
- `accessuncertaintyreason/urbangrowth_sell`
- `foodexp_timeunit`
- ... and 20 more

**Consumption** (11 variables):
- `consumptionpercentage`
- `foodgroups/meat_flesh`
- `foodgroups/meat_organ`
- `foodgroups_001/meat_flesh`
- `foodgroups_001/meat_organ`
- `recreation`
- `recreation/neg_notenough`
- `recreation/neg_toomany`
- `recreation/neutral_unimportant`
- `recreation/none`
- `recreation/pos_sufficient`

**Expenditure** (1 variables):
- `foodexpenditure`

**Food Related** (68 variables):
- `fewfoods`
- `foodenvironment`
- `foodenvironment_001`
- `foodenvironment_001/neg_notenough`
- `foodenvironment_001/neg_toomany`
- `foodenvironment_001/neutral_unimportant`
- `foodenvironment_001/none`
- `foodenvironment_001/pos_sufficient`
- `foodenvironment_002`
- `foodexp_timeunit`
- `foodexpenditure`
- `foodgroups/cereals`
- `foodgroups/eggs`
- `foodgroups/fish_seafood`
- `foodgroups/fruits_other`
- ... and 53 more

**Numbered Series** (8 variables):
- `reason_001_other`
- `reason_002_other`
- `reason_003_other`
- `reason_004_other`
- `reason_005_other`
- `reason_006_other`
- `reason_007_other`
- `reason_008_other`

**Quality** (6 variables):
- `clean`
- `moveaway-reasons/reputation`
- `movetowards-reasons/reputation`
- `reputation`
- `safe`
- `safe_reputation`

### Diet/Consumption Variables

- `farmlandtype_other`
- `farmlocation_other`
- `farmpurpose_other`
- `foodgroups/cereals`
- `foodgroups/eggs`
- `foodgroups/fish_seafood`
- `foodgroups/fruits_other`
- `foodgroups/fruits_vitamina`
- `foodgroups/legumes_nuts_seeds`
- `foodgroups/meat_flesh`
- `foodgroups/meat_organ`
- `foodgroups/milk`
- `foodgroups/oils_fats`
- `foodgroups/veg_other`
- `foodgroups_001/cereals`
- `foodgroups_001/eggs`
- `foodgroups_001/fish_seafood`
- `foodgroups_001/fruits_other`
- `foodgroups_001/fruits_vitamina`
- `foodgroups_001/legumes_nuts_seeds`
- `foodgroups_001/meat_flesh`
- `foodgroups_001/meat_organ`
- `foodgroups_001/milk`
- `foodgroups_001/oils_fats`
- `foodgroups_001/veg_other`
- `foodwaste_mainreason/other`
- `foodwaste_whatdo/other`
- `housingtype_other`
- `moveaway-reasons/other`
- `moveaway-reasons_other`
- `movetowards-reasons/other`
- `movetowards-reasons_other`
- `reason_001_other`
- `reason_002_other`
- `reason_003_other`
- `reason_004_other`
- `reason_005_other`
- `reason_006_other`
- `reason_007_other`
- `reason_008_other`
- `reason_other`
- `refusalreason/other`
- `refusalreason_other`
- `resp_ethn_other`

### Missing Data Summary

- Complete (0% missing): 12 variables
- Low missing (>0-10%): 8 variables
- Medium missing (>10-30%): 118 variables
- High missing (>30-<100%): 194 variables
- All missing (100%): 33 variables

### Operationalization Mapping

**OP001-002_Availability**: 18 variables
  - `foodgroups_001`
  - `foodgroups_001/cereals`
  - `foodgroups_001/eggs`
  - `foodgroups_001/fish_seafood`
  - `foodgroups_001/fruits_other`
  - ... and 13 more

**OP003_Affordability_Motive**: 0 variables
  - ❌ No matching variables

**OP004-007_Vendor_Quality**: 8 variables
  - `clean`
  - `infrastructure`
  - `moveaway-reasons/reputation`
  - `movetowards-reasons/reputation`
  - `reputation`
  - ... and 3 more

**OP009-011_Accessibility**: 52 variables
  - `Time`
  - `_submission_time`
  - `accessuncertainty`
  - `accessuncertaintyreason`
  - `accessuncertaintyreason/evictions_govt`
  - ... and 47 more

**OP012-016_Expenditure**: 2 variables
  - `foodexpenditure`
  - `income`

**OP017-020_Convenience**: 4 variables
  - `cookingsource`
  - `waterdistance`
  - `waterdistance_001`
  - `watersource`

**OP021-024_Desirability**: 81 variables
  - `accessuncertaintyreason`
  - `accessuncertaintyreason/evictions_govt`
  - `accessuncertaintyreason/familyissues`
  - `accessuncertaintyreason/flooding`
  - `accessuncertaintyreason/landgrab_companies`
  - ... and 76 more

**OP025_Food_Safety_Index**: 6 variables
  - `clean`
  - `moveaway-reasons/reputation`
  - `movetowards-reasons/reputation`
  - `reputation`
  - `safe`
  - ... and 1 more

**OP026-027_Social**: 1 variables
  - `resp_gender`

**OP028_Stability**: 0 variables
  - ❌ No matching variables

**OP029_HDDS**: 95 variables
  - `consumptionpercentage`
  - `farmlandtype_other`
  - `farmlocation_other`
  - `farmpurpose_other`
  - `fewfoods`
  - ... and 90 more

**OP030-032_Diet_Quality**: 2 variables
  - `healthy`
  - `wholeorprocessed`

**OP033_Diet_Tier**: 0 variables
  - ❌ No matching variables

## Vendor Data Structure

**Dimensions**: 284 rows × 132 columns

### Variable Patterns

**Accessibility** (4 variables):
- `Time`
- `_submission_time`
- `locationtime`
- `refusalreason/no_time`

**Consumption** (2 variables):
- `foodgroups/meat_flesh`
- `foodgroups/meat_organ`

**Food Related** (35 variables):
- `foodgroups`
- `foodgroups/cereals`
- `foodgroups/eggs`
- `foodgroups/fish_seafood`
- `foodgroups/fruits_other`
- `foodgroups/fruits_vitamina`
- `foodgroups/legumes_nuts_seeds`
- `foodgroups/meat_flesh`
- `foodgroups/meat_organ`
- `foodgroups/milk`
- `foodgroups/oils_fats`
- `foodgroups/spices_cond_bev`
- `foodgroups/sweets`
- `foodgroups/veg_darkgreenleafy`
- `foodgroups/veg_other`
- ... and 20 more

**Quality** (1 variables):
- `safe_reputation`

### Operationalization Mapping

**OP001-002_Availability**: 2 variables
  - `supplychain`
  - `typhoon_prepare/stockpiling`

**OP003_Affordability_Motive**: 2 variables
  - `typhoon_cope/cheaper`
  - `typhoon_cope/more_expensive`

**OP004-007_Vendor_Quality**: 3 variables
  - `infrastructure`
  - `safe_reputation`
  - `typhoon_prepare/strengthening_infrastructure`

**OP009-011_Accessibility**: 7 variables
  - `Time`
  - `_submission_time`
  - `locationtime`
  - `refusalreason/no_time`
  - `refusalreason/undisclosed`
  - ... and 2 more

**OP012-016_Expenditure**: 0 variables
  - ❌ No matching variables

**OP017-020_Convenience**: 0 variables
  - ❌ No matching variables

**OP021-024_Desirability**: 17 variables
  - `foodwaste_mainreason`
  - `foodwaste_mainreason/deteriorated`
  - `foodwaste_mainreason/other`
  - `foodwaste_mainreason/toomanyingredients`
  - `foodwaste_mainreason/toomuch`
  - ... and 12 more

**OP025_Food_Safety_Index**: 1 variables
  - `safe_reputation`

**OP026-027_Social**: 1 variables
  - `resp_gender`

**OP028_Stability**: 0 variables
  - ❌ No matching variables

**OP029_HDDS**: 39 variables
  - `foodgroups`
  - `foodgroups/cereals`
  - `foodgroups/eggs`
  - `foodgroups/fish_seafood`
  - `foodgroups/fruits_other`
  - ... and 34 more

**OP030-032_Diet_Quality**: 1 variables
  - `wholeorprocessed`

**OP033_Diet_Tier**: 0 variables
  - ❌ No matching variables

## Recommendations

1. **Phase 1 Priority**: Map actual variable names to OPs using codebooks
2. **Sample Size**: Document 214 household sample in all analyses
3. **HDDS Calculation**: Identify exact consumption variables before calculating
4. **Missing Data**: Use complete and low-missing variables for primary analyses
5. **Operationalization**: Reconcile OP guide with actual data structure

