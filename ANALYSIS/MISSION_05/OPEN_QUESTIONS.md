# OPEN_QUESTIONS — what M05 did not resolve, and the cheapest next experiment

`UNKNOWN` items are listed with the **exact** missing information, the evidence
that exists, and a concrete method that would resolve it. No answer is invented.
`SERVER CONFIRMED = 0`; backend behaviour is explicitly out of scope.

## A. Highest-value blockers for a faithful offline client

| # | Question | What is known (`VERIFIED_STATIC` unless noted) | What is missing | Cheapest resolution |
|---:|---|---|---|---|
| 1 | **Unlock / prerequisite rule** for path nodes | `GetPathMapState$invoke$3` reads `isCompleted`, `isRequired`, `getType`; `ChapterActivity$showUnlockAnimation`; 30 `path_map_state_fields` incl. `activeNodeIds`, `currentNodeId`, `ancestorNodeIds`, `childNodes`, `selectedSectionIndex` | exact predicate mapping a node to `locked / available / completed / practiceOptional`, and whether a challenge gates a section | decompile `GetPathMapState$invoke$3` bytecode (DEX `invoke` → Smali) and read the branch conditions; or runtime: complete one chapter and dump the path XML before/after |
| 2 | **Chapter / tutorial completion threshold** | Room `chapter_completions` / `tutorial_completions`; `SELECT COUNT(DISTINCT chapter_id)`; `GetChapterEndSuccessState` | how many lessons/attempts must pass before a completion row is written | instrument a real session (answer N lessons, observe `ChapterFinishedFragment`); private DB contents remain `UNKNOWN` without root |
| 3 | **All scoring formulas** | `rewardedSparksForCorrectAnswer`, `getRewardMultiplier`, `dailySparksGoal`, `dailyGoalCoinReward`, `activeStreakLength`, `DAILY_GOAL_*`, 5 leaderboard leagues | numerical values, first-try bonus, XP per lesson, streak break/repair, daily-goal level→target, coin reward | static: disassemble the `LessonProgressQueue`/`GetChapterEndSuccessState` bodies (JADX failed on these); runtime: not observable without an account |
| 4 | **`validatedInput` / `fillTheGap` index→token algorithm** | `Option(boolean correct, CharSequence content, int startIndex, int endIndex)`; `validatedInput startIndex=108 endIndex=113` resolves to `Login` in one real lesson; 1,772 / 9,957 occurrences | how the `<content>` token stream is built (whitespace, `<text type="break">`, nested `<code>`, unicode escapes, hard-mode variants) | read `ParserModule.kt` bytecode, or brute-force the reconstruction against all 1,772 samples to find the unique index rule |
| 5 | **`solvedContent` usage** | shipped for 4,024 executable lessons; `ui/lesson/executable/codediff/CodeDiffViewModel` exists | whether it is used locally for a diff/validation or only for display after a server `hasPassed` | decompile `CodeDiffViewModel`; runtime: submit one executable lesson offline |
| 6 | **Offline chapter-end composition** | `handleOfflineState$1`, `handleOnlineState$1`, `ChapterFinishedSynchronizationException`, `in_queue` outbox | which reward/streak/ETA screens are shown offline, and whether progress is replayed on reconnect | runtime: complete a chapter with wifi+data disabled (requires reaching a lesson first) |
| 7 | **Signed-in onboarding branch and remote-config gating** | **Full onboarding chain is `VERIFIED_RUNTIME` (42003884423, 24 taps)**: intro → 20 screens → path recommendation → daily goal (5/10/20 min) → reminder/permission → device reassurance → `AuthenticationActivity` → built-in `Skip` → `MainActivity` → `ChapterActivity` → real lesson. An account is **not** needed to reach the first lesson | the `signUpAndProceed` → `PreparingCurriculum` branch, which steps call the server, and which reassurance screens are A/B gated | would require an account (out of scope) or Smali of `MainViewModel$sendOnboardingData` |
| 8 | **App init / navigation internals** | `App.onCreate` (JADX `Method not decompiled`), 61 activities, 9 deep links, ~300 route strings | Hilt/DI graph init order, NavHost graph, back-stack behaviour | Smali of `App.onCreate` and the navigation graph XML |
| 9 | **`ExecuteFilesResponse.tests[]` semantics** | endpoints `…/runFiles`, `/v1/code/runfiles`; `ExecuteLessonResponse(hasPassed,error,output,tests[hasPassed,description])`; `ExecuteFilesResponse(hasPassed,consoleOutput,error,hostedProjectUrl,tests[hasPassed,description,error])` | test-case definitions, per-language runner, pass criteria | static: find the server request/response DTOs and any local mock; **do not** fabricate a server response |
| 10 | **Content update mechanism** | `publishSetVersion=753` shipped; `publish_set_version` stored per progress row | how a newer version is delivered (no endpoint among the 53 named for it) | search `remote_config.json` / Firebase RC keys and `DefaultTracksRepository.getPublishSetVersion` call sites |
| 11 | **Local cache of remote economy state** | `user_preferences` flags; `SharedPrefsBackedUserProperties`; WorkManager tables | whether XP/streak values are cached locally at all, and for how long | runtime with an account (out of scope) or `run-as`/root (prohibited) |
| 12 | **`spell` / `Reveal` / `MultipleChoice` behaviour in v753** | enum values + UI packages exist; v52 `testdata/127-0-1.html` uses `spell`; English v753 has 0 `spell` interactions | whether other locales use them | scan the other 9 locale directories (10,298 files) with the same stats script |

## B. Runtime gaps (no legitimate account used)

| # | Question | Status | Method |
|---:|---|---|---|
| 13 | Does an interactive lesson run and accept a correct answer offline? | A real interactive lesson **renders** (`VERIFIED_RUNTIME` STEP-24) and lesson content renders offline; answer submission not yet observed | run `42005358012` taps the `Q/R/D` options |
| 14 | Does progress survive force-stop / cold restart? | **Onboarding selections do** (`VERIFIED_RUNTIME` 42003884423 OFFLINE-00: cold start resumed at `AuthenticationActivity` with the chosen path, intro slides did not reappear). Per-lesson progress `UNKNOWN` | repeat a lesson then cold-start; compare path XML |
| 15 | What exactly happens when wifi+data are disabled at cold start? | **PARTIALLY RESOLVED** (`VERIFIED_RUNTIME`): run `42002808217` — intro + 3 onboarding states byte-identical to online; run `42003884423` — cold start resumes at `AuthenticationActivity` (persisted state), `Skip` → learning path with red **"Connect to the internet to progress further"** banner, practice-optional chapter card and a fully rendered executable lesson. Still `UNKNOWN`: whether progression is truly blocked, code execution offline, chapter-end offline | a session that submits an answer/code offline |
| 16 | Are the 4,257 external lesson URLs actually fetched at runtime? | `UNKNOWN` (content strings only). The two lessons observed at runtime use **inline** `<webview>` HTML/CSS/JS with no external asset | logcat/`dumpsys netstats` while rendering an affected lesson |
| 17 | Which native lib renders onboarding? | only 4 load lines observed; `librive-android.so` not observed on that path | `nativeloader` logcat at each screen |

## C. Deliberately out of scope (per mission definition)

- Any server-side business logic, response body, or backend reconstruction.
- Authentication, account creation, credentials, auth bypass, purchases,
  payments, TLS/certificate bypass, fake server responses.
- Root access / private DB file extraction (`allowBackup=false`).
- Rebuilding/repatching/repackaging the APK, DEX, resources, manifest,
  signature or native libraries.
- Rewriting `mimo-ui/UPGRADE`, v12.5-fa, or any M01–M04 deliverable.

## D. Known tool limitations (recorded once, not retried)

- JADX archive has only 2,211 `.java` files; many classes show
  `JADX ERROR: NullPointerException in pass: ClassModifier` or
  `Method not decompiled`. Workaround: DEX string/class-name evidence +
  Smali if a specific body is needed. Do **not** re-run JADX for the same output.
- Local sandbox has no emulator/ADB/SDK/Java/KVM; runtime evidence comes only
  from `.github/workflows/mimo-runtime-verification.yml` on GitHub Actions.
- `workflow_dispatch` on a non-default branch returned HTTP 404 in M03; the
  narrow `_DISPATCH_TRIGGER` push fallback is used instead.
- Pinned `android-emulator-runner` splits `script:` lines into separate `sh -c`
  invocations — the workflow `script:` **must remain one line**.
- M04 E2B token endpoint returned 403 (`e2b-traffic-access-token missing`);
  method 1 is disproved. Two-chunk Drive transfer is the working path.
- M05 run `42001925381` tap-picker bug (Compose descendant labels) made 0 taps;
  fixed in `42002808217`. Exact reason logged, not hidden.

**Cross-references:** `OFFLINE_DEPENDENCY_MATRIX.md`, `LEARNING_ENGINE.md`,
`CONTENT_MODEL.md`, `APPLICATION_STATE_MACHINE.md`, `EVIDENCE_DATABASE.json`,
`../RUNTIME/MISSION_05/`.
