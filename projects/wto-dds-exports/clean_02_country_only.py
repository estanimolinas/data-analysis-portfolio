import pandas as pd

print("loading clean dataset...")

df = pd.read_csv("dds_exports_clean.csv")

print("initial shape:", df.shape)

# lista explícita de agregados conocidos
aggregates = [
    "World",
    "Europe",
    "European Union",
    "Africa",
    "Asia",
    "Americas",
    "Oceania",
    "Middle East",
    "North America",
    "South America",
    "Central America",
    "Caribbean",
    "Eastern Europe",
    "Western Europe",
    "Southern Europe",
    "Northern Europe"
]

# filtrar solo países
df_countries = df[~df["country"].isin(aggregates)].copy()

print("after removing aggregates:", df_countries.shape)

# chequeos rápidos
print("unique countries:", df_countries["country"].nunique())
print("year range:", df_countries["year"].min(), df_countries["year"].max())

# guardar dataset final
output_file = "dds_exports_countries_only.csv"
df_countries.to_csv(output_file, index=False)

print(f"saved clean country-only dataset to {output_file}")
print("done")
