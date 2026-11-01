# Mission 6 — Content Delivery and Caching

## Scope
How content reaches the device: what is bundled, what is downloaded, what is cached, and what happens
when it is unavailable.

## Method
Asset census; API catalogue review for content endpoints; Room schema review; manifest dynamic-module
meta-data; repository class names/reads.

## Sources
`01_APK_AND_ARCHITECTURE/01_APK_STRUCTURE.md`, `evidence/API_CATALOG_V2.csv` (mission-05), Phase 6 docs.

## Findings
1. **Bundled** (VERIFIED_STATIC): `assets/lessons-en/tracks/` — 10,327 JSON documents, the English
   interactive corpus. Bundled code languages, fonts, 59 Rive animations.
2. **Downloaded as dynamic feature modules** (INFERRED_HIGH): `com.android.dynamic.apk.fused.modules`
   lists `content_de, content_es, content_fr, content_id, content_it, …`. This is Play Feature/Asset
   Delivery, so non-English content arrives through Play, not through the app's HTTP API.
3. **Downloaded over HTTP** (VERIFIED_STATIC): `GET /v1/package/preview` returns `application/zip`
   (`okhttp3.ResponseBody`) — content previews/packs are zip archives; `GET /v1/tracks/.../completion`,
   `/v1/tracks/{id}/eta`, `/v1/tutorials/...` deliver structural data.
4. **Cached**: **not in Room.** The Room database has exactly three tables (progress-related) and none
   for content. Content JSON is therefore read from assets (and, for dynamic modules, from the module's
   own assets) with in-memory/`Flow` reuse; there is no persisted content cache in this build.
   (VERIFIED_STATIC for the schema; "no disk cache at all" is INFERRED_HIGH — an OkHttp disk cache would
   not appear in Room.)
5. **Unavailable content**: the offline guard (`hg.e`) throws `NoConnectionException` for any HTTP
   attempt while offline; the app therefore still renders bundled lessons offline but cannot refresh
   structure or download packs. Labelled **VERIFIED_STATIC** for the guard, **INFERRED** for the UX
   consequence (no runtime observation).

## Evidence labels
Bundled corpus, zip endpoint, three-table DB, offline guard: **VERIFIED_STATIC**. Dynamic-module content
delivery: **INFERRED_HIGH**.

## Limitations
The OkHttp client in `ae.m` case 20 is built **without a `Cache`** in the decompiled constructor call
(no `cache(...)` invocation visible) — but DAD may have dropped it. `Q-19`.

## Open questions
`Q-19` HTTP disk cache presence; `Q-05` dynamic module contents; `Q-20` how `publishSetVersion` mismatch
is surfaced to the user.

## Reproduction
```bash
ls /tmp/x/assets/lessons-en/tracks | wc -l
grep -o 'content_[a-z]*' /tmp/manifest.xml | sort -u
grep -n 'package/preview' mimo-re/mission-05/evidence/API_CATALOG_V2.csv
```
