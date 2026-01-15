import pandas as pd

INPUT = "dds_exports_clean.csv"                 # dataset limpio base (incluye agregados)
OUTPUT = "dds_exports_countries_only.csv"       # salida final solo países

print("loading dataset...")
df = pd.read_csv(INPUT)

print("initial shape:", df.shape)
print("unique entities:", df["country"].nunique())

# Regla 1: partner=World ya está implícito del dataset base, pero acá filtramos "solo países"
# Regla 2: descartamos agregados típicos:
# - filas cuyo nombre contenga claves de agregación
# - y una lista explícita para casos comunes
patterns = [
    r"\bWorld\b",
    r"\bEurope\b",
    r"\bEuropean Union\b",
    r"\bAsia\b",
    r"\bAfrica\b",
    r"\bOceania\b",
    r"\bAmericas\b",
    r"\bCaribbean\b",
    r"\bCentral America\b",
    r"\bSouth America\b",
    r"\bNorth America\b",
    r"\bMiddle East\b",
    r"\bEuro Area\b",
    r"\bHigh income\b",
    r"\bUpper middle income\b",
    r"\bLower middle income\b",
    r"\bLow income\b",
    r"\bLeast developed\b",
    r"\bDeveloping\b",
    r"\bDeveloped\b",
    r"\bSub-Saharan\b",
]

explicit_drop = {
    "World",
    "Europe",
    "European Union",
    "South and Central America and the Caribbean",
}

mask_pattern = df["country"].str.contains("|".join(patterns), case=False, regex=True, na=False)
mask_explicit = df["country"].isin(explicit_drop)

df_countries = df.loc[~(mask_pattern | mask_explicit)].copy()

print("after removing aggregates:", df_countries.shape)
print("unique countries:", df_countries["country"].nunique())
print("year range:", df_countries["year"].min(), df_countries["year"].max())

# Validación mínima: 20 años por país (2005–2024) debería ser 20
years_per_country = df_countries.groupby("country")["year"].nunique()
print("min years per country:", years_per_country.min())
print("max years per country:", years_per_country.max())

# Guardado
df_countries.to_csv(OUTPUT, index=False)
print(f"saved to {OUTPUT}")
print("done")
