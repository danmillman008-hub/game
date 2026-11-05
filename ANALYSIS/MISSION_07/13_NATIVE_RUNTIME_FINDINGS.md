# MISSION 07 — 13 NATIVE / JNI RUNTIME FINDINGS

**Status:** `PARTIALLY VERIFIED` (environment) / `UNKNOWN` (JNI behaviour).
No native library was instrumented; nothing is claimed about JNI callbacks.

## Measured
* `ro.product.cpu.abilist=x86_64,arm64-v8a`,
  `ro.dalvik.vm.native.bridge=libndk_translation.so` (emulator ARM translation),
  app `primaryCpuAbi=arm64-v8a` (M05 `DEVICE_PROPERTIES.txt`).
* Frida server binary `frida-server-17.25.2-android-x86_64` ran as a native
  x86-64 ELF (`ELF shared object, 64-bit LSB x86-64, dynamic
  (/system/bin/linker64), for Android 21, built by NDK r29, stripped`) — proof
  that native code executes on this runner; it is a tool, not app code.
* `adb shell id` → `context=u:r:su:s0`, SELinux `Permissive` after
  `setenforce 0`; `/system/bin/strace` and `/system/bin/sqlite3` are present.
* App process had 125 threads at first launch (`ENV/POST_LAUNCH_PROCESS.txt`).
* `Java.enumerateLoadedClassesSync()` = 36,825 classes, 85 `com.getmimo.*`.
* M02/M06 native inventory established shipped `.so` libraries; M07 has not
  repeated that inventory.

## Not measured (`UNKNOWN`, not "unavailable")
`adb shell strace -p <pid>` / `am dumpheap` / JVMTI / Xposed-LSPosed / JNI
`RegisterNatives` or `Java_*` symbol tracing / `libndk_translation.so` hooking /
`dlopen` tracing / native crash tombstones. No JNI method was observed entering
or leaving a native frame in the Frida traces. The Frida traces are **Java/ART**
hooks; a native call made by an app `.so` would not appear unless a native hook
were installed.

## Why this matters
`09_OFFLINE_EXECUTION_RESULTS.md` classifies code-exercise execution as
`UNKNOWN` partly because the WebView/JS→native boundary is not traced. M05
found `lesson-webview.js` only relays gesture/ready/height/focus messages, so
any code evaluation must cross a boundary that M07 has not yet instrumented.
A future stage should hook `android.webkit.JavascriptInterface`-annotated
methods / `WebView.addJavascriptInterface` and `System.loadLibrary` before
claiming a local or remote execution path.
