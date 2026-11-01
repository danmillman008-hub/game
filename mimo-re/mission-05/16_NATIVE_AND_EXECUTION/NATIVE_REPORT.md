# Mission 5 — Native Library Report

## Scope
Every native (`*.so`) artifact in the APK: ABI coverage, size, machine type, linkage, exported JNI
surface, and vendor identification where the evidence supports it.

## Method
`readelf -h/-d`, `nm -D --defined-only`, `strings` over each library (binutils available in the
sandbox). JNI symbol names were mapped back to Java classes in the DEX. No disassembly was needed and
no library was executed.

## Sources
`/tmp/x/meta/lib/{arm64-v8a,armeabi-v7a}/*.so` (extracted from the APK under analysis).

## Findings — inventory (VERIFIED_STATIC)
| Library | arm64 bytes | armv7 bytes | Machine | Verdict |
|---|---|---|---|---|
| `librive-android.so` | 5,687,760 | 5,443,464 | AArch64 / ARM | **Rive** animation runtime (`Java_app_rive_core_*` JNI, links `libEGL`, `libGLESv3`, `libjnigraphics`, `libandroid`) |
| `libsigner.so` | 1,366,632 | 1,193,764 | AArch64 / ARM | **Adjust signature SDK** (`Java_com_adjust_sdk_sig_NativeLibHelper_nSign`, `nOnResume`) |
| `libc++_shared.so` | 1,292,904 | 872,872 | AArch64 / ARM | LLVM libc++ runtime required by the above |
| `libyrf.so` | 473,464 | 310,728 | AArch64 / ARM | JNI bridge for `bin.ghost.YRF` (see below) |
| `libdatastore_shared_counter.so` | 10,360 | 8,432 | AArch64 / ARM | AndroidX DataStore shared counter |
| `libandroidx.graphics.path.so` | 10,096 | 7,252 | AArch64 / ARM | AndroidX `graphics.path` |

Six libraries, two ABIs, no third ABI (no x86/x86_64). Total native payload ≈ 9.4 MB (arm64).

## Findings — `libyrf.so` ↔ `bin.ghost` (VERIFIED_STATIC structure, INFERRED_MEDIUM purpose)
`libyrf.so` exports only `JNI_OnLoad` plus static libc++ symbols; its Java side lives in
`bin/ghost/` — 19 classes in `classes12.dex` (`YRF`, `yrf` + 9 nested, `cup`, `cp`, `dw`, `gho`).
`bin.ghost.YRF` is a **blocking interstitial**: it extends `CountDownTimer`
(`AUTO_DISMISS_MILLIS = 10000`), holds a static `AlertDialog` with accept/exit text views and a
checkbox, and declares
```
public static native void execute(android.content.Context);
private static native int  dpToPx(android.content.Context, int);
private static native Drawable logo(android.content.Context);   // and logo2
public native void onClick(...); public native void onDismiss(...);
```
i.e. the decision to show it, its artwork and its dismissal policy live in native code. No plaintext
UI strings were found in either the class or the library.

**Assessment:** this is an out-of-band *enforcement surface* (integrity/kill-switch style dialog) that
the app can display to block or warn the user, driven entirely by `libyrf.so`. The exact trigger
conditions are **UNKNOWN** and were deliberately **not** probed (RULE 5: no bypass of integrity
checks). What is certain is that (a) the surface exists, (b) it is native-driven, (c) it is not part
of the lesson engine, and (d) no other component in the decompiled app references `bin.ghost`.

## Findings — code execution
Interactive lessons need no native helper. Executable lessons call the **remote** executor
(`POST /v1/code/runfiles` → `CodePlaygroundExecutionResponse`) — device-side code execution is not
performed by a bundled interpreter. No `libpython`, `libnode`, `libquickjs` or similar was found,
which supports a *remote-execution* model (**INFERRED_HIGH**).

## Evidence labels
- Inventory, sizes, machines, NEEDED, exported symbols, Java↔JNI mapping: **VERIFIED_STATIC**.
- Rive/Adjust identification: **VERIFIED_STATIC** (symbol names are vendor-owned).
- `bin.ghost` purpose: **INFERRED_MEDIUM** (structure verified, trigger unknown).
- Absence of an on-device interpreter: **INFERRED_HIGH** (negative evidence cannot be exhaustive).

## Limitations
No disassembly of native logic (`objdump -d` possible but out of scope for a specification mission);
symbols are stripped for `libyrf.so`, so its behaviour is opaque without deeper RE, which is not
justified for the deliverable.

## Unresolved
`U-18` trigger conditions for `bin.ghost.YRF`; `U-19` whether Adjust signature verification is
enforced at runtime by the app or only by the backend.

## Reproduction
```bash
cd /tmp/x/meta/lib/arm64-v8a
for f in *.so; do echo "== $f"; readelf -h "$f" | grep Machine; readelf -d "$f" | grep NEEDED; done
nm -D --defined-only libsigner.so | head        # Java_com_adjust_sdk_sig_NativeLibHelper_*
nm -D --defined-only librive-android.so | head  # Java_app_rive_core_*
nm -D --defined-only libyrf.so                   # JNI_OnLoad only -> logic is inside
strings -n 6 libyrf.so | grep -i 'ghost/YRF'     # Lbin/ghost/YRF;
```
