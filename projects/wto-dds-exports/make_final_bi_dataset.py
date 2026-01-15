from pathlib import Path
import pandas as pd


def main():
    root = Path(__file__).resolve().parent

    # Load source datasets
    df_country_year = pd.read_csv(root / "bi_country_year.csv")
    df_country_growth = pd.read_csv(root / "bi_country_growth.csv")
    df_global_year = pd.read_csv(root / "bi_global_year.csv")

    # Rename columns to be explicit and BI-friendly (keeping same data)
    df_country_year = df_country_year.rename(columns={
        "exports_value": "country_dds_exports_usd"
    })

    df_global_year = df_global_year.rename(columns={
        "global_exports_digital_services_usd_million": "global_dds_exports_usd_million"
    })

    df_country_growth = df_country_growth.rename(columns={
        "exports_2005": "country_dds_exports_2005_usd",
        "exports_2024": "country_dds_exports_2024_usd",
        "growth_2005_2024": "country_dds_exports_growth_2005_2024"
    })

    # Merge into one final table (country-year grain)
    df_final = (
        df_country_year
        .merge(
            df_global_year[["year", "global_dds_exports_usd_million"]],
            on="year",
            how="left"
        )
        .merge(
            df_country_growth[[
                "country",
                "country_dds_exports_2005_usd",
                "country_dds_exports_2024_usd",
                "country_dds_exports_growth_2005_2024"
            ]],
            on="country",
            how="left"
        )
        .sort_values(["year", "country"])
        .reset_index(drop=True)
    )

    out = root / "dds_bi_country_year_final.csv"
    df_final.to_csv(out, index=False)

    print(f"saved: {out.name} | shape={df_final.shape}")


if __name__ == "__main__":
    main()
