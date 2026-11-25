# UI Capture Specification

This file is the visual evidence contract for reproducing the existing app.

## Capture baseline

Run from the repository root:

```powershell
pip install -r requirements.txt
python -m pip install playwright
python -m playwright install chromium
streamlit run PersonalPortfolioAnalysis.py
```

In another terminal:

```powershell
python scripts/capture_ui_baseline.py
```

The script writes screenshots and browser evidence to:

- `docs/screenshots/baseline/<page>/`
- `docs/UI_CAPTURE.json`

Use synthetic data only. Do not upload real statements or account exports.

## Capture states

For every page, capture:

- 1440 px desktop, 1280 px desktop, 390 px mobile
- expanded and collapsed sidebar
- default widget values
- selected tab
- open and closed expanders
- sample/uploaded data states where they differ
- loading, empty, warning, error, success, and no-data states
- active and hover navigation states

## Navigation baseline

The exact left-menu entries must be extracted from screenshots and `UI_CAPTURE.json`, not guessed from filenames. Capture:

- label text
- order
- active state
- home entry
- icon behavior
- menu width
- item height
- hover and selected colors
- numbering and underscore cleanup
- duplicate `6_*` route behavior

## Exact theme

Effective theme source:

- `primaryColor`: `#1f77b4`
- `backgroundColor`: `#ffffff`
- `secondaryBackgroundColor`: `#f0f2f6`
- `textColor`: `#262730`
- `font`: `sans serif`
- `showErrorDetails`: `true`
- `toolbarMode`: `minimal`
- `gatherUsageStats`: `false`

The browser evidence must also record the effective Streamlit and browser-computed font, padding, margin, and color values because Streamlit package versions may change its DOM/CSS.

## Page specification

Create one evidence subsection for each route. For each, record:

- screenshot filenames
- route and browser title
- visible menu label
- sidebar state
- element bounding boxes
- computed CSS
- exact visible text
- tab names and selected tab
- widget labels/defaults/minimum/maximum/step/help text
- metric names/formats
- table headers/formats/sorting
- chart types/colors/axes/hover/height/legend
- expanders and callouts
- footers and privacy captions
- console/page/network errors

## Acceptance criterion

Visual parity is not proven until baseline and migrated screenshots are compared at the same viewport and state. Code inspection alone is insufficient.
