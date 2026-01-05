import pandas as pd
from pathlib import Path

# Configuration
BASE_DIR = Path(r"\\wsl.localhost\Ubuntu\home\dpolonia\CFEtmp")
PROCESSED_DIR = BASE_DIR / "data" / "processed"

def load_table(name):
    path = PROCESSED_DIR / f"{name}.parquet"
    if path.exists():
        return pd.read_parquet(path)
    print(f"Warning: {name} not found.")
    return None

def validate_data():
    print("--- Data Validation ---")
    
    # Load Tables
    dim_entities = load_table("dim_entities")
    dim_macro = load_table("dim_macro")
    fact_finance = load_table("fact_financials_monthly")
    fact_debt = load_table("fact_debt_monthly")
    fact_hr = load_table("fact_hr_monthly")
    # fact_contracts might not be ready yet
    fact_contracts = load_table("fact_procurement_contracts")

    # 1. Entity Coverage
    if dim_entities is not None:
        total_entities = len(dim_entities)
        print(f"\nTotal Entities in Dimension: {total_entities}")
        
        for name, df in [("Financials", fact_finance), ("Debt", fact_debt), ("HR", fact_hr)]:
            if df is not None:
                unique_nifs = df['entity_nif'].nunique()
                coverage = (unique_nifs / total_entities) * 100
                print(f"{name} Coverage: {unique_nifs} entities ({coverage:.1f}%)")
                
                # Check for NIFs not in dimension
                missing = set(df['entity_nif']) - set(dim_entities['entity_nif'])
                if missing:
                    print(f"  Alert: {len(missing)} NIFs in {name} not in dim_entities!")
                    print(f"  Examples: {list(missing)[:5]}")

    # 2. Time Coverage
    for name, df in [("Financials", fact_finance), ("Debt", fact_debt), ("HR", fact_hr)]:
        if df is not None and 'year' in df.columns and 'month' in df.columns:
            print(f"\n{name} Time Range:")
            print(f"  Years: {sorted(df['year'].unique())}")
            # Check for gaps (basic)
            
    # 3. Macro Check
    if dim_macro is not None:
        print(f"\nMacro Data Years: {sorted(dim_macro['year'].unique())}")

if __name__ == "__main__":
    validate_data()
