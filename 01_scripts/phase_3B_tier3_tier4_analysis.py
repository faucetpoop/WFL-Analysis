"""
Phase 3B: Tier 3 & 4 Statistical Analyses

Tier 3 - Correlation Analysis:
- Pearson correlation matrix for continuous predictors
- Spearman correlation matrix for robustness check
- Bivariate correlations with HDDS outcome

Tier 4 - Regression Analysis:
- Model 1: External Domain (Accessibility, Safety, etc.)
- Model 2: Personal Domain (Affordability, Resources, etc.)
- Model 3: Full Turner Framework (All predictors)
- Model 4: Interaction Effects (Accessibility × Affordability)

Generates Tables 3A-3C, 4A-4D, and 5 for thesis.

Author: Senior Data Scientist Skill (SuperClaude)
Date: 2025-11-23
Phase: 3B - Tier 3 & 4 Analyses
"""

import pandas as pd
import numpy as np
from scipy import stats
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# File paths
INPUT_PATH = Path("02_outputs/datasets/phase_3A_household_analysis_ready_COMPLETE.csv")
OUTPUT_DIR = Path("02_outputs/tables")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("="*80)
print("PHASE 3B: TIER 3 & 4 STATISTICAL ANALYSES")
print("="*80)
print()

# Load complete dataset
print(f"Loading dataset from: {INPUT_PATH}")
df = pd.read_csv(INPUT_PATH)
print(f"  ✓ Loaded {len(df)} households with {len(df.columns)} variables")
print()

# Convert categorical OP variables to numeric codes for regression
print("Converting categorical variables to numeric codes...")
categorical_vars = ['OP017_cooking_source', 'OP018_water_source']
for var in categorical_vars:
    if var in df.columns and df[var].dtype == 'object':
        # Create numeric codes (keeps NaN as NaN)
        df[f"{var}_numeric"] = pd.Categorical(df[var]).codes
        # Replace -1 (which represents NaN in categorical codes) with NaN
        df[f"{var}_numeric"] = df[f"{var}_numeric"].replace(-1, np.nan)
        print(f"  ✓ Converted {var} to {var}_numeric")
        # Use numeric version in regression
        df[var] = df[f"{var}_numeric"]
print()

# ============================================================================
# TIER 3: CORRELATION ANALYSIS
# ============================================================================

print("="*80)
print("TIER 3: CORRELATION ANALYSIS")
print("="*80)
print()

# Define continuous predictor variables for correlation analysis
continuous_predictors = [
    'OP004_cleanliness',           # External Domain
    'OP005_neighborhood_safety',   # External Domain
    'OP006_reputation',            # External Domain
    'OP007_infrastructure',        # External Domain
    'OP009_travel_time',           # External Domain (Accessibility)
    'OP012_monthly_food_expenditure',  # Personal Domain
    'OP016_budget_share_pct',      # Personal Domain (Affordability)
    'OP019_water_distance',        # Personal Domain (Resources)
    'OP023_food_env_perception',   # Personal Domain (Perception)
    'OP010_shopping_frequency',    # Personal Domain (Behavior)
    'OP028_frequency_variation',   # Personal Domain (Diversity)
    'OP029_HDDS'                   # Outcome variable
]

# Check which variables are available
available_vars = [var for var in continuous_predictors if var in df.columns]
missing_vars = [var for var in continuous_predictors if var not in df.columns]

print(f"Available continuous variables: {len(available_vars)}/{len(continuous_predictors)}")
if missing_vars:
    print(f"⚠ Missing variables: {missing_vars}")
print()

# Extract data for correlation analysis
corr_data = df[available_vars].copy()

# ============================================================================
# Table 3A: Pearson Correlation Matrix
# ============================================================================

print("Table 3A: Pearson Correlation Matrix")
print("-" * 80)

pearson_corr = corr_data.corr(method='pearson')

# Save correlation matrix
table_3a_path = OUTPUT_DIR / "Table_3A_Correlation_Matrix_Pearson.csv"
pearson_corr.to_csv(table_3a_path)
print(f"  ✓ Saved: {table_3a_path}")
print(f"    Matrix size: {pearson_corr.shape[0]} × {pearson_corr.shape[1]}")
print()

# ============================================================================
# Table 3B: Spearman Correlation Matrix
# ============================================================================

print("Table 3B: Spearman Correlation Matrix")
print("-" * 80)

spearman_corr = corr_data.corr(method='spearman')

# Save correlation matrix
table_3b_path = OUTPUT_DIR / "Table_3B_Correlation_Matrix_Spearman.csv"
spearman_corr.to_csv(table_3b_path)
print(f"  ✓ Saved: {table_3b_path}")
print(f"    Matrix size: {spearman_corr.shape[0]} × {spearman_corr.shape[1]}")
print()

# ============================================================================
# Table 3C: Bivariate Correlations with HDDS
# ============================================================================

print("Table 3C: Bivariate Correlations with HDDS (Outcome Variable)")
print("-" * 80)

hdds_correlations = []

# Calculate correlations for each predictor with HDDS
predictors_only = [var for var in available_vars if var != 'OP029_HDDS']

for predictor in predictors_only:
    # Get complete cases
    data = df[[predictor, 'OP029_HDDS']].dropna()
    n = len(data)

    if n > 2:  # Need at least 3 observations
        # Pearson correlation
        pearson_r, pearson_p = stats.pearsonr(data[predictor], data['OP029_HDDS'])

        # Spearman correlation
        spearman_r, spearman_p = stats.spearmanr(data[predictor], data['OP029_HDDS'])

        hdds_correlations.append({
            'Predictor': predictor,
            'N': n,
            'Pearson_r': pearson_r,
            'Pearson_p': pearson_p,
            'Spearman_rho': spearman_r,
            'Spearman_p': spearman_p,
            'Sig_Pearson': '***' if pearson_p < 0.001 else '**' if pearson_p < 0.01 else '*' if pearson_p < 0.05 else 'ns',
            'Sig_Spearman': '***' if spearman_p < 0.001 else '**' if spearman_p < 0.01 else '*' if spearman_p < 0.05 else 'ns'
        })
    else:
        hdds_correlations.append({
            'Predictor': predictor,
            'N': n,
            'Pearson_r': np.nan,
            'Pearson_p': np.nan,
            'Spearman_rho': np.nan,
            'Spearman_p': np.nan,
            'Sig_Pearson': 'insufficient_n',
            'Sig_Spearman': 'insufficient_n'
        })

hdds_corr_df = pd.DataFrame(hdds_correlations)

# Save HDDS correlations
table_3c_path = OUTPUT_DIR / "Table_3C_HDDS_Correlations.csv"
hdds_corr_df.to_csv(table_3c_path, index=False)
print(f"  ✓ Saved: {table_3c_path}")
print(f"    Predictors analyzed: {len(hdds_corr_df)}")
print()

# Display significant correlations
sig_corrs = hdds_corr_df[hdds_corr_df['Sig_Pearson'].isin(['*', '**', '***'])]
print(f"Significant correlations with HDDS (p < 0.05): {len(sig_corrs)}")
if len(sig_corrs) > 0:
    for _, row in sig_corrs.iterrows():
        print(f"  - {row['Predictor']}: r = {row['Pearson_r']:.3f} ({row['Sig_Pearson']}), n = {row['N']}")
else:
    print("  No significant correlations found")
print()

# ============================================================================
# TIER 4: REGRESSION ANALYSIS
# ============================================================================

print("="*80)
print("TIER 4: REGRESSION ANALYSIS")
print("="*80)
print()

def perform_regression(X, y, predictor_names, model_name):
    """
    Perform multiple linear regression using least squares.

    Parameters:
    - X: predictor matrix (n × p)
    - y: outcome vector (n × 1)
    - predictor_names: list of predictor variable names
    - model_name: name of the regression model

    Returns:
    - Dictionary with regression results
    """
    # Create dataframe with complete cases only
    data = pd.DataFrame(X, columns=predictor_names).copy()
    data['outcome'] = y

    # Listwise deletion
    complete_data = data.dropna()
    n_complete = len(complete_data)

    if n_complete < len(predictor_names) + 2:  # Need more observations than predictors
        print(f"  ⚠ WARNING: Only {n_complete} complete observations for {model_name}")
        print(f"    This is insufficient for {len(predictor_names)} predictors")
        return None

    # Extract clean data
    X_clean = complete_data[predictor_names].values
    y_clean = complete_data['outcome'].values

    # Add intercept column
    X_with_intercept = np.column_stack([np.ones(len(X_clean)), X_clean])

    # Perform least squares regression
    coefficients, residuals, rank, s = np.linalg.lstsq(X_with_intercept, y_clean, rcond=None)

    # Extract intercept and slopes
    intercept = coefficients[0]
    slopes = coefficients[1:]

    # Calculate predictions and residuals
    y_pred = X_with_intercept @ coefficients
    residuals = y_clean - y_pred

    # Calculate R-squared
    ss_total = np.sum((y_clean - np.mean(y_clean))**2)
    ss_residual = np.sum(residuals**2)
    r_squared = 1 - (ss_residual / ss_total)

    # Calculate adjusted R-squared
    n = len(y_clean)
    p = len(predictor_names)
    adj_r_squared = 1 - (1 - r_squared) * (n - 1) / (n - p - 1)

    # Calculate F-statistic and p-value
    mean_sq_regression = (ss_total - ss_residual) / p
    mean_sq_residual = ss_residual / (n - p - 1)
    f_statistic = mean_sq_regression / mean_sq_residual
    f_pvalue = 1 - stats.f.cdf(f_statistic, p, n - p - 1)

    # Calculate standard errors and t-statistics for coefficients
    mse = ss_residual / (n - p - 1)
    var_coef = mse * np.linalg.inv(X_with_intercept.T @ X_with_intercept).diagonal()
    se_coef = np.sqrt(var_coef)

    t_stats = coefficients / se_coef
    p_values = 2 * (1 - stats.t.cdf(np.abs(t_stats), n - p - 1))

    # Calculate standardized coefficients (beta weights)
    try:
        X_std = (X_clean - X_clean.mean(axis=0)) / (X_clean.std(axis=0) + 1e-10)  # Add small constant to avoid division by zero
        y_std = (y_clean - y_clean.mean()) / (y_clean.std() + 1e-10)
        X_std_with_intercept = np.column_stack([np.ones(len(X_std)), X_std])
        beta_coefficients, _, _, _ = np.linalg.lstsq(X_std_with_intercept, y_std, rcond=None)
        betas = beta_coefficients[1:]  # Exclude intercept
    except (np.linalg.LinAlgError, ValueError):
        # If standardization fails (e.g., due to collinearity), use unstandardized coefficients
        print(f"      ⚠ Warning: Could not compute standardized coefficients for {model_name}")
        print(f"        Using approximate betas from correlation of predictors with outcome")
        # Approximate beta as correlation coefficient when standardization fails
        betas = np.array([np.corrcoef(X_clean[:, i], y_clean)[0, 1] if np.std(X_clean[:, i]) > 0 else 0
                          for i in range(X_clean.shape[1])])

    # Create results table
    results = {
        'Model': model_name,
        'N': n_complete,
        'N_Dropped': len(data) - n_complete,
        'Predictors': p,
        'R_Squared': r_squared,
        'Adj_R_Squared': adj_r_squared,
        'F_Statistic': f_statistic,
        'F_pvalue': f_pvalue,
        'Intercept': intercept,
        'Intercept_SE': se_coef[0],
        'Intercept_t': t_stats[0],
        'Intercept_p': p_values[0],
        'Coefficients': {}
    }

    for i, pred in enumerate(predictor_names):
        results['Coefficients'][pred] = {
            'B': slopes[i],
            'SE': se_coef[i+1],
            't': t_stats[i+1],
            'p': p_values[i+1],
            'Beta': betas[i]
        }

    return results

# ============================================================================
# Table 4A: External Domain Regression
# ============================================================================

print("Table 4A: External Domain Regression Model")
print("-" * 80)

external_predictors = [
    'OP004_cleanliness',
    'OP005_neighborhood_safety',
    'OP006_reputation',
    'OP007_infrastructure',
    'OP009_travel_time'
]

# Check availability
available_external = [p for p in external_predictors if p in df.columns]
print(f"External domain predictors: {len(available_external)}/{len(external_predictors)}")

if len(available_external) > 0 and 'OP029_HDDS' in df.columns:
    X_external = df[available_external].values
    y_hdds = df['OP029_HDDS'].values

    external_results = perform_regression(X_external, y_hdds, available_external, "External Domain")

    if external_results:
        # Create table
        external_table = []
        external_table.append({
            'Variable': 'Model Summary',
            'B': '',
            'SE': '',
            't': '',
            'p': '',
            'Beta': '',
            'Note': f"N={external_results['N']}, R²={external_results['R_Squared']:.3f}, Adj R²={external_results['Adj_R_Squared']:.3f}, F({external_results['Predictors']},{external_results['N']-external_results['Predictors']-1})={external_results['F_Statistic']:.2f}, p={external_results['F_pvalue']:.3f}"
        })

        external_table.append({
            'Variable': 'Intercept',
            'B': f"{external_results['Intercept']:.3f}",
            'SE': f"{external_results['Intercept_SE']:.3f}",
            't': f"{external_results['Intercept_t']:.3f}",
            'p': f"{external_results['Intercept_p']:.3f}",
            'Beta': '',
            'Note': ''
        })

        for pred in available_external:
            coef = external_results['Coefficients'][pred]
            sig = '***' if coef['p'] < 0.001 else '**' if coef['p'] < 0.01 else '*' if coef['p'] < 0.05 else 'ns'
            external_table.append({
                'Variable': pred,
                'B': f"{coef['B']:.3f}",
                'SE': f"{coef['SE']:.3f}",
                't': f"{coef['t']:.3f}",
                'p': f"{coef['p']:.3f}",
                'Beta': f"{coef['Beta']:.3f}",
                'Note': sig
            })

        external_df = pd.DataFrame(external_table)
        table_4a_path = OUTPUT_DIR / "Table_4A_External_Domain_Regression.csv"
        external_df.to_csv(table_4a_path, index=False)
        print(f"  ✓ Saved: {table_4a_path}")
        print(f"    R² = {external_results['R_Squared']:.3f}, Adj R² = {external_results['Adj_R_Squared']:.3f}")
        print(f"    F({external_results['Predictors']}, {external_results['N']-external_results['Predictors']-1}) = {external_results['F_Statistic']:.2f}, p = {external_results['F_pvalue']:.3f}")
        print(f"    Significant: {'YES' if external_results['F_pvalue'] < 0.05 else 'NO'}")
print()

# ============================================================================
# Table 4B: Personal Domain Regression
# ============================================================================

print("Table 4B: Personal Domain Regression Model")
print("-" * 80)

personal_predictors = [
    'OP012_monthly_food_expenditure',
    'OP016_budget_share_pct',
    'OP017_cooking_source',
    'OP018_water_source',
    'OP019_water_distance',
    'OP023_food_env_perception',
    'OP010_shopping_frequency',
    'OP028_frequency_variation'
]

# Check availability
available_personal = [p for p in personal_predictors if p in df.columns]
print(f"Personal domain predictors: {len(available_personal)}/{len(personal_predictors)}")

if len(available_personal) > 0 and 'OP029_HDDS' in df.columns:
    X_personal = df[available_personal].values
    y_hdds = df['OP029_HDDS'].values

    personal_results = perform_regression(X_personal, y_hdds, available_personal, "Personal Domain")

    if personal_results:
        # Create table
        personal_table = []
        personal_table.append({
            'Variable': 'Model Summary',
            'B': '',
            'SE': '',
            't': '',
            'p': '',
            'Beta': '',
            'Note': f"N={personal_results['N']}, R²={personal_results['R_Squared']:.3f}, Adj R²={personal_results['Adj_R_Squared']:.3f}, F({personal_results['Predictors']},{personal_results['N']-personal_results['Predictors']-1})={personal_results['F_Statistic']:.2f}, p={personal_results['F_pvalue']:.3f}"
        })

        personal_table.append({
            'Variable': 'Intercept',
            'B': f"{personal_results['Intercept']:.3f}",
            'SE': f"{personal_results['Intercept_SE']:.3f}",
            't': f"{personal_results['Intercept_t']:.3f}",
            'p': f"{personal_results['Intercept_p']:.3f}",
            'Beta': '',
            'Note': ''
        })

        for pred in available_personal:
            coef = personal_results['Coefficients'][pred]
            sig = '***' if coef['p'] < 0.001 else '**' if coef['p'] < 0.01 else '*' if coef['p'] < 0.05 else 'ns'
            personal_table.append({
                'Variable': pred,
                'B': f"{coef['B']:.3f}",
                'SE': f"{coef['SE']:.3f}",
                't': f"{coef['t']:.3f}",
                'p': f"{coef['p']:.3f}",
                'Beta': f"{coef['Beta']:.3f}",
                'Note': sig
            })

        personal_df = pd.DataFrame(personal_table)
        table_4b_path = OUTPUT_DIR / "Table_4B_Personal_Domain_Regression.csv"
        personal_df.to_csv(table_4b_path, index=False)
        print(f"  ✓ Saved: {table_4b_path}")
        print(f"    R² = {personal_results['R_Squared']:.3f}, Adj R² = {personal_results['Adj_R_Squared']:.3f}")
        print(f"    F({personal_results['Predictors']}, {personal_results['N']-personal_results['Predictors']-1}) = {personal_results['F_Statistic']:.2f}, p = {personal_results['F_pvalue']:.3f}")
        print(f"    Significant: {'YES' if personal_results['F_pvalue'] < 0.05 else 'NO'}")
print()

# ============================================================================
# Table 4C: Full Turner Framework Regression
# ============================================================================

print("Table 4C: Full Turner Framework Regression Model")
print("-" * 80)

# Combine all predictors
full_predictors = list(set(available_external + available_personal))
print(f"Full framework predictors: {len(full_predictors)}")

if len(full_predictors) > 0 and 'OP029_HDDS' in df.columns:
    X_full = df[full_predictors].values
    y_hdds = df['OP029_HDDS'].values

    full_results = perform_regression(X_full, y_hdds, full_predictors, "Full Turner Framework")

    if full_results:
        # Create table
        full_table = []
        full_table.append({
            'Variable': 'Model Summary',
            'B': '',
            'SE': '',
            't': '',
            'p': '',
            'Beta': '',
            'Note': f"N={full_results['N']}, R²={full_results['R_Squared']:.3f}, Adj R²={full_results['Adj_R_Squared']:.3f}, F({full_results['Predictors']},{full_results['N']-full_results['Predictors']-1})={full_results['F_Statistic']:.2f}, p={full_results['F_pvalue']:.3f}"
        })

        full_table.append({
            'Variable': 'Intercept',
            'B': f"{full_results['Intercept']:.3f}",
            'SE': f"{full_results['Intercept_SE']:.3f}",
            't': f"{full_results['Intercept_t']:.3f}",
            'p': f"{full_results['Intercept_p']:.3f}",
            'Beta': '',
            'Note': ''
        })

        for pred in full_predictors:
            coef = full_results['Coefficients'][pred]
            sig = '***' if coef['p'] < 0.001 else '**' if coef['p'] < 0.01 else '*' if coef['p'] < 0.05 else 'ns'
            full_table.append({
                'Variable': pred,
                'B': f"{coef['B']:.3f}",
                'SE': f"{coef['SE']:.3f}",
                't': f"{coef['t']:.3f}",
                'p': f"{coef['p']:.3f}",
                'Beta': f"{coef['Beta']:.3f}",
                'Note': sig
            })

        full_df = pd.DataFrame(full_table)
        table_4c_path = OUTPUT_DIR / "Table_4C_Full_Framework_Regression.csv"
        full_df.to_csv(table_4c_path, index=False)
        print(f"  ✓ Saved: {table_4c_path}")
        print(f"    R² = {full_results['R_Squared']:.3f}, Adj R² = {full_results['Adj_R_Squared']:.3f}")
        print(f"    F({full_results['Predictors']}, {full_results['N']-full_results['Predictors']-1}) = {full_results['F_Statistic']:.2f}, p = {full_results['F_pvalue']:.3f}")
        print(f"    Significant: {'YES' if full_results['F_pvalue'] < 0.05 else 'NO'}")

        if full_results['Adj_R_Squared'] < 0:
            print(f"  ⚠ WARNING: Negative adjusted R² indicates severe overfitting!")
            print(f"    Predictor-to-observation ratio: 1:{full_results['N']/full_results['Predictors']:.1f}")
            print(f"    Recommended minimum: 1:10")
print()

# ============================================================================
# Table 4D: Interaction Effects Model
# ============================================================================

print("Table 4D: Interaction Effects Model (Accessibility × Affordability)")
print("-" * 80)

interaction_predictors = ['OP009_travel_time', 'OP016_budget_share_pct']

# Check if both variables are available
if all(p in df.columns for p in interaction_predictors) and 'OP029_HDDS' in df.columns:
    # Create interaction term
    interaction_data = df[interaction_predictors + ['OP029_HDDS']].dropna()

    if len(interaction_data) > 5:
        interaction_data['OP009_x_OP016'] = (
            interaction_data['OP009_travel_time'] * interaction_data['OP016_budget_share_pct']
        )

        X_interaction = interaction_data[interaction_predictors + ['OP009_x_OP016']].values
        y_interaction = interaction_data['OP029_HDDS'].values

        interaction_results = perform_regression(
            X_interaction, y_interaction,
            interaction_predictors + ['OP009_x_OP016'],
            "Interaction Model"
        )

        if interaction_results:
            # Create table
            interaction_table = []
            interaction_table.append({
                'Variable': 'Model Summary',
                'B': '',
                'SE': '',
                't': '',
                'p': '',
                'Beta': '',
                'Note': f"N={interaction_results['N']}, R²={interaction_results['R_Squared']:.3f}, Adj R²={interaction_results['Adj_R_Squared']:.3f}, F({interaction_results['Predictors']},{interaction_results['N']-interaction_results['Predictors']-1})={interaction_results['F_Statistic']:.2f}, p={interaction_results['F_pvalue']:.3f}"
            })

            interaction_table.append({
                'Variable': 'Intercept',
                'B': f"{interaction_results['Intercept']:.3f}",
                'SE': f"{interaction_results['Intercept_SE']:.3f}",
                't': f"{interaction_results['Intercept_t']:.3f}",
                'p': f"{interaction_results['Intercept_p']:.3f}",
                'Beta': '',
                'Note': ''
            })

            for pred in interaction_predictors + ['OP009_x_OP016']:
                coef = interaction_results['Coefficients'][pred]
                sig = '***' if coef['p'] < 0.001 else '**' if coef['p'] < 0.01 else '*' if coef['p'] < 0.05 else 'ns'
                interaction_table.append({
                    'Variable': pred,
                    'B': f"{coef['B']:.3f}",
                    'SE': f"{coef['SE']:.3f}",
                    't': f"{coef['t']:.3f}",
                    'p': f"{coef['p']:.3f}",
                    'Beta': f"{coef['Beta']:.3f}",
                    'Note': sig
                })

            interaction_df = pd.DataFrame(interaction_table)
            table_4d_path = OUTPUT_DIR / "Table_4D_Interaction_Effects.csv"
            interaction_df.to_csv(table_4d_path, index=False)
            print(f"  ✓ Saved: {table_4d_path}")
            print(f"    R² = {interaction_results['R_Squared']:.3f}, Adj R² = {interaction_results['Adj_R_Squared']:.3f}")
            print(f"    Interaction significant: {'YES' if interaction_results['Coefficients']['OP009_x_OP016']['p'] < 0.05 else 'NO'}")
    else:
        print(f"  ⚠ WARNING: Only {len(interaction_data)} complete observations for interaction model")
        print("    Insufficient data to estimate interaction effects")
        # Create placeholder table
        interaction_df = pd.DataFrame([{
            'Variable': 'Interaction Model Failed',
            'B': '',
            'SE': '',
            't': '',
            'p': '',
            'Beta': '',
            'Note': f'Only {len(interaction_data)} complete observations with both OP009 and OP016'
        }])
        table_4d_path = OUTPUT_DIR / "Table_4D_Interaction_Effects.csv"
        interaction_df.to_csv(table_4d_path, index=False)
        print(f"  ✓ Saved placeholder: {table_4d_path}")
else:
    print("  ⚠ WARNING: Required variables for interaction model not available")
    interaction_df = pd.DataFrame([{
        'Variable': 'Interaction Model Not Run',
        'B': '',
        'SE': '',
        't': '',
        'p': '',
        'Beta': '',
        'Note': 'Required variables (OP009, OP016) not available'
    }])
    table_4d_path = OUTPUT_DIR / "Table_4D_Interaction_Effects.csv"
    interaction_df.to_csv(table_4d_path, index=False)
    print(f"  ✓ Saved placeholder: {table_4d_path}")
print()

# ============================================================================
# Table 5: Standardized Coefficient Rankings
# ============================================================================

print("Table 5: Standardized Coefficient Rankings (Effect Sizes)")
print("-" * 80)

coefficient_rankings = []

# Add coefficients from all models
if external_results:
    for pred in available_external:
        coefficient_rankings.append({
            'Predictor': pred,
            'Model': 'External Domain',
            'Beta': external_results['Coefficients'][pred]['Beta'],
            'p_value': external_results['Coefficients'][pred]['p'],
            'Significant': 'Yes' if external_results['Coefficients'][pred]['p'] < 0.05 else 'No'
        })

if personal_results:
    for pred in available_personal:
        coefficient_rankings.append({
            'Predictor': pred,
            'Model': 'Personal Domain',
            'Beta': personal_results['Coefficients'][pred]['Beta'],
            'p_value': personal_results['Coefficients'][pred]['p'],
            'Significant': 'Yes' if personal_results['Coefficients'][pred]['p'] < 0.05 else 'No'
        })

if full_results:
    for pred in full_predictors:
        coefficient_rankings.append({
            'Predictor': pred,
            'Model': 'Full Framework',
            'Beta': full_results['Coefficients'][pred]['Beta'],
            'p_value': full_results['Coefficients'][pred]['p'],
            'Significant': 'Yes' if full_results['Coefficients'][pred]['p'] < 0.05 else 'No'
        })

coefficient_df = pd.DataFrame(coefficient_rankings)

# Sort by absolute beta value within each model
coefficient_df['Abs_Beta'] = coefficient_df['Beta'].abs()
coefficient_df = coefficient_df.sort_values(['Model', 'Abs_Beta'], ascending=[True, False])

table_5_path = OUTPUT_DIR / "Table_5_Standardized_Coefficient_Ranking.csv"
coefficient_df.to_csv(table_5_path, index=False)
print(f"  ✓ Saved: {table_5_path}")
print(f"    Total coefficients: {len(coefficient_df)}")
print(f"    Significant coefficients: {len(coefficient_df[coefficient_df['Significant'] == 'Yes'])}")
print()

# ============================================================================
# COMPLETION SUMMARY
# ============================================================================

print("="*80)
print("PHASE 3B COMPLETION SUMMARY")
print("="*80)
print()

print("✅ Tier 3 Outputs (Correlation Analysis):")
print("   - Table 3A: Pearson Correlation Matrix")
print("   - Table 3B: Spearman Correlation Matrix")
print("   - Table 3C: Bivariate HDDS Correlations")
print()

print("✅ Tier 4 Outputs (Regression Analysis):")
print("   - Table 4A: External Domain Regression")
print("   - Table 4B: Personal Domain Regression")
print("   - Table 4C: Full Turner Framework Regression")
print("   - Table 4D: Interaction Effects Model")
print("   - Table 5: Standardized Coefficient Rankings")
print()

print(f"📁 All tables saved to: {OUTPUT_DIR}")
print()

print("="*80)
print("PHASE 3B: TIER 3 & 4 ANALYSES COMPLETE")
print("="*80)
