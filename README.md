# Vertical Integration and Financial Distress in Portuguese Public Hospitals

## Replication Package

**Paper:** "Vertical Integration and Financial Distress in Portuguese Public Hospitals: Methodological Framework and Preliminary Evidence from the 2024 ULS Reform"

**Author:** Daniel Ferreira Polonia
**Affiliation:** Department of Economics, Management, Industrial Engineering and Tourism (DEGEIT), University of Aveiro, Portugal
**Contact:** dpolonia@ua.pt
**Submitted to:** Health Economics (Wiley)

---

## Abstract

This study establishes a methodological framework for evaluating Portugal's 2024 universal healthcare integration reform and provides preliminary evidence on short-term financial trajectories. We compare 31 newly-integrated ULS entities against 8 pre-existing ULS (integrated 1999-2012) using difference-in-differences, synthetic control, and triple-difference designs with quarterly panel data from 2014-2025 (n = 1,092 entity-quarters).

---

## Repository Structure

```
cfe-hospital-distress/
├── paper/                          # Final paper documents
│   ├── CFE_Empirical_Work_V6_HealthEconomics.pdf   # Published PDF
│   ├── CFE_Empirical_Work_V6_HealthEconomics.tex   # LaTeX source
│   ├── CFE_Empirical_Work_V6_HealthEconomics.md    # Markdown source
│   └── CFE_Empirical_Work_V6_HealthEconomics.docx  # Word version
│
├── scripts/                        # Python analysis scripts
│   ├── DATA PIPELINE
│   │   ├── initialize_db.py        # Database initialization
│   │   ├── ingest_sns.py           # SNS Transparency Portal ingestion
│   │   ├── ingest_impic.py         # IMPIC procurement data ingestion
│   │   ├── ingest_ine.py           # INE macroeconomic indicators
│   │   ├── entity_resolution.py    # Fuzzy matching for entity NIFs
│   │   ├── enrich_entities.py      # NUTS II region mapping
│   │   ├── create_panel.py         # Panel dataset construction
│   │   └── validate_data.py        # Data quality validation
│   │
│   ├── ANALYSIS
│   │   ├── analysis_descriptive.py     # Descriptive statistics
│   │   ├── run_regression.py           # Main DiD regression (PanelOLS)
│   │   ├── run_enhanced_regression.py  # Robustness checks
│   │   ├── run_corrected_analysis.py   # Corrected specifications
│   │   ├── run_all_improvements.py     # Full analysis pipeline
│   │   └── assess_spa_relevance.py     # SPA vs EPE analysis
│   │
│   └── UTILITIES
│       ├── search_scopus.py            # Scopus literature search
│       ├── search_health_economics.py  # Health economics search
│       ├── evaluate_paper.py           # Paper evaluation metrics
│       └── create_docx.py              # Document generation
│
├── data/
│   ├── raw/impic/                  # Raw IMPIC procurement contracts (2012-2025)
│   │   └── contratos20XX.xlsx      # Annual contract files
│   ├── processed/                  # Cleaned dimension/fact tables
│   │   ├── dim_entities.parquet    # Entity dimension table
│   │   ├── dim_macro.parquet       # Macroeconomic indicators
│   │   ├── fact_debt_monthly.parquet       # Monthly debt data
│   │   ├── fact_financials_monthly.parquet # Financial statements
│   │   ├── fact_hr_monthly.parquet         # Human resources data
│   │   └── fact_procurement_contracts.parquet # Procurement contracts
│   ├── analytical/                 # Final analysis dataset
│   │   └── analytical_panel.parquet # Panel dataset (n=1,092)
│   ├── hospital_to_uls_mapping_corrected.csv  # Historical entity mappings
│   ├── nifs_saude.xlsx             # Master entity NIF list
│   └── TC NUTS 2013_ NUTS 2024 a município.xlsx # NUTS regional mapping
│
├── results/                        # Analysis outputs
│   ├── regression_results.txt      # Main regression output
│   ├── descriptive_report.md       # Descriptive statistics
│   ├── enhanced_regression_results.md  # Robustness results
│   ├── corrected_did_analysis.md   # Corrected DiD results
│   ├── did_parallel_trends.png     # Pre-trends visualization
│   ├── pretrend_visualization.png  # Parallel trends check
│   ├── health_economics_similar_articles.md # Literature comparison
│   ├── scopus_literature.md        # Scopus search results
│   └── *.json                      # Evaluation metrics
│
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git exclusions
└── README.md                       # This file
```

---

## Data Sources

| Source | Description | Access |
|--------|-------------|--------|
| **SNS Transparency Portal** | Financial statements, HR data, debt | `transparencia.sns.gov.pt/api/` |
| **IMPIC (Base)** | Public procurement contracts | `dados.gov.pt` |
| **INE** | Regional GDP, unemployment, demographics | `ine.pt/api/` |
| **ACSS** | Entity master list (NIFs) | Manual download |

---

## Replication Instructions

### 1. Environment Setup

```bash
# Clone repository
git clone https://github.com/dpolonia/cfe-hospital-distress.git
cd cfe-hospital-distress

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Keys (Optional)

Create a `.env` file for literature search functionality:
```env
SCOPUS_API_KEY=your_scopus_key
GEMINI_API_KEY=your_gemini_key
```

### 3. Run Analysis

**Option A: Use Pre-processed Data (Recommended for Replication)**
```bash
cd scripts
python run_regression.py
# Results saved to results/regression_results.txt
```

**Option B: Full Pipeline from Raw Data**
```bash
cd scripts
python initialize_db.py
python ingest_sns.py
python ingest_impic.py
python ingest_ine.py
python entity_resolution.py
python enrich_entities.py
python create_panel.py
python validate_data.py
python analysis_descriptive.py
python run_regression.py
python run_enhanced_regression.py
```

---

## Key Variables

### Primary Outcome
- **Overdue Debt Ratio**: Supplier payments >90 days past due / Total supplier debt

### Treatment Variables
- **NewULS**: Indicator for entities integrated in January 2024 (vs. pre-existing ULS 1999-2012)
- **Post**: Indicator for post-reform period (Q1 2024 onwards)

### Controls
- Log staff count
- Region fixed effects (NUTS II)
- Time fixed effects (quarterly)

---

## Main Results

| Specification | DiD Estimate | 95% CI | p-value |
|--------------|--------------|--------|---------|
| Simple DiD | +6.2pp | [-9.3, +21.7] | 0.433 |
| + Time FE | +4.8pp | [-12.1, +21.7] | 0.578 |
| + Controls | +5.1pp | [-11.4, +21.6] | 0.546 |
| Wild Bootstrap | +6.2pp | — | 0.456 |

**Key Finding:** Pre-existing ULS exhibited 18.5pp higher baseline distress (p = 0.006), suggesting early adoption targeted structurally disadvantaged regions.

---

## Requirements

```
pandas>=2.0
numpy>=1.24
pyarrow>=14.0
requests>=2.31
python-dotenv>=1.0
rapidfuzz>=3.5
linearmodels>=5.3
statsmodels>=0.14
tabulate>=0.9
```

---

## Citation

```bibtex
@article{polonia2025uls,
  author = {Polonia, Daniel Ferreira},
  title = {Vertical Integration and Financial Distress in Portuguese Public Hospitals:
           Methodological Framework and Preliminary Evidence from the 2024 ULS Reform},
  journal = {Health Economics},
  year = {2025},
  note = {Submitted}
}
```

---

## License

MIT License - Academic use encouraged with citation.

---

## AI Disclosure

AI tools (Claude, Gemini) assisted with:
- Data pipeline development
- Literature organization
- Draft structuring

All analytical decisions and interpretations were made by the author.

---

## Contact

For questions about this replication package:
**Daniel Ferreira Polonia**
dpolonia@ua.pt
University of Aveiro, Portugal
