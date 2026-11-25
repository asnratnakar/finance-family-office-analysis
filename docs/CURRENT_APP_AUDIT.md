# Current App Audit

**Audit date:** 25 November 2026
**Purpose:** separate facts from roadmap goals and prevent migration assumptions

## Summary

The repository is a Streamlit multi-page dashboard with legacy CSV inputs. It is not a shared-ledger app and does not yet provide cross-account risk, tax, or advice infrastructure.

## Entry point

- `PersonalPortfolioAnalysis.py`
- Set page title: Personal Finance Analysis
- Set page icon: 💰
- Layout: wide
- Initial sidebar state: expanded
- Adds custom CSS reducing `.main` padding to `0rem 0rem`
- Renders welcome copy and a three-tool overview
- Renders a footer in HTML with centered text

## Working page inventory

| Page | File | Current implementation | Caveats |
|---|---|---|---|
| Home | `PersonalPortfolioAnalysis.py` | Welcome dashboard and feature overview | Stale copy says three tools; no live portfolio overview |
| Bank Accounts | `pages/1_Bank_Accounts.py` | Checking, savings, CDs, market-rate chart, PV/FV converter | Known bugs and data-column mismatches |
| Market Investments | `pages/4_Market_Investments.py` | Vanguard snapshot summaries, sector pies, trends, top holdings | Vanguard-only and snapshot-based |
| Metals | `pages/5_Metals.py` | Transactions, allocation, live/fallback prices, procurement/divestment | API calls, fallback and timestamp behavior need tests |
| Loan Calculator | `pages/6_Loan_Calculator.py` | Single loan, amortization, comparison tabs | Independent widget keys preserve separate state |
| Knowledge Base | `pages/7_Knowledge_Base.py` | 15-tab learning hub across 10 modules | Educational content only |
| Family Office | `pages/8_Family_Office.py` | Static NetworkX/Plotly service diagram and action tree | No account or advice data |

## Broken or incomplete page inventory

| Page | File | Status | Required action |
|---|---|---|---|
| Real Estate | `pages/2_RealEstate.py` | Empty file | Replace only in P1/P6 UI scope |
| Commodities | `pages/6_CommoditiesAccounts.py` | Empty file | Remove or implement after ledger/input design |
| Forex | `pages/6_ForexAccounts.py` | Empty file | Remove or implement after ledger/input design |
| Life Insurance | `pages/6_LifeInsuranceAccounts.py` | Empty file | Remove or implement after ledger/input design |
| Retirement | `pages/3_Retirement.py` | Mislabelled sector-analysis page | Replace with retirement UI; do not call it a working retirement feature |

## Utility inventory

| Utility | Role | Migration concern |
|---|---|---|
| `utils/loan.py` | Loan payment/amortization/scenario calculations | Test independently; preserve formulas |
| `utils/metals.py` | Metals valuation, procurement, divestment, summaries | Handle unavailable prices and no-quantity cases |
| `utils/portfolio_calc_van.py` | Vanguard lot summary calculations and file discovery | Broker-specific and filename/sort bugs exist |
| `utils/portfolio.py` | Legacy duplicate portfolio calculations | Consolidate or remove after tests |
| `utils/keyManagement.py` | API-key loading | Move secrets to OS keyring/env policy |

## Shared code concerns

- Every page reads separate CSV formats or utility functions.
- There is no instrument/lot/transaction ledger shared across pages.
- Multi-account net worth is not implemented.
- Risk analytics are not implemented.
- TWR/XIRR are not implemented.
- Daily snapshot history is not implemented.
- US and India tax bases are not unified.
- `networkx` is required for Family Office but is not currently pinned.
- Some pages use direct local file paths and assume a working directory.

## Known Bank Accounts behavior

- Checking latest-row logic depends on sorting and account names.
- Month sorting must include year and a date value, not text alone.
- Savings page has a known column mismatch: code expects `Current Balance`, local file/expected structure may differ.
- CD maturity is currently simple-interest-like in the observed code and must be compared to true APY compounding rules.
- The PV/FV converter has independent radio state and rate/years/compound controls.

## Known Metals behavior

- The live API uses a yesterday date in the URL.
- API responses are cached for one hour.
- Missing API key may fall back to local spot-price CSV.
- Missing live price must not silently create an inflated or false valuation.
- The page makes an additional API call for JSON detail expanders.
- The timestamp label may say UTC even though source code uses local `datetime.now()`.

## Known Market Investments behavior

- The latest and historical values come from summary CSV filename reports.
- Filename parsing/sort behavior must not rely on text ordering of MMDDYYYY names.
- Summary globbing must exclude generated summary files.
- Portfolio results are per snapshot and do not provide true time-weighted/money-weighted returns.

## Data files

Real portfolio, banking, metals, and API-key data may exist under `data/`. The new repository must not copy these files. Synthetic examples may be created under `data/samples/`.

## UI baseline status

Use `UI_BASELINE.md` for intended baseline details and `scripts/capture_ui_baseline.py` for browser evidence.

No screenshot set should be considered proof until it includes:

- desktop 1440 px
- desktop 1280 px
- mobile/narrow 390 px
- left navigation/menu
- each page default state
- relevant expanded tabs/expanders
- synthetic or no-data/error states
