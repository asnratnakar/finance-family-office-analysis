# Backlog

**Status:** implementation queue

**Current Focus**
- Run 1: Repo hygiene (In review)
- Run 2: Replace `test_functions.py` with pytest utilities tests (In review)
- Run 3: Fix Bank Accounts calculations and sorting (Not started)

Task execution rules are in `TASK_EXECUTION_CONTRACT.md`. This file is the machine-readable work queue mirrored from `WEEKLY_BACKLOG.md`.

| Run | Phase | Task | Depends on | Status |
| --- | --- | --- | --- | --- |
| 1 | P0 | Repo hygiene: ignore real data and keys; keyring or `.env`; pin requirements; ruff/pre-commit; synthetic CSVs | - | Done |
| 2 | P0 | Replace `test_functions.py` with pytest tests for loan, metals, and Vanguard utilities | 1 | Done |
| 3 | P0 | Fix Bank Accounts: ending balance, month/year sorting, and CD APY compounding | 2 | In review |
| 4 | P0 | Fix metals no-price behavior, cache/API time labels, and Vanguard date sorting | 2 | Not started |
| 5 | P0 | Merge duplicate portfolio utilities into a broker-neutral module | 2 | Not started |
| 6 | - | BUFFER: lint, tests, TODOs | - | Not started |
| 7 | P0 | Remove empty pages, replace Retirement page, fix typo, refresh README | 5 | Not started |
| 8 | P1 | Input layout, account registry, and manual CSV templates | 7 | Not started |
| 9 | P1 | Family asset register | 8 | Not started |
| 10 | P1 | Net-worth views and valuation history | 9 | Not started |
| 11 | P1 | Dual cost bases and parents' care runway | 9 | Not started |
| 12 | - | BUFFER: lint, tests, TODOs | - | Not started |
| 13 | P1 | Remittance, gift, and trigger tracking | 10 | Not started |
| 14 | Data health | Freshness, missing data, update checklist | 8 | Not started |
| 15 | Foundations | Ledger schema and migrations | 14 | Not started |
| 16 | P12 | Encryption at rest | 15 | Not started |
| 17 | P2 | Import framework and Vanguard importer | 16 | Not started |
| 18 | - | BUFFER: lint, tests, TODOs | - | Not started |
| 19 | P2 | Fidelity importer | 17 | Not started |
| 20 | P2 | IBKR importer | 17 | Not started |
| 21 | P2 | Generic CSV mapper | 17 | Not started |
| 22 | P2 | India bank/CAMS/KFintech importers | 17 | Not started |
| 23 | P2 | Existing pages read from ledger | 19-22 | Not started |
| 24 | - | BUFFER: lint, tests, TODOs | - | Not started |
| 25 | P3 | FX table and currency switch | 23 | Not started |
| 26 | P3 | Consolidated net worth | 25 | Not started |
| 27 | P3 | Net-worth history split | 26 | Not started |
| 28 | P11 | On-demand live prices | 23 | Not started |
| 29 | P4 | TWR and XIRR | 27 | Not started |
| 30 | - | BUFFER: lint, tests, TODOs | - | Not started |
| 31 | P4 | Benchmarks and income calendar | 29 | Not started |
| 32 | P5 | Risk core | 29 | Not started |
| 33 | P5 | Look-through concentration | 32 | Not started |
| 34 | P5 | Correlation and stress replay | 32 | Not started |
| 35 | P5 | Hypothetical stress scenarios | 34 | Not started |
| 36 | - | BUFFER: lint, tests, TODOs | - | Not started |
| 37 | P5 | Liquidity and insurance checks | 26 | Not started |
| 38 | P5 | Estate risk and assembled risk page | 35,37 | Not started |
| 39 | P8 | Dated country tax-rule packs | 15 | Not started |
| 40 | P7 | Residency timeline tests | 39 | Not started |
| 41 | P7 | RNOR window calculator | 40 | Not started |
| 42 | - | BUFFER: lint, tests, TODOs | - | Not started |
| 43 | P8 | US lot matching and wash sales | 39 | Not started |
| 44 | P8 | Tax-loss harvesting guardrails | 43 | Not started |
| 45 | P8 | India capital gains and NRI TDS | 39 | Not started |
| 46 | P8 | US and India year-end packs | 43,45 | Not started |
| 47 | P7 | Sale-sequencing optimizer | 41,46 | Not started |
| 48 | - | BUFFER: lint, tests, TODOs | - | Not started |
| 49 | P7 | UCITS and retirement-account residency planner | 47 | Not started |
| 50 | P6 | Real-estate cash-flow model | 26 | Not started |
| 51 | P6 | Dual-basis sale gains and Indian reliefs | 50,41 | Not started |
| 52 | P6 | Agricultural land, apartments, and jewellery options | 51 | Not started |
| 53 | P9 | Advice engine v1 | 43,38 | Not started |
| 54 | - | BUFFER: lint, tests, TODOs | - | Not started |
| 55 | P9 | Income engineering | 53 | Not started |
| 56 | P9 | Optimizers and what-if sandbox | 55 | Not started |
| 57 | P9 | Advice report | 53,14 | Not started |
| 58 | P10 | Monte Carlo retirement | 47 | Not started |
| 59 | P10 | Location, green-card, and goal planning | 58 | Not started |
| 60 | - | BUFFER: lint, tests, TODOs | - | Not started |
| 61 | P11 | Deadline calendar and monthly family report | 57 | Not started |
| 62 | P12 | Encrypted backups, masking, and audit log | 16 | Not started |
| 63 | P13 | Jupyter and cross-market backtesting | 29 | Not started |
