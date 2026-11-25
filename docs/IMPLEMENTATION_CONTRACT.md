# Implementation Contract

**Status:** authoritative migration baseline
**Updated:** 25 November 2026

This document is the default source of truth for implementation decisions. It is more specific than roadmap prose and must be followed unless a task explicitly replaces it.

## 1. Product scope

Build a local-first, read-only advisory system for cross-border personal and family wealth. The app must:

1. Aggregate US and Indian financial positions in one ledger.
2. Preserve native currency and tax-lot history.
3. Calculate net worth, performance, risk, tax exposure, residency implications, and actionable recommendations.
4. Keep the current Streamlit UI visually intact unless a task is explicitly labelled UI redesign.
5. Never place trades, move cash, or execute financial transactions.
6. Never send financial statements or account identifiers to external services.

Live price and FX providers may receive only symbols and requested dates. API keys remain local.

## 2. Data truth hierarchy

For every reported value, source and as-of date must be stored or derivable.

Priority by purpose:

1. Imported position statement or manually entered ledger row
2. Dated price/FX table
3. Cached live price
4. Explicit estimate or model input

Never silently replace a missing value with a guessed market value. The UI must distinguish:

- zero
- unavailable
- stale
- estimated
- computed
- conflicting

## 3. Existing app preservation

The existing app is a compatibility baseline, not a blank canvas.

Preserve until an approved task replaces it:

- page filenames and rendered routes
- home page and left navigation order
- titles and icons
- page-level sidebar controls
- tab names and source order
- widget labels, defaults, options, minimum/maximum/step values
- 2/3/4-column structures
- metric labels and currency formats
- table headers and display formatting
- chart types and meaningful chart labels/colors
- footer/privacy text
- empty, warning, error, and data-source states

Use `docs/UI_BASELINE.md`, `docs/UI_CAPTURE.md`, `docs/Prompts/06_ui_preservation_prompt.md`, and browser screenshots as the UI evidence chain.

## 4. Architecture constraints

### Source of truth

Every page eventually reads from one local ledger. Pages must not read independent broker CSV formats.

During migration, adapters may translate legacy CSV formats, but no page may contain broker-specific parsing after P2.

### Storage

Use one encrypted local store, initially DuckDB or SQLite plus migration tooling.

Required logical entities:

- entity
- residency_period
- account
- instrument
- property
- transaction
- lot
- valuation
- price
- fx_rate
- tax_rule
- input_file
- audit_event

### Import lifecycle

An import must:

1. register the source file and SHA-256 hash
2. identify account and import type
3. validate required columns
4. count input rows
5. normalize into typed domain objects
6. detect duplicate rows
7. reconcile totals against source/statement totals
8. write atomically
9. store success/failure status and row counts
10. expose as-of data and stale warnings

An import is complete only if reconciliation discrepancies are zero or explicitly approved in the import record.

### Currencies

Store source amount and source currency. Store a dated FX rate used for conversion. Do not silently overwrite the native amount.

A report must show:

- reporting currency
- source currency
- FX date
- FX source
- conversion purpose
- unrounded underlying values where applicable

## 5. Performance contract

The system must support these definitions:

- TWR: excludes the effect of external cash flows
- XIRR/MWR: includes timing and size of external cash flows
- Returns: exclude currency effects unless explicitly stated as a reporting-currency result
- Income: separate dividend, interest, rent, coupon, and withholding components
- Since-purchase: use the earliest valid lot/cost input and disclose gaps

A result without the basis is incomplete.

## 6. Risk contract

The risk engine must expose inputs used. It must not display VaR/CVaR, stress losses, or probability of success without:

- as-of date
- horizon
- source assumptions
- currency
- confidence level for VaR/CVaR
- model/method
- scenario shock values
- number of observations or simulations

Monte Carlo probability is a model result, not a guaranteed outcome.

## 7. Tax contract

Tax rules are dated configuration, never Python constants in tax calculations.

A rule record must contain:

- country
- rule name
- value or threshold
- effective start date
- effective end date
- source URL/document
- source as-of date
- review status
- legal caveat

An answer must identify which tax rule generated it and the date range under which it applied.

No tax feature may claim final professional advice. Ambiguous treatments must stop with a named human-review item.

## 8. Security contract

The repository must not contain:

- account statements
- full account numbers
- brokerage downloads
- tax documents
- passwords or API keys
- real balances or transaction histories
- personal property address records

`data/` and `input/` are local-only except explicit synthetic files under `data/samples/`.

Encryption at rest is required before real financial data is imported. Development with real data must remain opt-in and local-only.

## 9. Testing contract

Every implementation task must define tests before implementation or while implementing. Tests must prove behavior, not merely that a function was called.

Required test categories:

- unit calculations with hand-derived expected values
- import fixtures with known totals
- duplicate detection
- reconciliation discrepancy handling
- stale/missing-data behavior
- FX and reporting-currency conversion
- tax rule effective-dating
- page render smoke tests
- synthetic UI baseline tests
- regression tests for known bugs
- no-network tests

Live APIs must be mocked. No test may read or write `data/` outside `data/samples/`.

## 10. Definition of done

A task is done only when:

1. all task acceptance tests pass
2. `ruff check .` passes or the task includes an exact resolved lint delta
3. `pytest` passes
4. no real-data files or secrets enter the diff
5. UI behavior is unchanged unless explicitly approved
6. as-of/source information is visible or derivable for financial outputs
7. known limits and assumptions are documented
8. no unrelated task is started
