# COMPREHENSIVE SURVEY SECTION MAP
## Household Survey - Long Bien District 2024

**Created**: 2025-11-23
**Purpose**: Systematic documentation of ALL survey sections with conditional display logic
**Total Survey Variables**: 398
**Total Households**: 214

---

## 📊 SURVEY STRUCTURE OVERVIEW

This survey contains **10 major conditional sections** where questions are shown only to specific household subsamples based on gatekeeping questions. Understanding these sections is CRITICAL for variable construction and analysis planning.

### Key Subsample Definitions

| Subsample | N | % of Total | Defining Variable |
|-----------|---|------------|-------------------|
| **Location Choosers** | 99 | 46.3% | `lifelonglocation == 'no'` |
| **Lifelong Residents** | 66 | 30.8% | `lifelonglocation == 'yes'` |
| **Gatekeeping NaN** | 49 | 22.9% | `lifelonglocation.isna()` |
| **Farming Households** | 40 | 18.7% | `farms == 'yes'` |
| **Non-farming** | 122 | 57.0% | `farms == 'no'` |
| **Household Vendors** | 41 | 19.2% | `hh_vendor in ['yes', 'supplier']` |
| **Non-vendors** | 121 | 56.5% | `hh_vendor == 'no'` |
| **No Piped Water** | 1 | 0.5% | `watersource == 'no'` |
| **Piped Water Access** | 160 | 74.8% | `watersource == 'yes'` |

---

## 🔴 SECTION 1: LOCATION CHOICE FACTORS
### ⚠️ CRITICAL SECTION - Affects OP Variables

**Section Type**: Conditional
**Gatekeeping Question**: `lifelonglocation` - "Have you lived in this house all your life?"
**Display Logic**: Only shown if `lifelonglocation == 'no'`
**Conceptual Basis**: Location choice motivations only applicable to households who MADE a location choice

### Expected Respondents
- **Show to**: Location Choosers (N=99, 46.3%)
- **Skip for**: Lifelong residents (N=66, 30.8%) + Gatekeeping NaN (N=49, 22.9%)
- **Expected Missing**: 115 households (53.7%)

### Variables in Section (10 total)

| Variable | Question | Type | Valid N | Missing N | Missing % |
|----------|----------|------|---------|-----------|-----------|
| `bridge_city` | Bridge to city center importance | Likert -2 to +2 | 99 | 115 | 53.7% |
| `waterdistance` | Proximity to water importance | Likert -2 to +2 | 99 | 115 | 53.7% |
| `safe_reputation` | Safety/reputation importance | Likert -2 to +2 | 99 | 115 | 53.7% |
| `flooding` | Flooding concerns importance | Likert -2 to +2 | 99 | 115 | 53.7% |
| `infrastructure` | Infrastructure quality importance | Likert -2 to +2 | 99 | 115 | 53.7% |
| `foodenvironment` | Food environment importance | Likert -2 to +2 | 99 | 115 | 53.7% |
| `schools` | School quality importance | Likert -2 to +2 | 99 | 115 | 53.7% |
| `medical` | Medical services importance | Likert -2 to +2 | 99 | 115 | 53.7% |
| `religion` | Religious facilities importance | Likert -2 to +2 | 99 | 115 | 53.7% |
| `leisure` | Leisure facilities importance | Likert -2 to +2 | 99 | 115 | 53.7% |

### ⚠️ OP Variables Affected

| OP Variable | Source Variable | Implications |
|-------------|-----------------|--------------|
| **OP007_infrastructure** | `infrastructure` | Only applicable to Location Choosers (N=99) |
| **OP019_water_distance** | `waterdistance` | Only applicable to Location Choosers (N=99) |

### Verification
```python
# Skip logic PERFECTLY enforced
lifelong_yes = (df['lifelonglocation'] == 'yes')  # 66 households
lifelong_yes_answered = (lifelong_yes & df['infrastructure'].notna()).sum()  # 0
# Result: ZERO lifelong residents answered these questions ✅
```

### Analysis Implications
- ⚠️ Including these variables in regression reduces sample to N=64 (70% loss)
- ✅ Conceptually appropriate: Cannot ask "why did you choose this location?" to someone who never chose it
- ✅ This is STRUCTURAL missingness (MNAR by design), NOT random missing data
- ❌ Multiple imputation INAPPROPRIATE - cannot impute location choice motivations for non-choosers

---

## 🔴 SECTION 2: MIGRATION PUSH FACTORS
### "Why Did You Leave Previous Location?"

**Section Type**: Conditional
**Gatekeeping Question**: `lifelonglocation` - "Have you lived in this house all your life?"
**Display Logic**: Only shown if `lifelonglocation == 'no'`
**Conceptual Basis**: Push factors only relevant for households who moved FROM somewhere

### Expected Respondents
- **Show to**: Location Choosers (N=99, 46.3%)
- **Expected Missing**: 117 households (54.7%)
- **Actual Respondents**: 97 households (2 location choosers didn't answer)

### Variables in Section (20 total)

**Base variable**: `moveaway-reasons` (multi-select)

**Individual factors** (all binary 0/1):
1. `moveaway-reasons/husband` - Husband's decision
2. `moveaway-reasons/family` - Family reasons
3. `moveaway-reasons/inherited` - Inherited property
4. `moveaway-reasons/own` - Owned property
5. `moveaway-reasons/rent` - Rental reasons
6. `moveaway-reasons/services` - Access to services
7. `moveaway-reasons/reputation` - Neighborhood reputation
8. `moveaway-reasons/flooding` - Flooding issues
9. `moveaway-reasons/workdistance` - Distance to work
10. `moveaway-reasons/familydistance` - Distance to family
11. `moveaway-reasons/jobloss` - Job loss
12. `moveaway-reasons/newjob` - New job opportunity
13. `moveaway-reasons/allocated` - Housing allocation
14. `moveaway-reasons/highrent` - High rent
15. `moveaway-reasons/justcause` - Legal eviction
16. `moveaway-reasons/refugee` - Displacement/refugee
17. `moveaway-reasons/forcemajor` - Force majeure event
18. `moveaway-reasons/other` - Other reason

### ⚠️ OP Variables Affected
**Currently**: None identified in existing OP001-OP033 set
**Check if needed**: Verify no OP variables derived from push factors

---

## 🔴 SECTION 3: MIGRATION PULL FACTORS
### "Why Did You Choose Current Location?"

**Section Type**: Conditional
**Gatekeeping Question**: `lifelonglocation` - "Have you lived in this house all your life?"
**Display Logic**: Only shown if `lifelonglocation == 'no'`
**Conceptual Basis**: Pull factors only relevant for households who chose TO move here

### Expected Respondents
- **Show to**: Location Choosers (N=99, 46.3%)
- **Expected Missing**: 117 households (54.7%)
- **Actual Respondents**: 97 households

### Variables in Section (15 total)

**Base variable**: `movetowards-reasons` (multi-select)

**Individual factors** (all binary 0/1):
1. `movetowards-reasons/husband` - Husband's location
2. `movetowards-reasons/family` - Family proximity
3. `movetowards-reasons/inherited` - Inherited property
4. `movetowards-reasons/own` - Owned property
5. `movetowards-reasons/rent` - Affordable rent
6. `movetowards-reasons/house` - Housing quality
7. `movetowards-reasons/services` - Service access
8. `movetowards-reasons/reputation` - Good reputation
9. `movetowards-reasons/workdistance` - Proximity to work
10. `movetowards-reasons/familydistance` - Proximity to family
11. `movetowards-reasons/jobopportunity` - Job opportunities
12. `movetowards-reasons/allocated` - Allocated housing
13. `movetowards-reasons/other` - Other reason

### ⚠️ OP Variables Affected
**Currently**: None identified
**Check if needed**: Verify no OP variables derived from pull factors

---

## 🔴 SECTION 4: LOCATION HISTORY DETAILS

**Section Type**: Conditional
**Gatekeeping Question**: `lifelonglocation` - "Have you lived in this house all your life?"
**Display Logic**: Only shown if `lifelonglocation == 'no'`

### Expected Respondents
- **Show to**: Location Choosers (N=99, 46.3%)
- **Expected Missing**: ~115 households (53.7%)

### Variables in Section (3 total)

| Variable | Question | Valid N | Missing N | Missing % |
|----------|----------|---------|-----------|-----------|
| `previouslocation` | Previous location type | 99 | 115 | 53.7% |
| `previouslocationnua` | Specific previous location | ~99 | ~115 | 53.7% |
| `locationtime` | Year moved here | 98 | 116 | 54.2% |
| `locationtime_age` | Age when moved here | 66 | 148 | 69.2% |

### ⚠️ OP Variables Affected
**Currently**: None identified

---

## 🟡 SECTION 5: TYPHOON YAGI PREPARATION

**Section Type**: Conditional (likely based on typhoon exposure/awareness)
**Gatekeeping Question**: UNKNOWN - needs investigation
**Hypothesis**: Possibly shown only to households in typhoon-affected areas or with typhoon awareness

### Expected Respondents
- **Answered**: 105 households (49.1%)
- **Missing**: 109 households (50.9%)

### Variables in Section (9 total)

**Base variable**: `typhoon_prepare` (multi-select)

**Individual preparation measures** (all binary 0/1):
1. `typhoon_prepare/stockpiling` - Stockpiling food/water
2. `typhoon_prepare/securing` - Securing property
3. `typhoon_prepare/securing_away` - Securing items away
4. `typhoon_prepare/strengthening_infrastructure` - Strengthening structure
5. `typhoon_prepare/collaborating_vendors` - Coordinating with vendors
6. `typhoon_prepare/saving_cash` - Saving cash
7. `typhoon_prepare/communicating_customers` - Informing customers
8. `typhoon_prepare/contingency_poweroutages` - Power outage contingency

### ⚠️ OP Variables Affected
**Currently**: None identified
**Action**: Investigate gatekeeping logic - why 109 households skipped this section

---

## 🟡 SECTION 6: TYPHOON YAGI COPING STRATEGIES

**Section Type**: Conditional (likely based on typhoon impact)
**Gatekeeping Question**: UNKNOWN - needs investigation
**Hypothesis**: Possibly shown only to households directly impacted by Typhoon Yagi

### Expected Respondents
- **Answered**: 141 households (65.9%)
- **Missing**: 73 households (34.1%)

### Variables in Section (6 total)

**Base variable**: `typhoon_cope` (multi-select)

**Individual coping strategies** (all binary 0/1):
1. `typhoon_cope/lockdown` - Full lockdown
2. `typhoon_cope/partial_lockdown` - Partial lockdown
3. `typhoon_cope/socialaccess` - Social network access
4. `typhoon_cope/financialaccess` - Financial assistance access
5. `typhoon_cope/physicalaccess` - Physical access maintained

**Additional variables**:
- `typhoon_financial` - Financial impact (categorical)
- `typhoon_damages` - Damage assessment (categorical)

### ⚠️ OP Variables Affected
**Currently**: None identified
**Action**: Investigate gatekeeping logic - why 73 households skipped this section

---

## 🟠 SECTION 7: URBAN AGRICULTURE / FARMING

**Section Type**: Conditional
**Gatekeeping Question**: `farms` - "Does your household engage in farming activities?"
**Display Logic**: Only shown if `farms == 'yes'`
**Conceptual Basis**: Farming details only relevant for households that farm

### Expected Respondents
- **Show to**: Farming households (N=40, 18.7%)
- **Skip for**: Non-farming (N=122, 57.0%) + NaN (N=52, 24.3%)
- **Expected Missing**: 174 households (81.3%)

### Variables in Section (6 total)

| Variable | Question | Type | Valid N | Missing N | Missing % |
|----------|----------|------|---------|-----------|-----------|
| `farmlandtype` | Type of farming space | Categorical | 40 | 174 | 81.3% |
| `farmlandtype_other` | Other type (specify) | Text | ~10 | ~204 | ~95% |
| `farmlocation` | Farm location | Categorical | 40 | 174 | 81.3% |
| `farmpurpose` | Farming purpose | Categorical | 40 | 174 | 81.3% |
| `farmpurpose_other` | Other purpose (specify) | Text | ~10 | ~204 | ~95% |
| `consumptionpercentage` | % production consumed | Numeric 0-100% | 40 | 174 | 81.3% |
| `farmsize` | Farm size | Numeric (m²) | 39 | 175 | 81.8% |

### Sub-Section: Land Access Uncertainty

**Gatekeeping**: `accessuncertainty == 'yes'` (within farmers only)
**Expected respondents**: ~15 households (7% of total, ~38% of farmers)
**Expected missing**: 199 households (93.0%)

Variables asking about:
- Uncertainty concerns
- Duration of uncertainty
- Impact on farming decisions

### ⚠️ OP Variables Affected
**Currently**: None identified
**Check if needed**: Verify no OP variables derived from farming activities

---

## 🟠 SECTION 8: HOUSEHOLD VENDING ACTIVITIES

**Section Type**: Conditional
**Gatekeeping Question**: `hh_vendor` - "Does your household have a vendor/seller?"
**Display Logic**: Only shown if `hh_vendor in ['yes', 'supplier']`
**Conceptual Basis**: Vending details only relevant for households that sell food

### Expected Respondents
- **Show to**: Vendor households (N=41, 19.2% - includes 34 'yes' + 7 'supplier')
- **Skip for**: Non-vendors (N=121, 56.5%) + NaN (N=52, 24.3%)
- **Expected Missing**: 173 households (80.8%)

### Variables in Section (2 total)

| Variable | Question | Type | Valid N | Missing N | Missing % |
|----------|----------|------|---------|-----------|-----------|
| `vendortype` | Type of vending | Categorical | 34 | 180 | 84.1% |
| `reason` | Reason for vending location | Categorical | 34 | 180 | 84.1% |

**Note**: These variables appear to only capture 'yes' respondents, not 'supplier' respondents (34 vs 41)

### ⚠️ OP Variables Affected
**Currently**: None identified
**Check if needed**: Verify no OP variables derived from vending activities

---

## 🟠 SECTION 9: WATER SOURCE DISTANCE (ACTUAL MEASUREMENT)

**Section Type**: Conditional
**Gatekeeping Question**: `watersource` - "Does your household have piped water access?"
**Display Logic**: Only shown if `watersource == 'no'`
**Conceptual Basis**: Distance to water source only relevant for households WITHOUT piped water

### Expected Respondents
- **Show to**: No piped water (N=1, 0.5%)
- **Skip for**: Piped water (N=160, 74.8%) + NaN (N=53, 24.8%)
- **Expected Missing**: 213 households (99.5%)

### Variables in Section (1 total)

| Variable | Question | Type | Valid N | Missing N | Missing % |
|----------|----------|------|---------|-----------|-----------|
| `waterdistance_001` | Distance to water source | Numeric (meters) | 1 | 213 | 99.5% |

### ⚠️ CRITICAL DISTINCTION

| Variable | Type | Section | Gatekeeping | Applicable To |
|----------|------|---------|-------------|---------------|
| **`waterdistance`** | Likert perception (-2 to +2) | Location Choice Factors | `lifelonglocation == 'no'` | Location Choosers (N=99) |
| **`waterdistance_001`** | Actual distance (meters) | Water Source Distance | `watersource == 'no'` | No piped water (N=1) |

### ⚠️ OP Variables Affected

| OP Variable | Uses Which Variable? | Check Needed |
|-------------|---------------------|--------------|
| **OP019_water_distance** | Need to verify: `waterdistance` (perception) vs `waterdistance_001` (actual) | **HIGH PRIORITY** |

**Action Required**: Verify which variable OP019 uses. If it uses `waterdistance_001`, applicable sample is N=1 (essentially unusable).

---

## 🟠 SECTION 10: FOOD WASTE

**Section Type**: Conditional (likely survey wave-based)
**Gatekeeping Question**: UNKNOWN - possibly survey version/wave
**Hypothesis**: Food waste questions added in later survey wave

### Expected Respondents
- **Answered**: ~39-47 households (18-22%)
- **Missing**: ~167-175 households (78-82%)

### Variables in Section (10 total)

| Variable | Question | Type | Missing N | Missing % |
|----------|----------|------|-----------|-----------|
| `foodwaste_amount` | Amount wasted | Numeric (kg or bags) | 167 | 78.0% |
| `foodwaste_amount_unit` | Time unit | Categorical (day/week/month) | 175 | 81.8% |
| `foodwaste_freq` | Frequency | Numeric (days/month) | 169 | 79.0% |
| `foodwaste_mainreason` | Main reasons (base) | Multi-select | 175 | 81.8% |
| `foodwaste_mainreason/deteriorated` | Food deteriorated | Binary 0/1 | 175 | 81.8% |
| `foodwaste_mainreason/usebydate` | Passed use-by date | Binary 0/1 | 175 | 81.8% |
| `foodwaste_mainreason/unappetizing` | Unappetizing | Binary 0/1 | 175 | 81.8% |
| `foodwaste_mainreason/toomuch` | Cooked too much | Binary 0/1 | 175 | 81.8% |
| `foodwaste_mainreason/toomanyingredients` | Too many ingredients | Binary 0/1 | 175 | 81.8% |
| `foodwaste_mainreason/other` | Other reason | Binary 0/1 | 175 | 81.8% |

**Disposal methods** (separate multi-select):
- `foodwaste_whatdo/throwaway` - Throw away
- `foodwaste_whatdo/giveaway` - Give away
- `foodwaste_whatdo/foodbank` - Food bank donation
- `foodwaste_whatdo/composting_community` - Community composting
- `foodwaste_whatdo/composting_hh` - Household composting
- `foodwaste_whatdo/animalfood` - Animal feed
- `foodwaste_whatdo/other` - Other method

### ⚠️ OP Variables Affected
**Currently**: None identified
**Action**: Investigate gatekeeping logic - appears to be survey wave, not conditional question

---

## 📋 SECTION SUMMARY TABLE

| Section | Gatekeeping | Variables | Missing N | Missing % | OP Variables Affected |
|---------|-------------|-----------|-----------|-----------|----------------------|
| **1. Location Choice Factors** | `lifelonglocation == 'no'` | 10 | 115 | 53.7% | OP007, OP019 ⚠️ |
| **2. Migration Push Factors** | `lifelonglocation == 'no'` | 20 | 117 | 54.7% | None identified |
| **3. Migration Pull Factors** | `lifelonglocation == 'no'` | 15 | 117 | 54.7% | None identified |
| **4. Location History** | `lifelonglocation == 'no'` | 3 | ~115 | ~53.7% | None identified |
| **5. Typhoon Preparation** | Unknown (needs investigation) | 9 | 109 | 50.9% | None identified |
| **6. Typhoon Coping** | Unknown (needs investigation) | 6 | 73 | 34.1% | None identified |
| **7. Farming Activities** | `farms == 'yes'` | 6 | 174 | 81.3% | None identified |
| **8. Vendor Activities** | `hh_vendor in ['yes', 'supplier']` | 2 | 173 | 80.8% | None identified |
| **9. Water Distance (Actual)** | `watersource == 'no'` | 1 | 213 | 99.5% | OP019? (verify) ⚠️ |
| **10. Food Waste** | Unknown (survey wave?) | 10 | ~175 | ~81.8% | None identified |

**TOTAL CONDITIONAL VARIABLES**: 82+ variables across 10 sections

---

## 🚨 CRITICAL ACTIONS REQUIRED

### Priority 1: Validate OP019_water_distance Source
**Issue**: Two variables with similar names but VASTLY different applicability:
- `waterdistance` - Likert perception (N=99, Location Choosers)
- `waterdistance_001` - Actual distance (N=1, no piped water)

**Action**:
```python
# Check phase_1_CORRECTED_variable_construction.py
# Verify which source variable OP019 uses
# If waterdistance → N=99 applicable
# If waterdistance_001 → N=1 applicable (CRITICAL ISSUE)
```

### Priority 2: Verify All 25 OP Variables Against Sections
**Remaining to check**: OP001-OP006, OP008-OP018, OP020-OP033

**Sections to cross-reference**:
- Migration factors (push/pull)
- Typhoon sections
- Farming/vendor sections
- Location history
- Food waste

### Priority 3: Investigate Unknown Gatekeeping Logic
**Sections needing investigation**:
- Typhoon Preparation (50.9% missing)
- Typhoon Coping (34.1% missing)
- Food Waste (~82% missing)

**Method**:
- Check survey codebook for display logic
- Analyze raw survey files
- Consult with survey team if needed

---

## 📝 USAGE GUIDELINES

### For Variable Construction (Phase 1)
1. **Check this map FIRST** before creating any OP variable
2. **Document survey context** in variable metadata
3. **Calculate expected missingness** based on gatekeeping logic
4. **Flag high missingness** (>40%) for automatic investigation
5. **Define applicable subsample** explicitly

### For Analysis Planning (Phase 2)
1. **Map ALL predictors** to survey sections
2. **Identify universal vs conditional** predictors
3. **Calculate sample sizes** for each model specification
4. **Consider subsample analyses** where appropriate
5. **Pre-register** decisions about conditional variables

### For Limitations Writing (Phase 4)
1. **Explain structural missingness** correctly (survey design, not data loss)
2. **Justify inclusion/exclusion** of conditional variables
3. **Define applicable population** for each analysis
4. **Acknowledge conceptual constraints** of subsample-specific variables

---

**Document Status**: ✅ COMPLETE - All 10 conditional sections mapped
**Last Updated**: 2025-11-23
**Next Actions**: Validate OP019 source + verify all 25 OP variables
