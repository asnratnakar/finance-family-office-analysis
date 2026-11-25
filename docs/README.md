# Documentation Index

## Read first

1. `IMPLEMENTATION_CONTRACT.md` — product scope and implementation rules
2. `TASK_EXECUTION_CONTRACT.md` — how AI and manual work must execute
3. `CURRENT_APP_AUDIT.md` — what is implemented today
4. `UI_BASELINE.md` — exact current UI behavior
5. `DATA_CONTRACT.md` — ledger/import/currency/tax-rule data rules
6. `TESTING_CONTRACT.md` — required tests
7. `SECURITY_AND_PRIVACY_CONTRACT.md` — real-data and secret boundaries

## Planning

- `ROADMAP.md` — goals, sequencing, architecture, and cautions
- `WEEKLY_BACKLOG.md` — implementation queue
- `PHASE_DETAILS.md` — phase-level behavior and done conditions
- `TASK_TEMPLATE.md` — format for future precise backlog rows

## Migration and UI

- `MIGRATION_MAP.md` — legacy file/page/utility to target system mapping
- `UI_BASELINE.md` — current UI source inventory
- `UI_CHANGE_CONTROL.md` — UI change rules
- `UI_CAPTURE.md` — browser/screenshot evidence process
- `screenshots/` — synthetic UI artifacts

## Prompts

- `Prompts/01_repo_bootstrap_prompt.md`
- `Prompts/02_docs_to_repo_prompt.md`
- `Prompts/03_weekly_executor_prompt.md`
- `Prompts/04_main_stage_git_flow_prompt.md`
- `Prompts/05_new_repo_migration_checklist.md`
- `Prompts/06_ui_preservation_prompt.md`

## Legacy/reference

- `DOCUMENTATION.md` — older prose documentation; not an authoritative UI specification
- `DATA_STRUCTURE.md` — older data-layout reference; superseded for new imports by `DATA_CONTRACT.md`

## Conflict policy

If these documents disagree:

1. Do not guess.
2. Identify the conflict.
3. Add a review/decision item.
4. Use the most specific constraint relevant to the task.
5. Update this docs set after the decision is approved.
