#!/usr/bin/env bash
# Clone, pin, prepare and install the two independent engines. Idempotent and safe to re-run.
#
#   mimo/engines/src/epm           → cloned at the pinned commit, frontend built with base=/practice/
#   mimo/engines/src/learnharness  → cloned at the pinned commit, basePath=/max added
#
# Nothing here touches an existing database: EPM data goes to mimo/.runtime/epm-data and LearnHarness to
# mimo/.runtime/lh-data, both created fresh and excluded from git.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MIMO="$(cd "$HERE/.." && pwd)"
SRC="$MIMO/engines/src"
RUNTIME="$MIMO/.runtime"
EPM_REPO="https://github.com/mo9652962-ai/english-multiple-choice-practice-machine.git"
LH_REPO="https://github.com/amosblomqvist/learnharness.git"
EPM_COMMIT="$(python3 -c "import json;print(json.load(open('$MIMO/engines/pins.json'))['epm']['commit_full'])")"
LH_COMMIT="$(python3 -c "import json;print(json.load(open('$MIMO/engines/pins.json'))['learnharness']['commit'])")"

say() { printf '\033[1;36m[bootstrap]\033[0m %s\n' "$*"; }
fail() { printf '\033[1;31m[bootstrap] %s\033[0m\n' "$*" >&2; exit 1; }

command -v git >/dev/null || fail "git نصب نیست"
command -v node >/dev/null || fail "Node.js نصب نیست (نسخهٔ ۲۲ یا بالاتر)"
command -v npm >/dev/null || fail "npm نصب نیست"
command -v python3 >/dev/null || fail "python3 نصب نیست"

mkdir -p "$SRC" "$RUNTIME"

# ---------- EPM ----------
if [ ! -d "$SRC/epm/.git" ]; then
  say "دریافت EPM…"
  git clone --quiet "$EPM_REPO" "$SRC/epm"
fi
if [ "$(git -C "$SRC/epm" rev-parse HEAD 2>/dev/null || true)" != "$EPM_COMMIT" ]; then
  say "تنظیم EPM روی commit $EPM_COMMIT"
  git -C "$SRC/epm" fetch --quiet origin "$EPM_COMMIT" || git -C "$SRC/epm" fetch --quiet --all
  git -C "$SRC/epm" checkout --quiet "$EPM_COMMIT"
fi

python3 "$MIMO/engines/prepare_epm.py"

if [ ! -d "$SRC/epm/frontend/node_modules" ]; then
  say "نصب وابستگی‌های EPM (چند دقیقه)…"
  ( cd "$SRC/epm/frontend" && npm install --registry=https://registry.npmjs.org --no-audit --no-fund )
fi

if [ ! -f "$SRC/epm/frontend/dist-preview/index.html" ]; then
  say "ساخت فرانت‌اند EPM با پیشوند /practice (چند دقیقه)…"
  ( cd "$SRC/epm/frontend" && VITE_API_ROOT=/practice/api npx vite build --base=/practice/ --outDir dist-preview --emptyOutDir )
fi

if [ ! -x "$RUNTIME/epm-venv/bin/python" ]; then
  say "ساخت محیط پایتون EPM…"
  python3 -m venv "$RUNTIME/epm-venv"
  "$RUNTIME/epm-venv/bin/pip" install --quiet --upgrade pip
  "$RUNTIME/epm-venv/bin/pip" install --quiet -r "$SRC/epm/requirements.txt"
fi

mkdir -p "$RUNTIME/epm-data"

# ---------- LearnHarness ----------
if [ ! -d "$SRC/learnharness/.git" ]; then
  say "دریافت LearnHarness…"
  git clone --quiet "$LH_REPO" "$SRC/learnharness"
fi
if [ "$(git -C "$SRC/learnharness" rev-parse HEAD 2>/dev/null || true)" != "$LH_COMMIT" ]; then
  say "تنظیم LearnHarness روی commit $LH_COMMIT"
  git -C "$SRC/learnharness" fetch --quiet origin "$LH_COMMIT" || git -C "$SRC/learnharness" fetch --quiet --all
  git -C "$SRC/learnharness" checkout --quiet "$LH_COMMIT"
fi

python3 "$MIMO/engines/prepare_learnharness.py"

if [ ! -d "$SRC/learnharness/node_modules" ]; then
  say "نصب وابستگی‌های LearnHarness (چند دقیقه)…"
  ( cd "$SRC/learnharness" && npm install --no-audit --no-fund )
fi

mkdir -p "$RUNTIME/lh-data"
[ -f "$RUNTIME/lh-auth.json" ] || echo '{}' > "$RUNTIME/lh-auth.json"

say "همهٔ موتورها آماده‌اند."
