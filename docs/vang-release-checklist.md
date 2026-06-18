# Release Checklist For `/vang` And `/vang/nhan-9999`

Related files:

- `docs/vang-dev-prompt.md`
- `docs/vang-hub-content-spec.md`
- `docs/vang-qa-checklist.md`
- `docs/vang-review-template.md`
- `docs/vang-checker-dispatch-example.md`
- `.github/workflows/check-vang-pages.yml`
- `scripts/check-vang-page.py`
- `scripts/trigger-vang-check-dispatch.sh`

Date: 2026-06-18

## Purpose

Use this checklist after engineering deploys changes for:

- `https://checkgia.com/vang`
- `https://checkgia.com/vang/nhan-9999`

This is the operational flow for:

1. deploy confirmation
2. automated checker run
3. manual QA
4. release decision
5. follow-up request if needed

## 1. Confirm Deploy Inputs

Before running QA, confirm:

1. the target environment:
   - production / staging
2. the exact URLs to review
3. the deploy is finished successfully
4. HTML-affecting cache is already refreshed
5. engineering provided:
   - changed file list
   - staging or production URLs
   - proof that hero SSR is in rendered HTML

Do not start final review before those inputs are available.

## 2. Trigger Automated Check

Choose one method.

### Option A: Run Locally

```bash
python3 scripts/check-vang-page.py
```

For staging:

```bash
python3 scripts/check-vang-page.py \
  "https://staging.checkgia.com/vang" \
  "https://staging.checkgia.com/vang/nhan-9999"
```

### Option B: Trigger GitHub Action Manually

Use:

- `.github/workflows/check-vang-pages.yml`

Run it with:

- default live URLs
- or custom staging URLs

### Option C: Trigger Repository Dispatch

```bash
export GITHUB_TOKEN=YOUR_TOKEN
bash scripts/trigger-vang-check-dispatch.sh
```

For staging:

```bash
export GITHUB_TOKEN=YOUR_TOKEN
bash scripts/trigger-vang-check-dispatch.sh \
  "https://staging.checkgia.com/vang" \
  "https://staging.checkgia.com/vang/nhan-9999"
```

Reference:

- `docs/vang-checker-dispatch-example.md`

## 3. Read Automated Results

Interpret the checker output in this order:

1. fetch failures
2. indexability issues
3. canonical issues
4. schema issues
5. hero SSR issues
6. tone and slang issues
7. content block issues like missing KPI or answer layer

Immediate no-go failures:

- page cannot be fetched
- page is noindexed
- canonical is wrong
- `FAQPage` still exists where it should be removed
- `Dataset` still exists on entity page
- hero still shows placeholder `—`

## 4. Run Manual QA

Use:

- `docs/vang-qa-checklist.md`

Manual QA still matters even if the checker passes, because the script does not fully verify:

- mobile layout
- visual regression
- hydration mismatch symptoms
- whether a widget becomes too visually dominant
- whether copy is genuinely useful rather than only technically present

## 5. Collect Evidence

Attach:

1. checker output
2. HTML snippet or view-source proof for hero SSR
3. screenshot only if needed for UI issues
4. links to the reviewed environment

Minimum evidence for approval:

- `/vang` HTML confirms indexable output and removed `FAQPage`
- `/vang/nhan-9999` HTML confirms real hero values and removed `FAQPage` / `Dataset`

## 6. Write Review Outcome

Use:

- `docs/vang-review-template.md`

Fill in:

1. passed checks
2. failed checks
3. blockers
4. requested follow-up changes
5. release decision

## 7. Decide Release Status

Choose one:

### Approve

Use when:

- checker is clean or only has trivial non-blocking follow-up
- manual QA finds no important issue
- evidence supports SSR and schema fixes

### Approve With Minor Follow-Up

Use when:

- the page is releasable
- remaining issues do not weaken indexability or trust materially

Example:

- a copy improvement is still desirable, but core SSR/schema/navigation work is correct

### Do Not Approve Yet

Use when any blocker remains.

Typical blockers:

- hero values still client-only
- hub page still has poor or slangy FAQ
- savings widget overpowers main gold intent
- timestamps or freshness language are misleading

## 8. Send Follow-Up To Engineering

When there are failures, send:

1. exact page
2. exact failed condition
3. why it matters
4. requested implementation fix
5. evidence

Recommended format:

1. `/vang/nhan-9999` still shows placeholder hero values in initial HTML.
2. This weakens indexability and answer extraction for the page’s primary numbers.
3. Move the hero data path fully into SSR and ensure source, buy, sell, and update time are present in rendered HTML.
4. Evidence: checker failure plus view-source snippet attached.

## 9. Re-Run After Fix

After engineering ships the follow-up:

1. rerun the automated checker
2. rerun the manual QA sections affected
3. update the review template
4. make a final release decision

## Definition Of Done

This release flow is complete when:

1. deploy is verified
2. checker has been run
3. manual QA has been completed
4. review output is written
5. approval or rejection is explicit
6. follow-up requests, if any, are concrete and evidenced
