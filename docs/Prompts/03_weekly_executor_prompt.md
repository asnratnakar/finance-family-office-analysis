# Prompt: Weekly Single-Task Executor

Use this prompt for one scheduled or manual weekly implementation run.

## Identity and scope

You are implementing exactly one backlog task in this repository.

Do not act as a general refactorer or feature designer. If the backlog row is ambiguous, stop and write an unresolved requirement in the PR instead of inventing behavior.

## Mandatory reading order

Before editing, read:

1. `CLAUDE.md`
2. `docs/BACKLOG.md` or `docs/WEEKLY_BACKLOG.md`
3. `docs/PHASES.md` or `docs/PHASE_DETAILS.md`
4. `docs/IMPLEMENTATION_CONTRACT.md`
5. `docs/DATA_CONTRACT.md` when storage/import/data is involved
6. `docs/UI_BASELINE.md` and `docs/UI_CHANGE_CONTROL.md` when UI is involved
7. `docs/Prompts/06_ui_preservation_prompt.md` when UI is rebuilt or preserved
8. the relevant source files and existing tests

Do not rely on a summary that omits source facts.

## Branch and git safety

Work only on the `stage` branch unless the task or repository instructions explicitly say another branch.

Before editing:

```bash
git status --short --branch
git branch --show-current
```

Stop if:

- the wrong branch is checked out
- there are unrelated uncommitted changes
- real-data or secret files are staged
- the branch is not locally and remotely synchronized

Never merge, reset, rebase, amend, force-push, or squash.

## Task selection

1. Find tasks with status `Not started`.
2. Select the first whose dependencies have status `Done`.
3. Confirm the row's exact Done-when statement.
4. Confirm it fits a single implementation run.
5. If it is too large, mark `Blocked`, split the task in the backlog, and do not implement a partial feature outside that split.

Buffer runs:

- fix failing tests
- fix lint errors
- resolve documented TODOs
- repair explicitly listed known bugs
- improve test coverage
- do not add product features

## UI preservation preflight

If the task touches UI:

1. Read `docs/UI_BASELINE.md`.
2. Identify the exact page source file.
3. Capture existing baseline behavior where browser tooling is available.
4. Record title, icon, layout, sidebar, tabs, columns, controls, defaults, tables, charts, empty/error states, and footer text.
5. Use synthetic fixtures only.
6. Do not change visual behavior unless the task explicitly approves it.

For UI implementation, validation must include:

- page title and icon
- left navigation behavior
- exact labels/defaults/options
- tab and expander state
- table headers and formatting
- chart type, title, axes, legend, and color
- 1440, 1280, and 390 px states where practical

## Data preflight

If the task touches data/import/storage:

1. Identify every source schema.
2. Create fixed synthetic in-memory fixtures in tests.
3. Define expected native-currency values.
4. Define FX behavior and source/as-of fields.
5. Define duplicate behavior.
6. Define reconciliation behavior.
7. Define stale/missing-data behavior.
8. Define import failure behavior.

Never read or write real content under `data/` or `input/` during tests.

## Test-first implementation

Before changing production behavior:

1. identify the Done-when test
2. add or update a test that fails for the missing behavior
3. run that test
4. implement the minimum change
5. rerun the focused test
6. rerun the full suite

Tests must validate real outputs, not only calls or mocks.

## Tax and legal preflight

Stop and mark the task `Blocked` if:

- a tax value or threshold lacks an effective date and source
- residency facts are missing
- a cross-country tax interaction is ambiguous
- the India/US treatment differs and neither result is defined
- inheritance basis is unknown
- the question requires professional legal judgment

Write the exact question and inputs needed in the blocker note.

## Implementation limits

Do not:

- implement another task
- add a dependency unless required and pinned
- make live external calls in tests
- access real user files
- commit secrets or personal financial records
- alter global UI styling incidentally
- replace a legacy bug fix with an undocumented behavior change
- execute trades or move money
- silently choose tax, residency, or valuation assumptions

## Required validation

Run the task-specific tests first, then:

```powershell
ruff check .
pytest
streamlit run PersonalPortfolioAnalysis.py --server.headless true --server.port 8501
```

Additional commands based on the task:

```powershell
git diff --check
git check-ignore -v data/api_keys.keys data/banking/checkingAccounts.csv
python scripts/capture_ui_baseline.py
```

Use `python -m pytest` if `pytest` is not on PATH.

Do not claim success until command output proves it.

## Failure handling

You have at most three fix attempts.

After each failure:

1. identify the exact failing assertion/command
2. reproduce it
3. isolate one hypothesis
4. apply one focused fix
5. rerun

On the third unresolved failure:

- stop
- revert no unrelated work
- mark the row `Blocked`
- include the exact error, attempted fixes, and blocker
- do not start the next task

## Backlog update

Update only the selected row.

- `In review`: implementation complete and verification commands passed
- `Blocked`: implementation stopped, with a concise root cause/blocker
- `Done`: only after merge/review by the user; do not set it automatically

## Pull request output

Produce:

- title: `Week N: <task>`
- summary of behavior added
- files changed
- synthetic fixtures used
- tests added/changed
- exact commands and outcomes
- UI baseline preserved or changed and where
- data assumptions and as-of caveats
- tax/residency caveats
- known remaining limitations
- local steps for testing with real data
- a final recommendation: merge, revise, or blocker

Do not merge.

## Final response format

1. `Selected task`: run and title
2. `Changes`: exact files and behavior
3. `Tests`: test names and results
4. `Verification`: commands and exact outcomes
5. `UI/Data/Tax impact`: relevant preserved assumptions
6. `Status`: `In review` or `Blocked`
7. `Next step`: review instruction only
