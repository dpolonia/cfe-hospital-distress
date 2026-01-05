import requests
import pandas as pd
from pathlib import Path
import io
from entity_resolution import resolve_entities

# Configuration
BASE_API = "https://transparencia.sns.gov.pt/api/explore/v2.1/catalog/datasets"
BASE_DIR = Path(r"\\wsl.localhost\Ubuntu\home\dpolonia\CFEtmp")
PROCESSED_DIR = BASE_DIR / "data" / "processed"

DATASETS = {
    "financials": "agregados-economico-financeiros",
    "debt": "divida-total-vencida-e-pagamentos",
    "hr": "trabalhadores-por-grupo-profissional"
}

def fetch_dataset_export(dataset_id):
    """Fetch full dataset export as JSON."""
    url = f"{BASE_API}/{dataset_id}/exports/json?use_labels=true"
    print(f"Fetching {dataset_id} from {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        df = pd.DataFrame(response.json())
        print(f"Columns in {dataset_id}: {df.columns.tolist()}")
        return df
    except Exception as e:
        print(f"Error fetching {dataset_id}: {e}")
        return None

def normalize_cols(df):
    """Normalize column names to lowercase ascii to find match."""
    # Create a map of normalized -> original
    col_map = {c.lower().replace('ç', 'c').replace('ã', 'a').replace('õ', 'o').replace('í', 'i').strip(): c for c in df.columns}
    return col_map

def get_col_name(df, candidates):
    """Find the actual column name from a list of candidates."""
    col_map = normalize_cols(df)
    for cand in candidates:
        norm_cand = cand.lower().replace('ç', 'c').replace('ã', 'a').replace('õ', 'o').replace('í', 'i').strip()
        if norm_cand in col_map:
            return col_map[norm_cand]
    return None

def standardize_dates(df, date_col):
    """Convert date column to datetime and extract Year-Month."""
    df['date'] = pd.to_datetime(df[date_col], errors='coerce')
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['date_key'] = df['date'].dt.to_period('M').dt.to_timestamp()
    return df

def apply_resolution(df, name_col):
    """Resolve entity names to NIFs."""
    unique_names = df[name_col].dropna().unique().tolist()
    print(f"Resolving {len(unique_names)} unique entities...")
    
    matches = resolve_entities(unique_names)
    
    if matches is None or matches.empty:
        print("Warning: No matches returned.")
        return df
    
    # Merge matches back to original dataframe
    name_map = matches.set_index('original_name')['matched_nif'].to_dict()
    df['entity_nif'] = df[name_col].map(name_map)
    
    matched_count = df['entity_nif'].notnull().sum()
    print(f"Matched {matched_count} / {len(df)} rows ({matched_count/len(df):.1%})")
    return df

def process_financials():
    df = fetch_dataset_export(DATASETS["financials"])
    if df is None: return

    print("Processing Financials...")
    inst_col = get_col_name(df, ['Instituição', 'Entidade', 'instituicao', 'entidade'])
    date_col = get_col_name(df, ['Período', 'Periodo', 'Data', 'periodo'])
    
    if not inst_col:
        print(f"CRITICAL: Could not find Institution column. Available: {df.columns.tolist()}")
        return

    df = apply_resolution(df, inst_col)
    
    if date_col:
        df = standardize_dates(df, date_col)
    else:
        print("Warning: No date column found.")
    
    # numeric conversion (exclude non-numeric)
    exclude_cols = [inst_col, 'date', 'date_key', 'entity_nif']
    if date_col: exclude_cols.append(date_col)
    
    cols_to_numeric = [c for c in df.columns if c not in exclude_cols]
    for c in cols_to_numeric:
        if df[c].dtype == 'object':
             df[c] = pd.to_numeric(df[c].astype(str).str.replace(',', '.'), errors='coerce')
    
    output_path = PROCESSED_DIR / "fact_financials_monthly.parquet"
    df.to_parquet(output_path, index=False)
    print(f"Saved {output_path}")

def process_debt():
    df = fetch_dataset_export(DATASETS["debt"])
    if df is None: return

    print("Processing Debt...")
    inst_col = get_col_name(df, ['Instituição', 'Entidade', 'instituicao', 'entidade'])
    date_col = get_col_name(df, ['Período', 'Periodo', 'Data', 'periodo'])
    
    if not inst_col:
        print(f"CRITICAL: Could not find Institution column. Available: {df.columns.tolist()}")
        return

    df = apply_resolution(df, inst_col)
    if date_col:
        df = standardize_dates(df, date_col)
    
    output_path = PROCESSED_DIR / "fact_debt_monthly.parquet"
    df.to_parquet(output_path, index=False)
    print(f"Saved {output_path}")

def process_hr():
    df = fetch_dataset_export(DATASETS["hr"])
    if df is None: return

    print("Processing HR...")
    inst_col = get_col_name(df, ['Instituição', 'Entidade', 'instituicao', 'entidade'])
    date_col = get_col_name(df, ['Período', 'Periodo', 'Data', 'periodo'])

    if not inst_col:
        print(f"CRITICAL: Could not find Institution column. Available: {df.columns.tolist()}")
        return
    
    df = apply_resolution(df, inst_col)
    if date_col:
        df = standardize_dates(df, date_col)
    
    output_path = PROCESSED_DIR / "fact_hr_monthly.parquet"
    df.to_parquet(output_path, index=False)
    print(f"Saved {output_path}")

if __name__ == "__main__":
    process_financials()
    process_debt()
    process_hr()
