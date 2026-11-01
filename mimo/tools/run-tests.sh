#!/usr/bin/env bash
# اجرای همهٔ آزمون‌های پیش‌نمایش با شمارش واقعی
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MIMO="$(cd "$HERE/.." && pwd)"
PY="${PYTHON:-python3}"
if [ -x "$MIMO/.runtime/epm-venv/bin/python" ]; then PY="$MIMO/.runtime/epm-venv/bin/python"; fi
fail=0
if [ ! -d "$MIMO/tests/node_modules" ]; then
  echo "── نصب وابستگی آزمون‌های DOM (jsdom)"
  ( cd "$MIMO/tests" && npm install --registry=https://registry.npmjs.org --no-audit --no-fund >/dev/null 2>&1 ) \
    || { echo "نصب jsdom ناموفق بود؛ آزمون‌های DOM اجرا نمی‌شوند"; fail=1; }
fi
run() { echo; echo "── $1"; shift; "$@" || fail=1; }

run "هم‌ارزی قرارداد (۱۶)" node --test "$MIMO/learn/tests/parity.test.mjs"
run "DOM موتور یادگیری (۶)" bash -c "cd '$MIMO/tests' && node --test dom.test.mjs"
run "ماندگاری (۳)" bash -c "cd '$MIMO/tests' && node --test persistence.test.mjs"
run "لایهٔ فارسی/RTL (۳)" bash -c "cd '$MIMO/tests' && node --test overlay.test.mjs"
run "اعتبارسنج‌ها (۱۲)" "$PY" -m pytest "$MIMO/tests/test_validators.py" -q
run "آزمون سرتاسری EPM (۱۰)" bash -c "cd '$MIMO/content-templates/epm-question-bank' && $PY tools/e2e_exam_test.py"

echo
if [ "$fail" -eq 0 ]; then
  echo "✅ همهٔ مجموعه‌ها موفق"
else
  echo "❌ دست‌کم یک مجموعه شکست خورد (جزئیات بالا)"; exit 1
fi
