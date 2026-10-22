"""Inline the browser engine into a single, self-contained playable HTML file.

    python -m prototype.tools.make_web

Reads  prototype/web/shell.html   (page, styles, input, 60 Hz loop)
       prototype/web/neon_alley.js (the conformance-tested JS port)
Writes prototype/release/index.html            (the playable page; served as the preview)
       prototype/release/neon_alley_play.html  (identical copy, explicit name)

The result has no <script src>, no fetch, no CDN and no assets: open it from the
filesystem and it plays. The build fails if any external reference sneaks in.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SHELL = ROOT / "prototype" / "web" / "shell.html"
ENGINE = ROOT / "prototype" / "web" / "neon_alley.js"
RELEASE = ROOT / "prototype" / "release"

PLACEHOLDER = "/*__ENGINE__*/"
EXTERNAL = re.compile(r'(<script[^>]+src=)|(<link[^>]+href=)|(https?://)|(@import)', re.I)


def build() -> Path:
    shell = SHELL.read_text(encoding="utf-8")
    engine = ENGINE.read_text(encoding="utf-8")

    if "</script" in engine:
        raise SystemExit("engine contains a closing script tag; cannot inline safely")
    if PLACEHOLDER not in shell:
        raise SystemExit(f"placeholder {PLACEHOLDER} missing from {SHELL.name}")

    page = shell.replace(PLACEHOLDER, engine)
    matches = [m.group(0) for m in EXTERNAL.finditer(page)]
    if matches:
        raise SystemExit("page is not self-contained, found: " + ", ".join(sorted(set(matches))))

    RELEASE.mkdir(parents=True, exist_ok=True)
    out = RELEASE / "index.html"
    out.write_text(page, encoding="utf-8")
    (RELEASE / "neon_alley_play.html").write_text(page, encoding="utf-8")

    digest = hashlib.sha256(page.encode("utf-8")).hexdigest()
    print(f"wrote {out.relative_to(ROOT)} ({len(page) / 1024:.0f} KiB, "
          f"{len(page.splitlines())} lines)")
    print(f"wrote {Path('prototype/release/neon_alley_play.html')} (identical copy)")
    print(f"sha256 {digest}")
    print("self-contained: no script/link/url references")
    return out


if __name__ == "__main__":
    build()
    sys.exit(0)
