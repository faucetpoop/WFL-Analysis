---
title: "Phase 1: Data Cleaning & Variable Specification"
date: 2025-11-23
phase: 1
status: "Ready to Execute"
---

# Phase 1: Data Cleaning & Variable Specification

**Objective**: Clean data, construct operationalized variables, and prepare for Tier 1-2 analyses
**Duration**: 3-4 hours
**Input**: Phase 0 processed datasets
**Output**: Complete analysis-ready dataset with all operationalized variables

---

## Phase 1 Overview

### What You'll Do
1. Load Phase 0 checkpoint datasets
2. Recode and validate data values
3. Construct all 33 operationalized variables from raw data
4. Create T2 stratification variables
5. Handle missing data systematically
6. Create analysis-ready dataset

### Why It Matters
- Translates raw survey data into operationalized measures aligned with Turner Framework
- Creates the variables you'll use in all subsequent analyses
- Ensures consistency between operationalization spec and actual variables
- Creates the analysis dataset needed for Tier 1-2 studies

---

## Detailed Tasks

### Task 1: Load Phase 0 Datasets

```r
# Load Phase 0 processed data
household_df <- read_csv("01_scripts/Phase_0_household_processed.csv")
vendor_df <- read_csv("01_scripts/Phase_0_vendor_processed.csv")

# Load operationalization specs
ops <- yaml::read_yaml("DOCUMENTATION/REFERENCE/operationalization_master.yaml")
```

### Task 2: Validate Data Values

For each key variable, check:
- [ ] Numeric variables are numeric (no accidental text)
- [ ] Categories are in expected range
- [ ] No impossible values (e.g., negative time)
- [ ] Date fields properly formatted

---

## Variable Construction by Domain

### EXTERNAL DOMAIN (OP001-OP008)

#### OP001: Food Group Availability - Overall
**Definition**: Count of food groups available from all vendors
**Operationalization**:
```r
# For vendor df, count availability items
vendor_df <- vendor_df %>%
  mutate(
    food_groups_available = rowSums(
      select(., starts_with("foodgroups_001_")),
      na.rm = FALSE
    ),
    OP001 = food_groups_available
  )
```

#### OP002: Vendor Diversity
**Definition**: Number of different vendor types with food
**Operationalization**:
```r
# Count unique vendor types with food available
# Method: Group by location, count distinct vendor types
vendor_diversity <- vendor_df %>%
  filter(foodgroups_available > 0) %>%
  group_by(location) %>%
  summarise(OP002 = n_distinct(vendor_type))
```

#### OP003: Price Affordability Motive
**Definition**: Household reports "affordability" as shopping motive
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    OP003 = ifelse(reason_001_affordability == 1, "yes", "no")
  )
```

#### OP004-OP007: Vendor Quality Dimensions
**Definition**: Household perceptions of vendor characteristics
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    OP004 = clean,           # Cleanliness
    OP005 = safe,            # Food safety
    OP006 = reputation,      # Vendor reputation
    OP007 = infrastructure   # Infrastructure/facilities
  )
```

#### OP008: Marketing & Regulation
**Status**: Not measured (document as limitation)
```r
household_df <- household_df %>%
  mutate(
    OP008 = NA,  # Not measured - policy audit not conducted
    OP008_note = "Not measured - documented limitation"
  )
```

---

### PERSONAL DOMAIN (OP009-OP024)

#### OP009: Travel Time - Household Reported
**Definition**: Minutes to main food source
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    OP009 = time_to_main_source,  # in minutes
    OP009_unit = "minutes"
  )
```

#### OP010: Visit Frequency
**Definition**: How often household visits food sources per week
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    OP010 = rowMeans(
      select(., market_freq, supermarket_freq, street_vendor_freq),
      na.rm = TRUE
    )
  )
```

#### OP011: Accessibility Tier (T2 STRATIFICATION VARIABLE)
**Definition**: Binary classification of accessibility
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    OP011_binary = ifelse(time_to_main_source <= 5, "Close", "Far"),
    OP011_numeric = ifelse(time_to_main_source <= 5, 0, 1)
  )
```

#### OP012: Food Expenditure
**Definition**: Amount household spends on food per period
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    OP012 = foodexpenditure,
    OP012_unit = foodexp_timeunit  # daily/weekly/monthly
  )
```

#### OP013: Income Proxy
**Definition**: Asset-based income proxy from household assets
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    OP013 = rowSums(
      select(., land_area, house_materials, appliances, livestock),
      na.rm = TRUE
    )
  )
```

#### OP014: Income Estimate
**Definition**: Estimated income from proxy measures
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    OP014 = case_when(
      OP013 < quantile(OP013, 0.33, na.rm = TRUE) ~ "low",
      OP013 < quantile(OP013, 0.67, na.rm = TRUE) ~ "medium",
      TRUE ~ "high"
    )
  )
```

#### OP015: Affordability Motive
**Definition**: Household reports affordability motivation for shopping
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    OP015 = reason_001_affordability  # 0/1 or yes/no
  )
```

#### OP016: Food Budget Share Tier (T2 STRATIFICATION VARIABLE)
**Definition**: Food expenditure as % of income (tertile)
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    # Calculate budget share
    OP016_raw = (OP012 / OP013) * 100,  # percentage

    # Tertile split
    OP016_tier = case_when(
      OP016_raw <= quantile(OP016_raw, 0.33, na.rm = TRUE) ~ "Low",
      OP016_raw <= quantile(OP016_raw, 0.67, na.rm = TRUE) ~ "Medium",
      TRUE ~ "High"
    ),

    # Store both raw and categorical
    OP016 = OP016_tier
  )
```

#### OP017-OP020: Convenience Domain
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    OP017 = cookingsource,          # Type of cooking facility
    OP018 = watersource,            # Where water comes from
    OP019 = waterdistance,          # Distance to water
    OP020 = electricity_access      # Electricity access (if available)
  )
```

#### OP021-OP024: Desirability Domain
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    OP021 = reason_health,          # Health-motivated shopping
    OP022 = reason_trust,           # Trust-motivated shopping
    OP023 = perception_food_quality, # Perception of food quality
    OP024 = food_preference         # Food preference/habits
  )
```

---

### EMERGENT DIMENSIONS (OP025-OP028)

#### OP025: Food Safety Index (T2 STRATIFICATION VARIABLE)
**Definition**: Aggregate perception of food safety
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    # Standardize components (z-scores)
    clean_z = scale(OP004),
    safe_z = scale(OP005),
    reputation_z = scale(OP006),

    # Create index
    OP025_raw = (clean_z + safe_z + reputation_z) / 3,

    # Binary classification (median split)
    OP025 = ifelse(OP025_raw >= median(OP025_raw, na.rm = TRUE), "High", "Low")
  )
```

#### OP026: Trust-Based Shopping
**Definition**: Trust in vendors influences shopping
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    OP026 = reason_trust  # Trust motivation score
  )
```

#### OP027: Decision-Maker Gender
**Definition**: Gender of primary household food decision-maker
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    OP027 = decision_maker_gender  # "M", "F", or other
  )
```

#### OP028: Frequency Stability
**Definition**: Consistency of shopping across outlets
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    # Calculate coefficient of variation in visit frequency
    freq_cv = sd(c(market_freq, supermarket_freq, street_vendor_freq), na.rm = TRUE) /
              mean(c(market_freq, supermarket_freq, street_vendor_freq), na.rm = TRUE),

    OP028 = freq_cv  # Higher = less stable
  )
```

---

### OUTCOME VARIABLES (OP029-OP033)

#### OP029: Household Dietary Diversity Score (PRIMARY DV)
**Definition**: Count of food groups consumed in past 7 days
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    OP029 = rowSums(
      select(., starts_with("hh_consumption_")),
      na.rm = FALSE
    ),
    OP029_name = "HDDS"
  )
```

#### OP030: Nutrient-Dense Food %
**Definition**: Percentage of foods that are nutrient-dense
**Operationalization**:
```r
# Define nutrient-dense groups
nutrient_dense <- c("hh_consumption_legumes", "hh_consumption_meat",
                    "hh_consumption_vegetables", "hh_consumption_fruits")

household_df <- household_df %>%
  mutate(
    OP030 = rowSums(select(., all_of(nutrient_dense)), na.rm = FALSE) / OP029 * 100
  )
```

#### OP031: Processed Food %
**Definition**: Percentage of foods that are processed
**Operationalization**:
```r
# Define processed groups
processed <- c("hh_consumption_oilseeds")  # adjust based on your definition

household_df <- household_df %>%
  mutate(
    OP031 = rowSums(select(., all_of(processed)), na.rm = FALSE) / OP029 * 100
  )
```

#### OP032: Simple Carbs %
**Definition**: Percentage of simple carbohydrates
**Operationalization**:
```r
simple_carbs <- c("hh_consumption_cereals")

household_df <- household_df %>%
  mutate(
    OP032 = rowSums(select(., all_of(simple_carbs)), na.rm = FALSE) / OP029 * 100
  )
```

#### OP033: Diet Quality Tier
**Definition**: Classification of overall diet quality
**Operationalization**:
```r
household_df <- household_df %>%
  mutate(
    OP033 = case_when(
      OP029 < 4 ~ "Poor",           # <4 food groups
      OP029 < 7 ~ "Adequate",       # 4-6 food groups
      TRUE ~ "Diverse"              # 7+ food groups
    )
  )
```

---

## Data Cleaning Tasks

### Recode Missing Values
```r
# Identify missing value codes
household_df <- household_df %>%
  mutate(across(everything(),
    ~ifelse(. %in% c(-99, "NA", "N/A", ""), NA, .)))
```

### Validate Ranges
```r
# Check for out-of-range values
household_df %>%
  summarise(
    time_min = min(OP009, na.rm = TRUE),
    time_max = max(OP009, na.rm = TRUE),
    hdds_min = min(OP029, na.rm = TRUE),
    hdds_max = max(OP029, na.rm = TRUE)
  )
```

### Create Analytic Sample
```r
# Remove rows with critical missing values
household_analytic <- household_df %>%
  filter(!is.na(OP029),           # HDDS required
         !is.na(OP011),           # Accessibility required
         !is.na(OP016))           # Affordability required

cat(sprintf("Analytic sample: %d households\n", nrow(household_analytic)))
```

---

## Phase 1 Output

### Files Created
- [ ] `01_scripts/Phase_1_variables_constructed.csv` - All OPs added
- [ ] `01_scripts/Phase_1_codebook.csv` - Variable names and definitions
- [ ] `01_scripts/Phase_1_summary.RDS` - Descriptive statistics for all OPs

### Sample Descriptive Statistics
```r
# Create summary table
summary_table <- household_analytic %>%
  summarise(
    across(starts_with("OP"), list(
      n = ~sum(!is.na(.)),
      mean = ~mean(., na.rm = TRUE),
      sd = ~sd(., na.rm = TRUE),
      min = ~min(., na.rm = TRUE),
      max = ~max(., na.rm = TRUE)
    ), .names = "{.col}_{.fn}")
  )
```

---

## Phase 1 Completion Criteria

✅ **All 33 Operationalizations Constructed**
- OP001-OP008: External domain variables
- OP009-OP024: Personal domain variables
- OP025-OP028: Emergent dimension variables
- OP029-OP033: Outcome variables

✅ **T2 Stratification Variables Created**
- OP011: Accessibility Tier (binary: Close/Far)
- OP016: Affordability Tier (tertile: Low/Medium/High)
- OP025: Food Safety Tier (binary: Low/High)

✅ **Data Quality Verified**
- Missing data documented
- Out-of-range values handled
- Analytic sample identified (n=?)

✅ **Analysis-Ready Dataset Created**
- All 33 OPs present
- No conflicts or errors
- Ready for Tier 1-2 analyses

---

## Next Phase

When Phase 1 is complete:
→ **Phase 2: Tier 1 & 2 Analyses**
See: `PLANNING/Phase_2/PHASE_2_TIER1_TIER2.md`

---

**Phase 1 Status**: Ready to Execute
**Last Updated**: 2025-11-23
