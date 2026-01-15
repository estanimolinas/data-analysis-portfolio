import pandas as pd

INPUT = "dds_exports_countries_only.csv"   # tu dataset país-only
OUT_COUNTRY_YEAR = "pbi_country_year.csv"
OUT_COUNTRY_GROWTH = "pbi_country_growth.csv"
OUT_GLOBAL_YEAR = "pbi_global_year.csv"

print("loading dataset...")
df = pd.read_csv(INPUT)

# --- sanity checks básicos ---
required_cols = {"country", "year", "exports_digital_services_usd_million"}
missing = required_cols - set(df.columns)
if missing:
    raise ValueError(f"missing columns in {INPUT}: {missing}")

# --- 1) country_year (hecho, pero ordenado y listo para Power BI) ---
country_year = (
    df[["country", "year", "exports_digital_services_usd_million"]]
    .copy()
    .sort_values(["country", "year"])
)

country_year.to_csv(OUT_COUNTRY_YEAR, index=False)
print(f"saved: {OUT_COUNTRY_YEAR} | shape={country_year.shape}")

# --- 2) country_growth (2005 vs 2024 + growth factor) ---
pvt = country_year.pivot_table(
    index="country",
    columns="year",
    values="exports_digital_services_usd_million",
    aggfunc="sum"
)

# asegurar columnas clave si existen en el dataset
for y in [2005, 2024]:
    if y not in pvt.columns:
        raise ValueError(f"year {y} not found in dataset. available years: {sorted(pvt.columns.tolist())}")

growth = pvt[[2005, 2024]].rename(columns={2005: "exports_2005", 2024: "exports_2024"}).reset_index()

# growth factor: exports_2024 / exports_2005
# si exports_2005 es 0, dejamos NaN para evitar infinito
growth["growth_2005_2024"] = growth["exports_2024"] / growth["exports_2005"].replace({0: pd.NA})

growth = growth.sort_values("exports_2024", ascending=False)
growth.to_csv(OUT_COUNTRY_GROWTH, index=False)
print(f"saved: {OUT_COUNTRY_GROWTH} | shape={growth.shape}")

# --- 3) global_year (serie global agregada desde países) ---
global_year = (
    country_year.groupby("year", as_index=False)["exports_digital_services_usd_million"]
    .sum()
    .rename(columns={"exports_digital_services_usd_million": "global_exports_digital_services_usd_million"})
    .sort_values("year")
)

global_year.to_csv(OUT_GLOBAL_YEAR, index=False)
print(f"saved: {OUT_GLOBAL_YEAR} | shape={global_year.shape}")

print("done.")
