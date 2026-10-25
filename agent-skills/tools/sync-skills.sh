#!/usr/bin/env bash
# نصب / به‌روزرسانی مهارت‌ها در agent-skills/vendor/
#
#   bash agent-skills/tools/sync-skills.sh            # نصب نسخه‌های پین‌شده در registry.json
#   bash agent-skills/tools/sync-skills.sh --latest   # گرفتن HEAD روزِ upstream و پیشنهاد commit جدید
#
# نکته: هیچ‌وقت --latest را بدون بازبینی مستقیم وارد برنچ اصلی نکنید.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"     # agent-skills/
REPO="$(cd "$ROOT/.." && pwd)"
VENDOR="$ROOT/vendor"
MODE="${1:---pinned}"

command -v git >/dev/null || { echo "git لازم است"; exit 1; }

# id|repo|sha
read_sources() {
  python3 - "$ROOT/registry.json" <<'PY'
import json, sys
for s in json.load(open(sys.argv[1]))["sources"]:
    print(f"{s['id']}|{s['repo']}|{s['commit']}")
PY
}

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

while IFS='|' read -r id repo sha; do
  ref="$sha"
  [ "$MODE" = "--latest" ] && ref="main"
  echo "→ $repo @ ${ref:0:10}  →  vendor/$id"
  rm -rf "$TMP/$id"
  git clone -q --depth 1 "https://github.com/$repo.git" "$TMP/$id"
  if [ "$MODE" = "--pinned" ]; then
    git -C "$TMP/$id" fetch -q --depth 1 origin "$sha" && git -C "$TMP/$id" checkout -q "$sha"
  fi
  actual="$(git -C "$TMP/$id" rev-parse HEAD)"
  rm -rf "$TMP/$id/.git"
  # چیزهایی که لازم نداریم (هم‌راستا با registry)
  case "$id" in
    chrisbanes-skills)             rm -rf "$TMP/$id/evals" ;;
    compose-kotlin-agent-skills)   rm -rf "$TMP/$id/assets" "$TMP/$id/marketing" ;;
  esac
  rm -rf "${VENDOR:?}/$id"
  cp -a "$TMP/$id" "$VENDOR/$id"
  echo "   commit=$actual"
  if [ "$MODE" = "--latest" ] && [ "$actual" != "$sha" ]; then
    echo "   ⚠ registry می‌گوید ${sha:0:10} — اگر تغییر را پذیرفتید، registry.json را به‌روز کنید"
  fi
done < <(read_sources)

echo
python3 "$ROOT/tools/build_index.py"
python3 "$ROOT/tools/check.py"
echo "تمام. تغییرات را بازبینی و commit کنید:"
echo "  git -C \"$REPO\" status --short agent-skills | head"
