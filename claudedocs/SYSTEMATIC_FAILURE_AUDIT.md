# SYSTEMATIC FAILURE AUDIT
## Data Processing and Survey Understanding Gaps

---

**Audit Date**: 2025-11-23
**Trigger**: User observation: "it seems like crucial data processing and deep understanding of surveys was missed at beginning, feels systemic"
**Status**: ✅ **AUDIT COMPLETE** - Multiple systemic failures identified

---

## 🚨 EXECUTIVE SUMMARY

### User is Absolutely Right

This investigation revealed **systemic failures** in the early data processing phases (Phase 0-1) that cascaded through all subsequent analyses. The issue isn't just missing one detail—it's a pattern of incomplete survey structure documentation that affected:

1. **Variable creation** (Phase 1)
2. **Missing data interpretation** (Phase 2-3)
3. **Sample size explanations** (Phase 4)
4. **Thesis limitation framing** (Phase 4)

---

## 📋 WHAT SHOULD HAVE HAPPENED (vs WHAT DID HAPPEN)

### Phase 0: Exploratory Data Analysis

| Should Have Happened | What Actually Happened | Evidence |
|---------------------|----------------------|----------|
| **Systematic survey section mapping** | ✅ Acknowledged skip logic exists | Phase 0 ACTUAL_OUTCOMES.md: "Conditional questions (skip logic) cause expected missingness" |
| **Document all conditional sections** | ❌ No systematic documentation | No survey section map found in any Phase 0-2 docs |
| **Identify gatekeeping questions** | ❌ Not documented | `lifelonglocation` as gatekeeping not identified until Phase 4 |
| **Map variables to survey sections** | ❌ Not done | Variables treated independently, not as section groups |
| **Create survey flow diagram** | ❌ Not created | No visual/structured representation of survey logic |
| **Document missingness patterns by section** | ⚠️ Partial | Noted high missingness, but didn't link to sections |

**Impact**: Variables were understood individually, not as part of coherent survey sections with shared skip logic.

---

### Phase 1: Variable Construction

| Should Have Happened | What Actually Happened | Evidence |
|---------------------|----------------------|----------|
| **Verify source variable survey context** | ❌ Not systematically done | OP007/OP019 created without understanding they're from "Location Choice" section |
| **Document which OP variables come from conditional sections** | ❌ Not documented | No warnings that OP007/OP019 would have high structural missingness |
| **Flag variables with >40% expected missingness** | ❌ Not flagged | OP007 (53.7% missing) and OP019 (53.7% missing) not identified as problematic |
| **Create OP variable → survey section mapping** | ❌ Not created | Data dictionary shows variables but not survey context |

**Impact**: OP variables included in analyses without understanding their survey context or applicability scope.

---

### Phase 2-3: Analysis

| Should Have Happened | What Actually Happened | Evidence |
|---------------------|----------------------|----------|
| **Check if listwise deletion is removing entire survey sections** | ❌ Not checked | Full Framework N=64 accepted without investigating WHY 70% lost |
| **Identify if missing data is structural vs random** | ❌ Not done until Phase 4 | Structural missingness only discovered during troubleshooting |
| **Consider subsample analyses** | ❌ Not considered | Could have run analyses separately for "location choosers" vs all |
| **Document which predictors apply to which subsamples** | ❌ Not documented | All predictors treated as universal |

**Impact**: Severe sample size reduction (N=64) accepted as unavoidable without exploring whether it was methodologically necessary.

---

### Phase 4: Limitations

| Should Have Happened | What Actually Happened | Evidence |
|---------------------|----------------------|----------|
| **Explain structural missingness mechanism** | ❌ Framed as "data loss" | Original language: "representing a 70.1% data loss" |
| **Justify inclusion of conditional section variables** | ❌ Not justified | No discussion of whether location choice variables should be in Turner Framework |
| **Propose alternative analysis strategies** | ❌ Not proposed | Only discovered during troubleshooting in Phase 4 |

**Impact**: Thesis limitations section would have misrepresented the nature of the missingness.

---

## 🔍 SURVEY STRUCTURE THAT WAS MISSED

### The 7 Major Conditional Survey Sections

Based on missingness cluster analysis, the survey has at least 7 distinct conditional sections that were NOT systematically documented:

| Section Name | Missingness % | N Variables | Gatekeeping Question | Applied To |
|--------------|---------------|-------------|---------------------|-----------|
| **1. Location Choice Factors** | **53.7%** | **49** | `lifelonglocation == 'no'` | **Only non-lifelong residents (99 households)** |
| **2. Typhoon Preparation** | 50.9% | 10 | Unknown (need to check) | ~105 households answered |
| **3. Typhoon Coping** | 34.1% | 11 | Unknown (need to check) | ~141 households answered |
| **4. Vendor/Food Selling** | 84.1% | 30 | `hh_vendor == 'yes'` | Only household vendors (~34 households) |
| **5. Urban Farming** | 81.3% | 40 | `farms == 'yes'` | Only farming households (~40 households) |
| **6. Land Access Uncertainty** | 93.0% | 15 | `accessuncertainty == 'yes'` | Only farmers with uncertain access (~15 households) |
| **7. Food Waste** | 81.8% | 10 | Unknown (need to check) | ~39 households answered |

**CRITICAL**: Only Section #1 (Location Choice Factors) was investigated. The other 6 sections were never systematically examined!

---

## 🎯 WHICH OP VARIABLES COME FROM CONDITIONAL SECTIONS?

### Location Choice Section (~54% missing)

✅ **IDENTIFIED**:
- **OP007_infrastructure** ← `infrastructure` (location choice factor)
- **OP019_water_distance** ← `waterdistance` (location choice factor perception, NOT actual distance)

❓ **NEED TO VERIFY** if these additional location perception variables are also OP variables:
- `bridge_city`
- `safe_reputation`
- `flooding`
- `foodenvironment`
- `schools`
- `medical`
- `religion`
- `leisure`

### Other Conditional Sections

❓ **NEED TO INVESTIGATE**: Do any other OP variables come from:
- Typhoon sections?
- Vendor section?
- Farming section?

---

## 📊 SPECIFIC FAILURES IN OP007 & OP019 CASE

### What We Now Know:

1. **Both are Likert perception scales** (-2 to +2)
2. **Both are from "Location Choice Factors" section**
3. **This section has 10 total variables**, all with identical 53.7% missingness
4. **Section is only shown to households who moved** (`lifelonglocation == 'no'`)
5. **Asking lifelong residents these questions makes no sense** (cannot assess importance of factors in a choice you never made)

### What Was Documented in Phase 1:

```python
# From phase_1_CORRECTED_variable_construction.py:
'OP007_infrastructure': 'infrastructure'
'OP019_water_distance': 'waterdistance'
```

**That's it.** No context about:
- Survey section membership
- Skip logic
- Expected missingness
- Applicability scope
- Conceptual meaning (location choice factors)

### What Should Have Been Documented:

```python
'OP007_infrastructure': {
    'source': 'infrastructure',
    'survey_section': 'Location Choice Factors',
    'gatekeeping_question': 'lifelonglocation',
    'applies_to': 'non-lifelong residents only',
    'expected_missingness': '~54% (lifelong residents + gatekeeping NaN)',
    'type': 'Likert scale (-2 to +2)',
    'conceptual_meaning': 'Importance of infrastructure quality in location choice decision',
    'note': 'NOT applicable to lifelong residents (never made location choice)'
}
```

---

## 🔴 SYSTEMATIC FAILURE PATTERNS

### Pattern 1: Documentation Incompleteness

**Symptom**: Acknowledged issue exists, but didn't follow through with systematic documentation

**Evidence**:
- Phase 0 ACTUAL_OUTCOMES.md: "Pattern analysis: Conditional questions (skip logic) cause expected missingness" ✅
- But NO survey section mapping document created ❌
- But NO OP variable survey context documentation ❌

**Why This Failed**: Recognized the issue conceptually but didn't operationalize it into usable documentation.

---

### Pattern 2: Individual Variable Focus vs Section-Level Understanding

**Symptom**: Variables treated as independent entities rather than members of survey sections

**Evidence**:
- OP007 and OP019 documented separately
- No recognition they're part of same 10-variable section
- No investigation of other variables in same section

**Why This Failed**: Missing the forest for the trees - focused on specific variables without understanding survey structure.

---

### Pattern 3: Acceptance Without Investigation

**Symptom**: High missingness accepted as "normal" without deep investigation

**Evidence**:
- Phase 2-3: N=64 for Full Framework accepted
- No investigation into WHY 70% sample loss occurred
- Only discovered root cause during Phase 4 troubleshooting

**Why This Failed**: Should have questioned severe sample loss earlier, not accepted it as unavoidable.

---

### Pattern 4: Missing Cross-Phase Integration

**Symptom**: Knowledge from one phase not systematically integrated into later phases

**Evidence**:
- Phase 0 knew about skip logic
- Phase 1 variable construction didn't use this knowledge
- Phase 2-3 analyses didn't account for it
- Phase 4 limitations framed it as "data loss"

**Why This Failed**: No mechanism to ensure early discoveries inform later work.

---

## 💡 ROOT CAUSES OF SYSTEMATIC FAILURE

### 1. No Formal Survey Structure Analysis Protocol

**Missing Process**:
- Step 1: Map all survey sections
- Step 2: Identify gatekeeping questions
- Step 3: Document skip logic flows
- Step 4: Calculate expected missingness by section
- Step 5: Flag conditional variables for special handling

**Why It Matters**: Without this protocol, survey structure understanding was ad-hoc and incomplete.

---

### 2. Insufficient Survey Documentation Integration

**Problem**: Survey codebook existed but wasn't systematically integrated into data processing

**Evidence**:
- Codebook clearly shows `Display Logic: Only shown if selected(${lifelonglocation}, 'no')`
- This information never made it into OP variable documentation
- Data dictionary doesn't mention survey context

**Why It Matters**: Documentation exists but isn't being used to inform processing decisions.

---

### 3. No "Red Flags" System for High Missingness

**Problem**: No systematic flagging of variables with >40% missingness for special investigation

**Should Have Triggered**:
- OP007: 53.7% missing → **INVESTIGATE WHY**
- OP019: 53.7% missing → **INVESTIGATE WHY**
- Identical missingness patterns → **INVESTIGATE RELATIONSHIP**

**Why It Matters**: High missingness should trigger automatic investigation, not acceptance.

---

### 4. Lack of Subsample Awareness

**Problem**: All households treated as single homogeneous sample

**Reality**: Survey designed with multiple subsamples:
- Lifelong vs moved residents
- Vendors vs non-vendors
- Farmers vs non-farmers
- Affected by typhoon vs not

**Why It Matters**: Analyses may need subsample-specific approaches, not universal frameworks.

---

## ✅ WHAT NEEDS TO BE DONE NOW

### Immediate Remediation (Phase 4 - Before Thesis Submission)

1. **✅ DONE**: Identify Location Choice Section and its 10 variables
2. **⏳ TODO**: Verify ALL OP variables don't come from other conditional sections
3. **⏳ TODO**: Decide on analysis strategy:
   - Keep all OP variables (N=64, acknowledge severe limitations)
   - Exclude location choice variables (N=102+, better powered)
   - Subsample analysis (N=99 location choosers, conceptually focused)
4. **⏳ TODO**: Update all thesis language with corrected understanding
5. **⏳ TODO**: Create proper survey structure documentation for appendix

---

### Long-Term Process Improvements (Future Research)

1. **Create Survey Structure Analysis Protocol**:
   - Mandatory Phase 0 deliverable
   - Survey section mapping
   - Skip logic documentation
   - Expected missingness calculations

2. **Enhance Variable Documentation Standards**:
   - Source column
   - Survey section
   - Gatekeeping logic
   - Applicability scope
   - Expected missingness
   - Conceptual meaning

3. **Implement Red Flag System**:
   - Auto-flag variables with >40% missingness
   - Auto-flag identical missingness patterns
   - Require investigation before proceeding

4. **Cross-Phase Integration Checklist**:
   - Phase 0 findings → inform Phase 1 variable creation
   - Phase 1 variable context → inform Phase 2-3 analyses
   - Phase 2-3 sample issues → properly explained in Phase 4

---

## 📚 LESSONS LEARNED

### What Went Wrong

1. **Survey structure understanding was incomplete** despite acknowledging skip logic exists
2. **Documentation was insufficient** for complex survey designs
3. **High missingness was accepted without investigation**
4. **Variables were treated independently** rather than as section members
5. **Early findings didn't systematically inform later phases**

### What Went Right

1. **User pushed for deeper investigation** when something felt wrong
2. **Raw data examination revealed true structure**
3. **Systematic audit identified patterns**, not just individual issues
4. **Problem is fixable** before thesis submission

### Key Insight

> **"Knowing skip logic exists" ≠ "Understanding survey structure"**

Phase 0 acknowledged skip logic but didn't create the systematic documentation needed to use that knowledge throughout the analysis pipeline.

---

## 🎓 IMPLICATIONS FOR THESIS

### Critical Question to Answer NOW

**Which of these 10 location choice variables are in your Turner Framework regression?**

Location Choice Section Variables (all 53.7% missing):
1. `bridge_city` - Bridge to city importance
2. `waterdistance` - **Proximity to water importance** ← OP019
3. `safe_reputation` - Safety/reputation
4. `flooding` - Flooding concerns
5. `infrastructure` - **Infrastructure quality** ← OP007
6. `foodenvironment` - Food environment
7. `schools` - School quality
8. `medical` - Medical services
9. `religion` - Religious facilities
10. `leisure` - Leisure facilities

**If ONLY OP007 and OP019**:
- Exclude these 2 → N=102 (+59% sample gain)
- Still comprehensive Turner Framework (14 predictors)

**If ANY OTHERS are also OP variables**:
- May need to exclude entire section
- Reassess Turner Framework operationalization

---

## 📝 NEXT STEPS

### Priority 1: Verify OP Variable Sourcing
- Check if any other OP variables come from this section
- Check if any OP variables come from other conditional sections (typhoon, vendor, farming)

### Priority 2: Choose Analysis Strategy
- Decide: keep all (N=64), exclude section (N=102), or subsample (N=99)
- Justify choice methodologically

### Priority 3: Create Proper Documentation
- Survey structure map (what should have been created in Phase 0)
- OP variable survey context (what should have been created in Phase 1)
- Subsample definitions and sizes

### Priority 4: Update Thesis
- Revise limitations language
- Add survey structure explanation
- Justify variable selection/exclusion choices

---

**Audit Status**: ✅ **COMPLETE**
**Root Cause**: Incomplete survey structure analysis in Phase 0, cascading through all subsequent phases
**User Assessment**: **CORRECT** - This is indeed systemic, not isolated
**Remediation**: Possible before thesis submission, but requires systematic review of all OP variables

---

**Files Created**:
- `claudedocs/SYSTEMATIC_FAILURE_AUDIT.md` (this file)
- `claudedocs/CORRECTED_ROOT_CAUSE_ANALYSIS.md` (corrected understanding of OP007/OP019)

**Files Needing Revision**:
- `LISTWISE_DELETION_DIAGNOSTIC_REPORT.md` (based on incorrect skip logic hypothesis)
- `INVESTIGATION_SUMMARY_SURVEY_SKIP_LOGIC.md` (based on incorrect skip logic hypothesis)
- All Phase 0-3 documentation (should have included survey structure)

**Recommendation**: Complete remediation before thesis submission. The systematic failures are fixable, but require thorough review of all OP variables against survey structure.
