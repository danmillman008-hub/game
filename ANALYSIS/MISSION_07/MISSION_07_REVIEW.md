# MISSION 07 — REVIEW

**Branch:** `arena/aebb90b7-game` · **baseline:** M06 `cfc8ea41` ·
**original APK unchanged:** SHA-256
`48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`
(142,353,499 B) · **`SERVER CONFIRMED = 0`** · **7/7 workflow runs SUCCESS**.
M01–M06 evidence preserved verbatim; `ANALYSIS/EVIDENCE_INDEX.json` gained
`mission_07_append`.

## What was asked
Live runtime reconstruction of the Mimo 9.35 client and offline state
forensics: assess root/Frida/private-DB access, hook recovered DEX methods,
invoke validators with controlled inputs, capture a real correct/wrong answer
with before/after Room rows, verify genuine offline isolation and force-stop
restoration, classify every operation A–E, and produce 18 numbered reports,
an evidence database, diagrams, acceptance criteria and open questions —
without modifying the APK or reconstructing a server.

## What was delivered
* 18 numbered reports `00`–`18` (+ `README.md`, `MISSION_07_REVIEW.md`),
  5 Mermaid diagrams, 2 distilled experiment notes,
  `16_EVIDENCE_DATABASE.json` (**202 entries**, every referenced path verified
  to exist, 0 missing), and the global index append.
* Runtime harness in `ANALYSIS/RUNTIME/MISSION_07/`: 6 stage scripts, PID-attach
  Frida driver, Java bridge, answer driver, shipped-answer lesson classifier,
  SQLite snapshot tool, plus all raw evidence (`ENV/`, `FRIDA/`, `TRACES/`,
  `DB/SNAPSHOT_*`, `UI/`, `EXPERIMENTS/`, `LOGS/`).
* Static-decode supplement and a 2,855-question shipped-answer index extracted
  from the ORIGINAL APK, so automation never guesses an answer.

## Headline measured results
1. **Environment** — Android 16 / API 36 `sdk_gphone64_x86_64`, `adb root`
   uid 0, SELinux Enforcing→Permissive, `/system/bin/sqlite3`, private app data
   readable. Frida 17.25.2 needs an explicit Java bridge: bundling
   `frida-tools 14.11.0`'s compiled `java.js` (237,079 B) fixed
   `ReferenceError: 'Java' is not defined` and enabled **42 Java hooks**.
2. **Validators at runtime** — `qm.i.a` is a Unicode-aware
   lowercase+`isLetterOrDigit`+`<>() :{},.` normaliser (21 cases);
   `km.f.b(List)` is `∀ item: selected == correct` (8 cases);
   `LessonProgress.isSolvedCorrectly() = tries >= 1`, independent of
   `attempts` (20 objects — corrects M05's `attempts >= 1`); `te.c.b()`
   parses real shipped `Paragraph`/`Code`/`FillTheGap`/`Selection` modules;
   `gm.h.a()` maps empty→`None(slide)` and a real fill-the-gap list→
   `FillTheGap(interactionTypeName=fill_the_gap)`.
3. **Real answer → persisted row** — wrong `Q` → `Try again` (Q disabled, no
   native hook, no DB change); correct `D` → `Correct!`, `D O G`, `dog_yawn`;
   `Continue` → next code-editor lesson **and a new `lesson_progress` row**:
   `151403 | … | tries=1 | tutorialId=904 | tutorialVersion=161 | trackId=219 |
   publishSetVersion=753 | attempts=1 | isPracticeProgress=0 | inQueue=1`.
4. **Hook chain at the exact answer moment** (stage 6, 13:20:08) —
   `c.U() → c.H(1,1) → LessonProgressRepository.createLessonProgress(
   LessonBundle(lessonId=151403, lessonIndex=1, tutorialTitle=Discovering HTML
   and Tags)) → c.e0() → LessonProgressQueue.storeLessonProgress →
   isSolvedCorrectly()=true → c.f0(false,true) → c.N()`. `f0`'s first argument
   is **false**, correcting M06. **No `V()/W()/X()` dispatch** occurred: the
   WebView exercise is JS-local, a measured negative.
5. **Offline** — `Active default network: none` + `Network is unreachable` +
   `airplane_mode_on=1`. `postUnsyncedLessonProgress` throws
   `com.getmimo.network.NoConnectionException`; `DELETE FROM lesson_progress
   WHERE in_queue = 1` removes queued rows. Measured 1→0 (stage 4) and
   **2→0** (stages 5/6) across force-stop + cold start, while
   `tutorial_completions` (868) and the Room identity hash stay unchanged.
   **Correction:** the `in_queue=1` queue is not durable across an offline cold
   start on this build; M05/M06's restore expectation is not confirmed.
6. **Operations classified A–E** in `09_OFFLINE_EXECUTION_RESULTS.md`:
   curriculum, navigation, Room, prefs, validators, connectivity and
   force-stop UI restoration are local; analytics/queued progress are local+queued;
   auth/purchase/keys/leaderboard/XP are remote or unknown.

## Honest limitations (not hidden)
* Native `V()/W()/X()` feedback (`jm/m`, `jm/n`, `jm/o`) was never dispatched
  by a submitted validatedInput/selection/fillTheGap answer → `UNKNOWN`.
* Scoring/XP/streak/leaderboard formulas: no local arithmetic found, remote
  DTOs only → `UNKNOWN`. No XP column in `mimo.db`.
* Unlock key shape is static (`"<long>:<long>:<long>"` set membership); live key
  values and `SubscriptionTier` gating → `UNKNOWN`. `mimo_dev_prefs.xml` absent.
* Chapter completion never reached (`chapter_completions = 0` in all snapshots);
  no chapter-end screen, streak modal or paywall.
* Code evaluation boundary (WebView JS interface, JNI/native libs, remote
  executor) not instrumented → `UNKNOWN`. `WebView.addJavascriptInterface`
  emitted no event in the stage-6 attach window.
* Xposed/LSPosed/JVMTI/`strace`/heap dump were not exercised — `UNKNOWN`, not
  "unavailable".
* Stage 2 initially failed (`ReferenceError: 'Java' is not defined`), stage 3
  reached the wrong lesson, stage 5's hooks went silent after an onboarding
  process restart. All three are documented in `14_EXPERIMENT_LOG_AND_LIMITATIONS.md`
  and were fixed in later runs.
* Adaptive onboarding differs from M05's exact 24-tap chain; M07 uses measured
  `uiautomator` coordinates instead of blind replay.
* No server response, no credentials, no APK patch. `SERVER CONFIRMED = 0`.

## Acceptance summary
`17_ACCEPTANCE_CRITERIA.md`: **15 PASS, 3 PARTIAL, 2 NOT MET** (the two NOT
MET items are scoring/XP reconstruction and unlock/chapter-completion
reconstruction; native validator dispatch is a measured-negative PARTIAL — all
explicitly reported as `UNKNOWN` rather than fabricated). The mission's core requirement — live
answer → correct/wrong UI → exact Room row → offline queue behaviour with
runtime-verified validators — is met.

## Start here
`README.md` (deliverable index) → `15_ANSWER_TO_SCORING_RECONSTRUCTION.md`
(executable local spec) → `17_ACCEPTANCE_CRITERIA.md` →
`18_OPEN_QUESTIONS.md` → `16_EVIDENCE_DATABASE.json` (machine-readable claims).
Raw evidence: `ANALYSIS/RUNTIME/MISSION_07/`.
