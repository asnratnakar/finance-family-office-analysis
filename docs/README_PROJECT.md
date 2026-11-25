# Personal Portfolio Analysis

A local-first advisory application for personal and family wealth.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
pre-commit install
```

## Run

```powershell
streamlit run PersonalPortfolioAnalysis.py
```

Only synthetic fixtures under `data/samples/` are commit-safe. Real data belongs in ignored `data/` and `input/` locations and must not be committed.

## Verify

```powershell
ruff check .
pytest
streamlit run PersonalPortfolioAnalysis.py --server.headless true
git check-ignore -v data/api_keys.keys data/banking/checkingAccounts.csv input/example.csv data/samples/checkingAccounts.csv
```
