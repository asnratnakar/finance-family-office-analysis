# New Repo Migration Checklist

## Copy as-is (recommended)
- docs/ROADMAP.md
- docs/WEEKLY_BACKLOG.md
- docs/PHASE_DETAILS.md
- docs/DATA_STRUCTURE.md
- docs/DOCUMENTATION.md (after command/path cleanup)

## Convert to prompts (recommended)
- Weekly execution workflow
- Branching and release workflow
- Bug-fix execution style
- Test strategy and acceptance checks

## Do not copy directly
- Any real statements, exports, balances, or key files
- data/* except synthetic samples
- local environment files with secrets

## First commit in new repo should include
- project skeleton
- docs baseline
- .gitignore and secret handling
- pre-commit + ruff + pytest smoke checks

## Verify before push
- streamlit run PersonalPortfolioAnalysis.py
- pytest
- ruff check .
- git check-ignore data/api_keys.keys data/banking/checkingAccounts.csv

## Preserve UI baseline
- Copy docs/UI_BASELINE.md to the new repo.
- Add docs/Prompts/06_ui_preservation_prompt.md.
- Capture screenshots of every working page using synthetic data before rebuilding the data model.
- Reuse exact titles, metric labels, defaults, tabs, table columns, sidebar controls, and chart types.
- Do not treat the old Documentation.md as a complete UI specification; use UI_BASELINE.md plus the implementation pages.

## Copy these authoritative contracts
- docs/IMPLEMENTATION_CONTRACT.md
- docs/DATA_CONTRACT.md
- docs/TASK_EXECUTION_CONTRACT.md
- docs/TESTING_CONTRACT.md
- docs/SECURITY_AND_PRIVACY_CONTRACT.md
- docs/CURRENT_APP_AUDIT.md
- docs/MIGRATION_MAP.md
- docs/UI_BASELINE.md
- docs/UI_CHANGE_CONTROL.md
- docs/UI_CAPTURE.md
- docs/TASK_TEMPLATE.md
