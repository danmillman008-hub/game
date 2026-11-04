#!/usr/bin/env bash
# TOOLS/install.sh — full, isolated install of the temporary Mimo analysis toolchain.
# Never writes into mimo-ui/UPGRADE, ZIP, MANIFEST, verifier, or the v12 Drive plan.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
echo "repo root: $ROOT"

# 1) Both upstream repos, complete, pinned, in this separate GitHub folder.
if [[ -f .gitmodules ]]; then
  git submodule sync --recursive
  git submodule update --init --recursive
else
  echo '!! .gitmodules missing — run from a checkout of arena/aebb90b7-game' >&2
  exit 1
fi

# 2) REA CLI + real decompiler binaries, delivered through the ALLOWED npm registry.
mkdir -p TOOLS/_npm
if [[ ! -f TOOLS/_npm/node_modules/jadx-mcp/jadx-mcp.jar ]]; then
  ( cd TOOLS/_npm && npm init -y >/dev/null 2>&1 || true
    npm install --no-audit --no-fund \
      rea-agents@6.7.0 \
      jadx-mcp@1.4.1 \
      apktool-jar@2.4.1 \
      @mishguru/jadx-node@3.1.0 )
fi

# 3) JDK + androguard through the ALLOWED PyPI index.
mkdir -p TOOLS/_pylib
if [[ ! -d TOOLS/_pylib/jdk4py ]]; then
  python3 -m pip install --no-deps --target TOOLS/_pylib \
    'jdk4py==25.0.2.1' 'androguard==4.1.4'
fi
JAVA="$ROOT/TOOLS/_pylib/jdk4py/java-runtime/bin/java"

# 4) Optional: official Ghidra release binary (needs unrestricted network;
#    on this sandbox the GitHub Actions workflow mimo-re-toolchain.yml does it).
if [[ "${1:-}" == "--with-ghidra-release" ]]; then
  URL="${GHIDRA_ZIP_URL:-https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_12.2_build/ghidra_12.2_PUBLIC_20261016.zip}"
  echo "fetching $URL"
  curl -fL --retry 3 -o TOOLS/_npm/ghidra.zip "$URL"
  mkdir -p TOOLS/_ghidra_release
  unzip -q -o TOOLS/_npm/ghidra.zip -d TOOLS/_ghidra_release
  echo "installed: $(find TOOLS/_ghidra_release -maxdepth 1 -mindepth 1 -type d -name 'ghidra_*' | head -1)"
fi

echo
echo '=== installed toolchain ==='
printf '  %-34s %s\n' 'Ghidra source files' "$(find TOOLS/ghidra -type f | wc -l)"
printf '  %-34s %s\n' 'REA source files' "$(find TOOLS/rea -type f | wc -l)"
printf '  %-34s %s\n' 'java' "$("$JAVA" -version 2>&1 | head -1)"
printf '  %-34s %s\n' 'JADX MCP jar' "$(stat -c '%s bytes' TOOLS/_npm/node_modules/jadx-mcp/jadx-mcp.jar)"
printf '  %-34s %s\n' 'apktool jar' "$(stat -c '%s bytes' TOOLS/_npm/node_modules/apktool-jar/bin/apktool_2.4.1.jar)"
printf '  %-34s %s\n' 'REA CLI' "$(test -x TOOLS/_npm/node_modules/.bin/rea-agents && echo present || echo MISSING)"
echo
echo 'NOTE: jdk4py ships java.compiler but not the jdk.compiler module / javac;'
echo '      REA doctor will still report that limitation. JADX and apktool run fine.'
