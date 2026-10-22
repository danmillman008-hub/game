"""Build the downloadable package and the self-contained HTML preview.

    python -m prototype.tools.make_release

Outputs (prototype/release/):
  neon_alley.html              one file, no network: embedded demo GIFs + art + guide
  neon_alley-prototype.zip     full source, tests, docs, screenshots, recorded input
  SHA256SUMS.txt               checksums of both
"""
from __future__ import annotations

import base64
import hashlib
import html
import os
import sys
import zipfile
from pathlib import Path

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

PROTO = ROOT / "prototype"
RELEASE = PROTO / "release"

ZIP_INCLUDE = [
    "README.md", "ARCHITECTURE.md", "RULES.md", "TEST_REPORT.md", "COMPLETION_REPORT.md",
    "__init__.py",
]
ZIP_NOTE = """Neon Alley — standalone prototype package
=========================================

This archive contains a complete, runnable copy of the prototype:
  prototype/            the game, its tests, tools, data and screenshots
  components/           the verified engine slice the game runs on

Quick start (from this directory):

    python3 -m venv .venv
    .venv/bin/pip install pygame
    .venv/bin/python -m prototype.neon_alley

Headless check:

    SDL_VIDEODRIVER=dummy .venv/bin/python -m prototype.tools.run_tests

Read prototype/README.md first. Nothing here is a remake or a port of any
existing game; see prototype/COMPLETION_REPORT.md, section 1.
"""
ZIP_DIRS = ["prototype/neon_alley", "prototype/tests", "prototype/tools",
            "prototype/data", "prototype/screenshots", "prototype/web",
            "components/sor_engine", "components/data"]

CONTROLS = [
    ("A / D", "walk left / right"),
    ("W / S", "step through the depth lanes"),
    ("SPACE", "jump (hold A or D for air control)"),
    ("J", "punch — fast, 7 damage"),
    ("K", "kick — slower, 13 damage, longer recovery"),
    ("R", "restart"),
    ("ENTER", "start from the title screen"),
    ("ESC", "quit"),
]


def b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


def build_html() -> Path:
    media = PROTO / "media"
    shots = PROTO / "screenshots"
    highlight = b64(media / "neon_alley_highlight.gif")
    full = b64(media / "neon_alley_full.gif")
    gallery = "".join(
        f'<figure><img src="data:image/png;base64,{b64(shots / name)}" alt="{html.escape(cap)}">'
        f"<figcaption>{html.escape(cap)}</figcaption></figure>"
        for name, cap in [
            ("01_title.png", "Title card with the control guide"),
            ("03_jump.png", "Jump: body airborne, shadow still on the ground"),
            ("04_punch_hit.png", "Punch connecting — spark, ring, damage number"),
            ("05_kick.png", "Kick connecting for 13"),
            ("06_wave2.png", "Wave 2: the brute closes in"),
            ("07_victory.png", "AREA CLEARED"),
            ("08_defeat.png", "YOU ARE DOWN"),
        ]
    )
    controls = "".join(f"<tr><td><kbd>{html.escape(k)}</kbd></td><td>{html.escape(v)}</td></tr>"
                       for k, v in CONTROLS)

    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Neon Alley — playable prototype</title>
<style>
  :root {{
    --ink:#07050f; --panel:#120d22; --line:#2a2144;
    --cyan:#22e6ff; --pink:#ff2d95; --amber:#ffb020; --text:#e8eefc; --dim:#9aa6c4;
  }}
  * {{ box-sizing:border-box; }}
  body {{
    margin:0; background:radial-gradient(1200px 700px at 50% -10%, #1b1035 0%, var(--ink) 60%);
    color:var(--text); font:15px/1.6 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  }}
  .wrap {{ max-width:1040px; margin:0 auto; padding:28px 20px 64px; }}
  header {{ text-align:center; margin-bottom:26px; }}
  h1 {{
    font:800 clamp(30px,6vw,54px)/1.05 ui-sans-serif,system-ui,sans-serif; margin:0 0 8px;
    letter-spacing:.06em; text-transform:uppercase;
    color:#fff; text-shadow:0 0 18px rgba(34,230,255,.65), 0 0 44px rgba(255,45,149,.45);
  }}
  .sub {{ color:var(--dim); margin:0; }}
  .badges {{ display:flex; gap:8px; justify-content:center; flex-wrap:wrap; margin:14px 0 0; }}
  .badge {{
    border:1px solid var(--line); border-radius:999px; padding:3px 12px; font-size:12.5px;
    color:var(--dim); background:#0e0a1b;
  }}
  .panel {{
    background:linear-gradient(180deg,#140f26,#0d0a1a); border:1px solid var(--line);
    border-radius:16px; padding:18px; margin:18px 0; box-shadow:0 18px 50px rgba(0,0,0,.45);
  }}
  h2 {{ font-size:15px; letter-spacing:.16em; text-transform:uppercase; color:var(--cyan);
       margin:0 0 12px; }}
  img {{ display:block; width:100%; height:auto; border-radius:10px; image-rendering:pixelated; }}
  .grid {{ display:grid; grid-template-columns:1fr 1fr; gap:18px; }}
  @media (max-width:760px) {{ .grid {{ grid-template-columns:1fr; }} }}
  table {{ width:100%; border-collapse:collapse; }}
  td {{ padding:6px 8px; border-bottom:1px solid #1d1733; font-size:14px; }}
  td:first-child {{ width:110px; }}
  kbd {{
    display:inline-block; min-width:34px; text-align:center; padding:2px 7px; border-radius:6px;
    background:#1b1430; border:1px solid #3a2f5e; border-bottom-width:2px;
    font:600 12.5px ui-monospace,SFMono-Regular,Menlo,monospace; color:#fff;
  }}
  ol {{ margin:0; padding-left:20px; }}
  li {{ margin:6px 0; }}
  code {{
    background:#191231; border:1px solid #2b2350; border-radius:6px; padding:1px 6px;
    font:13px ui-monospace,SFMono-Regular,Menlo,monospace; color:#cfe6ff;
  }}
  pre {{
    background:#0b0817; border:1px solid #241c40; border-radius:10px; padding:12px 14px;
    overflow:auto; font:13px/1.55 ui-monospace,SFMono-Regular,Menlo,monospace; color:#cfe6ff;
  }}
  a {{ color:var(--cyan); }}
  .note {{ color:var(--dim); font-size:13.5px; }}
  .downloads a {{
    display:inline-block; margin:6px 10px 0 0; padding:10px 16px; border-radius:10px;
    text-decoration:none; font-weight:700; letter-spacing:.02em;
    background:linear-gradient(180deg,#25e6ff,#12a9c9); color:#03222a;
  }}
  .downloads a.alt {{ background:linear-gradient(180deg,#ff4fa6,#c81f74); color:#2b0016; }}
  .stats {{ display:grid; grid-template-columns:repeat(4,1fr); gap:10px; text-align:center; }}
  @media (max-width:680px) {{ .stats {{ grid-template-columns:repeat(2,1fr); }} }}
  .stat {{ background:#0c0918; border:1px solid var(--line); border-radius:12px; padding:10px; }}
  .stat b {{ display:block; font-size:20px; color:#fff; }}
  .stat span {{ font-size:12px; color:var(--dim); }}
  figure {{ margin:0; }}
  figcaption {{ color:var(--dim); font-size:12.5px; margin-top:6px; }}
  footer {{ color:#6d7794; font-size:12.5px; text-align:center; margin-top:26px; }}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <h1>Neon Alley</h1>
    <p class="sub">A small original beat-'em-up prototype running on the verified engine slice.</p>
    <div class="badges">
      <span class="badge">1 fighter · 3 enemies · 2 waves</span>
      <span class="badge">60 Hz deterministic, no RNG</span>
      <span class="badge">52 integration tests passing</span>
      <span class="badge">not a remake of anything</span>
    </div>
  </header>

  <div class="panel">
    <h2>Recorded run — highlight loop</h2>
    <img src="data:image/gif;base64,{highlight}" alt="Neon Alley highlight loop">
    <p class="note">Replayed from <code>prototype/data/scripted_run.json</code>: 875 recorded input
    frames reproduce this run exactly — victory at frame 875, 3/3 knockouts, 56/80 health.</p>
  </div>

  <div class="panel">
    <h2>Full encounter — 875 frames</h2>
    <img src="data:image/gif;base64,{full}" alt="Neon Alley full encounter">
    <p class="note">Same simulation with no input at all ends in defeat at frame 1025 — the
    enemies can and will beat you.</p>
  </div>

  <div class="grid">
    <div class="panel">
      <h2>Controls</h2>
      <table>{controls}</table>
      <p class="note">Also printed on the title screen and along the bottom of the HUD.</p>
    </div>
    <div class="panel">
      <h2>Run it locally</h2>
      <ol>
        <li>Download the ZIP below and unpack it.</li>
        <li>From the repository root:
          <pre>python3 -m venv .venv
.venv/bin/pip install pygame
.venv/bin/python -m prototype.neon_alley</pre></li>
        <li>No network needed after the install. All art is generated in code.</li>
      </ol>
      <div class="downloads">
        <a href="index.html">Play it in the browser</a>
        <a class="alt" href="neon_alley-prototype.zip" download>Download the prototype (ZIP)</a>
      </div>
      <p class="note">The browser build is the same game ported to JavaScript and verified
      against the Python reference frame by frame (see
      <code>prototype/tools/web_conformance.py</code>).</p>
    </div>
  </div>

  <div class="panel">
    <h2>Measurements</h2>
    <div class="stats">
      <div class="stat"><b>52</b><span>tests passed</span></div>
      <div class="stat"><b>7,740</b><span>ROM comparisons, unchanged</span></div>
      <div class="stat"><b>875</b><span>frames to victory</span></div>
      <div class="stat"><b>≈400</b><span>FPS sim + draw</span></div>
    </div>
  </div>

  <div class="panel">
    <h2>Screenshots</h2>
    <div class="grid">{gallery}</div>
  </div>

  <div class="panel">
    <h2>What is reused, and what is new</h2>
    <p><b>Reused from the recovered engine</b> (called on the real update / collision /
    render path, not beside it): fixed-point world, gravity and vertical velocity, air control,
    terminal-velocity clamp, frame integration with the <code>$00442C</code> freeze predicate,
    ROM-derived body boxes, the <code>$00450C</code> AABB predicate, world→screen projection and
    the engine's sprite culling.</p>
    <p><b>New in this game:</b> the character, the street, all art, the enemies and their AI,
    the attack frame data, health, waves, hit reactions and the HUD. This is an original game
    built on verified rules — <em>not</em> a remake, port or reconstruction of the original.</p>
    <p class="note">Prototype rules are tagged <code>[PROTO]</code> and are never presented as
    behaviour of the original game. See <code>prototype/RULES.md</code>.</p>
  </div>

  <footer>Neon Alley · built on components/sor_engine · this page is a single self-contained
  file and works offline.</footer>
</div>
</body>
</html>
"""
    out = RELEASE / "neon_alley.html"
    out.write_text(doc, encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)} ({out.stat().st_size / 1024:.0f} KiB)")

    # NOTE: release/index.html is the *playable* page, written by tools/make_web.py.
    return out


def build_zip() -> Path:
    out = RELEASE / "neon_alley-prototype.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        zf.writestr("HOW_TO_RUN.txt", ZIP_NOTE)
        for name in ZIP_INCLUDE:
            path = PROTO / name
            if path.exists():
                zf.write(path, f"prototype/{name}")
        for extra in ("components/__init__.py", "components/README.md"):
            path = ROOT / extra
            if path.exists():
                zf.write(path, extra)
        for d in ZIP_DIRS:
            for path in sorted((ROOT / d).rglob("*")):
                if path.is_dir() or "__pycache__" in path.parts or path.suffix == ".pyc":
                    continue
                zf.write(path, str(path.relative_to(ROOT)))
        zf.write(PROTO / "media" / "neon_alley_highlight.gif",
                 "prototype/media/neon_alley_highlight.gif")
    print(f"wrote {out.relative_to(ROOT)} ({out.stat().st_size / 1024:.0f} KiB)")
    return out


def checksums(paths) -> Path:
    paths = [p for p in paths if p.exists()]
    out = RELEASE / "SHA256SUMS.txt"
    lines = []
    for p in paths:
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        lines.append(f"{digest}  {p.name}")
    out.write_text("\n".join(lines) + "\n")
    print(out.read_text())
    return out


def main() -> int:
    RELEASE.mkdir(parents=True, exist_ok=True)
    page = build_html()
    archive = build_zip()
    checksums([page, archive,
               RELEASE / "index.html", RELEASE / "neon_alley_play.html"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
