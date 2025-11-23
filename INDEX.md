---
title: "WFL-Analysis Master Index and Navigation"
date: 2025-11-23
status: "✅ Organized and Ready"
version: 1.0
---

# 📚 WFL-Analysis Master Index

**Welcome to your analysis workspace!** This document guides you through the complete directory structure and helps you find what you need quickly.

---

## 🎯 Quick Navigation

### I Want to...

| Goal | Start Here |
|------|-----------|
| **Get started immediately** | → `DOCUMENTATION/START_HERE/README_ANALYSIS_WORKFLOW.md` |
| **Verify setup is complete** | → `DOCUMENTATION/START_HERE/SETUP_COMPLETION_VERIFICATION.md` |
| **Find a specific variable (OP#)** | → `DOCUMENTATION/REFERENCE/OPERATIONALIZATION_MASTER_AI_OPTIMIZED.md` |
| **Look up a variable quickly** | → `DOCUMENTATION/REFERENCE/OPERATIONALIZATION_QUICK_REFERENCE.md` |
| **Load data into R/Python** | → `DOCUMENTATION/REFERENCE/operationalization_master.yaml` |
| **Understand my data files** | → `DOCUMENTATION/REFERENCE/DATA_INVENTORY_AND_SETUP.md` |
| **Execute the analysis workflow** | → `DOCUMENTATION/GUIDES/Data_Analysis_Workflow_Complete.md` |
| **Know where my data is** | → `00_inputs/` |
| **Save my analysis scripts** | → `01_scripts/` |
| **Store my results** | → `02_outputs/` |
| **Document my decisions** | → `03_logs/` |

---

## 📁 Complete Directory Structure

```
WFL-Analysis/
│
├── 📖 DOCUMENTATION/                    ← All documents organized here
│   │
│   ├── 🚀 START_HERE/                   ← Begin here on first use
│   │   ├── README_ANALYSIS_WORKFLOW.md          (18 KB) Navigation guide
│   │   ├── WORKFLOW_SETUP_SUMMARY.md            (14 KB) What's been set up
│   │   └── SETUP_COMPLETION_VERIFICATION.md    (Final verification checklist)
│   │
│   ├── 📚 REFERENCE/                    ← Look up details during work
│   │   ├── OPERATIONALIZATION_MASTER_AI_OPTIMIZED.md  (47 KB) Complete reference
│   │   ├── OPERATIONALIZATION_QUICK_REFERENCE.md      (12 KB) Quick lookup
│   │   ├── operationalization_master.yaml             (21 KB) For R/Python
│   │   └── DATA_INVENTORY_AND_SETUP.md               (Data file locations)
│   │
│   └── 🔬 GUIDES/                      ← Execute workflow from here
│       └── Data_Analysis_Workflow_Complete.md  (30 KB) 6-phase workflow
│
├── 📥 00_inputs/                        ← All input data here
│   ├── data/
│   │   ├── household_survey_LONG_BIEN_2024_ALL_merged.csv
│   │   ├── vendor_survey_LONG_BIEN_2024_ALL_merged.csv
│   │   ├── Household_survey_*_with/withoutFoodWaste.xlsx
│   │   ├── Vendor_survey_*_with/withoutFoodWaste.xlsx
│   │   └── *.kml (geospatial files)
│   │
│   └── survey_instruments/
│       ├── household-survey/ (ODK files)
│       ├── vendor-survey/ (ODK files)
│       ├── household-survey-codebook.md
│       └── vendor-survey-codebook.md
│
├── 💻 01_scripts/                       ← Save your analysis code here
│   └── [Your Phase 0-6 analysis scripts]
│
├── 📊 02_outputs/                       ← Save your results here
│   ├── tables/ (Statistical tables)
│   ├── figures/ (Plots and visualizations)
│   └── datasets/ (Processed/derived datasets)
│
├── 📝 03_logs/                          ← Document your work here
│   └── [Your analysis notes and decisions]
│
└── 📋 INDEX.md                          ← This file
```

---

## 🚀 Getting Started (5 Minutes)

### Step 1: Orient Yourself (2 min)
1. Read: `DOCUMENTATION/START_HERE/README_ANALYSIS_WORKFLOW.md`
2. Skim: `DOCUMENTATION/START_HERE/WORKFLOW_SETUP_SUMMARY.md`

### Step 2: Verify Everything is Ready (1 min)
- Read: `DOCUMENTATION/START_HERE/SETUP_COMPLETION_VERIFICATION.md`
- Confirm all items are checked ✅

### Step 3: Prepare for Phase 0 (2 min)
1. Print: `DOCUMENTATION/REFERENCE/OPERATIONALIZATION_QUICK_REFERENCE.md`
2. Bookmark: `DOCUMENTATION/GUIDES/Data_Analysis_Workflow_Complete.md`

---

## 📚 Documentation Folder Details

### START_HERE/ — First Time Setup & Navigation

**README_ANALYSIS_WORKFLOW.md** (18 KB)
- **Purpose**: Your primary navigation guide
- **Contains**:
  - How to use this workflow system
  - Which file to use when
  - Finding information strategies
  - Setting up your analysis environment
  - Troubleshooting guide
- **When to use**: First thing when starting; whenever you're lost
- **Read time**: 10-15 minutes

**WORKFLOW_SETUP_SUMMARY.md** (14 KB)
- **Purpose**: Overview of what's been completed
- **Contains**:
  - Summary of setup work
  - Key statistics (33 operationalizations, 31 in data)
  - "Big Three" T2 variables explained
  - Next steps in order
  - Quick troubleshooting guide
- **When to use**: First time, or when you need an overview
- **Read time**: 5-10 minutes

**SETUP_COMPLETION_VERIFICATION.md**
- **Purpose**: Final verification that everything is ready
- **Contains**:
  - Complete setup checklist with ✅ marks
  - File verification (all 7 docs present)
  - Data file verification (all 10 datasets present)
  - Sample size confirmation
  - Unmeasured variables documented
  - Critical variable naming issues explained
- **When to use**: Before starting Phase 0
- **Read time**: 5 minutes

### REFERENCE/ — Lookup During Analysis

**OPERATIONALIZATION_MASTER_AI_OPTIMIZED.md** (47 KB)
- **Purpose**: Complete reference for all 33 operationalizations
- **Contains**: All variables with:
  - OP_ID and Turner component
  - Theoretical construct definition
  - Survey variable names (ODK codes)
  - Data file location
  - Data variable names
  - How values are coded
  - Role in analysis (DV/IV/Control)
  - Research question addressed
  - Limitations and proxies noted
  - Status (in_data vs planned_only)
- **When to use**: When constructing variables or writing methods
- **Search**: Use browser Find (Ctrl+F) for "OP###" or variable name
- **Example lookup**: "Find OP011" → Accessibility Tier, close/far classification

**OPERATIONALIZATION_QUICK_REFERENCE.md** (12 KB)
- **Purpose**: Condensed summary (print this!)
- **Contains**:
  - By the numbers (33 total, 31 in data, 2 planned)
  - Find what you need (by domain, by role)
  - Critical operationalizations (Big Three)
  - Key limitations
  - Quick verification checklist
  - One-page cheat sheet
  - How to cite in thesis
- **When to use**: During analysis for quick lookups
- **Best practice**: Print this and keep at your desk
- **Format**: Print-friendly with clear sections

**operationalization_master.yaml** (21 KB)
- **Purpose**: Machine-readable YAML for code integration
- **Contains**: All metadata in YAML structure:
  ```yaml
  metadata:
    total_operationalizations: 33
    in_data: 31
  external_domain:
    - op_id: OP001
      data_variable: "foodgroups_001_*"
      data_file: "data_vendor_survey.csv"
  analysis_structure:
    tier_2_group_comparisons:
      stratification_variables: [...]
  ```
- **When to use**: When loading into R/Python scripts
- **Example R usage**:
  ```r
  library(yaml)
  ops <- yaml::read_yaml("DOCUMENTATION/REFERENCE/operationalization_master.yaml")
  t2_vars <- ops$analysis_structure$tier_2_group_comparisons
  ```
- **Example Python usage**:
  ```python
  import yaml
  with open('DOCUMENTATION/REFERENCE/operationalization_master.yaml') as f:
      ops = yaml.safe_load(f)
  ```

**DATA_INVENTORY_AND_SETUP.md**
- **Purpose**: Complete mapping of all data files
- **Contains**:
  - All 10 data files listed with locations
  - Sample sizes confirmed (n=241 households, n=284 vendors)
  - Survey instruments documented
  - Codebook references
  - **CRITICAL**: Variable naming conflict explanation
    - `foodgroups_001_*` = consumption items (for HDDS)
    - `foodgroups` = sales string
  - Data verification checklist
  - Phase 0 preparation notes
- **When to use**: Before Phase 0, when looking up file locations
- **Critical section**: Read the variable conflict section carefully!

### GUIDES/ — Execute Analysis From Here

**Data_Analysis_Workflow_Complete.md** (30 KB)
- **Purpose**: Your complete, step-by-step analysis roadmap
- **Contains**: 6 phases:
  - **Phase 0**: Setup & Data Consolidation (with R code samples)
  - **Phase 1**: Data Cleaning & Variable Specification
  - **Phase 2**: Tier 1 & 2 Analyses (descriptive + bivariate)
  - **Phase 3**: Tier 3 & 4 Analyses (correlation + regression)
  - **Phase 4**: Outputs & Thesis Integration
  - **Phase 5**: Minimal Viable Completion Checklist
  - **Phase 6**: Progress Tracking
- **When to use**: Follow from start to finish of your analysis
- **Best practice**:
  - Copy code samples directly into your scripts
  - Adapt variable names to your actual data
  - Save progress notes in `03_logs/`
  - Checkpoint after each phase

---

## 📊 Data Folder Details (00_inputs/)

### data/ — All Datasets (1.6 MB total)

**Household Survey Files** (n=241 households)
- `household_survey_LONG_BIEN_2024_ALL_merged.csv` ← Load this for analysis
- `Household_survey_LONG_BIEN_2024_ALL_withFoodWaste.xlsx` (102 households)
- `Household_survey_LONG_BIEN_2024_ALL_withoutFoodWaste.xlsx` (139 households)
- `households_LongBien_2024_ALL_withFoodWaste.kml` (geospatial)
- `households_LongBien_2024_ALL_withoutFoodWaste.kml` (geospatial)

**Vendor Survey Files** (n=284 vendors)
- `vendor_survey_LONG_BIEN_2024_ALL_merged.csv` ← Load this for analysis
- `Vendor_survey_LONG_BIEN_2024_ALL_withFoodWaste.xlsx` (284 vendors)
- `Vendor_survey_LONG_BIEN_2024_ALL_withoutFoodWaste.xlsx` (284 vendors)
- `vendors_LongBien_2024_ALL_withFoodWaste.kml` (geospatial)
- `vendors_LongBien_2024_ALL_withoutFoodWaste.kml` (geospatial)

**What to Load in Phase 0**:
- Start with merged CSV files in Phase 0
- Handle "with/without food waste module" separation (see Phase 0 code)
- KML files for geospatial visualization (optional, after Phase 0)

### survey_instruments/ — ODK Survey Files

**Household Survey**
- `household-survey/` folder (XLS + XML from ODK)
- `household-survey-codebook.md` (122 KB - variable reference)

**Vendor Survey**
- `vendor-survey/` folder (XLS + XML from ODK)
- `vendor-survey-codebook.md` (45 KB - variable reference)

**When to use**: Reference codebooks when:
- Finding survey variable names
- Understanding how data was collected
- Checking answer options and codes

---

## 💻 Work Folders (01_scripts, 02_outputs, 03_logs)

### 01_scripts/ — Your Analysis Code

Store all R/Python scripts here:
```
01_scripts/
├── Phase_0_DataConsolidation.R
├── Phase_1_Cleaning_VariableConstruction.R
├── Phase_2_Tier1_Tier2_Analysis.R
├── Phase_3_Tier3_Tier4_Analysis.R
├── Phase_4_OutputsIntegration.R
└── utility_functions.R
```

### 02_outputs/ — Your Results

Organize results by type:
```
02_outputs/
├── tables/
│   ├── Table_1_DescriptiveStats_AllVariables.csv
│   ├── Table_2_T2_HDDS_by_Affordability.csv
│   └── ...
├── figures/
│   ├── Figure_1_HDDS_Distribution.pdf
│   └── ...
└── datasets/
    ├── household_processed_Phase0.csv
    └── ...
```

### 03_logs/ — Your Documentation

Store analysis notes and decisions:
```
03_logs/
├── Phase_0_DataConsolidation_Log.md
├── Phase_1_VariableConstruction_Decisions.md
├── Phase_2_T2_Analysis_Notes.md
└── Limitations_and_Issues.md
```

---

## 🔑 Key Information Summary

### The "Big Three" T2 Stratification Variables
| Variable | OP_ID | Groups | Purpose |
|----------|-------|--------|---------|
| **Accessibility Tier** | OP011 | Close (≤5 min) / Far (>5 min) | PRIMARY stratification |
| **Food Budget Share Tier** | OP016 | Low / Medium / High | PRIMARY stratification |
| **Food Safety Tier** | OP025 | Low / High | SECONDARY stratification |

### Sample Sizes
- **Households**: 241 total
  - With food waste module: 102
  - Without food waste module: 139
- **Vendors**: 284

### Total Operationalizations
- **Total**: 33
- **In Data**: 31 (ready for analysis)
- **Planned Only**: 2 (OP008 Marketing/Regulation, OP024/OP027 status TBD)

### Critical Variable Naming Conflict
⚠️ **Must handle in Phase 0**:
- `foodgroups_001_*` = consumption items → rename to `hh_consumption_*`
- `foodgroups` = sales string → rename to `hh_sales_string`

**Solution code** in Phase 0:
```r
rename_with(~gsub("foodgroups_001_", "hh_consumption_", .x), starts_with("foodgroups_001_"))
rename(hh_sales_string = foodgroups)
```

---

## ❓ Finding What You Need

### By Task

| Task | File | Section |
|------|------|---------|
| Getting oriented | `START_HERE/README_ANALYSIS_WORKFLOW.md` | All |
| Verifying setup | `START_HERE/SETUP_COMPLETION_VERIFICATION.md` | All |
| Finding a variable | `REFERENCE/OPERATIONALIZATION_MASTER_AI_OPTIMIZED.md` | Search for OP### |
| Quick variable lookup | `REFERENCE/OPERATIONALIZATION_QUICK_REFERENCE.md` | Find What You Need |
| Understanding limitations | `REFERENCE/OPERATIONALIZATION_QUICK_REFERENCE.md` | Key Limitations |
| Loading data in code | `REFERENCE/operationalization_master.yaml` | All |
| File locations | `REFERENCE/DATA_INVENTORY_AND_SETUP.md` | Data Files section |
| Variable naming issues | `REFERENCE/DATA_INVENTORY_AND_SETUP.md` | Critical Notes |
| Executing Phase 0 | `GUIDES/Data_Analysis_Workflow_Complete.md` | Phase 0 |
| Understanding T2 variables | `REFERENCE/OPERATIONALIZATION_QUICK_REFERENCE.md` | T1-T2-T4 Mapping |

### By Document Type

**Human-Readable Guides**
- START_HERE/ (for orientation)
- REFERENCE/ (MD files for lookup)
- GUIDES/ (for step-by-step execution)

**Machine-Readable Code**
- `REFERENCE/operationalization_master.yaml` (R/Python loading)

**Data Files**
- `00_inputs/data/` (CSV, XLSX, KML)
- `00_inputs/survey_instruments/` (ODK, codebooks)

---

## 📋 Next Steps Checklist

Before beginning Phase 0:

- [ ] Read `DOCUMENTATION/START_HERE/README_ANALYSIS_WORKFLOW.md`
- [ ] Skim `DOCUMENTATION/START_HERE/WORKFLOW_SETUP_SUMMARY.md`
- [ ] Review `DOCUMENTATION/START_HERE/SETUP_COMPLETION_VERIFICATION.md`
- [ ] Print or bookmark `DOCUMENTATION/REFERENCE/OPERATIONALIZATION_QUICK_REFERENCE.md`
- [ ] Locate all data files in `00_inputs/data/`
- [ ] Understand the variable naming conflict (see REFERENCE folder)
- [ ] Open `DOCUMENTATION/GUIDES/Data_Analysis_Workflow_Complete.md`
- [ ] Start Phase 0: Data Consolidation

---

## 🆘 Troubleshooting

**Can't find a file?**
→ Use `INDEX.md` (this file) → Quick Navigation table

**Don't know which document to read?**
→ Use "I Want to..." section at the top of this file

**Need to find a specific variable?**
→ Search `DOCUMENTATION/REFERENCE/OPERATIONALIZATION_MASTER_AI_OPTIMIZED.md` for "OP###" or variable name

**Have a quick question during analysis?**
→ Check `DOCUMENTATION/REFERENCE/OPERATIONALIZATION_QUICK_REFERENCE.md` (print this!)

**Need to see your data files?**
→ Open `DOCUMENTATION/REFERENCE/DATA_INVENTORY_AND_SETUP.md`

---

## 📊 Directory Statistics

| Component | Count | Size | Status |
|-----------|-------|------|--------|
| Documentation files | 7 | ~140 KB | ✅ Complete |
| Data files | 10 | 1.6 MB | ✅ Complete |
| Survey instruments | 4 | 300 KB | ✅ Complete |
| Work directories | 4 | Empty | ✅ Ready |
| **TOTAL** | **25 items** | **~2.2 MB** | **✅ READY** |

---

## ✅ Status

**Workspace Organization**: ✅ Complete
**Documentation**: ✅ Organized and Cross-Referenced
**Data**: ✅ All Files Present and Verified
**Ready for Analysis**: ✅ YES

**Last Updated**: 2025-11-23
**Your Next Action**: Open `DOCUMENTATION/START_HERE/README_ANALYSIS_WORKFLOW.md`

---

**Welcome to your organized analysis workspace. Everything you need is here and properly organized. Begin whenever you're ready!**
