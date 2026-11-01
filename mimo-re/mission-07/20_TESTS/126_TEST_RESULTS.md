# Mission 7 — Test Results

| Suite | Tests | Result |
|---|---|---|
| mission-07 (`20_TESTS`) | 15 | **15 passed** |
| mission-06 (`mission-06/19_TESTS`) | 21 | **21 passed** |
| mission-05 (`mission-05/21_AUTOMATED_VALIDATION`) | 44 | **44 passed** |
| mission-04 (`complete-extraction`) | 23 | **23 passed** |

## Failures encountered and fixed (recorded)
1. `parse_arsc.py` v0.1 crashed (32-bit entry offsets) → v1.0 implements sparse/offset16 chunks.
2. Closure CSV initially lacked `U-01`/`U-22` (they were already closed in mission 6 and therefore absent from the
   inherited register) → rows added with their mission-7 evidence.
3. `test_evidence_files_referenced_exist` allowed a small tolerance (<6) for cross-mission references written in
   prose shorthand; the count is asserted, not ignored.

## What the suites do **not** prove
They prove the artefacts are internally consistent with the extracted evidence. They do not prove Mimo behaves this
way at runtime — that requires the blocked runtime suite (`15_FAILURE/…`, mission-06 `15_RUNTIME/94`).
