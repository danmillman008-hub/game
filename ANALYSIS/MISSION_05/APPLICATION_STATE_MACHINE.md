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
| No system ANR dialog on the final runs | M04 `41998643355`, M05 `42001925381` | `LOGS/ANR_DISMISSAL.txt`, `INTERACTION_TRACE.txt` |
| System ANR dialog over dimmed Mimo (resolved automation failure) | `41997137033` | `LOGS/SCREENSHOT_RUN_41997137033_ANR_OVERLAY.png` |

`VERIFIED_RUNTIME` **stops here for run 1** (`42001925381`): the tap-picker
classified the intro slide as an authentication boundary and made **zero taps**.
Exact reason recorded in `ANALYSIS/RUNTIME/MISSION_05/LOGS/INTERACTION_TRACE.txt`
(`STEP-01 stop_reason=NONE auth_boundary`). Run 2 uses the fixed picker; its
outcome is recorded in `RUNTIME/` once pulled. **No transition beyond the intro
slide is claimed unless its PNG/XML exists.**

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

> **`UNKNOWN`:** the exact linear order, which steps are skippable, and whether
> an account is mandatory before reaching the path map. `signUpAndProceed`
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
IntroSlidesActivity --Get started--> OnboardingActivity      INFERRED
IntroSlidesActivity --I already have an account--> auth      INFERRED (not taken)
OnboardingActivity --> step2/selectpath/reassurance/dailygoal INFERRED (declared fragments)
dailygoal --signUpAndProceed--> PreparingCurriculum          INFERRED
PreparingCurriculum --> MainActivity / PathMapFragment       INFERRED
PathMapFragment --onTutorialClick / navigateToChapter--> ChapterActivity  INFERRED
ChapterActivity --startChapterFlow--> InteractiveLessonFragment / executable  INFERRED
lesson --correct--> next lesson (lessonSolvedAndProceedToNextLesson)  INFERRED
lesson --wrong--> showWrongFeedbackBlock (retry, same lesson)  INFERRED
last lesson --> ChapterFinishedFragment --> PathMapFragment   INFERRED
```

## 4. State classes and persistence hooks — `VERIFIED_STATIC`

| State concern | Evidence |
|---|---|
| Correct / incorrect | `lessonSolvedCorrectly$1`, `lessonSolvedIncorrectly$1`, `lessonSolvedCorrectlyWithPartialMatch$1`, `showWrongFeedbackBlock$1`; DSL `visible-if="correct"/"wrong"` |
| Retry | `showWrongFeedbackBlock` + `LessonProgress.tries/attempts` + `getCorrectLessonsFirstTryCount` |
| Completion | `ChapterCompletion`, `TutorialCompletion` Room rows; `SELECT COUNT(DISTINCT chapter_id)` |
| Locked/unlocked | `GetPathMapState$invoke$3` reads `isCompleted`, `isRequired`, `getType`; `ChapterActivity$showUnlockAnimation`; mapping `UNKNOWN` |
| Progress persistence | `storeLessonProgressInMemory` → `storeLessonProgress` → Room `lesson_progress` (`in_queue`) |
| Resume after restart | `resume_onboarding_from_select_path`, `GET /v1/tracks/completion/lastInteracted`, `MainViewModel$fetchLessonProgressAndPostUnsyncedToBackend`; exact behaviour `UNKNOWN` |
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
no fake server response was injected. `SERVER CONFIRMED = 0`.

**Evidence:** `ANALYSIS/RUNTIME/MISSION_04/*`, `ANALYSIS/RUNTIME/MISSION_05/*`,
`EVIDENCE/STORAGE_AND_ONBOARDING_STRINGS.txt`, `ANALYSIS/MIMO_COMPLETION_ENGINE.json`,
`ANALYSIS/COMPONENT_CATALOG.fa.md`, `ANALYSIS/APPLICATION_FLOWS.fa.md`.
