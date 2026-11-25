# Legacy-to-New Migration Map

**Status:** implementation map

## Principle

Preserve the UI first, migrate data behind it, then replace legacy pages only when explicitly scheduled.

## Entry point

| Legacy | Target | Migration rule |
|---|---|---|
| `PersonalPortfolioAnalysis.py` | `app.py` or retained entry | Keep the exact home UI until task explicitly renames it |
| `pages/*.py` | Streamlit route pages | Preserve route filenames and menu order during migration |
| `utils/*.py` | domain modules or adapter modules | Remove duplication after tests |
| `data/` | `input/` + encrypted ledger | Real files never enter git |

## Page migration

| Legacy page | Preserve | First implementation target |
|---|---|---|
| Home | welcome copy, title/icon, footer | no UI redesign in data tasks |
| Bank Accounts | all headings, tables, chart, PV/FV controls | ledger-backed account snapshots and tests |
| Real Estate | empty state only | P1 family asset register |
| Retirement | do not preserve mislabelled behavior | replace with retirement view |
| Market Investments | title, metrics, pies, trends, top holdings | Vanguard/other-broker ledger importer |
| Metals | all controls, procurement/divestment sections | preserve UI with data adapter and live-price cache |
| Commodities | none | remove or implement separately |
| Forex | none | remove or implement separately |
| Life Insurance | none | remove or implement separately |
| Loan | exact tabs/widgets/charts | refactor formulas behind tests, no UI redesign |
| Knowledge Base | tabs and module layout | extract content into stable modules only |
| Family Office | exact static network/legend | preserve until a data-driven replacement is approved |

## Utility migration

| Legacy utility | Target | Done condition |
|---|---|---|
| `utils/loan.py` | `domain/loans.py` or existing utility | Hand-calculated tests and no UI formula duplication |
| `utils/metals.py` | `domain/metals.py` | Missing-price tests and unified valuation behavior |
| `utils/portfolio_calc_van.py` | `adapters/vanguard.py` + ledger importer | Lot/summary sample import reconciles |
| `utils/portfolio.py` | remove or adapter only | no duplicated portfolio logic |
| `utils/keyManagement.py` | `infra/secrets.py` | OS keyring/env fallback policy tested |

## Legacy data migration

| Legacy source | Target importer/adapter | Required evidence |
|---|---|---|
| Vanguard cost-basis CSV | Vanguard lot importer | lot count, quantity, basis, market value reconcile |
| Vanguard summary CSV | snapshot/import adapter | report date, symbol, cost, market value reconcile |
| Metals transaction history | transactions and lot adapter | quantity and cost reconcile |
| Metals spot price | price table | date, metal, source, currency reconcile |
| Gold/silver advisory | local reference data | advisor output remains unchanged initially |
| Bank CSVs | bank importer/manual templates | balances, month/year, CD principal/term/APY reconcile |
| Portfolio uploaded CSV | generic CSV adapter | required columns and invalid-row behavior |

## UI migration compatibility rule

For each migrated page:

1. create synthetic fixture
2. capture baseline screenshot
3. introduce adapter/ledger read behind existing widget code
4. rerun page
5. compare screenshot
6. report only approved visual differences

Do not rewrite all pages to a new component framework in the same task as ledger migration.
