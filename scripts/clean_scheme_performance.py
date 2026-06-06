import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Numeric columns to validate
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

# Convert to numeric
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check missing after conversion
print("Missing after numeric conversion:")
print(df[numeric_cols].isnull().sum())

# Expense ratio validation
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratio Records:")
print(len(invalid_expense))

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("\nScheme Performance Cleaned Successfully!")