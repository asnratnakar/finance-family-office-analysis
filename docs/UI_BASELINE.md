# Local App UI Baseline

**Purpose:** preserve the existing Streamlit UI precisely when migrating code into a new repository.

**Baseline date:** 14 November 2026

## Global

- Framework: Streamlit multi-page app
- Main entry: `PersonalPortfolioAnalysis.py`
- Default page layout: `wide`, except each page explicitly may repeat `st.set_page_config(... layout="wide")`
- Main navigation: Streamlit sidebar automatically lists `pages/` in filename order
- Streamlit derives the visible filename entry until overridden by page/config behavior
- Shared visual style: simple headings, horizontal rules, Plotly charts, Streamlit metrics, tables, and muted informational captions
- Default reporting currency in current working pages: US dollars
- Current app status: working pages coexist with broken, empty, and mislabelled pages

## Left navigation menu / page list

Capture the rendered menu labels and order from the running app. The source filenames below are the expected navigation order:

| Order | Source file | Streamlit route label to verify | Page title | UI status |
|---:|---|---|---|---|
| 1 | `PersonalPortfolioAnalysis.py` | Home / app entry name | `💰 Personal Finance Analysis` | Working welcome/home page |
| 2 | `pages/1_Bank_Accounts.py` | `1_Bank_Accounts` or cleaned label | `🏦 Bank Accounts` | Working conceptually; known bugs |
| 3 | `pages/2_RealEstate.py` | `2_RealEstate` or cleaned label | No implementation title | Empty (0 bytes) |
| 4 | `pages/3_Retirement.py` | `3_Retirement` or cleaned label | `🎯 Sector-wise Investment Analysis` while configured as `Sector Analysis` | Mislabelled legacy sector page |
| 5 | `pages/4_Market_Investments.py` | `4_Market_Investments` or cleaned label | `📈 Market Investments - Portfolio Analysis` | Working for Vanguard summaries |
| 6 | `pages/5_Metals.py` | `5_Metals` or cleaned label | `🧈 Metals Investment Performance Analysis` | Working with known bugs/data/API concerns |
| 7 | `pages/6_CommoditiesAccounts.py` | `6_CommoditiesAccounts` or cleaned label | None | Empty |
| 8 | `pages/6_ForexAccounts.py` | `6_ForexAccounts` or cleaned label | None | Empty |
| 9 | `pages/6_LifeInsuranceAccounts.py` | `6_LifeInsuranceAccounts` or cleaned label | None | Empty |
| 10 | `pages/6_Loan_Calculator.py` | `6_Loan_Calculator` or cleaned label | `💳 Loan Repayment Calculator` | Working |
| 11 | `pages/7_Knowledge_Base.py` | `7_Knowledge_Base` or cleaned label | `📚 Knowledge Base Hub - Step-by-Step Learning Path` | Working |
| 12 | `pages/8_Family_Office.py` | `8_Family_Office` or cleaned label | `👨‍👩‍👧‍👦 Family Office` | Working static diagram |

Navigation capture requirements:

- Record exact labels displayed in the left menu, including underscores, spaces, emoji, numbering, and capitalization.
- Record whether menu labels come from filenames or explicit page configuration.
- Record whether `st.set_page_config(page_title=...)` changes the browser title only or also affects menu text.
- Record menu width, item height, selected-item highlight, hover state, icon position, and padding.
- Capture active-item styling and scroll position after selecting a page.
- Record home-page placement and numbered-page ordering.
- Record duplicate-number pages (`6_*`) and their actual rendered order.
- Record whether empty page entries should remain or be removed from the target app.
- Baseline screenshots must include the left menu with all entries and each page's selected state.

## Home / `PersonalPortfolioAnalysis.py`

- Page title: `💰 Personal Finance Analysis`
- Page icon: `💰`
- Wide layout
- Expanded sidebar
- CSS: reduced top/main padding
- Main welcome heading: `Welcome to Personal Financial Analysis Dashboard`
- Three feature summaries:
  1. Metal Investment Performance
  2. Sector-wise Investment Analysis
  3. Loan Repayment Calculator
- Intro text says to select a tool from the sidebar
- Info tip: `Tip: You can upload your own CSV files or use sample data to get started!`
- Footer: `Personal Finance Analysis Tool | Built with Streamlit | v1.0`

## 1 — Bank Accounts

**Status:** working conceptually, known column/sort/CD bugs

- Title: `🏦 Bank Accounts`
- Wide layout
- Data source: local CSV files only

### Checking accounts

- Section: `💰 Checking Accounts`
- Two columns: 2:1
- Left: latest account table with Account, Month, Year, Ending Balance
- Right metric: `Total Ending Balance`
- Section: `Checking Account Ending Balance Trend`
- Plot: line chart, one trace per account, monthly x-axis, ending-balance y-axis
- Plot title: `Checking Account Ending Balance Trends`
- Template: Plotly white

### Savings accounts

- Section: `🏪 Savings Accounts`
- Two columns: 2:1
- Left table: Account and Balance
- Right metric: `Total Savings Balance`
- Known behavior: missing/incorrect current-balance column handling must be tested

### CD accounts

- Section: `💳 Certificate of Deposit (CD) Accounts`
- Table: Bank, Principal, APY, Term, Interest Earned, Maturity Value, Annual Yield, Maturity Date
- Four summary metrics:
  - Total CD Principal
  - Total Interest to Earn
  - Total Maturity Value
  - Average Rate

### Rates comparison

- Section: `📊 Fed Funds vs Inflation vs Savings Rate`
- Plot: Fed Funds Rate, Inflation Rate, and Savings Account Interest Rates over time

### remaining exact details

- A horizontal radio control follows the Fed Funds/savings section: `What would you like to calculate?`
- Radio options, in source order: `Future Value (PV → FV)` and `Present Value (FV → PV)`
- The radio is horizontal and uses key `converter_type`.
- Future-value defaults:
  - Present Value ($): `10000.0`, minimum `0`, step `100`
  - Annual Rate (%): `4.5`, range `0–20`, step `0.01`
  - Years: `5.0`, range `0–50`, step `0.5`
  - Compound: `Annually`, `Semi-Annually`, `Quarterly`, `Monthly`, `Daily`, default `Annually`
- Future-value metric names: `Future Value`, `Interest Earned`, `Total Return`.
- Present-value defaults:
  - Future Value ($): `15000.0`, minimum `0`, step `100`
  - Annual Rate (%): `4.5`, range `0–20`, step `0.01`
  - Years: `5.0`, range `0–50`, step `0.5`
  - Compound options and order match future-value mode.
- Present-value metric names: `Present Value`, `Interest Needed`, `Interest Percentage`.
- Both formula branches render a Markdown formula block and variable-by-variable value list.
- Footer: `All calculations are estimates. Actual results may vary based on bank policies and market conditions.`
- Source footers use `<small>` HTML and `unsafe_allow_html=True`.

## 2 — Real Estate

- File exists but is empty (0 bytes)
- No UI baseline exists in code
- Do not invent a replacement screen; preserve the empty-page status until P1/P6 defines the real screen

## 3 — Retirement

**Status:** mislabelled and contains a legacy sector-analysis implementation

- Streamlit page title: `Sector Analysis`
- Visible title: `🎯 Sector-wise Investment Analysis`
- Sidebar radio: `Sample Data` or `Upload CSV`
- Upload CSV type: `csv`
- Required fields: Sector, Stock, Investment_Amount, Current_Value, Quantity
- Raw-data expander: `📊 View Raw Data`
- Four metrics:
  - Total Investment
  - Current Value
  - Total Return
  - Return (%)
- Sector allocation: pie chart plus allocation table
- Sector performance: horizontal return chart and vertical value chart
- Detailed sector analysis follows below
- This UI should be replaced, not preserved as the Retirement UI

### remaining exact details

- Sidebar header: `Data Source`
- Default radio source: `Sample Data`; alternate: `Upload CSV`
- Sidebar upload accepts only `csv` and shows its CSV-column help text.
- In sample mode, a blue info callout says `Using sample portfolio data for demonstration`.
- Four summary metrics are in a 4-column row.
- Sector-allocation pie title: `Portfolio Allocation by Sector (%)`.
- Sector table columns: `Sector`, `Current Value ($)`, `Allocation (%)`, `Return (%)`, sorted by current value descending.
- Sector return chart: horizontal bar chart, title `Return Percentage by Sector`, red-to-green continuous scale.
- Sector value chart: vertical bar chart, title `Current Value by Sector`, blue continuous scale.
- Detailed selector label: `Select a sector to analyze in detail:`.
- Sector detail metrics: `Sector Value`, `Allocation %`, `Return %`.
- Holdings table columns: `Stock`, `Investment ($)`, `Current Value ($)`, `Quantity`, `Return %`.
- Holdings pie title: `Holdings Distribution in <sector> Sector`.
- Diversification metrics: `Number of Sectors`, `Total Holdings`, `Avg Sector Allocation`.
- Diversification info text begins `📊 Diversification Score:`.
- Privacy footer uses `<small>` HTML.

## 4 — Market Investments

- Title: `📈 Market Investments - Portfolio Analysis`
- Wide layout
- Data: latest and historical Vanguard cost-basis summaries in `data/portfolio/`
- Overall summary with four metrics:
  - Total Cost
  - Market Value
  - Total Gains/Loss
  - Return %
- Combined portfolio sector pie chart
- Stocks vs ETFs section in two columns
- Each stock/ETF panel has:
  - Total Cost
  - Total Gains
  - Market Value
  - Holdings
  - sector pie chart
- Market value trend charts:
  - Stock Market Value Trends
  - ETF Market Value Trends
  - One line by `Symbol/CUSIP`
- Top holdings section:
  - Top Stocks by Market Value
  - Top ETFs by Market Value
  - Ten rows per table
- Full portfolio expander: `📋 View Full Portfolio Data`

## 5 — Metals

- Title: `🧈 Metals Investment Performance Analysis`
- Wide layout
- Sidebar radio: `Local Data (metals_transactionHistory.csv)` or `Upload CSV`
- Upload help: `CSV should have columns: Date, Metal, Cost, Quantity_oz`
- Allocation section:
  - two pie charts: market value and cost
  - gold is gold RGB, silver is silver RGB, other metals are light gray
  - allocation table: Metal, Cost, Quantity_oz, Market Value, % Growth, Unrealized Gains/Loss
- Live prices section: `💲Current Live Metal Prices`
- Two metrics: Gold (XAU), Silver (XAG)
- Each has collapsed `ℹ️ More Details` JSON expander
- Caption records last update time
- Procurement section: `🛒 Metals Procurement Analysis`
- Separate Gold Procurement and Silver Procurement tables
- Later sections calculate investment return, divestment scenarios, and detailed metal analysis

### remaining exact details

- Sidebar header: `Data Source`.
- Radio options: `Local Data (metals_transactionHistory.csv)` and `Upload CSV`.
- Uploaded CSV help text requires `Date, Metal, Cost, Quantity_oz`.
- Allocation uses 2 equal columns, one market-value pie and one cost pie.
- Both pies use 30% holes and `use_container_width=True`.
- Gold pie slice color: `rgb(255, 215, 0)`.
- Silver pie slice color: `rgb(192, 192, 192)`.
- Other-metal fallback color: `lightgray`.
- Allocation table formatting: cost, quantity, market value, growth, and gain/loss are display strings.
- Tax bracket input default is `27.0`, range `0–100`, step `1.0`.
- Gold divestment scenarios use `[-2, -3, -4]` percent; silver uses `[-5, -7, -9]` percent.
- Bullion discount expander is collapsed by default with label `💰 Selling Bullion - Dealer Discount Information`.
- Transaction history expander is collapsed by default and has label `📊 View detailed Transaction History`.
- The live-prices timestamp is shown as local-machine text in the existing code, despite the source label wording including UTC.

## 6 — Loan Calculator

- Title: `💳 Loan Repayment Calculator`
- Three tabs:
  1. `Single Loan Calculator`
  2. `Amortization Schedule`
  3. `Loan Comparison`

### Single loan

- Three number inputs:
  - Loan Amount ($), default 200,000
  - Annual Interest Rate (%), default 5.5
  - Loan Duration (Years), default 30
- Four metrics:
  - Monthly Payment
  - Total Interest
  - Total Amount Paid
  - Interest as % of Principal
- Includes a blue loan-summary info box

### Amortization schedule

- Same three inputs with independent widget keys
- `Show first N rows`, default 12
- `Show all months` checkbox
- Table of Month, Payment, Principal, Interest, and Balance
- Two charts:
  - Principal vs Interest donut chart
  - Remaining balance area/line chart

### Loan comparison

- Inputs:
  - Loan Amount ($), default 200,000
  - Annual Interest Rate (%), default 5.5
- Checkboxes for 5, 10, 15, 20, 30 and Custom Years
- Five-year/10-year/15-year/30-year are default checked
- Results include side-by-side scenario metrics/tables and comparison charts

### remaining exact details

- The page uses exactly 3 tabs in source order:
  1. `Single Loan Calculator`
  2. `Amortization Schedule`
  3. `Loan Comparison`
- Single-loan number inputs default to principal `200000.0`, annual rate `5.5`, and duration `30`.
- Single-loan metric names and order are the same as the existing baseline.
- Amortization defaults: principal `200000.0`, annual rate `5.5`, years `30`, shown rows `12`, step `12`.
- The schedule can show all months or the first N rows.
- Principal-versus-interest chart uses a 30% donut hole.
- Remaining-balance chart uses a line/area fill named `Remaining Balance`.
- Loan-comparison input defaults: principal `200000.0`, annual rate `5.5`.
- Terms are individually checkboxes in rows: 5, 10, 15 / 20, 30, Custom.
- Default checked terms: 5, 10, 15, and 30 years.
- Custom-year default: `25`, range minimum `1`, step `1`.
- Comparison table headers are `Loan Term (Years)`, `Monthly Payment ($)`, `Total Interest ($)`, `Total Paid ($)`.
- Payment chart title: `Monthly Payment vs Loan Duration`; line color `#1f77b4`, width `3`.
- Interest chart title: `Total Interest vs Loan Duration`; line color `#ff7f0e`, width `3`, with area fill.
- Privacy footer uses `<small>` HTML.

## 7 — Knowledge Base

- Title: `📚 Knowledge Base Hub - Step-by-Step Learning Path`
- Intro describes a five-stage progressive learning journey
- Table of contents is split across three columns
- Five sections are created with tabs:
  1. Macroeconomics
  2. Banking Basics + Credit Markets
  3. Securities Overview + Market Investing
  4. Stocks + Bonds + Mutual Funds + ETFs
  5. Precious Metals + Real Estate
  6. Retirement + S&P 500 + All Weather Portfolio
- Section names and tab labels preserve the educational navigation
- Footer: `Last updated: March 2026 | Total Modules: 10`

### exact navigation

- Intro text is a Markdown learning journey covering Foundation, Macro, Banking/Credit, Securities/Investing, Alternative Investments, and Retirement/Strategies.
- Table-of-contents links use 3 columns.
- Section anchors are generated as `<a id="...">` elements.
- Section 1 tab label: `Macroeconomics - Understanding the Economy`.
- Section 2 tabs: `Banking Basics - Savings & Accounts`, `Credit Markets - How Money Flows`.
- Section 3 tabs: `Securities Overview - Stocks, Bonds, ETFs, Mutual Funds`, `Market Investing - Investment Vehicles`.
- Section 3A tabs: `Stocks Guide - Equity Investing`, `Bonds Guide - Fixed Income`, `Mutual Funds Guide - Pooled Investment`, `ETFs Guide - Exchange-Traded Funds`.
- Section 4 tabs: `Precious Metals - Alternative Asset Class`, `Real Estate - Property Investing`.
- Section 5 tabs: `Retirement Planning - 401(k), IRA, Pensions`, `S&P 500 Guide - Index Investing`, `All Weather Portfolio - Dalio's Strategy`.
- Footer: `Last updated: March 2026 | Total Modules: 10`.

## 8 — Family Office

- Title: `👨‍👩‍👧‍👦 Family Office`
- Wide layout
- Intro: `Family Office Management`
- Section: `📊 Family Office Services Network`
- Interactive network graph built with NetworkX + Plotly
- Center node: Family Office
- Customer node at right
- Eight main service categories:
  - Wealth Management
  - Wealth Planning
  - Tax Planning
  - Estate Planning
  - Risk Management
  - Family Governance
  - Real Estate
  - Legal Services
- Graph includes category nodes and subcategory nodes
- Current page is static diagram guidance, not account or transaction data

### exact diagram styling

- Network title: `Family Office Services Network Structure`.
- Center node is gold, category nodes are blue, subcategory nodes are gray circles, and customer is green.
- Center text font: 12 px, black, `Arial Black`.
- Category text font: 11 px, black, `Arial Black`.
- Subcategory text font: 10 px, black.
- Customer marker size: `60`; subcategory marker size: `22`.
- Center rectangle: `1.0 × 0.5` layout units.
- Category rectangle: `0.9 × 0.45` layout units.
- Edge color: blue with 60% alpha and width `1.5`; customer edge is black with width `2.5`.
- Figure height: `800 px`.
- Paper/plot background: `rgba(245, 245, 250, 0.5)`.
- Margins: bottom `20`, left `5`, right default, top `40`.
- Grid, zero line, and tick labels are hidden.
- Four legend cards explain Yellow, Blue, Gray, and Green nodes.
- Eight category expanders are collapsed and show subcategories and action-item bullets.

## Empty / incomplete pages

The following page files exist but have no implemented UI and must not be described as working:

- `pages/2_RealEstate.py`
- `pages/6_CommoditiesAccounts.py`
- `pages/6_ForexAccounts.py`
- `pages/6_LifeInsuranceAccounts.py`

## UI migration rules

1. Preserve working screens until explicitly replaced.
2. Preserve page titles, tabs, table columns, metric names, defaults, and chart types.
3. Add synthetic-data fallbacks before removing the legacy local CSV behavior.
4. Do not preserve known bugs as intentional UI behavior.
5. Replace, rather than repair in place, pages that are mislabelled or empty.
6. Capture Playwright/Streamlit screenshots for every working screen after the migration baseline is complete.
7. Treat this document as the UI contract; code changes require either a matching UI update or an approved design change.
