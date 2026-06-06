# Data Dictionary

## 02_nav_history_cleaned.csv

| Column Name | Data Type | Description             |
| ----------- | --------- | ----------------------- |
| amfi_code   | Integer   | Unique AMFI scheme code |
| date        | Date      | NAV recorded date       |
| nav         | Float     | Net Asset Value         |

## 07_scheme_performance_cleaned.csv

| Column Name       | Data Type | Description              |
| ----------------- | --------- | ------------------------ |
| amfi_code         | Integer   | Unique AMFI scheme code  |
| scheme_name       | Text      | Mutual fund scheme name  |
| return_1yr_pct    | Float     | 1-year return percentage |
| expense_ratio_pct | Float     | Expense ratio percentage |
| risk_grade        | Text      | Fund risk category       |

## 08_investor_transactions_cleaned.csv

| Column Name      | Data Type | Description               |
| ---------------- | --------- | ------------------------- |
| investor_id      | Text      | Unique investor ID        |
| transaction_date | Date      | Transaction date          |
| transaction_type | Text      | SIP, Lumpsum, Redemption  |
| amount_inr       | Float     | Transaction amount in INR |
| kyc_status       | Text      | KYC verification status   |
