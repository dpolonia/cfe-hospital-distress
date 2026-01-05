import pandas as pd
from pathlib import Path
import sys

# Configuration
BASE_DIR = Path(r"\\wsl.localhost\Ubuntu\home\dpolonia\CFEtmp")
PROCESSED_DIR = BASE_DIR / "data" / "processed"
ANALYTICAL_DIR = BASE_DIR / "data" / "analytical"

def load_table(name):
    path = PROCESSED_DIR / f"{name}.parquet"
    if path.exists():
        print(f"Loading {name}...", flush=True)
        try:
            df = pd.read_parquet(path)
            print(f"  {name} columns: {df.columns.tolist()}", flush=True)
            return df
        except Exception as e:
            print(f"  Error loading {name}: {e}", flush=True)
            return None
    print(f"Warning: {name} not found.", flush=True)
    return None

def create_panel():
    ANALYTICAL_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Load Data
    dim_entities = load_table("dim_entities")
    dim_macro = load_table("dim_macro")
    fact_finance = load_table("fact_financials_monthly")
    fact_debt = load_table("fact_debt_monthly")
    fact_hr = load_table("fact_hr_monthly")
    fact_contracts = load_table("fact_procurement_contracts")

    # 2. Create Spine
    print("\n--- Creating Spine ---", flush=True)
    facts = []
    if fact_finance is not None: facts.append(fact_finance)
    if fact_debt is not None: facts.append(fact_debt)
    if fact_hr is not None: facts.append(fact_hr)
    
    spine_parts = []
    for i, df in enumerate(facts):
        req = ['entity_nif', 'year', 'month']
        if all(c in df.columns for c in req):
            spine_parts.append(df[req])
        else:
            print(f"Fact table {i} missing standard columns.", flush=True)
            
    if not spine_parts:
        print("No valid fact tables found.", flush=True)
        return

    spine = pd.concat(spine_parts).drop_duplicates()
    print(f"Spine created: {len(spine)} rows.", flush=True)

    panel = spine.copy()

    # 3. Join Dimensions
    if dim_entities is not None:
        print("Joining Dim Entities...", flush=True)
        if 'entity_nif' in dim_entities.columns and 'entity_nif' in panel.columns:
            try:
                panel = pd.merge(panel, dim_entities, on='entity_nif', how='left')
            except Exception as e:
                print(f"Error joining Dim Entities: {e}", flush=True)
        else:
            print("dim_entities missing entity_nif or panel missing entity_nif", flush=True)

    if dim_macro is not None:
        print("Joining Dim Macro...", flush=True)
        try:
            # Check keys
            # Check keys
            # Use region_nuts2 (enriched names like 'Norte', 'Centro') instead of region_nuts1 (codes 'PT1')
            region_col = 'region_nuts2'
            if region_col in panel.columns and 'year' in panel.columns and 'year' in dim_macro.columns and 'region_name' in dim_macro.columns:
                panel['region_join'] = panel[region_col].astype(str).str.upper().str.strip()
                dim_macro['region_join'] = dim_macro['region_name'].astype(str).str.upper().str.strip().str.replace(r' \(PT\)', '', regex=True)
                # Ensure types match
                panel['year'] = panel['year'].astype(int)
                dim_macro['year'] = dim_macro['year'].astype(int)
                
                panel = pd.merge(panel, dim_macro.drop(columns=['region_name']), 
                                 left_on=['year', 'region_join'], right_on=['year', 'region_join'], how='left', suffixes=('', '_macro'))
                panel.drop(columns=['region_join'], inplace=True)
            else:
               print(f"Skipping Dim Macro join. Missing keys ({region_col}). Panel columns: {panel.columns.tolist()}", flush=True)
        except Exception as e:
            print(f"Merge Macro Failed: {e}", flush=True)

    # 4. Join Facts
    print("Joining Facts...", flush=True)
    for name, df, suffix in [("Video", fact_finance, "_fin"), ("Debt", fact_debt, "_debt"), ("HR", fact_hr, "_hr")]:
        if df is not None:
            try:
               panel = pd.merge(panel, df, on=['entity_nif', 'year', 'month'], how='left', suffixes=('', suffix))
            except Exception as e:
                print(f"Error merging {name}: {e}", flush=True)

    # 5. Join Contracts
    if fact_contracts is not None:
        print("Aggregating Contracts...", flush=True)
        # Check cols
        cols = fact_contracts.columns.tolist()
        date_col = next((c for c in cols if 'data' in c.lower() and 'celebracao' in c.lower()), None)
        price_col = next((c for c in cols if 'preco' in c.lower() and 'contratual' in c.lower()), None)
        
        if date_col and price_col:
            fact_contracts[date_col] = pd.to_datetime(fact_contracts[date_col], errors='coerce')
            fact_contracts['year'] = fact_contracts[date_col].dt.year
            fact_contracts['month'] = fact_contracts[date_col].dt.month
            # Extract NIF if not present
            if 'entity_nif' not in fact_contracts.columns:
                 # Check if 'adjudicante' exists and extract
                 adj_col = next((c for c in cols if 'adjudicante' in c.lower()), None)
                 if adj_col:
                     fact_contracts['entity_nif'] = fact_contracts[adj_col].astype(str).str.extract(r'^(\d+)')
            
            if 'entity_nif' in fact_contracts.columns:
                agg = fact_contracts.groupby(['entity_nif', 'year', 'month']).agg({
                    price_col: 'sum',
                    date_col: 'count'
                }).reset_index().rename(columns={price_col: 'contracts_amount', date_col: 'contracts_count'})
                
                panel = pd.merge(panel, agg, on=['entity_nif', 'year', 'month'], how='left')

    out_path = ANALYTICAL_DIR / "analytical_panel.parquet"
    panel.to_parquet(out_path, index=False)
    print(f"SUCCESS: Analytical Panel saved to {out_path} ({len(panel)} rows)", flush=True)

if __name__ == "__main__":
    create_panel()
