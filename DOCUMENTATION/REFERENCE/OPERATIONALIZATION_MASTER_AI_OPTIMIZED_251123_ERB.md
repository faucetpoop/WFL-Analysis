---
title: "Turner Framework Operationalization Master Index"
subtitle: "AI-Optimized Structured Reference for WFL-Analysis Thesis"
author: "Emerson Richmond Burke"
date: 2025-11-23
version: "1.0 (AI-Optimized)"
type: "operationalization-reference"
status: "active"
machine_readable: true
---

# Turner Framework Operationalization: AI-Optimized Master Reference

## 📋 Document Purpose

This document replaces the Excel-based operationalization table with a **comprehensive, AI-friendly, plain-text reference** that:

- ✅ Maintains complete operationalization mapping (all 33 OPs)
- ✅ Uses structured markdown/YAML for easy parsing by AI and code
- ✅ Enables version control and diff-tracking
- ✅ Provides multiple lookup methods (by OP_ID, Domain, Role, Status)
- ✅ Grounds workflow analysis and methodology validation
- ✅ Integrates with analysis scripts (copy/paste variable names, filter patterns)

## 🎯 Quick Navigation

- **[Complete Operationalization Index](#complete-operationalization-index)** – All 33 OPs in structured format
- **[Lookup Tables](#lookup-tables)** – By domain, status, role, research question
- **[Data Verification Checklist](#data-verification-checklist)** – Variables to confirm in datasets
- **[Analysis Workflow Mapping](#analysis-workflow-mapping)** – T1/T2/T4 structure
- **[YAML Export](#yaml-export-for-parsing)** – Structured format for code/tools
- **[JSON Export](#json-export-for-tools)** – Machine-readable format
- **[Variable Name Index](#variable-name-index)** – Quick reference for all data variables

---

## 📊 Master Summary Statistics

| Category | Count | Status | Notes |
|----------|-------|--------|-------|
| **Total Operationalizations** | 33 | 100% mapped | All Turner components + emergent |
| **In Data (Ready for Analysis)** | 31 | 94% ✅ | Can be used in T1-T2-T4 analyses |
| **Planned Only (Documented Limitation)** | 2 | 6% ⚠️ | OP008, OP024, OP027 |
| **External Domain** | 8 | Complete | 1 unmeasured (OP008) |
| **Personal Domain** | 16 | Complete | All in data except OP024 |
| **Emergent Dimensions** | 4 | Extended | Food safety, social forces, stability |
| **Outcome Variables** | 5 | Complete | DDS + diet composition + quality tier |

---

## 🔑 The "Big Three" for Analysis

These three variables drive your **T2 stratification** and group comparison analyses:

| OP_ID | Variable | Role | Stratification | Data File | Key Use |
|-------|----------|------|-----------------|-----------|---------|
| **OP016** | Food Budget Share | T2 IV | 3 tiers (low/med/high) | household | **PRIMARY**: DDS by affordability |
| **OP011** | Accessibility Tier | T2 IV | 2 tiers (≤5 vs >5 min) | household | **PRIMARY**: DDS by accessibility |
| **OP025** | Food Safety Index | T2 IV | 2 tiers (low vs high) | household | **SECONDARY**: DDS by safety perception |

---

## Complete Operationalization Index

### **EXTERNAL DOMAIN (OP001-OP008)**

Objective features of the food environment that exist independently of household characteristics.

---

#### **OP001: Vendor Availability - Nutrient-dense Food Groups**

| Field | Value |
|-------|-------|
| Domain | External |
| Turner Component | Availability |
| Theoretical Construct | Vendor Availability - Nutrient-dense Food Groups |
| ODK Variable | `foodgroups_001_cereals` through `foodgroups_001_oils_fats` |
| ODK Item Label | Which food groups does your outlet sell? (binary for each: cereals, dark leafy veg, fruits with vitamin A, fish/seafood, meat, eggs, milk/dairy, legumes/nuts/seeds, sweets, oils/fats) |
| Response Format | Binary (yes/no per food group) |
| Data File | `data_vendor_survey.csv` |
| Data Variable(s) | `foodgroups_001_*` |
| Coding | 1=yes, 0=no |
| Role in Analysis | IV (external domain descriptor) |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | % vendors selling nutrient-dense vs. processed groups; outlet-level analysis |
| Status | ✅ in_data |

---

#### **OP002: Outlet Classification**

| Field | Value |
|-------|-------|
| Domain | External |
| Turner Component | Availability |
| Theoretical Construct | Outlet Classification |
| ODK Variable | `vendor_type` OR `outlet_classification` |
| ODK Item Label | Type of food retail outlet |
| Response Format | Categorical |
| Data File | `data_vendor_survey.csv` |
| Data Variable(s) | `vendor_type` |
| Coding | wet_market, supermarket, street_vendor, wholesaler, retail_shop |
| Role in Analysis | IV (external domain descriptor) |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Stratification variable for outlet type comparison |
| Status | ✅ in_data |

---

#### **OP003: Price Affordability - Perceived**

| Field | Value |
|-------|-------|
| Domain | External |
| Turner Component | Prices |
| Theoretical Construct | Price Affordability - Perceived |
| ODK Variable | `reason_003` |
| ODK Item Label | HH cites 'cheap' or 'low price' as reason for choosing outlet |
| Response Format | Binary |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `reason_cheap_motive` |
| Coding | 1=cheap cited as motive, 0=not cited |
| Role in Analysis | IV (external domain proxy) |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | ⚠️ Perceived price proxy; no direct price audit conducted; single-item measure; weak proxy for actual prices |
| Status | ✅ in_data |

---

#### **OP004: Perceived Vendor Cleanliness**

| Field | Value |
|-------|-------|
| Domain | External |
| Turner Component | Vendor & Product Properties |
| Theoretical Construct | Perceived Food Safety/Quality - Vendor Cleanliness |
| ODK Variable | `clean` |
| ODK Item Label | HH perception of vendor outlet cleanliness (Likert scale) |
| Response Format | Ordinal (1-5 or 1-7) |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `vendor_clean` |
| Coding | 1=very dirty, 5=very clean (or 1-7 scale) |
| Role in Analysis | IV (component of safety index) |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Aggregate into `safety_quality_index`; single-item perception measure |
| Status | ✅ in_data |

---

#### **OP005: Perceived Food Safety**

| Field | Value |
|-------|-------|
| Domain | External |
| Turner Component | Vendor & Product Properties |
| Theoretical Construct | Perceived Food Safety/Quality - Food Safety |
| ODK Variable | `safe` |
| ODK Item Label | HH perception of food safety at outlet (Likert scale) |
| Response Format | Ordinal (1-5 or 1-7) |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `vendor_safe` |
| Coding | 1=very unsafe, 5=very safe (or 1-7 scale) |
| Role in Analysis | IV (component of safety index) |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Aggregate into `safety_quality_index`; single-item perception measure |
| Status | ✅ in_data |

---

#### **OP006: Perceived Vendor Reputation/Trust**

| Field | Value |
|-------|-------|
| Domain | External |
| Turner Component | Vendor & Product Properties |
| Theoretical Construct | Perceived Vendor Trust/Reputation |
| ODK Variable | `reputation` |
| ODK Item Label | HH perception of vendor trustworthiness (Likert scale) |
| Response Format | Ordinal (1-5 or 1-7) |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `vendor_reputation` |
| Coding | 1=untrustworthy, 5=highly trustworthy (or 1-7 scale) |
| Role in Analysis | IV (component of safety index) |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Aggregate into `safety_quality_index`; desirability component |
| Status | ✅ in_data |

---

#### **OP007: Vendor Infrastructure Adequacy**

| Field | Value |
|-------|-------|
| Domain | External |
| Turner Component | Vendor & Product Properties |
| Theoretical Construct | Vendor Infrastructure Adequacy |
| ODK Variable | `infrastructure` |
| ODK Item Label | Vendor-reported infrastructure quality (shelving, storage, refrigeration, cleanliness) |
| Response Format | Categorical/Ordinal |
| Data File | `data_vendor_survey.csv` |
| Data Variable(s) | `vendor_infrastructure` |
| Coding | Categories for cold chain, storage quality, cleanliness |
| Role in Analysis | IV (external domain descriptor) |
| RQ/Hypothesis | RQ1 |
| Limitations | Vendor-reported not HH-observed; limited information on actual conditions |
| Status | ✅ in_data |

---

#### **OP008: Marketing & Regulation Impacts**

| Field | Value |
|-------|-------|
| Domain | External |
| Turner Component | Marketing & Regulation |
| Theoretical Construct | Marketing & Regulation Impacts |
| ODK Variable | ❌ **NOT MEASURED** |
| ODK Item Label | Advertising, promotion, policy enforcement, media exposure |
| Response Format | Not measured |
| Data File | Not collected |
| Data Variable(s) | Not applicable |
| Coding | Not applicable |
| Role in Analysis | **Limitation only** - not included in analysis |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | ⚠️ **HIGH SEVERITY**: Direct observation of marketing/advertising not conducted; regulatory enforcement not audited; gap in framework operationalization |
| Status | ⚠️ **planned_only** |

---

### **PERSONAL DOMAIN (OP009-OP024)**

Individual and household characteristics that mediate how people experience the food environment.

---

#### **OP009: Travel Time - General**

| Field | Value |
|-------|-------|
| Domain | Personal |
| Turner Component | Accessibility |
| Theoretical Construct | Travel Time - General |
| ODK Variable | `transportation_001` through `transportation_007` |
| ODK Item Label | Minutes to reach each outlet type (supermarket, large supermarket, market, street vendor, wholesaler, retail shop, other) |
| Response Format | Continuous (minutes) |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `time_to_[outlet_type]` |
| Coding | Numeric (minutes) |
| Role in Analysis | IV (accessibility tier) |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Measured travel time for each outlet type; stratify as ≤5 min (close) vs >5 min (far) |
| Status | ✅ in_data |

---

#### **OP010: Travel Frequency**

| Field | Value |
|-------|-------|
| Domain | Personal |
| Turner Component | Accessibility |
| Theoretical Construct | Travel Frequency |
| ODK Variable | `supermarket_freq`, `largesupermarket_freq`, `market_freq`, `streetven_freq`, `wholesaler_freq`, `retail_freq` |
| ODK Item Label | How often HH shops at each outlet type (daily, weekly, monthly, occasional) |
| Response Format | Categorical/Ordinal |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `[outlet_type]_freq` |
| Coding | 1=daily, 2=weekly, 3=monthly, 4=occasional |
| Role in Analysis | IV (accessibility descriptor) |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Outlet diversity index derived from frequency patterns |
| Status | ✅ in_data |

---

#### **OP011: Accessibility Tier (T2 Stratification) ⭐**

| Field | Value |
|-------|-------|
| Domain | Personal |
| Turner Component | Accessibility |
| Theoretical Construct | Accessibility Tier |
| ODK Variable | **Derived from** `transportation_*` |
| ODK Item Label | Binary classification: close access (≤5 min) vs. far access (>5 min) |
| Response Format | Binary |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `accessibility_tier` |
| Coding | 1=close (≤5 min), 0=far (>5 min) |
| Role in Analysis | **IV (T2 stratification variable)** ⭐ PRIMARY |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Categorical for group comparison; 5-min threshold based on urban context reasoning |
| Status | ✅ in_data |
| Analysis Use | **Tier 2 group comparisons**: DDS by accessibility tier (close vs. far) |

---

#### **OP012: Food Expenditure Amount**

| Field | Value |
|-------|-------|
| Domain | Personal |
| Turner Component | Affordability |
| Theoretical Construct | Food Expenditure Amount |
| ODK Variable | `foodexpenditure` |
| ODK Item Label | Household food spending (amount) |
| Response Format | Continuous (currency) |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `food_exp_amount` |
| Coding | VND or USD per time period |
| Role in Analysis | IV (component of affordability) |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Currency and time period must be standardized |
| Status | ✅ in_data |

---

#### **OP013: Food Expenditure Time Unit**

| Field | Value |
|-------|-------|
| Domain | Personal |
| Turner Component | Affordability |
| Theoretical Construct | Food Expenditure Time Unit |
| ODK Variable | `foodexp_timeunit` |
| ODK Item Label | Period for food expenditure reporting |
| Response Format | Categorical |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `food_exp_period` |
| Coding | daily, weekly, monthly |
| Role in Analysis | Control variable for standardization |
| RQ/Hypothesis | RQ1 |
| Limitations | Standardize all to monthly equivalent for food budget share calculation |
| Status | ✅ in_data |

---

#### **OP014: Income Proxy**

| Field | Value |
|-------|-------|
| Domain | Personal |
| Turner Component | Affordability |
| Theoretical Construct | Income Proxy |
| ODK Variable | `income` OR housing/asset variables |
| ODK Item Label | Household income or proxy indicators (house ownership, asset ownership, livelihood type) |
| Response Format | Categorical/Ordinal |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `income_proxy` |
| Coding | Categorical (low/medium/high) or asset indices |
| Role in Analysis | Control variable |
| RQ/Hypothesis | RQ1 |
| Limitations | ⚠️ Direct income may not be collected; use asset ownership as proxy; acknowledge measurement limitation |
| Status | ✅ in_data |

---

#### **OP015: Affordability Motive**

| Field | Value |
|-------|-------|
| Domain | Personal |
| Turner Component | Affordability |
| Theoretical Construct | Affordability Motive |
| ODK Variable | `reason_003` |
| ODK Item Label | HH cites 'cheap' as reason for choosing outlet (affordability-driven) |
| Response Format | Binary |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `affordability_motive` |
| Coding | 1=affordability is motive, 0=not |
| Role in Analysis | IV (affordability descriptor) |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Same as prices reason_003; overlaps with perceived price accessibility |
| Status | ✅ in_data |

---

#### **OP016: Food Budget Share Tier (T2 Stratification) ⭐**

| Field | Value |
|-------|-------|
| Domain | Personal |
| Turner Component | Affordability |
| Theoretical Construct | Food Budget Share (Derived) |
| ODK Variable | **Derived**: `foodexpenditure / estimated_income` |
| ODK Item Label | Food spending as % of estimated monthly income |
| Response Format | Continuous (%) |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `food_budget_share_pct` |
| Coding | 0-100% (or decimal 0-1) |
| Role in Analysis | **IV (T2 stratification variable)** ⭐ PRIMARY |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Analyst-derived; requires income estimation or proxy conversion; tertile stratification (low/med/high) |
| Status | ✅ in_data |
| Analysis Use | **Tier 2 group comparisons**: DDS by affordability tier (low/medium/high budget share) |

---

#### **OP017: Proximity Motive**

| Field | Value |
|-------|-------|
| Domain | Personal |
| Turner Component | Convenience |
| Theoretical Construct | Proximity Motive |
| ODK Variable | `reason_001`, `reason_002` |
| ODK Item Label | HH cites 'close' or 'neighborhood' as reason for choosing outlet |
| Response Format | Binary |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `proximity_motive` |
| Coding | 1=proximity cited, 0=not |
| Role in Analysis | IV (convenience descriptor) |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Multi-item; aggregates into convenience score |
| Status | ✅ in_data |

---

#### **OP018: Cooking Infrastructure Access**

| Field | Value |
|-------|-------|
| Domain | Personal |
| Turner Component | Convenience |
| Theoretical Construct | Cooking Infrastructure Access |
| ODK Variable | `cookingsource` |
| ODK Item Label | Access to cooking infrastructure (gas, electricity, charcoal, other) |
| Response Format | Categorical |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `cooking_source` |
| Coding | gas, electricity, charcoal, none, other |
| Role in Analysis | IV (convenience component) |
| RQ/Hypothesis | RQ1 |
| Limitations | Measured as presence/type; part of preparation infrastructure |
| Status | ✅ in_data |

---

#### **OP019: Water Source Access**

| Field | Value |
|-------|-------|
| Domain | Personal |
| Turner Component | Convenience |
| Theoretical Construct | Water Source Access |
| ODK Variable | `watersource` |
| ODK Item Label | Access to water for cooking/washing |
| Response Format | Categorical |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `water_source` |
| Coding | tap water, well, other |
| Role in Analysis | IV (convenience component) |
| RQ/Hypothesis | RQ1 |
| Limitations | Related to preparation convenience; affects food processing |
| Status | ✅ in_data |

---

#### **OP020: Water Distance**

| Field | Value |
|-------|-------|
| Domain | Personal |
| Turner Component | Convenience |
| Theoretical Construct | Water Distance (if not in-home) |
| ODK Variable | `waterdistance_001` |
| ODK Item Label | Distance to water if not in household |
| Response Format | Continuous or Categorical |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `water_distance` |
| Coding | Meters OR in-house, <50m, <100m, >100m |
| Role in Analysis | IV (convenience descriptor) |
| RQ/Hypothesis | RQ1 |
| Limitations | Secondary to in-home water access |
| Status | ✅ in_data |

---

#### **OP021: Health/Nutrition Motive**

| Field | Value |
|-------|-------|
| Domain | Personal |
| Turner Component | Desirability |
| Theoretical Construct | Health/Nutrition Motive |
| ODK Variable | `reason_004` |
| ODK Item Label | HH cites 'healthy' or 'nutritious' as reason for shopping |
| Response Format | Binary |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `health_motive` |
| Coding | 1=health is motive, 0=not |
| Role in Analysis | IV (desirability component) |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Single-item indicator; weak proxy for dietary intention |
| Status | ✅ in_data |

---

#### **OP022: Trust Motive (Social Capital)**

| Field | Value |
|-------|-------|
| Domain | Personal |
| Turner Component | Desirability |
| Theoretical Construct | Trust Motive |
| ODK Variable | `reason_005` |
| ODK Item Label | HH cites 'trust' in vendor or food quality as reason |
| Response Format | Binary |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `trust_motive` |
| Coding | 1=trust is motive, 0=not |
| Role in Analysis | IV (desirability component; social forces) |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Reflects social capital and vendor relationship strength |
| Status | ✅ in_data |

---

#### **OP023: Food Environment Quality Perception**

| Field | Value |
|-------|-------|
| Domain | Personal |
| Turner Component | Desirability |
| Theoretical Construct | Food Environment Quality Perception |
| ODK Variable | `foodenvironment_002` |
| ODK Item Label | Perception of neighborhood food environment quality (Likert) |
| Response Format | Ordinal |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `foodenv_quality_perception` |
| Coding | Scale depends on original; typically 1-5 or 1-7 |
| Role in Analysis | IV (desirability descriptor) |
| RQ/Hypothesis | RQ1 |
| Limitations | Neighborhood-level perception; overlaps with safety/quality index |
| Status | ✅ in_data |

---

#### **OP024: Food Preference/Habit**

| Field | Value |
|-------|-------|
| Domain | Personal |
| Turner Component | Desirability |
| Theoretical Construct | Food Preference/Habit |
| ODK Variable | `preference_*` OR `habit_*` |
| ODK Item Label | Preference for certain foods or vendors (if collected) |
| Response Format | Categorical |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `food_preference` |
| Coding | Categorical (e.g., prefer fish, always buy from vendor X) |
| Role in Analysis | IV (desirability descriptor) |
| RQ/Hypothesis | RQ1 |
| Limitations | ⚠️ May not be systematically collected; cultural/behavioral dimension |
| Status | ⚠️ **planned_only** |

---

### **EMERGENT DIMENSIONS (OP025-OP028)**

Extensions beyond Turner's core 8 that emerged from LMIC context and recent literature.

---

#### **OP025: Food Safety Index (T2 Stratification) ⭐**

| Field | Value |
|-------|-------|
| Domain | Emergent |
| Turner Component | Food Safety |
| Theoretical Construct | Food Safety Index (Derived) |
| ODK Variable | **Aggregate**: `clean` + `safe` (+ `reputation`) |
| ODK Item Label | Perceived safety/quality score = mean(clean, safe) or mean(clean, safe, reputation) |
| Response Format | Continuous (0-100) |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `food_safety_index` |
| Coding | 0-100 or z-standardized |
| Role in Analysis | **IV (T2 stratification variable)** ⭐ SECONDARY |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Z-standardized aggregate; internal consistency via Cronbach's ω; overlaps with external vendor properties domain |
| Status | ✅ in_data |
| Composition | Combines OP004 (clean) + OP005 (safe) + OP006 (reputation) |
| Analysis Use | **Tier 2 group comparisons**: DDS by safety perception tier (low vs. high) |

---

#### **OP026: Trust-Based Shopping (Social Capital)**

| Field | Value |
|-------|-------|
| Domain | Emergent |
| Turner Component | Social Forces |
| Theoretical Construct | Vendor Relationship - Trust-Based Shopping |
| ODK Variable | `trust_motive` (`reason_005`) + vendor frequency concentration |
| ODK Item Label | High trust in vendor as primary shopping motive; outlet loyalty (concentrated visits) |
| Response Format | Binary + Continuous |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `trust_based_shopping` |
| Coding | 1=trust is primary motive, 0=not; Herfindahl-type concentration index |
| Role in Analysis | IV (social capital descriptor) |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Reflects intra-community relationships and social capital; gender of food decision-maker could extend this |
| Status | ✅ in_data |

---

#### **OP027: Food Decision-Maker Gender**

| Field | Value |
|-------|-------|
| Domain | Emergent |
| Turner Component | Social Forces |
| Theoretical Construct | Food Decision-Maker Gender |
| ODK Variable | `gender_food_decisionmaker` |
| ODK Item Label | Gender of primary household food decision-maker (M/F/joint) |
| Response Format | Categorical |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `food_decision_maker_gender` |
| Coding | M, F, joint |
| Role in Analysis | IV (stratification for social forces) |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | ⚠️ Gendered dimension of food environments; relevant for women's access and agency |
| Status | ⚠️ **planned_only** |

---

#### **OP028: Outlet Usage Frequency Variation (Stability)**

| Field | Value |
|-------|-------|
| Domain | Emergent |
| Turner Component | Stability |
| Theoretical Construct | Outlet Usage Frequency Variation |
| ODK Variable | Frequency variables: `*_freq` across outlet types |
| ODK Item Label | Consistency of food source access over time (SD of frequencies across outlet types) |
| Response Format | Continuous |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `outlet_frequency_variation` |
| Coding | Standard deviation or coefficient of variation |
| Role in Analysis | IV (stability descriptor) |
| RQ/Hypothesis | RQ1 |
| Limitations | ⚠️ Single-timepoint survey limits temporal analysis; only within-respondent variation available |
| Status | ✅ in_data |

---

### **OUTCOME VARIABLES (OP029-OP033)**

Dietary outcomes that are your dependent variables.

---

#### **OP029: Dietary Diversity Score (DDS) - PRIMARY OUTCOME**

| Field | Value |
|-------|-------|
| Domain | Outcome |
| Turner Component | Diet Outcomes |
| Theoretical Construct | Dietary Diversity Score |
| ODK Variable | `foodgroups_001_*` (11-12 food group items) |
| ODK Item Label | 24-hour food recall: which food groups did you consume? (binary for each group) |
| Response Format | Binary (yes/no per food group) |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `DDS` or `dietary_diversity_score` |
| Coding | Count (0-12): sum of all foodgroup_001_* items |
| Role in Analysis | **Dependent Variable (DV)** - PRIMARY OUTCOME |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | 24-hour recall; cross-sectional snapshot; not seasonal variation |
| Status | ✅ in_data |
| Analysis Use | **Tier 1**: Mean, SD by domain; **Tier 2**: Compare by strata (OP011, OP016, OP025) |

---

#### **OP030: % Nutrient-Dense Food Groups**

| Field | Value |
|-------|-------|
| Domain | Outcome |
| Turner Component | Diet Outcomes |
| Theoretical Construct | Food Type Quality - Nutrient-Dense |
| ODK Variable | **Derived** from `foodgroups_001_*` classification |
| ODK Item Label | Proportion of nutrient-dense groups consumed (vs. processed/empty calories) |
| Response Format | Continuous (%) |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `pct_nutrient_dense` |
| Coding | 0-100%; analyst-classified groups |
| Role in Analysis | Dependent Variable (DV) - Secondary outcome |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Classification of "nutrient-dense" vs. "processed" is analyst judgment |
| Status | ✅ in_data |

---

#### **OP031: % Processed Food Groups**

| Field | Value |
|-------|-------|
| Domain | Outcome |
| Turner Component | Diet Outcomes |
| Theoretical Construct | Food Type Quality - Processed |
| ODK Variable | **Derived** from `foodgroups_001_*` classification |
| ODK Item Label | Proportion of processed/low-nutrition groups consumed |
| Response Format | Continuous (%) |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `pct_processed` |
| Coding | 0-100%; analyst-classified groups |
| Role in Analysis | Dependent Variable (DV) - Secondary outcome |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Inverse of OP030; overlapping dimension |
| Status | ✅ in_data |

---

#### **OP032: Diet Quality Composition**

| Field | Value |
|-------|-------|
| Domain | Outcome |
| Turner Component | Diet Outcomes |
| Theoretical Construct | Food Type Quality - Composition |
| ODK Variable | **Derived** classification: whole/processed binary |
| ODK Item Label | Aggregated diet composition tier (nutrient-dense focused vs. mixed vs. processed-heavy) |
| Response Format | Categorical/Ordinal |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `diet_composition_tier` |
| Coding | 1=nutrient-dense, 2=mixed, 3=processed-heavy |
| Role in Analysis | Dependent Variable (DV) - Secondary outcome |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Derived classification; three categories may be reductive |
| Status | ✅ in_data |

---

#### **OP033: Diet Quality Category**

| Field | Value |
|-------|-------|
| Domain | Outcome |
| Turner Component | Diet Outcomes |
| Theoretical Construct | Diet Quality Category (Categorical Summary) |
| ODK Variable | **Derived** from DDS + composition |
| ODK Item Label | Overall dietary quality classification |
| Response Format | Categorical |
| Data File | `data_household_survey.csv` |
| Data Variable(s) | `diet_quality_category` |
| Coding | Poor, Adequate, Diverse (based on DDS thresholds + composition) |
| Role in Analysis | Dependent Variable (DV) - Secondary outcome |
| RQ/Hypothesis | RQ1, RQ2 |
| Limitations | Categorical simplification of continuous DDS |
| Status | ✅ in_data |

---

## Lookup Tables

### By Domain

#### External Domain (OP001-OP008)

| OP_ID | Variable | Status | Use |
|-------|----------|--------|-----|
| OP001 | Vendor Availability - Food Groups | ✅ in_data | T1 Descriptive |
| OP002 | Outlet Classification | ✅ in_data | T1 Descriptive + Stratification |
| OP003 | Price Affordability Motive | ✅ in_data | T1, T2 |
| OP004 | Vendor Cleanliness | ✅ in_data | T1 + Safety Index |
| OP005 | Food Safety Perception | ✅ in_data | T1 + Safety Index |
| OP006 | Vendor Reputation | ✅ in_data | T1 + Safety Index |
| OP007 | Vendor Infrastructure | ✅ in_data | T1 Descriptive |
| OP008 | Marketing & Regulation | ⚠️ planned_only | **Not in analysis** (Limitation) |

#### Personal Domain (OP009-OP024)

| OP_ID | Variable | Status | Use |
|-------|----------|--------|-----|
| OP009 | Travel Time - General | ✅ in_data | T1 Descriptive |
| OP010 | Travel Frequency | ✅ in_data | T1 Descriptive |
| OP011 | Accessibility Tier ⭐ | ✅ in_data | **T2 Primary Stratification** |
| OP012 | Food Expenditure Amount | ✅ in_data | T1 + Budget Share |
| OP013 | Expenditure Time Unit | ✅ in_data | Standardization |
| OP014 | Income Proxy | ✅ in_data | Control |
| OP015 | Affordability Motive | ✅ in_data | T1, T2 |
| OP016 | Food Budget Share Tier ⭐ | ✅ in_data | **T2 Primary Stratification** |
| OP017 | Proximity Motive | ✅ in_data | T1, T2 |
| OP018 | Cooking Infrastructure | ✅ in_data | T1 Descriptive |
| OP019 | Water Source | ✅ in_data | T1 Descriptive |
| OP020 | Water Distance | ✅ in_data | T1 Descriptive |
| OP021 | Health Motive | ✅ in_data | T1, T2 |
| OP022 | Trust Motive | ✅ in_data | T1, T2 + Social Capital |
| OP023 | Food Env. Quality Perception | ✅ in_data | T1 Descriptive |
| OP024 | Food Preference/Habit | ⚠️ planned_only | **Not in analysis** (Limitation) |

#### Emergent Dimensions (OP025-OP028)

| OP_ID | Variable | Status | Use |
|-------|----------|--------|-----|
| OP025 | Food Safety Index ⭐ | ✅ in_data | **T2 Secondary Stratification** |
| OP026 | Trust-Based Shopping | ✅ in_data | T1, T2 (Social Capital) |
| OP027 | Food Decision-Maker Gender | ⚠️ planned_only | **Not in analysis** (Limitation) |
| OP028 | Outlet Frequency Variation | ✅ in_data | T1 Descriptive |

#### Outcome Variables (OP029-OP033)

| OP_ID | Variable | Status | Use |
|-------|----------|--------|-----|
| OP029 | DDS - PRIMARY | ✅ in_data | **Tier 1-4 Primary DV** |
| OP030 | % Nutrient-Dense | ✅ in_data | Tier 1-2 Secondary DV |
| OP031 | % Processed | ✅ in_data | Tier 1-2 Secondary DV |
| OP032 | Diet Composition Tier | ✅ in_data | Tier 1-2 Secondary DV |
| OP033 | Diet Quality Category | ✅ in_data | Tier 1-2 Secondary DV |

---

### By Role in Analysis

#### T2 Stratification Variables (PRIMARY GROUP COMPARISON)

| OP_ID | Variable | Data Variable | Strata | Primary Use |
|-------|----------|---------------|--------|-------------|
| **OP011** | Accessibility Tier | `accessibility_tier` | Close (≤5 min) / Far (>5 min) | DDS comparison by distance |
| **OP016** | Food Budget Share | `food_budget_share_pct` | Low / Medium / High (tertiles) | DDS comparison by affordability |
| **OP025** | Food Safety Index | `food_safety_index` | Low / High (median split) | DDS comparison by safety perception |

#### Dependent Variables (DV)

| OP_ID | Variable | Data Variable | Primary? |
|-------|----------|---------------|----------|
| **OP029** | Dietary Diversity Score | `DDS` | ✅ PRIMARY |
| OP030 | % Nutrient-Dense | `pct_nutrient_dense` | Secondary |
| OP031 | % Processed | `pct_processed` | Secondary |
| OP032 | Diet Composition | `diet_composition_tier` | Secondary |
| OP033 | Diet Quality Category | `diet_quality_category` | Secondary |

#### Independent Variables - Domain Descriptors (T1 Reporting)

| Domain | OP_IDs | Variables | Count | Use |
|--------|--------|-----------|-------|-----|
| External Availability | OP001-OP002 | Vendor food groups, outlet type | 2 | T1 Descriptive |
| External Prices | OP003 | Price motive | 1 | T1, T2 |
| External Vendor Properties | OP004-OP007 | Cleanliness, safety, reputation, infrastructure | 4 | T1 Descriptive + Indexing |
| Personal Accessibility | OP009-OP011 | Travel time, frequency, tier | 3 | T1 + T2 Tier |
| Personal Affordability | OP012-OP016 | Expenditure, income, motive, tier | 5 | T1 + T2 Tier |
| Personal Convenience | OP017-OP020 | Proximity, cooking, water, distance | 4 | T1 Descriptive |
| Personal Desirability | OP021-OP024 | Health, trust, perception, preference | 4 | T1 + T2 (Subset) |

---

### By Data Availability Status

#### In Data (Ready for Analysis) - 31 OPs

```
✅ READY: OP001, OP002, OP003, OP004, OP005, OP006, OP007
✅ READY: OP009, OP010, OP011, OP012, OP013, OP014, OP015, OP016
✅ READY: OP017, OP018, OP019, OP020, OP021, OP022, OP023
✅ READY: OP025, OP026, OP028
✅ READY: OP029, OP030, OP031, OP032, OP033
```

#### Planned Only (Documented Limitations) - 2 OPs

```
⚠️ NOT MEASURED: OP008 (Marketing & Regulation)
⚠️ NOT MEASURED: OP024 (Food Preference/Habit)
⚠️ NOT MEASURED: OP027 (Food Decision-Maker Gender) [planned_only in dataset]
```

---

## Data Verification Checklist

### Before Starting Analysis - Variable Inventory

#### Household Survey Data (`data_household_survey.csv`)

**Consumption Items (OP029 - Dietary Diversity)**
- [ ] `foodgroups_001_cereals`
- [ ] `foodgroups_001_darkveg` (dark leafy vegetables)
- [ ] `foodgroups_001_vitamin_a_fruit`
- [ ] `foodgroups_001_fish` (fish/seafood)
- [ ] `foodgroups_001_meat`
- [ ] `foodgroups_001_eggs`
- [ ] `foodgroups_001_dairy`
- [ ] `foodgroups_001_legumes`
- [ ] `foodgroups_001_sweets`
- [ ] `foodgroups_001_oils_fats`
- [ ] [Additional if applicable]

**Shopping Motives (OP003, OP015, OP017, OP021, OP022)**
- [ ] `reason_001` or `reason_cheap`
- [ ] `reason_002` or `reason_proximity`
- [ ] `reason_003` or `reason_affordable`
- [ ] `reason_004` or `reason_health`
- [ ] `reason_005` or `reason_trust`

**Perception Items (OP004, OP005, OP006)**
- [ ] `vendor_clean` (cleanliness Likert)
- [ ] `vendor_safe` (food safety Likert)
- [ ] `vendor_reputation` (trustworthiness Likert)

**Accessibility Variables (OP009-OP011)**
- [ ] `transportation_001` through `transportation_007` (or similar)
- [ ] `time_to_supermarket`
- [ ] `time_to_market`
- [ ] `time_to_[outlet_type]` (for each type)

**Frequency Variables (OP010)**
- [ ] `supermarket_freq`
- [ ] `largesupermarket_freq`
- [ ] `market_freq`
- [ ] `streetven_freq` (street vendor)
- [ ] `wholesaler_freq`
- [ ] `retail_freq`

**Affordability Variables (OP012-OP016)**
- [ ] `foodexpenditure` (amount)
- [ ] `foodexp_timeunit` (period: daily, weekly, monthly)
- [ ] `income` or `income_proxy` (asset-based if available)

**Convenience Variables (OP017-OP020)**
- [ ] `cookingsource` (gas, electricity, charcoal, etc.)
- [ ] `watersource` (tap, well, other)
- [ ] `waterdistance` or `waterdistance_001`

**Other Household Survey**
- [ ] `foodenvironment_002` (neighborhood perception)
- [ ] Household size variables
- [ ] Respondent demographics

#### Vendor Survey Data (`data_vendor_survey.csv`)

**Vendor Availability (OP001-OP002, OP007)**
- [ ] `foodgroups_001_cereals` through `foodgroups_001_oils_fats` (or similar)
- [ ] `vendor_type` (wet market, supermarket, street vendor, wholesaler, retail)
- [ ] `vendor_infrastructure` (cold chain, storage, cleanliness)

#### Sample Sizes & Missing Data

- [ ] Household survey N = ________
- [ ] Vendor survey N = ________
- [ ] % Missing for each variable: ________
- [ ] Variables with >30% missing: ________
- [ ] Handling strategy (listwise deletion, imputation, etc.): ________

---

## Analysis Workflow Mapping

### Tier 1 (T1): Descriptive Statistics

**What to report**: Mean, SD, frequencies, n, missing for all "in_data" variables

**Master Table Rows**: All OP001-OP033 except OP008, OP024, OP027

**Organized by**:
- External Domain (OP001-OP007): Availability, Prices, Vendor Properties
- Personal Domain (OP009-OP023): Accessibility, Affordability, Convenience, Desirability
- Emergent (OP025-OP028): Food Safety, Social Forces, Stability
- Outcomes (OP029-OP033): DDS + Diet Quality

**Output**: Table 1 (Summary Statistics) organized by domain

---

### Tier 2 (T2): Group Comparisons

**What to test**: DV (OP029-OP033) stratified by T2 strata

**Stratification Variables**:
| Strata | OP_ID | Groups | Primary? |
|--------|-------|--------|----------|
| Accessibility | OP011 | Close (≤5 min) vs. Far (>5 min) | ✅ PRIMARY |
| Affordability | OP016 | Low / Medium / High (tertiles) | ✅ PRIMARY |
| Safety | OP025 | Low / High (median split) | Secondary |
| Social Forces | OP026-OP027 | [To be specified] | Secondary |

**Analyses to run**:
- ANOVA or t-test: DDS (OP029) by Accessibility Tier (OP011)
- ANOVA: DDS (OP029) by Affordability Tier (OP016) [3 groups]
- t-test: DDS (OP029) by Safety Index Tier (OP025)
- (Optional) Post-hoc tests, effect sizes

**Output**: Tables 2a-2d showing mean DDS and comparison statistics

---

### Tier 4 (T4): Framework Assessment

**What to compare**: Effect sizes across domains

**Analyses**:
- **Domain Comparison**: Which External vs. Personal determinants most strongly associated with DDS?
- **Individual Variable Effect Ranking**: Order all significant T2 tests by effect size
- **Interaction Analysis**: Do OP011 and OP016 interact? (accessibility × affordability)

**Output**: Table comparing domain effect sizes; interpretation of Turner framework fit

---

## Variable Name Index (Quick Reference for Coding)

### All Data Variables in Master Table

| OP_ID | Data Variable | Source File | Data Type | Use in Analysis |
|-------|---------------|-------------|-----------|-----------------|
| OP001 | `foodgroups_001_*` | vendor | Binary (array) | T1 Descriptive |
| OP002 | `vendor_type` | vendor | Categorical | T1 Stratification |
| OP003 | `reason_cheap_motive` | household | Binary | T1, T2 |
| OP004 | `vendor_clean` | household | Ordinal (1-5/1-7) | T1 + Index |
| OP005 | `vendor_safe` | household | Ordinal (1-5/1-7) | T1 + Index |
| OP006 | `vendor_reputation` | household | Ordinal (1-5/1-7) | T1 + Index |
| OP007 | `vendor_infrastructure` | vendor | Categorical/Ordinal | T1 Descriptive |
| OP008 | NOT MEASURED | - | - | - |
| OP009 | `time_to_[outlet_type]` | household | Continuous (min) | T1, Derive OP011 |
| OP010 | `[outlet_type]_freq` | household | Categorical (1-4) | T1 Descriptive |
| OP011 | `accessibility_tier` | household | Binary | **T2 Stratification** |
| OP012 | `food_exp_amount` | household | Continuous ($) | T1, Derive OP016 |
| OP013 | `food_exp_period` | household | Categorical | Standardization |
| OP014 | `income_proxy` | household | Categorical/Ordinal | T1 Control |
| OP015 | `affordability_motive` | household | Binary | T1, T2 |
| OP016 | `food_budget_share_pct` | household | Continuous (%) | **T2 Stratification** |
| OP017 | `proximity_motive` | household | Binary | T1, T2 |
| OP018 | `cooking_source` | household | Categorical | T1 Descriptive |
| OP019 | `water_source` | household | Categorical | T1 Descriptive |
| OP020 | `water_distance` | household | Continuous/Cat | T1 Descriptive |
| OP021 | `health_motive` | household | Binary | T1, T2 |
| OP022 | `trust_motive` | household | Binary | T1, T2 + Social |
| OP023 | `foodenv_quality_perception` | household | Ordinal | T1 Descriptive |
| OP024 | `food_preference` | household | Categorical | NOT IN ANALYSIS |
| OP025 | `food_safety_index` | household | Continuous (derived) | **T2 Stratification** |
| OP026 | `trust_based_shopping` | household | Binary/Continuous | T1, T2 |
| OP027 | `food_decision_maker_gender` | household | Categorical | NOT IN ANALYSIS |
| OP028 | `outlet_frequency_variation` | household | Continuous (derived) | T1 Descriptive |
| OP029 | `DDS` | household | Count (0-12) | **Primary DV All Tiers** |
| OP030 | `pct_nutrient_dense` | household | Continuous (%) | T1, T2 Secondary |
| OP031 | `pct_processed` | household | Continuous (%) | T1, T2 Secondary |
| OP032 | `diet_composition_tier` | household | Categorical (1-3) | T1, T2 Secondary |
| OP033 | `diet_quality_category` | household | Categorical | T1, T2 Secondary |

---

## YAML Export (For Parsing)

```yaml
operationalizations:
  - op_id: OP001
    domain: External
    turner_component: Availability
    theoretical_construct: "Vendor Availability - Nutrient-dense Food Groups"
    data_variable: foodgroups_001_*
    data_file: data_vendor_survey.csv
    role: "IV (external domain descriptor)"
    status: in_data

  - op_id: OP011
    domain: Personal
    turner_component: Accessibility
    theoretical_construct: "Accessibility Tier"
    data_variable: accessibility_tier
    data_file: data_household_survey.csv
    role: "IV (T2 stratification variable)"
    status: in_data
    t2_use: "Stratify DDS by close (≤5 min) vs. far (>5 min)"

  - op_id: OP016
    domain: Personal
    turner_component: Affordability
    theoretical_construct: "Food Budget Share (Derived)"
    data_variable: food_budget_share_pct
    data_file: data_household_survey.csv
    role: "IV (T2 stratification variable)"
    status: in_data
    t2_use: "Stratify DDS by low/medium/high food budget share (tertiles)"

  - op_id: OP025
    domain: Emergent
    turner_component: Food Safety
    theoretical_construct: "Food Safety Index (Derived)"
    data_variable: food_safety_index
    data_file: data_household_survey.csv
    role: "IV (T2 stratification variable)"
    status: in_data
    composition: [OP004, OP005, OP006]
    t2_use: "Stratify DDS by low vs. high safety perception"

  - op_id: OP029
    domain: Outcome
    turner_component: Diet Outcomes
    theoretical_construct: "Dietary Diversity Score"
    data_variable: DDS
    data_file: data_household_survey.csv
    role: "Dependent Variable (Primary)"
    status: in_data
    composition: "Sum of foodgroups_001_* items (count 0-12)"

limitations:
  - op_id: OP008
    status: planned_only
    severity: high
    reason: "Marketing & Regulation not measured; direct observation not conducted"

  - op_id: OP024
    status: planned_only
    severity: medium
    reason: "Food Preference/Habit may not be systematically collected"

  - op_id: OP027
    status: planned_only
    severity: medium
    reason: "Food Decision-Maker Gender may not be in dataset"

t2_strata:
  - name: Accessibility Tier
    op_id: OP011
    groups: ["Close (≤5 min)", "Far (>5 min)"]
    use: primary

  - name: Affordability Tier
    op_id: OP016
    groups: ["Low", "Medium", "High"]
    use: primary
    calculation: "food_expenditure / income * 100, then tertile split"

  - name: Safety Perception Tier
    op_id: OP025
    groups: ["Low", "High"]
    use: secondary
    calculation: "median split of food_safety_index"
```

---

## JSON Export (For Tools)

```json
{
  "metadata": {
    "title": "Turner Framework Operationalization",
    "date": "2025-11-23",
    "total_ops": 33,
    "in_data": 31,
    "planned_only": 2
  },
  "operationalizations": [
    {
      "op_id": "OP001",
      "domain": "External",
      "turner_component": "Availability",
      "theoretical_construct": "Vendor Availability - Nutrient-dense Food Groups",
      "odk_variable": "foodgroups_001_cereals through foodgroups_001_oils_fats",
      "data_file": "data_vendor_survey.csv",
      "data_variable": "foodgroups_001_*",
      "coding": "1=yes, 0=no",
      "role": "IV (external domain descriptor)",
      "status": "in_data"
    }
  ],
  "t2_stratification": [
    {
      "op_id": "OP011",
      "name": "Accessibility Tier",
      "groups": 2,
      "strata": ["Close (≤5 min)", "Far (>5 min)"],
      "primary": true
    },
    {
      "op_id": "OP016",
      "name": "Affordability Tier",
      "groups": 3,
      "strata": ["Low", "Medium", "High"],
      "primary": true
    }
  ],
  "outcomes": [
    {
      "op_id": "OP029",
      "variable": "DDS",
      "role": "primary_dv",
      "type": "count",
      "range": [0, 12]
    }
  ]
}
```

---

## Integration with Thesis Chapters

### Chapter 3 (Methods): Operationalization Section

**How to structure**:

```
3.4 Operationalization of Measures
3.4.1 External Domain Operationalization
   - Availability (OP001-OP002)
   - Prices (OP003)
   - Vendor & Product Properties (OP004-OP007)
   - Marketing & Regulation [Not measured, OP008]

3.4.2 Personal Domain Operationalization
   - Accessibility (OP009-OP011)
   - Affordability (OP012-OP016)
   - Convenience (OP017-OP020)
   - Desirability (OP021-OP024)

3.4.3 Emergent Dimensions
   - Food Safety Index (OP025)
   - Social Forces (OP026-OP027)
   - Stability (OP028)

3.4.4 Outcome Variables
   - Dietary Diversity Score (OP029)
   - Diet Composition Quality (OP030-OP033)

3.5 Study Limitations [Reference OP008, OP024, OP027]
```

### Chapter 4 (Results): Reference in Table Captions

Example: "Table 2. Dietary Diversity Score by Accessibility Tier (OP011) and Affordability Tier (OP016) – Tier 2 Group Comparisons"

### Chapter 5 (Discussion): Limitations Section

Example: "Marketing and Regulation (OP008) was not measured through direct observation or policy audit, representing a gap in full operationalization of Turner's framework. This was a deliberate design choice due to resource constraints..."

---

## Quick Troubleshooting Guide

**Q: A variable doesn't exist in my data. What do I do?**
A: (1) Search data dictionary again, (2) Check for name variations, (3) Verify it's truly missing, (4) Update Status to "NOT_FOUND", (5) Document as limitation

**Q: Should I include OP008 (Marketing & Regulation) in analysis?**
A: No. It's marked "planned_only." Document in Methods/Limitations why it wasn't measured.

**Q: How do I create OP016 (Food Budget Share)?**
A: Derive from OP012 and OP014: `food_budget_share = (food_expenditure_monthly / estimated_income) × 100`, then create tertile categories

**Q: Can I combine multiple OPs into an index?**
A: Yes! Document the method (e.g., "Food Safety Index combines OP004+OP005+OP006 using z-standardized mean, Cronbach's ω=0.78")

**Q: How do I cite operationalizations in Results?**
A: "Dietary diversity significantly varied by accessibility tier (OP011; p<0.05). Households with close access (≤5 min) consumed M=8.3 [SD=1.2] food groups compared to M=6.1 [SD=2.1] for far access."

---

## Methodological Transparency Checklist

✅ **Before Analysis**
- [ ] All 33 OPs reviewed and understood
- [ ] OP001-OP033 (except OP008, OP024, OP027) verified in data
- [ ] Sample sizes documented (n_household, n_vendor)
- [ ] Missing data patterns assessed
- [ ] T2 strata cutpoints pre-specified (OP011: 5 min; OP016: tertiles; OP025: median)

✅ **During Analysis**
- [ ] Every result references specific OP_ID(s)
- [ ] T1 descriptive stats cover all "in_data" OPs
- [ ] T2 group comparisons use pre-specified strata
- [ ] Limitations documented for OP003, OP008, OP014, OP024, OP027, OP028

✅ **In Write-up**
- [ ] Methods section explicitly cites operationalizations
- [ ] Results tables include OP_ID references
- [ ] Limitations section explains unmeasured components
- [ ] Appendix includes version of this master table

---

## Document Information

**Version**: 1.0 (AI-Optimized)
**Created**: 2025-11-23
**Status**: Active - Master Reference
**Related Files**:
- `OPERATIONALIZATION_QUICK_REFERENCE_251123_ERB.md` (Summary version)
- `OPERATIONALIZATION_MASTER_TABLE_GUIDE_251123_ERB.md` (Full user guide)
- `OPERATIONALIZATION_MASTER_TABLE_251123_ERB.xlsx` (Original Excel version)
- `Data_Analysis_Workflow_Complete.md` (Phase-by-phase analysis workflow)

**For AI/Programmatic Use**: This document uses structured markdown, YAML, and JSON for parsing. All variable names, data files, and codes are specified explicitly for code integration.

**Last Updated**: 2025-11-23
**Next Review**: After data verification complete

---

**END OF DOCUMENT**
