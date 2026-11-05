# MISSION 07 — LIVE RUNTIME RECONSTRUCTION AND OFFLINE STATE FORENSICS

**Baseline:** `cfc8ea41` (MISSION 06 FINAL) · **branch** `arena/aebb90b7-game`
**Original APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`
(142,353,499 B, unchanged).
Prior M01–M06 evidence is preserved verbatim. `SERVER CONFIRMED = 0`.

## Environment assessment (initial, before first run)
Local sandbox (`/home/user/game`): **no** `adb`, `emulator`, `java`, `javac`,
`qemu-system-x86_64`, `frida`, `frida-server`, `gdb`, `lldb`, `sqlite3`, `apktool`,
`baksmali`, `dexdump`, `aapt`, `jadx`, `radare2`, `strace`, `ltrace`, `run-as`,
`docker`, `podman`. `/dev/kvm` **absent**; `/proc/cpuinfo` has **no** `vmx`/`svm`.
`uname`: Linux 6.1.158+ x86_64. `su` exists as the Unix utility (not Android su).
Conclusion: **a local emulator cannot boot here**. Available local tools:
Python 3 (Androguard 4.1.4 venv from M06), `readelf`/`objdump`/`nm`, `node`, `git`,
`gh`, Google Drive connector.

**Actual runtime environment** is the project's GitHub Actions job
`mimo-runtime-verification.yml` (pinned `reactivecircus/android-emulator-runner`
v2.35.0). M05 run `42006697783` proved: Android 16 / API 36,
`sdk_gphone64_x86_64`, fingerprint `.../userdebug/dev-keys`,
`ro.product.cpu.abilist=x86_64,arm64-v8a`,
`ro.dalvik.vm.native.bridge=libndk_translation.so`, original APK installed
`Success`, `com.getmimo` version 9.35, `primaryCpuAbi=arm64-v8a`.
`userdebug/dev-keys` is the concrete indication that `adb root` may work.

## Techniques to be *measured*, not assumed
`adb root` · `adb shell id` · `run-as` · `su` · SELinux `setenforce` ·
Frida 17.25.2 `frida-server-android-x86_64` + Python `frida`/`frida-tools` ·
`Java.use`/`Java.perform` dynamic hooking of recovered DEX methods ·
direct runtime invocation of pure/static validators with controlled inputs ·
`adb pull` of `/data/data/com.getmimo/{databases,shared_prefs,files,datastore}` ·
SQLite WAL/SHM + `sqlite_master` + row-level diffs via Python `sqlite3` ·
`dumpsys`/`logcat`/`uiautomator`/`screencap` · `am`/`cmd` · process/thread
inspection · instrumented-APK test copies (only if needed; original stays unchanged).
Xposed/LSPosed/JVMTI/JNI tracing are recorded as **candidates** whose
availability is assessed from the measured device state.

## Unresolved runtime hypotheses carried over from M06
Q-1 correct-answer runtime UI · Q-2 persisted `lesson_progress` row after answer ·
Q-5 exact unlock condition · Q-7 `W()` partial-match feedback · Q-8 `d0()` booleans ·
Q-9 `SingleChoice`/`MultipleChoice`/`Reveal` dispatch · Q-12 loader selection ·
Q-16 `q.I()` applicability · Q-19 offline exception UI · Q-23 force-stop restore ·
Q-24 Room migrations · Q-25 offline external-URL substitution.
All require *live* evidence; M06 explicitly left them `UNKNOWN`.

## Stage plan (short, concrete, each resets the AVD)
| Stage | Hypothesis | Deterministic experiment |
|---|---|---|
| 1 | Root + Frida + private DB are reachable; recovered validators behave at runtime as M06 bytecode says | fresh AVD, install APK, `adb root`, push `frida-server`, attach, **directly invoke** `qm.i.a`, `km.f.b`, `LessonProgress.isSolvedCorrectly`, `network.a.a/b`, `te.c.b`, `gm.h.a` with controlled inputs; capture DB schema before/after one exact tap |
| 2 | A real correct answer executes `onLessonRun$1 → V() → H() → createLessonProgress` and mutates Room | replay deterministic M05 run-003 chain (24 recorded taps) with Frida hooks live; tap **D** (correct) and **Q** (wrong) in separate controlled states; DB snapshots C/D/E/F, UI hierarchy, logcat |
| 3 | Offline cold start + force-stop restore uses local `lesson_progress`/DataStore | disable network (`cmd connectivity` + verify no active default network), force-stop, restart, compare DB rows and path-map state |
| 4 | Unlock condition and chapter-end state are client-computable | seed controlled local DB/DataStore states, observe path-map UI + `GetPathMapState` hook values |
| 5 | Code exercise execution boundary | open executable lesson, edit file, observe `q.I()` and WebView/JS message path |

## Evidence classification
`VERIFIED_RUNTIME` (measured on emulator) · `VERIFIED_STATIC` (M06 bytecode) ·
`VERIFIED_BOTH` · `INFERRED` · `UNKNOWN`. No server reconstruction.
