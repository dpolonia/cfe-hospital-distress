import pandas as pd
import numpy as np
from linearmodels.panel import PanelOLS
import statsmodels.api as sm

def run_regression():
    print("Loading Panel Data...")
    df = pd.read_parquet("data/analytical/analytical_panel.parquet")
    
    # 1. Filtering & Cleaning
    # Focus on resolved entities with valid NIFs
    df = df.dropna(subset=['entity_nif', 'year', 'month'])
    
    # Create Index for Panel
    # Use month-level or aggregate to annual? 
    # Plan says "Period: 2017-2024", frequency "Monthly -> aggregate to annual for stability".
    # Let's try annual aggregation first for the baseline, as Financials can be noisy monthly (and GDP is annual).
    
    print("Aggregating to Annual Frequency...")
    # Numeric columns to sum or mean
    cols_sum = ['divida_total_fornecedores_externos', 'divida_vencida_fornecedores_externos']
    cols_mean = ['gdp_per_capita', 'unemployment_rate', 'total_geral'] # Size is sounder as mean
    
    # Group by Entity/Year
    df_annual = df.groupby(['entity_nif', 'year']).agg({
        'divida_total_fornecedores_externos': 'last', # Balance sheet is stock, take last month
        'divida_vencida_fornecedores_externos': 'last',
        'gdp_per_capita': 'max', # Annual constant
        'unemployment_rate': 'max',
        'total_geral': 'mean',
        'entity_name': 'first',
        'entity_type': 'first' # Assuming constant type per year
    }).reset_index()

    # 2. Variable Construction
    # Dependent: Overdue Debt Ratio
    # Handle division by zero/negative debt (unlikely but possible in errors)
    df_annual = df_annual[df_annual['divida_total_fornecedores_externos'] > 0]
    
    df_annual['overdue_ratio'] = df_annual['divida_vencida_fornecedores_externos'] / df_annual['divida_total_fornecedores_externos']
    
    # Sanity Check / Winsorization
    # Cap ratio at 1.5 (some entities might be distressed > 100% but >200% is likely data error or insolvence outlier)
    # Actually, let's just inspect statistics first.
    print(df_annual['overdue_ratio'].describe())
    
    # Independent: Is_ULS
    # Use entity_name or entity_type logic
    # "ULS" usually in name
    df_annual['is_uls'] = df_annual['entity_name'].str.contains("ULS", case=False, na=False).astype(int)
    
    # Independent: Size (Log Staff)
    df_annual['log_staff'] = np.log(df_annual['total_geral'] + 1)
    
    # Independent: GDP (Log)
    df_annual['log_gdp'] = np.log(df_annual['gdp_per_capita'] + 1)
   
    # Set Indices for PanelOLS
    df_annual = df_annual.set_index(['entity_nif', 'year'])
    
    print("\nRunning Fixed Effects Model...")
    # Model: Ratio ~ Is_ULS + Log_Staff + Log_GDP + TimeEffects
    # Note: Entity Effects absorbs Is_ULS if Is_ULS is constant over time.
    # HOWEVER, 2024 is the REFORM year. So many entities CHANGED status!
    # Hospital X -> ULS X.
    # IF the NIF stayed the same (it often does, or we mapped it), then Entity FE allows testing the SWITCH.
    # If NIF changed, they are different entities -> Entity FE absorbs "ULS status" if constant.
    
    # Switch to Time Effects ONLY.
    # Entity FE absorbs 'is_uls' if it doesn't change over time for the same entity.
    # Since we want to compare ULS vs EPE (Cross-Sectional variation), we need to relax Entity FE.
    # We will use Clustered Standard Errors (by Entity) to handle serial correlation.
    
    exog_vars = ['is_uls', 'log_staff', 'log_gdp']
    
    # Drop rows with missing regressors
    data = df_annual.dropna(subset=['overdue_ratio'] + exog_vars)

    mod = PanelOLS(data['overdue_ratio'], sm.add_constant(data[exog_vars]), entity_effects=False, time_effects=True, drop_absorbed=True)
    res = mod.fit(cov_type='clustered', cluster_entity=True)
    
    print(res)
    
    # Save Results
    with open("results/regression_results.txt", "w") as f:
        f.write(str(res))
        f.write("\n\n")
        f.write("Descriptive Statistics (Annual):\n")
        f.write(df_annual.describe().to_markdown())

if __name__ == "__main__":
    run_regression()
