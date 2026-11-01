# MISSION 5 — Complete Mimo Reverse Engineering (report)

**Target:** `com.getmimo` 9.35 (versionCode 1792759685) · minSdk 28 · targetSdk 36
**APK:** md5 `f9cef2d8029e59da3668ec1c18e21566` · sha256 `48ce1740…1e0f7c7a`
**Branch:** `arena/ecb8af07-game` · **starting commit:** `9dbc278f07bd085f3da00e6012c7c412be358bf0`

## Scope
Deepen the reverse engineering of Mimo from the existing artifacts, re-validate historical claims
before relying on them, and close the domains that were previously guesses: content DSL, lesson
runtime, assessment, progress, API contracts, local persistence, AI tutor, analytics, native
components. Specification only — no clone, no app, no binary mutation.

## Method
1. **Revalidate before reuse.** Mission-04's annotation dump and API catalogue were treated as
   *claims*, not data. Both failed revalidation and were regenerated.
2. **Locate by evidence, not by name.** The lesson parser was found by instruction-level xref on the
   `Tag` enum, not by grepping for "parser" — which is why it was missed four missions running.
3. **Batch decompile outside the repo.** 3,323 classes were decompiled with androguard DAD into
   `/tmp/dad`; only derived inventories are committed (RULE 6).
4. **Cross-check every load-bearing reading** against string literals, method descriptors, annotations
   or a second call site, because DAD emits pseudo-Java.
5. **Label everything** with the mission's nine-label set; static and runtime confidence kept apart.

## Sources
See `01_TOOLCHAIN_AND_ENVIRONMENT/TOOLCHAIN_AND_REPRODUCIBILITY.md` for tool versions and per-dex
SHA-256; `evidence/DECOMPILE_MANIFEST_*.json` for each decompilation run; `evidence/*.csv|json` for the
machine-readable data behind every figure below.

## Findings — what is now known

### 1. The content format is HTML-shaped XML with 29 tags
The `Tag` enum has **29 constants in ordinals 0–28** (`HTML, BODY, PARAGRAPH, EM, CODE, SELECTION,
IMAGE, WEBVIEW, TABLE, TABLES, ROW, HEADER, DATA, DATABASE, STRONG, SPAN, CONTENT, TEXT, INTERACTIONS,
INTERACTION, OPTIONS, OPTION, ITEM, NUMBER, BREAK, OUTPUT, COLLAPSIBLE_LINES, COLLAPSIBLE_LINE, A`).
`<code>` is the interactive unit; it carries `content`, an `interactions` block, an optional `output`
(console **or** table) and `collapsibleLines`. `visible-if` ∈ {`always`,`correct`,`wrong`} maps to a
three-value enum used for feedback selection. Full grammar + JSON-Schema AST:
`04_CONTENT_AND_DSL/`.

### 2. The parser lives outside `com.getmimo`
`te.a`–`te.g`. This is the single most consequential structural correction of the mission: the first
decompilation pass used `--filter 'Lcom/getmimo'` and therefore could not see them. `ku.a`, previously
suspected, is a generic utility holder and is **not** a parser.

### 3. Grading is exact-or-normalised, with real partial credit
Validated input:
`normalize(s) = lowercase(US)` then **keep only letters, digits, `<` and `.`**. Exact equality → correct;
normalised-only equality → *correct-with-correction* (the app overwrites the learner's text and records
a success); otherwise incorrect. Verdicts are dispatched through a **closed** three-way sealed type and
applied after a deliberate **300 ms** delay. Option-bearing types grade purely on an authored flag.

### 4. `tries` is not a counter — it is a 0/1 flag
`LessonProgress.isSolvedCorrectly() { return tries >= 1; }`; `attempts` is the counter; first-try is
`attempts == 1 && solved`. This corrects a four-mission-old error.

### 5. The local store is a transmit buffer, not an archive
Three tables (`lesson_progress`, `chapter_completions`, `tutorial_completions`), no migrations
registered at all, and rows are **deleted after the server acknowledges them**.

### 6. The API surface is 62 endpoints with recoverable DTOs
`GET 28 · POST 24 · PATCH 4 · DELETE 4 · PUT 2`; **85 parameter bindings** (45 path, 20 body, 17 query,
3 header); **34 distinct response types** recovered from Kotlin continuation generics — previously
UNKNOWN. Verbs were constrained by Retrofit's own rules and produce **zero** violations. No API host is
hard-coded anywhere in the decompiled app.

### 7. Native payload identified
`librive-android.so` (Rive), `libsigner.so` (Adjust signature), `libc++_shared.so`,
`libdatastore_shared_counter.so`, `libandroidx.graphics.path.so`, and `libyrf.so` — a native bridge for
an obfuscated `bin.ghost` package (19 classes) that drives a blocking 10-second auto-dismiss dialog via
`native execute(Context)`. Its trigger conditions are unknown and were deliberately not probed.

## Findings — corrections to earlier claims
| Earlier claim | Corrected claim | Reason | Evidence | Affected artifacts |
|---|---|---|---|---|
| The interactive parser is in `com.getmimo.data.content.lessonparser` | The parser is obfuscated `te.a`–`te.g`; the `lessonparser` package holds only **models** | xref on `Tag` shows 35 refs, all from `te/*` | `find_refs.py` output, `te.a` read | mission-03/04 DSL docs |
| `ku.a` is the parser | `ku.a` is a generic obfuscated utility holder (dialog URI builder, RevenueCat callback, builder) | full class read | `/tmp/dad/ku.a.java` | mission-04 note |
| `option.c/.d` are gap bounds | they are **style-span bounds**; the slot is `[prevEnd, c)` | render site uses `SpannableStringBuilder(source, c, d)` | `fillthegap.a` | mission-04 DSL/AST docs |
| Grading compares raw strings | grading normalises (case + punctuation-insensitive) and has a partial-match outcome | normaliser body read | `qm.i.a`, fragment lambda | mission-04 assessment claims |
| `tries` counts restarts, `attempts` counts checks | `tries` is a 0/1 correctness flag | `isSolvedCorrectly()` body | `LessonProgress:284` | mission-04 progress model |
| Parameter annotations: 162 rows | 105 valid rows; the 162 were a parser defect | wrong item type fed to the annotation-set reader | `ANNOTATIONS_V2.csv` | mission-04 `annotations.json.gz` |
| API verbs are LOW confidence | GET/DELETE/POST INFERRED_HIGH (0 Retrofit rule violations), PATCH/PUT INFERRED_MEDIUM | body-presence constraints + same-path pairing | `API_CATALOG_V2.csv` | mission-04 API catalogue |
| Response types unknown | 34 distinct response DTOs recovered from continuation generics | `Ld70/b<-T;>` in method `Signature` | `DTO_CATALOG.csv` | mission-04 API catalogue |
| "305 analytics events"; "137 Segment / 62 Mixpanel / 315 Adjust …" | those are **class counts per package**, not events; only Firebase and Adjust are named SDKs, four handles are unidentified | package census + facade read | `ANALYTICS_REGISTRY.md` | mission-04 analytics section |

## Evidence labels
Per-document labels are stated inside each report. Aggregate: **VERIFIED_STATIC** for every structural
finding above; **INFERRED_HIGH** for verb assignment (GET/DELETE/POST), server-side quota and
transmit-buffer intent; **INFERRED_MEDIUM** for PATCH/PUT and the `bin.ghost` purpose;
**VERIFIED_RUNTIME: none**; **BLOCKED** for everything requiring execution.

## Limitations
- No device, emulator or adb → **zero runtime evidence**; every behavioural statement is static.
- No JDK → no smali, no `aapt2`, no resource decoding; UI strings/themes are out of reach.
- DAD's pseudo-Java omits modifiers and reuses locals; claims were cross-checked but a smali pass would
  raise confidence (U-04).
- 26 open items in `evidence/UNRESOLVED_REGISTER.csv`, of which 5 are environment-blocked and 4 need an
  authorised account.

## Unresolved
See `evidence/UNRESOLVED_REGISTER.csv`. Highest-value: `U-01` (finish `te.b`–`te.g`), `U-20`
(authoritative analytics events), `U-22` (API base URL), `U-23` (PATCH vs PUT).

## Reproduction
```bash
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install androguard==4.1.4 pytest
/tmp/venv/bin/python tools/decompile_apk.py --dex-dir /tmp/x --out /tmp/dad --filter 'Lcom/getmimo' \
  --inventory evidence/CLASS_INVENTORY_APP.csv --manifest evidence/DECOMPILE_MANIFEST_APP.json
/tmp/venv/bin/python tools/extract_annotations_v2.py --dex-dir /tmp/x \
  --csv evidence/ANNOTATIONS_V2.csv.gz.gz --json evidence/ANNOTATIONS_V2.json
/tmp/venv/bin/python tools/build_api_catalog_v2.py --annotations evidence/ANNOTATIONS_V2.csv \
  --csv evidence/API_CATALOG_V2.csv --json evidence/API_CATALOG_V2.json
/tmp/venv/bin/python tools/build_dto_catalog.py
python -m pytest 21_AUTOMATED_VALIDATION -q      # 44 passed
```
