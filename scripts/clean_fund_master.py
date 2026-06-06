import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

# Convert launch date
df["launch_date"] = pd.to_datetime(df["launch_date"])

# Remove duplicates
df = df.drop_duplicates()

# Validate expense ratio
invalid_expense = df[df["expense_ratio_pct"] < 0]

print("Invalid Expense Ratio Records:", len(invalid_expense))

# Validate minimum investment amounts
invalid_sip = df[df["min_sip_amount"] <= 0]
invalid_lumpsum = df[df["min_lumpsum_amount"] <= 0]

print("Invalid SIP Amount Records:", len(invalid_sip))
print("Invalid Lumpsum Amount Records:", len(invalid_lumpsum))

# Save cleaned file
df.to_csv(
    "data/processed/01_fund_master_cleaned.csv",
    index=False
)

print("\nFund Master Cleaned Successfully!")