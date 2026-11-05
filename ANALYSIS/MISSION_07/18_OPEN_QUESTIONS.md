# MISSION 07 — 18 OPEN QUESTIONS AND RESIDUAL UNKNOWNS

`UNKNOWN` means not measured; it does not mean impossible or unavailable.
`SERVER CONFIRMED = 0`.

## Resolved by M07 runtime evidence
| M06 Q | Question | Resolution |
|---|---|---|
| Q-2 | persisted `lesson_progress` row after answer | **RESOLVED**: stage 5 row `151403` with all 11 values |
| Q-1 | correct-answer runtime UI | **RESOLVED** for WebView lesson 151403: `Correct!`, `D O G`, `dog_yawn` |
| Q-7 | `W()` partial-match feedback | **PARTIAL**: bytecode fully decoded (`jm/n`, analytics name), live dispatch `UNKNOWN` |
| Q-16 | `q.I()` equality with `solvedContent` | **PARTIAL**: `km.f.b` all-match predicate verified; `q.I` not exercised |
| Q-19 | offline exception UI | **PARTIAL**: `NoConnectionException` thrown in repository; the user-visible UI of that exception was not captured |
| Q-23 | force-stop restore | **RESOLVED (negative)**: `in_queue=1` rows are deleted at offline cold start |
| Q-12 | loader / interaction selection | **MOSTLY RESOLVED**: `gm.h.a(emptyList)=None(slide)` AND `gm.h.a(shippedFillTheGapModules)=FillTheGap(interactionTypeName=fill_the_gap)` verified; other types `UNKNOWN` |
| Q-9 | SingleChoice / MultipleChoice / Reveal dispatch | **PARTIAL**: `Selection`/`SelectionItem` DSL objects verified; dispatch `UNKNOWN` |

## Still `UNKNOWN`
1. Live `onLessonRun$1 → Y(true)/Y(false) → V()/W()/X()` dispatch for a native
   validatedInput / selection / fillTheGap / spell / executable answer. Stage 6
   proved the WebView letter exercise bypasses these (`U()/H()` instead) but
   did not submit a native fill-the-gap or selection answer.
2. Live `jm/m` (correct), `jm/n` (partial), `jm/o` (wrong) LiveData values and the
   seven booleans of `jm/o`.
3. `solutionFeedbackCorrect` / `solutionFeedbackWrong` / `solutionFeedbackTryAgain`
   conditions and the exact feedback UI for a submitted selection answer.
4. Absolute XP / points / streak / daily-goal / leaderboard formulas and whether
   any are computed locally at all.
5. `LessonProgressQueue.updateCorrectAnswersCount` semantics and its consumers.
6. `ds/w.c` unlock key operands: where the three longs come from, and whether
   the `Set<String>` is remote (`DefaultKeysRepository.fetchKeys`) or local.
7. `GetPathMapState` runtime values for `v19`, `v21`, `v22`, `SubscriptionTier`,
   and `cc/b.y` section classification floats. `mimo_dev_prefs.xml` was absent.
8. Chapter/tutorial completion transitions: `chapter_completions` stayed 0 and
   all `tutorial_completions` rows had `is_completed=0`.
9. Chapter-end screen, streak modal, reward screen, leaderboard, paywall.
10. Code evaluation boundary: `WebView.addJavascriptInterface` object class,
    JS→Kotlin message contract, JNI/native libraries, `System.loadLibrary`,
    or any remote executor. Stage 6 adds the interface hook.
11. `lesson-webview.js` gesture/activity/focus/height/ready consumers at runtime.
12. Offline external-URL substitution (M05 Q-25) and image loading offline
    (`https://mimo.app/i/dog_yawn.png` was referenced in shipped JS).
13. Room migration history (M06 Q-24) beyond the measured identity hash
    `2b8ab6d303d9a501bd8c8fb78d8352fc`.
14. Protobuf DataStore `user_preferences.preferences_pb` key/value semantics.
15. Xposed / LSPosed / JVMTI / `strace` / `am dumpheap` / JNI trace availability
    and behaviour on this runner.
16. Server acknowledgement / response body for progress, keys, subscription,
    leaderboard — deliberately out of scope (`SERVER CONFIRMED=0`).
17. Why `DELETE FROM lesson_progress WHERE in_queue = 1` runs even when the
    offline post throws: exact ordering inside `postUnsyncedLessonProgress`.
18. Why the app process restarts during onboarding (observed stage 5), and how
    to keep Frida hooks attached across it without re-attaching.
19. Whether the `f0(false,true)` first argument is a constant or a computed
    `isPracticeProgress`-like flag in all branches (measured only for slides).
20. Whether `tries`/`attempts` can exceed 1 in real interaction (only `1` was
    measured; the constructed-object truth table covers -1/0/1/2/5).
21. Analytics event payload fields for `validated_input_execution_correct_partial_match`.
22. `sk/a` dev-prefs switches: runtime effect of `CREATE_LESSON_PROGRESS_WHEN_SWIPING`,
    `USE_UNPUBLISHED_TRACKS_PACKAGE`, `DISABLE_PREMIUM`.
23. Full `gm.h.a` mapping from `List<LessonModule>` to `LessonInteractionType`.
24. `q.I()` `List.equals` vs `solvedContent` for executable output validation.
25. Multi-locale / non-English shipped content behaviour at runtime.
