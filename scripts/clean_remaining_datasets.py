import pandas as pd
import os

files = [
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    print(f"\nProcessing {file}")

    df = pd.read_csv(f"data/raw/{file}")

    print("Missing Values:")
    print(df.isnull().sum().sum())

    print("Duplicate Rows:")
    print(df.duplicated().sum())

    df = df.drop_duplicates()

    output_file = file.replace(".csv", "_cleaned.csv")

    df.to_csv(
        f"data/processed/{output_file}",
        index=False
    )

    print(f"{output_file} saved successfully")