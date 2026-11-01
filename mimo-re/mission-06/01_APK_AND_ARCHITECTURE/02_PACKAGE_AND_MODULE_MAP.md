# Mission 6 — Package and Module Map

## Scope
The real package structure of the app (as built), which packages are app code vs bundled libraries, and
where the obfuscated app-specific code lives.

## Method
Class inventory over all 12 DEX (29,454 classes) grouped by top-level package and by
`com.getmimo.*` sub-package; cross-referenced with recovered source (3,283 classes).

## Sources
`01_APK_AND_ARCHITECTURE/06_CLASS_METHOD_INVENTORY.csv`, `evidence/DI_GRAPH.json`.

## Findings
**Top-level:** `com` 12,171 · `androidx` 1,696 · `app` 983 · `kotlin` 741 · `io` 512 · `okhttp3` 428 ·
`org` 369 · `b1` 236 (plus ~1,210 smaller single-letter/obfuscated packages).

**`com.getmimo.*` (app code)** — 3,133 classes were recovered as source; the sub-package layout is the
product architecture and is not obfuscated at the package level:

| Package | Role (evidence) |
|---|---|
| `com.getmimo.ui.lesson.interactive.*` | lesson fragments + view models; `base.c` is the shared state machine |
| `com.getmimo.data.content.lessonparser.interactive.model` | AST models (41 classes) |
| `com.getmimo.data.content.model.track` | content DTOs (`LessonContent$Interactive`, `CodeLanguage`) |
| `com.getmimo.data.source.remote.*` | Retrofit repositories (`progress`, `authentication`, `iap`, `livepreview`, `certificates`) |
| `com.getmimo.data.source.local.aitutor` | AI tutor repository + prompt types |
| `com.getmimo.data.source.local.room` | Room database |
| `com.getmimo.data.model.*` | wire DTOs (progress, keys, coins, leaderboard, store, aitutor, …) |
| `com.getmimo.analytics.*` | analytics facade + 305 property classes |
| `com.getmimo.ui.widget` | Glance streak widgets (small/medium/large receivers) |
| `com.getmimo.network` | connectivity guard + monitor |
| `com.getmimo.interactors.*` | path/progress interactors |

**App code that is *not* in `com.getmimo`** — this is the structural lesson of mission 5, now mapped:
| Package | Role | Confidence |
|---|---|---|
| `te.*` | the interactive-lesson XML parser (7 classes) | VERIFIED_STATIC |
| `qm.*` | validated-input view model + verdict types + normaliser | VERIFIED_STATIC |
| `cg.*` | Room generated statements | VERIFIED_STATIC |
| `ae.m` | Dagger/Hilt component factory (127 provider cases) | VERIFIED_STATIC |
| `ku.*` | session/token store + misc holders | INFERRED |
| `fh.*`, `hg.*` | OkHttp interceptors (auth, device header, offline guard) | VERIFIED_STATIC |
| `pg.*` | code-execution WebSocket listener | VERIFIED_STATIC |
| `np.*`, `be.*`, `oy.*` | analytics/attribution handles (`np.h` = dispatch, not recovered) | INFERRED/NOT_RECOVERED |
| `ie0.*` | obfuscated Retrofit annotations (verbs, `@Headers`, auth marker) | VERIFIED_STATIC (types) |
| `bin.ghost.*` | injected protection layer (`yrf` base app, `YRF` dialog) | INFERRED_HIGH |

**Bundled ecosystems:** Facebook (`com.facebook.*`), Google Ads/Play services (983 classes under
`app`), Gist/Customer.io (`io.customer.*`), Rive (`app.rive.*`), Adjust, RevenueCat, Mixpanel,
Firebase, WorkManager, Hilt, Room, Retrofit/OkHttp, Compose (+ `b1`/`a1`/`x1` Compose runtime
packages), Glance.

## Evidence labels
Package counts and membership: **VERIFIED_STATIC**. Role mapping: **VERIFIED_STATIC** where a class was
read; **INFERRED** for `ku.*`, `np.*`, `be.*`, `oy.*`.

## Limitations
Package names are *not* a safe guide to ownership — `te`/`qm`/`cg` prove that. The map therefore mixes
two evidence bases (package census + class reads) and each row says which.

## Open questions
`Q-06` identity of the four analytics handles; `Q-07` whether `b1`/`a1`/`x1` are re-obfuscated Compose
or a fork.

## Reproduction
`python3 -c "import csv,collections;r=list(csv.DictReader(open('01_APK_AND_ARCHITECTURE/06_CLASS_METHOD_INVENTORY.csv')));print(collections.Counter(x['top_package'] for x in r).most_common(10))"`
