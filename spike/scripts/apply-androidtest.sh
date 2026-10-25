#!/usr/bin/env bash
# کپی تست‌های ابزارداری (instrumented) به داخل چک‌اوت Algidy.
# Usage: apply-androidtest.sh <spike-dir> <algidy-checkout>
set -euo pipefail
SPIKE="$(cd "${1:?usage: apply-androidtest.sh <spike-dir> <algidy-checkout>}" && pwd)"
ROOT="$(cd "${2:?usage: apply-androidtest.sh <spike-dir> <algidy-checkout>}" && pwd)"
DEST="$ROOT/feature/scanner/src/androidTest"

mkdir -p "$DEST"
cp -r "$SPIKE/androidtest/scanner/androidTest/." "$DEST/"
echo "instrumented tests installed:"
find "$DEST" -type f | sed "s|$ROOT/||"
