# UI Change Control

**Status:** mandatory for UI work

## Rule

Visual equivalence is a requirement unless the task explicitly says otherwise.

## Allowed UI changes

A UI change is allowed only for:

- an explicitly named redesign
- replacement of an empty page
- replacement of a mislabelled page
- bug fixing that names the visual effect
- accessibility work that does not change information architecture
- responsive layout work that preserves desktop semantics

Backend/data-migration work is not UI redesign work.

## Baseline before edit

For the target page, create and commit outside real data:

- a 1440 px screenshot
- a 1280 px screenshot
- a 390 px screenshot
- open/closed expander states
- open/closed sidebar states
- every tab state
- error/loading/empty states
- default data and uploaded/synthetic data states

## Exact match dimensions

The migration must compare:

- viewport width
- sidebar width
- content width
- page title position
- horizontal divider position
- title font size/weight
- section font size/weight
- section vertical spacing
- column width ratios
- table width/height
- chart width/height
- metric label/value spacing
- expander header height
- tab label spacing
- footer position
- error/warning callout spacing

## Source evidence

For every page maintain:

- source page file
- theme file
- CSS blocks
- chart definitions
- exact widget definitions
- exact label strings
- exact defaults/options
- screenshot set
- DOM/CSS evidence if Playwright is available

## Page transition policy

Backend task:

- use a compatibility adapter
- preserve displayed labels and layouts
- replace data source only behind a stable interface

Bug-fix task:

- document the bug
- add a failing test
- change only affected behavior
- verify unchanged areas

Redesign task:

- label every approved change
- show before/after screenshots
- update `UI_BASELINE.md`
- update route/navigation documentation
- obtain explicit acceptance

## Navigation policy

The app menu is part of the UI baseline. Record:

- exact rendered labels
- source route
- order
- active state
- hover state
- expanded/collapsed state
- mobile behavior
- selected-page behavior

No new page should be silently inserted ahead of existing pages.

## Screenshot comparison

Where possible:

- same browser/OS/theme
- same synthetic fixture
- same viewport
- same sidebar state
- same tabs/expanders open
- same chart animation state

Compare screenshots at pixel level and list each approved visual difference.

## Done criteria

UI work is done only when:

1. baseline screenshots exist
2. migrated screenshots exist
3. labels/defaults/tables/charts match
4. navigation matches
5. responsive states are reviewed
6. visual differences are listed and approved
7. no real data appears in artifacts
