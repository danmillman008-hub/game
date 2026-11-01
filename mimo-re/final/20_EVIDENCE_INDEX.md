# 20 — Evidence index

Every claim in `final/00`…`final/21` is traceable to one of the artefacts below.
IDs are stable and are referenced from the section text where precision matters.

| Evidence ID | Artefact | What it proves | Measured content | SHA-256 (16) |
|---|---|---|---|---|
| `EV-MAN-001` | `evidence/components.json` | manifest component inventory, exports, deep links | 61 activities, 19 services, 8 providers | `7b9627f5964b78bf` |
| `EV-MAN-002` | `evidence/manifest-decoded.xml` | raw decoded AndroidManifest | full AXML | `771fb39178551d77` |
| `EV-RES-001` | `evidence/resources.json` | locale list, resource types, string catalogue | 1721 strings, 117 locales (incl. sentinel) | `b6e2afe4afd2b517` |
| `EV-RES-002` | `evidence/resources-strings.xml` | verbatim app strings (state/behaviour vocabulary) | 1,721 strings | `91967848751a7757` |
| `EV-RES-003` | `evidence/design-tokens.json` | colours, dimensions, fonts, derived scales | 234 app colours, 300 app dimens, 59 inferred pairs | `7b7d6b34cd208407` |
| `EV-UI-001` | `evidence/screens.json` | screen/modal/fragment/sheet inventory | 61 activities, 22 modals, 87 sheets, 809 layouts | `4062ed7bd7fd7411` |
| `EV-DEX-001` | `evidence/dex-inventory.json` | DEX file sizes and class counts | 12 dex files, 29454 classes | `01998b3b0d18630b` |
| `EV-DEX-002` | `evidence/class-strings.json.gz` | per-class string literals (responsibility evidence) | 3028 app classes | `93feed9cee6e25b9` |
| `EV-DEX-003` | `evidence/data-contracts.json` | recovered data-class field lists (API/progress contracts) | 265 contracts | `ab72f1cfeaf148eb` |
| `EV-DEX-004` | `evidence/feature-evidence.json` | feature → class index | 42 features | `21df07e4c2d3fdd5` |
| `EV-DEX-005` | `evidence/literal-index.json` | literal → declaring classes (incl. obfuscated) | 69 literals, 631 pairs | `6b99fbfa86dc5608` |
| `EV-DEX-006` | `evidence/method-literals.json` | method-level literals for parser/lesson classes | 420 classes | `ad6456d14f171daa` |
| `EV-CNT-001` | `evidence/content-deep.json` | corpus conformance: DSL, offsets, integrity | 18272 lessons, 17526 offsets in bounds, 42 issues | `0d812d4d16273260` |
| `EV-CNT-002` | `evidence/tracks.csv` | per-entity inventory | 19 rows | `3abb4759e84c10c2` |
| `EV-CNT-003` | `evidence/tutorials.csv` | per-entity inventory | 1029 rows | `7055342be1560fef` |
| `EV-CNT-004` | `evidence/lessons.csv` | per-entity inventory | 18272 rows | `e42bc01996f5fa6f` |
| `EV-CNT-005` | `evidence/languages.csv` | per-entity inventory | 10 rows | `0a92d0c1f607fb2c` |

## Reproduce everything

```bash
python3 -m venv .venv && .venv/bin/pip install androguard==4.1.4
# 1) split-archive reassembly (see README.md) → Mimo_9.35.apk
.venv/bin/python tools/export_manifest_resources.py APK evidence
.venv/bin/python tools/design_tokens.py APK evidence/design-tokens.json
.venv/bin/python tools/screen_inventory.py ASSETS evidence
.venv/bin/python tools/dex_evidence.py EXTRACTED evidence
.venv/bin/python tools/literal_reverse_index.py EXTRACTED evidence/literal-index.json
.venv/bin/python tools/content_deep.py ASSETS evidence
.venv/bin/python tools/build_evidence_index.py evidence final
.venv/bin/python tools/build_final_report.py final report.html
```

## Evidence classes used in this report

| Class | Meaning | Where it dominates |
|---|---|---|
| **VERIFIED STATIC** | read directly from the APK (manifest, resources, DEX literals, bundled content) with a reproducible command | §01, §04, §05, §06, §13, §14 |
| **VERIFIED RUNTIME** | not used — no instrumented session was performed | — |
| **INFERRED** | reasoned from verified artefacts, labelled `(I)` at the point of use | §02 states, §07 server grading, §08 prompt assembly, §09 thresholds |
| **UNKNOWN** | stated as unknown, collected in §21 | §15 precedence, §21 (12 questions) |
