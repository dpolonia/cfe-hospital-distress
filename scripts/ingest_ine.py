import requests
import pandas as pd
from pathlib import Path

# Configuration
BASE_DIR = Path(r"\\wsl.localhost\Ubuntu\home\dpolonia\CFEtmp")
PROCESSED_DIR = BASE_DIR / "data" / "processed"
BASE_URL = "https://www.ine.pt/ine/json_indicador/pindica.jsp"

INDICATORS = {
    "gdp_per_capita": "0009950",        # PIB por habitante
    "unemployment_rate": "0000539",     # Taxa de desemprego
    "population": "0004167"             # População residente
}

def fetch_indicator(code):
    """Fetch all years (Dim1=T) for an indicator."""
    # dim1=T (Time), dim2/3 will be geography depending on indicator
    url = f"{BASE_URL}?op=2&varcd={code}&Dim1=T&lang=PT"
    print(f"Fetching {code} from {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        print(f"Error fetching {code}: {e}")
        return None

def parse_ine_json(data, value_col_name):
    """Parse the specific INE JSON structure into a DataFrame."""
    # Handle list response
    if isinstance(data, list) and len(data) > 0:
        data = data[0]
        
    if not data or 'Dados' not in data:
        return pd.DataFrame()
    
    rows = []
    
    # Check if Dados is a list or dict
    dados = data['Dados']
    
    if isinstance(dados, dict):
        # Format: { "2015": [...], "2016": [...] }
        for year_key, entries in dados.items():
            for entry in entries:
                region = entry.get('geodsg', '') or entry.get('Dim2', '')
                value = entry.get('valor', '').replace(',', '.')
                
                if not value: continue
                try:
                    val_float = float(value)
                except ValueError: continue
                
                rows.append({
                    'year': int(year_key) if year_key.isdigit() else year_key,
                    'region_name': region,
                    value_col_name: val_float
                })
    elif isinstance(dados, list):
        # Format: [ { "Dim1": "2015", ... } ]
        for entry in dados:
            year = entry.get('Dim1', '')
            region = entry.get('Dim2', '') or entry.get('geodsg', '')
            value = entry.get('Valor', '') or entry.get('valor', '')
            value = value.replace(',', '.')
            
            if not value: continue
            try:
                val_float = float(value)
            except ValueError: continue
            
            rows.append({
                'year': int(year) if year.isdigit() else year,
                'region_name': region,
                value_col_name: val_float
            })
            
    return pd.DataFrame(rows)

def ingest_ine():
    dfs = []
    
    # Process each indicator
    for name, code in INDICATORS.items():
        data = fetch_indicator(code)
        df = parse_ine_json(data, name)
        
        if not df.empty:
            print(f"Fetched {len(df)} rows for {name}")
            # Normalize region names (simple cleanup)
            df['region_name'] = df['region_name'].str.strip()
            df = df.drop_duplicates(subset=['year', 'region_name'])
            dfs.append(df)
    
    if not dfs:
        print("No data fetched.")
        return

    # Merge all indicators on Year + Region
    # Start with the first one
    final_df = dfs[0]
    for df in dfs[1:]:
        final_df = pd.merge(final_df, df, on=['year', 'region_name'], how='outer')
    
    # Map Regions to ID (Optional: create a mapping if needed)
    # For now, keeping region_name is fine as dim_macro is a wide table
    
    output_path = PROCESSED_DIR / "dim_macro.parquet"
    final_df.to_parquet(output_path, index=False)
    print(f"Saved dim_macro to {output_path}")
    print(final_df.head())

if __name__ == "__main__":
    ingest_ine()
