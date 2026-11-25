# Prompt: Two-Branch Git Flow (main + stage)

Use this when you want the assistant to prepare safe commit and merge steps.

## Prompt

I use exactly two branches: main and stage.

Please:
1. Inspect git status and branch list.
2. Explain current state in one paragraph.
3. Provide exact non-destructive commands for:
   - initial commit if repo has no commits
   - pushing main and stage
   - opening a PR from stage to main
4. Include rollback-safe options only (no hard reset).
5. Include verification commands after each step.

Assume I want:
- main = stable baseline
- stage = active development
