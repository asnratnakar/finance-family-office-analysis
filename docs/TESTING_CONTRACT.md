# Testing Contract

**Status:** mandatory quality baseline

## Test runner

- Framework: pytest
- Lint/format: ruff
- Hooks: pre-commit
- Browser: Playwright only for UI baseline/diff when available

## Test isolation

Tests must:

- use fixed synthetic fixtures
- not read or write real content under `data/` or `input/`
- not write real input folders
- not make live API calls
- not require account credentials
- not depend on machine-specific absolute paths
- not depend on wall-clock time without injection

## Required test types

### Domain calculations

Use hand-calculated fixtures and edge cases:

- loan monthly payment
- amortization final balance
- loan comparison ordering
- metals cost/market/gain
- unavailable metal price
- CD maturity and compounding
- PV/FV compounding
- FX conversion and inverse
- lot matching
- TWR
- XIRR
- VaR/CVaR with fixed seed or fixed observations

### Imports

For every importer:

- valid row import
- missing required column
- extra column
- duplicate row
- empty file
- malformed number/date
- wrong encoding/delimiter
- statement-total mismatch
- duplicate file hash
- import rollback on failure

### Storage

- migration up/down
- required foreign keys
- no float money values
- encrypted-at-rest behavior
- atomic write
- audit event written
- restore from backup behavior

### UI

- page renders
- exact title and key labels exist
- default values match
- tab count/order match
- sidebar control options match
- table headers match
- chart container renders
- no real data path executes
- empty/error states render

### Security

- real-data patterns are ignored
- `.env` and key files are ignored
- synthetic in-memory fixtures are required
- secret values are never printed/logged
- API key is not included in request payload except authorization headers

## Test naming

Use behavior-focused names:

```text
test_amortization_final_balance_is_zero()
test_duplicate_vanguard_rows_are_rejected()
test_missing_fx_rate_is_reported_not_guessed()
test_bank_account_page_has_expected_default_metrics()
```

Avoid tests that only assert mocks were called.

## Failure rules

- a failing test must state the observed and expected value
- currency results must state currency and FX source
- a test may not pass by rounding away a reconciliation difference
- no live network call may be wrapped with a permissive retry that makes tests nondeterministic

## Coverage priority

Highest:

1. money and lot calculations
2. import reconciliation
3. duplicate and stale data behavior
4. tax effective-dating
5. security and secret handling
6. UI labels/defaults/page smoke tests

Lower but still required:

- chart code
- static content modules
- cosmetic page layout
