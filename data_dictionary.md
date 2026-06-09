# Data Dictionary – Mutual Fund Analytics Project

## 1. Fund Master (`01_fund_master_cleaned.csv`)

| Column Name        | Description                                         |
| ------------------ | --------------------------------------------------- |
| amfi_code          | Unique AMFI code identifying the mutual fund scheme |
| fund_house         | Name of the asset management company                |
| scheme_name        | Name of the mutual fund scheme                      |
| category           | Fund category (Equity, Debt, Hybrid, etc.)          |
| sub_category       | Detailed category classification                    |
| plan               | Direct or Regular plan                              |
| launch_date        | Scheme launch date                                  |
| benchmark          | Benchmark index used for comparison                 |
| expense_ratio_pct  | Annual expense ratio (%)                            |
| exit_load_pct      | Exit load charged on redemption                     |
| min_sip_amount     | Minimum SIP investment amount                       |
| min_lumpsum_amount | Minimum lump sum investment amount                  |
| fund_manager       | Fund manager name                                   |
| risk_category      | Risk classification                                 |
| sebi_category_code | SEBI category identifier                            |

---

## 2. AUM by Fund House (`03_aum_by_fund_house_cleaned.csv`)

| Column Name    | Description                            |
| -------------- | -------------------------------------- |
| date           | Reporting date                         |
| fund_house     | Fund house name                        |
| aum_crore      | Assets Under Management (₹ Crore)      |
| aum_lakh_crore | Assets Under Management (₹ Lakh Crore) |
| num_schemes    | Number of schemes managed              |

---

## 3. Monthly SIP Inflows (`04_monthly_sip_inflows_cleaned.csv`)

| Column Name               | Description                                |
| ------------------------- | ------------------------------------------ |
| month                     | Month-Year                                 |
| sip_inflow_crore          | Monthly SIP inflow (₹ Crore)               |
| active_sip_accounts_crore | Active SIP accounts (Crore)                |
| new_sip_accounts_lakh     | New SIP accounts opened (Lakh)             |
| sip_aum_lakh_crore        | SIP Assets Under Management (₹ Lakh Crore) |
| yoy_growth_pct            | Year-over-Year growth percentage           |

---

## 4. Industry Folio Count (`06_industry_folio_count_cleaned.csv`)

| Column Name         | Description                   |
| ------------------- | ----------------------------- |
| month               | Reporting month               |
| total_folios_crore  | Total folios (Crore)          |
| equity_folios_crore | Equity folios (Crore)         |
| debt_folios_crore   | Debt folios (Crore)           |
| hybrid_folios_crore | Hybrid folios (Crore)         |
| others_folios_crore | Other category folios (Crore) |

---

## 5. Investor Transactions (`08_investor_transactions_cleaned.csv`)

| Column Name        | Description                   |
| ------------------ | ----------------------------- |
| investor_id        | Unique investor identifier    |
| transaction_date   | Transaction date              |
| amfi_code          | Fund scheme code              |
| transaction_type   | Purchase / Redemption         |
| amount_inr         | Transaction amount (₹)        |
| state              | Investor state                |
| city               | Investor city                 |
| city_tier          | Tier classification (T30/B30) |
| age_group          | Investor age group            |
| gender             | Investor gender               |
| annual_income_lakh | Annual income (₹ Lakh)        |
| payment_mode       | Payment method                |
| kyc_status         | KYC verification status       |

---

## 6. Portfolio Holdings (`09_portfolio_holdings_cleaned.csv`)

| Column Name       | Description              |
| ----------------- | ------------------------ |
| amfi_code         | Fund scheme code         |
| stock_symbol      | Stock ticker symbol      |
| stock_name        | Company name             |
| sector            | Industry sector          |
| weight_pct        | Portfolio weight (%)     |
| market_value_cr   | Market value (₹ Crore)   |
| current_price_inr | Current stock price      |
| portfolio_date    | Portfolio reporting date |

---

## 7. Fund Performance Metrics (`fund_performance_metrics.csv`)

| Column Name        | Description                   |
| ------------------ | ----------------------------- |
| amfi_code          | Fund scheme code              |
| scheme_name        | Scheme name                   |
| fund_house         | Fund house                    |
| category           | Fund category                 |
| plan               | Plan type                     |
| return_1yr_pct     | 1-Year return (%)             |
| return_3yr_pct     | 3-Year return (%)             |
| return_5yr_pct     | 5-Year return (%)             |
| benchmark_3yr_pct  | Benchmark return (%)          |
| alpha              | Alpha                         |
| beta               | Beta                          |
| sharpe_ratio       | Sharpe Ratio                  |
| sortino_ratio      | Sortino Ratio                 |
| std_dev_ann_pct    | Annualized standard deviation |
| max_drawdown_pct   | Maximum drawdown (%)          |
| aum_crore          | Assets Under Management       |
| expense_ratio_pct  | Expense ratio (%)             |
| morningstar_rating | Morningstar rating            |
| risk_grade         | Risk grade                    |

---

## 8. Derived Analytics Files

### fund_scorecard.csv

| Column Name | Description                         |
| ----------- | ----------------------------------- |
| amfi_code   | Fund scheme code                    |
| scheme_name | Scheme name                         |
| fund_score  | Composite performance score (0–100) |

### alpha_beta.csv

| Column Name | Description      |
| ----------- | ---------------- |
| amfi_code   | Fund scheme code |
| alpha       | Fund alpha       |
| beta        | Fund beta        |

### sharpe_results.csv

| Column Name  | Description                 |
| ------------ | --------------------------- |
| amfi_code    | Fund scheme code            |
| sharpe_ratio | Risk-adjusted return metric |

### max_drawdown.csv

| Column Name  | Description                        |
| ------------ | ---------------------------------- |
| amfi_code    | Fund scheme code                   |
| max_drawdown | Maximum observed portfolio decline |

### tracking_error.csv

| Column Name    | Description                          |
| -------------- | ------------------------------------ |
| amfi_code      | Fund scheme code                     |
| tracking_error | Deviation from benchmark performance |
