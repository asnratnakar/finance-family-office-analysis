# Prompt: Capture and Preserve the Complete Existing Streamlit UI

## Objective

Preserve the app's existing visual design and interaction behavior when rebuilding code. This is a pixel-and-behavior preservation task, not a fresh UI redesign.

## Source of truth hierarchy

When details conflict, use this order:

1. Screenshots captured from the running app
2. Browser DOM/CSS measurements
3. Streamlit page Python source
4. Streamlit theme configuration
5. Existing markdown documentation

Do not infer missing details from framework defaults alone. Record unknowns instead.

## Required source files

Before capturing or changing UI, inspect:

- `.streamlit/config.toml`
- `PersonalPortfolioAnalysis.py`
- every file under `pages/`
- every file under `knowledge_base_modules/` rendered by a page
- `docs/UI_BASELINE.md`
- `docs/DOCUMENTATION.md`

## Phase 1: capture the running baseline

Run the app only with synthetic, non-sensitive data:

```powershell
streamlit run PersonalPortfolioAnalysis.py
```

For every page, capture:

1. Default state at 1440 px desktop width
2. Default state at 1280 px desktop width
3. Mobile/narrow view at approximately 390 px width
4. Every tab, expander, sidebar state, and data source option
5. Empty, error, loading, warning, and success states
6. Uploaded-data state and sample-data state where they differ

Save artifacts under:

```text
docs/screenshots/baseline/<page-slug>/
```

Use descriptive names such as:

```text
01-default-1440.png
02-sidebar-expanded-1440.png
03-empty-data-1280.png
04-error-state-1280.png
05-mobile-default-390.png
```

## Phase 1A: capture the left navigation/menu

Do not treat the page list as part of the main page screenshot only. Capture it separately.

Record:

- every menu entry displayed
- exact rendered label text
- numbering and capitalization
- file/route mapping
- rendered order
- home-page entry position
- selected entry and hover/active styling
- menu icon/emoji behavior
- menu width and item height
- sidebar expanded/collapsed state
- duplicate-number page ordering
- whether empty or mislabelled pages appear
- whether menu labels come from filenames or explicit page configuration

Create baseline screenshots:

```text
docs/screenshots/baseline/navigation/desktop-expanded-1440.png
docs/screenshots/baseline/navigation/desktop-collapsed-1440.png
docs/screenshots/baseline/navigation/mobile-expanded-390.png
```

For migrated pages, capture the same states and compare:

- list length
- labels and order
- menu width
- item spacing
- active/hover styles
- icon positions
- selected-page highlight
- collapsed and expanded behavior

Add `left_navigation` to `docs/ui-baseline.json` or `docs/ui-baseline.yaml` with entries mapped to source files and rendered labels.

## Phase 2: extract exact design details

Create `docs/UI_CAPTURE.md` and document every captured page with these sections.

### 1. Page identity

Record:

- route/filename
- page title
- favicon/page icon
- browser title
- Streamlit navigation label
- layout mode (`wide` or `centered`)
- initial sidebar state
- page status: working, broken, empty, mislabelled, or static

### 2. Theme

Copy the effective theme values:

- primary color
- background color
- secondary background color
- text color
- font family
- border radius
- base font size
- heading font sizes
- line height
- link color
- sidebar background
- code/editor defaults if visible
- toolbar mode
- usage-stat setting

Also record custom CSS found in source, including:

- selectors
- property values
- padding
- margins
- widths
- heights
- overflow behavior
- unsafe HTML behavior

### 3. Global layout

Measure and record:

- viewport width
- content width
- sidebar width
- sidebar expansion/collapse behavior
- main-container side padding
- top padding
- section vertical gaps
- horizontal rule style and spacing
- number and ratio of columns
- whether columns stack at narrow widths
- sticky elements

### 4. Page hierarchy

For every visible element, record:

- exact text
- emoji icon
- heading level
- font weight
- approximate font size
- text alignment
- top/bottom margin
- color
- divider location
- whether it is inside a card, container, tab, expander, column, sidebar, or dialog

### 5. Sidebar

Record:

- heading text
- radio/select/multiselect/text/number inputs
- label text
- default value
- selected value
- help text
- tooltip text
- options order
- disabled/hidden controls
- file-uploader type restrictions
- uploader label
- upload instructions
- spacing and separators

### 6. Widgets and controls

For every button/input/control, capture:

- exact label
- widget type
- default value
- min/max/step value
- key if visible in source
- formatting (`$`, `%`, decimals)
- enabled/disabled state
- help text
- validation/error text
- session-state behavior
- on-change behavior
- keyboard behavior

### 7. Metrics and tables

For metrics, record:

- label
- exact default display
- number format
- decimal places
- currency symbol
- positive/negative presentation
- column width
- delta if present
- help text
- label/value alignment

For tables, record:

- exact column headers
- source field names
- display field names
- row sorting
- row count behavior
- number/date/currency formatting
- hidden columns
- hidden index
- row heights
- horizontal overflow
- full-width/container behavior
- expander state
- empty-table behavior

### 8. Charts

For every Plotly/chart element, record:

- chart type
- title
- title font and position
- x-axis label, scale, tick format, ordering, and timezone
- y-axis label, scale, tick format, and range
- legend position, labels, icons, and visibility
- series names and order
- colors and opacity
- line width/style and marker shape/size
- bar orientation and spacing
- pie hole size and slice colors
- donut labels and percentages
- hovermode and hover text
- template/background
- height
- margins
- animation/transition behavior
- loading or empty state
- whether `use_container_width=True`
- export menu visibility

### 9. Text, callouts, and HTML

Record:

- exact wording
- Markdown bold/italic/emoji usage
- code blocks
- info/warning/error/success styling
- button/clickable-link behavior
- anchors generated by HTML
- footer text and alignment
- caption text
- JSON expander content
- line breaks and separators

### 10. Browser/DOM evidence

Where Playwright or browser automation is available, collect:

- screenshot at each viewport
- full-page screenshot
- viewport screenshot
- DOM accessibility snapshot
- element bounding boxes
- computed CSS for typography and major containers
- sidebar height/width
- chart SVG dimensions
- table widths and overflow
- console errors
- failed network requests
- HTTP status for local assets

Use a small browser script or Playwright test rather than visually estimating measurements.

## Phase 3: produce machine-readable UI inventory

Where practical, add `docs/ui-baseline.json` or `docs/ui-baseline.yaml` containing:

```yaml
page:
  file: pages/4_Market_Investments.py
  title: "📈 Market Investments - Portfolio Analysis"
  icon: "📈"
  layout: wide
  sidebar: expanded
  sections:
    - name: Overall Portfolio Summary
      layout: 4-columns
      metrics:
        - label: Total Cost
          format: currency-usd
        - label: Market Value
          format: currency-usd
  charts:
    - title: Portfolio Distribution by Sector
      type: pie
      full_width: true
```

Use the simplest format that can be reviewed and regenerated. Do not invent values that are not in source or screenshots.

## Hard preservation rules

1. Never redesign the UI as part of a backend, ledger, importer, or bug-fix task.
2. Preserve exact public labels even when the underlying field name changes.
3. Separate an intentional UI change from a bug fix.
4. Do not silently change spacing, headings, chart colors, defaults, sidebar controls, or page order.
5. Do not remove a legacy screen when replacing only its data source; migrate the UI and data independently.
6. Preserve mislabelled/empty pages only as known baseline states. Do not present them as finished features.
7. Synthetic data must support every default and wide/narrow layout state.
8. The UI baseline must not require real account, bank, tax, or broker data.

## Verification for implementation tasks

For each changed page:

1. Run page-level smoke tests.
2. Verify required visible labels.
3. Verify exact default values and options.
4. Verify table and chart containers render.
5. Verify no real-data paths are executed.
6. Compare screenshots at desktop and narrow widths.
7. Compare key DOM boxes and computed CSS when possible.
8. Report differences by pixel or CSS property only when available.

Do not claim visual parity from code inspection alone.

## Required deliverables

A UI-preservation run must produce:

- `docs/UI_CAPTURE.md`
- baseline screenshots for each state
- migrated screenshots for each corresponding state
- a screenshot diff or reported visual differences
- a page-by-page parity checklist
- unresolved visual discrepancies
- exact source files that control theme, CSS, charts, and layout

## Response format

For each page, report:

- exact page identity
- source files controlling layout
- theme/CSS details
- layout and spacing measurements
- widgets and defaults
- chart/table specifications
- state coverage
- visual parity result
- unmatched differences with suggested follow-up

## Reproducible capture script

Use `scripts/capture_ui_baseline.py` with the app running on port 8501. It captures:

- all named page routes
- desktop 1440 px and 1280 px
- mobile 390 px
- full-page screenshots
- browser title and URL
- visible body text
- navigation links and labels
- main element bounding boxes
- computed typography, colors, padding, margins, and border radius
- document and viewport dimensions
- console warnings/errors
- page exceptions
- failed requests

Inspect `docs/UI_CAPTURE.json` after each run. Never assume filename-derived labels are the exact rendered labels.

## Source-level exactness

Before implementing any UI page, extract all values directly from the source:

- `st.set_page_config`: title, icon, layout, initial sidebar state
- every exact `st.title`, `st.header`, `st.subheader`, `st.markdown`, `st.write`, `st.info`, `st.warning`, `st.error`, `st.success`, `st.caption`, and footer string
- every `st.columns` ratio and nested-column ratio
- every tab label and source order
- every radio/select/number/text/file control
- every default, minimum, maximum, step, key, help string, checkbox default, uploader type, and selected state
- every metric label and format string
- every table column source name, display name, sort, row limit, index setting, and currency/percentage formatting
- every Plotly title, trace, color, line width, marker shape, pie hole, legend, axis, template, margin, height, hover mode, fill, grid, and background
- every custom HTML/CSS block and its exact selector/property values

Use `docs/UI_BASELINE.md` as the human-readable source inventory and `docs/UI_CAPTURE.json` as browser evidence.

## UI parity report

A final report must be page-by-page and include:

- screenshot paths for baseline and migrated states
- route/title/nav-label match
- viewport dimensions
- text-match status
- widget/control match status
- table and chart match status
- spacing/layout difference in pixels or percentages
- CSS property differences
- console/page/network issues
- unresolved differences and explicit approval needed for redesign
