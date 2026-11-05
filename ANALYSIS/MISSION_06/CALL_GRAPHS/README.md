# MISSION 06 — REAL CALL GRAPHS

Nine `.mmd` diagrams + nine `.json` machine-readable graphs. Every edge is an actual
`invoke-*` xref extracted from the 12 original DEX files with Androguard 4.1.4 and the
**corrected** xref cache (78,560 targets / 105,012 caller edges). BFS from the listed root
methods, bounded depth and node count; bounds and roots are recorded in each `.json`.

| File | Root | Nodes | Edges |
|---|---|---|---|
| `01_answer_validation_core.json` | USER INPUT → RUN → CORRECT/INCORRECT → PROGRESS RECORD | 36 | 63 |
| `02_fillthegap_path.json` | fillTheGap: content module → state → run handler → validation | 17 | 17 |
| `03_selection_path.json` | selection: content module → state → run handler → km/f.b validator | 23 | 26 |
| `04_spell_path.json` | spell: content module → state → run handler → validation | 19 | 20 |
| `05_validatedinput_path.json` | validatedInput: typed text → normalizer → Correct/Partial/Incorrect → V/W/X | 34 | 80 |
| `06_content_pipeline.json` | APK assets → AssetManager → JSON → XmlPullParser DSL → LessonModule → renderer | 40 | 248 |
| `07_progress_persistence.json` | correct/incorrect → LessonProgress → local Room queue → sync attempt | 40 | 71 |
| `08_executable_lesson.json` | executableFiles → solvedContent comparison → progress / browser output | 12 | 10 |
| `09_progression_and_offline.json` | GetPathMapState / chapter completion / offline gate | 40 | 97 |

Node labels use only manually verified semantic method names; heuristic low-vote names from
`SCHEMAS/METHOD_NAME_MAP.json` are deliberately not displayed as fact. Each `.json` node also
carries DEX file, code offset and instruction count where available.
