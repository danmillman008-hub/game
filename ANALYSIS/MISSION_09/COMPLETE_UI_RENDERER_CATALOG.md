# MIMO 9.35 — COMPLETE UI / RENDERER CATALOG

**Document:** `COMPLETE_UI_RENDERER_CATALOG.md` · **Mission:** MISSION 09 (final reconstruction) · **Branch:** `arena/aebb90b7-game`
**Target APK:** `com.getmimo` 9.35, `versionCode=1792759685`, 142,353,499 B, SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` — unchanged.
**SERVER CONFIRMED = 0.** Classification vocabulary: `VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_ASSET`, `VERIFIED_DATABASE`, `VERIFIED_NETWORK_OBSERVATION`, `INFERRED`, `UNKNOWN`, `SERVER_DEPENDENT`.
Evidence codes resolve in `COMPLETE_EVIDENCE_DATABASE.json` / `COMPLETE_SYSTEM_MAP.json -> evidence_index`.

---


## 1. Screen hierarchy (measured resource IDs / content descriptions)

`MainActivity`: `main_activity_root`, `contentFrame`, `bottom_navigation_view`
(`com.getmimo:id/bottom_navigation_view`), `container_bottombar` (`#7f0a01d1`, measured in
`MainActivity.B()` `this_fields.C`), `toolbar` with numeric counters.
`ChapterActivity`: `vp_lessons` (ViewPager), `container_lesson_interactive`,
`btn_lesson_close`, `practice_lesson_button`, `btn_explanation_continue`, quit dialog.
Compose: `anonymous_user_lock_view`, path-map nodes exposed through `content-desc`
(`Path Icon`, `PRACTICE`, `TUTORIAL`, `CHAPTER`) rather than resource IDs [E14, E29].

### Bottom navigation (GAP A — closed at method level in M09)

`com.getmimo.ui.navigation.NavigationBar.setActive` executed with
`args=["Path(showStore=false, showDiscountDrawer=false, shouldSkipDialogRefresh=false)"]` and `this_fields.e` = the **exact destination map** [E29]:

```
2131361976 -> Path(showStore=false, showDiscountDrawer=false, shouldSkipDialogRefresh=false)
2131361974 -> Practice
2131361973 -> Leaderboard
2131361975 -> Profile(scrollToPlayground=false)
```
Measured UI bounds / resource IDs [E14]:
`Learn [0,2190][270,2337]` `bottom_navigation_item_track`,
`Practice [270,2190][540,2337]` `bottom_navigation_item_practice`,
`Leaderboard [540,2190][810,2337]` `bottom_navigation_item_leaderboard`,
`Profile [810,2190][1080,2337]` `bottom_navigation_item_profile`.

`MainActivity.B()` returns `com.getmimo.ui.main.d` (MainViewModel) whose live fields are
the **bottom-nav -> ViewModel -> Repository** chain [E29]:

| Field | Live object | Role |
|---|---|---|
| `A` | `com.getmimo.network.a` | connectivity |
| `B`,`E` | `com.getmimo.data.source.remote.iap.b` | IAP / subscription |
| `G` | `com.getmimo.data.source.remote.keys.a` | remote keys repository |
| `I` | `com.getmimo.interactors.practice.c` | practice interactor |
| `J`,`K`,`L`,`M` | `capacity=64,data=[]` channels | UI effect/ SharedFlow |
| `N` | `kotlinx.coroutines.flow.i` | state flow |

`MainViewModel.F()` is invoked from `MainActivity$onCreate$2`, `I(true)` on start,
`H()` from `checkIfLeaderboardBadgeShouldBeShown` / `shouldShowLeaderboardBadge`,
`updateData$1` invokes `com.getmimo.interactors.path.sections.a` (unlock state), and
`RefreshPathToolbarState$refreshCoinsFlow$1` / `$refreshKeysFlow$1` invoke the coins and
keys remote repositories. All are `VERIFIED_RUNTIME` in M09 run `42077425594` [E29].

**Limitation:** the M09 run reached `MainActivity` with an explicit intent after the
fixed 20-tap onboarding chain stalled at step 4 on this build; the subsequent
Practice/Leaderboard/Profile taps resumed an incomplete `OnboardingActivity` back stack.
Those three *screen contents* are therefore `UNKNOWN`, not claimed as destinations.
The destination **map** and the `setActive` dispatch are, however, directly measured.
M08 `UI/S234_resume_02_after.xml` independently verifies the guest **Practice** gate
screen (`Lock in your learning / Create a profile to access practice content`).

## 2. Lesson renderer catalogue

See `COMPLETE_LESSON_ENGINE_SPEC.md` §2–§3 for exact DSL, parser and validators.
Renderer families derived from shipped DSL tags (VERIFIED_ASSET):
`fillTheGap`, `MultipleChoice`, `executableFiles`, `validatedInput`,
`InteractiveWebView`, `noninteractiveSlide`, `SingleChoice`, `Spell`, `Reveal`.
The `COMPLETE_CURRICULUM_GRAPH.json` `rendererFamilies` field classifies all 37,183 lesson
placements.

## 3. WebView / editor / native boundaries

* `lesson-webview.js` bridge messages: `gesture`, `activity`, `focus`, `height`, `ready` [E33].
* WebView hooks added in M09: `loadUrl`, `loadDataWithBaseURL`, `evaluateJavascript`,
  `postUrl`, `WebViewClient.shouldOverrideUrlLoading`. **Result: 0 `webview` events in M09**
  because no interactive lesson was reached (`lesson_matrix_not_executed`) [E29].
  M07 stage 6 likewise recorded 0 `WebView.addJavascriptInterface` events.
  Native bridge object/method names, payload schema and callbacks remain `UNKNOWN`.
* Editor: `CodeEditViewModel`, `CodeDiffViewModel`, `CodePlaygroundActivity`, bundled
  `highlight.min.js`, `prettier`, `spieglein/editor.bundle.js`; shipped `solvedContent`
  enables an offline `List.equals` validator (A11) [E10, E24].
* Native: 12 arm64-v8a `.so` libraries; M09 observed `loadLibrary("conscrypt_gmscore_jni")`.
  JNI internals remain `UNKNOWN` by explicit scope [E29, M06 14].
* Interaction states: `RunButton$State` 8 states, `InteractionKeyboardButtonState` 3 states,
  `CheckSolutionResult.Failure { error, exception }`, `IncorrectSolutionException`,
  `IncorrectCodeException`, `NoConnectionException`, `NullCodeException`,
  `AccessTokenUnavailableException` [E05, E10, E29].

## 4. Visual effects / third-party libraries

Deliberately out of scope where they do not affect the offline learning engine
(Rive animations, Lottie, confetti, typography). The only third-party pieces required
by the blueprint are an HTML renderer, an optional syntax highlighter and an optional
local code sandbox.
