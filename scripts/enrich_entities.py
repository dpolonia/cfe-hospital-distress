import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(r"\\wsl.localhost\Ubuntu\home\dpolonia\CFEtmp")
PROCESSED_DIR = BASE_DIR / "data" / "processed"

def enrich_entities():
    dim_path = PROCESSED_DIR / "dim_entities.parquet"
    if not dim_path.exists():
        print("dim_entities.parquet not found.")
        return

    df = pd.read_parquet(dim_path)
    print(f"Loaded {len(df)} entities.")

    # Mapping Logic
    def get_region(name):
        n = name.lower()
        if 'norte' in n or 'braga' in n or 'porto' in n or 'minho' in n or 'tamega' in n or 'tras-os-montes' in n or 'douro' in n or 'gaia' in n or 'matosinhos' in n or 'sao joao' in n or 'barcelos' in n or 'povoa' in n or 'santo antonio' in n or 'alto ave' in n or 'medio ave' in n or 'nordeste' in n:
            return 'Norte'
        if 'centro' in n or 'coimbra' in n or 'leiria' in n or 'castelo branco' in n or 'guarda' in n or 'viseu' in n or 'covilha' in n or 'aveiro' in n or 'cova da beira' in n or 'baixo mondego' in n or 'dao' in n:
            return 'Centro'
        # Oeste and Medio Tejo are NUTS II Centro statistically (usually), though ARS LVT
        if 'oeste' in n and 'lisboa' not in n: 
             return 'Centro' # Map to Centro for INE GDP compatibility (NUTS 2013)
        if 'medio tejo' in n:
             return 'Centro'

        # Leziria do Tejo is NUTS II Alentejo (2013) or Centro (2024)? 
        # INE data likely 2013 NUTS II -> Alentejo.
        if 'leziria' in n:
            return 'Alentejo'

        # LISBOA / AML
        if 'lisboa' in n or 'lvt' in n or 'tejo' in n or 'sintra' in n or 'amadora' in n or 'loures' in n or 'odivelas' in n or 'cascais' in n or 'setubal' in n or 'garcia de orta' in n or 'santa maria' in n or 'sao jose' in n or 'capuchos' in n or 'arrabida' in n or 'almada' in n or 'arco ribeirinho' in n or 'estuario' in n:
            return 'Área Metropolitana de Lisboa'
        
        if 'alentejo' in n or 'evora' in n or 'beja' in n or 'alegre' in n or 'litoral alentejano' in n:
            return 'Alentejo'
        if 'algarve' in n or 'faro' in n or 'portimao' in n:
            return 'Algarve'
        if 'acores' in n:
            return 'Região Autónoma dos Açores'
        if 'madeira' in n:
             return 'Região Autónoma da Madeira'
        return 'Unknown'

    df['region_nuts2'] = df['entity_name'].apply(get_region)
    
    # Specific Ovar Override (User request: ULS Entre Douro e Vouga -> Norte)
    # The heuristic 'douro' catches it (Entre Douro e Vouga), mapping to Norte.
    # ULS Regiao de Aveiro -> Centro (caught by 'aveiro')
    
    print("Region Distribution:")
    print(df['region_nuts2'].value_counts())
    
    # Check remaining unknowns
    unknowns = df[df['region_nuts2'] == 'Unknown']['entity_name'].tolist()
    if unknowns:
        print(f"Remaining Unknowns ({len(unknowns)}): {unknowns[:5]}...")

    df.to_parquet(dim_path, index=False)
    print(f"Updated {dim_path} with region_nuts2")

if __name__ == "__main__":
    enrich_entities()
