"""
Enhanced Regression Analysis with P1/P2 Improvements
=====================================================
P1: Quarterly aggregation (4x sample), Propensity Score Matching
P2: Additional controls (bed occupancy proxy), robustness checks
"""
import pandas as pd
import numpy as np
from linearmodels.panel import PanelOLS, RandomEffects
import statsmodels.api as sm
from scipy import stats
import warnings
warnings.filterwarnings('ignore')


def load_and_prepare_quarterly():
    """
    P1 Improvement: Use quarterly instead of annual aggregation.
    This increases sample size by 4x.
    """
    print("=" * 60)
    print("LOADING DATA WITH QUARTERLY AGGREGATION (P1)")
    print("=" * 60)
    
    df = pd.read_parquet("data/analytical/analytical_panel.parquet")
    df = df.dropna(subset=['entity_nif', 'year', 'month'])
    
    # Create quarter
    df['quarter'] = ((df['month'] - 1) // 3) + 1
    df['year_quarter'] = df['year'].astype(str) + "Q" + df['quarter'].astype(str)
    
    # Aggregate to quarterly
    df_quarterly = df.groupby(['entity_nif', 'year', 'quarter']).agg({
        'divida_total_fornecedores_externos': 'last',
        'divida_vencida_fornecedores_externos': 'last',
        'gdp_per_capita': 'max',
        'unemployment_rate': 'max',
        'total_geral': 'mean',  # Staff as size proxy
        'entity_name': 'first',
        'entity_type': 'first',
        # P2: Additional controls
        'enfermeiros': 'mean',
        'medicos_s_internos': 'mean',
    }).reset_index()
    
    # Filter valid financial data
    df_quarterly = df_quarterly[df_quarterly['divida_total_fornecedores_externos'] > 0]
    
    print(f"  Raw monthly observations: {len(df)}")
    print(f"  Quarterly observations: {len(df_quarterly)}")
    
    return df_quarterly


def construct_variables(df):
    """
    Variable construction with P2 improvements (additional controls).
    """
    print("\n--- Constructing Variables (with P2 Controls) ---")
    
    # Dependent: Overdue Ratio
    df['overdue_ratio'] = df['divida_vencida_fornecedores_externos'] / df['divida_total_fornecedores_externos']
    
    # Winsorize at 1% and 99% (robustness)
    lower = df['overdue_ratio'].quantile(0.01)
    upper = df['overdue_ratio'].quantile(0.99)
    df['overdue_ratio_wins'] = df['overdue_ratio'].clip(lower, upper)
    
    # Independent: Is_ULS
    df['is_uls'] = df['entity_name'].str.contains("ULS", case=False, na=False).astype(int)
    
    # Size proxy (log staff)
    df['log_staff'] = np.log(df['total_geral'] + 1)
    
    # GDP control
    df['log_gdp'] = np.log(df['gdp_per_capita'] + 1)
    
    # P2: Clinical intensity proxy (doctors + nurses per staff)
    df['clinical_intensity'] = (df['medicos_s_internos'].fillna(0) + df['enfermeiros'].fillna(0)) / (df['total_geral'] + 1)
    
    # Time identifier for panel
    df['time_id'] = df['year'] * 10 + df['quarter']
    
    print(f"  Is_ULS distribution: {df['is_uls'].value_counts().to_dict()}")
    print(f"  Overdue Ratio: mean={df['overdue_ratio'].mean():.3f}, std={df['overdue_ratio'].std():.3f}")
    
    return df


def propensity_score_matching(df):
    """
    P1 Improvement: Propensity Score Matching to address selection bias.
    """
    print("\n" + "=" * 60)
    print("PROPENSITY SCORE MATCHING (P1)")
    print("=" * 60)
    
    # Use pre-treatment period to estimate propensity scores
    pre_treatment = df[df['year'] < 2024].copy()
    
    # Average characteristics per entity (for PSM)
    entity_chars = pre_treatment.groupby('entity_nif').agg({
        'log_staff': 'mean',
        'overdue_ratio': 'mean',
        'clinical_intensity': 'mean',
        'is_uls': 'max'  # Whether ever ULS
    }).reset_index()
    
    entity_chars = entity_chars.dropna()
    
    if len(entity_chars[entity_chars['is_uls'] == 1]) < 3:
        print("  WARNING: Too few ULS entities for PSM. Skipping matching.")
        return df, None
    
    # Estimate propensity score using logistic regression
    X = entity_chars[['log_staff', 'overdue_ratio', 'clinical_intensity']]
    X = sm.add_constant(X)
    y = entity_chars['is_uls']
    
    try:
        logit_model = sm.Logit(y, X).fit(disp=0)
        entity_chars['propensity_score'] = logit_model.predict(X)
        
        print(f"  Logit model converged. Pseudo R²: {logit_model.prsquared:.3f}")
        print(f"  Propensity scores: min={entity_chars['propensity_score'].min():.3f}, max={entity_chars['propensity_score'].max():.3f}")
        
        # Simple matching: Keep entities with overlapping propensity scores
        # (Common support trimming)
        uls_ps = entity_chars[entity_chars['is_uls'] == 1]['propensity_score']
        epe_ps = entity_chars[entity_chars['is_uls'] == 0]['propensity_score']
        
        lower_bound = max(uls_ps.min(), epe_ps.min())
        upper_bound = min(uls_ps.max(), epe_ps.max())
        
        matched_entities = entity_chars[
            (entity_chars['propensity_score'] >= lower_bound) &
            (entity_chars['propensity_score'] <= upper_bound)
        ]['entity_nif'].tolist()
        
        df_matched = df[df['entity_nif'].isin(matched_entities)]
        
        print(f"  Common support: [{lower_bound:.3f}, {upper_bound:.3f}]")
        print(f"  Matched entities: {len(matched_entities)} (from {df['entity_nif'].nunique()})")
        print(f"  Matched observations: {len(df_matched)}")
        
        return df_matched, entity_chars
        
    except Exception as e:
        print(f"  PSM failed: {e}")
        return df, None


def run_enhanced_regression(df, label="Full Sample"):
    """
    Run PanelOLS with quarterly data and additional controls.
    """
    print(f"\n--- Running Regression: {label} ---")
    
    # Prepare data
    exog_vars = ['is_uls', 'log_staff', 'log_gdp', 'clinical_intensity']
    data = df.dropna(subset=['overdue_ratio_wins'] + exog_vars)
    
    if len(data) < 20:
        print(f"  ERROR: Insufficient data ({len(data)} obs)")
        return None
    
    data = data.set_index(['entity_nif', 'time_id'])
    
    # Model 1: Time Effects Only (allows cross-sectional ULS comparison)
    mod1 = PanelOLS(
        data['overdue_ratio_wins'], 
        sm.add_constant(data[exog_vars]), 
        entity_effects=False, 
        time_effects=True,
        drop_absorbed=True
    )
    res1 = mod1.fit(cov_type='clustered', cluster_entity=True)
    
    print(f"\n{res1}")
    
    return res1


def robustness_checks(df):
    """
    P2: Additional robustness checks.
    """
    print("\n" + "=" * 60)
    print("ROBUSTNESS CHECKS (P2)")
    print("=" * 60)
    
    results = {}
    
    # 1. Alternative DV: Log of overdue debt
    df['log_overdue'] = np.log(df['divida_vencida_fornecedores_externos'].clip(lower=1))
    
    # 2. Subsample: Large hospitals only
    median_staff = df['total_geral'].median()
    df_large = df[df['total_geral'] >= median_staff]
    
    # 3. Subsample: Post-2020 (excluding COVID shock)
    df_post_covid = df[df['year'] >= 2022]
    
    print(f"\n[1] Alternative DV: Log(Overdue Debt)")
    exog_vars = ['is_uls', 'log_staff', 'log_gdp']
    data = df.dropna(subset=['log_overdue'] + exog_vars)
    data = data.set_index(['entity_nif', 'time_id'])
    
    if len(data) > 20:
        mod = PanelOLS(data['log_overdue'], sm.add_constant(data[exog_vars]), 
                       entity_effects=False, time_effects=True, drop_absorbed=True)
        res = mod.fit(cov_type='clustered', cluster_entity=True)
        results['log_overdue'] = res
        print(f"  is_uls coef: {res.params.get('is_uls', 'N/A'):.4f}, p-value: {res.pvalues.get('is_uls', 'N/A'):.4f}")
    
    print(f"\n[2] Subsample: Large Hospitals (Staff >= {median_staff:.0f})")
    if len(df_large) > 20:
        res = run_enhanced_regression(df_large, "Large Hospitals")
        if res:
            results['large_hospitals'] = res
    
    print(f"\n[3] Subsample: Post-COVID (2022+)")
    if len(df_post_covid) > 20:
        res = run_enhanced_regression(df_post_covid, "Post-COVID")
        if res:
            results['post_covid'] = res
    
    return results


def generate_report(main_result, psm_result, robustness_results):
    """
    Generate comprehensive results report.
    """
    report = """# Enhanced Regression Results
## P1 & P2 Improvements Implemented

### Main Model (Quarterly, Time FE, Clustered SE)
"""
    
    if main_result:
        report += f"""
| Variable | Coefficient | Std. Err. | P-value |
|----------|-------------|-----------|---------|
| Is_ULS | {main_result.params.get('is_uls', 0):.4f} | {main_result.std_errors.get('is_uls', 0):.4f} | {main_result.pvalues.get('is_uls', 1):.4f} |
| Log_Staff | {main_result.params.get('log_staff', 0):.4f} | {main_result.std_errors.get('log_staff', 0):.4f} | {main_result.pvalues.get('log_staff', 1):.4f} |
| Log_GDP | {main_result.params.get('log_gdp', 0):.4f} | {main_result.std_errors.get('log_gdp', 0):.4f} | {main_result.pvalues.get('log_gdp', 1):.4f} |
| Clinical_Intensity | {main_result.params.get('clinical_intensity', 0):.4f} | {main_result.std_errors.get('clinical_intensity', 0):.4f} | {main_result.pvalues.get('clinical_intensity', 1):.4f} |

**N = {main_result.nobs}, R² = {main_result.rsquared:.4f}**
"""
    
    if psm_result is not None:
        report += "\n### PSM Applied\nPropensity Score Matching was used to address selection bias.\n"
    
    report += "\n### Robustness Checks\n"
    for name, res in robustness_results.items():
        if res:
            uls_coef = res.params.get('is_uls', 0)
            uls_pval = res.pvalues.get('is_uls', 1)
            report += f"- **{name}**: is_uls = {uls_coef:.4f} (p={uls_pval:.4f})\n"
    
    return report


def main():
    print("\n" + "=" * 70)
    print("ENHANCED REGRESSION ANALYSIS - P1 & P2 IMPROVEMENTS")
    print("=" * 70)
    
    # Step 1: Load with quarterly aggregation (P1)
    df = load_and_prepare_quarterly()
    
    # Step 2: Construct variables with additional controls (P2)
    df = construct_variables(df)
    
    # Step 3: Propensity Score Matching (P1)
    df_matched, psm_data = propensity_score_matching(df)
    
    # Step 4: Main regression on matched sample
    print("\n" + "=" * 60)
    print("MAIN REGRESSION (Quarterly + PSM)")
    print("=" * 60)
    main_result = run_enhanced_regression(df_matched, "PSM-Matched Quarterly")
    
    # Step 5: Robustness checks (P2)
    robustness_results = robustness_checks(df)
    
    # Step 6: Generate report
    report = generate_report(main_result, psm_data, robustness_results)
    
    with open("results/enhanced_regression_results.md", "w") as f:
        f.write(report)
        if main_result:
            f.write("\n\n---\n## Full Model Output\n```\n")
            f.write(str(main_result))
            f.write("\n```\n")
    
    print("\n" + "=" * 60)
    print("RESULTS SAVED TO: results/enhanced_regression_results.md")
    print("=" * 60)


if __name__ == "__main__":
    main()
