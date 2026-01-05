import pandas as pd
import numpy as np
import os

# Configuration
INPUT_FILE = r"data/analytical/analytical_panel.parquet"
OUTPUT_FILE = r"results/descriptive_report.md"

def generate_report():
    print(f"Loading {INPUT_FILE}...")
    try:
        df = pd.read_parquet(INPUT_FILE)
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    print(f"Loaded {len(df)} rows and {len(df.columns)} columns.")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# Descriptive Analysis Report\n\n")
        f.write(f"**Total Observations**: {len(df)}\n")
        f.write(f"**Total Entities**: {df['entity_nif'].nunique()}\n")
        f.write(f"**Time Period**: {df['year'].min()} - {df['year'].max()}\n\n")

        # 1. Variable Availability
        f.write("## 1. Variable Availability (Top 50)\n")
        f.write("| Variable | Non-Null Count | Coverage % |\n")
        f.write("|---|---|---|\n")
        
        # Sort by coverage
        coverage = df.count().sort_values(ascending=False).head(50)
        for col, count in coverage.items():
            f.write(f"| {col} | {count} | {count/len(df):.1%} |\n")
        f.write("\n")

        # 2. Key Financial Statistics
        # Identify columns simply by keywords if exact names vary
        fin_keywords = ['rendimentos', 'gastos', 'ebitda', 'resultado', 'divida', 'vencida']
        fin_cols = [c for c in df.columns if any(k in c.lower() for k in fin_keywords) and pd.api.types.is_numeric_dtype(df[c])]
        
        if fin_cols:
            f.write("## 2. Key Financial Statistics (Mean/Median)\n")
            stats = df[fin_cols].describe().T[['mean', '50%', 'min', 'max', 'std']]
            f.write(stats.to_markdown())
            f.write("\n\n")

        # 3. Macro & Context
        macro_cols = ['gdp_per_capita', 'unemployment_rate', 'population', 'contracts_amount', 'contracts_count']
        existing_macro = [c for c in macro_cols if c in df.columns]
        
        if existing_macro:
             f.write("## 3. Macro & Context Statistics\n")
             stats_macro = df[existing_macro].describe().T
             f.write(stats_macro.to_markdown())
             f.write("\n\n")

        # 4. Outlier Detection (Top 5 Debt Ratios)
        # Attempt to find 'Divida Vencida' and 'Divida Total'
        d_vencida = next((c for c in df.columns if 'vencida' in c.lower()), None)
        d_total = next((c for c in df.columns if 'divida total' in c.lower() or 'divida_total' in c.lower()), None)

        if d_vencida and d_total:
             f.write("## 4. Top 10 Ratios (Overdue / Total Debt)\n")
             df['debt_ratio'] = df[d_vencida] / df[d_total]
             top_ratios = df.nlargest(10, 'debt_ratio')[['entity_name', 'year', 'month', 'debt_ratio', d_vencida, d_total]]
             f.write(top_ratios.to_markdown(index=False))
        else:
             f.write("## 4. Outlier Detection\n")
             f.write(f"Could not calculate debt ratios. Columns found: Vencida={d_vencida}, Total={d_total}\n")

    print(f"Report saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_report()
