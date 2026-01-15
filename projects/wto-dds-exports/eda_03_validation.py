import pandas as pd

print("loading clean dataset...")
df = pd.read_csv("dds_exports_clean.csv")

print("\n=== SHAPE ===")
print(df.shape)

print("\n=== COLUMNS ===")
print(df.columns.tolist())

print("\n=== DTYPES ===")
print(df.dtypes)

# Basic sanity checks
print("\n=== BASIC CHECKS ===")
print("missing values:\n", df.isna().sum())
print("duplicate rows:", df.duplicated().sum())

# Year coverage
print("\n=== YEAR COVERAGE ===")
print("year min/max:", df["year"].min(), df["year"].max())
years_per_country = df.groupby("country")["year"].nunique().sort_values()
print("countries:", df["country"].nunique())
print("min years per country:", years_per_country.min())
print("max years per country:", years_per_country.max())

print("\nCountries with <= 5 years of data:")
print(years_per_country[years_per_country <= 5].head(30))

# Value checks
col = "exports_digital_services_usd_million"
print("\n=== VALUE CHECKS ===")
print("value min/max:", df[col].min(), df[col].max())
print("negative values:", (df[col] < 0).sum())
print("zero values:", (df[col] == 0).sum())

print("\n=== DESCRIBE (VALUE) ===")
print(df[col].describe(percentiles=[0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99]))

# Outliers preview
print("\n=== TOP 20 VALUES (COUNTRY-YEAR) ===")
print(df.sort_values(col, ascending=False).head(20))

print("\n=== BOTTOM 20 VALUES (COUNTRY-YEAR) ===")
print(df.sort_values(col, ascending=True).head(20))

# Check for missing years inside each country series (gaps)
print("\n=== YEAR GAPS CHECK (per country) ===")
gap_examples = []
for c, g in df.groupby("country"):
    yrs = sorted(g["year"].unique())
    if not yrs:
        continue
    full = set(range(min(yrs), max(yrs) + 1))
    missing = sorted(list(full - set(yrs)))
    if missing:
        gap_examples.append((c, yrs[0], yrs[-1], len(missing), missing[:10]))

gap_examples = sorted(gap_examples, key=lambda x: x[3], reverse=True)

if gap_examples:
    print("countries with gaps:", len(gap_examples))
    print("top 20 gap examples:")
    for row in gap_examples[:20]:
        c, y0, y1, nmiss, miss_preview = row
        print(f"- {c}: {y0}-{y1} missing {nmiss} years (first missing: {miss_preview})")
else:
    print("no gaps found within country ranges.")

print("\nvalidation complete.")
