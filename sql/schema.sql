-- Fund Master Table
CREATE TABLE 01_fund_master (
    scheme_code INTEGER,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT,
    risk_category TEXT
);

-- NAV History Table
CREATE TABLE 02_nav_history (
    scheme_code INTEGER,
    nav_date DATE,
    nav_value REAL
);

-- AUM Table
CREATE TABLE 03_aum_by_fund_house (
    fund_house TEXT,
    quarter TEXT,
    aum_crore REAL
);

-- SIP Inflows Table
CREATE TABLE 04_monthly_sip_inflows (
    month_year TEXT,
    sip_inflow_crore REAL,
    active_accounts INTEGER
);

-- Investor Transactions Table
CREATE TABLE 08_investor_transactions (
    investor_id INTEGER,
    scheme_code INTEGER,
    transaction_type TEXT,
    amount REAL
);