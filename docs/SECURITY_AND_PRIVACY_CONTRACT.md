# Security and Privacy Contract

**Status:** mandatory before real data is imported

## Secret and data boundaries

Real financial data and secrets must remain outside version control.

Never commit:

- CSV statements
- PDFs of statements
- tax forms
- account numbers
- card numbers
- API keys
- environment files with real values
- names paired with balances or holdings
- screenshots containing real values
- broker error logs containing account identifiers

## Data folders

- `data/`: local real-data directory; no personal CSV or statement should be committed
- `input/`: local real imports; ignored
- `tests/fixtures/`: optional synthetic, non-personal fixture files with no real identifiers or balances

## Secret storage

Preferred:

1. OS keyring
2. OS environment variable
3. `.env.local`, ignored and never committed
4. `.env.example`, placeholders only

No module should print or log a secret value.

## Encryption

Before real data import:

- enable encryption at rest
- use a non-derivable OS-managed key if feasible
- test unreadable behavior without the key
- test restore from encrypted backup
- test backup integrity and file permissions

Do not describe encryption as complete until a restore test is performed.

## External APIs

External calls may receive:

- ticker/symbol
- metal symbol
- currency pair
- date range needed for requested public market data

External calls must not receive:

- account numbers
- owner names
- quantities
- cost basis
- tax ID
- transaction history
- portfolio composition as account data
- Indian/US property addresses

## Logging

Logs must redact:

- paths containing user names only if they reveal a personal machine location
- account numbers
- tax IDs
- balances
- API keys
- transaction descriptions containing personal names

Audit logs are financial events, not debug logs, and must themselves be treated as sensitive.

## Sharing

Adviser exports must:

- require an explicit export action
- support masking
- exclude secrets
- exclude full account numbers
- include as-of and source metadata
- be reproducible only from the local ledger

## Backups

Apply 3-2-1:

- local copy
- external copy
- encrypted cloud or off-site copy

Every backup process must include:

- backup frequency
- retention
- encryption
- restore test
- key recovery plan
- audit of backup failure
