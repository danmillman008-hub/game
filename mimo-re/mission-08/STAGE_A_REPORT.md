# Mission 8 — Stage A Report (Phase 0: baseline & reconciliation)

**Status:** complete · **Date:** 2026-11-01 · **Base commit:** `b95f56da1a16dd09167ae0ef7ec251dedd6b216e`

## Delivered

| File | Content |
|---|---|
| `00_BASELINE/BASELINE_REPORT.md` | measured environment, artefact inventory, universe counts, stage acceptance |
| `00_BASELINE/HISTORICAL_FINDINGS_RECONCILIATION.md` | R-01…R-10, original claim vs invalidating evidence, both records kept |
| `00_BASELINE/CANONICAL_OPEN_QUESTION_REGISTER.json` | 39 questions, one current status each, 8-value vocabulary, resolved evidence files |
| `00_BASELINE/CANONICAL_DOMAIN_REGISTER.json` | 45 domains, one classification each, `runtime_executed` = NONE everywhere |
| `00_BASELINE/PREVIOUS_EVIDENCE_INDEX.json` | per-file size + `sha256[:16]` for missions 4–7 (derived metadata only) |
| `00_BASELINE/HISTORICAL_COUNT_AUDIT.md` | every Mission-7 number recomputed; defect table |
| `00_BASELINE/EXISTING_TOOL_STATUS.json` | T-01…T-10 with verified/not-rerun status and the decompiler failure profile |
| `00_BASELINE/REGRESSION_TEST_RESULTS.md` | 23 + 44 + 21 + 15 = 103 green, no test weakened |
| `00_BASELINE/WORKSPACE_INTEGRITY.json` | tree sizes, hashes, class-universe and decompiled-gap measurements |
| `tools/dex_inspect.py` | DEX-level inspector (coverage, scans, instruction dumps) |
| `tools/build_canonical_registers.py` | rebuilds all registers and the count audit |
| `evidence/*.json` | the raw dumps the reconciliation cites |

## Measurements that change how later phases must work

1. **1,059 of 2,178 queue classes have no decompiled body** (48.6 %). Any "deep investigation" of those must be
   instruction-level, so the DEX path is not an optional extra — it is the primary source for half the queue.
2. **Q-121 is answered**: no app-owned token store exists; `ku.a.d(Z)` returns Firebase ID tokens with a
   client-side `exp` check and one forced refresh, failure type `AccessTokenUnavailableException`.
3. **The `ri.*` family is a connectivity monitor**, not a credential store — the Mission-7 hypothesis is refuted
   by the class's own superclass (`ConnectivityManager$NetworkCallback`).
4. **Mission-7's `Runtime: complete` column cannot mean execution**; `runtime_executed` is `NONE` for 45/45
   domains.
5. **The Compose Rive composable is missing from the dex set**, while its lambdas survive — a structural gap, to
   be reported as `NOT_RECOVERED` rather than as a decompiler limit.

## Not claimed

No runtime verification, no new endpoint counts, no re-running of the Mission-4…7 pipelines, no edits inside
`mission-04…07`.

## Next stage

Stage B (Phase 1): categorise and prioritise the 2,178-class queue into P0–P3, then produce per-class 23-point
records with the 11-value method-status scale, explicitly recording for each class whether the claim rests on
`decompiled_java` or `dex_instructions`.
