# Mission 7 — Extraction Toolchain

## Audit before adding
| Tool | Origin | Re-used? | Decision |
|---|---|---|---|
| `decompile_apk.py` | mission-05 | yes (5 batches, +7 classes) | kept as-is |
| `find_refs.py` | mission-05 | yes | kept |
| `build_baseline.py`, `extract_resources.py`, `build_class_inventory.py`, `extract_parser_grammar.py`, `extract_di_graph.py`, `extract_event_candidates.py`, `extract_class_fields.py` | mission-06 | yes | kept |
| **`parse_arsc.py`** | **mission-07** | new | needed: androguard cannot expose ARSC values |
| **`build_m7_inventory.py`** | **mission-07** | new | needed: cross-mission class/method universe + investigation queue |

Only two new tools were written, both to close a gap that a previous tool could not cover. No rewrite of
functioning tools.

## Requirements met
Deterministic output (sorted iteration, fixed key order), explicit `--in/--out` paths, input hashes recorded in
`00_BASELINE/CURRENT_WORKSPACE_STATUS.md`, no network access, read-only on inputs, error reporting via exit codes
and `{"found": false}` records, unit-level assertions in the semantic suite (`124`).
