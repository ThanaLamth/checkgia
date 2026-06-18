# Repository Dispatch Example For Vang Checker

Related files:

- `.github/workflows/check-vang-pages.yml`
- `scripts/trigger-vang-check-dispatch.sh`

Date: 2026-06-18

## Purpose

Use this when the deploy pipeline should trigger the gold-page checker right after release.

The workflow already accepts:

- `workflow_dispatch`
- `repository_dispatch`
- scheduled runs

For deploy integration, use `repository_dispatch`.

## Event Type

Use:

- `check-vang-pages`

## Required Secret

The caller needs a GitHub token that can dispatch workflows for:

- `ThanaLamth/checkgia`

Recommended env var:

- `GITHUB_TOKEN`

## Example With Script

```bash
export GITHUB_TOKEN=YOUR_TOKEN
bash scripts/trigger-vang-check-dispatch.sh
```

Custom URLs:

```bash
export GITHUB_TOKEN=YOUR_TOKEN
bash scripts/trigger-vang-check-dispatch.sh \
  "https://staging.checkgia.com/vang" \
  "https://staging.checkgia.com/vang/nhan-9999"
```

Optional custom repo:

```bash
export GITHUB_TOKEN=YOUR_TOKEN
export GITHUB_REPOSITORY_NAME="ThanaLamth/checkgia"
bash scripts/trigger-vang-check-dispatch.sh
```

## Raw API Example

```bash
curl -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.github.com/repos/ThanaLamth/checkgia/dispatches \
  -d '{
    "event_type": "check-vang-pages",
    "client_payload": {
      "hub_url": "https://checkgia.com/vang",
      "entity_url": "https://checkgia.com/vang/nhan-9999"
    }
  }'
```

## Expected Behavior

After dispatch:

1. GitHub Actions starts `Check Vang Pages`
2. the workflow uses the provided URLs if present
3. the run fails if the checker finds SEO or SSR issues

## Deploy Hook Recommendation

Call the dispatch only after:

1. deploy finished successfully
2. target URLs are publicly reachable
3. caches that affect HTML output are already refreshed

## Suggested Team Usage

- production deploy: dispatch against live URLs
- staging deploy: dispatch against staging URLs first
- use the failing run URL as QA evidence in the release thread
