-- 1. Total Funds
SELECT COUNT(*) AS total_funds
FROM "01_fund_master";

-- 2. Funds by Category
SELECT category, COUNT(*) AS total_funds
FROM "01_fund_master"
GROUP BY category;

-- 3. Funds by Risk Category
SELECT risk_category, COUNT(*) AS total_funds
FROM "01_fund_master"
GROUP BY risk_category;

-- 4. Top Fund Houses by Number of Schemes
SELECT fund_house, COUNT(*) AS total_schemes
FROM "01_fund_master"
GROUP BY fund_house
ORDER BY total_schemes DESC;

-- 5. Average NAV
SELECT AVG(nav) AS average_nav
FROM "02_nav_history";

-- 6. Highest NAV Fund
SELECT amfi_code, MAX(nav) AS highest_nav
FROM "02_nav_history";

-- 7. Transactions by State
SELECT state, COUNT(*) AS total_transactions
FROM "08_investor_transactions"
GROUP BY state;

-- 8. Transaction Type Distribution
SELECT transaction_type, COUNT(*) AS total
FROM "08_investor_transactions"
GROUP BY transaction_type;

-- 9. KYC Status Distribution
SELECT kyc_status, COUNT(*) AS total
FROM "08_investor_transactions"
GROUP BY kyc_status;

-- 10. Average Expense Ratio
SELECT AVG(expense_ratio_pct) AS avg_expense_ratio
FROM "07_scheme_performance";