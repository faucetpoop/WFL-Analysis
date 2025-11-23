# Phase 4: Thesis Integration Guide
## WFL Analysis - Vietnamese Urban Households

---

**Project**: Whole Food Literacy Analysis
**Phase**: 4 - Outputs & Thesis Integration
**Date Completed**: 2025-11-23
**Status**: ✅ COMPLETE

---

## 📚 Document Purpose

This guide provides a comprehensive mapping of all analysis outputs to thesis chapters and sections, ensuring seamless integration of results into the dissertation.

---

## 📊 Table Integration Mapping

### Chapter 4: Results

#### Section 4.1: Sample Characteristics & Descriptive Statistics

**Table 1A: Descriptive Statistics - Continuous Variables**
- **File**: `02_outputs/tables/Table_1A_Descriptive_Continuous.csv`
- **Purpose**: Present means, standard deviations, ranges for all continuous outcome and predictor variables
- **Key Variables**: HDDS, expenditure, travel time, budget share, shopping frequency
- **Sample Size**: N=214 households
- **Thesis Location**: Beginning of Results chapter - sets baseline context

**Table 1B: Descriptive Statistics - Categorical Variables**
- **File**: `02_outputs/tables/Table_1B_Descriptive_Categorical.csv`
- **Purpose**: Present frequency distributions and percentages for categorical variables
- **Key Variables**: Accessibility tier, budget share tier, safety tier, diet quality tier
- **Sample Size**: N=214 households
- **Thesis Location**: Following Table 1A - completes sample description

---

#### Section 4.2: Bivariate Analyses (Tier 2)

**Table 2A: HDDS by Accessibility Perception**
- **File**: `02_outputs/tables/Table_2A_Accessibility_Comparison.csv`
- **Purpose**: Compare dietary diversity across accessibility perception levels (binary/tertiles)
- **Statistical Test**: Independent samples t-test or One-way ANOVA
- **Key Finding**: [Report effect size and significance]
- **Thesis Location**: T2 Analysis subsection - accessibility effects

**Table 2B: HDDS by Affordability (Food Budget Share - 3 Groups)**
- **File**: `02_outputs/tables/Table_2B_Affordability_Comparison.csv`
- **Purpose**: Compare dietary diversity across affordability tertiles (low/medium/high budget share)
- **Statistical Test**: One-way ANOVA with post-hoc comparisons
- **Key Finding**: [Report effect size and significance]
- **Thesis Location**: T2 Analysis subsection - affordability effects
- **Companion Figure**: Figure 3

**Table 2C: HDDS by Food Safety Perception**
- **File**: `02_outputs/tables/Table_2C_Safety_Comparison.csv`
- **Purpose**: Compare dietary diversity across safety perception levels
- **Statistical Test**: Independent samples t-test or One-way ANOVA
- **Key Finding**: [Report effect size and significance]
- **Thesis Location**: T2 Analysis subsection - safety effects
- **Companion Figure**: Figure 4

---

#### Section 4.3: Correlation Analysis (Tier 3)

**Table 3A: Pearson Correlation Matrix (Primary)**
- **File**: `02_outputs/tables/Table_3A_Correlation_Matrix_Pearson.csv`
- **Purpose**: Full correlation matrix of 12 continuous predictors
- **Dimensions**: 12×12 matrix with correlations and significance
- **Key Finding**: OP028 (Outlet Frequency Variation) r=0.542***
- **Thesis Location**: Main Results - Correlation Analysis subsection

**Table 3B: Spearman Correlation Matrix (Supplementary)**
- **File**: `02_outputs/tables/Table_3B_Correlation_Matrix_Spearman.csv`
- **Purpose**: Non-parametric correlation matrix (robustness check)
- **Dimensions**: 12×12 matrix with rank correlations
- **Thesis Location**: Appendix or supplementary materials
- **Use**: Confirm Pearson results, check for non-linear relationships

**Table 3C: HDDS Bivariate Correlations with Significance**
- **File**: `02_outputs/tables/Table_3C_HDDS_Correlations.csv`
- **Purpose**: Focused table of HDDS correlations with all 11 predictors
- **Includes**: Pearson r, Spearman ρ, p-values, significance markers
- **Key Finding**: Only OP028 significant (p<0.001)
- **Thesis Location**: Main Results - highlights key predictor

---

#### Section 4.4: Regression Analysis (Tier 4)

**Table 4A: External Domain Regression**
- **File**: `02_outputs/tables/Table_4A_External_Domain_Regression.csv`
- **Predictors**: 5 external environment variables (OP004-007, OP009)
- **Sample Size**: N=75 (35% of total due to listwise deletion)
- **Model Performance**: R²=0.081, Adj R²=0.014, F(5,69)=1.21, p=0.314
- **Key Finding**: Non-significant model, weak predictive power
- **Thesis Location**: Regression Results - External Domain subsection
- **Critical Note**: Acknowledge non-significance and sample size loss

**Table 4B: Personal Domain Regression**
- **File**: `02_outputs/tables/Table_4B_Personal_Domain_Regression.csv`
- **Predictors**: 8 personal/household variables (OP003, OP010, OP012-013, OP015-016, OP019, OP023)
- **Sample Size**: N=76 (35.5% of total)
- **Model Performance**: R²=0.056, Adj R²=-0.057, F(8,67)=0.50, p=0.855
- **Key Finding**: Non-significant model, negative adjusted R² (overfitting)
- **Thesis Location**: Appendix (due to poor performance)
- **Critical Note**: Severe overfitting and sample reduction

**Table 4C: Full Turner Framework Regression (PRIMARY REGRESSION)**
- **File**: `02_outputs/tables/Table_4C_Full_Framework_Regression.csv`
- **Predictors**: 14 variables (both domains combined)
- **Sample Size**: N=64 (29.9% of total - 70% data loss!)
- **Model Performance**: R²=0.193, Adj R²=-0.016, F(13,50)=0.92, p=0.537
- **Key Finding**: Non-significant, overfitted (1:4.9 predictor-to-case ratio)
- **Thesis Location**: Main Results - Full Framework subsection
- **Critical Framing**: **EXPLORATORY ANALYSIS ONLY**
- **Companion Figure**: Figure 5 (standardized coefficients)

**Reporting Strategy for Table 4C**:
✅ **DO Report**:
- Full model specification with all 14 predictors
- Sample size reduction (N=64, 29.9% of total)
- Complete statistics (R², Adj R², F, p-values)
- Standardized coefficients (Beta) for effect size comparison
- Non-significance clearly stated

❌ **DO NOT Claim**:
- Turner Framework "validated" (model non-significant)
- Causal relationships (cross-sectional data)
- Generalizability (sample size and listwise deletion issues)

**Table 4D: Interaction Effects (Accessibility × Affordability)**
- **File**: `02_outputs/tables/Table_4D_Interaction_Effects.csv`
- **Interaction**: OP009 (Travel Time) × OP016 (Budget Share)
- **Sample Size**: N=96 (55% data loss)
- **Model Performance**: R²=0.028, Adj R²=-0.002, p>0.05
- **Key Finding**: No significant interaction effect
- **Thesis Location**: Appendix - Exploratory Analyses
- **Interpretation**: Effects are independent, not multiplicative

---

#### Section 4.5: Effect Sizes & Predictor Rankings

**Table 5: Standardized Coefficient Ranking**
- **File**: `02_outputs/tables/Table_5_Standardized_Coefficient_Ranking.csv`
- **Purpose**: Rank all predictors by standardized coefficient magnitude
- **Includes**: Beta coefficients, p-values, absolute values for sorting
- **Top Predictor**: OP017_cooking_source (β=0.206)
- **Key Finding**: Despite non-significant model, effect sizes provide exploratory insights
- **Thesis Location**: After Table 4C - contextualizes regression results
- **Companion Figure**: Figure 5 (top 10 predictors visualized)

---

## 📈 Figure Integration Mapping

### Chapter 4: Results Figures

**Figure 1: HDDS Distribution**
- **File**: `02_outputs/figures/Phase_2_HDDS_Distribution.png`
- **Type**: Histogram with density curve
- **Purpose**: Show dietary diversity distribution across sample
- **Key Descriptive**: Mean HDDS, standard deviation, range, normality assessment
- **Thesis Location**: Beginning of Results - Sample Characteristics
- **Created**: Phase 2

**Figure 2: HDDS by Accessibility, Affordability, and Safety**
- **File**: `02_outputs/figures/Phase_2_T2_Comparisons_Boxplots.png`
- **Type**: Multi-panel box plots (3 comparisons)
- **Purpose**: Visualize bivariate relationships from Tier 2 analyses
- **Panels**: Accessibility / Affordability / Safety
- **Thesis Location**: T2 Analysis Results section
- **Created**: Phase 2
- **Accompanies**: Tables 2A-C

**Figure 3: HDDS by Affordability Tertiles**
- **File**: `02_outputs/figures/Figure_3_HDDS_by_Affordability_Tertiles.png`
- **Type**: Box plot (3 groups: Low/Medium/High Budget Share)
- **Purpose**: Detailed affordability stratification analysis
- **Sample Size**: N=124 (households with complete data)
- **Key Insight**: Relationship between food budget share and dietary diversity
- **Thesis Location**: T2 Analysis Results - Affordability subsection
- **Created**: Phase 4
- **Accompanies**: Table 2B

**Figure 4: HDDS by Neighborhood Safety**
- **File**: `02_outputs/figures/Figure_4_HDDS_by_Food_Safety.png`
- **Type**: Box plot (2 or 3 groups: Lower/Higher Safety)
- **Purpose**: Neighborhood safety environment effects on diet quality
- **Sample Size**: N=162 (households with complete data)
- **Variable Used**: OP025_neighborhood_safety_index (proxy for food safety)
- **Thesis Location**: T2 Analysis Results - Safety subsection
- **Created**: Phase 4
- **Accompanies**: Table 2C

**Figure 5: Top 10 Predictors of Dietary Diversity**
- **File**: `02_outputs/figures/Figure_5_Standardized_Coefficients.png`
- **Type**: Horizontal bar chart (standardized coefficients)
- **Purpose**: Visualize relative effect sizes from Full Turner Framework regression
- **Top Predictor**: OP017_cooking_source (β=0.206)
- **Color Coding**: Green (positive effects) / Red (negative effects)
- **Thesis Location**: Regression Results - Effect Sizes subsection
- **Created**: Phase 4
- **Accompanies**: Tables 4C and 5
- **Critical Note**: Display despite model non-significance for exploratory insights

---

## 📦 Summary Datasets for Thesis

### Dataset 1: Household Analysis Final
**File**: `02_outputs/datasets/household_analysis_final.csv`
**Description**: Complete dataset with all 25 constructed OP variables + HDDS outcome
**Dimensions**: 214 households × 25 columns
**Use Cases**:
- Thesis appendix data availability statement
- Supplementary materials for reviewers
- Replication data for future research
- Custom analyses requested by committee

**Key Variables**:
- **Outcome**: OP029_HDDS (Household Dietary Diversity Score)
- **External Domain**: OP004-009 (cleanliness, safety, reputation, infrastructure, marketing, travel time)
- **Personal Domain**: OP003, OP010, OP012-013, OP015-016, OP019, OP021-023, OP028 (motives, expenditure, affordability, water, frequency)
- **Composite Indices**: OP011, OP025, OP033 (tier variables)

---

### Dataset 2: T2 Comparison Results
**File**: `02_outputs/datasets/t2_comparison_results.csv`
**Description**: Consolidated bivariate comparison results from Tables 2A-C
**Dimensions**: 7 comparison groups × 14 summary columns
**Use Cases**:
- Quick reference for Tier 2 findings
- Meta-analysis across stratification variables
- Sensitivity analyses

**Included Comparisons**:
- Accessibility (2-3 groups)
- Affordability (3 groups - tertiles)
- Food Safety (2-3 groups)

**Summary Statistics per Group**:
- Group labels and sample sizes
- Mean HDDS and standard deviation
- Test statistics (t or F)
- p-values and significance markers
- Effect sizes (Cohen's d or eta-squared)

---

### Dataset 3: Correlation Summary
**File**: `02_outputs/datasets/correlation_summary.csv`
**Description**: Complete bivariate HDDS correlations from Table 3C
**Dimensions**: 11 predictors × 8 columns
**Use Cases**:
- Quick reference for correlation magnitudes
- Identifying candidates for deeper analysis
- Comparison to literature findings

**Columns**:
- Predictor variable name
- Pearson correlation coefficient (r)
- Pearson p-value
- Spearman correlation coefficient (ρ)
- Spearman p-value
- Sample size (varies by missing data)
- Significance markers (* p<0.05, ** p<0.01, *** p<0.001)
- Interpretation (strength and direction)

**Key Finding**: Only OP028 (Outlet Frequency Variation) shows significant correlation (r=0.542, p<0.001)

---

## 📑 Table and Figure Indices

### Comprehensive Table Index
**File**: `02_outputs/tables/TABLE_INDEX_THESIS_INTEGRATION.csv`
**Purpose**: Master reference for all 13 tables with thesis mapping
**Columns**:
- Table Number (1A, 1B, 2A, 2B, 2C, 3A, 3B, 3C, 4A, 4B, 4C, 4D, 5)
- Filename (exact CSV file path)
- Description (clear table content summary)
- Phase Created (0, 1, 2, or 3)
- Thesis Chapter (Chapter 4 Results / Appendix)
- Section (specific subsection placement)

**Use**: Systematic table placement and cross-referencing in thesis

---

### Comprehensive Figure Index
**File**: `02_outputs/figures/FIGURE_INDEX_THESIS_INTEGRATION.csv`
**Purpose**: Master reference for all 5 figures with thesis mapping
**Columns**:
- Figure Number (1, 2, 3, 4, 5)
- Filename (exact PNG file path)
- Description (clear figure content summary)
- Phase Created (2 or 4)
- Thesis Chapter (Chapter 4 Results)
- Section (specific subsection placement)

**Use**: Systematic figure placement and cross-referencing in thesis

---

## 🎯 Thesis Chapter Structure Recommendations

### Chapter 4: Results

**Section 4.1: Sample Characteristics**
- Table 1A (continuous descriptive statistics)
- Table 1B (categorical descriptive statistics)
- Figure 1 (HDDS distribution)
- Text: Sample demographics, data quality, representativeness

**Section 4.2: Bivariate Analyses (Tier 2 - Group Comparisons)**
- Table 2A + text (accessibility effects)
- Table 2B + Figure 3 (affordability effects - tertiles)
- Table 2C + Figure 4 (safety effects)
- Figure 2 (combined visualization of all three)
- Text: Statistical test results, effect sizes, interpretation

**Section 4.3: Correlation Analysis (Tier 3)**
- Table 3A (Pearson correlations - main)
- Table 3C (HDDS-focused correlations)
- Text: Highlight OP028 finding prominently, note weak other correlations
- Interpretation: Outlet diversity emerges as key predictor

**Section 4.4: Regression Analysis (Tier 4)**
- Table 4A (External Domain - brief mention, acknowledge non-significance)
- Table 4C (Full Framework - PRIMARY analysis)
- Table 5 + Figure 5 (standardized coefficients and rankings)
- Text: Full model specification, results, **limitations prominently**
- Framing: Exploratory pilot study, not confirmatory

**Section 4.5: Synthesis of Findings**
- Summary of key findings across tiers
- OP028 (Outlet Frequency Variation) as strongest predictor
- Weak Turner Framework relationships
- Transition to Discussion chapter

---

### Chapter 5: Discussion

**Section 5.1: Interpretation of Key Findings**
- **Novel Contribution**: Outlet diversity finding (OP028, r=0.542***)
- Theoretical implications: Food sourcing diversity vs single-outlet focus
- Urban LMIC context: Informal + formal system complexity

**Section 5.2: Weak Turner Framework Relationships**
- Why weak effects? (measurement, context, complexity)
- Perception-based vs objective measures
- Cross-sectional design limitations
- Omitted confounders (income, education, household size)

**Section 5.3: Practical Implications**
- Policy: Support outlet type diversity, not just single food source
- Planning: Urban food systems require multi-outlet access
- Intervention design: Broaden beyond market accessibility alone

**Section 5.4: Limitations (PROMINENT SECTION)**
- **Sample Size Reduction**: 70% listwise deletion in full model
- **Underpowered Models**: Personal and Full models violate sample size requirements
- **Overfitting**: Full model has negative adjusted R² (1:4.6 predictor ratio)
- **Weak Relationships**: No regression models achieved significance
- **Measurement**: 24-hour HDDS recall, perception-based predictors
- **Design**: Cross-sectional (no causality), single timepoint
- **Generalizability**: Urban Vietnam specificity, selection bias

**Section 5.5: Future Research Directions**
- Larger samples (n≥300) for stable regression estimates
- Objective food environment measures (GIS, audits)
- Longitudinal design with multiple HDDS measurements
- Multilevel models (households nested in neighborhoods)
- Non-linear specifications (thresholds, splines)
- Outlet diversity indices (building on OP028)

---

## 🚨 Critical Framing Guidance

### What to Emphasize

✅ **Exploratory Nature**: Frame entire analysis as pilot study, not confirmatory research
✅ **Novel Contribution**: OP028 (Outlet Frequency Variation) finding is reliable and important
✅ **Methodological Transparency**: Report all limitations prominently and honestly
✅ **Weak Effects Documented**: Present non-significant models without overstating implications
✅ **Urban LMIC Context**: Unique setting contributes to literature gap

---

### What to Avoid

❌ **"Validated Turner Framework"**: Models are non-significant, cannot claim validation
❌ **Causal Language**: Cross-sectional design precludes causal inference
❌ **Overgeneralization**: Sample size and context limit generalizability
❌ **Ignoring Overfitting**: Negative adjusted R² must be acknowledged
❌ **Suppressing Non-Significance**: Report all models, including failed ones

---

### Recommended Language Templates

**For Regression Results**:
> "The full Turner Framework regression model (Table 4C) did not achieve statistical significance (F(13,50)=0.92, p=0.537), suggesting weak linear relationships between food environment perceptions and dietary diversity in this sample. However, standardized coefficients (Table 5, Figure 5) provide exploratory insights into relative effect sizes..."

**For Sample Size Reduction**:
> "Due to listwise deletion across 14 predictors with varying missing data patterns, the full model sample was reduced to N=64 households (29.9% of the total sample). This 70% data loss substantially reduced statistical power and introduced potential selection bias..."

**For OP028 Finding**:
> "Outlet frequency variation (OP028) emerged as the strongest and only significant bivariate predictor of dietary diversity (r=0.542, p<0.001, N=214). This finding suggests that households sourcing food from a diverse array of outlet types (high variation in shopping frequency across outlet categories) exhibit significantly higher dietary diversity..."

**For Overall Framing**:
> "This pilot study provides exploratory evidence regarding the Turner Framework's applicability to urban Vietnamese household food environments. While regression models did not achieve statistical significance—likely due to sample size constraints, perception-based measurement, and omitted confounders—the analysis identified outlet sourcing diversity as a promising avenue for future research..."

---

## 📊 Data Availability Statement (For Thesis)

### Recommended Text:

> "All data and analysis code are available in the project repository: https://github.com/faucetpoop/WFL-Analysis"
>
> **Summary Datasets**:
> - `household_analysis_final.csv`: Complete dataset with 25 OP variables (N=214)
> - `t2_comparison_results.csv`: Tier 2 bivariate comparison summaries
> - `correlation_summary.csv`: Complete HDDS correlation matrix
>
> **Analysis Scripts** (Python 3.9+, open-source):
> - Phase 0: Data consolidation and EDA
> - Phase 1: Variable construction and operationalization
> - Phase 2: Tier 1 descriptive statistics and Tier 2 group comparisons
> - Phase 3: Tier 3 correlation analysis and Tier 4 regression modeling
> - Phase 4: Visualization and thesis integration
>
> **Reproducibility**: All analyses are fully reproducible using provided scripts and datasets. See `README_FIRST.txt` for setup instructions.

---

## 📋 Thesis Integration Checklist

### Pre-Writing Phase
- [ ] Review all 13 tables and understand key findings
- [ ] Review all 5 figures and identify key visual insights
- [ ] Read Phase 3 SIGNOFF document thoroughly (limitations!)
- [ ] Confirm sample sizes for each analysis (vary by missing data)
- [ ] Understand why regression models are non-significant

### Writing Phase - Chapter 4 Results
- [ ] **Section 4.1**: Integrate Tables 1A-B and Figure 1 (sample characteristics)
- [ ] **Section 4.2**: Integrate Tables 2A-C and Figures 2-4 (bivariate analyses)
- [ ] **Section 4.3**: Integrate Tables 3A, 3C (correlation analysis)
- [ ] **Section 4.4**: Integrate Tables 4A, 4C, 5 and Figure 5 (regression)
- [ ] **Section 4.5**: Synthesize key findings (emphasize OP028)

### Writing Phase - Chapter 5 Discussion
- [ ] **Section 5.1**: Interpret OP028 finding (outlet diversity)
- [ ] **Section 5.2**: Explain weak framework relationships
- [ ] **Section 5.3**: Practical implications for policy and intervention
- [ ] **Section 5.4**: **LIMITATIONS section prominent and comprehensive**
- [ ] **Section 5.5**: Future research directions with specifics

### Quality Checks
- [ ] All 13 tables referenced at least once in thesis
- [ ] All 5 figures referenced at least once in thesis
- [ ] Sample sizes reported for all analyses
- [ ] Limitations acknowledged for every major finding
- [ ] Non-significant results clearly stated (not hidden)
- [ ] No causal language used (cross-sectional design)
- [ ] Exploratory framing used throughout
- [ ] OP028 contribution highlighted prominently

---

## 🎓 Committee Preparation

### Anticipated Questions

**Q1: "Why are the regression models non-significant?"**
**A**: Sample size reduction (70% listwise deletion), perception-based measures (not objective), omitted confounders (income, education), and possible weak true effects in this context.

**Q2: "Can you claim the Turner Framework is validated?"**
**A**: No. The non-significant models suggest weak linear relationships in this sample. We frame this as exploratory pilot work, not framework validation.

**Q3: "What is the novel contribution of this work?"**
**A**: OP028 finding—outlet frequency variation (sourcing diversity) as strongest predictor (r=0.542***). Challenges single-outlet research focus and suggests multi-source food access matters most.

**Q4: "How do you address the 70% data loss in full model?"**
**A**: Acknowledge prominently in limitations. Likely introduced selection bias and reduced power. Future work needs larger samples with targeted data collection to minimize missingness.

**Q5: "Are findings generalizable beyond this sample?"**
**A**: Limited. Urban Vietnam context, small sample post-deletion, cross-sectional design, and perception-based measures restrict generalizability. Frame as hypothesis-generating for future research.

---

## 📞 Support Resources

### For Questions on Specific Tables/Figures:
- **Completion Logs**: `03_logs/PHASE_[0-3]_COMPLETION_LOG.md`
- **Phase Documentation**: `PLANNING/Phase_[0-4]/`
- **Variable Definitions**: `DOCUMENTATION/REFERENCE/OPERATIONALIZATION_MASTER_*.md`

### For Analysis Methodology:
- **Phase 3 Signoff**: `03_logs/PHASE_3_SIGNOFF.md` (comprehensive limitations!)
- **Analysis Scripts**: `01_scripts/phase_[0-4]_*.py`
- **Survey Instruments**: `00_inputs/survey_instruments/household-survey-codebook.md`

### For Data Quality Issues:
- **EDA Reports**: `03_logs/phase_0_eda_comprehensive_report.md`
- **Cleaning Logs**: `03_logs/EXPENDITURE_CLEANING_DOCUMENTATION.md`
- **Variable Audit**: `03_logs/VARIABLE_LABEL_AUDIT_COMPLETE.md`

---

**Document Version**: 1.0
**Last Updated**: 2025-11-23
**Status**: ✅ COMPLETE AND READY FOR THESIS WRITING

---

**Next Steps**:
1. Review this guide thoroughly before starting thesis writing
2. Cross-reference with Phase 3 SIGNOFF for limitations
3. Integrate tables and figures systematically by chapter section
4. Prepare responses to anticipated committee questions
5. Maintain exploratory framing throughout all results reporting

**Phase 4 Thesis Integration Guide - COMPLETE**
