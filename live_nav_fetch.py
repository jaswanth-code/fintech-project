import requests
import pandas as pd
import os

# Create folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# HDFC Top 100 Direct Plan Growth
scheme_code = 125497

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    print("Scheme Name:")
    print(data["meta"]["scheme_name"])

    print("\nFund House:")
    print(data["meta"]["fund_house"])

    print("\nScheme Code:")
    print(data["meta"]["scheme_code"])

    # Convert NAV history to DataFrame
    nav_df = pd.DataFrame(data["data"])

    # Save CSV
    nav_df.to_csv(
        "data/raw/hdfc_top100_nav.csv",
        index=False
    )

    print("\nNAV History Saved Successfully!")

    print("\nFirst 5 Rows:")
    print(nav_df.head())

else:
    print("Failed to fetch data")
    print("Status Code:", response.status_code)