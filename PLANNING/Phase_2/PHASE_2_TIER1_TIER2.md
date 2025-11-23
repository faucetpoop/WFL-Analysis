---
title: "Phase 2: Tier 1 & 2 Analyses (Descriptive & Bivariate)"
date: 2025-11-23
phase: 2
status: "Ready to Execute"
---

# Phase 2: Tier 1 & 2 Analyses

**Objective**: Describe all variables and compare outcomes by T2 stratification variables
**Duration**: 3-4 hours
**Input**: Phase 1 analysis-ready dataset with all 33 OPs
**Output**: Descriptive tables and T2 comparison results

---

## Phase 2 Overview

### Tier 1: Descriptive Statistics (All Variables)
Summarize all 31 "in data" operationalizations:
- Frequency/count variables
- Continuous variables (mean, SD, range)
- Categorical variables (proportions)
- Report by domain (External, Personal, Emergent, Outcome)

### Tier 2: Group Comparisons
Stratify outcome variables (OP029-OP033) by T2 strata:
- **OP011** (Accessibility): DDS by Close vs Far access
- **OP016** (Affordability): DDS by Low vs Medium vs High budget share
- **OP025** (Safety): DDS by Low vs High food safety perception

Compare means, proportions, and effect sizes.

---

## Task 1: Tier 1 Descriptive Statistics

### Step 1a: Continuous Variables

```r
# Create summary for continuous variables
t1_continuous <- household_df %>%
  select(OP009, OP012, OP013, OP019, OP028, OP029, OP030, OP031, OP032) %>%
  summarise(across(everything(), list(
    N = ~sum(!is.na(.)),
    Mean = ~mean(., na.rm = TRUE),
    SD = ~sd(., na.rm = TRUE),
    Min = ~min(., na.rm = TRUE),
    Q25 = ~quantile(., 0.25, na.rm = TRUE),
    Median = ~median(., na.rm = TRUE),
    Q75 = ~quantile(., 0.75, na.rm = TRUE),
    Max = ~max(., na.rm = TRUE)
  ), .names = "{.col}_{.fn}"))

write_csv(t1_continuous, "02_outputs/tables/Table_1_Descriptive_Continuous.csv")
```

### Step 1b: Categorical Variables

```r
# Create frequency table for categorical variables
t1_categorical <- household_df %>%
  select(OP003, OP011, OP014, OP015, OP016, OP017, OP018, OP021, OP022, OP025, OP033) %>%
  map_df(function(x) {
    if (is.factor(x) | is.character(x)) {
      tibble(
        Variable = deparse(substitute(x)),
        Category = names(table(x)),
        N = as.numeric(table(x)),
        Percent = as.numeric(prop.table(table(x)) * 100)
      )
    }
  })

write_csv(t1_categorical, "02_outputs/tables/Table_1_Descriptive_Categorical.csv")
```

### Step 1c: Aggregate by Domain

```r
# Organize by domain
t1_summary <- list(
  external_domain = list(OP001, OP002, OP003, OP004, OP005, OP006, OP007),
  personal_domain = list(OP009, OP010, OP011, OP012, OP013, OP014, OP015, OP016, OP017, OP018, OP019, OP020, OP021, OP022, OP023, OP024),
  emergent = list(OP025, OP026, OP027, OP028),
  outcome = list(OP029, OP030, OP031, OP032, OP033)
)
```

---

## Task 2: Tier 2 Comparisons - OP011 Accessibility

```r
# Group by accessibility tier
t2_accessibility <- household_df %>%
  group_by(OP011) %>%
  summarise(
    N = n(),
    HDDS_Mean = mean(OP029, na.rm = TRUE),
    HDDS_SD = sd(OP029, na.rm = TRUE),
    Diet_Diverse_Pct = sum(OP033 == "Diverse", na.rm = TRUE) / n() * 100,
    .groups = 'drop'
  )

# Statistical test
t_test_access <- t.test(
  household_df$OP029[household_df$OP011 == "Close"],
  household_df$OP029[household_df$OP011 == "Far"]
)

write_csv(t2_accessibility, "02_outputs/tables/Table_2A_Accessibility_Comparison.csv")
```

---

## Task 3: Tier 2 Comparisons - OP016 Affordability

```r
# Group by affordability tier
t2_affordability <- household_df %>%
  group_by(OP016) %>%
  summarise(
    N = n(),
    HDDS_Mean = mean(OP029, na.rm = TRUE),
    HDDS_SD = sd(OP029, na.rm = TRUE),
    Diet_Diverse_Pct = sum(OP033 == "Diverse", na.rm = TRUE) / n() * 100,
    .groups = 'drop'
  )

# Statistical test (ANOVA for 3 groups)
anova_afford <- aov(OP029 ~ OP016, data = household_df)

write_csv(t2_affordability, "02_outputs/tables/Table_2B_Affordability_Comparison.csv")
```

---

## Task 4: Tier 2 Comparisons - OP025 Safety

```r
# Group by food safety tier
t2_safety <- household_df %>%
  group_by(OP025) %>%
  summarise(
    N = n(),
    HDDS_Mean = mean(OP029, na.rm = TRUE),
    HDDS_SD = sd(OP029, na.rm = TRUE),
    Diet_Diverse_Pct = sum(OP033 == "Diverse", na.rm = TRUE) / n() * 100,
    .groups = 'drop'
  )

# Statistical test
t_test_safety <- t.test(
  household_df$OP029[household_df$OP025 == "High"],
  household_df$OP029[household_df$OP025 == "Low"]
)

write_csv(t2_safety, "02_outputs/tables/Table_2C_Safety_Comparison.csv")
```

---

## Phase 2 Outputs

### Tables Created
- **Table 1A**: Descriptive Statistics - Continuous Variables
- **Table 1B**: Descriptive Statistics - Categorical Variables
- **Table 2A**: HDDS by Accessibility Tier (OP011)
- **Table 2B**: HDDS by Affordability Tier (OP016)
- **Table 2C**: HDDS by Food Safety Tier (OP025)

### Statistical Summary
- [ ] All descriptive statistics calculated
- [ ] T-tests completed for binary comparisons (OP011, OP025)
- [ ] ANOVA completed for 3-group comparison (OP016)
- [ ] Effect sizes (Cohen's d or eta-squared) calculated
- [ ] P-values and confidence intervals reported

---

## Phase 2 Completion Criteria

✅ **Descriptive statistics for all variables**
✅ **T2 comparisons for all three stratification variables**
✅ **All tables saved as CSV files**
✅ **Statistical tests completed with p-values**
✅ **Documentation of findings**

---

## Next Phase

→ **Phase 3: Tier 3 & 4 Analyses** (Correlation & Regression)
See: `PLANNING/Phase_3/PHASE_3_TIER3_TIER4.md`

---

**Phase 2 Status**: Ready to Execute
**Last Updated**: 2025-11-23
