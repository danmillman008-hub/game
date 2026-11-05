# APPLICATION_STATE_MACHINE — Mimo 9.35 screens, states and transitions

`VERIFIED_STATIC` = class/string evidence in the original APK ·
`VERIFIED_RUNTIME` = emulator PNG/XML/`dumpsys` · `VERIFIED_BOTH` ·
`INFERRED` (argued) · `UNKNOWN`.
APK `48ce1740…7c7a`, `com.getmimo` 9.35, Android 16 / API 36 / `pixel_7`.

## 1. Runtime-proven states — `VERIFIED_RUNTIME`

| State | Run | Evidence |
|---|---|---|
| Cold launch → `SplashActivity_default` | M04 `41998643355`, M05 `42001925381`/`42002808217` | `resolve-activity --brief`, `am start`, logcat `Start proc …com.getmimo` |
| `IntroSlidesActivity` foreground with 13–15 `com.getmimo` UI nodes | M04 `41998643355`, M05 `42001925381` | `mCurrentFocus=Window{… com.getmimo/com.getmimo.ui.onboarding.intro.IntroSlidesActivity}`, `topResumedActivity=…IntroSlidesActivity`, `UI_HIERARCHY/STEP-00.xml` |
| Intro carousel slides | M04 `41997975847` ("Learn at your own pace"), `41998643355` ("Change your career"), M05 `42001925381` ("Build projects") | `SCREENSHOTS/TEST-004_first_usable_screen.png`, `ANALYSIS/RUNTIME/MISSION_05/SCREENSHOTS/STEP-00.png` |
| Buttons `Get started` / `I already have an account` | M04 + M05 | `UI_HIERARCHY/STEP-00.xml` (exact bounds `[68,1989][1012,2110]` and `[204,2148][876,2274]`) |
| `com.getmimo:id/vp_intro_slides` (ViewPager), `tv_onboarding_page_title`, `tv_onboarding_page_description`, `compose_content` | M04 + M05 | XML resource ids |
| No system ANR dialog on the final runs | M04 `41998643355`, M05 `42001925381`, `42002808217` | `LOGS/ANR_DISMISSAL.txt`, `INTERACTION_TRACE.txt` |
| `Get started` → `OnboardingActivity` "Welcome to Mimo!" | M05 `42002808217` | `STEP-01.png/.xml`, `mCurrentFocus=…OnboardingActivity` |
| 12-step onboarding questionnaire, all in `OnboardingActivity` | M05 `42002808217` | `STEP-01..12.*`, `RUNTIME/STATES.jsonl` |
| On-device path recommendation "Front-End Developer is the best choice for you!" (HTML/CSS/JS/React) | M05 `42002808217` | `STEP-11.png/.xml` |
| Transient loading screen (7 nodes, no text) → next question | M05 `42002808217` | `STEP-08.*` → `STEP-09.*` |
| Cold start with `Active default network: none` → full intro + 3 onboarding states, UI XML byte-identical to online | M05 `42002808217` | `OFFLINE-00..03.*`, `RUNTIME/OFFLINE_EQUALITY_PROOF.json` |
| **Full 24-tap chain**: intro → 20-screen onboarding → path recommendation → daily goal (5/10/20 min) → notification permission → device reassurance → `AuthenticationActivity` | M05 `42003884423` | `RUN_42003884423/LOGS/INTERACTION_TRACE.txt`, `STEP-00..21.*` |
| Built-in **`Skip`** on the signup screen → `MainActivity` "Welcome to your learning path!" → `ChapterActivity` → **real lesson** "Guess the letter" | M05 `42003884423` | `STEP-21..24.png/.xml` |
| Offline cold start resumes at `AuthenticationActivity` (onboarding state persisted across `am force-stop`) | M05 `42003884423` | `OFFLINE-00.*` |
| Offline learning path shows red banner **"Connect to the internet to progress further"**; practice-optional chapter and executable lesson still open | M05 `42003884423` | `OFFLINE-01..05.*` |
| **Incorrect-answer state**: tapping wrong option `Q` → red "Try again", `Q` disabled, retry available; `Continue` → next lesson | M05 `42005358012` | `RUN_42005358012/SCREENSHOTS/LESSON-WRONG-01.png`, `…/LESSON-CONTINUE.*` |
| Different onboarding answers select track 274 **"Automating Tasks with AI"**; offline AI/ChatGPT lessons render (Luma for Teams, ideal customer, challenge checklist) | M05 `42006697783` | `OFFLINE-01..06.*`, `STEP-22.*` |
| System ANR dialog over dimmed Mimo (resolved automation failure) | `41997137033` | `LOGS/SCREENSHOT_RUN_41997137033_ANR_OVERLAY.png` |

`VERIFIED_RUNTIME` **stops here for run 1** (`42001925381`): the tap-picker
classified the intro slide as an authentication boundary and made **zero taps**
(exact reason in `LOGS/INTERACTION_TRACE.txt`). Run `42002808217` captured 16
taps + an offline cold start (`RUNTIME/RUN_42002808217_FINDINGS.md`). Run
`42003884423` captured **24 taps through to a real lesson** and an offline chain
that reached the learning path and an executable practice lesson
(`RUNTIME/RUN_42003884423_FINDINGS.md`). Run `42005358012` probes correct/wrong
answer states. **No transition beyond a captured PNG/XML is claimed.**

## 2. Screen/component inventory — `VERIFIED_STATIC` (DEX class names)

Recovered from `classes.dex` string table and JADX package tree
(`EVIDENCE/STORAGE_AND_ONBOARDING_STRINGS.txt`, `SCHEMAS/JADX_MODEL_FIELDS.json`):

### 2.1 Entry / main
`com.getmimo.App`, `ui/main/MainActivity`, `MainViewModel` with
`doOnMainActivityCreated`, `sendOnboardingData$1..5`,
`fetchLessonProgressAndPostUnsyncedToBackend`,
`goToMainActivity` / `makeMainActivity`.
`ui/onboarding/OnboardingActivity`, `ui/onboarding/intro/IntroSlidesActivity`,
`IntroSlidesViewModel.viewPagerRotationFlow` (auto-rotating intro carousel).

### 2.2 Onboarding flow (declared, order `INFERRED`)
| Fragment / ViewModel | Suggested stage |
|---|---|
| `onboarding.intro.IntroSlidesActivity` | 3 intro slides — `VERIFIED_RUNTIME` |
| `onboarding.step2.SetExperienceFragment` / `SetExperienceViewModel` | experience level |
| `onboarding.selectpath.OnboardingSelectPathContainerFragment` | path selection container |
| `onboarding.selectpath.pickapath.OnboardingPickAPathFragment` / `ViewModel` (`onContinueClick`, `onBack`, `dispatch$1..4`) | choose a learning path |
| `onboarding.reassurance.OnboardingMotiveReassuranceFragment` | motive reassurance |
| `.OnboardingPathReassuranceFragment` | path reassurance |
| `.OnboardingDeviceReassuranceFragment` | device reassurance |
| `onboarding.dailygoal.OnboardingSetDailyGoalFragment` / `ViewModel.signUpAndProceed` | daily goal (Casual/Regular/Serious per `MIMO_SCORING_MODEL.json`) |
| `onboarding.postsignup.OnboardingPreparingCurriculumFragment` / `ViewModel.curriculumViewState` | "preparing curriculum" (post-signup) |
| `interactors.path.LoadOnboardingPaths`, `interactors.settings.SetOnboardingSettings` | onboarding side-effects |
| `OnboardingSetPreference`, `Onboarding(authenticationLocation=…)`, `SignupAfterOnboardingPurchase` | onboarding state objects |

`VERIFIED_STATIC` literals: `onboarding_skill_preference_picked`,
`resume_onboarding_from_select_path`, `show_learning_preference_reassurance`,
`onboarding_daily_notifications_enabled`,
`onboarding_daily_notifications_reminder_time`,
`trigger_paywall_onboarding_exit_offer`,
`experiment_adapted_onboarding_android_local`.

> **`VERIFIED_RUNTIME` (runs `42002808217`, `42003884423`):** the **entire**
> onboarding chain is now observed: 20+ screens, daily goal
> (Casual 5 / Regular 10 / Serious 20 min), reminder + notification permission,
> device reassurance, `AuthenticationActivity`, the built-in `Skip`, and entry
> into `MainActivity` → `ChapterActivity` → a real lesson. An account is **not**
> required to reach the first lesson. **`UNKNOWN`:** the signed-in branch
> (`signUpAndProceed` → `PreparingCurriculum`), which onboarding steps call the
> server, and remote-config gating of individual reassurance screens. `signUpAndProceed`
 suggests authentication is embedded in onboarding; no credential was created
 and no auth boundary was crossed in M05.

### 2.3 Learning path (main learning surface)
`ui/path/map/PathMapFragment`, `PathMapViewModel` with `init$2..5`,
`navigateToChapter`, `onTutorialClick`, `onNextSectionShown`,
`onCertificateClick`, `fetchTrackEta`, `refreshDialogs`,
`setHardModeEnabled`, `pathOverviewTooltipState`, `practiceOptionalIntroTutorial`,
`showResubscribeMascotOverlay`, `showUnlockAnimation`.
Interactors: `GetPathMapState`, `GetPathMapDialogs`,
`ObservePathToolbarState`, `RefreshPathToolbarState`.
M02 recorded 30 `path_map_state_fields` (e.g. `activeNodeIds`, `currentNodeId`,
`ancestorNodeIds`, `childNodes`, `selectedSectionIndex`, `chapterIndex`,
`borderPath`, `radiusY`, `offsetXPx/YPx`, `snapRadius`, `touchRadius`) and
55 `path_map_interactors`. Geometry/lock mapping remains `UNKNOWN`.

### 2.4 Chapter / lesson session
`ui/chapter/ChapterActivity` with `startChapterFlow`, `setupChapterToolbar`,
`openHardModeSessionFromIntro`, `showHardModeIntro` (regular vs hard mode),
`showUnlockAnimation`, `showConfirmExitDialog`, `tryExitLesson`,
`showReportLessonFragment`, `releaseChapterContent`.
`ui/lesson/interactive/InteractiveLessonFragment` + `InteractiveLessonViewModel`
(`initialise`, `loadLessonContent`, `withClientSideSyntaxHighlighting`),
`base/InteractiveLessonBaseViewModel` with:
`initialiseViewModel`, `initialiseCodeBlocks`, `onLessonRun`,
`onValidatedInputExecuted`, `lessonSolvedCorrectly`,
`lessonSolvedCorrectlyWithPartialMatch`, `lessonSolvedIncorrectly`,
`lessonSolvedAndProceedToNextLesson`, `showWrongFeedbackBlock`,
`storeLessonProgressInMemory`, `createInteractiveAiTutorInfo`,
`isAiTutorUnlimited`.
Exercise-specific ViewModels: `fillthegap`, `selection`, `spell`,
`validatedinput`, `webview`, `nointeraction` (`goToNextPage`), plus
`InteractiveLessonFeedbackBottomSheetDialogFragment`.
`ui/lesson/executable/*` incl. `codediff/CodeDiffViewModel` and
`ui/codeplayground/*`, `ui/codeeditor/*`.

### 2.5 Chapter-end / rewards
`chapterendview/main/ChapterFinishedFragment` (`onChapterFinishedContinue`,
`showReward`, `showRatingBottomSheet`), `ChapterFinishedViewModel`
(`handleOnlineState`, `handleOfflineState`, `handleChapterAlreadyCompletedState`,
`getChapterEndSuccessStateWithRetry`, `storeAndPostAllLessonProgress`,
`shouldShowStreakChallengeScreen`, `shouldShowRatingBottomSheet`,
`showSignupPrompt`, `consumeKeyIfNeeded`), plus
`ChapterFinishedEtaFragment`, `ChapterFinishedStreakFragment`,
`ChapterFinishedFreeStreakGoalFragment`, `ChapterFinishedLeaderboardFragment`,
`ChapterFinishedDailyGoalProgressView`, `ChapterFinishedSynchronizationException`.
Interactors: `GetChapterEndSuccessState`, `CreateChapterEndScreens`,
`GetChapterToolbarType`, `GetChapterEndProgressWithEtaScreenData`,
`QueuePathOverviewEtaIfNeeded`.

## 3. Reconstructed transitions — `INFERRED` unless marked

```
[launcher] --resolve-activity--> SplashActivity_default      VERIFIED_RUNTIME
SplashActivity_default --> IntroSlidesActivity               VERIFIED_RUNTIME
IntroSlidesActivity --Get started--> OnboardingActivity      VERIFIED_RUNTIME (42002808217)
IntroSlidesActivity --I already have an account--> auth      INFERRED (not taken)
OnboardingActivity --> Welcome --> motive/goal/reassurance
      --> role/work/experience --> loading --> interest
      --> PATH RECOMMENDATION (Front-End Developer)
      --> "10M+ people" reassurance                         VERIFIED_RUNTIME (STEP-01..12)
OnboardingActivity --> step2/selectpath/dailygoal            INFERRED (declared fragments beyond STEP-12)
dailygoal --> reminder/permissions --> AuthenticationActivity  VERIFIED_RUNTIME (42003884423)
AuthenticationActivity --built-in Skip--> MainActivity       VERIFIED_RUNTIME (42003884423)
MainActivity --> ChapterActivity --> InteractiveLesson       VERIFIED_RUNTIME (STEP-23..24)
dailygoal --signUpAndProceed--> PreparingCurriculum          INFERRED (signed-in branch, not taken)
PreparingCurriculum --> PathMapFragment                      INFERRED
PathMapFragment --onTutorialClick / navigateToChapter--> ChapterActivity  INFERRED
ChapterActivity --startChapterFlow--> InteractiveLessonFragment / executable  INFERRED
lesson --correct--> next lesson (lessonSolvedAndProceedToNextLesson)  INFERRED
lesson --wrong--> showWrongFeedbackBlock (retry, same lesson)  INFERRED
last lesson --> ChapterFinishedFragment --> PathMapFragment   INFERRED
```

## 4. State classes and persistence hooks — `VERIFIED_STATIC`

| State concern | Evidence |
|---|---|
| Correct / incorrect | DSL `visible-if="correct"/"wrong"`; **incorrect state `VERIFIED_RUNTIME`** ("Try again", option disabled, retry) in run `42005358012`; static hooks `lessonSolvedCorrectly$1`, `lessonSolvedIncorrectly$1`, `lessonSolvedCorrectlyWithPartialMatch$1`, `showWrongFeedbackBlock$1`. Correct state `UNKNOWN` |
| Retry | `showWrongFeedbackBlock` + `LessonProgress.tries/attempts` + `getCorrectLessonsFirstTryCount` |
| Completion | `ChapterCompletion`, `TutorialCompletion` Room rows; `SELECT COUNT(DISTINCT chapter_id)` |
| Locked/unlocked | `GetPathMapState$invoke$3` reads `isCompleted`, `isRequired`, `getType`; `ChapterActivity$showUnlockAnimation`; mapping `UNKNOWN` |
| Progress persistence | `storeLessonProgressInMemory` → `storeLessonProgress` → Room `lesson_progress` (`in_queue`) |
| Resume after restart | `VERIFIED_RUNTIME` (42003884423): offline cold start after `am force-stop` resumed at `AuthenticationActivity` with the chosen path, i.e. onboarding selections persisted. Static hooks: `resume_onboarding_from_select_path`, `GET /v1/tracks/completion/lastInteracted`, `MainViewModel$fetchLessonProgressAndPostUnsyncedToBackend`. Exact per-lesson resume `UNKNOWN` |
| Offline / online | `ChapterFinishedViewModel$handleOfflineState$1`, `$handleOnlineState$1`, `ChapterFinishedSynchronizationException` |
| Back / exit | `ChapterActivity$showConfirmExitDialog`, `tryExitLesson`, `OnboardingPickAPathViewModel$onBack$1` |
| Hard mode | `setupHardModeState`, `setHardModeEnabled`, `StoreSyntheticHardModeProgress`, `openHardModeSessionFromIntro` |

## 5. Navigation mechanism — `UNKNOWN` with static clues

- 9 deep links and ~300 route-like strings recorded in M02; `NavHost`/back-stack
  shape not recovered.
- Official launcher activity: `com.getmimo/.ui.SplashActivity_default`
  (`VERIFIED_RUNTIME` via `cmd package resolve-activity`, run `41998643355`).
- `AndroidManifest.xml` has 61 activities / 24 permissions (M02).
- No claim about Jetpack Navigation vs fragment transactions is made without a
  decompiled call site; `UNKNOWN`.

## 6. Deliberate boundary

No credentials were invented, no account was created, no login/signup button
was pressed, no `I already have an account` was tapped, no private DB was read,
no fake server response was injected. The **shipped `Skip` control** on the
signup screen was tapped once; that is a normal UI path of the original app,
not an authentication bypass. The signup screen itself is captured at
`STEP-21.png/.xml`. `SERVER CONFIRMED = 0`.

**Evidence:** `ANALYSIS/RUNTIME/MISSION_04/*`, `ANALYSIS/RUNTIME/MISSION_05/*`,
`EVIDENCE/STORAGE_AND_ONBOARDING_STRINGS.txt`, `ANALYSIS/MIMO_COMPLETION_ENGINE.json`,
`ANALYSIS/COMPONENT_CATALOG.fa.md`, `ANALYSIS/APPLICATION_FLOWS.fa.md`.
