# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged) · `SERVER CONFIRMED = 0` · classification on every finding.

---

## OPEN QUESTIONS — all explicitly `UNKNOWN`
`SERVER CONFIRMED = 0`. No item below is guessed or filled with a plausible value.

| # | Question | Exact pointer | Why unresolved / what would resolve it |
|---|---|---|---|
| Q-1 | Correct-answer **runtime** UI state | `base/c.V()`, M05 runs 001–005 | M05 never produced a correct answer; no new M06 run. Needs deterministic replay of `42003884423`'s exact 24 taps plus an answer that satisfies `Lqm/i.a` |
| Q-2 | Persisted `lesson_progress` row **after** an answer | Room `lesson_progress`, `LessonProgressDao` (`Lcg/a;`) | Requires root / private DB extraction — forbidden. Static write path is verified |
| Q-3 | Server response bodies for progress / runFiles / ETA / keys | `LessonProgressApi`, `HTTP_VERBS_RESOLVED.json` (53 endpoints) | Deliberately out of scope (no backend reconstruction) |
| Q-4 | Absolute XP / keys / coins / streak / daily-goal award formulas and thresholds | `Progress`, `PostProgressResponse`, `TrackEtaResponse`, `ChapterFinishedSuccessType` | Depend on server bodies; client only consumes |
| Q-5 | **Full unlock rule** (Locked / UnlockedButNoKeys / Unlocked) | `GetPathMapState$invoke$3.invokeSuspend`, `classes.dex` @10129608, 659 insns | Junk `const/4` decoys + 3 suspension labels; full body saved but boolean combination not decoded |
| Q-6 | `CanOpenChapterWithKeys` true-branch result | `CanOpenChapterWithKeys$invoke$1` @10104004 | 102-insn coroutine with unreachable-looking branch; needs full decode |
| Q-7 | `W()` partial-match feedback difference vs `V()` | `base/c.W(qm/f, cont)` @10953916, 202 insns | Body saved, not fully interpreted |
| Q-8 | `d0()` hard-mode / AI-Tutor / attempts boolean combination | `base/c.d0(cont)` @10956096, 148 insns | Body saved, not fully interpreted |
| Q-9 | `SingleChoice` vs `MultipleChoice` vs `Reveal` exact dispatch | `Lgm/h.a(List)` @12460480, 437 insns | Only type constants and marker strings verified |
| Q-10 | `Lte/a.a` full interaction/option construction | `Lte/a.a(XmlPullParser)` 490 insns | Inputs/outputs verified; internal offsets not decoded |
| Q-11 | `Interaction$ValidatedInput.e:String`, `f:String[]` semantics | `Interaction$ValidatedInput` | Fields known, usage not decoded |
| Q-12 | `Lye/b.a(Tutorial)` filter and `Lye/d` loader selection / update trigger | `Lye/b`, `Lye/d` | Which loader wins at runtime is a DI binding not decoded |
| Q-13 | `DefaultTracksRepository.i` full 409-insn state machine | `tracks/c.i(J,cont)` @9750496 | Body saved, caching/completion merge partially decoded |
| Q-14 | `Lhg/e.intercept` (network interceptor) | `Lhg/e;->intercept` | Not decoded; no request/response reconstruction attempted |
| Q-15 | `DefaultTrackLoader$getExecutableLesson$2` full coroutine | inner class | Body saved, not fully interpreted |
| Q-16 | Exact `q.I()` applicability to all executable lessons | `q.I()` @10912932, callers=1 | One MVI reducer caller not fully decoded |
| Q-17 | Remote code-execution service behaviour | `/v1/code/runfiles`, `/v1/tutorials/{id}/runFiles` | Server-owned boundary, `SERVER CONFIRMED = 0` |
| Q-18 | Full offline blocking for **every** operation (IAP, leaderboards, profile, AiTutor, publishing, account deletion) | per-feature Retrofit clients | Only progress-post, chapter-end, keys and content rendering gates decoded |
| Q-19 | `NoConnectionException` UI propagation / reconnect | `postUnsyncedLessonProgress` catch sites | Not decoded; M05 `svc wifi/data enable` did not restore connectivity |
| Q-20 | Native `.so` ↔ Kotlin API surface and `System.loadLibrary` call sites | `libsigner.so`, `libdatastore_shared_counter.so`, etc. | Method-string scan finds only Rive; no native disassembly performed (forbidden boundary) |
| Q-21 | Exact DI framework / scopes / singleton graph | `<init>` signatures in `METHOD_CATALOG_MIMO.json` | No Hilt/Koin metadata decoded |
| Q-22 | Navigation graph routes / fragment transactions | `ChapterActivity`, `MainActivity`, `PathMapFragment` | Only component names and LiveData events decoded |
| Q-23 | Force-stop / process-recreation restoration | `LessonProgressQueue`, DataStore | No runtime test, no private DB read |
| Q-24 | Room migration class list / SQL | Room identity hashes only | Not decoded in M06 |
| Q-25 | External URL offline substitution (4,257 refs, M05) | shipped lesson HTML | Content strings; no offline substitution rule decoded |

## What is NOT an open question anymore (closed in M06)
`isSolvedCorrectly` field, `createLessonProgress` 11-column mapping, all interaction
validators, `validatedInput` normaliser, executable `solvedContent` comparison, DSL parser
technology, nine interaction types, asset locale paths, offline `NetworkUtils` gate,
offline chapter-end fallback, `AnswersInChapter` counting formula, smob anti-decompilation.
