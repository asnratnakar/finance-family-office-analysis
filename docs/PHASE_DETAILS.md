# Phase details

Each phase lists its goal, features, and a done-when test; backlog run numbers are in brackets. The weekly run reads this tab as `docs/PHASES.md`.

## Track A: now

### P0 Foundations and hygiene \[runs 1-7\]

Goal: a codebase that is safe to commit and trustworthy enough to build on.

- `.gitignore` covers `data/api_keys.keys`, `data/**/*.csv`, and `input/`; shareable synthetic files live in `data/samples/`
- API keys in the OS keyring (`keyring`) or `.env`
- Every bug in the repo's known-bugs table fixed, each with a test
- `utils/portfolio.py` and `utils/portfolio_calc_van.py` merged into one broker-neutral module
- Pinned `requirements.txt` (add `networkx`, `requests`) and recorded Python version
- `pytest` suite replaces `test_functions.py`; `ruff` and `pre-commit` hooks
- Empty pages removed or finished, Retirement page replaced, README refreshed, `debug_quotes.py` moved to `scripts/`

Done when: `pytest` passes, `git status` shows no keys or statements, and every page loads on sample data.

### P1 Family balance sheet and inherited-asset register \[runs 8-13\]

Goal: the whole family's financial picture in one place, with the numbers later decisions depend on.

- Input folder and account registry, with manual CSV templates for assets that have no export
- Agricultural land: location, acreage, value per acre, lease income, annual costs
- Vizag plots: size, value, holding cost; apartment buildings: units, rent, occupancy, deposits held (a liability), tax, maintenance, insurance, net operating income and net yield
- Jewellery and silver: weight, purity, IBJA rate minus making and melting loss; sentimental items excluded from investable wealth
- Co-ownership percentage per asset; net worth for me, my parents, and my expected share, in USD and INR
- Valuation history with source (guideline value, broker quote, registered valuer)
- Dual cost basis: US basis is date-of-death fair market value; Indian basis is the parents' cost (or FMV on 1 Apr 2001) with their holding period
- Parents' care cash flow: medical spending forecast, Indian income, shortfall funded from the US, runway in months
- Remittance ledger (effective rate vs mid-market, fees; 1% US excise on cash-funded transfers from 2026) and gift tracking against the US annual exclusion
- Trigger flags: Form 3520 above $100k inherited in a year, NRO USD 1M repatriation cap, FBAR and Form 8938

Done when: one page shows family net worth in USD and INR by owner, country, and asset class, with a current value, net yield, and both cost bases for every inherited asset.

### Data health \[run 14\]

Goal: every report says how fresh its inputs are and what to update.

- Freshness check on every input file's as-of date: stale after 6 months, softer notice after 30 days for positions (full rules in the Roadmap tab)
- Missing-data check: registry accounts with no file, holdings without cost basis, lots without dates, tickers with no price
- Update checklist naming which CSV to download from which broker, plus extra files needed (e.g. realized gains at tax time)
- As-of stamp on every number and chart

Done when: aging or deleting a sample file produces the right warning on every page.

## Track B: core platform

### Foundation capabilities \[run 15\]

Every sale decision, rebalance, and tax number depends on these five existing first.

1. **Multi-account aggregation:** one ledger across US brokerage, 401(k), IRA, HSA, India NRE/NRO/FCNR(B), bank and CD, bullion.
2. **Tax lots with cost basis and dates:** per country; FIFO, LIFO, specific ID; inherited-asset basis.
3. **Transaction and dividend history:** buys, sells, dividends, interest, fees, splits, transfers, FX conversions, rent, remittances, with currency, FX rate used, and TDS or withholding.
4. **Time-weighted and money-weighted returns:** TWR and XIRR in local and reporting currency, FX contribution separate.
5. **Snapshot history:** each import kept as a dated snapshot, so reports can be rebuilt for past dates.

Done when: the schema supports all five and sample data loads into three accounts (US brokerage, US bank, India NRO).

| Table | Key fields |
| --- | --- |
| `entity` | id, name, type (individual / estate / HUF / trust) |
| `residency_period` | entity\_id, country, status (US: RA / NRA; India: NR / RNOR / ROR), start, end |
| `account` | id, institution, country, type, currency, owners \[{entity\_id, pct}\] |
| `instrument` | id, ISIN, CUSIP, ticker, exchange, asset\_class, fund domicile, PFIC flag |
| `property` | id, country, location, kind, area, owners |
| `transaction` | id, account or property, date, type, qty, amount, currency, fx\_rate\_used |
| `lot` | id, instrument\_id, acquired\_on, qty, basis\_us, basis\_in, method |
| `valuation` | asset\_id, date, value, currency, source |
| `price`, `fx_rate` | series, date, value, source |
| `tax_rule` | country, rule, value, effective\_from, effective\_to |
| `input_file` | path, broker, account, type, as\_of, imported\_at, row\_count, status |

### P2 Unified ledger and CSV ingestion \[runs 16-23\]

Goal: every account in both countries flows from the input folder into the one ledger.

- Encrypted DuckDB or SQLite file with `pydantic` schemas and migrations
- Input folder layout `input/<broker>/<account>/<type>_<YYYY-MM-DD>.csv`; file types: positions, activity, cost basis by lot, realized gains
- US importers: Vanguard, Fidelity, IBKR Flex Query, generic column mapper (Empower, SoFi)
- India importers: bank statements (CSV or PDF), CAMS/KFintech CAS (`casparser`), NSDL/CDSL statements, EPFO, NPS
- Instruments keyed by ISIN with CUSIP, ticker, AMFI code, NSE/BSE symbol as aliases
- Import checks: row counts, statement-total reconciliation, duplicate detection; manual entry for illiquid assets

Done when: Vanguard, Fidelity, IBKR, one Indian bank statement, and the metals history import, and every page reads the ledger.

### P3 Consolidated multi-currency net worth \[runs 25-27\]

Goal: one trustworthy family net-worth number in either currency.

- FX table by purpose: FBIL reference rate (reporting), SBI TT buying rate (Indian tax), US Treasury reporting rates (FBAR), IRS yearly averages (US tax)
- USD/INR switch on every page
- Balance sheet with liabilities: loans, deposits held, accrued tax, deferred tax on unrealized gains in each country
- Breakdowns by country, asset class, currency, owner, liquidity (2 days, 30 days, 1 year, illiquid)
- Net-worth history split into contributions, market, and FX; after-tax net worth under current residency

Done when: net worth reconciles to the ledger in both currencies and each month's change splits into the three parts.

### P4 Performance \[runs 29, 31\]

Goal: know what each part earned, and against what.

- TWR and XIRR per account, asset class, country, owner, total; local and reporting currency
- Benchmarks: S&P 500, total US market, MSCI ACWI, US aggregate bonds, Nifty 50, Nifty 500, Indian 10-year bond, gold in USD and INR, Indian FD rate, T-bills
- Brinson attribution; income tracking and forward 12-month calendar; cost drag; real returns after US and Indian CPI

Done when: every holding shows TWR, XIRR, benchmark-relative return, and income yield over 1 month, 1, 3, 5 years, and since purchase.

### P5 Risk analytics \[runs 32-38\]

Goal: know how much could be lost, why, and in which scenarios.

- **Portfolio:** volatility, max drawdown and duration, Sharpe, Sortino, Calmar, beta, tracking error; VaR and CVaR (historical, parametric, Monte Carlo) over 1 day, 1 month, 1 year in USD and INR; correlations including crash-time jumps; Fama-French and IIM Ahmedabad factors; look-through concentration (HHI, top-10, sector, country)
- **Stress tests:** 2008, 2013 taper tantrum, 2020, 2022; US equities -35%, INR -15%, Indian real estate -20% and unsellable for 2 years, US rates +2 pp; duration and convexity for bonds, FDs, CDs
- **Currency:** USD/INR exposure vs spending currency per scenario, hedging cost, long-run INR depreciation
- **Liquidity:** lock-in ladder (FDs, PPF, EPF, NPS, 401(k)/IRA before 59 1/2, property sale times); H-1B test: job loss, 60-day grace, relocation without forced sales
- **Counterparty:** FDIC $250k, SIPC $500k incl. $250k cash, DICGC Rs 5 lakh; uninsured balances flagged
- **Profile-specific:** US estate tax above the $60k nonresident exemption (up to 40%, no India-US estate treaty) with term-life cover needed; real-estate concentration in one region; Vizag cyclone exposure vs insurance

Done when: one risk page shows VaR/CVaR, drawdown, stress losses, currency exposure by scenario, the H-1B test, and estate-tax exposure, each with inputs visible.

## Track C: decision engines

### P6 Real-estate transition analyser \[runs 50-52\]

Goal: decide property by property how to turn inherited real estate into low-maintenance income, using numbers.

| Option | What it means | Typical trade-off |
| --- | --- | --- |
| Keep, self-managed | Collect rent, handle repairs | Most effort; conflicts with the no-landlord goal |
| Keep, professionally managed | A manager handles tenants and repairs | Fee eats into a low residential yield |
| Joint development (JDA) | A builder develops plots for a share of flats or revenue | Takes years; taxed on completion (s.45(5A)) |
| Sell and reinvest in India | Proceeds into bonds, FDs, REITs, equities | Liquid; check PFIC rules while a US person |
| Sell and repatriate | Proceeds to the US via NRO (USD 1M per Indian FY) | Diversifies currency; taxed in the US while US-resident |

- 10-20 year cash flow per option: rent growth, vacancy, costs, repairs, fees, sale proceeds, tax in both countries; outputs after-tax IRR, net yield, maintenance hours, months to cash, concentration and currency effects
- Two gains per sale: US gain from date-of-death value (usually small), Indian gain from the parents' cost (often large); foreign tax credit offsets only US tax on the same income
- Indian rate options (12.5% without indexation, or 20% with indexation for qualifying pre-23 Jul 2024 property); reliefs s.54, s.54EC (Rs 50 lakh cap, 5-year lock-in), s.54F, Indian tax only
- NRI seller TDS and s.197 lower-deduction certificate; phasing across Indian FYs and US tax years under the USD 1M cap
- Agricultural land near Gudivada: rural land is not a capital asset; urban bands 2/6/8 km by municipal population (Gudivada likely 6 km; measure); NRI can sell only to resident Indian citizens; agricultural income exempt in India but taxable in the US while US-resident; lease vs sell
- Vizag apartments: tenant TDS under s.195 (about 31%) unless a lower certificate; net yield vs REITs, FDs, bonds after tax and effort; Schedule E with 30-year depreciation while US-resident
- Jewellery and silver: keep, sell, or convert vs gold ETFs; sentimental items tracked separately
- Sale proceeds hand off to P9

Done when: each property shows a ranked option table with after-tax IRR, net yield, effort, and liquidity under scenarios A and B.

### P7 Residency transition and sequencing \[runs 40-41, 47, 49\]

Goal: decide what to sell, hold, or move, and when, based on tax residency.

- Residency timeline: US substantial presence test and dual-status year; India NR/RNOR/ROR from day counts
- RNOR window calculator: usually about 2-3 tax years where foreign income isn't taxed in India
- Sequencing rules: Indian property sold while US-resident is taxed in both countries; US stocks sold after becoming a US nonresident are generally free of US capital-gains tax (unless 183+ days in the US) and, during RNOR, generally untaxed in India; Indian assets sold after becoming India-resident are taxed in India only
- No US exit tax on an H-1B; flag if a green card arrives and is held 8+ years
- Pre-departure financial checklist: harvest losses and gains, 401(k)/IRA keep or withdraw, HSA plan, brokers that restrict non-residents, W-8BEN
- Fund-domicile switch to Ireland-domiciled UCITS only after US tax residency ends (PFIC rules before that)
- US dividends as an India resident (25% treaty withholding, Form 67 credit); US retirement accounts under s.89A (now s.158 under the 2025 Act; Roth treatment uncertain)
- Social Security: 40 credits, no US-India totalisation agreement, paid abroad with withholding
- Third-country pack interface for scenario C

Done when: each scenario A-D gets a dated action list and the tax saved vs a sell-everything-now baseline.

### P8 Tax engine, US and India \[runs 39, 43-46\]

Goal: know the tax position in both countries at any time and produce clean packs for the CPA and CA.

- **US:** FIFO, specific ID, HIFO lot matching; short/long-term split; wash sales across all accounts incl. IRAs; harvesting candidates with substitutes; qualified vs ordinary dividends, 3.8% NIIT, state tax; quarterly estimates; Form 1116; FBAR, 8938, 3520, 8621 triggers; PFIC guardrail before buying Indian funds, Indian REITs/InvITs, or UCITS while a US person; Schedule E for Indian rent
- **India:** capital gains under post-23 Jul 2024 rules (listed equity STCG 20%, LTCG 12.5% above Rs 1.25 lakh; other assets 12.5% after 24 months; debt funds from 1 Apr 2023 at slab rates; 31 Jan 2018 grandfathering); NRI TDS with refund tracking; AIS and 26AS reconciliation; advance tax; Schedule FA once ROR; Form 67
- **Both:** rules as dated config per country pack; US CPA pack and Indian CA pack

Done when: year-end packs reconcile to statements, and wash sales and PFIC purchases are caught before they happen.

### P9 Advice engine and income portfolio \[runs 53, 55-57\]

Goal: turn the analysis into concrete suggestions I act on manually, and turn lump sums into low-effort income in the spending currency.

- Drift check against the investment policy; rebalancing suggestions sized to bring sleeves back in range
- Cash-flow suggestions: where dividends and new cash go; which positions to stop auto-reinvesting
- Tax-lot picks, harvesting ideas, wash-sale check, and estimated US and Indian tax per suggestion
- Targets per goal (retirement, parents' care, emergency fund, Vizag home); buckets (0-2 years cash, 3-7 bonds, 8+ equities) with refill rules
- Income ladders per currency (Treasuries, CDs, T-bills; Indian FDs, G-secs, corporate bonds, NRI-eligible only); sustainable withdrawal rate per scenario
- Currency glide path toward the spending currency; asset location across taxable, 401(k)/IRA, and Indian accounts
- Optimisers: constrained mean-variance, Black-Litterman, HRP, min-CVaR; what-if sandbox for hypothetical trades
- Advice report (HTML/PDF): actions, reasons, tax cost, data-health section, as-of stamps; no orders are ever placed

Done when: given P6 sale proceeds, the app proposes an income portfolio with yield, risk, currency mix, and effort, and shows its effect on P5 risk.

### P10 Goals, retirement, and location scenarios \[runs 58-59\]

Goal: see which futures are affordable and how sure I can be.

- Monte Carlo per scenario A-D with market, inflation, and FX paths
- Cost of living and healthcare per location (US metro, Bengaluru, Hyderabad, Delhi-NCR, Vizag, third country)
- INR depreciation and inflation gap as explicit inputs; green-card timing sensitivity (2 years, 5 years, never)
- Goal tracker; insurance needs (term life for dependants and estate-tax exposure, health cover per location)

Done when: A-D appear side by side with probability of success and required savings rate.

## Track D: operate and protect

### P11 Market data on demand \[runs 28, 61\]

- Prices pulled only when I ask: `yfinance` (US and NSE/BSE `.NS`/`.BO`), AMFI daily NAV file, goldapi.io (USD bullion), IBJA (INR gold and silver)
- Macro and FX: FRED, RBI DBIE, FBIL
- Cache with as-of labels; data-quality checks for stale prices, gaps, outliers
- Alerts shown on open: allocation drift, FD/CD maturities, uninsured deposits, moves beyond VaR
- Dual-country deadline calendar (Appendix A) and a monthly family report

Done when: a price pull refreshes every holding with its time, and the calendar shows every Appendix A deadline.

### P12 Security, privacy, and family access \[runs 16, 62\]

- Encryption at rest (SQLCipher or encrypted DuckDB), secrets in the OS keyring
- Roles: owner, spouse or sibling (view or edit), adviser (read-only export)
- Audit log of every import and edit; masking mode for screen sharing
- Emergency access instructions; 3-2-1 backups (local, external drive, encrypted cloud)

Done when: the data file is unreadable without the key and a restore from backup has been tested.

### P13 Research and platform \[run 63\]

- Jupyter notebooks on the same ledger; backtesting of allocation and rebalancing rules across both markets with FX
- Optional FastAPI backend so the interface isn't tied to Streamlit; plug-in interface for country packs and importers

## Reference

### Key thresholds (verify every year)

| Item | Value | As of |
| --- | --- | --- |
| FBAR | Foreign accounts > $10,000 at any point in the year | Not indexed |
| Form 8938 (living in the US) | Single > $50k year end or > $75k any time; MFJ > $100k / > $150k | Not indexed |
| Form 3520 | Gifts or bequests from non-US persons > $100k in a year | Not indexed |
| US estate tax, non-domiciled | $60k exemption on US-situs assets | Not indexed |
| US estate tax, domiciled | $15M per person | 2026 |
| NIIT | 3.8% above $200k single / $250k MFJ | Not indexed |
| FDIC / SIPC | $250k per depositor, bank, category / $500k incl. $250k cash | Current |
| DICGC (India) | Rs 5 lakh per depositor per bank | Since 2020 |
| India listed equity | STCG 20%; LTCG 12.5% above Rs 1.25 lakh per year | From 23 Jul 2024 |
| India other LTCG | 12.5% without indexation; 24-month holding | From 23 Jul 2024 |
| s.54EC bonds | Up to Rs 50 lakh, within 6 months, 5-year lock-in | Current |
| NRO repatriation | USD 1M per Indian financial year | Current |
| LRS (India residents) | USD 250,000 per year; 20% TCS on investment remittances above Rs 10 lakh | From 1 Apr 2025 |
| RNOR test | NR in 9 of previous 10 years, or <= 729 days in India over previous 7 years | Current |
| Urban agricultural land | 2 / 6 / 8 km bands by municipal population | Since 2013-14 |
| US remittance excise | 1% on cash-funded transfers; bank-funded exempt | From 1 Jan 2026 |
| H-1B grace period | Up to 60 days after employment ends | Current |

### Dual-country calendar

| Country | Date | Item |
| --- | --- | --- |
| US | 15 Jan | Q4 estimated tax (previous year) |
| US | 15 Apr | Form 1040, FBAR, Form 3520; Q1 estimated tax |
| US | 15 Jun | Q2 estimated tax; automatic extension if living abroad on 15 Apr |
| US | 15 Sep | Q3 estimated tax |
| US | 15 Oct | Extended 1040; FBAR automatic extension |
| India | 15 Jun / 15 Sep / 15 Dec / 15 Mar | Advance tax: 15% / 45% / 75% / 100% cumulative |
| India | 31 Jul | Return due for non-audit cases (check extensions) |
| India | Before filing | Form 67 for foreign tax credit |
| India | 31 Dec | Belated or revised return (verify under the 2025 Act) |
| India | 31 Mar | Year end: USD 1M repatriation cap and LRS reset |

Rolling: FD and CD maturities, lease renewals, property-tax dues, the 6-month s.54EC window after any property sale.

### Parked: legal and estate administration

Outside the app for now; worked through with an AP property advocate, a US estate attorney, the CA, and the CPA. These items unlock app features:

| Legal item | Unlocks |
| --- | --- |
| Date-of-death registered valuer report | P1 dual cost basis; P6 and P8 gains |
| Mutation and clear title | P6 "ready to sell" flag and time-to-sell |
| Co-heir release or partition deeds | P1 ownership percentages |
| NRO account | P2 account list; P6 repatriation path |
| Power of attorney (apostilled, stamped in India within 3 months) | P6 selling without travelling |
| Nominations and beneficiaries | P12 emergency access; P10 estate view |

Also parked: parents' and my own wills, title records (pattadar passbook, 1-B, Adangal, sale deeds, encumbrance certificates, GVMC tax records), tenant agreements, jewellery inventory, legal-heir certificate, probate or succession certificate, Form 15CA/15CB for each repatriation.

### Questions for advisers

- **US CPA:** estate-tax domicile on an H-1B; reporting an inheritance (Form 3520) and supporting date-of-death basis; Indian rental income while US-resident; which sales go before vs after departure; direct medical payments and gift tax; which Indian investments are PFICs.
- **Indian CA:** whether the Gudivada land is rural agricultural land; my cost basis for inherited property and indexation eligibility; lower-deduction certificates for rent and sale TDS; my RNOR dates; whether s.54 or s.54EC is worth it given US tax; mapping sections to the Income-tax Act, 2025.
- **AP property advocate:** registered will vs probate; mutation steps and timing; settling co-heir shares and stamp duty; buyer title checks; using a power of attorney for sale registration.
