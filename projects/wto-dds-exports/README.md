# WTO Digitally Delivered Services (DDS) – Exports (2005–2024)

Source dataset: WTO Digitally Delivered Services (DDS) trade dataset  
https://data.wto.org/en/dataset/dideliveredservices

## Project purpose
This project builds a clean, country-level dataset of digitally delivered services exports to enable
comparative analysis and dashboarding across countries and time (2005–2024).

The main goal is to transform a raw, aggregate-heavy WTO dataset into analysis-ready tables suitable
for BI tools and international trade analysis.

## What this project does
- Loads raw WTO DDS dataset
- Filters exports only (FLOW = X)
- Keeps total digitally delivered services (DDS)
- Performs basic data validation and sanity checks
- Removes aggregates (regions, income groups, totals)
- Produces country-only datasets
- Generates descriptive statistics and BI-ready tables

## Pipeline scripts
- `eda_01_overview.py` – initial exploration and structure checks
- `clean_01_base_dataset.py` – base filtering and normalization
- `eda_03_validation.py` – consistency and coverage validation
- `clean_03_remove_aggregates.py` – keeps countries only
- `eda_04_descriptive_stats.py` – summary stats and growth indicators
- `export_for_powerbi.py` – exports BI-friendly tables

## Outputs
Core dataset:
- `dds_exports_countries_only.csv` – clean country-level DDS exports (2005–2024)

BI-ready tables (designed for Power BI or similar tools):
- `bi_global_year.csv` – global DDS exports by year
- `bi_country_year.csv` – country-year DDS exports
- `bi_country_growth.csv` – growth rates and trends by country

## How to run
```bash
python3 eda_01_overview.py
python3 clean_01_base_dataset.py
python3 eda_03_validation.py
python3 clean_03_remove_aggregates.py
python3 eda_04_descriptive_stats.py
python3 export_for_powerbi.py
