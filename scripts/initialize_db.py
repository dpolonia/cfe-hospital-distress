import os
import pandas as pd
from pathlib import Path

# Configuration
BASE_DIR = Path(r"\\wsl.localhost\Ubuntu\home\dpolonia\CFEtmp")
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
ANALYTICAL_DIR = DATA_DIR / "analytical"
NIFS_SOURCE = BASE_DIR / "nifs_saude.xlsx"

def setup_directories():
    """Create the required directory structure."""
    dirs = [RAW_DIR, PROCESSED_DIR, ANALYTICAL_DIR]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        print(f"Verified directory: {d}")

def normalize_text(series):
    """Normalize text columns: clean whitespace, uppercase."""
    return series.astype(str).str.strip().str.upper()

def create_dim_entities():
    """Read master NIF file and create dim_entities.parquet."""
    print(f"Reading master entity source: {NIFS_SOURCE}")
    
    try:
        # Read Excel file
        df = pd.read_excel(NIFS_SOURCE)
        
        # Select and Rename Columns (adjust based on actual file headers verified earlier)
        # We saw: ['nifEntidade', 'desigEntidade', 'NUTS I']
        df = df.rename(columns={
            'nifEntidade': 'entity_nif',
            'desigEntidade': 'entity_name',
            'NUTS I': 'region_nuts1'
        })
        
        # Data Cleaning
        df['entity_nif'] = df['entity_nif'].astype(str).str.replace(r'\.0$', '', regex=True)
        df['entity_name'] = normalize_text(df['entity_name'])
        
        # Feature Engineering: Entity Type
        df['entity_type'] = 'OTHER'
        df.loc[df['entity_name'].str.contains('ULS'), 'entity_type'] = 'ULS'
        df.loc[df['entity_name'].str.contains('CENTRO HOSPITALAR'), 'entity_type'] = 'CH'
        df.loc[df['entity_name'].str.contains('HOSPITAL'), 'entity_type'] = 'HOSPITAL'
        df.loc[df['entity_name'].str.contains('IPO'), 'entity_type'] = 'IPO'
        
        # Deduplicate (just in case)
        df = df.drop_duplicates(subset=['entity_nif'])
        
        # Save to Parquet
        output_path = PROCESSED_DIR / "dim_entities.parquet"
        df.to_parquet(output_path, index=False)
        print(f"Successfully created {output_path} with {len(df)} entities.")
        print(df.head())
        
    except Exception as e:
        print(f"Error creating dim_entities: {e}")

if __name__ == "__main__":
    setup_directories()
    create_dim_entities()
