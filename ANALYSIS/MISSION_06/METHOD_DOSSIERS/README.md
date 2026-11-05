# MISSION 06 — METHOD DOSSIERS

22 dossiers. Each gives the obfuscated signature, recovered semantic name, DEX file and
code offsets, constructor/field tables, verified implementation behaviour, real caller and
callee lists, output/state changes and an explicit **Remaining uncertainty** section.

| # | Dossier | Core claim |
|---|---|---|
| 01 | InteractiveLessonBaseViewModel | 33-method session state machine, `Y/V/X/U/H/e0/f0` |
| 02 | LessonProgressRepository | exact 11-column `createLessonProgress` |
| 03 | LessonProgressQueue | `AnswersInChapter` counting formula |
| 04 | LessonProgress.isSolvedCorrectly | **`tries >= 1`**, M05 correction |
| 05 | FillTheGap | ordered exact-string answer comparison |
| 06 | Selection | `list.all{ selected == isCorrect }` |
| 07 | Spell | letter-by-letter exact comparison |
| 08 | ValidatedInput | normalizer + 3-way Correct/Partial/Incorrect |
| 09 | WebViewLesson | `mimo.activity.*` client-side completion |
| 10 | ExecutableLessonViewModel | `solvedContent` `List.equals` check |
| 11 | DSL_LessonParser | `XmlPullParserFactory` dispatch |
| 12 | LessonInteractionTypeSelector | nine renderer types |
| 13 | AssetLoaders | exact locale asset paths |
| 14 | DefaultTracksRepository | `loadTrackWithChapters` |
| 15 | GetPathMapState | path-map state classes; exact unlock rule `UNKNOWN` |
| 16 | CompletionRepository | Room completion attachment |
| 17 | ChapterFinishedViewModel | offline fallback `handleOfflineState$1` |
| 18 | NetworkUtils | `hasTransport(WIFI|CELLULAR)` gate |
| 19 | CanOpenChapterWithKeys | keys gate |
| 20 | DataStoreUserPreferences | local preference state |
| 21 | LessonBundle_and_LessonContent | verified field tables |
| 22 | BaseFragment_and_NonInteractive | UI wiring / auto-advance |

Classification on every section. `SERVER CONFIRMED = 0`.
