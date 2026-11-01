# Mission 8 — Stage 1 Report (symbol & lambda recovery)

**Status:** complete · **Base:** Stage 0 commit `4291d42` · **Date:** 2026-11-01

## Delivered (brief §5 outputs)

| File | Content |
|---|---|
| `01_SYMBOL_RECOVERY/RENAMED_CLASS_REGISTER.csv` | 1,148 app classes outside the `com.getmimo` namespace, with superclass, interfaces, method/field counts, recovered owners |
| `01_SYMBOL_RECOVERY/ORIGINAL_METHOD_NAME_MAPPINGS.csv` | 436 original→renamed method mappings (`HIGH 385`, `MEDIUM 51`) |
| `01_SYMBOL_RECOVERY/ORPHAN_LAMBDA_REGISTER.csv` | 1,275 orphan lambdas with original owner, method hint, candidate owner, confidence |
| `01_SYMBOL_RECOVERY/LAMBDA_ENCLOSURE_MAP.json` | 265 original owners → ranked candidate classes with invoke counts and share |
| `01_SYMBOL_RECOVERY/RECOVERY_EVIDENCE.json` | per-lambda instruction evidence (top targets, methods per target) |
| `01_SYMBOL_RECOVERY/SYMBOL_CONFIDENCE_AUDIT.md` | method, confidence rules, HIGH table, five documented limits |
| `01_SYMBOL_RECOVERY/UNRESOLVED_SYMBOLS.csv` | lambdas with no usable candidate, with competing candidates listed |
| `01_SYMBOL_RECOVERY/COMPONENT_CLUSTERS.json` | 12 clusters (content 37 owners, ui/nav 55, authentication 31, learner 12, …) |
| `01_SYMBOL_RECOVERY/evidence/NAMES_*.json` | per-package method-name recovery for 9 packages (109 families, 86 HIGH) |
| `tools/build_symbol_recovery.py` | deterministic builder |

## The decisive rule

Candidates are accepted **only inside the original owner's package**. Renaming preserved packages, so this removes
the two false families a naive run produced (Orbit's DSL builder and the app logger), and it is the reason the
remaining HIGH mappings are trustworthy rather than plausible.

## Owners recovered that the next phases depend on

| Original | Renamed | Lambdas |
|---|---|---|
| `DataStoreUserPreferences` | `com.getmimo.data.local.a` | 70 |
| `ExecutableLessonViewModel` | `com.getmimo.ui.lesson.executable.q` | 70 |
| `InteractiveLessonBaseViewModel` | `com.getmimo.ui.lesson.interactive.base.c` | 18 |
| `InteractiveLessonBaseFragment` | `…interactive.base.b` | 18 |
| `DefaultTracksRepository` | `com.getmimo.data.content.tracks.c` | 7 |
| `CompletionRepository` | `com.getmimo.data.source.local.completion.a` | 7 |
| `DefaultFavoriteTracksRepository` | `…content.tracks.a` | 6 |

## Method vocabularies recovered (HIGH)

* content: `getAllTracks`, `getTrackById`, `getTrackWithChapters`, `getPublishSetVersion`, `getInteractiveLesson`,
  `getExecutableLesson`, `getTutorial`; favorites: `addTrackToFavorites`, `removeTrackFromFavorites`,
  `getFavoriteTracks`, `getRemoteFavoriteTracks`, `syncFavoriteTracksToAdd`, `syncFavoriteTracksToRemove`
* lesson engine: `initialiseViewModel`, `lessonSolvedCorrectly`, `lessonSolvedCorrectlyWithPartialMatch`,
  `lessonSolvedIncorrectly`, `lessonSolvedAndProceedToNextLesson`, `storeLessonProgressInMemory`,
  `initialiseCodeBlocks`, `createInteractiveAiTutorInfo`, `isAiTutorUnlimited`, `showWrongFeedbackBlock`
* executable lessons: `performCodeExecution`, `postCodeExecutionResult`, `generateDiffAndShowSheet`,
  `hideResultSheet`, `doOnLessonIncorrectlySolved`, `ExecutableLessonContent`
* preferences: `clear`, `shouldQueuePathOverviewEta`, `markChapterCompletedInHardMode`, hard-mode intro flags
* billing: `acknowledgePurchase`, `connect`, `loadProductDetails`, `purchaseSubscription`, `awaitCurrentOffering`,
  `awaitPurchaseSafely`, `setFirebaseAppInstanceId`

## Not claimed

Mappings are naming evidence only. No mapping in this stage asserts that a method *does* what its name says — each
must still be read. 144 owners remain unresolved, with the reasons in §5 of the audit.
