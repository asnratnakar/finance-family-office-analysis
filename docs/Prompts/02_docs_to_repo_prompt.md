# Prompt: Convert Roadmap Docs Into Repo Artifacts

Use this prompt to transform planning docs into implementation-ready files.

## Prompt

I have planning documents with roadmap, backlog, and phase details. Convert them into working repo artifacts.

Input documents to use:
- docs/ROADMAP.md
- docs/WEEKLY_BACKLOG.md
- docs/PHASE_DETAILS.md

Create/Update:
- docs/BACKLOG.md (machine-readable backlog copy)
- docs/PHASES.md (phase details copy)
- docs/DECISIONS.md (architecture decisions and assumptions)
- docs/DEFINITION_OF_DONE.md (global done criteria)
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

Rules:
- Keep legal/tax disclaimers.
- Keep only implementation-relevant details.
- Remove duplicated prose.
- Preserve run order and dependencies.
- Add a top section called "Current Focus" with the next 3 tasks.

Return:
- a summary of what was preserved, collapsed, and dropped
- any ambiguities requiring human decision
