import pandas as pd
from pathlib import Path
try:
    from rapidfuzz import process, fuzz
except ImportError:
    from fuzzywuzzy import process, fuzz
from difflib import SequenceMatcher
from difflib import SequenceMatcher
import re

# Configuration
BASE_DIR = Path(r"\\wsl.localhost\Ubuntu\home\dpolonia\CFEtmp")
PROCESSED_DIR = BASE_DIR / "data" / "processed"
DIM_ENTITIES_PATH = PROCESSED_DIR / "dim_entities.parquet"

def clean_text(text):
    """Aggressively clean text for matching."""
    if not isinstance(text, str):
        return ""
    text = text.upper()
    # Remove common prefixes/suffixes
    text = re.sub(r'\b(HOSPITAL|CENTRO HOSPITALAR|ULS|EPE|SPA|DE|DO|DA|DOS|DAS)\b', ' ', text)
    # Remove punctuation and extra spaces
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def calculate_similarity(a, b):
    """Return similarity ratio between 0 and 1."""
    return SequenceMatcher(None, a, b).ratio()

def resolve_entities(target_names, threshold=0.6):
    """
    Match a list of names against the master entity list.
    Returns a DataFrame with columns: [original_name, matched_nif, matched_name, score, status]
    """
    print(f"Loading master entities from {DIM_ENTITIES_PATH}...")
    try:
        dim_entities = pd.read_parquet(DIM_ENTITIES_PATH)
    except FileNotFoundError:
        print("Error: dim_entities.parquet not found. Run initialize_db.py first.")
        return None

    # Pre-clean master names
    master_records = []
    for _, row in dim_entities.iterrows():
        master_records.append({
            'nif': row['entity_nif'],
            'name': row['entity_name'],
            'clean_name': clean_text(row['entity_name'])
        })

    # Create reference lists
    reference_names = dim_entities['entity_name'].tolist()
    # Create name -> nif map
    reference_entities_map = dim_entities.set_index('entity_name')['entity_nif'].to_dict()
    # Also map Desig to NIF? No, entity_name is desigEntidade.
    
    # Load mapping file
    mapping_path = Path(__file__).parent / "hospital_to_uls_mapping_corrected.csv"
    name_map = {}
    if mapping_path.exists():
        try:
            map_df = pd.read_csv(mapping_path, sep=';')
            for _, row in map_df.iterrows():
                old = str(row.get('old_hospital_name', '')).strip()
                new = str(row.get('parent_uls', '')).strip()
                if old and new:
                    name_map[old.lower()] = new
        except Exception as e:
            print(f"Error loading mapping file: {e}")

    results = []
    
    print(f"Resolving {len(target_names)} entities...")
    
    for original_name in target_names:
        if not isinstance(original_name, str):
            results.append({'original_name': original_name, 'matched_nif': None, 'matched_name': None, 'confidence_score': 0, 'status': 'INVALID'})
            continue
            
        clean_name_for_map = original_name.strip()
        
        best_match_name = None
        best_score = 0.0

        # 1. Try Mapping File first
        if clean_name_for_map.lower() in name_map:
            mapped_name_candidate = name_map[clean_name_for_map.lower()]
            # print(f"DEBUG: Mapped '{original_name}' -> '{mapped_name_candidate}'")
            
            # Use token_sort_ratio for precise mapped name matching
            match_result_mapped = process.extractOne(mapped_name_candidate.upper(), reference_names, scorer=fuzz.token_sort_ratio)
            # print(f"DEBUG: Match Result from map: {match_result_mapped}")
            
            if match_result_mapped:
                best_match_name = match_result_mapped[0]
                best_score = match_result_mapped[1] / 100.0
        
        # 2. If no good match from mapping (or no mapping applied), try Direct Fuzzy Match
        # Only perform direct fuzzy match if the current best_score is below the threshold
        # or if no mapping was found/applied.
        if best_score < threshold:
            # FORCE UPPERCASE for matching
            match_result_direct = process.extractOne(original_name.upper(), reference_names, scorer=fuzz.token_set_ratio)
            if match_result_direct:
                score_direct = match_result_direct[1] / 100.0
                if score_direct > best_score: # Only update if direct match is better
                    best_match_name = match_result_direct[0]
                    best_score = score_direct

        status = "MATCH" if best_score >= threshold else "UNMATCHED"
        
        matched_nif = None
        matched_name = None
        if best_match_name and status == "MATCH":
             # Need to find NIF from best_match_name. 
             # reference_entities_map is set up above.
             if best_match_name in reference_entities_map:
                 matched_nif = reference_entities_map[best_match_name]
             else:
                 # fallback if name not in map (unlikely if extracted from list of keys)
                 # Try finding row in df
                 matched_nif = dim_entities[dim_entities['entity_name'] == best_match_name]['entity_nif'].iloc[0]

             matched_name = best_match_name

        results.append({
            'original_name': original_name,
            'matched_nif': matched_nif,
            'matched_name': matched_name,
            'confidence_score': round(best_score, 2),
            'status': status
        })

    return pd.DataFrame(results)

if __name__ == "__main__":
    # Test with some sample messy names often found in SNS data
    test_names = [
        "hosp. santa maria",
        "centro hosp. lisboa norte",
        "uls da guarda",
        "hospital de braga",
        "unidade local de saude do alto minho"
    ]
    
    df_results = resolve_entities(test_names)
    if df_results is not None:
        print("\nResolution Results:")
        print(df_results.to_markdown(index=False))
