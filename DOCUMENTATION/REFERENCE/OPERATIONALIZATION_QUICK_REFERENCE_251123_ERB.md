---
title: "Operationalization Master Table - Quick Reference"
date: 2025-11-23
author: "Emerson Richmond Burke"
type: "quick-reference"
---

# Operationalization Quick Reference

**Master Table File**: `OPERATIONALIZATION_MASTER_TABLE_251123_ERB.xlsx`
**Full Guide**: `OPERATIONALIZATION_MASTER_TABLE_GUIDE_251123_ERB.md`

---

## 📊 By the Numbers

| Category | Count | Status |
|----------|-------|--------|
| **Total Operationalizations** | 33 | 100% mapped |
| **In Data (Ready)** | 31 | 94% ✅ |
| **Planned Only (Limitation)** | 2 | 6% ⚠️ |
| **External Domain** | 8 | Complete (1 unmeasured) |
| **Personal Domain** | 16 | Complete |
| **Emergent Dimensions** | 3 | Complete |
| **Outcome Variables** | 5 | Complete |

---

## 📍 Find What You Need

### By Domain

**EXTERNAL DOMAIN (OP001-OP008)**
- **Availability** (OP001-OP002): Vendor surveys, outlet types, food group presence
- **Prices** (OP003): Perceived affordability motive
- **Vendor & Product** (OP004-OP007): Cleanliness, safety, reputation, infrastructure
- **Marketing & Regulation** (OP008): ❌ NOT MEASURED (documented limitation)

**PERSONAL DOMAIN (OP009-OP024)**
- **Accessibility** (OP009-OP011): Travel time, frequency, tier classification
- **Affordability** (OP012-OP016): Expenditure, income proxy, motive, budget share tier
- **Convenience** (OP017-OP020): Proximity, cooking source, water access
- **Desirability** (OP021-OP024): Health motive, trust motive, perception, preference

**EMERGENT (OP025-OP028)**
- **Food Safety** (OP025): Aggregate index (clean + safe + reputation)
- **Social Forces** (OP026-OP027): Trust-based shopping, gender of decision-maker
- **Stability** (OP028): Frequency variation across outlets

**OUTCOME (OP029-OP033)**
- **Dietary Diversity Score** (OP029): Count of food groups consumed
- **Food Type Quality** (OP030-OP032): % nutrient-dense, % processed, quality tier
- **Diet Quality Category** (OP033): Poor/Adequate/Diverse classification

---

### By Role in Analysis

**DEPENDENT VARIABLES (DV)**
- OP029: DDS (Dietary Diversity Score) - primary outcome
- OP030-OP033: Diet composition and quality measures

**INDEPENDENT VARIABLES (IV) - T2 Stratification**
- OP011: Accessibility Tier (close ≤5 min vs. far >5 min) ⭐ Major
- OP016: Affordability Tier (low/medium/high food budget share) ⭐ Major
- OP025: Food Safety Tier (low vs. high perception index)
- OP027: Trust-based shopping & gender of decision-maker

**INDEPENDENT VARIABLES (IV) - Domain Descriptors**
- OP001-OP010, OP012-OP015, OP017-OP024: Detailed component measures

**DERIVED/CONSTRUCTED**
- OP016: Food Budget Share (food_expenditure / income × 100)
- OP025: Food Safety Index (mean of clean, safe, reputation)
- OP031-OP033: Diet quality compositions (derived from OP029)

---

## 🔑 Critical Operationalizations

### The "Big Three" for Your Research Question

| OP_ID | Variable | Survey Source | Data Variable | T2 Use |
|-------|----------|---------------|---------------|--------|
| **OP016** | Affordability Tier | HH expenditure + income proxy | `food_budget_share_pct` | **PRIMARY**: Stratify DDS by 3 tiers |
| **OP011** | Accessibility Tier | Travel time to outlets | `time_to_main_source` | **PRIMARY**: Stratify DDS by 2 tiers (≤5 vs >5 min) |
| **OP025** | Food Safety Index | Aggregate perception (clean, safe, reputation) | `food_safety_index` | **SECONDARY**: Stratify DDS by tier |

**→ These three variables drive your T2 group comparison analyses**

---

## ⚠️ Key Limitations

| OP_ID | Component | Limitation | Severity |
|-------|-----------|-----------|----------|
| **OP003** | Prices | Motive-based proxy, not actual price audit | Medium |
| **OP008** | Marketing & Regulation | Not measured; no observation/audit | High |
| **OP014** | Income Proxy | Likely asset-based, not direct income | Medium |
| **OP024** | Food Preference/Habit | May not be systematically collected | Medium |
| **OP028** | Stability | Single-timepoint survey limits temporal analysis | High |

**→ These are legitimate study design choices, not oversights. Document clearly in Limitations section.**

---

## 🔍 Data Verification - Quick Checklist

Before you analyze, verify these key files exist:

```
HOUSEHOLD SURVEY DATA:
[ ] data_household_survey.csv contains 35+ columns
    - foodgroups_001_* (food group consumption, 11 items)
    - reason_001-005 (shopping motives)
    - clean, safe, reputation (perceptions)
    - time_001-007 or transportation_001-007 (travel times)
    - [outlet_type]_freq (visit frequency)
    - foodexpenditure, foodexp_timeunit
    - cookingsource, watersource, waterdistance

VENDOR SURVEY DATA:
[ ] data_vendor_survey.csv contains 20+ columns
    - foodgroups_001_* (food group availability, 11 items)
    - vendor_type (outlet classification)
    - infrastructure (vendor-reported)

Sample Sizes:
[ ] Household survey: n = [FILL IN]
[ ] Vendor survey: n = [FILL IN]
```

---

## 📝 How to Cite in Your Thesis

### In Methods Section
"Accessibility was operationalized as self-reported travel time to food sources (measured in minutes) from household surveys. For analysis, households were classified into binary categories: close access (≤5 minutes travel) and far access (>5 minutes) based on time to their primary food source (OP011)."

### In Results Section
"Dietary diversity significantly varied by accessibility tier (T2 comparison, OP029 by OP011). Households with close access (≤5 min) consumed a mean of X food groups [SD=Y], compared to Z groups [SD=W] for households with far access (p=0.05)."

### In Limitations Section
"The Prices determinant (OP003) was operationalized as household-reported shopping motive ('buying because cheap') rather than direct price audits. This single-item proxy may not fully capture price barriers and availability of affordable options. Additionally, Marketing & Regulation (OP008) was not measured through structured observation or policy document review, limiting assessment of this external domain component."

---

## 🚀 Analysis Workflow Using the Master Table

### **Phase 1: T1 Descriptive Statistics**
Use all "in_data" rows (OP001-OP033 except OP008, OP024)
- **Report**: Mean/SD for continuous; frequencies for categorical; n/missing
- **Organize**: By domain (External, Personal, Emergent, Outcome)
- **Reference**: "Summary statistics for operationalizations OP001-OP033 presented in Table 1"

### **Phase 2: T2 Group Comparisons**
Use DV (OP029-OP033) stratified by T2 strata (OP011, OP016, OP025, OP027)
- **Create tables**: DDS [OP029] by Affordability Tier [OP016], by Accessibility Tier [OP011], etc.
- **Run tests**: t-tests or ANOVAs with p-values and effect sizes
- **Reference**: "Dietary diversity (OP029) by affordability tier (OP016) in Table 2; p=0.04"

### **Phase 3: T4 Framework Assessment**
Compare effect sizes and patterns across domains
- **External domain effects** (OP001-OP007): Which determinants most strongly associated with diet?
- **Personal domain effects** (OP009-OP024): Which determinants most strongly associated with diet?
- **Domain interaction**: Does affordability (OP016) moderate accessibility (OP011)?
- **Reference**: "Framework assessment (T4, OP016 × OP011 interaction): β = -0.23, p=0.08"

---

## 🎯 T1-T2-T4 Mapping to Master Table

| Analysis Phase | What You Do | Master Table Rows |
|---|---|---|
| **T1 Descriptive** | Report all variables | All OP (01-33) except OP008, OP024 |
| **T2 Affordability** | Stratify DDS by food budget share | OP029 DV × OP016 IV |
| **T2 Accessibility** | Stratify DDS by travel time | OP029 DV × OP011 IV |
| **T2 Safety** | Stratify DDS by safety perception | OP029 DV × OP025 IV |
| **T2 Social** | Stratify DDS by trust/gender | OP029 DV × OP027 IV |
| **T4 External** | Effect ranking (OP001-OP007) | External domain OP001-OP007 |
| **T4 Personal** | Effect ranking (OP009-OP024) | Personal domain OP009-OP024 |
| **T4 Interaction** | Test moderation | OP016 × OP011, OP025 × OP016, etc. |

---

## 🔗 File Organization

Your thesis folder now contains:

```
Ch03-Methods/Working/
├── OPERATIONALIZATION_MASTER_TABLE_251123_ERB.xlsx
│   └── The authoritative 33-row operationalization map
├── OPERATIONALIZATION_MASTER_TABLE_GUIDE_251123_ERB.md
│   └── Complete user guide (this document's source)
├── OPERATIONALIZATION_QUICK_REFERENCE_251123_ERB.md
│   └── This summary (print-friendly)
├── TURNER-VariableMapping_251123_ERB.md
│   └── Detailed technical mapping (reference document)
├── PRIORITY-NextSteps_251123_ERB.md
│   └── T1-T2-T4 timeline and next steps
└── ANALYSIS-CrossReference_251123_ERB.md
    └── Feedback implementation checklist
```

---

## ✅ Verification Checklist (Print & Use)

**Before You Start Analysis**

- [ ] Open OPERATIONALIZATION_MASTER_TABLE_251123_ERB.xlsx
- [ ] Scan all 33 rows; understand the 4 domains
- [ ] Identify the 2 "planned_only" rows (OP008, OP024); document why unmeasured
- [ ] Identify the 4 "IV T2 stratification" rows (OP011, OP016, OP025, OP027)
- [ ] Load your household survey data; verify all variables from Master Table exist
- [ ] Load your vendor survey data; verify all variables from Master Table exist
- [ ] Document sample sizes (n_household, n_vendor)
- [ ] Check for missing data; flag variables with >30% missingness
- [ ] Make working copy of Master Table; update Status as you verify each variable
- [ ] Create analysis script with references to OP_IDs in comments
- [ ] Before writing results, link every table/finding back to specific OP rows

---

## 🎓 What This Demonstrates to Examiners

✅ **Theoretical Rigor**: Every Turner component explicitly operationalized
✅ **Methodological Transparency**: All measurement choices documented with limitations
✅ **Data Integrity**: Variables grounded in actual surveys, not speculation
✅ **Analytical Coherence**: Analysis plan flows directly from operationalization
✅ **Reflexivity**: Gaps (marketing/regulation) acknowledged, not hidden
✅ **Reproducibility**: Reader can trace any finding back to specific operationalization

---

## 📞 Quick Troubleshooting

**Q: A variable doesn't exist in my data. What do I do?**
A: (1) Check spelling in data dictionary (2) Search for similar names (3) Check if derived/renamed (4) If truly missing, update Status to "NOT FOUND" and document as limitation

**Q: Should I include marketing/regulation (OP008) in my analysis?**
A: No. Mark as "Not Measured" in Methods. This is a valid limitation, not a failure.

**Q: How do I aggregate variables into indices?**
A: Document the method: "Food Safety Index (OP025) computed as z-standardized mean of clean (OP004), safe (OP005), and reputation (OP006), with Cronbach's ω = 0.78"

**Q: What if I want to add a new operationalization?**
A: Use next OP_ID number (OP034+). Maintain same 14-column structure. Consider whether it strengthens or dilutes Turner framework focus.

---

## 📋 One-Page Cheat Sheet

```
EXTERNAL DOMAIN
├─ Availability (OP001-002): ✅ In data | Vendor surveys
├─ Prices (OP003): ✅ In data | Motive-based proxy (limitation)
├─ Vendor Props (OP004-007): ✅ In data | Clean, safe, reputation
└─ Marketing/Regulation (OP008): ❌ NOT MEASURED (limitation)

PERSONAL DOMAIN
├─ Accessibility (OP009-011): ✅ In data | Travel time, tier ⭐
├─ Affordability (OP012-016): ✅ In data | Food budget share tier ⭐
├─ Convenience (OP017-020): ✅ In data | Proximity, cooking, water
└─ Desirability (OP021-024): ✅ In data | Health, trust motives

EMERGENT
├─ Food Safety (OP025): ✅ In data | Aggregate index ⭐
├─ Social Forces (OP026-027): ✅ In data | Trust & gender
└─ Stability (OP028): ✅ In data | Frequency variation (single timepoint)

OUTCOME
├─ DDS (OP029): ✅ In data | Primary DV
├─ Diet Type (OP030-032): ✅ In data | % Nutrient-dense, % Processed
└─ Diet Tier (OP033): ✅ In data | Poor/Adequate/Diverse

T2 STRATIFICATION
├─ OP016: Affordability Tier (low/med/high) ⭐⭐⭐ PRIMARY
├─ OP011: Accessibility Tier (close ≤5 min / far >5 min) ⭐⭐⭐ PRIMARY
├─ OP025: Safety Tier (low/high) ⭐⭐ SECONDARY
└─ OP027: Trust & Gender ⭐ SECONDARY
```

---

**Quick Ref Created**: 23 November 2025
**Status**: Ready to print and keep handy
**For detailed guide, see**: `OPERATIONALIZATION_MASTER_TABLE_GUIDE_251123_ERB.md`

