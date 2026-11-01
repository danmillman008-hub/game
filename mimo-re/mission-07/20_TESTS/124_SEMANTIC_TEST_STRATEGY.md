# Mission 7 — Semantic Test Strategy

## Principle
Tests validate the **model**, not the file tree. Each test names the claim it protects and fails when an artefact
drifts from its evidence. Circular validation is avoided by deriving expectations from source-level artefacts
(extracted JSON, DEX inventories) rather than from the documents the tests accompany.

| Test group | Protects | Derived from |
|---|---|---|
| ARSC/design tokens | token values really decoded, not asserted | `evidence/DESIGN_TOKENS_VALUES.json` |
| DI catalogue | 127 cases, provider counts | mission-06 `DI_GRAPH.json` |
| class/method universe | 29,454 classes, kind totals, 15,087 methods | DEX scan |
| analytics | ≥14 events each with a call site | `EVENTS_WITH_CALLSITES.csv` |
| closure register | statuses ∈ 8-value enum, covers the inherited register | mission-06 register |
| AST schema | `$ref` resolution, offset typing (`STYLE_SPAN` vs gap) | schema itself + code semantics |
| DSL closures | `NUMBER` dead, no `multiple` | corpus scan results |
| diagrams | exactly 20 Mermaid sources | files |
| grading | vectors reproduce the normaliser and verdict mapping | `qm.i` semantics |
| runtime discipline | no document claims `VERIFIED_RUNTIME` | all `.md` |
| evidence integrity | referenced evidence paths exist | filesystem |
| corrections | keys consumption recorded as a correction | doc text |

## Non-circularity note
Where an expectation could only come from the same document it validates (e.g. Rive asset count), the test compares
against an **independent measurement** (zip listing), so a fabricated number fails.
