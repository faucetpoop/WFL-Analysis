# Descriptive Report Package - Long Biên Food Environment Survey

**Generated**: 2025-11-23
**Purpose**: Comprehensive descriptive analysis of Long Biên household and vendor survey data

---

## 📊 Report Overview

This package contains **three types of descriptive reports** in **two versions**:

### Version 1 (V1) - Raw Merged Data
- Uses original merged CSV files from data collection
- Baseline descriptive statistics

### Version 2 (V2) - Phase 0 Processed Data ✨ **RECOMMENDED**
- Uses cleaned Phase 0 processed datasets
- Better data quality (missing values handled)
- Standardized variable names
- Cleaner categorical labels

---

## 📁 Report Structure

### **Report A: Household Descriptive Profile**
*Who are these 214 households and how do they navigate Long Biên's food environment?*

**Tables (9 total):**
1. **Table_1A** - Demographics (Continuous): Household size, age, workers
2. **Table_1B** - Demographics (Categorical): Gender, education, ethnicity, neighborhood
3. **Table_2A** - Neighborhood Perceptions: Cleanliness, safety, reputation scores
4. **Table_2B** - Travel Times: Minutes to reach different vendor types
5. **Table_3A** - Food Expenditure: VND spending patterns
6. **Table_3B** - Food Sharing: Giving, receiving, no exchange
7. **Table_4A** - Food Groups Consumed: Prevalence of 16 food groups
8. **Table_4B** - HDDS Distribution: Dietary diversity scores
9. **Table_5** - Integrated Summary: Cross-domain overview

---

### **Report B: Vendor Landscape Profile**
*What does the external food environment look like from vendor perspective?*

**Tables (7 total):**
1. **Table_V1A** - Vendor Demographics (Continuous): Age, staff, years at location
2. **Table_V1B** - Vendor Demographics (Categorical): Gender, type, ownership, ethnicity
3. **Table_V2A** - Geographic Distribution: Vendors by neighborhood (top 20)
4. **Table_V3A** - Food Groups Sold: Product availability across 16 food groups
5. **Table_V3B** - Product Diversity: Number of food groups per vendor
6. **Table_V4A** - Whole vs Processed: Product processing patterns
7. **Table_V5** - Integrated Summary: Cross-domain vendor overview

---

### **Report C: Integrated Narrative**
*The data journey from vendors → households → diets*

**Document**: `INTEGRATED_NARRATIVE_REPORT_v2.md` (Markdown)

**Structure:**
- **Part 1**: The Food Landscape (Vendor Data) - What's available?
- **Part 2**: Household Navigation (Household Data) - How do households respond?
- **Part 3**: Dietary Outcomes (HDDS Analysis) - What do they eat?
- **Part 4**: Key Patterns & Insights - Integrated findings

**Additional Table:**
- **Table_INTEGRATED_Summary_Comparison** - Side-by-side vendor vs household metrics

---

## 🎯 Key Findings Snapshot (from V2 data)

### Household Sample (N=214)
- **Mean household size**: 4.5 ± 2.2 members
- **Neighborhood safety perception**: 1.66 ± 0.78 (scale: -2 to +2)
- **Median food expenditure**: 110,000 VND (IQR: 200 - 3,000,000)
- **Mean HDDS**: 0.89 ± 2.48 food groups

### Vendor Sample (N=284)
- **Mean vendor age**: 49.9 ± 29.6 years
- **Geographic coverage**: 55 neighborhoods
- **Mean product diversity**: 3.55 ± 3.14 food groups/vendor
- **Product processing**: 53.9% processed vs 46.1% whole foods
- **Most common vendor type**: Food truck (20.4%)

### Travel Accessibility
- **Wet Market**: 5.9 min average (most accessible)
- **Food Truck**: 12.7 min average
- **Street Vendor**: 10.2 min average
- **Supermarket**: 7.1 min average
- **Convenience Store**: 7.6 min average
- **Restaurant**: 6.5 min average

---

## 📖 How to Use These Reports

### For Thesis Writing

**Methods Chapter:**
- Use **Table_1A** and **Table_1B** for sample description
- Reference **Table_V1A** and **Table_V1B** for vendor characteristics

**Results Chapter:**
- Use **Table_2A-2B** for accessibility/neighborhood findings
- Use **Table_4A-4B** for dietary diversity results
- Use **Table_V3A-3B** for product availability patterns

**Discussion Chapter:**
- Reference **Integrated Narrative Report** for synthesis
- Use **Table_INTEGRATED_Summary_Comparison** for vendor-household alignment

### For Presentations

**Slide Deck:**
- **Table_5** and **Table_V5**: One-slide summary statistics
- **Table_INTEGRATED_Summary_Comparison**: Comparing supply and demand
- Extract key numbers from narrative report

### For Supplementary Materials

**Appendices:**
- Full **Table_1B** (all neighborhoods) for geographic detail
- **Table_4A** and **Table_V3A** for complete food group prevalence

---

## 🔧 Technical Notes

### Data Sources

**V1 Reports:**
```
/Resources/Datasets/DataLongBien2024/household_survey_LONG_BIEN_2024_ALL_merged.csv
/Resources/Datasets/DataLongBien2024/vendor_survey_LONG_BIEN_2024_ALL_merged.csv
```

**V2 Reports (Recommended):**
```
/02_outputs/datasets/phase_0_household_processed.csv
/02_outputs/datasets/phase_0_vendor_processed.csv
```

### Scripts

All reports are reproducible via Python scripts in `01_scripts/`:
- `descriptive_report_households_v2_phase0.py`
- `descriptive_report_vendors_v2_phase0.py`
- `descriptive_report_integrated_narrative_v2_phase0.py`

To regenerate:
```bash
python3 01_scripts/descriptive_report_households_v2_phase0.py
python3 01_scripts/descriptive_report_vendors_v2_phase0.py
python3 01_scripts/descriptive_report_integrated_narrative_v2_phase0.py
```

---

## 📊 V2 Improvements Over V1

✅ **Better Data Quality**
- Phase 0 processing handled missing values systematically
- Variable type conversions performed correctly

✅ **Cleaner Labels**
- Vendor types: "Wet Market" instead of "Vendor Type 2"
- Food groups: "Spices Cond Bev" instead of "spices_cond_bev"
- Standardized neighborhood names (title case)

✅ **Better Formatting**
- Currency formatted with commas: "110,000 VND"
- Improved table headers and descriptions

✅ **More Accurate**
- Uses data that has been validated in Phase 0
- Consistent with operationalization master

---

## 🎓 Theoretical Alignment

These descriptive reports map to Turner et al. (2018) food environment framework:

### External Domain (Vendor Data)
- **Availability**: Table_V3A (food groups sold)
- **Prices**: Not directly captured (future enhancement)
- **Vendor Quality**: Table_V4A (whole vs processed)
- **Marketing/Regulation**: Not directly captured

### Personal Domain (Household Data)
- **Accessibility**: Table_2B (travel times)
- **Affordability**: Table_3A (food expenditure)
- **Convenience**: Implicit in travel time data
- **Desirability**: Not directly captured

### Outcomes
- **Dietary Diversity**: Table_4B (HDDS scores)

---

## 📝 Citation Suggestion

When referencing these descriptive statistics in your thesis:

> "Household survey respondents (N=214) reported a mean household size of 4.5 members (SD=2.2)
> and median food expenditure of 110,000 VND (IQR: 200-3,000,000 VND). Vendor survey data (N=284)
> revealed an average product diversity of 3.55 food groups per vendor (SD=3.14) across 55 neighborhoods
> in Long Biên District. Detailed descriptive statistics are provided in Appendix X."

---

## 🔄 Version History

**V1 (2025-11-23 Initial):**
- Generated from raw merged survey data
- 17 tables + 1 narrative report

**V2 (2025-11-23 Phase 0):**
- Regenerated using Phase 0 processed data
- 17 tables + 1 narrative report (improved quality)
- Added vendor type labels and cleaner formatting

---

## 📧 Questions?

For questions about:
- **Data sources**: See `/DOCUMENTATION/REFERENCE/DATA_INVENTORY_AND_SETUP.md`
- **Variables**: See `/DOCUMENTATION/REFERENCE/OPERATIONALIZATION_MASTER_AI_OPTIMIZED.md`
- **Methods**: See `/DOCUMENTATION/GUIDES/Data_Analysis_Workflow_Complete.md`

---

**Last Updated**: 2025-11-23
**Status**: ✅ Complete - Ready for thesis integration
