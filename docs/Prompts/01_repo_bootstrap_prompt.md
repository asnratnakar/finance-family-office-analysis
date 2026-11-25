# Prompt: Bootstrap New Personal Repo

Use this prompt in your new repo to generate the initial project skeleton and safety baseline.

## Prompt

You are helping me bootstrap a new private repo for a local-first personal finance app.

Constraints:
- Python + Streamlit
- No real financial data in repo
- Keep root clean (entry point + config only)
- Create folders: docs, scripts, tests, pages, utils, data/samples, input
- Add .gitignore to block real data and keys
- Add .env.example
- Add requirements.txt with: streamlit, pandas, plotly, numpy, requests, networkx, pytest, ruff, pre-commit, python-dotenv, keyring
- Add .pre-commit-config.yaml with ruff and basic file hooks
- Add a minimal app entry file named PersonalPortfolioAnalysis.py
- Add docs/README_PROJECT.md with run instructions

Acceptance criteria:
1. streamlit run PersonalPortfolioAnalysis.py starts successfully.
2. pytest runs at least one smoke test.
3. git check-ignore confirms keys and data files are ignored.

After creating files, print:
- created file tree
- exact run commands
- exact verification commands
