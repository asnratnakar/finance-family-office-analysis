# Weekly backlog

**Status:** implementation queue

One row is one weekly run: 53 tasks plus 10 buffer runs, about 63 weeks (roughly 14 months). The scheduled run takes the first `Not started` row whose dependencies are `Done`; every 6th run is a `BUFFER` for fixing tests, lint, and TODOs.

> **Mandatory execution rules:** Read `TASK_EXECUTION_CONTRACT.md`, `IMPLEMENTATION_CONTRACT.md`, `DATA_CONTRACT.md`, and UI contracts before implementation. One run implements one row only. `In review` means implementation and verification are complete but not merged. `Blocked` means implementation stopped with a written blocker. `Done` means the user reviewed and merged it.

- Sizes assume one Claude Code session per task. If a run comes back Blocked for size, split the row in two rather than skipping it.
- If the inheritance decision comes first, move runs 50-52 (real-estate analyser) right after run 14, with a hand-entered residency assumption, and rebuild them after run 41.
- If the move to India is set sooner, pull runs 40-41 and 47 (residency and sale sequencing) forward.
- This tab is the planning copy; `docs/BACKLOG.md` in the repo is the copy the weekly run reads and updates.

## Track A: foundations and family balance sheet (runs 1-14)

| Run | Phase | Task | Depends on | Done when | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | P0 | Repo hygiene: `.gitignore` for `data/`, `input/`, keys; keys to keyring or `.env`; pin `requirements.txt` (add `networkx`, `requests`); `ruff` + `pre-commit`; synthetic CSVs in `data/samples/` | - | `git check-ignore` covers keys and data; fresh install runs every page on samples | In review |
| 2 | P0 | Replace `test_functions.py` with `pytest` tests for `utils/` (loan, metals, Vanguard calc) on fixed sample CSVs | 1 | `pytest` passes with known expected outputs | In review |
| 3 | P0 | Fix Bank Accounts: `Ending Balance` column, month+year sorting, APY compounding for CDs | 2 | Page loads; tests cover each fix | Not started |
| 4 | P0 | Fix metals (no-price valuation, cached API call, time labels) and Vanguard glob/filename-date sort bugs | 2 | Tests reproduce each bug and pass after the fix | Not started |
| 5 | P0 | Merge `utils/portfolio.py` into one broker-neutral portfolio module | 2 | No duplicated code; existing tests pass | Not started |
| 6 | - | BUFFER | - | All tests and lint green | Not started |
| 7 | P0 | Remove empty pages, replace mislabelled Retirement page, fix typo, refresh README, move `debug_quotes.py` to `scripts/` | 5 | Every page loads on samples; README matches the app | Not started |
| 8 | P1 | Input folder layout, account registry (`accounts.yaml`), manual CSV templates (property, jewellery, bank, 401(k)) | 7 | Template files validate; registry lists every account | Not started |
| 9 | P1 | Family asset register page: land, plots, apartments (NOI, net yield), jewellery (IBJA value minus making loss), co-ownership % | 8 | Page shows every asset with value and yield from templates | Not started |
| 10 | P1 | Net-worth views: mine, parents', my expected share, in USD and INR (manual FX for now); valuation history with source | 9 | Totals reconcile to templates in both currencies | Not started |
| 11 | P1 | Dual cost basis fields (US date-of-death FMV, India original cost or 2001 FMV); parents' care cash-flow forecast and runway | 9 | Both bases stored per asset; runway in months shown | Not started |
| 12 | - | BUFFER | - | All tests and lint green | Not started |
| 13 | P1 | Remittance ledger (true cost vs mid-market), gift tracking, trigger flags (Form 3520, NRO USD 1M cap, FBAR/8938) | 10 | Each trigger fires on a sample that crosses it | Not started |
| 14 | Data health | Freshness checker (6-month stale flag, 30-day notice for positions), missing-data checks, update checklist on every page | 8 | Aging or deleting a sample file produces the right warning | Not started |

## Track B: core platform (runs 15-38)

| Run | Phase | Task | Depends on | Done when | Status |
| --- | --- | --- | --- | --- | --- |
| 15 | Foundations | Ledger schema in DuckDB or SQLite with `pydantic` models: entity, residency\_period, account, instrument, lot, transaction, valuation, price, fx\_rate, tax\_rule; migrations | 14 | Schema supports all five foundation capabilities; sample data loads into 3 accounts | Not started |
| 16 | P12 | Encryption at rest (SQLCipher or encrypted DuckDB), key in OS keyring | 15 | Data file unreadable without the key | Not started |
| 17 | P2 | Importer framework (row counts, statement-total reconciliation, duplicate detection) + Vanguard importer into the ledger | 16 | Vanguard samples import; totals reconcile | Not started |
| 18 | - | BUFFER | - | All tests and lint green | Not started |
| 19 | P2 | Fidelity importer: positions, activity, cost basis | 17 | Fidelity samples import and reconcile | Not started |
| 20 | P2 | IBKR Flex Query importer: positions, trades, FX conversions | 17 | IBKR samples import; FX conversions recorded | Not started |
| 21 | P2 | Generic CSV column mapper (Empower, SoFi, any broker) + manual-template importer | 17 | A new broker maps with a config file, no code | Not started |
| 22 | P2 | India importers: NRO/NRE bank statement CSV, CAMS/KFintech CAS via `casparser` | 17 | Indian samples import in INR | Not started |
| 23 | P2 | Existing pages and the P1 register read from the ledger; retire per-page CSV formats | 19-22 | No page reads its own CSV | Not started |
| 24 | - | BUFFER | - | All tests and lint green | Not started |
| 25 | P3 | FX table (FBIL, SBI TT, US Treasury reporting rates, IRS averages) loaded from downloaded files; USD/INR switch on every page | 23 | Every page switches currency; rates dated by source | Not started |
| 26 | P3 | Consolidated net worth: assets minus liabilities, by country, asset class, currency, owner, liquidity | 25 | Totals reconcile to the ledger in both currencies | Not started |
| 27 | P3 | Net-worth history split into contributions, market, and FX; after-tax net worth under current residency | 26 | Monthly change splits cleanly into the three parts | Not started |
| 28 | P11 | On-demand live prices (yfinance or Finnhub, AMFI NAV, IBJA, goldapi) with cache and as-of labels; mocked in tests | 23 | Pull is optional; every price shows its time | Not started |
| 29 | P4 | TWR and XIRR (`pyxirr`) per account, asset class, owner, total; local and reporting currency | 27 | Matches hand-calculated sample returns | Not started |
| 30 | - | BUFFER | - | All tests and lint green | Not started |
| 31 | P4 | Benchmarks (S&P 500, ACWI, Nifty 50, gold, FD rate), income tracking, forward 12-month income calendar | 29 | Each holding shows return vs benchmark and income yield | Not started |
| 32 | P5 | Risk core: volatility, drawdown, Sharpe, Sortino, beta; historical and parametric VaR/CVaR in USD and INR | 29 | Matches `quantstats` on a sample series | Not started |
| 33 | P5 | Look-through concentration from issuer holdings files: HHI, top-10 names, sector, country | 32 | ETF overlap shows true per-company exposure | Not started |
| 34 | P5 | Correlation matrix, rolling correlations; historical stress replays (2008, 2013 taper, 2020, 2022) | 32 | Stress losses shown for the current portfolio | Not started |
| 35 | P5 | Hypothetical stresses (US equities -35%, INR -15%, Indian RE -20% and unsellable 2 years, rates +2 pp); rate sensitivity; currency exposure by scenario | 34 | Each scenario shows loss in USD and INR | Not started |
| 36 | - | BUFFER | - | All tests and lint green | Not started |
| 37 | P5 | Liquidity lock-in ladder, H-1B 60-day liquidity stress test, deposit-insurance check (FDIC, SIPC, DICGC) | 26 | Uninsured balances flagged; runway shown | Not started |
| 38 | P5 | US estate-tax exposure ($60k nonresident exemption), real-estate concentration, Vizag cyclone cover check; assemble risk page | 35, 37 | Risk page shows every metric with inputs visible | Not started |

## Track C: decision engines (runs 39-59)

| Run | Phase | Task | Depends on | Done when | Status |
| --- | --- | --- | --- | --- | --- |
| 39 | P8 | Country-pack framework: dated `tax_rule` config; US pack; India pack with a 1961-to-2025 Act section map | 15 | Rules load by date; changing a date changes the result | Not started |
| 40 | P7 | Residency timeline: US substantial presence test and dual-status year; India NR/RNOR/ROR from day counts | 39 | Sample travel histories give the expected statuses | Not started |
| 41 | P7 | RNOR window calculator and residency input page | 40 | Shows RNOR dates and which income the window covers | Not started |
| 42 | - | BUFFER | - | All tests and lint green | Not started |
| 43 | P8 | US tax: lot matching (FIFO, specific ID, HIFO), short/long-term split, wash-sale detection across all accounts incl. IRAs | 39 | Sample wash sales caught; gains match hand calculation | Not started |
| 44 | P8 | Tax-loss harvesting candidates with substitutes; PFIC guardrail; qualified dividends and NIIT | 43 | PFIC purchase warned before it happens | Not started |
| 45 | P8 | India capital gains (post-23 Jul 2024 rules, 31 Jan 2018 grandfathering), NRI TDS tracking, Schedule FA data | 39 | Sample gains match hand calculation | Not started |
| 46 | P8 | Year-end packs: US CPA pack and Indian CA pack | 43, 45 | Packs reconcile to sample statements | Not started |
| 47 | P7 | Sale-sequencing optimiser v1: dated action list per scenario vs a sell-everything-now baseline | 41, 46 | Each scenario lists actions and tax saved | Not started |
| 48 | - | BUFFER | - | All tests and lint green | Not started |
| 49 | P7 | UCITS switch planner (blocked until US nonresident), US dividends and retirement accounts as an India resident (s.89A, now s.158) | 47 | Switch only suggested after the nonresident date | Not started |
| 50 | P6 | Real-estate cash-flow model, 10-20 years, per option: keep self-managed, keep managed, JDA, sell and reinvest in India, sell and repatriate | 26 | After-tax IRR, net yield, effort hours per option | Not started |
| 51 | P6 | Two gains per sale (US date-of-death vs India original cost), Indian rate options, s.54/54EC/54F reliefs, TDS and s.197, phasing under the USD 1M cap | 50, 41 | Both gains shown; phasing respects the cap | Not started |
| 52 | P6 | Agricultural land (capital-asset distance test, buyer limits, lease vs sell), apartments (s.195 TDS, yield vs REITs and bonds), jewellery keep/sell | 51 | Each property shows a ranked option table for scenarios A and B | Not started |
| 53 | P9 | Advice engine v1: drift vs policy, rebalancing and cash-flow suggestions, tax-lot picks, wash-sale check | 43, 38 | Suggestions list reasons and estimated tax | Not started |
| 54 | - | BUFFER | - | All tests and lint green | Not started |
| 55 | P9 | Income engineering: bucket strategy, income ladders per currency, currency glide path, asset location | 53 | Proposed portfolio shows yield, risk, currency mix | Not started |
| 56 | P9 | Optimisers (HRP, min-CVaR via `riskfolio-lib`) and the what-if sandbox | 55 | A hypothetical trade shows risk, income, tax effect | Not started |
| 57 | P9 | Advice report (HTML/PDF): actions, reasons, tax cost, data-health section, as-of stamps | 53, 14 | One-click report from sample data | Not started |
| 58 | P10 | Monte Carlo retirement per scenario A-D with market, inflation, and FX paths | 47 | Probability of success per scenario | Not started |
| 59 | P10 | Location costs, green-card timing sensitivity, goal tracker, insurance needs; scenario comparison page | 58 | A-D side by side with required savings rate | Not started |

## Track D: operate and protect (runs 60-63)

| Run | Phase | Task | Depends on | Done when | Status |
| --- | --- | --- | --- | --- | --- |
| 60 | - | BUFFER | - | All tests and lint green | Not started |
| 61 | P11 | Dual-country deadline calendar with reminders; monthly family report (net worth, income, risk, actions due) | 57 | Every Appendix A deadline appears; report builds from samples | Not started |
| 62 | P12 | 3-2-1 encrypted backups with a tested restore, masking mode for screen sharing, audit log of every import and edit | 16 | Restore from backup tested; masking hides every amount | Not started |
| 63 | P13 | Jupyter notebooks on the same ledger; backtesting of allocation and rebalancing rules across both markets with FX | 29 | A notebook reproduces a dashboard number | Not started |
