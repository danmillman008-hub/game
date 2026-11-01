# Mission 6 — APK Structure

## Scope
What is physically inside the archive: code, resources, assets, native libraries, fonts, animations,
embedded data packs, and the security-relevant manifest surface.

## Method
`zipfile` entry census; androguard `AXMLPrinter` for `AndroidManifest.xml`; `ARSCParser` for
`resources.arsc`; `readelf`/`nm` for libraries; file-type census over `res/` and `assets/`.

## Sources
`00_BASELINE/APK_MANIFEST.json`, `evidence/RESOURCES.json`, `00_BASELINE/SOURCE_INVENTORY.json`.

## Findings
**Top-level distribution (14,398 entries):** `assets/` 10,564 · `res/` 3,177 · `org/` 489 ·
`META-INF/` 65 · `google/` 63 · `lib/` 12 · `kotlin/` 8 · `firebase/` 4 · `developers/` 1 · `logs/` 1 ·
13 root entries (manifest, arsc, 12 dex).

**Code:** 12 DEX files. `classes.dex` (16.2 MB) and `classes2.dex` (9.8 MB) and `classes3.dex` (2.8 MB)
carry the code; `classes4…12.dex` are 1,096-byte stubs except `classes12.dex` (19,520 bytes, which
holds the entire `bin.ghost` package — 19 classes). Total classes 29,454 across 1,220 packages.

**Resources:** 2,861 XML, 117 PNG, 113 WebP, **59 `.riv`** (Rive animation), 10 OTF, 9 JSON, 3 MP3,
2 TTF, 1 JPG, 1 binarypb. Resource table: 33,341 strings, one package (`com.getmimo`).

**Assets:** 10,564 files; the lesson corpus dominates (`assets/lessons-en/tracks/`, 10,327 JSON
documents). Further locale/feature packs are delivered as **Play dynamic feature modules** — the
manifest's fused-module meta-data lists `content_de, content_es, content_fr, content_id, content_it, …`.

**Native:** 6 libraries × 2 ABIs (arm64-v8a, armeabi-v7a): `librive-android.so` (5.69 MB),
`libsigner.so` (1.37 MB, Adjust), `libc++_shared.so`, `libyrf.so` (0.47 MB), 
`libdatastore_shared_counter.so`, `libandroidx.graphics.path.so`. No x86/x86_64 payload.

**Manifest surface (decoded, see also `15_SECURITY/94_*`)**
- `com.getmimo.App` is the Application class and **extends `bin.ghost.yrf`**.
- 61 activities, 6 `SplashActivity` aliases (`_default`, `_ninja`, `_ukraine`, `_chemist`, `_bat`, `_proud` — seasonal splash art), 19 services, 20 receivers, 8 providers.
- Deep links: `https://getmimo.com` (12 filters on `MainActivity`), custom scheme `mimo://getmimo.com`,
  plus regex-style patterns (`https://getmimo.com/learn/[0-9]+/courses/[0-9]+/chapters/[0-9]+(/lessons/[0-9]+)?`).
- 24 permissions incl. `CAMERA`, `RECORD_AUDIO`, `POST_NOTIFICATIONS`, `USE_BIOMETRIC`,
  `com.android.vending.BILLING`, Play `AD_ID`, and four `ACCESS_ADSERVICES_*`.
- `allowBackup="false"`, `requestLegacyExternalStorage="true"`, `supportsRtl="false"`.
- Embedded SDKs visible in meta-data: Play Billing **9.1.0**, Firebase (Crashlytics **disabled**),
  Facebook SDK, Mixpanel, AdMob, Gist (Customer.io), Adjust, RevenueCat.

## Evidence labels
Counts, names and manifest attributes: **VERIFIED_STATIC**. "Dynamic feature modules carry the locale
content packs": **INFERRED_HIGH** (fused-module meta-data + absence of non-English lesson trees in
`assets/`).

## Limitations
Resource *values* were read, but per-screen resource usage cannot be attributed without layout
inflation. `.riv` animation contents were not decoded (no Rive tooling).

## Open questions
`Q-04` which `.riv` files belong to which screens; `Q-05` the exact dynamic-module names and whether
content packs contain DSL or pre-rendered data.

## Reproduction
```bash
/tmp/venv/bin/python tools/build_baseline.py
/tmp/venv/bin/python tools/extract_resources.py --out evidence/RESOURCES.json
find /tmp/res/res -type f | sed 's/.*\.//' | sort | uniq -c | sort -rn
```
