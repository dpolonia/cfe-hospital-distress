"""
CORRECTED ANALYSIS: Financial Distress and ULS Reform (Jan 2024)
================================================================
Critical Correction: 8 ULS existed BEFORE the 2024 reform.

CONTROL GROUP (8 Pre-existing ULS - No structural change in 2024):
- ULS Matosinhos (1999)
- ULS Guarda (2008)
- ULS Baixo Alentejo (2008)
- ULS Alto Minho (2008)
- ULS Castelo Branco (2010)
- ULS Nordeste (2011)
- ULS Litoral Alentejano (2012)
- ULS Alto Alentejo / Norte Alentejano (2007)

TREATMENT GROUP (All other hospitals merged into NEW ULS on Jan 1, 2024)
"""
import pandas as pd
import numpy as np
from linearmodels.panel import PanelOLS
import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import warnings
warnings.filterwarnings('ignore')


# === CRITICAL: Define the 8 pre-existing ULS ===
PRE_EXISTING_ULS = [
    "matosinhos",
    "guarda", 
    "baixo alentejo",
    "alto minho",
    "castelo branco",
    "nordeste",
    "litoral alentejano",
    "alto alentejo",
    "norte alentejano",  # Former name of Alto Alentejo
]


def is_pre_existing_uls(entity_name):
    """Check if entity is one of the 8 pre-existing ULS."""
    if pd.isna(entity_name):
        return False
    name_lower = entity_name.lower()
    for uls_name in PRE_EXISTING_ULS:
        if uls_name in name_lower:
            return True
    return False


def load_and_classify_data():
    """
    Load data and classify entities into:
    - pre_existing_uls: The 8 ULS that existed before 2024 (CONTROL)
    - new_uls_2024: Entities that became ULS in Jan 2024 (TREATMENT)
    """
    print("=" * 70)
    print("LOADING AND CLASSIFYING DATA")
    print("=" * 70)
    
    df = pd.read_parquet("data/analytical/analytical_panel.parquet")
    df = df.dropna(subset=['entity_nif', 'year', 'month'])
    
    # Create quarter
    df['quarter'] = ((df['month'] - 1) // 3) + 1
    
    # Aggregate to quarterly
    df_q = df.groupby(['entity_nif', 'year', 'quarter']).agg({
        'divida_total_fornecedores_externos': 'last',
        'divida_vencida_fornecedores_externos': 'last',
        'gdp_per_capita': 'max',
        'total_geral': 'mean',
        'entity_name': 'first',
        'region_nuts2': 'first',
    }).reset_index()
    
    # Filter valid financial data
    df_q = df_q[df_q['divida_total_fornecedores_externos'] > 0]
    
    # === CRITICAL CLASSIFICATION ===
    # Check if entity is a pre-existing ULS
    df_q['is_pre_existing_uls'] = df_q['entity_name'].apply(is_pre_existing_uls).astype(int)
    
    # Create post-2024 indicator
    df_q['post_2024'] = (df_q['year'] >= 2024).astype(int)
    
    # Treatment indicator: Entity that became NEW ULS in 2024
    # Pre-2024: These were EPE hospitals (is_pre_existing_uls = 0)
    # Post-2024: These are now NEW ULS
    df_q['is_new_uls_treatment'] = ((df_q['is_pre_existing_uls'] == 0)).astype(int)
    
    # DiD Interaction: Treatment × Post
    df_q['did_interaction'] = df_q['is_new_uls_treatment'] * df_q['post_2024']
    
    # Variables
    df_q['overdue_ratio'] = df_q['divida_vencida_fornecedores_externos'] / df_q['divida_total_fornecedores_externos']
    df_q['log_staff'] = np.log(df_q['total_geral'] + 1)
    df_q['log_gdp'] = np.log(df_q['gdp_per_capita'] + 1)
    df_q['time_id'] = df_q['year'] * 10 + df_q['quarter']
    
    # Print classification summary
    pre_uls_entities = df_q[df_q['is_pre_existing_uls'] == 1]['entity_nif'].nunique()
    new_uls_entities = df_q[df_q['is_new_uls_treatment'] == 1]['entity_nif'].nunique()
    
    print(f"\n  Total Observations: {len(df_q)}")
    print(f"  Total Entities: {df_q['entity_nif'].nunique()}")
    print(f"\n  CONTROL (Pre-existing ULS): {pre_uls_entities} entities")
    print(f"  TREATMENT (New ULS 2024): {new_uls_entities} entities")
    
    # List the pre-existing ULS found
    pre_uls_names = df_q[df_q['is_pre_existing_uls'] == 1]['entity_name'].unique()
    print(f"\n  Pre-existing ULS identified:")
    for name in pre_uls_names[:10]:
        print(f"    - {name}")
    
    return df_q


def run_did_analysis(df):
    """
    Difference-in-Differences Analysis
    
    Model: Y_it = α + β₁(Treatment_i) + β₂(Post_t) + β₃(Treatment × Post) + ε_it
    
    β₃ is the DiD estimator - the causal effect of the 2024 ULS reform
    """
    print("\n" + "=" * 70)
    print("DIFFERENCE-IN-DIFFERENCES ANALYSIS")
    print("=" * 70)
    
    # Prepare data
    data = df.dropna(subset=['overdue_ratio', 'is_new_uls_treatment', 'post_2024']).copy()
    
    # Check we have variation in all dimensions
    print(f"\n  Treatment (New ULS): {data['is_new_uls_treatment'].value_counts().to_dict()}")
    print(f"  Post-2024: {data['post_2024'].value_counts().to_dict()}")
    print(f"  DiD Interaction: {data['did_interaction'].value_counts().to_dict()}")
    
    data = data.set_index(['entity_nif', 'time_id'])
    
    # Model 1: Simple DiD
    print("\n--- Model 1: Simple DiD ---")
    exog1 = ['is_new_uls_treatment', 'post_2024', 'did_interaction']
    
    try:
        mod1 = PanelOLS(data['overdue_ratio'], sm.add_constant(data[exog1]), 
                        entity_effects=False, time_effects=False, drop_absorbed=True)
        res1 = mod1.fit(cov_type='clustered', cluster_entity=True)
        
        print(f"\n  is_new_uls_treatment : {res1.params.get('is_new_uls_treatment', 0):.4f} (p={res1.pvalues.get('is_new_uls_treatment', 1):.4f})")
        print(f"  post_2024            : {res1.params.get('post_2024', 0):.4f} (p={res1.pvalues.get('post_2024', 1):.4f})")
        print(f"  DiD (Treatment×Post) : {res1.params.get('did_interaction', 0):.4f} (p={res1.pvalues.get('did_interaction', 1):.4f})")
        print(f"\n  >>> DiD Effect: {res1.params.get('did_interaction', 0):.4f}")
        
    except Exception as e:
        print(f"  Error: {e}")
        res1 = None
    
    # Model 2: DiD with Controls
    print("\n--- Model 2: DiD with Controls + Time FE ---")
    exog2 = ['is_new_uls_treatment', 'did_interaction', 'log_staff']
    data_ctrl = data.dropna(subset=exog2)
    
    try:
        mod2 = PanelOLS(data_ctrl['overdue_ratio'], sm.add_constant(data_ctrl[exog2]), 
                        entity_effects=False, time_effects=True, drop_absorbed=True)
        res2 = mod2.fit(cov_type='clustered', cluster_entity=True)
        
        print(f"\n  is_new_uls_treatment : {res2.params.get('is_new_uls_treatment', 0):.4f} (p={res2.pvalues.get('is_new_uls_treatment', 1):.4f})")
        print(f"  DiD (Treatment×Post) : {res2.params.get('did_interaction', 0):.4f} (p={res2.pvalues.get('did_interaction', 1):.4f})")
        print(f"  log_staff            : {res2.params.get('log_staff', 0):.4f} (p={res2.pvalues.get('log_staff', 1):.4f})")
        
    except Exception as e:
        print(f"  Error: {e}")
        res2 = None
    
    return res1, res2


def analyze_parallel_trends(df):
    """
    Test Parallel Trends Assumption
    Plot pre-2024 trends for Control vs Treatment groups
    """
    print("\n" + "=" * 70)
    print("PARALLEL TRENDS ANALYSIS")
    print("=" * 70)
    
    # Annual averages by group
    annual = df.groupby(['year', 'is_new_uls_treatment'])['overdue_ratio'].mean().unstack()
    annual.columns = ['Control (Pre-existing ULS)', 'Treatment (New ULS 2024)']
    
    print("\nAnnual Overdue Ratio by Group:")
    print(annual.to_markdown())
    
    # Calculate pre-2024 trend difference
    pre_2024 = annual[annual.index < 2024]
    if len(pre_2024) > 1:
        control_trend = pre_2024['Control (Pre-existing ULS)'].diff().mean()
        treatment_trend = pre_2024['Treatment (New ULS 2024)'].diff().mean()
        print(f"\n  Pre-2024 Trend (Control): {control_trend:.4f} per year")
        print(f"  Pre-2024 Trend (Treatment): {treatment_trend:.4f} per year")
        print(f"  Trend Difference: {abs(control_trend - treatment_trend):.4f}")
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(12, 7))
    
    if 'Control (Pre-existing ULS)' in annual.columns:
        annual['Control (Pre-existing ULS)'].plot(ax=ax, marker='o', linewidth=2, 
                                                   label='Control: Pre-existing ULS (8 entities)')
    if 'Treatment (New ULS 2024)' in annual.columns:
        annual['Treatment (New ULS 2024)'].plot(ax=ax, marker='s', linewidth=2,
                                                 label='Treatment: Hospitals -> New ULS (2024)')
    
    # Mark 2024 reform
    ax.axvline(x=2024, color='red', linestyle='--', linewidth=2, label='Jan 2024: ULS Reform')
    ax.axvspan(2024, annual.index.max(), alpha=0.1, color='red')
    
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Average Overdue Debt Ratio', fontsize=12)
    ax.set_title('Difference-in-Differences: Pre-existing ULS vs New ULS (2024 Reform)', fontsize=14)
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('results/did_parallel_trends.png', dpi=150)
    print("\n  Figure saved: results/did_parallel_trends.png")
    
    return annual


def generate_corrected_report(did_simple, did_controls, trends_data):
    """Generate the corrected comprehensive report."""
    
    report = """# CORRECTED ANALYSIS: ULS Reform and Financial Distress
## Difference-in-Differences with Proper Control Group

**Date:** January 2026  
**Critical Correction Applied:** 8 Pre-existing ULS identified as Control Group

---

## Research Design

### The 2024 ULS Reform (Decreto-Lei 102/2023)
On January 1, 2024, all Portuguese public hospitals were merged into ULS (Unidades Locais de Saude).
However, **8 ULS already existed** before this reform (created 1999-2012).

### Control vs Treatment Groups

| Group | Entities | Description |
|-------|----------|-------------|
| **Control** | 8 Pre-existing ULS | Matosinhos, Guarda, Baixo Alentejo, Alto Minho, Castelo Branco, Nordeste, Litoral Alentejano, Alto Alentejo |
| **Treatment** | All other hospitals | EPE hospitals that merged into NEW ULS on Jan 1, 2024 |

### DiD Model Specification

```
Overdue_Ratio = a + b1(Treatment) + b2(Post_2024) + b3(Treatment x Post_2024) + e

Where b3 = DiD estimator (causal effect of becoming NEW ULS)
```

---

## Results

### Difference-in-Differences Estimates

"""
    
    if did_simple:
        report += f"""| Coefficient | Estimate | P-value | Interpretation |
|-------------|----------|---------|----------------|
| Treatment (New ULS) | {did_simple.params.get('is_new_uls_treatment', 0):.4f} | {did_simple.pvalues.get('is_new_uls_treatment', 1):.4f} | Pre-existing difference |
| Post-2024 | {did_simple.params.get('post_2024', 0):.4f} | {did_simple.pvalues.get('post_2024', 1):.4f} | Time trend for control |
| **DiD (Treatment x Post)** | **{did_simple.params.get('did_interaction', 0):.4f}** | **{did_simple.pvalues.get('did_interaction', 1):.4f}** | **Causal Effect** |

"""
        
        did_effect = did_simple.params.get('did_interaction', 0)
        did_pval = did_simple.pvalues.get('did_interaction', 1)
        
        if did_pval < 0.05:
            sig = "statistically significant at 5%"
        elif did_pval < 0.10:
            sig = "marginally significant at 10%"
        else:
            sig = "not statistically significant"
        
        report += f"""### Interpretation

The DiD estimator is **{did_effect:.4f}** ({sig}).

This means that hospitals which became NEW ULS in 2024 experienced a 
**{abs(did_effect)*100:.1f} percentage point {"increase" if did_effect > 0 else "decrease"}** 
in overdue debt ratio compared to the pre-existing ULS control group.

"""
    
    report += """---

## Parallel Trends Visualization

![DiD Parallel Trends](results/did_parallel_trends.png)

---

## Validity Assessment

### Parallel Trends Assumption
- Visual inspection required (see figure above)
- If pre-2024 trends are parallel, DiD estimate is valid

### Selection Concerns
- Pre-existing ULS were created in regions with specific characteristics
- May not be perfectly comparable to hospitals that became ULS in 2024

---

*Report generated: January 2026*
*Corrected analysis with proper treatment/control classification*
"""
    
    with open("results/corrected_did_analysis.md", "w", encoding="utf-8") as f:
        f.write(report)
    
    print("\n" + "=" * 70)
    print("CORRECTED REPORT SAVED: results/corrected_did_analysis.md")
    print("=" * 70)


def main():
    print("\n" + "=" * 70)
    print("CORRECTED ANALYSIS: ULS REFORM DiD")
    print("With Pre-existing ULS as Control Group")
    print("=" * 70)
    
    # Load and classify
    df = load_and_classify_data()
    
    # Parallel trends
    trends = analyze_parallel_trends(df)
    
    # DiD analysis
    did_simple, did_controls = run_did_analysis(df)
    
    # Generate report
    generate_corrected_report(did_simple, did_controls, trends)
    
    print("\n" + "=" * 70)
    print("CORRECTED ANALYSIS COMPLETE!")
    print("=" * 70)


if __name__ == "__main__":
    main()
