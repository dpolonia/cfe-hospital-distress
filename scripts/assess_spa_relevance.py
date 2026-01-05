import pandas as pd

# Load Panel
df = pd.read_parquet("data/analytical/analytical_panel.parquet")

# Check if 'entity_type' is populated. If not, we might need to infer it or check how many rows have it.
# Our descriptive report said entity_type coverage was low (19.6%), only for resolved entities.
# We will focus on the resolved entities.

resolved = df.dropna(subset=['entity_nif'])

print(f"Total Resolved Rows: {len(resolved)}")

# Check distinct entity types
if 'entity_type' in resolved.columns:
    print("\nEntity Type Counts (Rows):")
    print(resolved['entity_type'].value_counts(dropna=False))

    print("\nEntity Type Counts (Distinct Entities):")
    distinct_types = resolved.groupby('entity_nif')['entity_type'].first()
    print(distinct_types.value_counts(dropna=False))

    # Financial Magnitude Comparison
    # We use 'divida_total_fornecedores_externos' as a proxy for size/relevance
    # Group by Type and sum metric (average annual maybe?)
    
    # Calculate simple mean of total debt per type
    summary = resolved.groupby('entity_type')['divida_total_fornecedores_externos'].describe()[['count', 'mean', 'max']]
    print("\nFinancial Magnitude (Total Debt) by Type:")
    print(summary.to_markdown())
else:
    print("Column 'entity_type' not found or empty.")
