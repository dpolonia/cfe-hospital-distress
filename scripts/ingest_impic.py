import requests
import pandas as pd
from pathlib import Path
import os
from entity_resolution import resolve_entities

# Configuration
BASE_DIR = Path(r"\\wsl.localhost\Ubuntu\home\dpolonia\CFEtmp")
RAW_DIR = BASE_DIR / "data" / "raw" / "impic"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
DIM_ENTITIES_PATH = PROCESSED_DIR / "dim_entities.parquet"

# Dataset ID for "Contratos (2012-2025)"
DATASET_ID = "contratos-publicos-portal-base-impic-contratos-de-2012-a-2025"
API_URL = f"https://dados.gov.pt/api/1/datasets/{DATASET_ID}/"

def get_target_nifs():
    """Load NIFs from dim_entities to filter contracts."""
    if not DIM_ENTITIES_PATH.exists():
        print("Dim Entities not found.")
        return []
    df = pd.read_parquet(DIM_ENTITIES_PATH)
    return set(df['entity_nif'].astype(str).tolist())

def download_file(url, local_path):
    """Download file if it doesn't exist."""
    if local_path.exists():
        print(f"File exists: {local_path}")
        return True
    
    print(f"Downloading {url} to {local_path}...")
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

def ingest_impic():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    target_nifs = get_target_nifs()
    print(f"Filtering for {len(target_nifs)} Health Sector Entities.")

    # 1. Get Resource URLs
    print("Fetching dataset metadata...")
    try:
        meta = requests.get(API_URL).json()
    except Exception as e:
        print(f"API Error: {e}")
        return

    resources = meta.get('resources', [])
    # Filter for xlsx files, ignore zips for now to avoid extraction complexity unless needed
    # Sort by year (descending)
    xlsx_resources = [r for r in resources if r['format'] == 'xlsx' and 'contratos20' in r['title']]
    
    all_contracts = []

    # Limit to recent years for testing? Or do all?
    # Let's do 2022-2024 for now to validate logic, or all if feasible.
    # We will try to process all found.
    
    for res in xlsx_resources:
        title = res['title']
        url = res['url']
        local_path = RAW_DIR / title
        
        if download_file(url, local_path):
            print(f"Processing {title}...")
            try:
                # Read specific columns to save memory
                # Columns usually: idcontrato, nif_entidade_adjudicante, entidade_adjudicante, ...
                # We need to inspect columns. Let's read header first.
                df_header = pd.read_excel(local_path, nrows=0)
                cols = [c for c in df_header.columns]
                
                # Identify NIF column or Adjudicante column
                nif_col = next((c for c in cols if 'nif' in c.lower() and 'adjudicante' in c.lower()), None)
                adj_col = 'adjudicante' if 'adjudicante' in [c.lower() for c in cols] else None
                
                target_col = nif_col if nif_col else adj_col
                
                if not target_col:
                    print(f"Skipping {title}: Could not find NIF or Adjudicante column.")
                    print(f"Columns found: {cols}")
                    continue
                
                # Read full file
                df = pd.read_excel(local_path)
                
                # Extract NIF if using 'adjudicante' column (format: "500000000 - Name")
                if target_col == adj_col:
                    # Extract the first sequence of digits
                    df['entity_nif'] = df[target_col].astype(str).str.extract(r'^(\d+)')
                else:
                    df['entity_nif'] = df[target_col].astype(str).str.replace(r'\.0$', '', regex=True)
                
                # Filter
                filtered = df[df['entity_nif'].isin(target_nifs)].copy()
                
                if not filtered.empty:
                    print(f"Found {len(filtered)} relevant contracts in {title}.")
                    # Standardize columns
                    filtered['source_file'] = title
                    
                    # Fix types for Parquet
                    text_cols = [
                        'objectoContrato', 'tipoContrato', 'tipoprocedimento', 'adjudicante', 'adjudicatarios',
                        'descContrato', 'LocalExecucao', 'fundamentacao', 'Observacoes',
                        'justifNReducEscrContrato', 'tipoFimContrato', 'CritMateriais', 'fundamentAjusteDireto'
                    ]
                    for tc in text_cols:
                        if tc in filtered.columns:
                            filtered[tc] = filtered[tc].astype(str)
                            
                    all_contracts.append(filtered)
            except Exception as e:
                print(f"Error processing {title}: {e}")

    if all_contracts:
        final_df = pd.concat(all_contracts, ignore_index=True)
        out_path = PROCESSED_DIR / "fact_procurement_contracts.parquet"
        final_df.to_parquet(out_path, index=False)
        print(f"Saved {len(final_df)} contracts to {out_path}")
    else:
        print("No contracts found for target entities.")

if __name__ == "__main__":
    ingest_impic()
