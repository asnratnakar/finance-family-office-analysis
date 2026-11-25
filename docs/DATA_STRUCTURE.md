# Data Folder Structure

**Status:** migration reference, not a guarantee of every current file
**Updated:** 25 November 2026

> **Authority:** `DATA_CONTRACT.md` governs new imports and ledger storage. The legacy structure below documents paths used by the current app and must not be copied into the new repo as an arbitrary design. Real data belongs outside version control. Only synthetic fixtures under `data/samples/` are commit-safe.

## Overview
The data folder has been reorganized into logical subfolders by asset class for better organization and scalability.

## Current Structure

```
data/
├── .gitkeep
├── api_keys.keys                          # API authentication keys
│
├── metals/                                # Precious metals & bullion
│   ├── metals_transactionHistory.csv     # Your metal purchases & sales history
│   ├── metals_spotPrice.csv              # Current spot prices (Gold, Silver)
│   ├── metals_gold_purchaseAdvisory.csv  # Gold procurement options & pricing
│   └── metals_silver_purchaseAdvisory.csv # Silver procurement options & pricing
│
├── portfolio/                             # Stock & securities portfolio
│   └── sample_portfolio.csv              # Your stock holdings by sector
│
├── banking/                               # Bank accounts & deposits
│   ├── checking_accounts.csv             # Checking account details (to be created)
│   ├── savings_accounts.csv              # Savings account details (to be created)
│   ├── cd_accounts.csv                   # CD account details (to be created)
│   └── interest_rates_history.csv        # Historical interest rates (to be created)
│
├── real_estate/                           # Property & real estate
│   ├── properties.csv                    # Property listings & valuations
│   ├── mortgages.csv                     # Mortgage details
│   └── property_valuations.csv           # Property value history
│
├── retirement/                            # Retirement accounts
│   ├── 401k_accounts.csv                 # 401(k) account details
│   ├── ira_accounts.csv                  # IRA account details
│   └── retirement_projections.csv        # Retirement planning projections
│
├── loans/                                 # Loan accounts
│   ├── personal_loans.csv                # Personal loan details
│   ├── student_loans.csv                 # Student loan details
│   └── loan_payments.csv                 # Loan payment history
│
├── insurance/                             # Insurance policies
│   ├── life_insurance.csv                # Life insurance policies
│   ├── health_insurance.csv              # Health insurance details
│   └── property_insurance.csv            # Property insurance details
│
├── forex/                                 # Foreign exchange
│   └── currency_pairs.csv                # Currency pair holdings
│
├── commodities/                           # Commodities
│   └── commodity_holdings.csv            # Commodity investments
│
└── knowledge_base/                        # Educational resources
    └── articles.csv                      # Knowledge base articles
```

## File Path Updates Made

### 5_Metals.py
All file paths have been updated from root `data/` to `data/metals/`:

- `data/metals_transactionHistory.csv` → `data/metals/metals_transactionHistory.csv`
- `data/metals_spotPrice.csv` → `data/metals/metals_spotPrice.csv`
- `data/metals_gold_purchaseAdvisory.csv` → `data/metals/metals_gold_purchaseAdvisory.csv`
- `data/metals_silver_purchaseAdvisory.csv` → `data/metals/metals_silver_purchaseAdvisory.csv`

## Future Updates Needed

When creating new pages, remember to update file paths:

### Banking Page (1_Bank_Accounts.py)
```python
Path('data/banking/checking_accounts.csv')
Path('data/banking/savings_accounts.csv')
Path('data/banking/cd_accounts.csv')
```

### Market Investments Page (4_Market_Investments.py)
```python
Path('data/portfolio/sample_portfolio.csv')
```

### Real Estate Page (2_RealEstate.py)
```python
Path('data/real_estate/properties.csv')
```

And so on for other pages...

## Benefits

✅ **Organization** - Related data grouped by asset class
✅ **Scalability** - Easy to add new files within each category
✅ **Maintainability** - Clear structure for finding specific data
✅ **Version Control** - Easier to track changes within categories
✅ **Documentation** - Self-documenting folder names

## CSV Files to Create Next

- `data/banking/checking_accounts.csv`
- `data/banking/savings_accounts.csv`
- `data/banking/cd_accounts.csv`
- `data/banking/interest_rates_history.csv`
- `data/portfolio/sector_analysis.csv`
- `data/portfolio/stock_holdings.csv`
- `data/real_estate/properties.csv`
- `data/real_estate/mortgages.csv`
- `data/retirement/401k_accounts.csv`
- `data/retirement/ira_accounts.csv`
- `data/loans/personal_loans.csv`
- `data/loans/student_loans.csv`
- `data/insurance/life_insurance.csv`
- `data/forex/currency_pairs.csv`
- `data/commodities/commodity_holdings.csv`
