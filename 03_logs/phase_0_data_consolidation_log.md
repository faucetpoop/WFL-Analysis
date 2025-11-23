---
title: "Phase 0: Data Consolidation Log"
date: 2025-11-23
duration: 0.1 seconds
---

# Phase 0 Data Consolidation Log

**Start Time**: 2025-11-23 16:57:59
**End Time**: 2025-11-23 16:57:59
**Duration**: 0.1 seconds

## Execution Log

```
[16:57:59] INFO: ======================================================================
[16:57:59] INFO: PHASE 0: SETUP & DATA CONSOLIDATION
[16:57:59] INFO: ======================================================================
[16:57:59] INFO: 
[16:57:59] INFO: STEP 1: Loading data files...
[16:57:59] INFO: 
[16:57:59] INFO: Loading household survey data...
[16:57:59] INFO:    File: /Users/emersonrburke/Desktop/working/working_thesis_211125/WFL-Analysis/00_inputs/data/household_survey_LONG_BIEN_2024_ALL_merged.csv
[16:57:59] INFO:    ✅ Loaded 214 rows, 365 columns
[16:57:59] INFO: Loading vendor survey data...
[16:57:59] INFO:    File: /Users/emersonrburke/Desktop/working/working_thesis_211125/WFL-Analysis/00_inputs/data/vendor_survey_LONG_BIEN_2024_ALL_merged.csv
[16:57:59] INFO:    ✅ Loaded 284 rows, 132 columns
[16:57:59] INFO: 
[16:57:59] INFO: ✅ STEP 1 COMPLETE: Data loading successful
[16:57:59] INFO: 
[16:57:59] INFO: STEP 2: Verifying sample sizes...
[16:57:59] INFO: 
[16:57:59] WARNING:    ⚠️  Household sample size: 214 (expected 241)
[16:57:59] INFO:    ✅ Vendor sample size: 284 (matches expected 284)
[16:57:59] WARNING: ⚠️  WARNING: Sample size mismatch detected
[16:57:59] INFO: 
[16:57:59] INFO: ✅ STEP 2 COMPLETE: Sample size verification done
[16:57:59] INFO: 
[16:57:59] INFO: STEP 3: Critical variable renaming...
[16:57:59] INFO: 
[16:57:59] INFO: 🚨 CRITICAL: Renaming household variables to avoid conflicts...
[16:57:59] INFO:    Found 0 consumption columns to rename
[16:57:59] INFO:    'foodgroups' sales string present: True
[16:57:59] INFO:       foodgroups → hh_sales_string
[16:57:59] INFO:    ✅ Renamed 1 variables
[16:57:59] INFO:    ✅ No naming conflicts remain
[16:57:59] INFO: 
[16:57:59] INFO: ✅ STEP 3 COMPLETE: Variable renaming successful
[16:57:59] INFO: 
[16:57:59] INFO: STEP 4: Data quality assessment...
[16:57:59] INFO: 
[16:57:59] INFO: --- Household Data Quality ---
[16:57:59] INFO: Assessing missing data for Household...
[16:57:59] INFO:    ⚠️  345 variables with >10% missing data
[16:57:59] INFO:       GI_I_THI_U_Xin_ch_o_l_i_n_i_c_a_b_n_ch_a: 100.0%
[16:57:59] INFO:       _validation_status: 100.0%
[16:57:59] INFO:       B_n_ng_hay_kh_ng_h_n_i_b_n_ang_s_ng: 100.0%
[16:57:59] INFO:       B_n_s_ng_y_v_i_t_ho_t_ng_n_ng_nghi_p: 100.0%
[16:57:59] INFO:       Kh_ng_c_ph_p_D_ng_a_ra_l_do_t_ch_i: 100.0%
[16:57:59] INFO:       B_n_s_ng_y_v_i_t_o_ho_t_ng_b_n_h_ng: 100.0%
[16:57:59] INFO:       B_n_ng_hay_kh_ng_n_th_c_ph_m_c_a_b_n: 100.0%
[16:57:59] INFO:       housingtype_other: 100.0%
[16:57:59] INFO:       reason_005_other: 100.0%
[16:57:59] INFO:       reason_008_other: 100.0%
[16:57:59] INFO: Checking data types for Household...
[16:57:59] INFO:    float64: 257 columns
[16:57:59] INFO:    object: 104 columns
[16:57:59] INFO:    int64: 4 columns
[16:57:59] INFO: Checking for duplicates in Household...
[16:57:59] INFO:    ✅ No duplicate rows
[16:57:59] INFO: 
[16:57:59] INFO: --- Vendor Data Quality ---
[16:57:59] INFO: Assessing missing data for Vendor...
[16:57:59] INFO:    ⚠️  114 variables with >10% missing data
[16:57:59] INFO:       GI_I_THI_U_Xin_ch_o_l_i_n_i_c_a_b_n_ch_a: 100.0%
[16:57:59] INFO:       resp_ethn_other: 100.0%
[16:57:59] INFO:       Thank_you_very_much_a_very_pleasant_day: 100.0%
[16:57:59] INFO:       Now_please_think_of_Typhoon_event_Yagi: 100.0%
[16:57:59] INFO:       Do_you_agree_or_disa_following_statements: 100.0%
[16:57:59] INFO:       No_permission_Stop_terwards_if_relevant: 100.0%
[16:57:59] INFO:       INTRODUCTION_Hello_bal_informed_consent: 100.0%
[16:57:59] INFO:       _tags: 100.0%
[16:57:59] INFO:       _notes: 100.0%
[16:57:59] INFO:       _validation_status: 100.0%
[16:57:59] INFO: Checking data types for Vendor...
[16:57:59] INFO:    float64: 98 columns
[16:57:59] INFO:    object: 32 columns
[16:57:59] INFO:    int64: 2 columns
[16:57:59] INFO: Checking for duplicates in Vendor...
[16:57:59] INFO:    ✅ No duplicate rows
[16:57:59] INFO: 
[16:57:59] INFO: ✅ STEP 4 COMPLETE: Data quality assessment done
[16:57:59] INFO: 
[16:57:59] INFO: STEP 5: Saving processed datasets...
[16:57:59] INFO: 
[16:57:59] INFO: Saving processed Household...
[16:57:59] INFO:    Output: /Users/emersonrburke/Desktop/working/working_thesis_211125/WFL-Analysis/02_outputs/datasets/phase_0_household_processed.csv
[16:57:59] INFO:    ✅ Saved 214 rows, 365 columns
[16:57:59] INFO:    ✅ File size: 334.3 KB
[16:57:59] INFO: Saving processed Vendor...
[16:57:59] INFO:    Output: /Users/emersonrburke/Desktop/working/working_thesis_211125/WFL-Analysis/02_outputs/datasets/phase_0_vendor_processed.csv
[16:57:59] INFO:    ✅ Saved 284 rows, 132 columns
[16:57:59] INFO:    ✅ File size: 250.5 KB
[16:57:59] INFO: 
[16:57:59] INFO: ✅ STEP 5 COMPLETE: Processed datasets saved
[16:57:59] INFO: 
[16:57:59] INFO: ======================================================================
[16:57:59] INFO: PHASE 0 COMPLETE: DATA CONSOLIDATION SUCCESSFUL
[16:57:59] INFO: ======================================================================
[16:57:59] INFO: 
[16:57:59] INFO: Summary:
[16:57:59] INFO:   • Household records: 214
[16:57:59] INFO:   • Vendor records: 284
[16:57:59] INFO:   • Household variables: 365
[16:57:59] INFO:   • Vendor variables: 132
[16:57:59] INFO: 
[16:57:59] INFO: Output Files:
[16:57:59] INFO:   • /Users/emersonrburke/Desktop/working/working_thesis_211125/WFL-Analysis/02_outputs/datasets/phase_0_household_processed.csv
[16:57:59] INFO:   • /Users/emersonrburke/Desktop/working/working_thesis_211125/WFL-Analysis/02_outputs/datasets/phase_0_vendor_processed.csv
[16:57:59] INFO: 
[16:57:59] INFO: Next Steps:
[16:57:59] INFO:   1. Review Phase 0 log file
[16:57:59] INFO:   2. Verify processed datasets
[16:57:59] INFO:   3. Proceed to Phase 1: Data Cleaning & Variable Specification
[16:57:59] INFO: 
```
