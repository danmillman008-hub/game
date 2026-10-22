"""Bundle the Stage-1 reconstruction into one self-contained HTML file.

The result has no prerequisites: no server, no separate JS/CSS/PNG files, no
network access. Open it from disk and it runs.

What is inlined:
  * the page markup and styles (already inline in index.html)
  * js/game.js and the asset loader, joined into a single classic script so the
    browser needs no module fetching (which file:// blocks)
  * every PNG asset, as a base64 data URI

The transform is deliberately mechanical and checked by tests/test_bundle.py and
reconstruction/stage1/test/bundle.test.mjs: the bundle must contain no external
references and must render the same frame as the module version.
"""
from __future__ import annotations

import base64
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "reconstruction" / "stage1"
OUT = SRC / "stage1.html"

ASSETS = {
    "plate": "assets/plate.png",
    "axel_stand": "assets/axel_stand.png",
    "axel_walk": "assets/axel_walk.png",
    "axel_walk2": "assets/axel_walk2.png",
    "thug_stand": "assets/thug_stand.png",
}

# Emitted instead of js/assets.js: the same loader, but with data URIs and no
# import.meta (unavailable in a classic script and pointless in a bundle).
LOADER = """// ---- assets, inlined as data URIs -------------------------------------------
const ASSET_MANIFEST = {
%s
};

const Assets = { images: {} };

function loadImage(src) {
  return new Promise((resolve) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = () => resolve(null);
    img.src = src;
  });
}

async function loadAssets() {
  const entries = await Promise.all(
    Object.entries(ASSET_MANIFEST).map(async ([k, src]) => [k, await loadImage(src)]),
  );
  for (const [k, img] of entries) Assets.images[k] = img;
  const missing = entries.filter(([, img]) => !img).map(([k]) => k);
  return { loaded: entries.length - missing.length, missing };
}
"""


def data_uri(path: Path) -> str:
    return "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def build() -> str:
    loader_block = LOADER % "\n".join(
        f"  {name}: '{data_uri(SRC / rel)}'," for name, rel in ASSETS.items()
    )

    game = (SRC / "js" / "game.js").read_text()
    # drop the module import: the loader above is defined in the same scope
    game = re.sub(r"^import\s+\{[^}]*\}\s+from\s+'\./assets\.js';\n", "", game, flags=re.M)
    if "import " in game or "export " in game:
        raise SystemExit("game.js still contains module syntax; bundling would break")

    html = (SRC / "index.html").read_text()
    script = (
        "(function () {\n'use strict';\n"
        + loader_block
        + "\n// ---- game ----------------------------------------------------------------\n"
        + game
        + "\n})();\n"
    )

    # one classic script, inlined
    html = html.replace(
        '<script type="module" src="js/game.js"></script>',
        "<script>\n" + script + "</script>",
    )
    # a note in the head so the file explains itself when opened directly
    html = html.replace(
        "<title>",
        "<!-- Self-contained build: every asset is embedded, no server needed. -->\n<title>",
    )
    return html


def main() -> int:
    missing = [p for p in ASSETS.values() if not (SRC / p).exists()]
    if missing:
        print("missing assets, run the extraction tools first:", missing)
        return 1
    html = build()
    OUT.write_text(html)

    # --- self-checks -------------------------------------------------------
    problems = []
    for pat, why in [
        (r'src="(?!data:)', "external src attribute"),
        (r'href="(?!data:|#)', "external href attribute"),
        (r"\bimport\s", "module import"),
        (r"\bimport\.meta\b", "import.meta"),
        (r"/assets/", "path reference to the assets directory"),
        (r'type="module"', "module script"),
    ]:
        if re.search(pat, html):
            problems.append(f"{why} ({pat})")

    print(f"bundle: {OUT}")
    print(f"  size      {len(html):,} bytes")
    print(f"  assets    {len(ASSETS)} inlined as data URIs")
    print(f"  scripts   {html.count('<script')} inline, 0 external")
    if problems:
        print("  PROBLEMS:", *problems, sep="\n    ")
        return 1
    print("  self-check no external references: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
