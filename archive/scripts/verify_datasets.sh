#!/usr/bin/env bash
# Verify dataset archive integrity against SHA256SUMS.
# Usage: bash scripts/verify_datasets.sh [HACKATHON_DIR]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
HACKATHON_DIR="${1:-$SCRIPT_DIR/../hackathon}"
SUMS_FILE="$HACKATHON_DIR/SHA256SUMS"

if [[ ! -f "$SUMS_FILE" ]]; then
    echo "❌ SHA256SUMS not found: $SUMS_FILE"
    exit 1
fi

cd "$HACKATHON_DIR"

echo "🔍 Verifying dataset checksums in $HACKATHON_DIR ..."
if sha256sum -c "$SUMS_FILE"; then
    echo ""
    echo "✅ All dataset archives verified."
else
    echo ""
    echo "❌ Checksum mismatch — dataset archives may be corrupted."
    exit 1
fi
