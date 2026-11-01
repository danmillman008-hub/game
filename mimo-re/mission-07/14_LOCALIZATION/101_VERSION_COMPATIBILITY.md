# Mission 7 — Version Compatibility

## Facts (VERIFIED_STATIC)
- `versionName 9.35`, `versionCode 1792759685`, compileSdk 37, minSdk 28, targetSdk 36.
- Content versioning: `publishSetVersion` + `trackVersion` (Phase 3.19).
- Progress rows store the content versions they were produced against.

## Compatibility rules recovered
| Change | Effect |
|---|---|
| content pack update | progress rows survive (version-agnostic key); no re-validation |
| lesson removed | existing row remains, orphaned |
| lesson id reused with new meaning | row would be inherited (no version check) — a real design risk |
| app update | Room schema has no migrations ⇒ destructive recreate ⇒ queued rows can be lost |
| OS/ABI | ARM-only native libs; no x86 support |

## Not available
Only one APK version exists in this workspace, so cross-version behavioural comparison is impossible
(explicit, per the brief).
