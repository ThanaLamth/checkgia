# Vang SEO/AISO Ops Index

Date: 2026-06-18

Use this as the single entry point for the `/vang` improvement workflow.

Targets:

- `https://checkgia.com/vang`
- `https://checkgia.com/vang/nhan-9999`

## 1. Dev Handoff

Start here when assigning work to engineering:

- `docs/vang-dev-prompt.md`

Supporting implementation specs:

- `docs/vang-hub-content-spec.md`
- `docs/nhan-9999-content-spec.md`
- `docs/nhan-9999-savings-widget-spec.md`

Use this stage for:

- implementation scope
- priorities
- definition of done
- delivery artifacts engineering must provide

## 2. Post-Deploy Automated Check

Use these when the build is live on staging or production:

- `scripts/check-vang-page.py`
- `.github/workflows/check-vang-pages.yml`
- `scripts/trigger-vang-check-dispatch.sh`
- `docs/vang-checker-dispatch-example.md`

Use this stage for:

- quick HTML-based validation
- scheduled monitoring
- post-deploy dispatch from pipeline

## 3. Manual QA

Use:

- `docs/vang-qa-checklist.md`

Use this stage for:

- mobile and layout review
- hydration symptom review
- content usefulness review
- validation of hub clarity and widget balance

## 4. Review Output

Use:

- `docs/vang-review-template.md`

Use this stage for:

- passed checks
- failed checks
- blockers
- follow-up requests to engineering
- release decision

## 5. Release Flow

Use:

- `docs/vang-release-checklist.md`

Use this stage for:

- deploy confirmation
- evidence collection
- approve / reject decision
- rerun flow after fixes

## Recommended Order

1. send `docs/vang-dev-prompt.md` to engineering
2. give supporting specs with it
3. after deploy, run checker locally or via GitHub Action
4. run manual QA with `docs/vang-qa-checklist.md`
5. write review using `docs/vang-review-template.md`
6. finalize approval with `docs/vang-release-checklist.md`

## Minimal File Set By Role

For engineering:

- `docs/vang-dev-prompt.md`
- `docs/vang-hub-content-spec.md`
- `docs/nhan-9999-content-spec.md`
- `docs/nhan-9999-savings-widget-spec.md`

For QA:

- `docs/vang-qa-checklist.md`
- `docs/vang-review-template.md`
- `scripts/check-vang-page.py`

For release / ops:

- `docs/vang-release-checklist.md`
- `.github/workflows/check-vang-pages.yml`
- `scripts/trigger-vang-check-dispatch.sh`
- `docs/vang-checker-dispatch-example.md`

## Fast Start

If someone only asks “what files do I need?”, send them:

1. `docs/vang-ops-index.md`
2. `docs/vang-dev-prompt.md`
3. `docs/vang-qa-checklist.md`
4. `docs/vang-release-checklist.md`
