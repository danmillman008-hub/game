# Mission 6 — Binary Analysis Status

## Scope
How far binary-level analysis of the APK and its native code went.

## Findings
1. **APK container**: fully enumerated (14,398 entries) — `00_BASELINE/02_FILE_INVENTORY.json`.
2. **DEX**: 12 files; class/method inventory built (29,454 classes, `06_CLASS_METHOD_INVENTORY.csv`);
   instruction-level constant scanning performed for host/watermark discovery.
3. **Resources**: `res/*` extracted (3,177 files); AXML decoded for the manifest; ARSC string pool read
   (33,341 values); **ARSC type tables (colours/dimens/styles) not decodable with this toolchain**.
4. **Native `.so`**: inventory only, no disassembly (no binary-analysis tool available).
5. **Signature**: `META-INF/YOUAREFINISHED.RSA` (942 B, sha256 `c93e9a58…`) proves third-party re-signing.

## Evidence labels
1–3, 5 **VERIFIED_STATIC**; 4 **BLOCKED** (tooling).

## Open questions
`Q-139` native symbol/section analysis (needs `readelf`/`objdump`).
