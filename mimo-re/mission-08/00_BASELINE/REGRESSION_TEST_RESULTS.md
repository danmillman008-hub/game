# Mission 8 — Regression Test Results (Stage A)

**Date:** 2026-11-01  
**Interpreter:** `/tmp/venv/bin/python` (pytest 9.2.0)  
**Rule:** no test was modified, skipped, deselected or weakened for this run. Mission-08 owns none of these
suites; they belong to missions 4–7 and are executed exactly as they exist in the tree.

| # | Suite | Command | Result |
|---|---|---|---|
| 1 | Mission 4 / complete-extraction | `python -m pytest complete-extraction/16_AUTOMATED_TESTS -q` | **23 passed** |
| 2 | Mission 5 | `python -m pytest mission-05/21_AUTOMATED_VALIDATION -q` | **44 passed** |
| 3 | Mission 6 | `python -m pytest mission-06/19_TESTS -q` | **21 passed** |
| 4 | Mission 7 | `python -m pytest mission-07/20_TESTS -q` | **15 passed** |

Totals: **103 assertions suites-wide, 0 failures, 0 errors, 0 skips.**

## Path correction (documentation, not a test change)

Mission-7 notes and the session log referred to the mission-7 suite as `19_TESTS`. The suite actually lives in
**`mission-07/20_TESTS/test_mission07_semantics.py`**; `19_TOOLS` is the tooling directory. Recorded here so the
next run does not quote a non-existent path.

## What these suites do and do not prove

* They prove the mission-4…7 artefacts are internally consistent and still parse (registers closed, IDs unique,
  counts matching their own CSVs).
* They do **not** prove behaviour of the Mimo application: they are artefact-consistency tests. Mission-8
  Phase 13 must add source-derived tests whose expectations can be traced to a specific method and instruction.

## Mission-8 additions in this stage

No new test is claimed yet. The stage-A deliverables are register-building tools; the semantic tests
(`13_SEMANTIC_VALIDATION/`) arrive in their own phase and must record, for each expectation, the exact source
method (and DEX instruction where the body is DEX-only) that justifies it.

## Reproduction

```bash
cd mimo-re
for d in complete-extraction/16_AUTOMATED_TESTS mission-05/21_AUTOMATED_VALIDATION \
         mission-06/19_TESTS mission-07/20_TESTS; do
  /tmp/venv/bin/python -m pytest "$d" -q | tail -1
done
```
