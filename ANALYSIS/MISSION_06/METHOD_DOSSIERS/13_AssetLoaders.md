# Asset loaders + locale selection + DefaultTrackLoader

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/AssetTracksLoader.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC — exact asset paths
`Lye/b;` fields: `a:Landroid/content/res/AssetManager;`, `b:Lke/a;` (locale provider),
`c:Ljava/util/LinkedHashMap;` (static).

`<clinit>` (97 insns):
```
ContentLocale.values().associate { it -> "lessons-" + it.getLanguageString() }
  → then { locale -> "lessons-<lang>/tracks" }
```
`ContentLocale` enum (`<clinit>` @9681384, 141 insns) = `RU(ru), EN(en), ES(es), PT(pt),
DE(de), FR(fr), IT(it), ID(id), TR(tr), PL(pl)` — 10 locales, matching M05's 10,298 files.

| Method | Path built | Action |
|---|---|---|
| `b(J)` | `"lessons-<lang>/tracks/tutorial-<id>.json"` | `AssetManager.open(path)` |
| `d()` | `"lessons-<lang>/tracks/tracks.json"` | `AssetManager.open(path)` |
| `c()` | `"file:///android_asset/lessons-common/icons"` | image base URL |
| `a(Tutorial)` | — | filters GuidedProject chapters/lessons by `CodeLanguage` and `LessonContentType.EXECUTABLE_FILES` |

`Lye/d;` is a second loader reading from `context.getFilesDir().getAbsolutePath()` (downloaded
/ updated content variant); its `b(J)`/`d()` use the same `tutorial-<id>.json` / `tracks.json`
names.

`Lcom/getmimo/data/content/tracks/b;` = `DefaultTrackLoader` (4 inner-class votes):
- `a(J,I,I) : kotlinx.serialization.json.JsonObject` — reads a stream, `Json.decodeFromString`,
  applies version/offset selectors;
- `b(J,cont)` launches `DefaultTrackLoader$getTutorial$2`;
- `c(InputStream) : String` — `InputStreamReader(UTF-8)` → `BufferedReader` → `readText()`;
- `d(String) : String` — rewrites image references (`"/"` substitution via `Ls7/a.n`).
Inner class `DefaultTrackLoader$getExecutableLesson$2` contains the string
`"executableContent"`.

## Remaining uncertainty
- Which loader (`Lye/b` assets vs `Lye/d` filesDir) wins at runtime, and the update/download
  trigger = `UNKNOWN`; selection is a DI binding not decoded here.
- `Lye/b.a(Tutorial)` full filter predicate = `INFERRED`.
