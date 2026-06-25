# GUI Spec For `check-vang-page.py`

Related files:

- `scripts/check-vang-page.py`
- `docs/vang-ops-index.md`
- `docs/vang-qa-checklist.md`

Date: 2026-06-25

## Purpose

This document describes how a GUI wrapper should expose the current audit logic in:

- `scripts/check-vang-page.py`

The goal is to keep GUI behavior aligned with the script, not invent a different audit standard.

## Scope

The GUI should act as a frontend for the existing HTML-source audit.

It should not assume:

- browser rendering
- JavaScript execution
- layout testing
- visual regression testing

Those remain outside the script scope.

## Core Behavior

The script:

1. fetches one or more URLs over HTTP
2. reads raw HTML
3. runs rule-based PASS/FAIL checks
4. prints results per URL
5. returns non-zero exit code if any failure exists

The GUI should preserve the same behavior model.

## Input Model

The GUI should support:

1. zero URLs entered
2. one URL entered
3. multiple URLs entered

If zero URLs are entered, the GUI should use the script defaults:

- `https://checkgia.com/vang`
- `https://checkgia.com/vang/nhan-9999`

Recommended input UI:

- multi-line textarea or tag input for URLs
- one URL per line

## Execution Model

When the user clicks `Run audit`, the GUI should:

1. collect the URL list
2. pass them to the script
3. capture stdout
4. capture exit code
5. convert result lines into structured UI output

The GUI should not reimplement the audit logic separately if avoidable.

Preferred integration:

- call the Python script directly
- parse its output

## Output Model

The GUI should show:

1. one result section per URL
2. each PASS/FAIL line as a discrete check item
3. total failure count
4. overall status

Suggested overall statuses:

- `Pass` when total failures is `0`
- `Fail` when total failures is greater than `0`
- `Error` when the script cannot execute or output cannot be parsed

## Result Line Structure

Each check line should map to:

- `status`
- `label`
- `detail` (optional)

Examples:

- `[PASS] title present - Giá vàng hôm nay ...`
- `[FAIL] FAQPage removed`

Suggested parsed structure:

```json
{
  "status": "PASS",
  "label": "title present",
  "detail": "Giá vàng hôm nay ..."
}
```

## URL Section Structure

Each audited URL should be represented as:

```json
{
  "url": "https://checkgia.com/vang",
  "checks": [
    {
      "status": "PASS",
      "label": "title present",
      "detail": "..."
    }
  ],
  "failures": 0
}
```

## Top-Level Result Structure

Suggested top-level response model:

```json
{
  "urls": [
    {
      "url": "https://checkgia.com/vang",
      "checks": [],
      "failures": 0
    }
  ],
  "total_failures": 0,
  "exit_code": 0,
  "overall_status": "Pass"
}
```

## Checks The GUI Must Support

The GUI should not hardcode only two pages conceptually, but it should display the current script behavior accurately.

### Common Checks For All URLs

The script currently emits these labels:

1. `title present`
2. `canonical present`
3. `canonical matches target URL`
4. `meta description present`
5. `H1 present`
6. `page is indexable (no noindex)`
7. `slang removed: mày`
8. `slang removed: tao`
9. `slang removed: cross threshold`
10. `slang removed: magic link`

### Additional Checks For `/vang`

If the URL is exactly:

- `https://checkgia.com/vang`

the script currently emits:

1. `FAQPage removed`
2. `Organization present`
3. `BreadcrumbList present`
4. `entity page linked`
5. `brand page linked`
6. `history page linked`

### Additional Checks For `/vang/nhan-9999`

If the URL is exactly:

- `https://checkgia.com/vang/nhan-9999`

the script currently emits:

1. `FAQPage removed`
2. `Dataset removed`
3. `Product present`
4. `AggregateOffer present`
5. `BreadcrumbList present`
6. `hero has no placeholder`
7. `answer summary present`
8. `KPI card: hôm qua`
9. `KPI card: 7 ngày`
10. `KPI card: 30 ngày`
11. `KPI card: 1 năm`
12. `spread mentioned`
13. `savings widget not yet required on live page`
14. `freshness/timestamp visible`

### Custom URL Mode

If the URL is neither:

- `https://checkgia.com/vang`
- `https://checkgia.com/vang/nhan-9999`

the script currently emits:

- `custom URL mode - only common checks applied`

The GUI should display this as an informational PASS line.

## Error Handling

If fetching a URL fails, the script emits:

- `fetch`

with `FAIL` and the exception detail.

The GUI should:

1. show this clearly at the top of the affected URL section
2. mark that URL section as failed
3. continue displaying other URL results if available

## Recommended UI Layout

Recommended sections:

1. URL input area
2. Run button
3. Summary bar
4. Per-URL result cards
5. Export actions

### Summary Bar

Should show:

- number of URLs audited
- total failures
- overall status

### Per-URL Card

Each URL card should show:

- URL
- pass/fail badge
- failure count
- grouped check list

Recommended grouping:

- Common checks
- Hub checks
- Entity checks
- Info / custom mode

## Sorting And Highlighting

Recommended behavior:

1. show FAIL checks before PASS checks inside each group
2. highlight failed labels in red
3. keep detail text visible without extra clicks where possible

## Export Options

Recommended exports:

1. plain text
2. JSON

Plain text export should preserve the script-like output.

JSON export should use a structured form similar to the examples in this document.

## Non-Goals

The GUI should not imply that this tool verifies:

- Core Web Vitals
- mobile rendering fidelity
- visual design quality
- JavaScript hydration quality in a real browser
- Google Search Console performance

Those are separate QA or SEO audit layers.

## Future-Friendly Note

The GUI should be built so new check labels can be added later without changing the UI architecture.

The safe assumption is:

- labels may increase
- some labels may change wording
- more page-specific branches may be added in the script

So the UI should prefer dynamic rendering over rigid hardcoded slots.
