# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged) · `SERVER CONFIRMED = 0` · classification on every finding.

---

## VERIFIED_STATIC (M05 inventory reused; M06 DEX cross-check)
12 `.so` libraries, `arm64-v8a`, from original APK:
`libsigner.so`, `libdatastore_shared_counter.so`, `libyrf.so`, `librive-android.so`,
`libandroidx.graphics.path.so`, `libc++_shared.so`, `libimage_processing_util_jni.so`,
`libbugsnag-ndk.so`, `libbugsnag-plugin-android-anr.so`, `libsqlcipher.so`,
`libbarhopper_v3.so`, `libmlkit_google_ocr_pipeline.so`.
M04 run `41998643355` verified native loads `: ok` (`VERIFIED_RUNTIME`).

## M06 DEX cross-check — VERIFIED_STATIC
`EVIDENCE/DEX_STRING_INDEX.txt` scan of **method string constants** found `System.loadLibrary`
only in Rive-related code (`app.rive.runtime.kotlin`). No other `loadLibrary` string appeared
in method constant pools. **This is NOT proof of absence**: libraries may be loaded by
`System.load` from an absolute path, by `native` method resolution from a static initializer
whose string lives in the class string pool, or by a third-party SDK. M05's `12 .so` doc
records the shipped files; M06 does not contradict it.

## JNI boundary — what is and is not reconstructed
| Library | Role (`VERIFIED_STATIC` name + `INFERRED` purpose) | Reconstructed? |
|---|---|---|
| `libsigner.so` | request signing / attestation (`INFERRED`) | **No** — native code, network protocol, auth bypass explicitly out of scope |
| `libdatastore_shared_counter.so` | DataStore cross-process counter (`INFERRED`) | **No** |
| `libyrf.so` | third-party SDK (`UNKNOWN`) | **No** |
| `librive-android.so` | Rive animation runtime | **No** |
| `libsqlcipher.so` | encrypted SQLite (`INFERRED`) | **No** — Room SQL strings are plain DEX constants |
| `libbugsnag*` | crash/ANR reporting | **No** |
| `libimage_processing_util_jni.so`, `libbarhopper_v3.so`, `libmlkit_google_ocr_pipeline.so` | CameraX / ML Kit | **No** |

## Explicit boundary
M06 did **not** disassemble native ARM64 code, did not reconstruct JNI method tables,
did not reconstruct any network protocol/signature algorithm, did not bypass TLS/certificate
pinning, and did not perform any auth/purchase/credential work. `SERVER CONFIRMED = 0`.
`EVIDENCE/DEX_STRING_INDEX.txt` contains the exact scan output for audit.

## Remaining uncertainty
- Exact `System.loadLibrary` call sites for the 12 libraries = `UNKNOWN` (string-pool scan
  limitation described above).
- Native ↔ Kotlin API surface = `UNKNOWN`.
