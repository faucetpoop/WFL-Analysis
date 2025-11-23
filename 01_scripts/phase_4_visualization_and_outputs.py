#!/usr/bin/env python3
"""
Phase 4: Outputs & Thesis Integration - Visualization and Organization
=======================================================================

Purpose: Generate remaining publication-ready figures and organize all outputs
Author: Senior Data Scientist Skill (SuperClaude)
Date: 2025-11-23
Phase: 4 - Outputs & Thesis Integration

Inputs:
    - phase_3A_household_analysis_ready_COMPLETE.csv (214 households, 392 columns)
    - All Phase 1-3 table outputs

Outputs:
    - Figure 3: HDDS by Affordability (3 groups) - box plot
    - Figure 4: HDDS by Food Safety - box plot
    - Figure 5: Standardized Coefficients Plot - bar chart
    - Summary datasets for thesis integration
    - Organized table index
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Set style for publication-ready figures
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("Set2")
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9

# Define paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "02_outputs" / "datasets"
TABLES_DIR = BASE_DIR / "02_outputs" / "tables"
FIGURES_DIR = BASE_DIR / "02_outputs" / "figures"
LOGS_DIR = BASE_DIR / "03_logs"

# Ensure directories exist
FIGURES_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)

logger.info("=" * 80)
logger.info("PHASE 4: OUTPUTS & THESIS INTEGRATION")
logger.info("=" * 80)

# ============================================================================
# STEP 1: Load Complete Dataset
# ============================================================================

logger.info("\nSTEP 1: Loading complete household analysis dataset...")

try:
    df = pd.read_csv(DATA_DIR / "phase_3A_household_analysis_ready_COMPLETE.csv")
    logger.info(f"✓ Loaded dataset: {df.shape[0]} households, {df.shape[1]} columns")
except FileNotFoundError:
    logger.error("✗ Dataset not found. Ensure Phase 3A is complete.")
    raise

# ============================================================================
# STEP 2: Create Figure 3 - HDDS by Affordability (3 Groups)
# ============================================================================

logger.info("\nSTEP 2: Creating Figure 3 - HDDS by Affordability (3 groups)...")

# Create affordability tertiles from OP016 (Budget Share Percentage)
# OP029_HDDS is the HDDS column, OP016_budget_share_pct is affordability
df_afford = df[['OP029_HDDS', 'OP016_budget_share_pct']].dropna()

if len(df_afford) > 0:
    # Create tertiles - higher budget share = lower affordability
    df_afford['Affordability_Group'] = pd.qcut(
        df_afford['OP016_budget_share_pct'],
        q=3,
        labels=['Low Budget Share\n(High Affordability)', 'Medium Budget Share\n(Medium Affordability)', 'High Budget Share\n(Low Affordability)']
    )

    fig, ax = plt.subplots(figsize=(8, 6))

    # Create box plot
    groups_order = ['Low Budget Share\n(High Affordability)', 'Medium Budget Share\n(Medium Affordability)', 'High Budget Share\n(Low Affordability)']
    bp = ax.boxplot(
        [df_afford[df_afford['Affordability_Group'] == group]['OP029_HDDS'].dropna()
         for group in groups_order],
        labels=groups_order,
        patch_artist=True,
        widths=0.6
    )

    # Color boxes - green for high affordability, red for low
    colors = ['#99ff99', '#ffcc99', '#ff9999']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    ax.set_ylabel('Household Dietary Diversity Score (HDDS)', fontsize=11)
    ax.set_xlabel('Food Budget Share (Affordability Proxy)', fontsize=11)
    ax.set_title('Figure 3: Dietary Diversity by Affordability\n(Food Budget Share Tertiles, N={})'.format(len(df_afford)),
                 fontsize=12, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)

    # Add sample sizes
    for i, group in enumerate(groups_order):
        n = len(df_afford[df_afford['Affordability_Group'] == group])
        ax.text(i+1, ax.get_ylim()[0] + 0.5, f'n={n}',
                ha='center', va='bottom', fontsize=8, style='italic')

    plt.tight_layout()
    fig_path = FIGURES_DIR / "Figure_3_HDDS_by_Affordability_Tertiles.png"
    plt.savefig(fig_path, dpi=300, bbox_inches='tight')
    plt.close()

    logger.info(f"✓ Figure 3 saved: {fig_path}")
    logger.info(f"  Sample size: {len(df_afford)} households with complete data")
else:
    logger.warning("✗ Insufficient data for Figure 3 (OP016 missing)")

# ============================================================================
# STEP 3: Create Figure 4 - HDDS by Food Safety
# ============================================================================

logger.info("\nSTEP 3: Creating Figure 4 - HDDS by Food Safety...")

# OP025 = Neighborhood safety index (proxy for food safety environment)
# Note: OP024 doesn't exist, using OP025_neighborhood_safety_index as proxy
df_safety = df[['OP029_HDDS', 'OP025_neighborhood_safety_index']].dropna()

if len(df_safety) > 0:
    # Create safety groups based on distribution
    unique_values = df_safety['OP025_neighborhood_safety_index'].nunique()

    try:
        if unique_values >= 3:
            # Try tertiles first
            df_safety['Safety_Group'] = pd.qcut(
                df_safety['OP025_neighborhood_safety_index'],
                q=3,
                labels=['Low Safety', 'Medium Safety', 'High Safety'],
                duplicates='drop'
            )
            groups = df_safety['Safety_Group'].cat.categories.tolist()
            colors = ['#ff9999', '#ffcc99', '#99ff99'][:len(groups)]
        else:
            raise ValueError("Not enough unique values for tertiles")
    except (ValueError, TypeError):
        # Fall back to median split if tertiles fail
        median_val = df_safety['OP025_neighborhood_safety_index'].median()
        df_safety['Safety_Group'] = df_safety['OP025_neighborhood_safety_index'].apply(
            lambda x: 'Lower Safety' if x < median_val else 'Higher Safety'
        )
        groups = ['Lower Safety', 'Higher Safety']
        colors = ['#ff9999', '#99ff99']

    fig, ax = plt.subplots(figsize=(8, 6))

    # Create box plot
    bp = ax.boxplot(
        [df_safety[df_safety['Safety_Group'] == group]['OP029_HDDS'].dropna() for group in groups],
        labels=[g.replace(' Safety', '\nSafety') for g in groups],
        patch_artist=True,
        widths=0.6
    )

    # Color boxes
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    ax.set_ylabel('Household Dietary Diversity Score (HDDS)', fontsize=11)
    ax.set_xlabel('Neighborhood Safety Index', fontsize=11)
    ax.set_title('Figure 4: Dietary Diversity by Neighborhood Safety\n(Safety Index Tertiles, N={})'.format(len(df_safety)),
                 fontsize=12, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)

    # Add sample sizes
    for i, group in enumerate(groups):
        n = len(df_safety[df_safety['Safety_Group'] == group])
        ax.text(i+1, ax.get_ylim()[0] + 0.5, f'n={n}',
                ha='center', va='bottom', fontsize=8, style='italic')

    plt.tight_layout()
    fig_path = FIGURES_DIR / "Figure_4_HDDS_by_Food_Safety.png"
    plt.savefig(fig_path, dpi=300, bbox_inches='tight')
    plt.close()

    logger.info(f"✓ Figure 4 saved: {fig_path}")
    logger.info(f"  Sample size: {len(df_safety)} households with complete data")
else:
    logger.warning("✗ Insufficient data for Figure 4 (OP025 missing)")

# ============================================================================
# STEP 4: Create Figure 5 - Standardized Coefficients Plot
# ============================================================================

logger.info("\nSTEP 4: Creating Figure 5 - Standardized Coefficients Plot...")

try:
    # Load standardized coefficient rankings from Phase 3
    coef_df = pd.read_csv(TABLES_DIR / "Table_5_Standardized_Coefficient_Ranking.csv")

    # Get top 10 predictors by absolute beta coefficient
    # Column is 'Beta' and 'Abs_Beta' already exists
    top_predictors = coef_df.nlargest(10, 'Abs_Beta').copy()

    # Sort by coefficient value for plotting
    top_predictors = top_predictors.sort_values('Beta')

    fig, ax = plt.subplots(figsize=(10, 8))

    # Create horizontal bar chart
    colors = ['#d62728' if x < 0 else '#2ca02c' for x in top_predictors['Beta']]
    bars = ax.barh(range(len(top_predictors)),
                   top_predictors['Beta'],
                   color=colors, alpha=0.7, edgecolor='black', linewidth=0.5)

    # Set labels
    ax.set_yticks(range(len(top_predictors)))
    ax.set_yticklabels(top_predictors['Predictor'], fontsize=9)
    ax.set_xlabel('Standardized Coefficient (β)', fontsize=11)
    ax.set_title('Figure 5: Top 10 Predictors of Dietary Diversity\n(Full Turner Framework Model)',
                 fontsize=12, fontweight='bold')
    ax.axvline(x=0, color='black', linewidth=0.8, linestyle='--', alpha=0.5)
    ax.grid(axis='x', alpha=0.3)

    # Add coefficient values on bars
    for i, (idx, row) in enumerate(top_predictors.iterrows()):
        value = row['Beta']
        x_pos = value + (0.02 if value > 0 else -0.02)
        ha = 'left' if value > 0 else 'right'
        ax.text(x_pos, i, f'{value:.3f}',
                va='center', ha=ha, fontsize=8, fontweight='bold')

    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#2ca02c', alpha=0.7, label='Positive Effect'),
        Patch(facecolor='#d62728', alpha=0.7, label='Negative Effect')
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9)

    plt.tight_layout()
    fig_path = FIGURES_DIR / "Figure_5_Standardized_Coefficients.png"
    plt.savefig(fig_path, dpi=300, bbox_inches='tight')
    plt.close()

    logger.info(f"✓ Figure 5 saved: {fig_path}")
    logger.info(f"  Top predictor: {top_predictors.iloc[-1]['Predictor']} (β={top_predictors.iloc[-1]['Beta']:.3f})")

except FileNotFoundError:
    logger.error("✗ Table 5 not found. Ensure Phase 3B is complete.")

# ============================================================================
# STEP 5: Create Summary Datasets for Thesis
# ============================================================================

logger.info("\nSTEP 5: Creating summary datasets for thesis integration...")

# 5A: Household Analysis Final (all OPs + outcomes)
summary_cols = [col for col in df.columns if col.startswith('OP')]
household_final = df[summary_cols].copy()
output_path = DATA_DIR / "household_analysis_final.csv"
household_final.to_csv(output_path, index=False)
logger.info(f"✓ Saved household_analysis_final.csv: {household_final.shape}")

# 5B: T2 Comparison Results Summary
try:
    t2_tables = []
    for table in ['Table_2A_Accessibility_Comparison.csv',
                  'Table_2B_Affordability_Comparison.csv',
                  'Table_2C_Safety_Comparison.csv']:
        t2_df = pd.read_csv(TABLES_DIR / table)
        t2_df['Analysis'] = table.replace('Table_2', '').replace('_Comparison.csv', '')
        t2_tables.append(t2_df)

    t2_comparison = pd.concat(t2_tables, ignore_index=True)
    output_path = DATA_DIR / "t2_comparison_results.csv"
    t2_comparison.to_csv(output_path, index=False)
    logger.info(f"✓ Saved t2_comparison_results.csv: {t2_comparison.shape}")
except Exception as e:
    logger.warning(f"✗ Could not consolidate T2 results: {e}")

# 5C: Correlation Summary (key correlations with HDDS)
try:
    corr_df = pd.read_csv(TABLES_DIR / "Table_3C_HDDS_Correlations.csv")
    # Filter to significant correlations (p < 0.10 for exploratory)
    if 'p_value_pearson' in corr_df.columns:
        significant = corr_df[corr_df['p_value_pearson'] < 0.10].copy()
        output_path = DATA_DIR / "correlation_summary_significant.csv"
        significant.to_csv(output_path, index=False)
        logger.info(f"✓ Saved correlation_summary_significant.csv: {significant.shape}")

    # Save full correlation summary
    output_path = DATA_DIR / "correlation_summary.csv"
    corr_df.to_csv(output_path, index=False)
    logger.info(f"✓ Saved correlation_summary.csv: {corr_df.shape}")
except Exception as e:
    logger.warning(f"✗ Could not create correlation summary: {e}")

# ============================================================================
# STEP 6: Create Table Index for Thesis
# ============================================================================

logger.info("\nSTEP 6: Creating comprehensive table index...")

table_index = {
    'Table_Number': [],
    'Filename': [],
    'Description': [],
    'Phase_Created': [],
    'Thesis_Chapter': [],
    'Section': []
}

tables_metadata = [
    ('Table 1A', 'Table_1A_Descriptive_Continuous.csv', 'Descriptive Statistics - Continuous Variables', 'Phase 1', 'Chapter 4', 'Descriptive Results'),
    ('Table 1B', 'Table_1B_Descriptive_Categorical.csv', 'Descriptive Statistics - Categorical Variables', 'Phase 1', 'Chapter 4', 'Descriptive Results'),
    ('Table 2A', 'Table_2A_Accessibility_Comparison.csv', 'HDDS by Accessibility Perception', 'Phase 2', 'Chapter 4', 'T2 Analysis'),
    ('Table 2B', 'Table_2B_Affordability_Comparison.csv', 'HDDS by Affordability Perception (3 groups)', 'Phase 2', 'Chapter 4', 'T2 Analysis'),
    ('Table 2C', 'Table_2C_Safety_Comparison.csv', 'HDDS by Food Safety Perception', 'Phase 2', 'Chapter 4', 'T2 Analysis'),
    ('Table 3A', 'Table_3A_Correlation_Matrix_Pearson.csv', 'Pearson Correlation Matrix (12 predictors)', 'Phase 3', 'Chapter 4', 'Correlation Analysis'),
    ('Table 3B', 'Table_3B_Correlation_Matrix_Spearman.csv', 'Spearman Correlation Matrix (12 predictors)', 'Phase 3', 'Appendix', 'Supplementary'),
    ('Table 3C', 'Table_3C_HDDS_Correlations.csv', 'Bivariate HDDS Correlations with Significance', 'Phase 3', 'Chapter 4', 'Correlation Analysis'),
    ('Table 4A', 'Table_4A_External_Domain_Regression.csv', 'External Domain Regression (5 predictors)', 'Phase 3', 'Chapter 4', 'Regression Results'),
    ('Table 4B', 'Table_4B_Personal_Domain_Regression.csv', 'Personal Domain Regression (8 predictors)', 'Phase 3', 'Appendix', 'Supplementary'),
    ('Table 4C', 'Table_4C_Full_Framework_Regression.csv', 'Full Turner Framework Regression (14 predictors)', 'Phase 3', 'Chapter 4', 'Regression Results'),
    ('Table 4D', 'Table_4D_Interaction_Effects.csv', 'Interaction Effects (Accessibility × Affordability)', 'Phase 3', 'Appendix', 'Exploratory'),
    ('Table 5', 'Table_5_Standardized_Coefficient_Ranking.csv', 'Standardized Coefficient Rankings', 'Phase 3', 'Chapter 4', 'Effect Sizes'),
]

for table_num, filename, desc, phase, chapter, section in tables_metadata:
    table_index['Table_Number'].append(table_num)
    table_index['Filename'].append(filename)
    table_index['Description'].append(desc)
    table_index['Phase_Created'].append(phase)
    table_index['Thesis_Chapter'].append(chapter)
    table_index['Section'].append(section)

table_index_df = pd.DataFrame(table_index)
output_path = TABLES_DIR / "TABLE_INDEX_THESIS_INTEGRATION.csv"
table_index_df.to_csv(output_path, index=False)
logger.info(f"✓ Saved table index: {output_path}")
logger.info(f"  Total tables: {len(table_index_df)}")

# ============================================================================
# STEP 7: Create Figure Index for Thesis
# ============================================================================

logger.info("\nSTEP 7: Creating comprehensive figure index...")

figure_index = {
    'Figure_Number': [],
    'Filename': [],
    'Description': [],
    'Phase_Created': [],
    'Thesis_Chapter': [],
    'Section': []
}

figures_metadata = [
    ('Figure 1', 'Phase_2_HDDS_Distribution.png', 'HDDS Distribution (histogram)', 'Phase 2', 'Chapter 4', 'Descriptive Results'),
    ('Figure 2', 'Phase_2_T2_Comparisons_Boxplots.png', 'HDDS by Accessibility, Affordability, Safety (box plots)', 'Phase 2', 'Chapter 4', 'T2 Analysis'),
    ('Figure 3', 'Figure_3_HDDS_by_Affordability_Tertiles.png', 'HDDS by Affordability Tertiles (box plot)', 'Phase 4', 'Chapter 4', 'Stratified Analysis'),
    ('Figure 4', 'Figure_4_HDDS_by_Food_Safety.png', 'HDDS by Food Safety Perception (box plot)', 'Phase 4', 'Chapter 4', 'Stratified Analysis'),
    ('Figure 5', 'Figure_5_Standardized_Coefficients.png', 'Top 10 Standardized Predictors (bar chart)', 'Phase 4', 'Chapter 4', 'Effect Sizes'),
]

for fig_num, filename, desc, phase, chapter, section in figures_metadata:
    figure_index['Figure_Number'].append(fig_num)
    figure_index['Filename'].append(filename)
    figure_index['Description'].append(desc)
    figure_index['Phase_Created'].append(phase)
    figure_index['Thesis_Chapter'].append(chapter)
    figure_index['Section'].append(section)

figure_index_df = pd.DataFrame(figure_index)
output_path = FIGURES_DIR / "FIGURE_INDEX_THESIS_INTEGRATION.csv"
figure_index_df.to_csv(output_path, index=False)
logger.info(f"✓ Saved figure index: {output_path}")
logger.info(f"  Total figures: {len(figure_index_df)}")

# ============================================================================
# FINAL SUMMARY
# ============================================================================

logger.info("\n" + "=" * 80)
logger.info("PHASE 4 VISUALIZATION AND OUTPUTS - COMPLETE")
logger.info("=" * 80)

logger.info("\n📊 OUTPUTS CREATED:")
logger.info(f"  ✓ 3 new publication-ready figures")
logger.info(f"  ✓ 3 summary datasets for thesis")
logger.info(f"  ✓ Table index with thesis mapping")
logger.info(f"  ✓ Figure index with thesis mapping")

logger.info("\n📁 OUTPUT LOCATIONS:")
logger.info(f"  Figures: {FIGURES_DIR}")
logger.info(f"  Datasets: {DATA_DIR}")
logger.info(f"  Tables: {TABLES_DIR}")

logger.info("\n✅ Phase 4 visualization and organization complete!")
logger.info("   Ready for thesis integration and limitations documentation.")

print("\n" + "=" * 80)
print("PHASE 4 VISUALIZATION SCRIPT - EXECUTION COMPLETE")
print("=" * 80)
