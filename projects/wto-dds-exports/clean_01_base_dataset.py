import pandas as pd

print("loading data")

df = pd.read_csv("DDS_bulk_download.csv", encoding="latin1")

print("filtering exports + total DDS")

df_clean = df[
    (df["FLOW"] == "X") &
    (df["INDICATOR"] == "DDS")
].copy()

df_clean = df_clean[[
    "REPORTER_NAME",
    "YEAR",
    "VALUE"
]]

df_clean = df_clean.rename(columns={
    "REPORTER_NAME": "country",
    "YEAR": "year",
    "VALUE": "exports_digital_services_usd_million"
})

print("clean dataset shape:", df_clean.shape)

print("\npreview:")
print(df_clean.head())

print("\nsaving clean dataset")

df_clean.to_csv("dds_exports_clean.csv", index=False)

print("done")
