import pandas as pd

print("loading country-only dataset...")

df = pd.read_csv("dds_exports_countries_only.csv")

print("shape:", df.shape)
print("countries:", df["country"].nunique())
print("years:", df["year"].min(), "-", df["year"].max())

# último año disponible
latest_year = df["year"].max()
df_latest = df[df["year"] == latest_year]

print(f"\n=== TOP 20 COUNTRIES BY DIGITAL SERVICES EXPORTS ({latest_year}) ===")
top20 = (
    df_latest
    .sort_values("exports_digital_services_usd_million", ascending=False)
    .head(20)
)

print(top20[["country", "exports_digital_services_usd_million"]])

# concentración
total_exports = df_latest["exports_digital_services_usd_million"].sum()
top10_share = (
    df_latest
    .sort_values("exports_digital_services_usd_million", ascending=False)
    .head(10)["exports_digital_services_usd_million"]
    .sum()
) / total_exports * 100

print(f"\nTop 10 countries share of global exports (%): {top10_share:.2f}")

# crecimiento 2005–2024
df_growth = (
    df.pivot(index="country", columns="year", values="exports_digital_services_usd_million")
    .dropna()
)

df_growth["growth_2005_2024"] = (
    (df_growth[2024] - df_growth[2005]) / df_growth[2005]
)

df_growth = df_growth.replace([float("inf"), -float("inf")], pd.NA).dropna()

print("\n=== TOP 10 COUNTRIES BY GROWTH (2005–2024) ===")
print(
    df_growth
    .sort_values("growth_2005_2024", ascending=False)
    .head(10)[["growth_2005_2024"]]
)

print("\nEDA descriptive stats complete.")
