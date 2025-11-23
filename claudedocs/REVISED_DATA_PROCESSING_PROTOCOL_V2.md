# REVISED DATA PROCESSING PROTOCOL V2.0
## A Ground-Up Redesign: Learning from Systematic Failures

---

**Purpose**: Complete data processing protocol for complex survey data with conditional sections, skip logic, and multiple subsamples
**Audience**: Researchers starting fresh OR auditing existing work
**Based On**: Lessons learned from WFL Analysis systematic failures (Nov 2025)
**Status**: Ready for implementation

---

## 🎯 CORE PHILOSOPHY

### Principles

1. **Survey Structure First, Variables Second**
   - Understand the survey BEFORE creating any variables
   - Map sections, skip logic, subsamples BEFORE coding

2. **Document Everything, Assume Nothing**
   - If it's not documented, it doesn't exist
   - Every decision needs a paper trail

3. **Red Flags Trigger Investigation, Not Acceptance**
   - High missingness = investigate why, not accept as normal
   - Unusual patterns = stop and understand

4. **Subsample Awareness Throughout**
   - Not all questions apply to all respondents
   - Design analyses appropriate for each subsample

5. **Cross-Phase Integration**
   - Phase N findings must inform Phase N+1 decisions
   - Create feedback loops, not linear workflows

---

## 📋 PHASE 0: SURVEY STRUCTURE ANALYSIS (MANDATORY FOUNDATION)

**GATE**: Cannot proceed to Phase 1 until ALL Phase 0 deliverables complete ✅

### Step 0.1: Raw Data Inventory

**Objective**: Understand what data you actually have

**Tasks**:
1. List all data files (household survey, vendor survey, etc.)
2. Check file formats (Excel sheets, CSV structure)
3. Verify row counts match expected sample sizes
4. Identify if data is split across files (with/without food waste, etc.)
5. Document merge strategy if needed

**Deliverable**: `00_RAW_DATA_INVENTORY.md`

**Template**:
```markdown
# Raw Data Inventory

## Files Available
- `household_with_foodwaste.xlsx` (75 rows × 352 columns)
- `household_without_foodwaste.xlsx` (139 rows × 347 columns)
- `household_merged.csv` (214 rows × 365 columns)

## Merge Status
- ✅ Merged file exists
- ✅ Row counts sum correctly (75 + 139 = 214)
- ⚠️ Column counts differ - investigate

## Expected Sample Sizes
- Target: 250 households
- Actual: 214 households (85.6% response rate)
- Missing: 36 households (refusals, not home, etc.)

## Data Quality Checks
- [x] No duplicate IDs
- [x] GPS coordinates present for all
- [x] Timestamps logical (end > start)
```

---

### Step 0.2: Survey Documentation Review

**Objective**: Gather ALL survey design documentation

**Required Documents**:
1. **Survey codebook** (KoboToolbox export or equivalent)
2. **Survey flow diagram** (if available)
3. **Questionnaire** (English + local language)
4. **Enumerator instructions** (if available)
5. **Data collection protocol**

**If Missing**: Contact survey team BEFORE proceeding

**Deliverable**: `00_SURVEY_DOCUMENTATION_INDEX.md`

---

### Step 0.3: Survey Section Mapping ⭐ CRITICAL

**Objective**: Map ALL survey sections, gatekeeping questions, and skip logic

**Process**:

**Step 3A: Identify All Survey Sections**

Read through codebook/questionnaire and create section inventory:

```markdown
# Survey Section Map

## Section 1: Household Demographics
- **Variables**: 15 variables (household_size, resp_gender, resp_edu, etc.)
- **Gatekeeping**: NONE - universal section
- **Expected Respondents**: ALL (N=214)
- **Expected Missingness**: <5% (non-response only)

## Section 2: Residential History
- **Variables**: 5 variables (lifelonglocation, locationtime, previouslocation, etc.)
- **Gatekeeping**: NONE - universal section
- **Expected Respondents**: ALL (N=214)
- **Expected Missingness**: <10%

## Section 3: Migration Motivations - WHY LEFT
- **Variables**: 20 variables (moveaway-reasons/*)
- **Gatekeeping**: `lifelonglocation == 'no'` (only non-lifelong residents)
- **Display Logic**: "Only shown if moved to current location"
- **Expected Respondents**: ~100 households (46% of total)
- **Expected Missingness**: ~54%
- **Conceptual Note**: Cannot ask "why did you leave" to someone who never left

## Section 4: Migration Motivations - WHY CHOSE HERE
- **Variables**: 15 variables (movetowards-reasons/*)
- **Gatekeeping**: `lifelonglocation == 'no'` (only non-lifelong residents)
- **Display Logic**: "Only shown if moved to current location"
- **Expected Respondents**: ~100 households (46% of total)
- **Expected Missingness**: ~54%
- **Conceptual Note**: Cannot ask "why did you choose here" to someone born here

## Section 5: Location Choice Factors ⚠️ CRITICAL SECTION
- **Variables**: 10 perception variables (bridge_city, waterdistance, safe_reputation, flooding, infrastructure, foodenvironment, schools, medical, religion, leisure)
- **Gatekeeping**: `lifelonglocation == 'no'` (only non-lifelong residents)
- **Display Logic**: "When you chose to move here, how important were the following factors?"
- **Question Type**: Likert scale -2 to +2 (Very unimportant to Very important)
- **Expected Respondents**: ~100 households (46% of total)
- **Expected Missingness**: ~54%
- **Conceptual Note**: Location choice factors only meaningful for households who MADE a location choice
- **Impact**: High structural missingness - NOT random, NOT fixable with imputation

## Section 6: Neighborhood Satisfaction
- **Variables**: 6 variables (clean, safe, floods, reputation, foodenvironment_002, happy)
- **Gatekeeping**: NONE - universal section
- **Expected Respondents**: ALL (N=214)
- **Expected Missingness**: <10%
- **Conceptual Note**: Different from Section 5 - this asks about CURRENT experience, not choice motivations

## Section 7: Urban Farming Activities
- **Variables**: 40 variables (farms, farmlandtype, farmsize, etc.)
- **Gatekeeping**: `farms == 'yes'` (only farming households)
- **Expected Respondents**: ~40 households (19% of total)
- **Expected Missingness**: ~81%

## Section 8: Household Vending Activities
- **Variables**: 30 variables (hh_vendor, vendortype, foodgroups sold, etc.)
- **Gatekeeping**: `hh_vendor == 'yes'` (only vendor households)
- **Expected Respondents**: ~35 households (16% of total)
- **Expected Missingness**: ~84%

## Section 9: Typhoon Yagi Preparation
- **Variables**: 10 variables (typhoon_prepare/*)
- **Gatekeeping**: UNKNOWN - need to investigate
- **Expected Respondents**: ~105 households (49% of total)
- **Expected Missingness**: ~51%
- **Note**: May be split by survey wave (before/after typhoon)

## Section 10: Typhoon Yagi Coping
- **Variables**: 11 variables (typhoon_cope/*)
- **Gatekeeping**: UNKNOWN - need to investigate
- **Expected Respondents**: ~141 households (66% of total)
- **Expected Missingness**: ~34%
- **Note**: May be conditional on typhoon impact

## Section 11: Food Security (FIES)
- **Variables**: 8 variables (worried, healthy, fewfoods, etc.)
- **Gatekeeping**: NONE - universal section
- **Expected Respondents**: ALL (N=214)
- **Expected Missingness**: <10%

## Section 12: Dietary Intake (24hr Recall)
- **Variables**: 16 food group variables (foodgroups_001/*)
- **Gatekeeping**: NONE - universal section
- **Expected Respondents**: ALL (N=214)
- **Expected Missingness**: <5% (core outcome measure)

## Section 13: Food Outlet Patronage
- **Variables**: 40 variables (8 outlet types × 5 questions each)
- **Gatekeeping**: NONE - universal section
- **Expected Respondents**: ALL (N=214)
- **Expected Missingness**: 10-30% (legitimate zeros for non-patronage)
```

**Step 3B: Create Gatekeeping Question Index**

```markdown
# Gatekeeping Questions

| Question | Variable | Values | Triggers Section(s) | N Expected |
|----------|----------|--------|---------------------|------------|
| "Have you lived here all your life?" | `lifelonglocation` | yes/no | Sections 3, 4, 5 (if no) | ~100 (46%) |
| "Does your household farm?" | `farms` | yes/no | Section 7 (if yes) | ~40 (19%) |
| "Does your household sell food?" | `hh_vendor` | yes/no | Section 8 (if yes) | ~35 (16%) |
| "Were you affected by Typhoon Yagi?" | ??? | ??? | Sections 9, 10 | ??? |
```

**Step 3C: Verify Skip Logic in Raw Data**

```python
# MANDATORY VERIFICATION SCRIPT
import pandas as pd

df = pd.read_csv('household_merged.csv')

# For each conditional section, verify skip logic worked
print("SECTION 5: Location Choice Factors - Skip Logic Verification")
print("=" * 80)

# Expected: lifelong=yes should have ALL Section 5 variables missing
section5_vars = ['bridge_city', 'waterdistance', 'safe_reputation', 'flooding',
                 'infrastructure', 'foodenvironment', 'schools', 'medical',
                 'religion', 'leisure']

lifelong_yes = df['lifelonglocation'] == 'yes'
lifelong_no = df['lifelonglocation'] == 'no'

print(f"Lifelong residents (yes): {lifelong_yes.sum()}")
print(f"Moved residents (no): {lifelong_no.sum()}")

# Check if skip logic was enforced
for var in section5_vars:
    lifelong_but_answered = (lifelong_yes & df[var].notna()).sum()
    moved_and_answered = (lifelong_no & df[var].notna()).sum()

    print(f"\n{var}:")
    print(f"  Lifelong residents who answered: {lifelong_but_answered}")
    print(f"  Moved residents who answered: {moved_and_answered}")

    if lifelong_but_answered > 0:
        print(f"  ⚠️ WARNING: Skip logic NOT enforced perfectly")
    else:
        print(f"  ✅ Skip logic enforced correctly")
```

**Deliverable**: `00_SURVEY_SECTION_MAP.md` + verification script results

**GATE**: This deliverable is MANDATORY before proceeding. If skip logic verification fails, must understand why.

---

### Step 0.4: Subsample Definition

**Objective**: Define ALL analysis-relevant subsamples

**Process**:

```markdown
# Subsample Definitions

## Primary Analysis Samples

### Sample 1: All Households (Universal)
- **N**: 214 (100%)
- **Definition**: All respondents who completed survey
- **Applicable Sections**: Demographics, Satisfaction, FIES, Dietary Intake, Outlet Patronage
- **Use For**: Universal predictors (demographics, satisfaction, food security)

### Sample 2: Location Choosers (Movers)
- **N**: 99 (46.3%)
- **Definition**: `lifelonglocation == 'no'`
- **Applicable Sections**: All universal sections + Sections 3, 4, 5
- **Use For**: Location choice analysis, migration motivations
- **Excluded**: 66 lifelong residents + 49 with gatekeeping NaN

### Sample 3: Lifelong Residents
- **N**: 66 (30.8%)
- **Definition**: `lifelonglocation == 'yes'`
- **Applicable Sections**: All universal sections (NOT location choice)
- **Use For**: Comparison group, neighborhood effects analysis
- **Note**: Location choice variables CONCEPTUALLY MISSING for this group

### Sample 4: Urban Farmers
- **N**: ~40 (18.7%)
- **Definition**: `farms == 'yes'`
- **Applicable Sections**: All universal sections + Section 7
- **Use For**: Urban agriculture analysis

### Sample 5: Food Vendors
- **N**: ~35 (16.4%)
- **Definition**: `hh_vendor == 'yes'`
- **Applicable Sections**: All universal sections + Section 8
- **Use For**: Informal food economy analysis

### Sample 6: Typhoon-Affected (TBD)
- **N**: TBD
- **Definition**: TBD - need to investigate
- **Applicable Sections**: All universal sections + Sections 9, 10

## Sample Overlap Analysis

```
All Households (N=214)
├── Location Choosers (N=99)
│   ├── Farmers (N=?)
│   ├── Vendors (N=?)
│   └── Typhoon-Affected (N=?)
└── Lifelong Residents (N=66)
    ├── Farmers (N=?)
    ├── Vendors (N=?)
    └── Typhoon-Affected (N=?)
└── Gatekeeping NaN (N=49)
    ├── Farmers (N=?)
    ├── Vendors (N=?)
    └── Typhoon-Affected (N=?)
```

## Critical Analysis Implications

1. **Turner Framework Analysis**:
   - If using location choice variables (OP007, OP019) → ONLY Location Choosers sample (N=99)
   - If excluding location choice variables → All Households sample (N=214)

2. **Food Environment Analysis**:
   - Universal food environment variables → All Households (N=214)
   - Location-specific perceptions → Location Choosers (N=99)

3. **Mixed Analyses**:
   - If framework includes BOTH universal AND location-choice variables → Maximum N=99
   - Should NOT mix conceptually incompatible variables
```

**Deliverable**: `00_SUBSAMPLE_DEFINITIONS.md`

---

### Step 0.5: Expected Missingness Baseline

**Objective**: Calculate expected missingness for EVERY variable based on survey design

**Process**:

```python
# EXPECTED MISSINGNESS CALCULATOR
import pandas as pd

df = pd.read_csv('household_merged.csv')

# Load survey section map
section_map = {
    'Section 1: Demographics': {
        'variables': ['household_size', 'resp_gender', ...],
        'expected_respondents': 214,
        'expected_missing_pct': 5
    },
    'Section 5: Location Choice': {
        'variables': ['bridge_city', 'waterdistance', ...],
        'expected_respondents': 99,
        'expected_missing_pct': 54
    },
    # ... etc
}

# Calculate actual vs expected missingness
results = []
for section, info in section_map.items():
    for var in info['variables']:
        if var not in df.columns:
            continue

        actual_missing = df[var].isna().sum()
        actual_pct = (actual_missing / len(df)) * 100
        expected_pct = info['expected_missing_pct']

        # Flag if actual differs from expected by >10%
        flag = "⚠️ INVESTIGATE" if abs(actual_pct - expected_pct) > 10 else "✅ OK"

        results.append({
            'Section': section,
            'Variable': var,
            'Expected_Missing_%': expected_pct,
            'Actual_Missing_%': actual_pct,
            'Difference_%': actual_pct - expected_pct,
            'Flag': flag
        })

results_df = pd.DataFrame(results)
print(results_df[results_df['Flag'] == '⚠️ INVESTIGATE'])
```

**Deliverable**: `00_EXPECTED_VS_ACTUAL_MISSINGNESS.csv`

**RED FLAG**: Any variable with >10% difference between expected and actual missingness MUST be investigated before proceeding

---

### Step 0.6: Phase 0 Quality Gate ⛔

**Cannot proceed to Phase 1 until ALL criteria met**:

- [x] Raw data inventory complete
- [x] Survey documentation reviewed
- [x] ALL survey sections mapped
- [x] ALL gatekeeping questions identified
- [x] Skip logic verified in raw data
- [x] ALL subsamples defined with N counts
- [x] Expected missingness calculated for ALL variables
- [x] No unexpected missingness flags (or all investigated)
- [x] Survey structure map reviewed by domain expert
- [x] Deliverables: 6 documents created

**Phase 0 Sign-Off**: `00_PHASE_0_COMPLETION_CHECKLIST.md`

---

## 📋 PHASE 1: VARIABLE CONSTRUCTION WITH SURVEY CONTEXT

**GATE**: Phase 0 complete ✅

### Step 1.1: Operationalization with Subsample Awareness

**Objective**: Map theoretical constructs to variables WITH subsample applicability

**Template**:

```markdown
# Operationalization Table - Turner Framework

## External Domain

| Turner Construct | OP Variable | Source Variable(s) | Survey Section | Applicable Subsample | Expected Missing % | Conceptual Definition |
|------------------|-------------|-------------------|----------------|---------------------|-------------------|----------------------|
| **Vendor Quality - Infrastructure** | OP007_infrastructure | `infrastructure` | Section 5: Location Choice | **Location Choosers ONLY (N=99)** | **54%** | Importance of infrastructure quality in **location choice decision** (Likert -2 to +2) |
| **Vendor Quality - Cleanliness** | OP004_cleanliness | `clean` | Section 6: Satisfaction | **All Households (N=214)** | 10% | Current neighborhood cleanliness perception (Likert -2 to +2) |

## Personal Domain

| Turner Construct | OP Variable | Source Variable(s) | Survey Section | Applicable Subsample | Expected Missing % | Conceptual Definition |
|------------------|-------------|-------------------|----------------|---------------------|-------------------|----------------------|
| **Convenience - Water Access** | OP019_water_distance | `waterdistance` | Section 5: Location Choice | **Location Choosers ONLY (N=99)** | **54%** | Importance of water proximity in **location choice decision** (Likert -2 to +2) |
| **Convenience - Water Source** | OP018_water_source | `watersource` | Section 6: Universal | **All Households (N=214)** | 10% | Current indoor water access (yes/no) |

## CRITICAL NOTES

### OP007 and OP019 Applicability
- ⚠️ These variables are ONLY applicable to Location Choosers (N=99)
- ⚠️ They measure importance of factors in PAST location choice decision
- ⚠️ They are CONCEPTUALLY MISSING for lifelong residents (never made choice)
- ⚠️ Cannot be used in analyses including lifelong residents without creating nonsensical data

### OP004 vs OP007 Conceptual Difference
- OP004 (`clean`): CURRENT neighborhood cleanliness → Universal variable
- OP007 (`infrastructure`): IMPORTANCE in PAST choice → Location choice variable
- These are DIFFERENT constructs despite both being perceptions

### Analysis Implications
- **Full Sample Analysis (N=214)**: Can ONLY use OP004, OP018, etc. (universal variables)
- **Location Choosers Analysis (N=99)**: Can use ALL variables including OP007, OP019
- **Mixed Models**: CANNOT mix location choice and universal variables without subsample restriction
```

**Deliverable**: `01_OPERATIONALIZATION_WITH_SUBSAMPLE_CONTEXT.md`

**GATE**: Every OP variable must have subsample applicability documented

---

### Step 1.2: Variable Construction Script with Built-in Validation

**Objective**: Create variables with automatic quality checks

**Template**:

```python
# phase_1_variable_construction_ROBUST.py
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def construct_op_variable(df, op_name, source_vars, survey_section,
                          applicable_subsample, expected_missing_pct,
                          construction_logic=None):
    """
    Construct OP variable with automatic validation

    Parameters:
    -----------
    df : DataFrame
    op_name : str (e.g., 'OP007_infrastructure')
    source_vars : list of str (source column names)
    survey_section : str (e.g., 'Section 5: Location Choice')
    applicable_subsample : str (e.g., 'Location Choosers (N=99)')
    expected_missing_pct : float (e.g., 54.0)
    construction_logic : function (optional, for derived variables)

    Returns:
    --------
    DataFrame with new OP variable + validation report
    """

    logger.info(f"=" * 80)
    logger.info(f"Constructing {op_name}")
    logger.info(f"=" * 80)

    # Check source variables exist
    for source_var in source_vars:
        if source_var not in df.columns:
            logger.error(f"❌ Source variable '{source_var}' not found in dataset!")
            logger.error(f"   Available columns: {df.columns.tolist()[:20]}...")
            raise ValueError(f"Source variable {source_var} not found")

    # Apply construction logic
    if construction_logic is None:
        # Simple direct mapping
        if len(source_vars) == 1:
            df[op_name] = df[source_vars[0]]
            logger.info(f"✅ Direct mapping: {op_name} ← {source_vars[0]}")
        else:
            raise ValueError("Multiple source vars require construction_logic function")
    else:
        df[op_name] = construction_logic(df, source_vars)
        logger.info(f"✅ Applied construction logic to create {op_name}")

    # VALIDATION CHECKS
    logger.info(f"\n📊 VALIDATION CHECKS:")
    logger.info(f"-" * 80)

    # 1. Check missing percentage
    actual_missing = df[op_name].isna().sum()
    actual_missing_pct = (actual_missing / len(df)) * 100
    missing_diff = abs(actual_missing_pct - expected_missing_pct)

    logger.info(f"1. Missingness Check:")
    logger.info(f"   Expected: {expected_missing_pct:.1f}%")
    logger.info(f"   Actual:   {actual_missing_pct:.1f}%")
    logger.info(f"   Diff:     {missing_diff:.1f}%")

    if missing_diff > 10:
        logger.warning(f"   ⚠️ WARNING: Missingness differs from expected by {missing_diff:.1f}%")
        logger.warning(f"   Survey Section: {survey_section}")
        logger.warning(f"   Applicable Subsample: {applicable_subsample}")
        logger.warning(f"   → INVESTIGATE before proceeding!")
    else:
        logger.info(f"   ✅ Missingness within expected range")

    # 2. Check value range (if numeric)
    if df[op_name].dtype in ['float64', 'int64']:
        logger.info(f"\n2. Value Range Check:")
        logger.info(f"   Min: {df[op_name].min()}")
        logger.info(f"   Max: {df[op_name].max()}")
        logger.info(f"   Unique values: {sorted(df[op_name].dropna().unique())}")

    # 3. Check sample size for applicable subsample
    valid_n = df[op_name].notna().sum()
    logger.info(f"\n3. Sample Size Check:")
    logger.info(f"   Valid N: {valid_n}")
    logger.info(f"   Applicable Subsample: {applicable_subsample}")

    # 4. Document metadata
    metadata = {
        'op_variable': op_name,
        'source_variables': source_vars,
        'survey_section': survey_section,
        'applicable_subsample': applicable_subsample,
        'expected_missing_pct': expected_missing_pct,
        'actual_missing_pct': actual_missing_pct,
        'valid_n': valid_n,
        'construction_date': pd.Timestamp.now()
    }

    logger.info(f"\n✅ {op_name} construction complete\n")

    return df, metadata


# EXAMPLE USAGE

# Load data
df = pd.read_csv('household_merged.csv')

# Store metadata for all OP variables
op_metadata = []

# OP007: Infrastructure (Location Choice Variable)
df, meta = construct_op_variable(
    df=df,
    op_name='OP007_infrastructure',
    source_vars=['infrastructure'],
    survey_section='Section 5: Location Choice Factors',
    applicable_subsample='Location Choosers ONLY (lifelonglocation == no)',
    expected_missing_pct=54.0,
    construction_logic=None  # Direct mapping
)
op_metadata.append(meta)

# OP004: Cleanliness (Universal Variable)
df, meta = construct_op_variable(
    df=df,
    op_name='OP004_cleanliness',
    source_vars=['clean'],
    survey_section='Section 6: Neighborhood Satisfaction',
    applicable_subsample='All Households',
    expected_missing_pct=10.0,
    construction_logic=None
)
op_metadata.append(meta)

# ... repeat for all OP variables ...

# Save metadata
meta_df = pd.DataFrame(op_metadata)
meta_df.to_csv('01_OP_VARIABLE_METADATA.csv', index=False)
logger.info(f"✅ Saved metadata for {len(op_metadata)} OP variables")
```

**Deliverable**:
- Constructed dataset with OP variables
- `01_OP_VARIABLE_METADATA.csv` with full documentation
- Construction log showing all validation checks

**GATE**: All validation checks must pass (or warnings investigated) before proceeding

---

### Step 1.3: Create Comprehensive Data Dictionary with Survey Context

**Objective**: Document every variable with subsample applicability

**Template**:

```markdown
# Comprehensive Data Dictionary - Survey Context Aware

## Variable: OP007_infrastructure

### Basic Information
- **OP ID**: OP007
- **Variable Name**: OP007_infrastructure
- **Source Variable**: `infrastructure` (raw survey column)
- **Data Type**: Numeric (Likert scale)
- **Unit**: Scale from -2 (Very unimportant) to +2 (Very important)

### Survey Context ⭐ CRITICAL
- **Survey Section**: Section 5: Location Choice Factors
- **Section Description**: Factors considered when choosing current residential location
- **Question Text**: "When you chose to move here, how important was the general infrastructure (electricity, gas, asphalted roads, etc.)?"
- **Question Type**: Likert scale perception of importance in PAST decision
- **Gatekeeping Question**: "Have you lived in this house all your life?" (`lifelonglocation`)
- **Display Logic**: Only shown if `lifelonglocation == 'no'` (non-lifelong residents)

### Applicability Scope ⚠️
- **Applicable To**: Location Choosers ONLY (households who moved to current location)
- **Applicable N**: 99 households (46.3% of total)
- **NOT Applicable To**: Lifelong residents (N=66, 30.8%) + Gatekeeping NaN (N=49, 22.9%)
- **Conceptual Reason**: Cannot assess importance of factor in choice that was never made
- **Missingness Type**: STRUCTURAL (by design), not RANDOM

### Missingness Details
- **Expected Missing**: 115 households (53.7%)
  - 66 lifelong residents (skip logic)
  - 49 gatekeeping NaN (section not shown)
- **Actual Missing**: 115 households (53.7%) ✅ Matches expected
- **Imputation Feasibility**: ❌ NOT APPROPRIATE (structural missingness)

### Statistical Properties
- **Valid N**: 99
- **Mean**: 0.13 (SD=0.9)
- **Range**: -1.0 to 1.0 (subset of full Likert scale)
- **Distribution**: -1 (N=34), 0 (N=18), 1 (N=47)

### Turner Framework Mapping
- **Domain**: External Domain
- **Construct**: Vendor/Product Quality - Infrastructure
- **Measurement**: Perceived importance in location decision

### Analysis Implications ⚠️
- **Can be used in**: Location Choosers subsample analyses (N=99)
- **CANNOT be used in**: Full sample analyses (N=214) without creating nonsensical data
- **Regression models**: If included, automatically restricts sample to N=99
- **Interpretation**: Reflects PAST decision importance, not CURRENT satisfaction

### Related Variables
- **OP004_cleanliness**: CURRENT neighborhood cleanliness (universal variable)
  - Different construct: current satisfaction vs. past choice factor
- **All Section 5 variables**: Same skip logic, same applicability (N=99)
  - `bridge_city`, `waterdistance`, `flooding`, etc.

### Creation Details
- **Phase Created**: 1
- **Construction Method**: Direct mapping from source variable
- **Validation Status**: ✅ Passed all checks (expected missingness matched)
- **Last Updated**: 2025-11-23

---

## Variable: OP004_cleanliness

### Basic Information
[Same structure as above]

### Survey Context ⭐ CRITICAL
- **Survey Section**: Section 6: Neighborhood Satisfaction
- **Section Description**: Current perceptions of neighborhood quality
- **Question Text**: "How would you rate the cleanliness of this neighborhood?"
- **Question Type**: Likert scale perception of CURRENT state
- **Gatekeeping Question**: NONE - universal question
- **Display Logic**: NONE - shown to all respondents

### Applicability Scope ⭐
- **Applicable To**: ALL HOUSEHOLDS
- **Applicable N**: 214 households (100% minus non-response)
- **NOT Applicable To**: None (universal)
- **Conceptual Reason**: All households can assess current cleanliness
- **Missingness Type**: RANDOM (non-response only)

### Missingness Details
- **Expected Missing**: <10% (random non-response)
- **Actual Missing**: 52 households (24.3%) ⚠️ Higher than expected - investigate
- **Imputation Feasibility**: ✅ Feasible if <40% missing

[Continue for all variables...]
```

**Deliverable**: `01_DATA_DICTIONARY_SURVEY_CONTEXT_AWARE.md`

**GATE**: Every OP variable must have complete survey context documentation

---

## 📋 PHASE 2: ANALYSIS PLANNING WITH SUBSAMPLE AWARENESS

**GATE**: Phase 1 complete ✅

### Step 2.1: Sample Size Planning by Model

**Objective**: Pre-calculate expected N for every planned model BEFORE running analyses

**Template**:

```markdown
# Sample Size Planning - Turner Framework Models

## Model 1: Full Turner Framework (16 Predictors)

### Predictors Inventory
| Predictor | OP Variable | Applicable Subsample | Expected N |
|-----------|-------------|---------------------|------------|
| Infrastructure | OP007_infrastructure | **Location Choosers** | **99** |
| Water Distance | OP019_water_distance | **Location Choosers** | **99** |
| Cleanliness | OP004_cleanliness | All Households | 214 |
| Safety | OP005_neighborhood_safety | All Households | 214 |
| ... | ... | ... | ... |

### Sample Size Calculation
- **Most Restrictive Predictor**: OP007, OP019 (Location Choosers, N=99)
- **Expected Final N after Listwise Deletion**:
  - Best case: 99 (if all Location Choosers have complete data)
  - Realistic: ~64 (accounting for other missingness)
- **Predictor-to-Case Ratio**: 16:64 = 1:4 ⚠️ SEVERELY UNDERPOWERED
- **Recommended Minimum**: 1:10 (160 cases needed for 16 predictors)

### ⚠️ RED FLAG ANALYSIS
- Sample size (64) is 60% BELOW recommended minimum (160)
- Statistical power: Severely insufficient
- Risk of Type II error: Very high
- Risk of overfitting: Very high

### RECOMMENDATIONS
1. **DO NOT proceed with this model configuration**
2. **Options**:
   - A: Reduce predictors to ≤6 (to achieve 1:10 ratio with N=64)
   - B: Exclude location choice variables (increase N to ~150)
   - C: Run separate models by subsample
   - D: Frame as exploratory/hypothesis-generating only

---

## Model 2: Core Turner Framework (Excluding Location Choice)

### Predictors Inventory
| Predictor | OP Variable | Applicable Subsample | Expected N |
|-----------|-------------|---------------------|------------|
| Cleanliness | OP004_cleanliness | All Households | 214 |
| Safety | OP005_neighborhood_safety | All Households | 214 |
| Price Motive | OP003_price_motive | All Households | 214 |
| ... | ... | ... | ... |

**Excluded from Full Framework**:
- ❌ OP007_infrastructure (location choice variable)
- ❌ OP019_water_distance (location choice variable)

### Sample Size Calculation
- **Most Restrictive Predictor**: OP012_monthly_expenditure (N=142, 66.4%)
- **Expected Final N after Listwise Deletion**: ~102
- **Number of Predictors**: 14
- **Predictor-to-Case Ratio**: 14:102 = 1:7.3 ⚠️ STILL UNDERPOWERED
- **Recommended Minimum**: 1:10 (140 cases needed)

### ⚠️ FLAG ANALYSIS
- Sample size (102) is 27% below recommended (140)
- Statistical power: Moderate but not ideal
- Acceptable for exploratory analysis
- Should report with appropriate caveats

### RECOMMENDATIONS
1. **ACCEPTABLE as primary analysis** with limitations acknowledged
2. **Sensitivity analyses**: Compare with imputation approach

---

## Model 3: Location Choosers Framework (Subsample Analysis)

### Predictors Inventory
- ALL variables (including OP007, OP019) conceptually appropriate
- Sample: Location Choosers ONLY (N=99)

### Sample Size Calculation
- **Maximum Possible N**: 99 (Location Choosers)
- **Expected Final N after Listwise Deletion**: ~64
- **Number of Predictors**: 16
- **Predictor-to-Case Ratio**: 16:64 = 1:4 ⚠️ SEVERELY UNDERPOWERED

### ⚠️ RED FLAG ANALYSIS
- Same power issues as Model 1
- BUT conceptually appropriate subsample

### RECOMMENDATIONS
1. **Conceptually appropriate** (all variables apply to this subsample)
2. **Statistically underpowered** (would need N=160)
3. **Frame as**: Exploratory subsample analysis
4. **Reduce predictors** to most theoretically important (aim for 6-8)

---

## Decision Matrix: Which Model to Run?

| Model | N | Predictors | Ratio | Power | Conceptual Fit | Recommendation |
|-------|---|------------|-------|-------|----------------|----------------|
| Full Framework (All) | 64 | 16 | 1:4 | ❌ Very Low | ⚠️ Mixed | ❌ Do not run as primary |
| Core Framework (No location) | 102 | 14 | 1:7.3 | ⚠️ Moderate | ✅ Good | ✅ **PRIMARY ANALYSIS** |
| Location Choosers (Subsample) | 64 | 16 | 1:4 | ❌ Very Low | ✅ Excellent | ⚠️ Exploratory only |

## Final Recommendation

**PRIMARY ANALYSIS**: Model 2 (Core Framework, N=102)
- Exclude OP007 and OP019 (location choice variables)
- Use all universal variables
- Report with power limitations acknowledged

**SENSITIVITY ANALYSIS**: Model 2 + Multiple Imputation
- Impute variables with <50% missing (OP012, OP009, OP016)
- Expected N: ~150
- Compare results to primary analysis

**SUPPLEMENTARY ANALYSIS**: Model 3 (Location Choosers, reduced predictors)
- Reduce to 6-8 most important predictors
- Frame as exploratory subsample analysis
- Report in appendix

**DO NOT RUN**: Model 1 (Full Framework, N=64, 16 predictors)
- Severely underpowered
- Mixes conceptually incompatible variables
- No scientific value
```

**Deliverable**: `02_SAMPLE_SIZE_PLANNING_ALL_MODELS.md`

**GATE**: Must have sample size projections for ALL planned models before running ANY regression

---

### Step 2.2: Pre-Registration of Analysis Decisions

**Objective**: Document ALL analysis decisions BEFORE seeing results

**Template**:

```markdown
# Analysis Plan Pre-Registration

## Research Question
What household and environmental factors predict dietary diversity (HDDS) among urban Vietnamese households?

## Theoretical Framework
Turner Framework for food environment (External + Personal domains)

## Analysis Strategy

### Primary Analysis
- **Model**: Core Turner Framework (excluding location choice variables)
- **Predictors**: 14 universal variables (OP003, OP004, OP005, OP006, OP009, OP010, OP012, OP013, OP016, OP017, OP018, OP021, OP022, OP023)
- **Outcome**: OP029_HDDS
- **Sample**: All Households with complete data (expected N=102)
- **Method**: OLS regression
- **Missing Data**: Listwise deletion (justified because structural missingness for excluded variables)

### Sensitivity Analyses (Pre-Specified)
1. **Multiple Imputation**: Add MICE for OP009, OP012, OP016 (all <45% missing)
   - Expected N: ~150
   - Compare coefficients to primary analysis

2. **Robust Standard Errors**: Check if heteroscedasticity affects inference

3. **Domain-Specific Models**: Run separate models for External vs Personal domains

### Supplementary Analyses (Pre-Specified)
1. **Location Choosers Subsample**: Reduced predictor model (6 predictors) with N=64
   - Exploratory only
   - Report in appendix

### What Will NOT Be Done
- ❌ Will NOT run full 16-predictor model with N=64 (underpowered, conceptually mixed)
- ❌ Will NOT impute OP007, OP019 (structural missingness >50%)
- ❌ Will NOT combine lifelong and location choosers for location choice variables

### Success Criteria
- Primary model N ≥ 100
- Predictor-to-case ratio ≥ 1:7
- Sensitivity analyses confirm primary findings

### Contingency Plans
If primary model N < 100:
1. Investigate why (unexpected missingness in universal variables)
2. Consider excluding problematic universal variables
3. Document in limitations

## Statistical Power
- Current N=102, 14 predictors → Power to detect medium effects (f² = 0.15) ≈ 0.70
- Acknowledge limited power in discussion

## Reporting Standards
- Report ALL models run (no selective reporting)
- Report exact p-values (not p<.05)
- Report confidence intervals for all coefficients
- Transparent about multiple comparisons

---
**Date**: [Before any analysis run]
**Analyst**: [Name]
**Reviewed By**: [Advisor/Committee]
```

**Deliverable**: `02_ANALYSIS_PLAN_PREREGISTRATION.md`

**GATE**: Must be approved by advisor BEFORE running analyses

---

## 📋 PHASE 3: ANALYSIS EXECUTION WITH VALIDATION

**GATE**: Phase 2 complete ✅ + Pre-registration approved

### Step 3.1: Verify Actual Sample Sizes Match Projections

**Before running ANY regression**:

```python
# SAMPLE SIZE VERIFICATION
import pandas as pd

df = pd.read_csv('analysis_ready_dataset.csv')

# Define predictor sets
primary_predictors = ['OP003_price_motive', 'OP004_cleanliness', ...]  # 14 predictors
outcome = 'OP029_HDDS'

# Calculate complete-case sample
complete_case = df[primary_predictors + [outcome]].dropna()

print("=" * 80)
print("SAMPLE SIZE VERIFICATION")
print("=" * 80)
print(f"Total N: {len(df)}")
print(f"Complete-case N: {len(complete_case)}")
print(f"Expected N: 102")
print(f"Difference: {len(complete_case) - 102}")

if abs(len(complete_case) - 102) > 5:
    print("⚠️ WARNING: Actual N differs from expected by >5 households")
    print("STOP AND INVESTIGATE before proceeding")
else:
    print("✅ Actual N matches expected")

# Show missingness breakdown
print("\nMissingness by variable:")
for var in primary_predictors + [outcome]:
    missing = df[var].isna().sum()
    print(f"  {var:30s}: {missing:3d} missing ({missing/len(df)*100:5.1f}%)")
```

**GATE**: Actual N must be within ±5 of projected N, or must investigate why

---

### Step 3.2: Model Diagnostics BEFORE Interpretation

**Run ALL diagnostics before looking at coefficients**:

```python
# MODEL DIAGNOSTICS (run BEFORE interpreting results)
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Fit model
X = complete_case[primary_predictors]
y = complete_case[outcome]
X_with_const = sm.add_constant(X)
model = sm.OLS(y, X_with_const).fit()

print("=" * 80)
print("MODEL DIAGNOSTICS")
print("=" * 80)

# 1. Sample size check
print(f"\n1. SAMPLE SIZE:")
print(f"   N = {len(complete_case)}")
print(f"   Predictors = {len(primary_predictors)}")
print(f"   Ratio = 1:{len(complete_case)/len(primary_predictors):.1f}")

if len(complete_case) / len(primary_predictors) < 7:
    print("   ⚠️ WARNING: Below recommended 1:10 ratio")
else:
    print("   ✅ Acceptable ratio")

# 2. Multicollinearity
print(f"\n2. MULTICOLLINEARITY (VIF):")
vif_data = pd.DataFrame()
vif_data["Variable"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]
print(vif_data)
if (vif_data["VIF"] > 10).any():
    print("   ⚠️ WARNING: VIF > 10 detected (multicollinearity)")
else:
    print("   ✅ No problematic multicollinearity")

# 3. Residual diagnostics
print(f"\n3. RESIDUAL DIAGNOSTICS:")
residuals = model.resid
print(f"   Shapiro-Wilk test: p = {sm.stats.diagnostic.normal_ad(residuals)[1]:.3f}")
print(f"   Breusch-Pagan test: p = {sm.stats.diagnostic.het_breuschpagan(residuals, X_with_const)[1]:.3f}")

# 4. Influential cases
print(f"\n4. INFLUENTIAL CASES:")
influence = model.get_influence()
cooks_d = influence.cooks_distance[0]
print(f"   Cases with Cook's D > 1: {(cooks_d > 1).sum()}")
print(f"   Cases with Cook's D > 0.5: {(cooks_d > 0.5).sum()}")

# GATE: If any critical diagnostic fails, must address before proceeding
print("\n" + "=" * 80)
print("DIAGNOSTIC SUMMARY:")
diagnostics_passed = True

if len(complete_case) / len(primary_predictors) < 5:
    print("❌ FAIL: Severely underpowered (ratio < 1:5)")
    diagnostics_passed = False
elif len(complete_case) / len(primary_predictors) < 7:
    print("⚠️ CAUTION: Underpowered (ratio < 1:7)")

if (vif_data["VIF"] > 10).any():
    print("❌ FAIL: Severe multicollinearity (VIF > 10)")
    diagnostics_passed = False

if (cooks_d > 1).sum() > 0:
    print("⚠️ CAUTION: Influential cases detected (Cook's D > 1)")

if diagnostics_passed:
    print("✅ All critical diagnostics passed - safe to interpret results")
else:
    print("⚠️ Review diagnostic failures before interpreting results")
```

**GATE**: Critical diagnostic failures must be addressed before interpretation

---

## 📋 PHASE 4: LIMITATIONS & INTEGRATION

### Step 4.1: Limitations Documentation with Survey Context

**Template**:

```markdown
# Study Limitations - Survey Context Aware

## Limitation 1: Sample Size Reduction from Structural Missingness

### Description
The Turner Framework model sample was reduced to N=102 (47.7% of total N=214) due to exclusion of location choice variables (OP007_infrastructure, OP019_water_distance).

### Root Cause
These variables originate from the "Location Choice Factors" survey section, which was intentionally NOT administered to lifelong residents (N=66, 30.8%) because location choice factors are conceptually irrelevant for households who never made a location choice decision. Additionally, 49 households (22.9%) did not answer the gatekeeping question determining section eligibility.

### Why This Is NOT a Data Processing Error
1. **Survey Design**: The skip logic is intentional and appropriate - cannot ask "how important was infrastructure in your location choice" to someone born in the location
2. **Conceptual Validity**: Including these variables would require imputing nonsensical data for lifelong residents
3. **Structural Missingness**: Data was never collected by design, not lost due to non-response

### Methodological Decision
We excluded OP007 and OP019 from the core Turner Framework model rather than:
- Restricting analysis to location choosers only (N=64 after listwise deletion)
- Imputing structurally missing data (methodologically inappropriate)

### Impact on Findings
- Turner Framework assessment limited to non-location-specific variables
- External Domain reduced from 5 to 3 variables (OP004, OP005, OP006)
- Statistical power moderate (14 predictors, N=102, ratio 1:7.3)

### Sensitivity Analysis
Subsample analysis (Location Choosers only, N=64) produced consistent findings despite reduced power (see Appendix C).

---

## Limitation 2: Statistical Power

### Description
With N=102 and 14 predictors (ratio 1:7.3), statistical power is moderate but below the ideal 1:10-1:15 ratio.

### Impact
- Power to detect medium effects (f² = 0.15) approximately 70%
- Risk of Type II error (false negatives) elevated
- Confidence intervals wider than ideal

### Mitigation
- Conducted sensitivity analysis with multiple imputation (N=150) showing consistent results
- Framed as exploratory analysis generating hypotheses for future research
- Report exact p-values and confidence intervals (not binary significance)

---

## Limitation 3: Survey Design - Subsample Heterogeneity

### Description
Survey includes multiple conditional sections creating analysis-relevant subsamples:
- Location Choosers vs Lifelong Residents (46% vs 31%)
- Farmers vs Non-farmers (19% vs 81%)
- Vendors vs Non-vendors (16% vs 84%)

### Impact
- Not all variables applicable to all households
- Mixed samples in universal analyses
- Potential unmeasured heterogeneity

### Addressed By
- Explicit subsample documentation
- Variable selection based on universal applicability
- Sensitivity analyses by subsample where appropriate
```

---

## 🔐 QUALITY GATES SUMMARY

### Cannot Proceed to Next Phase Until:

**Phase 0 → Phase 1**:
- [x] All survey sections mapped
- [x] All gatekeeping questions identified
- [x] Skip logic verified
- [x] All subsamples defined
- [x] Expected missingness calculated
- [x] No unexplained missingness flags

**Phase 1 → Phase 2**:
- [x] All OP variables have survey context documented
- [x] All OP variables have subsample applicability defined
- [x] All validation checks passed
- [x] Metadata file created

**Phase 2 → Phase 3**:
- [x] Sample sizes projected for all models
- [x] Underpowered models identified
- [x] Analysis plan pre-registered
- [x] Advisor approval obtained

**Phase 3 → Phase 4**:
- [x] Actual N matches projected N (±5)
- [x] Model diagnostics passed
- [x] Sensitivity analyses completed

---

## 📚 DELIVERABLES CHECKLIST

### Phase 0: Survey Structure (6 documents)
1. `00_RAW_DATA_INVENTORY.md`
2. `00_SURVEY_DOCUMENTATION_INDEX.md`
3. `00_SURVEY_SECTION_MAP.md` ⭐ CRITICAL
4. `00_SUBSAMPLE_DEFINITIONS.md` ⭐ CRITICAL
5. `00_EXPECTED_VS_ACTUAL_MISSINGNESS.csv`
6. `00_PHASE_0_COMPLETION_CHECKLIST.md`

### Phase 1: Variable Construction (3 documents + dataset)
7. `01_OPERATIONALIZATION_WITH_SUBSAMPLE_CONTEXT.md` ⭐ CRITICAL
8. `01_OP_VARIABLE_METADATA.csv`
9. `01_DATA_DICTIONARY_SURVEY_CONTEXT_AWARE.md` ⭐ CRITICAL
10. `01_analysis_ready_dataset.csv`

### Phase 2: Analysis Planning (2 documents)
11. `02_SAMPLE_SIZE_PLANNING_ALL_MODELS.md` ⭐ CRITICAL
12. `02_ANALYSIS_PLAN_PREREGISTRATION.md`

### Phase 3: Analysis Execution (results)
13. `03_MODEL_DIAGNOSTICS_REPORT.md`
14. `03_PRIMARY_ANALYSIS_RESULTS.md`
15. `03_SENSITIVITY_ANALYSES_RESULTS.md`

### Phase 4: Integration (1 document)
16. `04_LIMITATIONS_SURVEY_CONTEXT_AWARE.md` ⭐ CRITICAL

**Total**: 16 core deliverables (compared to original workflow: ~5)

---

## 🚨 RED FLAGS THAT TRIGGER IMMEDIATE INVESTIGATION

### Automatic Investigation Required If:

1. **Missingness > 10% different from expected**
   - Action: Review survey section map, check skip logic, verify subsample definitions

2. **Identical missingness patterns** (within 1%)
   - Action: Investigate if variables are from same survey section

3. **Sample size < projected by >5 households**
   - Action: Review which variables causing unexpected loss

4. **VIF > 10** (severe multicollinearity)
   - Action: Check if variables are from same construct, consider exclusion

5. **Cook's D > 1** for >5% of cases
   - Action: Investigate influential cases, check data quality

6. **Predictor-to-case ratio < 1:5**
   - Action: STOP - reduce predictors or increase sample before proceeding

---

## 💡 KEY DIFFERENCES FROM ORIGINAL WORKFLOW

| Aspect | Original Workflow | Revised Workflow V2.0 |
|--------|------------------|----------------------|
| **Survey Section Analysis** | Acknowledged but not systematically mapped | MANDATORY Phase 0 deliverable with verification |
| **Subsample Documentation** | Ad-hoc | Formal definitions with N counts |
| **Variable Context** | Source column only | Full survey section, gatekeeping logic, applicability |
| **Sample Size Planning** | Post-hoc (after seeing N=64) | Pre-specified with red flags |
| **Missingness Expectations** | "High missingness noted" | Expected vs actual with automatic flags |
| **Quality Gates** | None (linear progression) | 4 mandatory gates blocking progression |
| **Documentation Density** | 5 core documents | 16 core documents |
| **Red Flag System** | Manual judgment | Automatic triggers with thresholds |
| **Cross-Phase Integration** | Weak | Metadata flows through all phases |

---

## 🎓 LEARNING OBJECTIVES FOR FUTURE RESEARCHERS

After completing this protocol, you will be able to:

1. **Map complex survey structures** with confidence
2. **Identify structural vs random missingness** automatically
3. **Define and document subsamples** systematically
4. **Plan analyses** based on sample size realities, not hopes
5. **Explain limitations** with survey context, not vague "data loss"
6. **Prevent systematic failures** through quality gates
7. **Create transparent, reproducible** analysis pipelines

---

## 📝 FINAL RECOMMENDATION

**For the Current WFL Analysis**:
1. Go back to Phase 0 and create the missing survey structure documentation
2. Verify ALL 25 OP variables against survey sections
3. Update data dictionary with survey context
4. Re-run sample size projections
5. Choose analysis strategy based on projections
6. Update thesis limitations with survey context

**For Future Research**:
- Use this protocol from Day 1
- Do not skip quality gates
- Document everything
- Investigate red flags immediately

---

**Protocol Version**: 2.0
**Date Created**: 2025-11-23
**Based On**: WFL Analysis systematic failure audit
**Status**: Ready for implementation
**Estimated Time**: Phase 0 alone: 2-3 days (but saves weeks of confusion later)

---

**Remember**:
> "Spending 3 days on Phase 0 survey structure analysis prevents spending 3 weeks troubleshooting mysterious sample size reductions in Phase 4."

The systematic failures were preventable. This protocol prevents them.
