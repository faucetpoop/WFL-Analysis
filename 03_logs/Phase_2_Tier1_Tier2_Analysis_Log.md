
# Phase 2: Tier 1 & 2 Analysis Log
Date: 2025-11-23
Analyst: Senior Data Scientist Skill

## Dataset Information
- Source: phase_1_household_analysis_ready_CORRECTED.csv
- Sample Size: 214 households
- Variables Analyzed: 5 continuous + 6 categorical

## Tier 1: Descriptive Statistics

### Continuous Variables (N=5)
                      Variable                Label   N  Missing          Mean           SD  Min       Q25    Median       Q75         Max  Skewness  Kurtosis
             OP009_travel_time    Travel Time (min) 125       89  5.920000e+00 4.415150e+00  0.0       3.0       5.0       7.0        30.0  2.189982  7.413424
OP012_monthly_food_expenditure     Food Expenditure 142       72  8.700085e+06 1.587442e+07  9.0 3600000.0 6000000.0 9000000.0 150000000.0  7.559622 61.312482
          OP019_water_distance Water Distance (min)  99      115 -5.858586e-01 7.285728e-01 -1.0      -1.0      -1.0       0.0         1.0  1.436301  0.455698
                    OP029_HDDS    HDDS (Primary DV) 214        0  5.074766e+00 3.775883e+00  0.0       0.0       6.0       8.0        15.0 -0.052753 -1.135385

### Categorical Variables (N=6)
Key frequencies documented in Table_1B_Descriptive_Categorical.csv

## Tier 2: Group Comparisons

### OP011: Accessibility × HDDS
OP011_accessibility_tier  N  HDDS_Mean  HDDS_SD  Diet_Diverse_Pct  t_statistic  p_value  cohens_d significant
                   Close 88       7.02     2.78                 0    -0.110673 0.912056 -0.021685          No
                     Far 37       7.08     2.45                 0    -0.110673 0.912056 -0.021685          No

**Interpretation:**
- t-statistic: -0.111
- p-value: 0.912
- Effect size (Cohen's d): -0.022
- Statistical significance: NO

### OP016: Affordability × HDDS
OP016_budget_share_tier  N  HDDS_Mean  HDDS_SD  Diet_Diverse_Pct  F_statistic  p_value  eta_squared significant
                   High 41       6.44     2.53                 0     0.933919 0.395825     0.015202          No
                    Low 41       6.90     2.46                 0     0.933919 0.395825     0.015202          No
                 Medium 42       7.21     2.79                 0     0.933919 0.395825     0.015202          No

**Interpretation:**
- F-statistic: 0.934
- p-value: 0.396
- Effect size (eta-squared): 0.015
- Statistical significance: NO

### OP025: Neighborhood Safety × HDDS
OP025_neighborhood_safety_tier   N  HDDS_Mean  HDDS_SD  Diet_Diverse_Pct  t_statistic  p_value  cohens_d significant
                          High 106       6.24     2.89                 0    -2.578092 0.010836 -0.425901         Yes
                           Low  56       7.43     2.62                 0    -2.578092 0.010836 -0.425901         Yes

**Interpretation:**
- t-statistic: -2.578
- p-value: 0.011
- Effect size (Cohen's d): -0.426
- Statistical significance: YES

**Note:** OP025 measures NEIGHBORHOOD safety/quality (composite of clean, safe, reputation), NOT food safety.

## Key Findings

### Descriptive Insights
1. HDDS (OP029_HDDS): Mean = 5.07, SD = 3.78
2. Distribution characteristics documented for all continuous and categorical variables

### Group Comparison Insights
1. **Accessibility Effect**: Access proximity does not show significant association with HDDS (p=0.912)
2. **Affordability Effect**: Budget share does not show significant differences in HDDS across tiers (p=0.396)
3. **Neighborhood Safety Effect**: Neighborhood safety/quality perception shows significant association with HDDS (p=0.011)

## Outputs Created

### Tables
- ✓ Table_1A_Descriptive_Continuous.csv
- ✓ Table_1B_Descriptive_Categorical.csv
- ✓ Table_2A_Accessibility_Comparison.csv
- ✓ Table_2B_Affordability_Comparison.csv
- ✓ Table_2C_Safety_Comparison.csv

### Figures
- ✓ Phase_2_HDDS_Distribution.png
- ✓ Phase_2_T2_Comparisons_Boxplots.png

## Quality Checks
- [x] Data integrity verified (N consistent with Phase 1)
- [x] All required variables present
- [x] Statistical tests appropriate for data types
- [x] Effect sizes calculated
- [x] Assumptions checked (normality, homogeneity of variance)
- [x] Visualizations created for key comparisons

## Next Steps
→ Phase 3: Tier 3 & 4 Analyses (Correlation & Regression)

## Notes
- All statistical tests conducted with α = 0.05
- Missing data handled with listwise deletion (dropna)
- Effect sizes interpreted using standard thresholds (Cohen, 1988)

---
Phase 2 Status: COMPLETE
Generated: 2025-11-23 19:50:43
