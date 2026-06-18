# QA Checklist For `/vang` And `/vang/nhan-9999`

Date: 2026-06-18

Targets:

- `https://checkgia.com/vang`
- `https://checkgia.com/vang/nhan-9999`

Companion files:

- `docs/vang-dev-prompt.md`
- `docs/vang-hub-content-spec.md`
- `docs/vang-checker-dispatch-example.md`
- `docs/vang-review-template.md`
- `scripts/check-vang-page.py`

## 1. Run Automated Checks First

Command:

```bash
python3 scripts/check-vang-page.py
```

Optional custom URLs:

```bash
python3 scripts/check-vang-page.py https://checkgia.com/vang https://checkgia.com/vang/nhan-9999
```

Recommended for staging review:

```bash
python3 scripts/check-vang-page.py https://staging.checkgia.com/vang https://staging.checkgia.com/vang/nhan-9999
```

GitHub Action:

- `.github/workflows/check-vang-pages.yml`
- can run by `workflow_dispatch`, `repository_dispatch`, or schedule
- dispatch example: `docs/vang-checker-dispatch-example.md`

## 2. Manual QA For `/vang`

### Metadata

- title is present
- meta description is present
- canonical points to `/vang`

### Structured Data

- `FAQPage` is removed
- `Organization` exists
- `BreadcrumbList` exists

### Hub Clarity

- the page clearly explains what the gold section covers
- the page helps users choose between:
  - product pages
  - brand pages
  - historical date pages

### Tone

- no slang like:
  - `mày`
  - `Tao`
  - `cross threshold`

### Internal Links

- entity pages are linked
- brand pages are linked
- historical paths are linked

## 3. Manual QA For `/vang/nhan-9999`

### Metadata

- title is present
- meta description is present
- canonical points to `/vang/nhan-9999`

### Structured Data

- `FAQPage` is removed
- `Dataset` is removed
- `Product` exists
- `AggregateOffer` exists
- `BreadcrumbList` exists

### Hero SSR

- best source is visible in HTML
- best sell price is visible in HTML
- buy price is visible in HTML
- sell price is visible in HTML
- no placeholder `—` in the main hero price fields

### Freshness

- timestamps are visible
- freshness wording does not overstate certainty
- stale data is clearly flagged if applicable

### Answer Layer

- the page contains a short textual answer summary
- the summary states:
  - current lowest price
  - source
  - spread or freshness context

### KPI Row

- `So với hôm qua` exists
- `So với 7 ngày` exists
- `So với 30 ngày` exists
- `So với 1 năm` exists

### Source Table

- source names are visible
- buy prices are visible
- sell prices are visible
- spread is visible
- freshness per source is visible

### Savings Widget

- widget exists
- widget stays compact
- widget does not overpower the main gold intent

### FAQ Tone

- neutral Vietnamese
- no slang
- no overlong filler answers

## 4. Regression Checks

### Rendering

- page still loads without broken layout
- mobile layout still works
- no obvious hydration mismatch in main user-facing blocks

### Content Integrity

- structured data still matches visible content
- timestamps and prices are consistent between hero and table

### Navigation

- links to history, brand pages, and calculators still work

## 5. Fail Conditions

Request more dev work if any of these are true:

- hero on `/vang/nhan-9999` still shows `—`
- `FAQPage` remains on `/vang`
- `FAQPage` or `Dataset` remains on `/vang/nhan-9999`
- FAQ still uses slang
- no direct answer summary exists
- no KPI row exists
- savings widget turns into a large rate-comparison block

## 6. Review Output Format

When re-reviewing after implementation, report:

1. passed checks
2. failed checks
3. blockers
4. requested follow-up changes

Use:

- `docs/vang-review-template.md`
