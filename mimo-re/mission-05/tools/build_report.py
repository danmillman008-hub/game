#!/usr/bin/env python3
"""MISSION-05 — build a self-contained HTML index over the mission's documents and evidence.

Deterministic: file lists are sorted, no timestamps are embedded.
"""
from __future__ import annotations
import csv, html, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKIP_DIRS = {"tools", "__pycache__", ".pytest_cache"}

FINDINGS = [
    ("The lesson parser is obfuscated <code>te.a</code>–<code>te.g</code>, outside <code>com.getmimo</code>",
     "04_CONTENT_AND_DSL/DSL_GRAMMAR.md"),
    ("The DSL is HTML-shaped with 29 tags (Tag ordinals 0–28)", "04_CONTENT_AND_DSL/AST_AND_MODELS.md"),
    ("Validated-input grading normalises (lowercase; keep letters/digits/&lt;/. ) and has a partial-match outcome after a 300 ms delay",
     "06_ASSESSMENT_AND_EVALUATION/ASSESSMENT_SPEC.md"),
    ("<code>tries</code> is a 0/1 correctness flag, not a counter — <code>isSolvedCorrectly() { tries &gt;= 1 }</code>",
     "09_PROGRESS_AND_GAMIFICATION/PROGRESS_MODEL.md"),
    ("The local database is a transmit buffer (3 tables, no migrations, delete after ack)",
     "11_LOCAL_DATA_AND_SYNC/DB_SCHEMA_AND_DATAFLOW.md"),
    ("62 endpoints · 85 parameter bindings · 34 response DTOs recovered", "10_NETWORK_AND_API/API_CATALOG.md"),
    ("Native payload identified; <code>libyrf.so</code> drives an obfuscated <code>bin.ghost</code> blocking dialog",
     "16_NATIVE_AND_EXECUTION/NATIVE_REPORT.md"),
]


def count_csv(name: str) -> int | None:
    p = ROOT / "evidence" / name
    if not p.exists():
        return None
    with open(p, newline="", encoding="utf-8") as fh:
        return sum(1 for _ in csv.DictReader(fh))


def main() -> int:
    groups: dict[str, list[pathlib.Path]] = {}
    for p in sorted(ROOT.rglob("*")):
        if p.is_dir() or p.suffix not in {".md", ".html", ".csv", ".json", ".py"}:
            continue
        rel = p.relative_to(ROOT)
        if rel.parts[0] in SKIP_DIRS or p.name == "report.html":
            continue
        groups.setdefault(rel.parts[0] if len(rel.parts) > 1 else "(root)", []).append(p)

    api = count_csv("API_CATALOG_V2.csv") or 0
    ann = count_csv("ANNOTATIONS_V2.csv") or 0
    dto = count_csv("DTO_CATALOG.csv") or 0
    cls = count_csv("CLASS_INVENTORY_APP.csv") or 0
    unres = count_csv("UNRESOLVED_REGISTER.csv") or 0
    graph = json.load(open(ROOT / "18_SYSTEM_GRAPH" / "system_graph.json", encoding="utf-8"))

    out = ["""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Mimo — Mission 5 reverse engineering</title>
<style>
 :root{--fg:#111;--muted:#555;--line:#ddd;--accent:#0b6}
 body{font:15px/1.55 -apple-system,Segoe UI,Roboto,sans-serif;color:var(--fg);margin:0;padding:2rem;max-width:1100px}
 h1{font-size:1.6rem;margin:0 0 .3rem} h2{margin-top:2rem;border-bottom:1px solid var(--line);padding-bottom:.3rem}
 .meta{color:var(--muted);font-size:.9rem} .cards{display:flex;flex-wrap:wrap;gap:.75rem;margin:1rem 0}
 .card{border:1px solid var(--line);border-radius:8px;padding:.6rem .9rem;min-width:150px}
 .card b{display:block;font-size:1.35rem} code{background:#f6f6f6;padding:.05rem .3rem;border-radius:4px}
 table{border-collapse:collapse;width:100%} td,th{border-bottom:1px solid var(--line);padding:.35rem .4rem;text-align:left;vertical-align:top}
 a{color:#0a58ca;text-decoration:none} a:hover{text-decoration:underline}
 .lbl{font-size:.75rem;border:1px solid var(--line);border-radius:10px;padding:.05rem .45rem;color:var(--muted)}
</style></head><body>"""]
    out.append("<h1>Mimo — Mission 5 reverse engineering</h1>")
    out.append('<p class="meta"><code>com.getmimo</code> 9.35 · versionCode 1792759685 · '
               'specification only · <b>no runtime evidence</b> (no device/emulator/adb) · '
               'branch <code>arena/ecb8af07-game</code></p>')
    out.append('<div class="cards">')
    for label, value in [("endpoints", api), ("annotation rows", ann), ("DTO types", dto),
                         ("app classes", cls), ("graph nodes", len(graph["nodes"])),
                         ("open items", unres)]:
        out.append(f'<div class="card"><b>{value:,}</b>{html.escape(label)}</div>')
    out.append("</div>")

    out.append("<h2>Headline findings</h2><table><tr><th>Finding</th><th>Report</th></tr>")
    for text, link in FINDINGS:
        out.append(f'<tr><td>{text}</td><td><a href="{link}">{html.escape(link)}</a></td></tr>')
    out.append("</table>")

    out.append('<h2>Start here</h2><p>'
               '<a href="MISSION_05_REPORT.md">MISSION_05_REPORT.md</a> · '
               '<a href="22_FINAL_AUDIT/FINAL_AUDIT.md">FINAL_AUDIT.md</a> · '
               '<a href="19_INDEPENDENT_SPECIFICATIONS/README.md">E1/E2/E5 specs</a> · '
               '<a href="MISSION_05_REPORT_FA.md">گزارش فارسی</a></p>')
    out.append('<p class="meta">Evidence labels: VERIFIED_STATIC · VERIFIED_RUNTIME · VERIFIED_EXPERIMENTAL · '
               'INFERRED_HIGH · INFERRED_MEDIUM · INFERRED_LOW · UNKNOWN · BLOCKED · NOT_APPLICABLE</p>')

    for group in sorted(groups):
        out.append(f"<h2>{html.escape(group)}</h2><table><tr><th>File</th><th>Type</th></tr>")
        for p in groups[group]:
            rel = p.relative_to(ROOT).as_posix()
            out.append(f'<tr><td><a href="{rel}">{html.escape(p.name)}</a></td>'
                       f'<td class="lbl">{p.suffix.lstrip(".")}</td></tr>')
        out.append("</table>")
    out.append('<p class="meta">Generated by <code>tools/build_report.py</code> — deterministic, no timestamps.</p>')
    out.append("</body></html>")
    (ROOT / "report.html").write_text("\n".join(out), encoding="utf-8")
    print(f"report.html written — {sum(len(v) for v in groups.values())} files indexed, "
          f"{len(groups)} groups")
    return 0


if __name__ == "__main__":
    sys.exit(main())
