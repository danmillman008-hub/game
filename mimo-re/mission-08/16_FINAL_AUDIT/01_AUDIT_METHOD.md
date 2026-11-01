# Phase 16.1 — Audit method (interim)

**This is an interim audit.** Phases 3, 4, 6–11, 13–15 and 17 are not started; a final audit written now would
either be a fiction or would simply repeat the missing phases. It will be regenerated at mission end.

## Seven dimensions, never collapsed into one number

| Dimension | Question it answers | Measured how |
|---|---|---|
| inventory | are the objects known and counted? | register row counts |
| source availability | can the body be read at all? | `.java` presence, DEX co-location, decompiler failures |
| static reconstruction | is the mechanism described? | behaviour statements per method |
| behaviour | is the outcome (inputs → state change → side effects) stated? | `BEHAVIOUR_RECONSTRUCTED` count |
| relationships | are callers/callees known with evidence? | typed edges, per-method |
| tests | is there a source-derived test per expectation? | Phase 13 artefacts |
| runtime execution | was anything observed running? | always `NONE` here |

**No single aggregate percentage is produced.** A domain cannot compensate a missing runtime dimension with a rich
inventory dimension, so averaging them would be misleading by construction.

## Why per-domain numbers are mostly "inherited"

Mission-8 touched 7 of 45 domains. For the other 38 the only honest entry is `inherited` (Mission-7's claim, kept
verbatim) or `not_started`. `02_DOMAIN_DIMENSION_MATRIX.csv` contains exactly that, and the `mission08_note` column
says what was and was not done.
