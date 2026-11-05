# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged) · **branch** `arena/aebb90b7-game` · `SERVER CONFIRMED = 0`  
Evidence: `EVIDENCE/DISASM/*.smali.txt`, `SCHEMAS/METHOD_CATALOG_MIMO.json`,
`CALL_GRAPHS/*.json`, `METHOD_DOSSIERS/*.md`. Classification on every finding.

---

## VERIFIED_STATIC — component names recovered
`SCHEMAS/OBFUSCATION_MAP.json` (173 entries). Key UI components:
| Semantic | Obfuscated | Votes |
|---|---|---|
| `MainActivity` | `ui/main/d;` | 35 (ViewModel) / `MainActivity` |
| `SplashViewModel` | `ui/a;` | 1 |
| `ChapterActivity` | `ui/chapter/ChapterActivity;` | 16 |
| `ChapterViewModel` | `ui/chapter/ChapterViewModel;` | 15 |
| `PathMapViewModel` | `ui/path/map/j;` | 15 |
| `PathMapFragment` | `ui/path/map/a;` | 1 |
| `ChapterFinishedViewModel` | `chapterendview/main/f;` | 13 |
| `ChapterFinishedFragment` | `chapterendview/main/e;` | 7 |
| `InteractiveLessonFragment` | `ui/lesson/interactive/c;` | 2 |
| `InteractiveLessonViewModel` | `ui/lesson/interactive/d;` | 4 |
| `InteractiveLessonBaseViewModel/Fragment` | `base/c;` / `base/b;` | 14 / 11 |
| `NonInteractiveLessonFragment` | `nointeraction/a;` | 1 |
| `InteractiveWebViewLessonFragment/ViewModel` | `webview/b;` / `webview/c;` | 1 / 1 |
| `ExecutableLessonViewModel` | `executable/q;` | 46 |
| `CodeEditViewModel` | `codeeditor/view/b;` | 7 |
| `SettingsFragment/ViewModel`, `ProfileFragment/ViewModel`, `PracticeTabFragment/ViewModel`, `SearchTrackFragment/ViewModel`, `StoreViewModel`, `AiTutorViewModel`, `LeaderboardFragment`, `HonestFreeTrialFragment/ViewModel`, `Paywall` screens | see map | |

## VERIFIED_RUNTIME (M04/M05, reused)
Launch `.ui.SplashActivity_default` → `.ui.onboarding.intro.IntroSlidesActivity`;
`com.getmimo`, `9.35`, `versionCode 1792759685`, `arm64-v8a`.
M05 run `42002808217`: first three offline UI hierarchies byte-identical to online.
`42003884423`: 24 taps to "Guess the letter" Q/R/D lesson.
`42005358012`: wrong answer → red "Try again", Q disabled/grey, `Continue` → code editor.
`42006697783`: offline track 274 "Automating Tasks with AI" lessons rendered.
`VERIFIED_BOTH` asset↔runtime matches MATCH-1..5 in M05
`EVIDENCE/RUNTIME_STATIC_MATCH.json`.

## VERIFIED_STATIC — navigation events
`base/c.e : LiveData<Integer>` = chapter/next-page index (`lessonBundle.b`);
`base/c.A : m0` posts `CodePlaygroundBundle` (`Ljm/h`) when `Q()` is true;
`ChapterActivity.G(ChapterBundle,Z)` / `J(cont)` use `key_skip_unlock_animation`;
`ChapterViewModel$StartupStage` enum = `CheckingUnlock`, `Unlocking`, …;
`PathMapViewModel.L refreshPathMapState`, `M init`, `N shouldStartChapterInHardMode`;
`Lxn/n0 ScrollToSection(sectionIndex=…)` Compose event.

## VERIFIED_STATIC — runtime behaviours
`base/c.Y()` prevents double-run with `f==TRUE`;
`a0()` lesson reset; `g0()` interaction delete;
`c0()`/`d0()` feedback visibility; `N()` keyboard state reset;
`D()` deletes per-lesson temp dir; `I()` cleanup after solve.
`RunButton$State.a/b` and `InteractionKeyboardButtonState.a/b/c` gate input.

## Android framework interactions — VERIFIED_STATIC
`androidx.lifecycle.m0/i0` LiveData `setValue`/`postValue` (`l`,`k`,`d`);
`kotlinx.coroutines` `ra0/z`, `Lkotlinx/coroutines/a.delay(300)`, Orbit MVI
`Lorg/orbitmvi/orbit/a.d`; `android.os.Handler(Looper.getMainLooper()).postDelayed`;
`AssetManager.open`; `ConnectivityManager`; `XmlPullParserFactory`; Jetpack Compose and
WorkManager.

## Remaining uncertainty
- Exact navigation graph (NavHost routes / fragment transactions) = `UNKNOWN`; only
  component names and LiveData events were decoded.
- Full layout XML / Compose hierarchy = `UNKNOWN` (M05 UI hierarchies cover observed screens).
- Process-recreation restoration = `UNKNOWN`.
