## Outputs

This project produces multiple analysis-ready datasets derived from WTO DDS exports data (2005–2024).

### Core dataset
- `dds_exports_countries_only.csv`  
  Clean country-level DDS exports data (no aggregates).

### BI-ready tables
- `bi_country_year.csv`  
  Country-year DDS exports.
- `bi_country_growth.csv`  
  Growth rates and trends by country.
- `bi_global_year.csv`  
  Global DDS exports by year.

### Final unified dataset (recommended)
- `dds_bi_country_year_final.csv`  

This is the main output of the project.  
It combines:
- country-level DDS exports (USD)
- global DDS exports (USD, million)
- country growth indicators  

Designed for direct use in BI tools (Power BI Service, Tableau, Looker, etc.).

---

## How to run

```bash
# 1. Install dependencies
python3 -m pip install pandas

# 2. Generate BI base tables
python3 export_for_powerbi.py

# 3. Generate final unified dataset
python3 make_final_bi_dataset.py
