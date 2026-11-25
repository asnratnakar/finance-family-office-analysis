# Task Execution Contract

**Applies to:** Claude Code, Copilot, scripts, and manual implementation

## Task source

The backlog is the work queue. `docs/BACKLOG.md` or `docs/WEEKLY_BACKLOG.md` is authoritative for dependencies and status.

Tasks are executed sequentially unless a documented dependency or explicit instruction says otherwise.

## Before starting

A task owner must:

1. Read `CLAUDE.md` if present.
2. Read `IMPLEMENTATION_CONTRACT.md`.
3. Read `DATA_CONTRACT.md` when data/import/storage is involved.
4. Read `UI_BASELINE.md` and `06_ui_preservation_prompt.md` when UI is involved.
5. Read the exact backlog row and dependencies.
6. Confirm every dependency is `Done`.
7. Check git status.
8. Confirm branch policy.

Do not start from memory. Do not infer unclear requirements.

## One task per run

Implement only the selected row. It is prohibited to:

- start the next backlog task
- bundle unrelated fixes
- change UI styling incidentally
- fix another bug found during review
- add an unrequested dependency
- merge, squash, rebase, reset, or amend without explicit instruction

A related bug may be documented as follow-up only.

## UI tasks

Before editing UI:

- capture baseline state
- list every existing title, label, control, default, chart, table, and status state
- preserve exact layout unless the task explicitly approves a redesign
- add synthetic sample data before removing legacy data paths
- capture migrated screenshots
- report visual differences

## Data tasks

Before editing data logic:

- identify source files and schema
- provide a synthetic fixture
- state expected values
- prove reconciliation
- state missing-data behavior
- state stale-data behavior
- state currency behavior
- state failure behavior
- verify no real-data path executes in tests

## Tax and advice tasks

Stop and create a review item instead of guessing when:

- source law is dated or uncertain
- a rule's interaction is unclear
- residency facts are incomplete
- foreign tax credit methodology is disputed
- inheritance basis is incomplete
- a tax threshold is not locally sourced

No open question may be converted silently into a hard-coded assumption.

## Change limits

Do not:

- read or write personal data
- commit `.env`, `.keys`, statements, exports, or tax documents
- make live external calls in tests
- change a dependency without pinning it
- alter global styling during a backend task
- delete a page with no completed replacement task
- replace a bugfix with a workaround without tests

## Verification

Minimum for every task:

```powershell
ruff check .
pytest
streamlit run PersonalPortfolioAnalysis.py --server.headless true
```

Additional verification:

- `git check-ignore` for real data/secrets
- `git diff --check`
- UI screenshot comparison for UI tasks
- sample import and reconciliation for data tasks
- hand-calculated result test for calculations

No task is complete if the only validation is that the app starts.

## Failure handling

Maximum fix attempts: 3.

After 3 failures:

- stop implementation
- record the first failing result
- record the root-cause hypothesis
- document what was tried
- mark the task `Blocked`
- do not silently continue another task

## Status values

- `Not started`: dependency known; no implementation began
- `In review`: implementation complete and checks run
- `Blocked`: cannot progress; blocker documented
- `Done`: merged and verified after review

## PR summary

Every task result must contain:

- task name and run number
- files changed
- behavior added
- tests added
- exact verification commands/results
- data assumptions
- tax/legal assumptions
- UI behavior retained or changed
- known remaining issues
- local testing instructions
- one-line recommendation

Do not merge by default.
