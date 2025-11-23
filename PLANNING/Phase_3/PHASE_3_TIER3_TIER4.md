---
title: "Phase 3: Tier 3 & 4 Analyses (Correlation & Regression)"
date: 2025-11-23
phase: 3
status: "Ready to Execute"
---

# Phase 3: Tier 3 & 4 Analyses

**Objective**: Examine relationships among variables and assess Turner Framework domains
**Duration**: 4-5 hours
**Input**: Phase 1-2 completed dataset and analyses
**Output**: Correlation matrices, regression models, domain effect rankings

---

## Tier 3: Correlation & Relationship Analysis

### Task 1: Correlation Matrix

Create correlation matrix for continuous variables:

```r
# Select continuous predictors and outcome
cor_vars <- household_df %>%
  select(OP009, OP012, OP013, OP019, OP028, # continuous IVs
         OP004, OP005, OP006, OP007,        # perception scales
         OP029)                              # outcome

# Calculate correlations
cor_matrix <- cor(cor_vars, use = "complete.obs")

# Pearson and Spearman tests
cor_test <- rcorr(as.matrix(cor_vars))

write.csv(cor_matrix, "02_outputs/tables/Table_3_Correlation_Matrix.csv")
```

---

## Tier 4: Framework Assessment

### Task 1: Domain-Specific Regression

**Model 1: External Domain Only**
```r
model_external <- lm(OP029 ~ OP001 + OP002 + OP003 + OP004 + OP005 + OP006 + OP007,
                     data = household_df)
summary(model_external)
```

**Model 2: Personal Domain Only**
```r
model_personal <- lm(OP029 ~ OP009 + OP010 + OP012 + OP013 + OP015 + OP017 + OP018 + OP021 + OP022 + OP023,
                    data = household_df)
summary(model_personal)
```

**Model 3: Full Turner Framework**
```r
model_full <- lm(OP029 ~ OP001 + OP002 + OP003 + OP004 + OP005 + OP006 + OP007 +  # external
                        OP009 + OP010 + OP012 + OP013 + OP015 + OP017 + OP018 + OP021 + OP022 + OP023,  # personal
                data = household_df)
summary(model_full)
```

### Task 2: Interaction Effects

**Affordability × Accessibility**
```r
model_interaction <- lm(OP029 ~ OP011 + OP016 + OP011:OP016,
                       data = household_df)
```

**Safety × Budget Share**
```r
model_safety_interaction <- lm(OP029 ~ OP016 + OP025 + OP016:OP025,
                              data = household_df)
```

### Task 3: Effect Ranking

Rank predictor importance:
```r
# Extract standardized coefficients
std_coefs <- data.frame(
  Variable = names(model_full$coefficients)[-1],
  Coefficient = coef(model_full)[-1],
  P_value = summary(model_full)$coefficients[-1, 4],
  Sig = ifelse(summary(model_full)$coefficients[-1, 4] < 0.05, "***", "")
) %>%
  arrange(desc(abs(Coefficient)))
```

---

## Phase 3 Outputs

- [ ] **Table 3**: Correlation Matrix (OP029 with continuous predictors)
- [ ] **Table 4A**: Regression - External Domain Only
- [ ] **Table 4B**: Regression - Personal Domain Only
- [ ] **Table 4C**: Regression - Full Turner Framework
- [ ] **Table 4D**: Interaction Effects (Affordability × Accessibility)
- [ ] **Table 5**: Standardized Coefficient Ranking

---

## Phase 3 Completion Criteria

✅ **Correlations calculated and reported**
✅ **Domain-specific regression models created**
✅ **Full Turner model estimated**
✅ **Interactions examined**
✅ **Effect ranking completed**
✅ **Model assumptions checked**

---

## Next Phase

→ **Phase 4: Outputs & Thesis Integration**
See: `PLANNING/Phase_4/PHASE_4_OUTPUTS_INTEGRATION.md`

---

**Phase 3 Status**: Ready to Execute
**Last Updated**: 2025-11-23
