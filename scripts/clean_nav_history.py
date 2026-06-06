import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by fund and date
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Check missing values
print("Missing values:")
print(df.isnull().sum())

# Forward fill NAV within each fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Validate NAV > 0
invalid_nav = df[df["nav"] <= 0]

print("\nInvalid NAV records:", len(invalid_nav))

# Save cleaned file
df.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

print("\nCleaned NAV history saved successfully!")