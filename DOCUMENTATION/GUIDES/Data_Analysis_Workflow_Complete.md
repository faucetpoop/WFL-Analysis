---
title: "WFL-Analysis: Complete Data Analysis Workflow"
subtitle: "Household Dietary Diversity & Turner Framework Analysis"
type: "workflow"
category: "thesis_data_analysis"
status: "active"
priority: "critical"
version: 2
last_updated: "2025-11-23"
linked_documents:
  - "submitted_methodology"
  - "supervisor_feedback_methods"
  - "all_data_sheets"
  - "Turner_framework_specification"
---

## Executive Summary

This is your definitive, executable guide for analyzing Household Dietary Diversity Score (HDDS) against Turner's Food Environment Determinants Framework. This document merges:
- **Structural rigor**: Phase-based workflow ensuring nothing is missed
- **Project specificity**: Exact variable names, sample sizes, statistical tests, and data preparation steps
- **Deadline awareness**: Clear labeling of essential vs. optional analyses

**Key Context:**
- Total Sample: n=214 households (102 with food waste module + 139 without)
- Outcome: HDDS (Household Dietary Diversity Score, count 0-12)
- Framework: Turner's 5 domains (Availability, Prices, Accessibility, Affordability, Desirability)
- Critical Issue: Two distinct "foodgroups" variables—you must rename them on load to avoid conflict
- Analysis Tiers: Descriptive (Tier 1) → Bivariate (Tier 2) → Correlation (Tier 3) → Regression (Tier 4)

---

## 1. Goal (What This Workflow Is For)

Execute a **clean, defensible, deadline-aware** analysis workflow that:

- Aligns submitted methodology with **supervisor feedback** and **actual data structure**.
- Produces exact step-by-step instructions you can literally execute.
- Identifies which analyses are **essential** (non-negotiable) vs. **should-do** vs. **nice-to-have**.
- Maintains **transparency**: every decision, variable transformation, and test is documented.
- Integrates results directly into thesis chapters.

---

## 2. Inputs (What You Must Have Ready)

Ensure the following files/documents are accessible before starting:

- [ ] Latest **submitted methodology** (research questions, hypotheses, analysis plan)
- [ ] **Supervisor feedback** on methods/analysis approach
- [ ] All **final data files**:
  - `Household_survey_..._withFoodWaste.csv` (n=102)
  - `Household_survey_..._withoutFoodWaste.csv` (n=139)
  - `Vendor_survey_..._withFoodWaste.csv` (n=284 total)
  - `Vendor_survey_..._withoutFoodWaste.csv`
  - KML files for geospatial households and vendors
- [ ] Any **coding manuals, data dictionaries**, or survey documentation
- [ ] **Turner framework reference** (domain definitions, expected relationships)

---

## 3. Constraints & Reality Check

- **Time-sensitive**: Focus on minimum viable analysis that answers core research questions.
- **Data-bound**: Previous errors must not repeat—every variable must be explicitly mapped.
- **Supervisor alignment**: All analyses must match methodology and address feedback.
- **Transparency imperative**: Every step is documented; variables are traceable.

---

## 4. Workflow Overview (Phases)

1. **Phase 0** – Setup & Data Consolidation
2. **Phase 1** – Data Cleaning & Variable Specification
3. **Phase 2** – Tier 1 & 2 Analyses (Descriptive & Bivariate)
4. **Phase 3** – Tier 3 & 4 Analyses (Correlation & Regression)
5. **Phase 4** – Outputs & Thesis Integration
6. **Phase 5** – Minimal Viable Completion Checklist
7. **Phase 6** – Progress Tracking

---

## PHASE 0: Setup & Data Consolidation

### Objective
Create unified datasets from multiple raw files, with careful attention to column naming conflicts.

### 0.1 Create Project Folder Structure

```
analysis_rebuild/
├── 00_inputs/
│   ├── household_survey_withFoodWaste.csv
│   ├── household_survey_withoutFoodWaste.csv
│   ├── vendor_survey_withFoodWaste.csv
│   ├── vendor_survey_withoutFoodWaste.csv
│   ├── KML_files/ (geospatial data)
│   └── methodology_summary.md
├── 01_scripts/
│   ├── 01_load_and_consolidate.R (or .py)
│   ├── 02_cleaning_and_spec.R
│   ├── 03_tier1_tier2_analyses.R
│   ├── 04_tier3_tier4_analyses.R
│   └── README_scripts.md
├── 02_outputs/
│   ├── tables/
│   ├── figures/
│   └── datasets/ (cleaned, analysis-ready)
├── 03_logs/
│   ├── data_decisions.md
│   ├── variable_mapping.md
│   ├── cleaning_decisions.md
│   └── analysis_notes.md
└── README.md (project overview)
```

### 0.2 Write Project README

In `analysis_rebuild/README.md`, document:

- Date of workflow rebuild
- Reason for rebuild (previous version scrapped, clearer specifications)
- Tools used (R with dplyr, readr, sf OR Python with pandas, geopandas)
- High-level project goal (HDDS analysis against Turner framework)
- Key contacts/supervisors

### 0.3 Load & Consolidate Data with Critical Renaming

**CRITICAL ISSUE**: The `foodgroups` column appears in multiple forms. You must rename on load to avoid conflict.

**Software Recommendation**: Use **R** (with `dplyr`, `readr`, `sf`) or **Python** (with `pandas`, `geopandas`).

#### Step 0.3.1: Load and Stack Household Survey Data

```r
# R Example
library(dplyr)
library(readr)

# Load household with food waste module (n=102)
hh_with_fw <- read_csv("00_inputs/household_survey_withFoodWaste.csv") %>%
  mutate(has_foodwaste_module = TRUE)

# Load household without food waste module (n=139)
hh_without_fw <- read_csv("00_inputs/household_survey_withoutFoodWaste.csv") %>%
  mutate(has_foodwaste_module = FALSE)

# CRITICAL RENAMING:
# - foodgroups_001_* columns (consumption data) → rename to hh_consumption_*
# - foodgroups (string column, household sales) → rename to hh_sales_string

hh_with_fw <- hh_with_fw %>%
  rename_with(~gsub("foodgroups_001_", "hh_consumption_", .x),
              starts_with("foodgroups_001_")) %>%
  rename(hh_sales_string = foodgroups)

hh_without_fw <- hh_without_fw %>%
  rename_with(~gsub("foodgroups_001_", "hh_consumption_", .x),
              starts_with("foodgroups_001_")) %>%
  rename(hh_sales_string = foodgroups)

# Stack into single household dataset
household_df <- bind_rows(hh_with_fw, hh_without_fw)  # n=214
```

#### Step 0.3.2: Load and Stack Vendor Survey Data

```r
# Load vendor with food waste module
vendor_with_fw <- read_csv("00_inputs/vendor_survey_withFoodWaste.csv") %>%
  mutate(has_foodwaste_module = TRUE)

# Load vendor without food waste module
vendor_without_fw <- read_csv("00_inputs/vendor_survey_withoutFoodWaste.csv") %>%
  mutate(has_foodwaste_module = FALSE)

# CRITICAL RENAMING:
# - foodgroups (string column, vendor sales) → rename to vendor_sales_string

vendor_with_fw <- vendor_with_fw %>%
  rename(vendor_sales_string = foodgroups)

vendor_without_fw <- vendor_without_fw %>%
  rename(vendor_sales_string = foodgroups)

# Stack into single vendor dataset
vendor_df <- bind_rows(vendor_with_fw, vendor_without_fw)  # n=284
```

#### Step 0.3.3: Load Geospatial Data

```r
library(sf)

# Load household locations (KML → GeoDataFrame)
gdf_households <- st_read("00_inputs/KML_files/households.kml") %>%
  st_transform(crs = 32648)  # UTM Zone 48N for Hanoi (distance in meters)

# Load vendor locations (KML → GeoDataFrame)
gdf_vendors <- st_read("00_inputs/KML_files/vendors.kml") %>%
  st_transform(crs = 32648)  # UTM Zone 48N

# Ensure n matches: gdf_households should have 214 features, gdf_vendors should have 284
```

#### Step 0.3.4: Create Key Identifier

```r
# In household_df, create a binary column to flag food waste module presence
# This is ESSENTIAL for correctly filtering affordability variables

household_df <- household_df %>%
  mutate(has_foodwaste_module = as.logical(has_foodwaste_module))
```

### 0.4 Save Consolidated Data

```r
# Save cleaned consolidated datasets (checkpoint)
write_csv(household_df, "02_outputs/datasets/household_df_consolidated.csv")
write_csv(vendor_df, "02_outputs/datasets/vendor_df_consolidated.csv")

# Save geospatial data
st_write(gdf_households, "02_outputs/datasets/gdf_households.gpkg")
st_write(gdf_vendors, "02_outputs/datasets/gdf_vendors.gpkg")
```

**Status**: ✅ Phase 0 complete when you have three clean, consolidated datasets with correct sample sizes:
- `household_df` (n=214)
- `vendor_df` (n=284)
- Geospatial datasets with UTM projection

---

## PHASE 1: Data Cleaning & Variable Specification

### Objective
Define exactly how raw data becomes analysis-ready. Operationalize all variables from your methodology using Turner's framework structure.

### 1.1 Methodology Summary

**Document location**: `03_logs/methodology_summary.md`

From your submitted methodology, extract and list:

- [ ] **Research Questions / Hypotheses** (RQ1, RQ2, etc.)
- [ ] **Outcome Variable**: HDDS (Household Dietary Diversity Score)
- [ ] **Framework Determinants** (5 domains from Turner):
  1. **Availability** (neighborhood vendor diversity)
  2. **Prices** (proxy: motivation by price)
  3. **Accessibility** (distance to markets, travel time)
  4. **Affordability** (income category, food expenditure)
  5. **Desirability** (vendor cleanliness, safety, reputation)

### 1.2 Data Cleaning Rules

Create a file `03_logs/cleaning_decisions.md` documenting:

- [ ] **Missing values**:
  - For HDDS: Use `rowSums(..., na.rm=FALSE)` — if ANY consumption item is missing, HDDS = NA.
  - For other variables: Document rule per variable (e.g., "drop if >50% missing", "mean imputation", "exclude from analysis").

- [ ] **Invalid/out-of-range values**:
  - Check Likert scales (1–5), counts (≥0), percentages (0–100).
  - Flag and document any values outside expected ranges.

- [ ] **Duplicates**: Check household/vendor ID for exact duplicates. Document any found.

- [ ] **Outliers**: Decide per analysis whether to keep, transform, or exclude (document in analysis-specific notes).

### 1.3 Variable Specification Table

Create `03_logs/variable_mapping.md` with this structure:

| Domain | Variable Name | Data Type | Role | Source File/Column | Sample Size | Coding/Transformation | Notes |
|--------|---------------|-----------|------|-------------------|-------------|----------------------|-------|
| **Outcome** | HDDS | Count (0-12) | DV | household_df, hh_consumption_* | n=214 | rowSums(hh_consumption_*) | All 12 consumption items |
| **Availability** | neighborhood_mean_availability | Continuous | IV | vendor_df + aggregation | n=214 | Parse vendor_sales_string, count unique groups, aggregate by neighborhood | Spatial join to households |
| **Availability (Sub)** | hh_sales_food_diversity | Count (0-12) | IV | household_df, hh_sales_string | n=34 | Parse hh_sales_string for household-vendors only | Sub-analysis: household-vendors |
| **Prices** | motive_cheap | Binary (0/1) | IV | household_df, reason_* | n=214 | 1 if any reason_* mentions price | Proxy for price sensitivity |
| **Vendor Quality** | neighborhood_mean_quality | Continuous | IV | vendor_df | n=214 | z-score standardize: safe_reputation, infrastructure, inverse(flooding), aggregate by neighborhood | Quality index |
| **Accessibility (GIS)** | dist_to_nearest_market | Continuous (meters) | IV | gdf_households, gdf_vendors | n=214 | Calculate distance from each household to nearest vendor point | Uses UTM projection |
| **Accessibility (Survey)** | time_to_market | Continuous (minutes) | IV | household_df, time_001-007 | n=214 | Use survey response or mean of time_* | Proxy from survey |
| **Affordability (Income)** | income_categorical | Ordinal Factor | IV | household_df, income | n=92 | Recode income, filter has_foodwaste_module==FALSE | Sub-sample: only with affordability module |
| **Affordability (Expenditure)** | foodexp_monthly | Continuous | IV | household_df, foodexpenditure, foodexp_timeunit | n=64 | Parse text, convert to monthly, standardize | Sub-sample: only with complete data |
| **Convenience** | motive_close | Binary (0/1) | IV | household_df, reason_* | n=214 | 1 if any reason_* mentions proximity | Proxy for convenience |
| **Desirability** | Desirability_Index | Continuous | IV | household_df | n=214 | z-score standardize & sum: clean, safe, reputation columns | Household perception index |

### 1.4 Construct Core Variables

#### Outcome: HDDS

```r
household_df <- household_df %>%
  mutate(
    HDDS = rowSums(select(., starts_with("hh_consumption_")), na.rm = FALSE)
  )

# Check: HDDS should range 0-12 for non-missing cases
summary(household_df$HDDS)
```

#### External Domain: Availability (Neighborhood)

```r
# Step 1: Parse vendor_sales_string to get vendor food diversity
vendor_df <- vendor_df %>%
  mutate(
    vendor_food_diversity = str_count(vendor_sales_string, ",") + 1  # count of food groups
  )

# Step 2: Spatially join vendors to neighborhoods (or aggregate by neighborhood column if exists)
# Assume you have a neighborhood_id column in both vendor_df and household_df
vendor_agg <- vendor_df %>%
  group_by(neighborhood_id) %>%
  summarise(
    neighborhood_mean_availability = mean(vendor_food_diversity, na.rm = TRUE)
  )

# Step 3: Join back to household_df
household_df <- household_df %>%
  left_join(vendor_agg, by = "neighborhood_id")
```

#### External Domain: Vendor Quality

```r
vendor_df <- vendor_df %>%
  mutate(
    safe_reputation_z = scale(safe_reputation)[, 1],
    infrastructure_z = scale(infrastructure)[, 1],
    flooding_inv_z = scale(-flooding)[, 1],  # inverse: lower = better
    Vendor_Quality_Index = rowMeans(
      select(., safe_reputation_z, infrastructure_z, flooding_inv_z),
      na.rm = TRUE
    )
  )

# Aggregate to neighborhood
vendor_quality_agg <- vendor_df %>%
  group_by(neighborhood_id) %>%
  summarise(
    neighborhood_mean_quality = mean(Vendor_Quality_Index, na.rm = TRUE)
  )

household_df <- household_df %>%
  left_join(vendor_quality_agg, by = "neighborhood_id")
```

#### Personal Domain: Accessibility (GIS)

```r
library(sf)

# Calculate distance from each household to nearest vendor
household_distances <- st_nearest_feature(gdf_households, gdf_vendors)
household_df <- household_df %>%
  mutate(
    dist_to_nearest_market = as.numeric(
      st_distance(gdf_households, gdf_vendors[household_distances, ], by_element = TRUE)
    )
  )
```

#### Personal Domain: Affordability (Income)

```r
household_df <- household_df %>%
  mutate(
    income_categorical = ifelse(
      has_foodwaste_module == FALSE,
      recode_factor(income_raw,
                    "1" = "low", "2" = "medium", "3" = "high"),
      NA
    )
  )

# Check: n=92 should have income_categorical (those without food waste module)
table(is.na(household_df$income_categorical))
```

#### Personal Domain: Affordability (Expenditure)

```r
parse_foodexp <- function(text, timeunit) {
  # Simple parser: extract numeric value and convert to monthly
  value <- as.numeric(str_extract(text, "\\d+"))
  if (is.na(timeunit) || timeunit == "monthly") return(value)
  if (timeunit == "weekly") return(value * 4.33)
  if (timeunit == "yearly") return(value / 12)
  return(NA)
}

household_df <- household_df %>%
  mutate(
    foodexp_monthly = ifelse(
      has_foodwaste_module == FALSE,
      mapply(parse_foodexp, foodexpenditure, foodexp_timeunit),
      NA
    )
  )

# Check: n=64 should have foodexp_monthly (those with complete data)
```

#### Personal Domain: Convenience & Desirability

```r
household_df <- household_df %>%
  mutate(
    motive_cheap = ifelse(rowSums(select(., starts_with("reason_"))) > 0, 1, 0),
    motive_close = ifelse(str_detect(reason_text, "close|near|proximity"), 1, 0),

    # Desirability Index: z-score and average
    Desirability_Index = rowMeans(
      cbind(
        scale(clean)[, 1],
        scale(safe)[, 1],
        scale(reputation)[, 1]
      ),
      na.rm = TRUE
    )
  )
```

**Status**: ✅ Phase 1 complete when you have:
- Documented methodology summary
- Cleaning decisions logged
- Variable mapping table filled in
- All constructed variables in `household_df` and `vendor_df`
- Ready for analysis

---

## PHASE 2: Tier 1 & 2 Analyses (Descriptive & Bivariate)

### Objective
Produce descriptive statistics and bivariate tests addressing each Turner determinant. This forms the core of your results chapter.

### 2.1 Descriptive Statistics (Tier 1)

**Deliverable**: `02_outputs/tables/Table_01_Descriptive_Statistics.csv`

```r
# Full sample descriptive stats
desc_table <- household_df %>%
  summarise(
    N = n(),
    HDDS_mean = mean(HDDS, na.rm = TRUE),
    HDDS_sd = sd(HDDS, na.rm = TRUE),
    HDDS_range = paste(min(HDDS, na.rm = TRUE), "-", max(HDDS, na.rm = TRUE)),

    Availability_mean = mean(neighborhood_mean_availability, na.rm = TRUE),
    Availability_sd = sd(neighborhood_mean_availability, na.rm = TRUE),

    Quality_mean = mean(neighborhood_mean_quality, na.rm = TRUE),
    Quality_sd = sd(neighborhood_mean_quality, na.rm = TRUE),

    Distance_mean_m = mean(dist_to_nearest_market, na.rm = TRUE),
    Distance_sd_m = sd(dist_to_nearest_market, na.rm = TRUE),

    Desirability_mean = mean(Desirability_Index, na.rm = TRUE),
    Desirability_sd = sd(Desirability_Index, na.rm = TRUE)
  )

write_csv(desc_table, "02_outputs/tables/Table_01_Descriptive_Statistics.csv")
```

### 2.2 Bivariate Tests (Tier 2)

Each test below should be run, summarized, and saved to a separate table. Structure each as:

| Determinant | Variable | Test | Sample | p-value | Effect Size | Interpretation |
|-------------|----------|------|--------|---------|-------------|-----------------|

#### Test 1: Availability (Neighborhood) vs. HDDS
```r
# Spearman's rho (non-parametric)
availability_test <- cor.test(
  household_df$neighborhood_mean_availability,
  household_df$HDDS,
  method = "spearman"
)
# Result: rho, p-value, 95% CI
```

#### Test 2: Availability (Household Sales) vs. HDDS (Sub-analysis, n=34)
```r
# Spearman's rho for household-vendors only
hh_vendors <- household_df %>% filter(!is.na(hh_sales_food_diversity))
hh_sales_test <- cor.test(
  hh_vendors$hh_sales_food_diversity,
  hh_vendors$HDDS,
  method = "spearman"
)
```

#### Test 3: Price Motivation vs. HDDS
```r
# Mann-Whitney U Test (HDDS by motive_cheap)
price_test <- wilcox.test(
  household_df$HDDS ~ household_df$motive_cheap,
  exact = FALSE
)
# Also compute effect size (rank-biserial correlation)
```

#### Test 4: Vendor Quality vs. HDDS
```r
# Spearman's rho
quality_test <- cor.test(
  household_df$neighborhood_mean_quality,
  household_df$HDDS,
  method = "spearman"
)
```

#### Test 5: Distance to Market vs. HDDS
```r
# Spearman's rho
distance_test <- cor.test(
  household_df$dist_to_nearest_market,
  household_df$HDDS,
  method = "spearman"
)
```

#### Test 6: Income vs. HDDS (Sub-sample, n=92)
```r
# Kruskal-Wallis H-test (HDDS across income categories)
income_subset <- household_df %>% filter(!is.na(income_categorical))
income_test <- kruskal.test(
  income_subset$HDDS ~ income_subset$income_categorical
)
# Follow-up: Pairwise Mann-Whitney U tests with Bonferroni correction
```

#### Test 7: Food Expenditure vs. HDDS (Sub-sample, n=64)
```r
# Spearman's rho
exp_subset <- household_df %>% filter(!is.na(foodexp_monthly))
exp_test <- cor.test(
  exp_subset$foodexp_monthly,
  exp_subset$HDDS,
  method = "spearman"
)
```

#### Test 8: Convenience vs. HDDS
```r
# Mann-Whitney U Test (HDDS by motive_close)
convenience_test <- wilcox.test(
  household_df$HDDS ~ household_df$motive_close,
  exact = FALSE
)
```

#### Test 9: Desirability vs. HDDS
```r
# Spearman's rho
desirability_test <- cor.test(
  household_df$Desirability_Index,
  household_df$HDDS,
  method = "spearman"
)
```

### 2.3 Bivariate Results Table

**Deliverable**: `02_outputs/tables/Table_02_Bivariate_Tests.csv`

Compile all tests into a single results table with columns:
- Determinant Domain
- Variable Name
- Statistical Test
- Sample Size
- Test Statistic
- p-value
- Effect Size
- Interpretation (supports/refutes hypothesis?)

---

## PHASE 3: Tier 3 & 4 Analyses (Correlation Matrix & Regression)

### Objective
Integrate findings across determinants and model HDDS as a function of the full Turner framework.

### 3.1 Correlation Matrix (Tier 3)

**Deliverable**: `02_outputs/figures/Figure_01_Correlation_Heatmap.png` + `02_outputs/tables/Table_03_Correlation_Matrix.csv`

**Sample**: Use n=92 subset (those with income data—primary modeling sample)

```r
# Subset to n=92 (those with income_categorical)
modeling_sample <- household_df %>%
  filter(!is.na(income_categorical)) %>%
  select(
    HDDS,
    income_categorical,  # convert to numeric for correlation
    dist_to_nearest_market,
    Desirability_Index,
    neighborhood_mean_availability,
    neighborhood_mean_quality
  ) %>%
  mutate(
    income_numeric = as.numeric(income_categorical)  # low=1, medium=2, high=3
  )

# Spearman correlation matrix
corr_matrix <- cor(
  modeling_sample %>% select(-income_categorical),
  use = "complete.obs",
  method = "spearman"
)

# Visualize as heatmap
library(corrplot)
png("02_outputs/figures/Figure_01_Correlation_Heatmap.png", width = 800, height = 800)
corrplot(
  corr_matrix,
  method = "color",
  type = "upper",
  addCoef.col = "black",
  diag = TRUE
)
dev.off()

# Save numeric table
write_csv(as_tibble(corr_matrix, rownames = "Variable"),
          "02_outputs/tables/Table_03_Correlation_Matrix.csv")
```

### 3.2 Integrated Regression Model (Tier 4)

**Deliverable**: `02_outputs/tables/Table_04_Regression_Model.csv` + model diagnostics

**Sample**: n=92 (primary modeling sample with income data)

**Model Type**: Negative Binomial Regression (HDDS is count; allows overdispersion)

```r
library(MASS)

# Prepare modeling dataset
model_data <- household_df %>%
  filter(!is.na(income_categorical)) %>%
  select(
    HDDS,
    income_categorical,
    dist_to_nearest_market,
    Desirability_Index,
    motive_cheap,
    motive_close,
    neighborhood_mean_availability,
    neighborhood_mean_quality,
    total_household_size,
    resp_gender
  )

# Fit negative binomial model
model <- glm.nb(
  HDDS ~
    income_categorical +
    dist_to_nearest_market +
    Desirability_Index +
    motive_cheap +
    motive_close +
    neighborhood_mean_availability +
    neighborhood_mean_quality +
    total_household_size +
    resp_gender,
  data = model_data
)

# Extract results
summary(model)
coefficients(summary(model))

# Save model output
sink("02_outputs/tables/Table_04_Regression_Model.txt")
summary(model)
sink()

# Diagnostics
par(mfrow = c(2, 2))
plot(model)
dev.off()
```

**Interpretation Guidance**:
- Which determinants emerge as **strongest predictors** of HDDS?
- Which are statistically significant (p < 0.05)?
- Do results align with Turner framework expectations?
- Note any **limitations** (sample size=92, missing data on some variables).

---

## PHASE 4: Outputs & Thesis Integration

### Objective
Ensure every analysis has a clear destination in your thesis. Map outputs to chapters and sections.

### 4.1 Output Specification

Create `03_logs/output_mapping.md`:

| Analysis ID | Output Type | File Name | Thesis Chapter | Thesis Section | Status |
|-------------|------------|-----------|-----------------|-----------------|---------|
| A1 | Table | Table_01_Descriptive_Statistics.csv | Results | Sample Characteristics | ⏳ Pending |
| A2 | Table | Table_02_Bivariate_Tests.csv | Results | Determinant Associations | ⏳ Pending |
| A3 | Figure | Figure_01_Correlation_Heatmap.png | Results | Inter-determinant Relationships | ⏳ Pending |
| A4 | Table | Table_04_Regression_Model.txt | Results / Discussion | Integrated Framework Model | ⏳ Pending |

### 4.2 Thesis Section Alignment

For each major result:

- **Results Chapter**:
  - Descriptive stats (Table 01)
  - Bivariate tests by determinant (Table 02)
  - Correlation matrix visualization (Figure 01)
  - Regression model (Table 04)

- **Discussion Chapter**:
  - Interpret which determinants matter most
  - Address supervisor feedback on methodology
  - Discuss limitations (sample size, missing data, sub-analyses)
  - Synthesize findings against Turner framework

- **Appendices**:
  - Full variable specification table
  - Cleaning decisions log
  - R/Python script code
  - Raw correlation matrix numbers

---

## PHASE 5: Minimal Viable Completion Checklist

**If time gets tight, complete these in order. Do not skip.**

### Essential (MUST_DO)

- [ ] **Phase 0**: Data consolidation + renaming
  - Consolidated household_df (n=214), vendor_df (n=284)
  - No column naming conflicts
  - Geospatial data loaded and projected

- [ ] **Phase 1**: Variable specification
  - Methodology summary documented
  - Variable mapping table complete
  - All constructed variables computed (HDDS, availability, income, etc.)

- [ ] **Tier 2 Core**: Bivariate tests for RQ1 & RQ2
  - [ ] If RQ1 = Availability → availability_test (Test 1)
  - [ ] If RQ2 = Affordability → income_test (Test 6) + exp_test (Test 7)
  - [ ] Save results to Table_02_Bivariate_Tests.csv

- [ ] **Descriptive Statistics**
  - [ ] Table_01_Descriptive_Statistics complete
  - [ ] Describes full sample (n=214) and sub-samples (n=92, n=34 as needed)

- [ ] **Results Write-Up**
  - [ ] Methodology section finalized
  - [ ] Results section with tables/figures
  - [ ] Brief discussion of findings

### Should-Do (SHOULD_DO)

- [ ] **Tier 3**: Correlation matrix (Figure 01, Table 03)
- [ ] **Tier 4**: Regression model (Table 04)
- [ ] Full Discussion chapter integrating all findings
- [ ] Supervisor feedback addressed in final draft

### Nice-to-Have (NICE_TO_HAVE)

- [ ] Additional robustness checks (e.g., sub-group analyses)
- [ ] Sensitivity analyses (e.g., excluding outliers)
- [ ] Extended exploratory analyses beyond core RQs

---

## PHASE 6: Progress Tracking

### Quick Log Format

Keep a running log in `03_logs/progress_log.md`:

```
## 2025-11-23

- [2025-11-23 09:00] Started Phase 0: Data consolidation
- [2025-11-23 10:30] Loaded and renamed household_df, vendor_df
- [2025-11-23 11:15] Loaded geospatial data, verified n
- [2025-11-23 12:00] **CHECKPOINT**: Phase 0 complete

## 2025-11-24

- [2025-11-24 09:00] Phase 1: Began variable specification
- [2025-11-24 10:00] Constructed HDDS, availability, income variables
- [2025-11-24 11:30] **CHECKPOINT**: Phase 1 complete
- [2025-11-24 13:00] Phase 2: Running bivariate tests
- [2025-11-24 14:30] Completed all Tier 2 tests, saved Table_02
- [2025-11-24 15:00] **CHECKPOINT**: Phase 2 complete

## 2025-11-25

- [2025-11-25 10:00] Phase 3: Correlation matrix and regression
- [2025-11-25 11:00] **CHECKPOINT**: Correlation matrix complete
- [2025-11-25 13:00] Regression model fit, diagnostics checked
- [2025-11-25 14:00] **CHECKPOINT**: Phase 3 complete

## 2025-11-26

- [2025-11-26 09:00] Phase 4: Outputs mapping
- [2025-11-26 10:00] Thesis integration outline prepared
- [2025-11-26 15:00] **PROJECT COMPLETE**
```

### Metrics to Track

- **Phases completed**: 0, 1, 2, 3, 4, 5, 6
- **Tests run**: Tier 1 (descriptive), Tier 2 (bivariate), Tier 3 (correlation), Tier 4 (regression)
- **Sample sizes verified**: n=214, n=92, n=34, n=64
- **Sub-analyses completed**: household-vendors, income subset, expenditure subset
- **Supervisor feedback integrated**: Yes/No
- **Thesis sections written**: Results, Discussion, Appendices

---

## Key Decision Summary

| Decision Point | Your Choice | Rationale | Status |
|---|---|---|---|
| Software | R / Python | Both work; R more familiar for stats | ⏳ Choose |
| Outlier handling | Keep / Transform / Exclude | Decide per analysis | ⏳ Decide |
| Missing data rule | Listwise / Imputation / Other | Document in Phase 1 | ⏳ Decide |
| Primary modeling sample | n=92 (income available) or n=214 (full)? | n=92 used above; adjust if needed | ✅ n=92 |
| Regression model type | Negative Binomial / Poisson / OLS? | NB allows overdispersion (preferred) | ✅ Negative Binomial |
| Supervisor feedback | Incorporated? | Check all feedback from feedback doc | ⏳ Verify |

---

## Critical Reminders

### Data Integrity
- **NEVER** overwrite raw data files. Always work on copies in `02_outputs/datasets/`.
- **ALWAYS** document every transformation (variable renaming, recoding, aggregation).
- **ALWAYS** verify sample sizes match expectations after each step (n=214 households, n=284 vendors, etc.).

### Transparency
- Every analysis must be reproducible: save scripts, log decisions, document assumptions.
- Every test must be reported: include test statistic, p-value, effect size, sample size.
- Every finding must be interpreted: state whether it supports or refutes your hypothesis.

### Deadline Awareness
- Focus on **MUST_DO** items if time is limited.
- Regression model (Tier 4) is **SHOULD_DO** but strengthens results chapter significantly—prioritize if possible.
- Thesis integration (Phase 4) is **MUST_DO** to ensure outputs appear in correct chapters.

### Supervisor Communication
- Flag any data anomalies or methodological deviations from original plan.
- Share progress log and preliminary tables at checkpoint milestones.
- Address feedback in real-time; don't wait until the final revision.

---

## File Organization Checklist

Before declaring the workflow complete:

- [ ] `00_inputs/` contains all raw data files and methodology documents
- [ ] `01_scripts/` contains all analysis scripts (labeled 01_, 02_, 03_, 04_)
- [ ] `02_outputs/tables/` contains all output tables (Table_01, Table_02, Table_03, Table_04)
- [ ] `02_outputs/figures/` contains all visualizations (Figure_01, etc.)
- [ ] `02_outputs/datasets/` contains consolidated, cleaned datasets (checkpoint files)
- [ ] `03_logs/` contains all decision documentation (methodology_summary.md, variable_mapping.md, cleaning_decisions.md, data_decisions.md, progress_log.md, output_mapping.md)
- [ ] Root `README.md` explains project overview, tools, and links to phases

---

**Version History**

| Version | Date | Change |
|---------|------|--------|
| 1.0 | [Original] | Initial Workflow (Rebuild) template |
| 2.0 | 2025-11-23 | Merged with project-specific Who.md; integrated Turner framework, sample sizes, variable specs, Tier 1-4 analysis structure |

---

**Next Step**: Begin Phase 0 (Setup & Data Consolidation). Load your three consolidated datasets and verify sample sizes. Then proceed to Phase 1.
