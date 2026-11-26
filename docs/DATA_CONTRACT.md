# Data Contract

**Status:** authoritative
**Scope:** every broker import, manual entry, price, FX, and ledger result

## 1. File placement

Local real files:

```text
input/
  brokers/<broker>/<account>/
  manual/
  bank/
  estate/
  tax/
```

Synthetic repository fixtures:

```text
tests/fixtures/
```

Real personal data must never exist in repository test fixtures.

## 2. Input file naming

Recommended:

```text
<input-type>_<account-id>_<as-of-YYYY-MM-DD>_<source-extension>.<ext>
```

Examples:

```text
positions_US_BROKER001_2026-11-14.csv
activity_US_BROKER001_2026-10-31.csv
cost_basis_US_BROKER001_2026-10-31.csv
bank_statement_IN_NRO001_2026-09-30.csv
```

An imported file record must store:

- original file name
- sanitized relative path
- account ID
- broker/source
- import type
- as-of date
- import timestamp
- file SHA-256
- encoding
- delimiter
- row count
- accepted row count
- rejected row count
- duplicate row count
- reconciliation status
- reconciliation difference
- validation errors

## 3. Normalization rules

- Preserve source-native number types before conversion.
- Dates are ISO 8601 `YYYY-MM-DD` internally.
- Times are timezone-aware UTC in storage/export metadata.
- Decimals use `Decimal`, never float for money or basis calculations.
- Strings are trimmed and normalized according to source rules.
- Currency codes use ISO 4217 uppercase.
- Instrument identifiers are not assumed unique across exchanges.
- A missing/unknown CUSIP, ISIN, ticker, or AMFI code must remain unresolved, not guessed.
- Negative and positive quantity/cash semantics must follow transaction type.

## 4. Canonical entity types

- individual
- spouse
- parent
- estate
- HUF
- trust
- LLC
- co-owner

## 5. Account types

US examples:

- taxable_brokerage
- 401k
- traditional_ira
- roth_ira
- hsa
- 529
- bank_checking
- bank_savings
- cd
- bullion

India examples:

- NRE
- NRO
- FCNR_B
- resident_savings
- FD
- demat
- mutual_fund
- PPF
- EPF
- NPS
- SGB
- locker

## 6. Canonical transaction types

- buy
- sell
- dividend
- interest
- coupon
- fee
- split
- reverse_split
- bonus
- merger
- spin_off
- rights_issue
- transfer_in
- transfer_out
- fx_conversion
- remittance
- rent_received
- rent_deposit_held
- property_expense
- tax_withheld
- contribution
- withdrawal

Every transaction stores:

- transaction ID
- account or property ID
- entity ownership context
- date
- type
- instrument/property if applicable
- quantity
- unit/native amount
- source currency
- FX rate ID when conversion applies
- fee
- withholding
- tax lot references for sell/buy allocations
- source file row reference
- as-of date
- notes

## 7. Lot contract

A lot must store:

- instrument
- account
- entity ownership context
- acquired date
- original quantity
- remaining quantity
- US basis in USD or source currency plus conversion evidence
- Indian basis in INR or source currency plus conversion evidence
- lot-matching method
- inherited status
- date-of-death FMV if inheritance applies
- inherited from
- acquisition type
- source transaction IDs
- as-of date

Lot matching is explicit. Default matching method must be visible and not silently assumed.

## 8. Valuation contract

An asset valuation must identify:

- asset ID
- date
- value
- currency
- source: market, registered_valuer, broker, government_guideline, estimate
- source URL/document
- confidence
- owner shares if applicable
- stale flag

## 9. Price contract

A price record must identify:

- instrument or metal
- date/time
- currency
- close/spot/bid/ask value
- provider
- provider URL or API endpoint
- fetched timestamp
- cache status
- timezone
- fallback status

## 10. FX contract

An FX record must identify:

- base currency
- quote currency
- date
- rate
- purpose
- provider/source
- source URL/file
- source as-of date
- inverse relationship

Purpose examples:

- general_reporting
- indian_tax_rule_115
- fbar_year_end
- irs_annual_average
- remittance_effective_rate

## 11. Tax-rule contract

See `IMPLEMENTATION_CONTRACT.md` section 7.

## 12. Reconciliation

Reconciling import against statement totals must report:

- source expected total
- ledger computed total
- absolute difference
- percentage difference
- tolerance used
- discrepancy by row/account/category
- unresolved status

A reconciliation can pass only when:

- difference is within configured tolerance, or
- the import record explicitly records a reviewed and approved exception.
