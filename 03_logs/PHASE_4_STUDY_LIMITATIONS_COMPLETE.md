# Phase 4: Comprehensive Study Limitations Documentation
## WFL Analysis - Vietnamese Urban Households

---

**Project**: Whole Food Literacy Analysis
**Phase**: 4 - Outputs & Thesis Integration
**Document Type**: Limitations Inventory
**Date**: 2025-11-23
**Status**: ✅ COMPLETE

---

## 📋 Document Purpose

This document provides a comprehensive, categorized inventory of all study limitations that must be acknowledged in the thesis. Each limitation is rated by severity and includes recommended reporting language.

---

## 🔴 CRITICAL LIMITATIONS (Must Report Prominently)

### Limitation 1: Severe Sample Size Reduction (Listwise Deletion)

**Severity**: 🔴 **CRITICAL**
**Affects**: All regression models (Tier 4 analyses)

**Issue Description**:
- Original sample: 214 households (100%)
- **External Domain model**: 75 households (35.0%) → **65.0% loss**
- **Personal Domain model**: 76 households (35.5%) → **64.5% loss**
- **Full Framework model**: 64 households (29.9%) → **70.1% loss**

**Root Causes**:
1. Multiple variables with >40% missing data:
   - OP007 (Infrastructure): 53.7% missing
   - OP019 (Water distance): 53.7% missing
   - Market-only variables (OP003, 021, 022): 41.1% missing (applies to market shoppers only)
2. Listwise deletion across 14 predictors compounds missingness
3. Survey design: conditional questions created structural missingness

**Impacts**:
- ⚠️ **Drastically reduced statistical power** (power analysis: need n≥200, have n=64)
- ⚠️ **Potential selection bias** (only households with complete data on all 14 variables)
- ⚠️ **Unstable coefficient estimates** (wide confidence intervals)
- ⚠️ **Generalizability concerns** (complete-case sample may differ from full sample)

**Recommended Thesis Language**:
> "Due to listwise deletion across 14 predictors with varying missing data patterns, the full Turner Framework regression model sample was reduced to N=64 households (29.9% of the total sample), representing a 70.1% data loss. This substantial reduction in sample size severely limited statistical power and introduced potential selection bias, as complete-case households may systematically differ from those with missing data on multiple variables."

---

### Limitation 2: Model Overfitting (Negative Adjusted R²)

**Severity**: 🔴 **CRITICAL**
**Affects**: Personal Domain and Full Framework regression models

**Issue Description**:
- **Personal Domain**: Adj R² = **-0.057** (negative!)
- **Full Framework**: Adj R² = **-0.016** (negative!)

**Technical Details**:
- Full Framework: 13 predictors with 64 observations
- Predictor-to-observation ratio: **1:4.9**
- Recommended minimum: **1:10**
- Best practice: **1:15-20**

**What Negative Adjusted R² Means**:
- Model explains variance **no better than baseline** (intercept-only)
- After penalty for number of predictors, model performs **worse** than simple mean
- Severe overfitting: model is fitting noise, not signal

**Consequences**:
- ❌ Model is **unreliable** for inference
- ❌ Cannot support Turner Framework validation claims
- ❌ Coefficients are **unstable** and likely spurious
- ❌ Standard errors are inflated
- ❌ p-values are unreliable

**Recommended Thesis Language**:
> "The Full Turner Framework regression model exhibited severe overfitting, with a negative adjusted R² (-0.016) indicating that the model performs no better than a simple intercept-only model after penalizing for the number of predictors. With 13 predictors and only 64 observations (ratio 1:4.9), the model violates recommended minimum sample size guidelines (1:10 minimum, 1:15-20 optimal) and produces unstable coefficient estimates. Consequently, this model cannot support confirmatory conclusions about the Turner Framework and should be interpreted as exploratory only."

---

### Limitation 3: Non-Significant Regression Models

**Severity**: 🔴 **CRITICAL**
**Affects**: All three primary regression models

**Issue Description**:
- **External Domain**: F(5,69)=1.21, p=0.314 → **NOT SIGNIFICANT**
- **Personal Domain**: F(8,67)=0.50, p=0.855 → **NOT SIGNIFICANT**
- **Full Framework**: F(13,50)=0.92, p=0.537 → **NOT SIGNIFICANT**
- **Interaction Model**: F(3,92)=0.89, p=0.450 → **NOT SIGNIFICANT**

**Model Performance Summary**:

| Model | N | R² | Adj R² | F-statistic | p-value | Significant? |
|-------|---|----|----|-------------|---------|--------------|
| External Domain | 75 | 0.081 | 0.014 | 1.21 | 0.314 | ❌ NO |
| Personal Domain | 76 | 0.056 | -0.057 | 0.50 | 0.855 | ❌ NO |
| Full Framework | 64 | 0.193 | -0.016 | 0.92 | 0.537 | ❌ NO |
| Interaction | 96 | 0.028 | -0.002 | 0.89 | 0.450 | ❌ NO |

**Individual Predictor Significance**:
- **Zero individual predictors** significant in multivariate Full Framework model
- Only OP028 significant in bivariate correlations

**Implications**:
- ❌ **Cannot claim Turner Framework validation**
- ❌ **Weak evidence for food environment effects on dietary diversity**
- ❌ **No support for interaction hypotheses**
- ✓ **Can report exploratory effect sizes** (standardized coefficients)
- ✓ **Can highlight OP028 bivariate finding** (r=0.542***)

**Recommended Thesis Language**:
> "All three regression models testing the Turner Framework failed to achieve statistical significance (External: p=0.314; Personal: p=0.855; Full: p=0.537), indicating that food environment perceptions as operationalized in this study exhibited weak linear relationships with dietary diversity. Consequently, these models cannot support claims of Turner Framework validation in this context and should be interpreted as exploratory analyses generating hypotheses for future research."

---

### Limitation 4: Cross-Sectional Design (No Causality)

**Severity**: 🔴 **CRITICAL**
**Affects**: All causal interpretation

**Issue Description**:
- Single timepoint data collection
- No temporal variation captured
- Cannot establish directionality of relationships
- Third-variable confounding possible

**Precludes**:
- ❌ Causal claims (e.g., "food environment causes dietary diversity")
- ❌ Directionality statements (e.g., "X leads to Y")
- ❌ Temporal precedence (cannot say X precedes Y)
- ❌ Control for unmeasured time-varying confounders

**What CAN Be Claimed**:
- ✓ Associations and correlations
- ✓ Group differences (comparative descriptions)
- ✓ Predictive relationships (statistical, not causal)
- ✓ Hypothesis generation for future longitudinal research

**Recommended Thesis Language**:
> "The cross-sectional design of this study precludes causal inference. All findings represent associations only; temporal precedence and directionality of relationships cannot be established. While the Turner Framework posits that food environment perceptions influence dietary diversity, reverse causation (dietary diversity affecting food environment perceptions) or third-variable confounding (e.g., socioeconomic status affecting both) remain plausible alternative explanations."

---

## 🟡 IMPORTANT LIMITATIONS (Report in Limitations Section)

### Limitation 5: 24-Hour HDDS Recall (Temporal Validity)

**Severity**: 🟡 **IMPORTANT**
**Affects**: Outcome variable validity

**Issue Description**:
- HDDS measured via 24-hour recall (single day)
- May not reflect **typical** or **habitual** diet
- Subject to day-to-day variation
- Potential recall bias

**Evidence of Issue**:
- Intra-individual variation: diets vary across days
- Special occasions, illness, or unusual events may skew single-day measure
- No verification of "typical" day status

**Impact on Findings**:
- Measurement error in outcome variable
- Reduced statistical power (random error)
- Possible misclassification of dietary diversity levels
- Attenuation of true associations

**Recommended Mitigation (Future Work)**:
- Multiple 24-hour recalls (≥3 non-consecutive days)
- Food frequency questionnaire (FFQ) as supplement
- Combination of methods for validation

**Recommended Thesis Language**:
> "The HDDS outcome was measured via a single 24-hour dietary recall, which may not reflect habitual dietary patterns. Intra-individual day-to-day variation in food consumption introduces measurement error that likely attenuates observed associations with food environment predictors. Future research should employ multiple non-consecutive 24-hour recalls or food frequency questionnaires to capture typical dietary diversity more reliably."

---

### Limitation 6: Perception-Based Predictors (Subjective Measures)

**Severity**: 🟡 **IMPORTANT**
**Affects**: Predictor variable validity

**Issue Description**:
- All food environment variables based on **self-reported perceptions**
- No objective measurements (e.g., GIS, food audits, direct observation)
- Subject to:
  - Response bias (social desirability, acquiescence)
  - Recall error (frequency, distance estimates)
  - Cognitive heuristics (availability bias, anchoring)
  - Cultural interpretation differences

**Examples of Subjective Measures**:
- OP003: "Cheap" as motive (relative perception, not price data)
- OP009: Travel time (estimated, not GPS-measured)
- OP014: Asset-based income proxy (not actual income)
- OP023: Food environment perception (Likert scale, subjective)
- OP025: Neighborhood safety (perceived, not crime data)

**Objective Alternatives (Not Used)**:
- GIS-derived measures: distance to food outlets, density, variety
- Food outlet audits: actual prices, quality scores, safety inspections
- Administrative data: vendor licenses, health permits
- GPS tracking: actual shopping trips, time, locations

**Impact on Findings**:
- Perception-reality gap: perceptions may not match objective environment
- Shared method variance: self-report predictors and outcome
- Measurement error reduces true effect size detection

**Recommended Thesis Language**:
> "All food environment predictors were based on household self-reported perceptions rather than objective measures (e.g., GIS-derived distances, food outlet audits, administrative data). While perceptions are theoretically relevant to household food choices, the perception-reality gap and measurement error inherent in subjective assessments likely contributed to the weak observed associations. Future research should incorporate objective food environment measurements to complement perception-based measures."

---

### Limitation 7: Omitted Confounders (Model Misspecification)

**Severity**: 🟡 **IMPORTANT**
**Affects**: Validity of regression coefficients

**Issue Description**:
- Key determinants of dietary diversity **not included** in models
- Omitted variable bias: coefficients may be confounded

**Critical Omitted Variables**:
1. **Household Income**: Direct measure not available (only asset-based proxy)
2. **Education Level**: Not modeled (affects food knowledge, preferences)
3. **Household Size/Composition**: Not included (affects food purchasing, preparation)
4. **Cultural/Ethnic Background**: Not captured (dietary preferences, traditions)
5. **Food Preferences**: Individual taste, dietary restrictions not measured
6. **Neighborhood-Level Factors**: No multilevel structure (nesting in geography)

**Why OP008 (Marketing & Regulation) NOT Measured**:
- Questionnaire design: OP008 questions not included in household survey
- Limitation acknowledged in Phase 3 analysis
- Turner Framework incomplete operationalization

**Consequences of Omission**:
- Coefficients may be biased (upward or downward)
- Confounding: omitted variables correlated with both predictors and outcome
- True effects may be masked or spuriously amplified
- R² likely underestimates true explained variance

**Recommended Thesis Language**:
> "Several theoretically important determinants of dietary diversity were not included in regression models due to data availability constraints. These omitted variables—including direct household income measures, education level, household composition, and cultural background—may confound observed associations between food environment perceptions and dietary diversity. Additionally, OP008 (Marketing & Regulation dimension of the Turner Framework) was not measured, representing an incomplete operationalization of the framework."

---

### Limitation 8: Single-Item Measures (Psychometric Limitations)

**Severity**: 🟡 **IMPORTANT**
**Affects**: Reliability of specific predictors

**Issue Description**:
- Several constructs measured with **single binary or Likert items**
- Low reliability (no internal consistency checks possible)
- High measurement error

**Single-Item Variables**:
- **OP003**: Price motive (binary: "cheap" mentioned or not)
- **OP021**: Health motive (binary: "healthy" mentioned or not)
- **OP022**: Trust motive (binary: "trust" mentioned or not)
- OP004-007: External domain perceptions (single Likert items each)

**Psychometric Issues**:
- Cronbach's alpha cannot be computed (need ≥2 items per construct)
- Test-retest reliability unknown
- Construct validity unclear
- Measurement error inflates null findings

**Multi-Item Alternatives (Not Used)**:
- Affordability: multi-item scale (e.g., "I worry about food costs," "I can't afford variety," etc.)
- Trust: multi-item scale (vendor trust, food safety trust, label trust)
- Health: health consciousness scale

**Recommended Thesis Language**:
> "Several key constructs were operationalized using single-item measures (OP003, OP021, OP022, OP004-007), limiting measurement reliability and validity. Single-item measures are more susceptible to measurement error and lack the psychometric properties (internal consistency, dimensionality) of multi-item scales. This measurement limitation likely contributed to weak observed associations and should be addressed in future research through validated multi-item scales."

---

## 🟢 MODERATE LIMITATIONS (Report Briefly)

### Limitation 9: Market-Only Variables (Restricted Applicability)

**Severity**: 🟢 **MODERATE**
**Affects**: OP003, OP021, OP022 (motive variables)

**Issue Description**:
- Motive variables (OP003, 021, 022) derived from "Why shop at THIS market?" question
- Only applicable to households who shop at markets
- Non-market shoppers (grocery stores, street vendors only) coded as missing

**Sample Impact**:
- 41.1% of households missing on these variables
- Restricts analysis to market-shopping households
- May introduce selection bias if market shoppers differ systematically

**Alternative Approach (Not Used)**:
- General food choice motives survey (not market-specific)
- Separate analyses for market vs non-market shoppers

**Recommended Thesis Language**:
> "Motive variables (OP003 price, OP021 health, OP022 trust) were derived from market-specific survey questions and are only applicable to households who shop at markets. This restriction resulted in 41.1% missingness and limits generalizability to all food-sourcing strategies. Future research should employ general food choice motive surveys applicable across all outlet types."

---

### Limitation 10: Urban Vietnam Context Specificity

**Severity**: 🟢 **MODERATE**
**Affects**: Generalizability

**Issue Description**:
- Study conducted in urban Vietnamese households
- Food system characteristics unique to Vietnam/Southeast Asia:
  - Dual formal-informal market structure
  - High street vendor density
  - Wet markets as primary food source
  - Motorcycle-based shopping
  - Daily shopping culture

**Limits Generalizability To**:
- Other low- and middle-income countries (LMICs)
- High-income countries (HICs) with different food systems
- Rural Vietnamese contexts

**Turner Framework Context**:
- Framework developed in HIC contexts (UK, Australia, USA)
- May not translate directly to urban Southeast Asian food environments
- Informal food sector not well-represented in original framework

**Recommended Thesis Language**:
> "This study was conducted in urban Vietnamese households, a context characterized by dual formal-informal food systems, high street vendor density, wet markets, and daily motorcycle-based shopping. These food environment features differ substantially from the high-income country contexts where the Turner Framework was developed. Findings may not generalize to other LMIC or HIC settings, and the framework may require adaptation to capture informal food sector dynamics."

---

### Limitation 11: Expenditure as Income Proxy (OP014)

**Severity**: 🟢 **MODERATE**
**Affects**: OP014 (income proxy validity)

**Issue Description**:
- OP014 intended to measure income/socioeconomic status
- Operationalized as **asset-based proxy**, not direct income
- Assets: ownership of durable goods, housing quality, utilities
- **Assumption**: Asset ownership correlates with income

**Why Not Direct Income**:
- Household income questions sensitive (respondent reluctance)
- Asset-based approach less threatening
- Standard practice in LMIC surveys (DHS, LSMS)

**Validity Concerns**:
- Assets reflect **wealth accumulation**, not current income flow
- Assets lag behind income changes
- Cultural/regional variation in asset ownership
- Does not capture informal income

**Impact on Findings**:
- Measurement error in SES construct
- May underestimate true SES effects on dietary diversity
- Asset index may not fully capture economic access to food

**Recommended Thesis Language**:
> "Household income was operationalized using an asset-based proxy (OP014) rather than direct income measurement. While asset indices are standard in LMIC research, they reflect wealth accumulation rather than current income flow and may not fully capture economic access to food. Future research should include direct household income measures alongside asset-based SES indicators."

---

### Limitation 12: OP024/OP027 Status Verification Needed

**Severity**: 🟢 **MODERATE**
**Affects**: OP024, OP027 (unclear operationalization)

**Issue Description**:
- Phase 4 planning document mentions OP024/OP027 needing status verification
- Current analysis: OP024 not found in dataset
- Used OP025 (neighborhood safety index) as proxy for food safety
- OP027 status unclear

**Data Quality Issue**:
- Survey-to-variable mapping incomplete for these variables
- May represent:
  - Variables not collected in final survey
  - Mislabeled variables
  - Composite variables not yet constructed

**Impact on Findings**:
- Food safety construct incompletely measured
- OP024 proxy (OP025) may not align with original Turner Framework definition
- Potential construct validity issue

**Recommended Thesis Language**:
> "Food safety perception (OP024) was not directly available in the dataset; neighborhood safety index (OP025) was used as a proxy. This substitution may not fully align with the Turner Framework's conceptualization of food safety perceptions and represents a limitation in construct validity. Future research should ensure direct measurement of food safety perceptions as distinct from neighborhood safety."

---

## 📊 Limitation Impact Summary Table

| Limitation | Severity | Affects | Impact on Conclusions | Mitigation Strategy (Future) |
|------------|----------|---------|----------------------|------------------------------|
| **Sample Size Reduction (70% loss)** | 🔴 CRITICAL | Regression models | Severely underpowered, unstable estimates | Larger samples (n≥300), targeted data collection |
| **Model Overfitting (Neg Adj R²)** | 🔴 CRITICAL | Personal & Full models | Unreliable coefficients, no framework validation | Reduce predictors OR increase sample size |
| **Non-Significant Models** | 🔴 CRITICAL | All regressions | Cannot claim framework validation | Exploratory framing, larger samples, objective measures |
| **Cross-Sectional Design** | 🔴 CRITICAL | Causal inference | No causality, only associations | Longitudinal design, multiple timepoints |
| **24-Hour HDDS Recall** | 🟡 IMPORTANT | Outcome validity | Measurement error, day-to-day variation | Multiple 24h recalls, FFQ supplement |
| **Perception-Based Predictors** | 🟡 IMPORTANT | Predictor validity | Subjective bias, measurement error | Objective measures (GIS, audits, GPS) |
| **Omitted Confounders** | 🟡 IMPORTANT | Coefficient validity | Confounding, biased estimates | Include income, education, household size |
| **Single-Item Measures** | 🟡 IMPORTANT | Reliability | Low reliability, high measurement error | Multi-item validated scales |
| **Market-Only Variables** | 🟢 MODERATE | OP003, 021, 022 | Restricted sample, selection bias | General food choice motive surveys |
| **Urban Vietnam Context** | 🟢 MODERATE | Generalizability | Limited to similar contexts | Replicate in diverse settings |
| **Asset-Based Income Proxy** | 🟢 MODERATE | OP014 validity | SES measurement error | Direct income measurement |
| **OP024 Not Measured** | 🟢 MODERATE | Food safety construct | Incomplete framework operationalization | Direct food safety perception measure |

---

## 🎯 Thesis Limitations Section Template

### Recommended Structure

**Chapter 5: Discussion**
**Section 5.4: Limitations**

#### 5.4.1 Sample Size and Statistical Power
[Report Limitation 1 + 2: Sample reduction and overfitting]

#### 5.4.2 Model Specification and Non-Significance
[Report Limitation 3 + 7: Non-significant models and omitted confounders]

#### 5.4.3 Study Design Constraints
[Report Limitation 4: Cross-sectional design]

#### 5.4.4 Measurement Limitations
[Report Limitations 5, 6, 8: HDDS recall, perception-based predictors, single-item measures]

#### 5.4.5 Operationalization Issues
[Report Limitations 9, 11, 12: Market-only variables, asset-based income, OP024]

#### 5.4.6 Generalizability
[Report Limitation 10: Urban Vietnam context]

---

## 📝 Key Messaging for Thesis Defense

### Committee Question Preparation

**Q: "Your regression models are all non-significant. Does this mean the study failed?"**
**A**:
> "The non-significant models do not invalidate the study; rather, they provide important exploratory evidence about the Turner Framework's applicability in urban LMIC contexts. The key contribution is the OP028 finding (outlet diversity, r=0.542***), which emerged despite weak multivariate relationships. The non-significance, combined with sample size and measurement limitations, indicates this work is hypothesis-generating for future confirmatory research with larger samples and objective measures."

**Q: "Why didn't you collect larger samples or use objective measures?"**
**A**:
> "This was a pilot study using existing secondary data from a household food security survey. Sample size and measurement choices reflected resource constraints typical of master's-level research. The analysis identified critical methodological improvements (larger n, objective GIS measures, longitudinal design) for future work, which is a valuable contribution of exploratory research."

**Q: "Can you make any claims given these limitations?"**
**A**:
> "Yes, within appropriate scope:
> ✓ OP028 (outlet diversity) as strongest predictor (robust bivariate finding)
> ✓ Weak linear relationships between perception-based food environment measures and dietary diversity (descriptive finding)
> ✓ Urban LMIC food systems may require different framework adaptations than HIC contexts (contextual insight)
> ✗ NOT claiming: Framework validation, causal effects, generalizability beyond sample"

---

## ✅ Limitations Documentation Checklist

### Pre-Writing
- [x] All limitations identified and categorized by severity
- [x] Evidence documented for each limitation
- [x] Impacts on conclusions clearly stated
- [x] Future mitigation strategies specified

### Thesis Writing
- [ ] Limitations section is **prominent** (full subsection in Discussion)
- [ ] All 🔴 CRITICAL limitations reported in detail
- [ ] All 🟡 IMPORTANT limitations reported clearly
- [ ] All 🟢 MODERATE limitations mentioned briefly
- [ ] Limitations framed as **research opportunities**, not failures
- [ ] Each limitation links to specific finding/table affected

### Committee Preparation
- [ ] Anticipated questions prepared with honest, evidence-based answers
- [ ] Positive framing ready: exploratory contribution, hypothesis-generating
- [ ] Mitigation strategies articulated for future research
- [ ] Scope of valid claims clearly defined

---

**Document Status**: ✅ COMPLETE
**Last Updated**: 2025-11-23
**Review Status**: Ready for thesis integration

**Next Step**: Integrate limitations systematically into Chapter 5 Discussion, Section 5.4

---

**CRITICAL REMINDER FOR THESIS WRITER**:

🚨 **DO NOT**:
- Hide non-significant results
- Overstate weak findings
- Use causal language
- Claim framework validation
- Ignore overfitting and sample size issues

✅ **DO**:
- Report all limitations prominently and honestly
- Frame as exploratory pilot study
- Emphasize OP028 contribution (outlet diversity)
- Acknowledge measurement and design constraints
- Propose clear future research improvements

**Methodological transparency and intellectual honesty are paramount.**

---

**Phase 4 Study Limitations Documentation - COMPLETE**
