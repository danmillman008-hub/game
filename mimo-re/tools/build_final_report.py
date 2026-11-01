#!/usr/bin/env python3
"""Stage 12 — build the single-file HTML report for final/.

Concatenates final/NN_*.md in numeric order, renders Markdown (tables, fenced code),
adds a sticky table of contents, and inlines Mermaid diagram sources as collapsible
<details> blocks (no JS dependency, no CDN: diagrams stay editable in diagrams/*.mmd).

Usage:
    python tools/build_final_report.py FINAL_DIR OUT_HTML [--title T]
"""
from __future__ import annotations

import argparse
import glob
import html
import os
import re

CSS = """
:root{--bg:#0f1222;--fg:#e8eaf6;--muted:#a0a4c0;--acc:#885bde;--card:#181c31;--line:#2a2f4a}
*{box-sizing:border-box}
body{margin:0;font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;
     background:var(--bg);color:var(--fg)}
#wrap{display:flex;max-width:1500px;margin:0 auto}
nav{position:sticky;top:0;align-self:flex-start;width:280px;height:100vh;overflow:auto;
    padding:24px 16px;border-right:1px solid var(--line);font-size:14px}
nav a{display:block;color:var(--muted);text-decoration:none;padding:5px 8px;border-radius:6px}
nav a:hover{background:var(--card);color:#fff}
nav .grp{margin:14px 0 4px;color:var(--acc);font-weight:700;font-size:12px;letter-spacing:.08em;text-transform:uppercase}
main{flex:1;min-width:0;padding:32px 48px 120px}
h1{font-size:32px;margin:48px 0 16px;padding-bottom:8px;border-bottom:2px solid var(--acc)}
h2{font-size:23px;margin:32px 0 12px;color:#fff}
h3{font-size:18px;margin:24px 0 8px;color:#cfd3ee}
p,li{color:#dfe2f2}
table{border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;display:block;overflow-x:auto}
th,td{border:1px solid var(--line);padding:7px 10px;text-align:left;vertical-align:top}
th{background:var(--card);color:#fff;position:sticky;top:0}
tr:nth-child(even) td{background:#141830}
code{background:#12162a;padding:1px 5px;border-radius:4px;font-size:13px;color:#c9b8ff}
pre{background:#0b0e1c;border:1px solid var(--line);border-radius:10px;padding:14px;overflow:auto;font-size:13px}
pre code{background:none;color:#cdd3f0}
blockquote{border-left:3px solid var(--acc);margin:16px 0;padding:6px 16px;color:var(--muted)}
details{margin:12px 0;border:1px solid var(--line);border-radius:8px;padding:8px 12px;background:#12162a}
summary{cursor:pointer;color:var(--acc);font-size:13px}
.tag{display:inline-block;font-size:11px;padding:1px 6px;border-radius:999px;border:1px solid var(--line);color:var(--muted)}
.meta{color:var(--muted);font-size:14px}
"""


def md_to_html(md: str) -> str:
    try:
        import markdown
    except ImportError:  # pragma: no cover
        return "<pre>" + html.escape(md) + "</pre>"
    return markdown.markdown(md, extensions=["tables", "fenced_code", "sane_lists", "attr_list"])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("final_dir")
    ap.add_argument("out_html")
    ap.add_argument("--title", default="Mimo 9.35 — Reverse-engineering blueprint")
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(args.final_dir, "[0-9][0-9]_*.md")))
    if not files:
        raise SystemExit("no final/*.md files")
    parts, toc = [], []
    for f in files:
        base = os.path.basename(f)
        md = open(f, encoding="utf-8").read()
        body = md_to_html(md)
        anchor = base[:2]
        body = re.sub(r"<h1>(.*?)</h1>", lambda m: f'<h1 id="s{anchor}">{m.group(1)}</h1>', body, count=1)
        body = re.sub(r"<h2>(.*?)</h2>", lambda m: f'<h2 id="s{anchor}-{re.sub(r"[^a-z0-9]+","-",m.group(1).lower())[:40]}">{m.group(1)}</h2>', body)
        parts.append(body)
        title = re.search(r"<h1[^>]*>(.*?)</h1>", body)
        toc.append(f'<a href="#s{anchor}">{html.escape(re.sub("<[^>]+>", "", title.group(1)) if title else base)}</a>')

    diagrams = sorted(glob.glob(os.path.join(os.path.dirname(args.final_dir.rstrip("/")), "diagrams", "*.mmd")))
    dparts = []
    for d in diagrams:
        name = os.path.basename(d)
        src = open(d, encoding="utf-8").read()
        dparts.append(f'<details><summary>diagrams/{html.escape(name)} (Mermaid source)</summary>'
                      f'<pre><code>{html.escape(src)}</code></pre></details>')

    html_out = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(args.title)}</title><style>{CSS}</style></head><body><div id="wrap">
<nav><div class="grp">Sections</div>{''.join(toc)}
<div class="grp">Diagrams</div><a href="#diagrams">{len(diagrams)} Mermaid sources</a></nav>
<main><div class="meta">Generated from <code>final/*.md</code> by <code>tools/build_final_report.py</code> ·
evidence classes: VERIFIED STATIC / INFERRED / UNKNOWN · no runtime data</div>
{''.join(parts)}
<h1 id="diagrams">Diagrams (editable sources)</h1>
<p>Full Mermaid/Graphviz files live in <code>diagrams/</code>. Sources are inlined below for offline reading.</p>
{''.join(dparts)}
</main></div></body></html>"""
    open(args.out_html, "w", encoding="utf-8").write(html_out)
    print(f"wrote {args.out_html} ({len(html_out):,} bytes, {len(files)} sections, {len(diagrams)} diagrams)")


if __name__ == "__main__":
    main()
