#!/usr/bin/env bash
set -euo pipefail

if [[ -z "${GITHUB_TOKEN:-}" ]]; then
  echo "GITHUB_TOKEN is required" >&2
  exit 1
fi

REPO="${GITHUB_REPOSITORY_NAME:-ThanaLamth/checkgia}"
EVENT_TYPE="${EVENT_TYPE:-check-vang-pages}"
HUB_URL="${1:-${HUB_URL:-https://checkgia.com/vang}}"
ENTITY_URL="${2:-${ENTITY_URL:-https://checkgia.com/vang/nhan-9999}}"

API_URL="https://api.github.com/repos/${REPO}/dispatches"

curl --fail --silent --show-error \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer ${GITHUB_TOKEN}" \
  "$API_URL" \
  -d @- <<EOF
{
  "event_type": "${EVENT_TYPE}",
  "client_payload": {
    "hub_url": "${HUB_URL}",
    "entity_url": "${ENTITY_URL}"
  }
}
EOF

echo "Triggered ${EVENT_TYPE} for ${REPO}"
echo "hub_url=${HUB_URL}"
echo "entity_url=${ENTITY_URL}"
