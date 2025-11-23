---
title: "WFL-Analysis: Complete Workflow Directory"
subtitle: "Household Dietary Diversity Analysis Against Turner Framework"
date: 2025-11-23
version: 1.0
status: "active"
type: "workflow-index"
---

# WFL-Analysis Workflow Directory

## 🎯 Directory Purpose

This is your **dedicated analysis working directory** for the complete thesis data analysis workflow. It contains everything needed to:

- ✅ Plan and organize analysis phases
- ✅ Map operationalizations to data variables
- ✅ Execute Tier 1-4 analyses systematically
- ✅ Track progress and document decisions
- ✅ Integrate results into thesis chapters

**Important**: This directory is **independent from Ch03-Methods**. It contains analysis-specific documents, not chapter materials.

---

## 📁 Directory Structure & Files

```
WFL-Analysis/
├── README_ANALYSIS_WORKFLOW_251123_ERB.md (this file)
│   └── Directory index and navigation guide
│
├── Data_Analysis_Workflow_Complete.md
│   └── 6-phase executable workflow from setup through completion
│   └── USE THIS: Your step-by-step analysis roadmap
│
├── OPERATIONALIZATION_MASTER_AI_OPTIMIZED_251123_ERB.md
│   └── Complete operationalization reference (all 33 OPs)
│   └── USE THIS: Variable specifications, data mapping, limitations
│
├── OPERATIONALIZATION_QUICK_REFERENCE_251123_ERB.md
│   └── Quick lookup summary of operationalizations
│   └── USE THIS: Print and keep handy during analysis
│
├── operationalization_master.yaml
│   └── YAML-structured operationalization data
│   └── USE THIS: Load into R/Python scripts for analysis
│
├── 00_inputs/
│   ├── [household survey CSV files]
│   ├── [vendor survey CSV files]
│   ├── [geospatial data files (KML)]
│   └── [coding manuals, data dictionaries]
│
├── 01_scripts/
│   ├── 01_load_and_consolidate.R (or .py)
│   ├── 02_cleaning_and_spec.R
│   ├── 03_tier1_tier2_analyses.R
│   ├── 04_tier3_tier4_analyses.R
│   └── README_scripts.md
│
├── 02_outputs/
│   ├── tables/
│   │   ├── Table_01_Descriptive_Statistics.csv
│   │   ├── Table_02_Bivariate_Tests.csv
│   │   ├── Table_03_Correlation_Matrix.csv
│   │   └── Table_04_Regression_Model.txt
│   │
│   ├── figures/
│   │   ├── Figure_01_Correlation_Heatmap.png
│   │   └── [other visualizations]
│   │
│   └── datasets/
│       ├── household_df_consolidated.csv
│       ├── vendor_df_consolidated.csv
│       └── [cleaned, analysis-ready datasets]
│
└── 03_logs/
    ├── methodology_summary.md
    ├── variable_mapping.md
    ├── cleaning_decisions.md
    ├── data_decisions.md
    ├── analysis_notes.md
    ├── progress_log.md
    └── output_mapping.md
```

---

## 🚀 Quick Start: Which File to Use When

### **Starting Your Analysis**

**Step 1: Understand the Plan**
→ Read: **Data_Analysis_Workflow_Complete.md**
- Phases 0-6 explained
- Each phase has checkpoints
- References operationalization structure

**Step 2: Understand Your Variables**
→ Read: **OPERATIONALIZATION_MASTER_AI_OPTIMIZED_251123_ERB.md**
- All 33 operationalizations documented
- Data variables mapped to ODK surveys
- Limitations and measurement constraints
- T2 stratification specifications

**Step 3: Set Up Your Analysis**
→ Use: **operationalization_master.yaml**
- Load into R/Python scripts
- Extract variable names, metadata
- Reference in analysis code

### **During Analysis**

**Need quick reference to a variable?**
→ Check: **OPERATIONALIZATION_QUICK_REFERENCE_251123_ERB.md**
- Print this and keep handy
- All critical info on one page

**Need complete operationalization details?**
→ Search: **OPERATIONALIZATION_MASTER_AI_OPTIMIZED_251123_ERB.md**
- Ctrl+F for OP_ID (e.g., "OP016")
- Full documentation with limitations

**Writing analysis code?**
→ Use: **operationalization_master.yaml**
```r
ops <- yaml::read_yaml("operationalization_master.yaml")
t2_strata <- ops$analysis_structure$tier_2_group_comparisons
```

### **Writing Up Results**

**Organizing results tables?**
→ Reference: Master MD "Lookup Tables" section
- By domain, by role, by status
- Variable name index for exact naming

**Citing operationalizations?**
→ Use: Format "Variable (OP_ID)"
- "DDS (OP029) by Affordability Tier (OP016)"
- "Accessibility Tier (OP011; close ≤5 min vs. far >5 min)"

---

## 📋 Core Documents Explained

### **Data_Analysis_Workflow_Complete.md** (30 KB)

**What it is**: Your complete, executable analysis roadmap

**Contains**:
- Phase 0: Data consolidation with code
- Phase 1: Data cleaning & variable specification
- Phase 2: Tier 1 & 2 analyses (descriptive + bivariate)
- Phase 3: Tier 3 & 4 analyses (correlation + regression)
- Phase 4: Outputs & thesis integration
- Phase 5: Minimal viable completion checklist
- Phase 6: Progress tracking

**When to use**:
- Starting analysis (read Phases 0-1)
- Running tests (reference Phase 2-3)
- Creating outputs (reference Phase 4)
- Time pressure (use Phase 5)

**Key feature**: Contains actual R code samples you can copy/adapt

---

### **OPERATIONALIZATION_MASTER_AI_OPTIMIZED_251123_ERB.md** (47 KB)

**What it is**: Complete operationalization reference for all 33 variables

**Contains**:
- All 33 operationalizations (OP001-OP033) documented
- Lookup tables (by domain, status, role, RQ)
- Data verification checklist
- Analysis workflow mapping (T1/T2/T4)
- Variable name index for code
- YAML/JSON exports
- Integration guidance for thesis chapters

**When to use**:
- Verifying variables exist in data
- Writing methods section (copy/adapt text)
- Understanding variable limitations
- Checking data variable names for code
- Documenting analysis decisions

**Key feature**: Machine-readable + human-readable format

---

### **OPERATIONALIZATION_QUICK_REFERENCE_251123_ERB.md** (12 KB)

**What it is**: Condensed quick lookup version

**Contains**:
- Summary statistics (33 total, 31 in data, 2 planned only)
- "Big Three" T2 stratification variables
- Quick reference tables (by domain, status, role)
- One-page cheat sheet
- Data verification quick checklist

**When to use**:
- Quick lookups during analysis
- Print and keep at desk
- Find information fast
- Getting oriented

**Key feature**: Everything on ~12 pages for quick access

---

### **operationalization_master.yaml** (21 KB)

**What it is**: Machine-readable YAML structured data

**Contains**:
- All 33 OPs in YAML format
- Data variables, files, coding schemes
- T2 stratification specifications
- Analysis structure (Tier 1-4)
- Metadata (summary statistics)
- Data file inventory
- Verification checklist

**When to use**:
- Loading into R/Python scripts
- Programmatic access to variable metadata
- Configuration for analysis workflows
- Validation of variable names

**When to adapt**:
```r
# R example
ops <- yaml::read_yaml("operationalization_master.yaml")

# Get T2 stratification variables
t2_strata <- ops$analysis_structure$tier_2_group_comparisons
for (strata in t2_strata) {
  cat(strata$name, ":", strata$groups, "\n")
}

# Get all household survey variables
hh_vars <- ops$data_files$household_survey$contains_ops
```

---

## 🎯 The "Big Three" T2 Stratification Variables

These three drive your group comparison analyses:

| OP_ID | Variable | Strata | Role | Use |
|-------|----------|--------|------|-----|
| **OP011** | Accessibility Tier | Close (≤5 min) / Far (>5 min) | PRIMARY | DDS by accessibility |
| **OP016** | Food Budget Share | Low / Medium / High (tertiles) | PRIMARY | DDS by affordability |
| **OP025** | Food Safety Index | Low / High (median split) | SECONDARY | DDS by safety perception |

**All documented in**:
- Master MD: Search "T2 stratification"
- YAML: `analysis_structure.tier_2_group_comparisons`

---

## ✅ Workflow Phases at a Glance

### **Phase 0: Setup & Data Consolidation**
- Create folder structure (00_inputs/, 01_scripts/, 02_outputs/, 03_logs/)
- Load data with correct variable renaming
- Stack household & vendor datasets
- Load geospatial data
- **Checkpoint**: 3 consolidated datasets with correct n

### **Phase 1: Data Cleaning & Variable Specification**
- Document methodology summary
- Create variable mapping table
- Construct all derived variables
- Specify cleaning rules
- **Checkpoint**: All variables computed, ready for analysis

### **Phase 2: Tier 1 & 2 Analyses**
- Tier 1: Descriptive statistics (Table 01)
- Tier 2: Bivariate tests (Table 02)
- Organize by domain (External, Personal, Emergent, Outcome)
- **Checkpoint**: All primary tests run, tables created

### **Phase 3: Tier 3 & 4 Analyses**
- Tier 3: Correlation matrix (Figure 01, Table 03)
- Tier 4: Regression model (Table 04)
- Integrate across domains
- **Checkpoint**: All analyses complete, model fitted

### **Phase 4: Outputs & Thesis Integration**
- Map outputs to thesis chapters
- Create output specification table
- Prepare for thesis integration
- **Checkpoint**: All outputs documented

### **Phase 5: Minimal Viable Completion**
- If time tight, this is the must-do list
- Essential vs. should-do vs. nice-to-have
- Maintain quality on core analyses

### **Phase 6: Progress Tracking**
- Running log of completion dates
- Momentum tracking
- Supervisor communication

---

## 🔍 Finding Information

### Quick Reference

| Need | File | Search For |
|------|------|-----------|
| Understand analysis plan | Data_Analysis_Workflow | "Phase 0", "Phase 1", etc. |
| Find specific variable | OPERATIONALIZATION_MASTER | "OP016" or variable name |
| Get variable name for code | QUICK_REFERENCE or YAML | "Data Variable" column |
| Understand T2 strata | MASTER | "T2 stratification" |
| Copy code samples | Data_Analysis_Workflow | "```r" or "```python" |
| Get limitations | MASTER | "⚠️" or "Limitations" |
| Load for scripts | operationalization_master.yaml | Direct YAML load |

### Search Strategies

**Finding all T2 stratification variables**:
- Markdown: Ctrl+F "T2 stratification" → OP011, OP016, OP025
- YAML: Look for `is_t2_strata: true`

**Finding all variables in Personal Domain**:
- Markdown: Ctrl+F "personal_domain" → Section OP009-OP024
- YAML: `personal_domain:` section

**Finding unmeasured variables** (limitations):
- Markdown: Ctrl+F "planned_only" → OP008, OP024, OP027
- YAML: Look for `status: planned_only`

---

## 🛠️ Setting Up Your Analysis Environment

### **Before Starting Analysis**

1. **Create folder structure** (from Data_Analysis_Workflow Phase 0):
   ```bash
   mkdir -p 00_inputs 01_scripts 02_outputs/tables 02_outputs/figures 02_outputs/datasets 03_logs
   ```

2. **Copy data files** to `00_inputs/`:
   - Household survey CSV(s)
   - Vendor survey CSV(s)
   - KML files (geospatial)
   - Data dictionaries/manuals

3. **Load operationalization reference**:
   ```r
   # R
   ops <- yaml::read_yaml("operationalization_master.yaml")

   # Python
   import yaml
   with open("operationalization_master.yaml") as f:
       ops = yaml.safe_load(f)
   ```

4. **Begin Phase 0** following Data_Analysis_Workflow_Complete.md

---

## 📝 Using in Your Analysis

### **Example: Phase 1 - Variable Construction**

From Data_Analysis_Workflow, you need to construct HDDS. Check operationalization:

**In Master MD**:
- Search "OP029" → Dietary Diversity Score
- See: foodgroups_001_* items (11-12 count)
- Coding: 1=consumed, 0=not

**In your R code**:
```r
ops <- yaml::read_yaml("operationalization_master.yaml")
outcome <- ops$outcomes[[1]]  # OP029
cat("DDS composition:", outcome$odk_variable, "\n")

# Create DDS variable
data$DDS <- rowSums(data[, grepl("foodgroups_001", names(data))], na.rm = FALSE)

# Document in analysis notes
cat("OP029 (DDS): Sum of foodgroups_001_* items\n", file = "03_logs/analysis_notes.md", append = TRUE)
```

### **Example: Phase 2 - T2 Stratification**

From operationalization, create accessibility tier:

**In Master MD or YAML**:
- OP011: Close (≤5 min), Far (>5 min)
- Derived from: OP009 (travel time)

**In your R code**:
```r
ops <- yaml::read_yaml("operationalization_master.yaml")
t2_spec <- ops$personal_domain[[11]]  # OP011

# Create stratification variable
data$accessibility_tier <- ifelse(
  data$time_to_main_source <= 5,
  "Close (≤5 min)",
  "Far (>5 min)"
)

# Report with OP reference
cat("Tier 2 Group Comparison: DDS (OP029) by Accessibility Tier (OP011)\n")
```

### **Example: Phase 4 - Results Table Caption**

From Master MD, create table caption:

```
Table 2: Dietary Diversity Score (OP029) by Accessibility Tier (OP011)
and Affordability Tier (OP016) – Tier 2 Group Comparisons

Note: Accessibility tier (OP011) is binary (close ≤5 min vs. far >5 min).
Affordability tier (OP016) is tertile-stratified food budget share
(low/medium/high). DDS = Dietary Diversity Score (OP029; count of food
groups consumed, range 0-12).
```

---

## 📊 Analysis Structure (T1-T2-T4)

### **Tier 1: Descriptive Statistics**
- **What**: Mean, SD, frequencies, n, missing
- **Variables**: All "in_data" operationalizations (OP001-OP033 except OP008, OP024, OP027)
- **Organization**: By domain (External, Personal, Emergent, Outcome)
- **Output**: Table 1
- **Reference**: Data_Analysis_Workflow Phase 2, Master MD "Analysis Workflow Mapping"

### **Tier 2: Group Comparisons**
- **What**: DV (OP029-OP033) stratified by T2 strata
- **Strata**:
  - OP011 (Accessibility): 2 groups
  - OP016 (Affordability): 3 groups
  - OP025 (Safety): 2 groups
- **Tests**: ANOVA, t-tests, Mann-Whitney U
- **Output**: Tables 2a-2d
- **Reference**: Data_Analysis_Workflow Phase 2

### **Tier 4: Framework Assessment**
- **What**: Domain comparison, effect ranking, interactions
- **Analysis**:
  - Which determinants most strongly associated with DDS?
  - External vs. Personal domain effects
  - Interaction: Accessibility × Affordability
- **Output**: Table 3
- **Reference**: Data_Analysis_Workflow Phase 3

---

## ⚠️ Key Limitations to Document

| OP_ID | Component | Limitation | Severity |
|-------|-----------|-----------|----------|
| OP003 | Prices | Motive-based proxy, no actual price audit | Medium |
| OP008 | Marketing & Regulation | NOT MEASURED; not in analysis | HIGH |
| OP014 | Income Proxy | Likely asset-based, not direct income | Medium |
| OP024 | Food Preference | May not be systematically collected | Medium |
| OP027 | Food Decision-Maker Gender | Not measured; status TBD | Medium |
| OP028 | Stability | Single-timepoint survey limits temporal analysis | High |

**All documented in**: Master MD "Key Limitations" section

---

## 🔗 Connection to Thesis Chapters

**NOT in this directory**: Chapter 3 methodology text
- That lives in: `/Ch03-Methods/Working/`
- These documents inform that chapter but are separate

**THIS directory feeds to thesis chapters**:
- **Chapter 3 (Methods)**: Use operationalizations to write measurement section
- **Chapter 4 (Results)**: Use output tables created here
- **Chapter 5 (Discussion/Limitations)**: Reference OP limitations documented here

---

## 📞 Troubleshooting Guide

### "I can't find a variable in my data"

1. Check spelling in Master MD (Data Variable column)
2. Search YAML for alternate names
3. Check data dictionary
4. If still missing: Update Status to "NOT_FOUND" and document why

### "Should I include OP008 in analysis?"

**No**. Marketing & Regulation (OP008) is marked `planned_only` (not measured). Document as a study limitation in Methods/Limitations sections.

### "What if my T2 strata cutpoints are different?"

1. Update Master MD with your actual cutpoints
2. Update YAML `t2_calculation` field
3. Document rationale in analysis notes
4. Cite with amendment: "OP011 stratified at 10 min (not 5 min) based on..."

### "How do I track progress?"

Use: `03_logs/progress_log.md`

Format:
```
## 2025-11-23
- [09:00] Completed Phase 0: Data consolidation
- [10:30] Started Phase 1: Variable specification
- [12:00] ✅ CHECKPOINT: Phase 1 complete
```

---

## ✅ Before You Start: Checklist

- [ ] Read: Data_Analysis_Workflow_Complete.md
- [ ] Read: OPERATIONALIZATION_MASTER_AI_OPTIMIZED_251123_ERB.md (at least skim)
- [ ] Verify: All data files in 00_inputs/
- [ ] Create: Folder structure (00_inputs, 01_scripts, 02_outputs, 03_logs)
- [ ] Load: operationalization_master.yaml in your analysis environment
- [ ] Check: All variables from Master MD exist in your data
- [ ] Document: Sample sizes (n_household, n_vendor)
- [ ] Plan: Which analyses are MUST_DO vs. SHOULD_DO (Phase 5 of Workflow)

---

## 📚 Document Relationships

```
Data_Analysis_Workflow_Complete.md
├── References all 33 operationalizations
├── Uses Phase structure: 0→1→2→3→4→5→6
└── Points to operationalization reference for variable details

OPERATIONALIZATION_MASTER_AI_OPTIMIZED_251123_ERB.md
├── Complete reference for all variables
├── Maps to data files and analysis roles
└── Provides code samples and limitations

operationalization_master.yaml
├── YAML version of Master MD
├── Load into analysis scripts
└── Extract metadata programmatically

OPERATIONALIZATION_QUICK_REFERENCE_251123_ERB.md
├── Condensed summary of Master MD
└── Print and keep handy

→ All work together to ground your analysis
```

---

## 🚀 Starting Right Now

1. **Open**: Data_Analysis_Workflow_Complete.md
2. **Read**: Phase 0 & Phase 1
3. **Create**: Folder structure
4. **Load**: operationalization_master.yaml
5. **Begin**: Phase 0 (data consolidation)

---

## 📋 Files in This Directory

| File | Size | Purpose |
|------|------|---------|
| Data_Analysis_Workflow_Complete.md | 30 KB | Executable 6-phase workflow |
| OPERATIONALIZATION_MASTER_AI_OPTIMIZED_251123_ERB.md | 47 KB | Complete operationalization reference |
| OPERATIONALIZATION_QUICK_REFERENCE_251123_ERB.md | 12 KB | Quick lookup summary |
| operationalization_master.yaml | 21 KB | YAML-structured data for code |
| README_ANALYSIS_WORKFLOW_251123_ERB.md | This file | Directory index and navigation |

**Total**: ~110 KB of analysis documentation and workflow specification

---

## 💾 Version & Status

**Version**: 1.0
**Date**: 2025-11-23
**Status**: ✅ Active - Ready for Analysis
**Location**: `/WFL-Analysis/` (separate from Ch03-Methods)
**Scope**: Complete analysis workflow, independent from chapter materials

---

**This directory is your complete, self-contained analysis workspace. Everything you need to execute the full analysis workflow is here. Happy analyzing!** 🚀
