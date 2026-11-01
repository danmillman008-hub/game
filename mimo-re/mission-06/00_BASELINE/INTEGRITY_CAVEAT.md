# Integrity Caveat — read this before citing any finding

The analysed artifact is **not** a stock Mimo build.

| Fact | Value | Evidence |
|---|---|---|
| file | `/tmp/apk/Mimo_9.35 (1).apk` | `APK_MANIFEST.json` |
| size | 142,353,499 bytes | `APK_MANIFEST.json` |
| md5 | `f9cef2d8029e59da3668ec1c18e21566` | `APK_MANIFEST.json` |
| sha256 | `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` | `APK_MANIFEST.json` |
| signature | `META-INF/YOUAREFINISHED.RSA` + `.SF` (942 B, sha256 `c93e9a58…`) — **third-party re-signature** | zip listing |
| mod watermark | `Smob - Mod obfuscation tool v4.6 by Kirlif'` in **11,543** constant strings | DEX constant scan |
| injected application class | `com.getmimo.App extends bin.ghost.yrf` (+ `libyrf.so`) | decompiled `App` |
| ABIs | arm64-v8a, armeabi-v7a (no x86) | `lib/` listing |

## What this means for mission 6
- Every statement about **content, DSL/parser, lesson runtime, grading, progress, networking, AI tutor,
  gamification, navigation and business surface** is derived from Mimo's own code and is therefore
  representative of Mimo 9.35 — but strictly it describes *this artifact*.
- Every statement about **code integrity, tamper detection, injections or "mod" behaviour** is void as a
  Mimo claim. `bin.ghost`/`libyrf.so` are treated as **foreign** (`U-18`, `BLOCKED` as a Mimo question).
- No runtime claim can be made at all (`15_RUNTIME/97_RUNTIME_RESULTS.md`).

## Rule applied
RULE 4: a static finding is never upgraded to runtime; a client declaration is never upgraded to backend
behaviour. This file is the single place where the artifact-level caveat is stated; other documents
reference it instead of restating it.
