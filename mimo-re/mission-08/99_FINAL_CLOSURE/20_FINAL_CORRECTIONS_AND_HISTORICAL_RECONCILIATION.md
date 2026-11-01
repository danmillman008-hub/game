# 20 — Final corrections and historical reconciliation

Previous missions are preserved unchanged. Every correction below supersedes an earlier statement **without deleting
it**; the original text stays in its mission and this register is the authoritative reading.

## 1. Corrections carried into this mission

| ID | Correction | Supersedes |
|---|---|---|
| R-05 | `ri.*` family mapped (annotation / state / provider / callback) | mission-06 guess |
| R-11 | headers are not built "inside request builders"; a central interceptor exists | phase-2 data-flow note |
| C-14 | `solutionFeedbackCorrect/Wrong` are **property names**, not analytics events | mission-06 event candidate list |
| C-15 | `base.c.e0` = `storeLessonProgressInMemory`; `K` = `initialiseCodeBlocks` | Stage-1 mapping (A18 closed) |
| C-16 | progress key is `(lesson_id, tutorial_id)`, not `(trackId, lessonId)` | Stages 3–4 wording |
| C-17 | API host switch is a **dev-menu preference** (`sk.a.r[2]`), not a build flag | mission-06 Q-76 wording |
| C-18 | `fh.a` is annotation-conditional; token from `ku.a.d(Z)`; `ri.b` is an annotation, not a token holder | mission-06/07 `ri.b.d(0)` + "every request carries the header" |
| C-19 | offline gate throws `java.io.IOException` | phase-5 "NoConnectionException" at that site |
| C-20 | `d70.b` = `kotlin.coroutines.Continuation`; **no** `Result` envelope exists | mission-06 `51_ERROR_MODEL.md`, mission-07 `58` |

## 2. Corrections issued in this final mission

| ID | Statement now corrected | Reason |
|---|---|---|
| C-21 | "the app is offline-capable" | wrong without qualification: content/lesson/grading are offline, **progression is not** (`08`) |
| C-22 | "learner statistics are stored" | `tries` is a flag and `attempts` is session-local; no lifetime statistic exists (`07`) |
| C-23 | "misconfigured `DP`" (mission-07 metric table) | `mission-08/16_FINAL_AUDIT/02_DOMAIN_DIMENSION_MATRIX.csv` D-43 previously read `NOT_INVESTIGATED` while the auth phase had already reconstructed the lifecycle; the matrix now reflects `RECONSTRUCTED` |
| C-24 | mission-06 "9 unauthenticated endpoints" as a verified fact | it is an aggregate from a scan whose per-row column is absent from committed evidence; downgraded to `INFERRED_HIGH` pending `A-01` |

## 3. Count reconciliation (previous vs actual)

| Quantity | Earlier reports | Actual / current |
|---|---|---|
| Classes | 29,454 | 29,454 (unchanged) |
| Call edges | 85,724 | 85,724 (mission-08 recalculated from Stage-2 graph) |
| Call sites | 138,025 | 138,025 |
| Endpoints | 62 | 62 (29 interfaces) |
| Deep classes | 330 (m7) / 180 bodies | unchanged; +Stage 3–7 additions |
| Questions | 39 canonical | **91** total families closed here |
| Semantic tests | 103 inherited | **170** cumulative (103 + 68 from Stages 4–7 + 22 final closure) |
| Runtime-verified | 0 | **0** |

## 4. What was rejected during reconciliation

* mission-07's "every request carries the header" — refuted by the interceptor body (C-18);
* mission-06/07's `Result` envelope — refuted by mission-06's own obfuscation map (C-20);
* the reading of `ri.b` as a token holder — refuted by elimination across `ri.a`–`ri.d` (C-18);
* "the app works offline" in the general sense — refuted by the completion/coins/tutor boundary (C-21);
* "attempts is a lifetime counter" — refuted by the absence of any read-back into the view-model (C-22).

## 5. Historical documents that must keep their original text

`mission-04/`, `mission-05/`, `mission-06/`, `mission-07/` and mission-08 `STAGE_*_REPORT.md`. None of them was edited
in this mission; the only registers touched are the mission‑8 status/coverage/question files, which are append-only in
practice (new rows, no deletions).
