#!/usr/bin/env bash
# اجرای پیش‌نمایش میمو: پوستهٔ فارسی + موتور آفلاین یادگیری + EPM (تمرین) + LearnHarness (مکس)
#
#   ./start-preview.sh              → http://localhost:4000
#   ./start-preview.sh --no-engines → فقط پوسته و موتور یادگیری (بدون EPM/LH)
#
# هر سه سرویس روی همین ماشین اجرا می‌شوند؛ فقط یک پورت به مرورگر داده می‌شود و بقیه پشت پروکسی میمانند.
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RUNTIME="$HERE/.runtime"
LOGS="$RUNTIME/logs"
PORT="${PREVIEW_PORT:-4000}"
EPM_PORT="${EPM_PORT:-8765}"
LH_PORT="${LH_PORT:-3000}"
NO_ENGINES=0
[ "${1:-}" = "--no-engines" ] && NO_ENGINES=1

mkdir -p "$LOGS" "$RUNTIME/epm-data" "$RUNTIME/lh-data"
PIDS=()

say()  { printf '\033[1;36m[میمو]\033[0m %s\n' "$*"; }
warn() { printf '\033[1;33m[میمو]\033[0m %s\n' "$*"; }
bad()  { printf '\033[1;31m[میمو]\033[0m %s\n' "$*"; }

cleanup() {
  warn "در حال توقف سرویس‌ها…"
  for pid in "${PIDS[@]:-}"; do
    kill "$pid" 2>/dev/null || true
  done
  wait 2>/dev/null || true
}
trap cleanup EXIT INT TERM

wait_http() { # url, seconds, label
  local url="$1" limit="$2" label="$3" i=0
  while [ "$i" -lt "$limit" ]; do
    if curl -fsS -o /dev/null --max-time 2 "$url" 2>/dev/null; then say "$label آماده است"; return 0; fi
    i=$((i + 1)); sleep 1
  done
  warn "$label در ${limit} ثانیه پاسخ نداد (فایل گزارش: $LOGS)"
  return 1
}

command -v python3 >/dev/null || { bad "python3 نصب نیست"; exit 1; }

if [ "$NO_ENGINES" -eq 0 ]; then
  if [ ! -f "$HERE/engines/src/epm/frontend/dist-preview/index.html" ] || [ ! -d "$HERE/engines/src/learnharness/node_modules" ]; then
    say "موتورها آماده نیستند؛ یک‌بار نصب لازم است."
    bash "$HERE/tools/bootstrap_engines.sh" || bad "نصب موتورها کامل نشد؛ پیش‌نمایش بدون آن‌ها اجرا می‌شود."
  fi
fi

if [ "$NO_ENGINES" -eq 0 ] && [ -x "$RUNTIME/epm-venv/bin/python" ]; then
  say "اجرای EPM روی 127.0.0.1:$EPM_PORT"
  ( cd "$HERE/engines/src/epm" && \
    EPM_DATA_DIR="$RUNTIME/epm-data" \
    EPM_FRONTEND_DIST="$HERE/engines/src/epm/frontend/dist-preview" \
    EPM_AUTH=0 EPM_PORT="$EPM_PORT" EPM_HOST=127.0.0.1 \
    "$RUNTIME/epm-venv/bin/python" backend/standalone_main.py >"$LOGS/epm.log" 2>&1 ) &
  PIDS+=($!)
  wait_http "http://127.0.0.1:$EPM_PORT/api/health" 60 "EPM" || warn "بخش «تمرین و آزمون» غیرفعال خواهد بود"
fi

if [ "$NO_ENGINES" -eq 0 ] && [ -d "$HERE/engines/src/learnharness/node_modules" ]; then
  say "اجرای LearnHarness روی 127.0.0.1:$LH_PORT"
  ( cd "$HERE/engines/src/learnharness" && \
    LH_DATA_DIR="$RUNTIME/lh-data" LH_AUTH_FILE="$RUNTIME/lh-auth.json" \
    npx next dev --port "$LH_PORT" >"$LOGS/learnharness.log" 2>&1 ) &
  PIDS+=($!)
  wait_http "http://127.0.0.1:$LH_PORT/max" 120 "LearnHarness (Max)" || warn "بخش «مکس» غیرفعال خواهد بود"
fi

say "پوستهٔ میمو روی http://localhost:$PORT"
say "پورت‌ها: پوسته $PORT · EPM $EPM_PORT · LearnHarness $LH_PORT (دو مورد آخر فقط محلی‌اند)"
say "برای توقف: Ctrl+C"
PREVIEW_PORT="$PORT" EPM_URL="http://127.0.0.1:$EPM_PORT" LH_URL="http://127.0.0.1:$LH_PORT" \
  python3 "$HERE/host/preview_host.py" --port "$PORT"
