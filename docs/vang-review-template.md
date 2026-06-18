# Review Template For `/vang` After Dev Delivery

Date: 2026-06-18

Use this after engineering says the work is done.

Companion files:

- `docs/vang-dev-prompt.md`
- `docs/vang-qa-checklist.md`
- `scripts/check-vang-page.py`

## Inputs

- environment reviewed:
  - production / staging / local
- URLs reviewed:
  - `/vang`
  - `/vang/nhan-9999`
- checker command used:
  - `python3 scripts/check-vang-page.py ...`

## Review Output

### 1. Passed Checks

- list checks that are now clearly fixed
- include SSR-related passes separately
- include schema-related passes separately

### 2. Failed Checks

- list each failed check with:
  - page
  - exact issue
  - evidence from rendered HTML or visible UI

Recommended format:

- `/vang`: `FAQPage` still present in JSON-LD
- `/vang/nhan-9999`: hero still shows placeholder `—` in rendered HTML

### 3. Blockers

- note anything that prevents release
- note anything that makes Google indexing/understanding weaker

Typical blockers:

- primary hero values still client-only
- canonical wrong
- page accidentally noindexed
- stale or misleading freshness copy

### 4. Requested Follow-Up Changes

Write these as direct implementation requests to dev.

Format:

1. issue
2. why it matters
3. exact requested fix

Example:

1. `/vang/nhan-9999` hero still renders placeholder values in initial HTML.
2. This weakens indexability and answer extraction because the key numbers are not present in SSR output.
3. Move hero data fetch to server render path and ensure buy, sell, source, and update time are present in initial HTML.

### 5. Release Decision

Choose one:

- approve
- approve with minor follow-up
- do not approve yet

### 6. Evidence To Attach

- checker output
- view-source snippet or fetched HTML snippet
- screenshots only if they help explain a visual regression
