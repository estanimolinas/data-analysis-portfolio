import pandas as pd

print("starting script")

df = pd.read_csv("DDS_bulk_download.csv", encoding="latin1")

print("\n=== CSV LOADED ===")
print("shape:", df.shape)

print("\n=== COLUMNS ===")
print(df.columns.tolist())

print("\n=== DTYPES ===")
print(df.dtypes)

print("\n=== YEAR RANGE ===")
print(df["YEAR"].min(), df["YEAR"].max())

print("\n=== UNIQUE VALUES (KEY FIELDS) ===")
print("REPORTERS:", df["REPORTER_NAME"].nunique())
print("PARTNERS:", df["PARTNER"].nunique())
print("INDICATORS:", df["INDICATOR"].unique())
print("MODES:", df["MODE"].unique())
print("FLOW:", df["FLOW"].unique())

print("\n=== FIRST ROWS ===")
print(df.head(5))

