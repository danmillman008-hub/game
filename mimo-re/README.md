# mimo-re — Mimo 9.35 (`com.getmimo`) evidence-graded blueprint

Static, offline reverse engineering of the Mimo Android app 9.35
(versionCode 1792759685, APK 142,353,499 B, `sha256 48ce1740…0f7c7a`).
No server was contacted, no account used, no protection circumvented.

## What is where

| Path | Contents |
|---|---|
| `final/00`…`final/21` | **the deliverable**: 22 documents (inventory → screens → design → curriculum → DSL → grading → tutor → difficulty → economy → content ops → dev menu → persistence → API → config → offline → security → architecture → Konkur transfer → evidence → unknowns) |
| `final/report.html` / `report-v2.html` | single-file HTML build of all 22 sections + inlined diagram sources |
| `MIMO-REPORT.md`, `report.html` | earlier Persian report (kept unchanged, §0–§13) |
| `SENARIO_MIMO.md` | Persian operational/management scenario (backend + admin panel + runbooks + 90-day plan) |
| `ARCHITECTURE_MIMO.md` | Persian code + pedagogical architecture |
| `diagrams/` | 16 diagrams as editable Mermaid (`*.mmd`) + Graphviz (`*.dot`) |
| `schemas/` | JSON Schema for `tracks.json` / tutorial / progress payload, EBNF for the lesson DSL, OpenAPI skeleton |
| `samples/` | provenance material (real, do not redistribute) + placeholder templates that are safe to reuse |
| `evidence/` | machine-generated artefacts; every claim traces here (`final/20`) |
| `data/` | global string pool, class lists, endpoints, Room schema, content stats |
| `tools/` | 9 deterministic CLI tools (below) |

## Reproduce

```bash
python3 -m venv .venv && .venv/bin/pip install androguard==4.1.4
python3 -m venv /tmp/venv 2>/dev/null; # or reuse an existing venv with androguard

# 1) re-assemble the split archive from Google Drive (z01 + z02 + zip)
cat 'Mimo_9.35 (1).z01' 'Mimo_9.35 (1).z02' 'Mimo_9.35 (1).zip' > /tmp/mimo_full.zip
unzip -o /tmp/mimo_full.zip -d /tmp/apk            # → /tmp/apk/Mimo_9.35 (1).apk
sha256sum '/tmp/apk/Mimo_9.35 (1).apk'             # 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
unzip -o '/tmp/apk/Mimo_9.35 (1).apk' 'assets/*' 'classes*.dex' -d /tmp/x

# 2) evidence
.venv/bin/python tools/export_manifest_resources.py '/tmp/apk/Mimo_9.35 (1).apk' evidence
.venv/bin/python tools/design_tokens.py '/tmp/apk/Mimo_9.35 (1).apk' evidence/design-tokens.json
.venv/bin/python tools/screen_inventory.py /tmp/x/assets evidence
.venv/bin/python tools/dex_evidence.py /tmp/x evidence
.venv/bin/python tools/literal_reverse_index.py /tmp/x evidence/literal-index.json
.venv/bin/python tools/content_deep.py /tmp/x/assets evidence

# 3) publish
.venv/bin/python tools/build_evidence_index.py evidence final
.venv/bin/python tools/build_final_report.py final final/report.html
```

`python tools/<tool>.py --help` is not wired for every script (they take positional args and
validate their own inputs); `tools/README.md` documents each signature. All tools are
deterministic, read-only with respect to the APK, and print no secrets.

## Headline measured facts

* 61 activities / 19 services / 8 providers / 8 exported components; 22 fragments, 22 modals,
  87 bottom sheets, 44 dialogs, 809 layouts.
* Content: 19 tracks, 1,029 tutorials, 1,947 chapters, 18,272 lessons across 10 language packs at
  `publishSetVersion 753`; 13,027 assessed steps; 4,024 executable lessons with 6,746 files.
* Lesson DSL: 26 tags, 3 `visible-if` values, 0 unknown tags/attributes, **17,526/17,526 gap
  offsets in bounds** under “flatten `<text>`, break → `\n`”.
* 234 app colours / 300 app dimens / 59 light-dark pairs; fonts: Aeonik Pro, Aeonik Fono,
  Aeonik Mono, optimistic_vf.
* 71 endpoint literals (all in annotation space, none referenced by `const-string`), 265
  recovered data contracts, 305 analytics event classes, 3 Room tables.
* 55 developer-menu classes shipped in production.

## Limitations (read `final/21` before quoting anything)

No JADX/JDK 17 in this environment ⇒ no bytecode decompilation; 26,321 of 29,454 classes are
obfuscated. No runtime session ⇒ all server behaviour is inferred and labelled. Annotation
parsing for HTTP verbs was abandoned (parser in `tools/retrofit_endpoints.py`, currently
incomplete and documented as such).
