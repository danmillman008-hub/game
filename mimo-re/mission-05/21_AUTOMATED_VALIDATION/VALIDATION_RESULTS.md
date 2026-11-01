# Mission 5 — Automated Validation Results

## Scope
What was executed, what passed, and what the suite deliberately does *not* claim. Two suites exist:
the frozen mission-04 suite (regression gate) and the new mission-05 artifact suite.

## Method
`pytest -q` on both suites, after every write phase. The mission-05 suite validates **the evidence
artifacts**, not the app: it fails if a report loses a required section, if the API catalogue becomes
internally inconsistent with Retrofit's rules, if the corrected annotation pass regresses to garbage,
if the dependency graph references a non-existent node, or if proprietary material appears in the repo.

## Sources
- `mimo-re/complete-extraction/16_AUTOMATED_TESTS/` (mission-04, frozen)
- `mimo-re/mission-05/21_AUTOMATED_VALIDATION/test_mission05_artifacts.py` (new)

## Findings
| Suite | Tests | Result |
|---|---|---|
| mission-04 (`test_lesson_dsl.py` + conftest) | 23 | **23 passed** — no regression |
| mission-05 artifact suite | 44 cases (29 test functions; the document-hygiene test is parametrised over 21 reports) | **44 passed** |

Mission-05 tests, grouped:
| Group | Tests | What it guards |
|---|---|---|
| API catalogue | 5 | 62 endpoints; five-verb set; **zero** Retrofit body-rule violations; absolute paths; every `{placeholder}` bound |
| Annotations | 2 | 105 parameter rows, all keys printable (mission-04 emitted 162 garbage rows); exhaustive scopes |
| DSL | 2 | 29 tag constants with ordinals 0–28; the AST JSON Schema parses and has Module/Option definitions |
| DTO / graph / progress | 3 | 50 DTO rows typed; graph edges reference existing nodes and carry legal labels; `tries` is documented as a 0/1 flag |
| Document hygiene | 21 (parametrised) | every report has Scope/Method/Sources/Evidence labels/Limitations/Unresolved/Reproduction |
| Hygiene | 2 | no `.apk/.dex/.so/.java` committed by this mission; the pre-existing root APK is *reported*, not deleted |

## Evidence labels
Test outcomes: **VERIFIED_STATIC** (executed in this environment; the exact run is reproducible with
the command below).

## Limitations
- These tests validate *artifacts about the app*. They say nothing about app behaviour: **no runtime
  test exists for Mimo itself** (no device/emulator). A passing suite must never be read as runtime
  verification.
- The hygiene test is path-scoped by suffix; a decompiled `.txt` dump would slip through by design
  (inventories are text).

## Unresolved
No automated check exists for the *semantic* correctness of decompiled readings (e.g. the normaliser
rule). Those are backed by quoted code fragments in the reports, not by executable assertions.

## Reproduction
```bash
cd mimo-re/complete-extraction/16_AUTOMATED_TESTS && python -m pytest -q     # 23 passed
cd mimo-re/mission-05 && python -m pytest 21_AUTOMATED_VALIDATION -q          # 44 passed
```
