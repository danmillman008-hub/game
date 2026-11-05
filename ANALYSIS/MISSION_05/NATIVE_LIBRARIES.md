# NATIVE_LIBRARIES — Mimo 9.35 `.so` inventory and evidenced responsibilities

`APK_COMPLETE_INVENTORY.json` lists **12** libraries: 6 for `arm64-v8a`,
6 for `armeabi-v7a`, **none** for x86/x86_64. Runtime proof from M04
(run `41998643355`) and M05 (run `42001925381`) shows four `arm64` libraries
loading with `: ok` on an `x86_64` emulator via `libndk_translation.so`.

| Library (arm64 size) | Purpose | Classification | Evidence |
|---|---|---|---|
| `librive-android.so` (5,687,760 B) | Rive vector animation runtime; `app.rive.*` (Artboard, StateMachine, RenderContext, CommandQueue, RiveSurface, ViewModelInstance) and `com.getmimo.ui.compose.animation.rive.*` | `VERIFIED_STATIC` for call sites / `VERIFIED_RUNTIME` not loaded in observed onboarding path | APK `.so`, DEX `app/rive/**` class list, JADX `RiveAnimationProperties`, `RiveFontAssetLoader` |
| `libsigner.so` (1,366,632 B) | **Adjust SDK native signer** — JNI exports `Java_com_adjust_sdk_sig_NativeLibHelper_nOnResume` and `…_nSign`; DEX has `com.adjust.sdk.sig.Signer`, `getSignerInstance`, `getApkContentsSigners` | `VERIFIED_STATIC` (JNI symbol + class) | `strings libsigner.so`, `classes.dex` strings |
| `libyrf.so` (473,464 B) | Native component referencing `bin/ghost/YRF`, `com/getmimo/ui/main/MainActivity`, `com/getmimo/core/model/inapp/Subscription$Type`, `java/net/HttpURLConnection`, `android/app/AlertDialog`, `nativeLibraryDir` | `VERIFIED_BOTH` for *presence & load*; purpose **`INFERRED`** (in-app/subscription integrity / anti-tamper helper) | M04+M05 logcat `nativeloader: Load …/lib/arm64/libyrf.so … : ok`; `strings libyrf.so`; DEX class refs |
| `libdatastore_shared_counter.so` (10,360 B) | androidx DataStore `NativeSharedCounter` — JNI exports `nativeCreateSharedCounter`, `nativeGetCounterValue`, `nativeIncrementAndGetCounterValue`, `nativeTruncateFile` | `VERIFIED_BOTH` | JNI symbol names + M04/M05 `nativeloader … libdatastore_shared_counter.so : ok` |
| `libandroidx.graphics.path.so` (10,096 B) | androidx Graphics Path `PathIterator` / `ConicConverter` (`internalPathIteratorNext`, `createInternalPathIterator`, `ro.build.version.sdk` gate) | `VERIFIED_STATIC` (JNI symbols) | `strings .so`; no load line in observed onboarding |
| `libc++_shared.so` (1,292,904 B) | shared C++ standard runtime required by the above | `VERIFIED_STATIC` | standard LLVM runtime, linked by the other five |

## Call sites — `VERIFIED_STATIC`

- `nativeloader` logcat lines from `41998643355` / `42001925381`:
  `libyrf.so` (caller `classes12.dex`), `libdatastore_shared_counter.so`
  (caller `classes2.dex`), `librive-android.so` (caller `base.apk`),
  `libsigner.so` (caller `base.apk`) — all `: ok`.
- `MimoLesson.postMessage` JS bridge is **not** a native library; it is a
  JavascriptInterface implemented in Java/Kotlin plus `assets/lesson-webview.js`.
  DEX literal `MimoLesson @2,875,416`.
- `r8-map-id` / `classes12.dex` (19,520 B) is the smallest DEX and is the
  caller of `libyrf.so` — consistent with a small native bridge stub.
- `spieglein/editor.bundle.js` (2,369,375 B) is a **JavaScript** code editor,
  not a `.so`; code rendering/execution for HTML/CSS/JS runs in a WebView.

## Explicitly `UNKNOWN` / not claimed

- Exact cryptographic behaviour inside `libyrf.so` / `libsigner.so`
  (no disassembly, no Ghidra re-analysis in M05; M01 Ghidra findings preserved).
- Whether `librive-android.so` is used on the onboarding screens observed
  (no load line captured on that path) — do not claim it renders onboarding.
- `armeabi-v7a` variants were never loaded (`ro.product.cpu.abilist32` empty).
- No claim that any library handles lesson scoring, answer evaluation or
  storage of curriculum — all evidence points to Kotlin/Java + Room/DataStore +
  WebView JS for those.

## Offline implication

All six libraries ship inside the APK and load without network. They are **not**
an offline blocker. `VERIFIED_RUNTIME` (M04) + `VERIFIED_STATIC`.

**Evidence:** `ANALYSIS/APK_COMPLETE_INVENTORY.json`, `ANALYSIS/RUNTIME/MISSION_04/ABI_COMPATIBILITY.txt`,
`ANALYSIS/RUNTIME/MISSION_05/LOGS/LOGCAT_MIMO.txt`, `SAMPLES/lesson-webview.js`.
