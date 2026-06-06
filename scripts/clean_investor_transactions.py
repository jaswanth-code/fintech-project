import pandas as pd

# Load data
df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Convert date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Validate amount > 0
invalid_amounts = df[df["amount_inr"] <= 0]

print("Invalid Amount Records:", len(invalid_amounts))

# Check transaction types
print("\nTransaction Types:")
print(df["transaction_type"].unique())

# Check KYC Status values
print("\nKYC Status Values:")
print(df["kyc_status"].unique())

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print("\nInvestor Transactions Cleaned Successfully!")