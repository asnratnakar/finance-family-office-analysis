# Cross-Border Portfolio & Family Wealth App — Roadmap & Weekly Build Plan

Nov 14, 2026 · @Shivanga Ratnakar Addada - CW

> **Authority note:** This roadmap explains goals and sequencing. It is not a visual or data-schema implementation specification. Implementation decisions must also follow `IMPLEMENTATION_CONTRACT.md`, `DATA_CONTRACT.md`, `UI_BASELINE.md`, `UI_CHANGE_CONTROL.md`, `TASK_EXECUTION_CONTRACT.md`, and `WEEKLY_BACKLOG.md`. If documents disagree, stop and resolve the conflict; do not silently choose a third behavior.

## Overview

One local app covers my portfolio and my family's Indian assets: it reads broker CSVs and manual templates, measures risk across both countries, and advises on taxes, rebalancing, residency timing, and the inherited real estate. It never places trades. It is built one small, tested task per week by a scheduled Claude Code run, inside a Pro or Max subscription, starting from the existing Streamlit app.

This plan merges two earlier documents: the cross-border family wealth roadmap (planning profile, tracks P0-P13, current-app audit) and the local advisory app plan (CSV input folder, data freshness rules, advice-only design).

| Tab | What it holds |
| --- | --- |
| Roadmap (this tab) | Profile, current state, principles, architecture, phase map, data rules, and how the weekly AI loop runs |
| Weekly backlog | One task per weekly run, with a done-when test and a status to tick |
| Phase details | Features and done-when for every phase, plus thresholds, calendar, and parked legal items |

Not tax or legal advice. Thresholds are stored as dated configuration and confirmed with a US CPA and an Indian CA before acting.

## Planning profile

Every recommendation must hold up across four residency futures, because residency stays uncertain and leaving the US on an H-1B is hard to reverse.

|  |  |
| --- | --- |
| Owner | Indian citizen, about 15 years in the US on H-1B; employment-based green card pending (priority date Nov 2017) |
| Own assets | About $260K in US equities and ETFs (top four positions about 54%), US retirement accounts (401(k)s, Roth IRA, HSA), some US bullion |
| Family assets in India | Agricultural land near Gudivada (Krishna district, AP); plots and rented apartment buildings in Visakhapatnam; gold jewellery and silver |
| Goals | No landlord role; turn inherited property into low-maintenance, diversified income; keep residency options open; most likely retire in Vizag |
| Accounts today | Vanguard (brokerage, Roth IRA), Fidelity (401(k), brokerage, HSA, cash), Empower (401(k)), SoFi (ARKVX), IBKR, plus US bank accounts |

| ID | Scenario | Tax residence | Spending currency | What changes |
| --- | --- | --- | --- | --- |
| A | Stay in the US (green card arrives) | US | USD | Indian assets stay foreign holdings; FBAR, Form 8938, PFIC rules apply indefinitely |
| B | Return to India (current plan) | India: RNOR first, then ROR | INR | RNOR window and order of sales matter most; US estate-tax exposure on US-situs assets |
| C | Move to a third country | That country | Local | Needs a third country pack |
| D | Retire in Vizag | India | INR | Later stage of B or C; drives the long-run currency glide path |

## Where the app is today

The Streamlit app is a working local dashboard for Vanguard snapshots and metals, but it has no risk analytics, no shared ledger, USD only, and 13 known bugs. Weeks 1-6 of the backlog fix that before anything new is built.

| Area | Status | Fixed in |
| --- | --- | --- |
| Market Investments (Vanguard lots, sector pie, trend) | Working; Vanguard only | Weeks 15-20 (ledger importers) |
| Metals (spot, premiums, divestment tax) | Working; 3 bugs (no-price valuation, uncached API call, wrong time labels) | Week 4 |
| Loan Calculator, Knowledge Base | Working | No change |
| Bank Accounts | Broken: wrong column name, text-only month sort, simple interest on APY | Week 3 |
| Retirement | Mislabelled sector page on random data | Week 6 |
| Real Estate, Commodities, Forex, Life Insurance | Empty files | Week 6 (remove), later phases (rebuild) |
| Family Office | Static diagram; missing `networkx` dependency; typo | Weeks 1 and 6 |
| Vanguard utils | Duplicated module; glob and filename-sort bugs | Weeks 4-5 |
| Tests | A print script, not tests | Week 2 |
| Security | `data/api_keys.keys` and personal CSVs not git-ignored | Week 1, before the first commit |

The full bug list with file and line numbers stays in the repo's `ROADMAP.md`; the weekly run reads it from there.

## Design principles

Twelve rules, merged from both plans; every weekly task is checked against them.

1. **Local first, encrypted.** Financial data stays on my machine, encrypted at rest; secrets live in the OS keyring.
2. **Files in, advice out.** Data arrives as broker CSVs and manual templates in an input folder; the app never places trades.
3. **One ledger is the source of truth.** Every page reads one store of transactions, lots, valuations, prices, and FX rates.
4. **Honest about data gaps.** Every report shows the as-of date of its inputs and flags files older than 6 months, missing accounts, or missing cost basis.
5. **Store native, report in either currency.** Amounts keep their original currency; reports switch USD/INR using a dated FX table.
6. **Residency is an input.** Every tax, projection, and risk number takes a residency timeline, and runs for scenarios A-D.
7. **Two cost bases per asset.** US and Indian bases are stored separately, especially for inherited assets.
8. **Country packs.** Tax rules, account types, and fiscal calendars live in one pack per country; rules are dated configuration, never constants in code.
9. **Fractional ownership.** Any asset can have several owners with percentages.
10. **Point-in-time and reproducible.** Any report can be rebuilt for a past date with that date's prices, FX, and rules.
11. **Live prices only on demand.** Analysis uses file prices by default; a live pull is optional and labeled with its time.
12. **Synthetic data in the repo.** Code, tests, and samples go to GitHub; real statements never do, so the cloud-run AI never sees them.

## Architecture

Everything runs on my machine: CSV exports go into the input folder, the app builds a local data store, and the output is an advice report I act on manually.

&#91;embedded content: app architecture · CSV files in, advice report out\]

The freshness checker runs at import, so every report opens with a data-health section before any advice. The only outside calls are optional live price and FX pulls, which send ticker symbols, not account data.

## Phase map

The build runs in the order P0, P1, data health, ledger, net worth, prices, performance, risk, then the decision engines; each phase's features are in the Phase details tab.

&#91;embedded content: phase map · 16 phases across about 63 weekly runs\]

Gaps between bars are buffer runs. Track A finishes around week 14, risk analytics around week 38, and the advice engine starts around week 53; pulling the residency and real-estate phases forward is the main lever if the move or the inheritance comes sooner.

## Analysis cadence and data freshness

Analysis runs on demand, and every report says when its inputs are too old to trust. Any input older than 6 months is flagged as stale, with the exact file to re-download.

| Input | Suggested refresh | Flagged as stale after |
| --- | --- | --- |
| Positions / holdings | Monthly, and before acting on any advice | 6 months (plus a softer notice after 30 days, since balances move) |
| Transactions / activity | Quarterly | 6 months |
| Cost basis / unrealized gains by lot | Quarterly, and after any sale | 6 months |
| Realized gains | Once a year, at tax time | When the tax year closes |
| ETF look-through holdings | Monthly | 6 months |
| Live prices and USD/INR | Pulled at the start of a run, when I ask | Same day; cached prices labeled with their time |
| Investment policy | Once a year, or after a life change | 12 months |

Suggested rhythm:

- **Monthly:** download positions, run the risk report.
- **Quarterly:** refresh all CSVs, review the advice report, and act manually on any band breach.
- **Yearly:** add realized-gains files, do the tax review, and review the investment policy.

**Live vs file prices.** By default the app values holdings at the prices inside the CSVs. A live price pull is optional, and the report states which prices it used and when.

**Acting on advice without watching the market.** Vanguard supports recurring purchases of Vanguard ETFs and mutual funds, and recurring withdrawals from mutual funds only; Fidelity's recurring investments also cover individual stocks. Verify current rules on each site.

## APIs and data sources

Only live prices need an API; everything else comes from CSV files. Free tiers cover on-demand price pulls for about 40 holdings, so the expected cost is $0/month. Prices below were checked in November 2026.

| Need | Free options | Paid options |
| --- | --- | --- |
| Live prices, US and NSE/BSE | Finnhub (60 calls/min), Tiingo (1,000 requests/day) per [APILayer's comparison](https://blog.apilayer.com/analyzing-the-top-free-apis-for-stock-data/); yfinance (`.NS` / `.BO`) for prototyping | Massive, formerly Polygon.io: individual plans around $29 / $79 / $199 per month ([pricing summary](https://qveris.ai/guides/polygon-pricing-optimized/)) |
| Indian mutual fund NAVs | AMFI daily NAV file | Not needed |
| Gold and silver | goldapi.io (USD, already used), IBJA daily rates (INR) | goldapi.io paid tiers |
| ETF look-through holdings | Free holdings files from ETF issuers (iShares, Vanguard, VanEck) | Financial Modeling Prep paid tiers |
| Fundamentals | Financial Modeling Prep, 250 calls/day ([comparison](https://multiples.vc/compare/fmp-api-alternatives)) | FMP paid tiers |
| Rates, inflation, macro | FRED (US), RBI DBIE (India), U.S. Treasury yields | Not needed |
| FX rates (USD/INR) | FBIL reference rate, FRED; SBI TT and US Treasury reporting rates as downloaded files | Not needed |
| Company filings | SEC EDGAR | Not needed |

Dropped with the CSV approach: account aggregators (SnapTrade) and broker trading APIs (IBKR, Schwab). A read-only aggregator can be added later if downloading CSVs becomes tedious.

Cautions:

- Alpha Vantage's free tier (25 requests/day) is too low for 40+ holdings.
- IEX Cloud has been retired; skip tutorials that use it.
- Most free tiers are personal-use only and forbid redistributing data.
- Keep API keys in a local environment file, never in code or the input folder.

Open-source libraries that already implement most of the risk math: Riskfolio-Lib, PyPortfolioOpt, QuantStats, pandas.

## Weekly AI development loop

A Claude Code cloud scheduled task runs once a week, builds the next backlog task on a branch with tests, and leaves a pull request; I review and merge on the weekend. Cloud tasks run on Anthropic's servers with the laptop closed, clone the repo fresh each run, and push to `claude/`-prefixed branches ([docs](https://code.claude.com/docs/en/web-scheduled-tasks)). Because the cloud run only sees the GitHub repo, real statements stay on my machine.

### What happens each week

1. **Saturday 06:07 local:** the scheduled task clones the private repo. A few minutes past the hour avoids late starts.
2. It reads `CLAUDE.md` (rules) and `docs/BACKLOG.md`, and picks the first "Not started" task whose dependencies are done.
3. It builds that one task on a branch, adds tests using synthetic data, and runs `ruff` and `pytest`.
4. Green: it opens a PR with a summary, the done-when checklist, and how to test with real data, and marks the task "In review".
5. Red after three fix attempts, or the task is too big: it pushes a partial branch with notes and marks the task "Blocked".
6. **Weekend, 30-60 minutes:** I review the PR, run the app locally on my real data, merge, and set the task to Done.

### One-time setup

- [ ] Before any push: add `.gitignore` for `data/`, `input/`, and `*.keys`, then confirm with `git check-ignore` that no keys or statements are tracked
- [ ] Create a private GitHub repo; protect `main` so only I can merge
- [ ] Add `CLAUDE.md` (guardrails below), `docs/BACKLOG.md` and `docs/PHASES.md` (exported from the other two tabs as Markdown)
- [ ] Create the task at claude.ai/code/routines: weekly trigger, this repo, Default environment (package registries only), a setup script that installs `requirements.txt`
- [ ] Remove every connector from the task; it needs only the repo
- [ ] Click **Run now** once on week 1 and watch the session

### Fitting a monthly subscription

- Scheduled runs draw on the same subscription usage as my interactive sessions. With no usage credits, a run that hits the limit is rejected until the window resets, so nothing bills extra.
- Schedule the run when I'm not using Claude (early Saturday), and keep it to one task per run.
- Every task is sized for one session. If a run fails for size, split the task in the backlog instead of upgrading the plan.
- Each run starts with no memory. All state lives in the repo: `BACKLOG.md`, `CLAUDE.md`, and PR notes.
- Pick the model in the task. Use the larger model only for design-heavy weeks (ledger schema, tax engines, residency engine).
- Every 6th run is a buffer week: fix failing tests, lint, and TODOs; no new features.
- After four runs, check consumption at claude.ai/settings/usage and adjust the task size or plan.

### Guardrails in `CLAUDE.md`

- Never read or write real financial content under `data/` or `input/` in tests; never commit statements or exports.
- No live network calls in tests; mock every price, FX, and metals API.
- One backlog task per run; never start the next one, never merge.
- Tax rates and thresholds go only into dated config files, each with a source link and an "as of" date.
- No new dependency without pinning it in `requirements.txt`.
- If a rule or tax treatment is unclear, stop and write the question in the PR instead of guessing.

### The weekly prompt

```text
You are working on the cross-border portfolio app in this repository.
1. Read CLAUDE.md, docs/BACKLOG.md and docs/PHASES.md.
2. Pick the first task with Status "Not started" whose "Depends on" tasks are Done.
   If that row is a BUFFER week, fix failing tests, lint errors and TODOs instead.
3. Implement only that task on a new branch. Use fixed synthetic in-memory data for tests.
4. Add or update pytest tests that prove the task's "Done when" line.
   Run ruff and pytest until both pass, at most 3 fix attempts.
5. In docs/BACKLOG.md set the task to "In review", or "Blocked" with the reason.
6. Open a pull request titled "Week N: <task>" listing what changed, how I test it
   locally with real data, what is left, and any question for me.
Do not merge. Do not start a second task.
```

## Open questions and caveats

- [ ] Which CSV exports each broker offers (Vanguard, Fidelity, Empower, SoFi, IBKR), and whether they include lot-level cost basis.
- [ ] Download full transaction history and cost basis for every account before moving; will broker downloads keep working after a foreign address change?
- [ ] Which custodian will service my Roth IRA and 401(k)s as an India resident? Get it in writing.
- [ ] Exact date I become a US nonresident for tax purposes, and my RNOR years.
- [ ] Target allocation and band sizes for the investment policy.
- [ ] Which UCITS ETFs map to my current US ETFs.
- [ ] Gudivada land: measured aerial distance from the municipal limit (decides whether it is a capital asset).
- [ ] Date-of-death valuation: which registered valuer, and how soon after the event.
- [ ] Advice explanations: rules-only and local, or an anonymized summary sent to an AI model?
- [ ] Does one weekly run fit Pro usage without hitting limits? Check after four runs.

Caveats: the app's advice is a decision aid, not professional financial, tax, or legal advice. Tax rules in both countries change every year, so check any tax suggestion with a cross-border CPA and an Indian CA before acting.
