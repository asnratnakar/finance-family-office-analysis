# Personal Finance Analysis Tool - Documentation

**Version:** 1.0 | **Status:** legacy product documentation; verify against source | **Created:** February 18, 2026 | **Re-audited:** November 25, 2026

> **Accuracy notice:** This file contains older descriptions and must not be used as the sole UI or implementation specification. Use `UI_BASELINE.md`, `UI_CHANGE_CONTROL.md`, `IMPLEMENTATION_CONTRACT.md`, `DATA_CONTRACT.md`, and `TASK_EXECUTION_CONTRACT.md` for authoritative rules. The Streamlit entry point is `PersonalPortfolioAnalysis.py`. The app currently uses or may call external services, including the metals API; it should not be described as “no external APIs” unless a current verification proves that state.

---

## 📑 Table of Contents

1. [Quick Start](#quick-start)
2. [Installation](#installation)
3. [Features](#features)
4. [Project Structure](#project-structure)
5. [CSV Data Formats](#csv-data-formats)
6. [Usage Guide](#usage-guide)
7. [Examples & Scenarios](#examples--scenarios)
8. [Troubleshooting](#troubleshooting)
9. [Technology Stack](#technology-stack)
10. [Privacy & Security](#privacy--security)

---

## Quick Start

### Start in 2 Commands

> The project entry point is `PersonalPortfolioAnalysis.py`, not `app.py`.

```powershell
cd "c:\Users\user\Documents\GitRepos\Personal\private-fin-analysis"
pip install -r requirements.txt
streamlit run PersonalPortfolioAnalysis.py
```

**The app opens automatically at:** `http://localhost:8501`

**Time needed:** ~5 minutes

---

## Installation

### Requirements
- Python 3.8+
- pip (Python package manager)
- Internet connection (for first-time setup)

### Step-by-Step Installation

#### 1. Navigate to Project Folder
```powershell
cd "c:\Users\user\Documents\GitRepos\Personal\private-fin-analysis"
```

#### 2. Install Dependencies
```powershell
pip install -r requirements.txt
```

This installs:
- Streamlit 1.28.1
- Pandas 2.0.3
- Plotly 5.17.0
- NumPy 1.24.3

#### 3. Run the Application
```powershell
streamlit run PersonalPortfolioAnalysis.py
```

#### 4. Open in Browser
- App opens automatically at `http://localhost:8501`
- Or navigate manually if needed

### Optional: Virtual Environment Setup
```powershell
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run PersonalPortfolioAnalysis.py
```

---

## Features

### 🥇 Metal Investment Performance

**Purpose:** Track and analyze precious metals investments

**What You Can Do:**
- Upload CSV with metals data or use sample data
- Monitor price trends over time
- Calculate investment returns ($ and %)
- View portfolio allocation by metal
- Analyze individual metals
- Track Gold, Silver, Platinum, Palladium

**Key Metrics:**
- Current portfolio value
- Total investment amount
- Return percentage
- Price trends
- Allocation percentages

**CSV Format Required:**
```csv
Date,Metal,Price_per_oz,Quantity_oz
2024-02-18,Gold,2050.00,10.5
2024-03-18,Gold,2075.00,10.5
2024-04-18,Gold,2150.00,10.5
```

---

### 🎯 Sector-wise Investment Analysis

**Purpose:** Analyze your stock portfolio by investment sector

**What You Can Do:**
- Upload portfolio data or use sample portfolio
- View allocation by sector
- Track sector performance and returns
- Calculate diversification score
- View individual holdings by sector
- Compare sector performance

**Key Metrics:**
- Sector allocation percentages
- Sector returns
- Diversification score (0-100)
- Total portfolio value
- Sector performance comparison

**CSV Format Required:**
```csv
Sector,Stock,Investment_Amount,Current_Value,Quantity
Technology,TECH-1,15000,18500,150
Healthcare,HEALTH-1,20000,24300,100
Finance,FIN-1,25000,27500,200
Energy,ENERGY-1,10000,11500,100
Consumer,CONS-1,8000,9200,80
Utilities,UTIL-1,9000,10100,90
```

**Supported Sectors:**
- Technology
- Healthcare
- Finance
- Energy
- Consumer
- Utilities
- (or any custom sectors)

---

### 💳 Loan Repayment Calculator

**Purpose:** Calculate and plan loan repayments

**Three Calculator Modes:**

#### Mode 1: Single Loan Calculator
- Input: Loan amount, interest rate, duration
- Output: Monthly payment, total interest, total amount paid
- Useful for quick calculations

#### Mode 2: Amortization Schedule
- Shows month-by-month payment breakdown
- View principal vs interest payments
- Track remaining balance over time
- Export schedule if needed

#### Mode 3: Loan Comparison
- Compare multiple loan terms side-by-side
- 5-year, 10-year, 15-year, 20-year, 30-year options
- Custom loan terms supported
- Visual comparison charts

**Calculations Provided:**
- Monthly payment amount
- Total interest paid
- Total amount paid
- Interest as percentage of principal
- Balance over time

---

## Project Structure

```
private-fin-analysis/
│
├── 📱 Application Core
│   ├── PersonalPortfolioAnalysis.py   Main entry point
│   ├── requirements.txt               Dependencies
│   ├── .gitignore                     Git configuration
│   └── .env.example                   Local secret template
│
├── 📄 Multi-page app
│   ├── pages/1_Bank_Accounts.py       Bank/account tools
│   ├── pages/2_RealEstate.py          Real-estate tools
│   ├── pages/3_Retirement.py          Retirement views
│   ├── pages/4_Market_Investments.py  Portfolio analysis
│   ├── pages/5_Metals.py              Precious metals tools
│   ├── pages/6_CommoditiesAccounts.py
│   ├── pages/6_ForexAccounts.py
│   ├── pages/6_LifeInsuranceAccounts.py
│   ├── pages/6_Loan_Calculator.py     Loan calculator
│   ├── pages/7_Knowledge_Base.py      Knowledge base
│   └── pages/8_Family_Office.py      Family-office overview
│
├── 🛠️ Utility Functions
│   ├── utils/__init__.py              Package init
│   ├── utils/metals.py                Metal calculations
│   ├── utils/portfolio.py             Portfolio helpers
│   ├── utils/portfolio_calc_van.py    Vanguard cost-basis logic
│   └── utils/loan.py                  Loan formulas
│
├── 📊 Data
│   ├── data/                          Local financial data directory
│   └── data/samples/                 Synthetic sample data only
│
├── ⚙️ Config & tests
│   ├── .pre-commit-config.yaml
│   ├── tests/
│   └── .streamlit/
│
└── 📚 Documentation
    └── docs/
```

---

## CSV Data Formats

### Metal Investment CSV

**File Name:** `metals.csv` or `my_metals.csv`

**Required Columns:**
- `Date` - Date in YYYY-MM-DD or MM/DD/YYYY format
- `Metal` - Metal name (Gold, Silver, Platinum, Palladium, etc)
- `Cost` - Cost per unit (number)
- `Quantity_oz` - Quantity in ounces (number)

**Example:**
```csv
Date,Metal,Cost,Quantity_oz
2024-02-18,Gold,2050.00,10.5
2024-02-18,Silver,24.50,100.0
2024-02-18,Platinum,950.00,5.0
2024-02-18,Palladium,850.00,3.5
2024-03-18,Gold,2075.00,10.5
2024-03-18,Silver,25.00,100.0
2024-03-18,Platinum,975.00,5.0
2024-03-18,Palladium,875.00,3.5
```

**Tips:**
- Use consistent date format
- Metal names are case-sensitive
- Prices should be positive numbers
- Quantity can be decimal (e.g., 10.5 oz)

---

### Portfolio Investment CSV

**File Name:** `portfolio.csv` or `my_portfolio.csv`

**Required Columns:**
- `Sector` - Investment sector name
- `Stock` - Stock/holding name
- `Investment_Amount` - Original investment amount ($)
- `Current_Value` - Current market value ($)
- `Quantity` - Number of shares/units

**Example:**
```csv
Sector,Stock,Investment_Amount,Current_Value,Quantity
Technology,TECH-1,15000,18500,150
Technology,TECH-2,12000,14200,120
Healthcare,HEALTH-1,20000,24300,100
Healthcare,HEALTH-2,15000,16800,80
Finance,FIN-1,25000,27500,200
Finance,FIN-2,18000,19200,150
Energy,ENERGY-1,10000,11500,100
Energy,ENERGY-2,12000,10800,120
Consumer,CONS-1,8000,9200,80
Consumer,CONS-2,11000,12500,100
Utilities,UTIL-1,9000,10100,90
```

**Tips:**
- Investment_Amount = what you paid
- Current_Value = current market value
- Return is calculated as: (Current - Investment) / Investment × 100
- Use consistent sector names
- All amounts should be positive

---

## Usage Guide

### Using the Application

#### Starting the App
```powershell
cd "c:\Users\user\Documents\GitRepos\Personal\private-fin-analysis"
streamlit run PersonalPortfolioAnalysis.py
```

#### Navigation
The app has a sidebar with three main sections:
1. **Metal Investment** - First analysis tool
2. **Sector Analysis** - Second analysis tool
3. **Loan Calculator** - Third analysis tool

### Metal Investment Tool

**Step 1:** Click "Metal Investment" in sidebar

**Step 2:** Choose data source
- **Local Data:** Load from `data/metals.csv`
- **Upload CSV:** Your own data file

**Step 3:** If uploading, select your CSV file with columns:
- Date, Metal, Cost, Quantity_oz

**Step 4:** View results
- Portfolio summary (total value, quantity, average cost)
- Allocation pie chart (by metal)
- Current live metal prices from API
- Individual metal analysis
- Return calculations

**Step 5:** Analyze individual metals
- Select metal from dropdown
- View price trend
- Input purchase price and quantity
- See return in $ and %

---

### Sector Analysis Tool

**Step 1:** Click "Sector Analysis" in sidebar

**Step 2:** Choose data source
- **Sample Data:** Pre-loaded portfolio
- **Upload CSV:** Your portfolio file

**Step 3:** If uploading, select CSV with columns:
- Sector, Stock, Investment_Amount, Current_Value, Quantity

**Step 4:** View results
- Portfolio summary (total investment, current value, returns)
- Sector allocation pie chart
- Sector performance comparison
- Diversification score
- Holdings breakdown

**Step 5:** Detailed analysis
- Select sector from dropdown
- View holdings in that sector
- See sector allocation within portfolio
- Compare sector performance

---

### Loan Calculator Tool

**Step 1:** Click "Loan Calculator" in sidebar

**Step 2:** Choose calculator mode
- **Single Loan Calculator:** One loan analysis
- **Amortization Schedule:** Month-by-month breakdown
- **Loan Comparison:** Compare multiple terms

**Step 3: Single Loan Mode**
- Enter loan amount ($)
- Enter interest rate (%)
- Enter duration (years)
- View: Monthly payment, total interest, total paid
- See: Interest percentage of principal

**Step 4: Amortization Mode**
- Enter same details as Single Loan
- Choose how many rows to display
- View detailed payment schedule
- See: Payment, Principal, Interest, Balance
- Visualizations: Principal vs Interest pie, Balance over time

**Step 5: Comparison Mode**
- Enter loan details
- Check boxes for terms to compare
- 5, 10, 15, 20, 30-year options available
- Add custom term if needed
- View side-by-side comparison
- See: Monthly payment vs duration chart
- See: Total interest vs duration chart

---

## Examples & Scenarios

### Scenario 1: Gold Investment Analysis

**Your Data:**
- Bought 10.5 oz of Gold at $1950/oz on 2024-02-18
- Current price: $2150/oz on 2024-04-18

**CSV Entry:**
```csv
Date,Metal,Cost,Quantity_oz
2024-02-18,Gold,1950.00,10.5
2024-03-18,Gold,2050.00,10.5
2024-04-18,Gold,2150.00,10.5
```

**What You'll See:**
- Initial investment: $20,475
- Current value: $22,575
- Return: $2,100 (+10.25%)
- Current live market price from API
- Compare your cost vs current market price

---

### Scenario 2: Portfolio Diversification Analysis

**Your Portfolio:**
```
Technology:    50% ($50,000) - High growth
Healthcare:    25% ($25,000) - Stable
Finance:       15% ($15,000) - Dividend income
Consumer:      10% ($10,000) - Cyclical
```

**What You'll See:**
- Allocation pie chart
- Sector performance comparison
- Diversification score: 65/100 (Good)
- Recommendation: Increase Finance & Consumer exposure

---

### Scenario 3: Mortgage Loan Planning

**Your Loan:**
- Amount: $300,000
- Interest Rate: 6.5%
- Duration: 30 years

**Monthly Payment:** $1,896.20
**Total Interest:** $382,631.60
**Total Paid:** $682,631.60

**Comparison with 15-year:**
- 15-year monthly: $2,559.41
- 15-year total interest: $160,694.54

**Decision:** 30-year saves $663/month but costs $222k more in interest

---

### Scenario 4: Student Loan Repayment

**Loan Details:**
- Amount: $50,000
- Interest Rate: 5.0%
- Duration: 10 years

**Results:**
- Monthly payment: $530.33
- Total interest: $13,639.80
- Total paid: $63,639.80

**What if you paid more?**
- Extra $100/month reduces total interest
- Extra $200/month saves even more

---

## Troubleshooting

### Installation Issues

#### Error: "Python not found"
```powershell
# Check if Python is installed
python --version

# If not installed, download from python.org
```

#### Error: "pip not found"
```powershell
# Upgrade pip
python -m pip install --upgrade pip

# Then install requirements
pip install -r requirements.txt
```

#### Error: Module not found after install
```powershell
# Reinstall all requirements
pip install -r requirements.txt --force-reinstall
```

---

### Running the App

#### Port 8501 Already in Use
```powershell
# Use different port
streamlit run PersonalPortfolioAnalysis.py --server.port 8502

# Check what's using port 8501
netstat -ano | findstr :8501
```

#### App Won't Open in Browser
```powershell
# Open manually at:
http://localhost:8501
```

#### Streamlit Not Responding
```powershell
# Stop the app (Ctrl+C) and restart
streamlit run PersonalPortfolioAnalysis.py
```

---

### Data Upload Issues

#### CSV Not Recognized
- **Check 1:** Use comma (,) as delimiter
- **Check 2:** Column names match exactly (case-sensitive)
- **Check 3:** No extra spaces in headers
- **Check 4:** Date format is YYYY-MM-DD or MM/DD/YYYY

#### Error: "Column 'Metal' not found"
- Ensure CSV has exact column: `Metal`
- Not: `metal` or `METAL` or `Metal `

#### Values Not Showing Correctly
- Numbers should not have commas: `1000` not `1,000`
- Decimals use period: `10.5` not `10,5`
- Dates use standard format: `2024-02-18`

---

### Performance

#### App is Slow
- Streamlit processes all data in memory
- Works best with < 10,000 rows
- For larger datasets, preprocess data

#### Charts Not Loading
- Refresh browser (F5)
- Clear cache: Streamlit menu → Clear cache
- Restart app

---

## Technology Stack

| Component | Package | Version | Purpose |
|-----------|---------|---------|---------|
| Framework | Streamlit | 1.28.1 | Web UI |
| Data | Pandas | 2.0.3 | Data processing |
| Charts | Plotly | 5.17.0 | Visualizations |
| Math | NumPy | 1.24.3 | Calculations |
| Language | Python | 3.8+ | Core language |

### Why These Technologies?

- **Streamlit** - Easy to build interactive web apps without frontend expertise
- **Pandas** - Powerful data manipulation and analysis
- **Plotly** - Interactive charts that work in web browsers
- **NumPy** - Fast numerical calculations
- **Python** - Widely used, good for financial calculations

---

## Privacy & Security

### ✅ What Makes This Secure

**100% Local Processing**
- All calculations happen on your computer
- No data sent to servers
- No cloud storage
- No internet connection needed after setup

**Data Handling**
- CSV files read into memory only
- Not stored or transmitted
- Closed automatically when app closes
- Your data never leaves your machine

**No External APIs**
- No market data feeds
- No authentication required
- No user accounts
- No tracking or analytics

**Open Source**
- All code is visible
- You can audit every calculation
- No hidden operations
- Source of truth is your data

### Privacy Checklist

- ✅ Local-only processing
- ✅ No backend server
- ✅ No cloud storage
- ✅ No external APIs
- ✅ No user tracking
- ✅ No data transmission
- ✅ No authentication needed
- ✅ Complete data ownership

---

## Advanced Topics

### Custom Sectors

To add new sectors to portfolio analysis:
1. Edit your CSV with new sector name
2. App automatically recognizes it
3. Include in charts and analysis

Example:
```csv
Sector,Stock,Investment_Amount,Current_Value,Quantity
RealEstate,REIT-1,20000,22000,100
CryptoCurrency,BTC,5000,6500,0.2
```

### Loan Calculations

The loan calculator uses standard amortization formula:

```
Monthly Rate = Annual Rate / 100 / 12
Number of Payments = Years × 12

Monthly Payment = Principal × 
  [Monthly Rate × (1 + Monthly Rate)^Payments] /
  [(1 + Monthly Rate)^Payments - 1]
```

### Export Data

While app doesn't have built-in export, you can:
1. **Print to PDF:** Ctrl+P → Save as PDF
2. **Copy tables:** Select and copy
3. **Screenshot:** Take screenshots of charts
4. **Manual export:** Recreate calculations in Excel

---

## Best Practices

### Metal Investment
- Update prices monthly for trends
- Include all metals in portfolio
- Use consistent date format
- Track quantity in ounces

### Portfolio Analysis
- Update values quarterly minimum
- Use current market prices
- Group related stocks same sector
- Review diversification quarterly

### Loan Calculator
- Verify rate with lender
- Include all fees in principal
- Compare scenarios before decision
- Check monthly budget impact

---

## Getting Help

### Documentation
- This file contains complete documentation
- Read sections relevant to your question
- Check Examples & Scenarios section

### Common Questions

**Q: Can I use the same data multiple times?**
A: Yes, upload same file each time or use sample data

**Q: Can I save the app's output?**
A: Use Print (Ctrl+P) to save as PDF

**Q: Does the app work offline?**
A: Yes, completely offline after initial setup

**Q: Can I modify the code?**
A: Yes, all code is editable Python files

**Q: Can I add more tools?**
A: Yes, create new files in `pages/` folder

---

## Quick Commands Reference

```powershell
# Navigation
cd "c:\Users\user\Documents\GitRepos\Personal\private-fin-analysis"

# Install (first time)
pip install -r requirements.txt

# Run app
streamlit run PersonalPortfolioAnalysis.py

# Different port
streamlit run PersonalPortfolioAnalysis.py --server.port 8502

# Check versions
python --version
pip list

# Clear Streamlit cache
streamlit cache clear
```

---

## Project Status

| Item | Status |
|------|--------|
| Core Application | ✅ Complete |
| Metal Investment Tool | ✅ Complete |
| Sector Analysis Tool | ✅ Complete |
| Loan Calculator Tool | ✅ Complete |
| Sample Data | ✅ Included |
| Documentation | ✅ Comprehensive |
| Testing | ✅ Ready |
| Production Ready | ✅ Yes |

---

## Summary

Your Personal Finance Analysis tool is:
- ✅ Fully functional
- ✅ Ready to use
- ✅ Well documented
- ✅ Privacy-focused
- ✅ Feature-complete

**Get started with:**
```powershell
cd "c:\Users\user\Documents\GitRepos\Personal\private-fin-analysis"
pip install -r requirements.txt
streamlit run PersonalPortfolioAnalysis.py
```

**Happy analyzing!** 💰📊

---

**Version:** 1.0 | **Created:** February 18, 2026 | **Status:** Ready to Use ✅
