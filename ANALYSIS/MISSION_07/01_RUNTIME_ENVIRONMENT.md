# MISSION 07 — 01 RUNTIME ENVIRONMENT

**Status:** `VERIFIED_RUNTIME` for every measurement below; `UNKNOWN` where a
technique was not exercised. Original APK unchanged:
`48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`
(142,353,499 B). `SERVER CONFIRMED = 0` — no server was contacted or
reconstructed; the only network traffic observed was app/SDK analytics emitted
by the ORIGINAL app on the emulator.

## 1. Local sandbox (`/home/user/game`) — cannot host an emulator
Measured (`bash` inventory, M07 initial assessment): **absent** `adb`,
`emulator`, `java`, `javac`, `qemu-system-x86_64`, `fastboot`, Frida tools,
`gdb`, `lldb`, `sqlite3` CLI, `apktool`, `baksmali`, `dexdump`, `aapt`,
`aapt2`, `jadx`, `radare2`, `strace`, `ltrace`, `run-as`, `docker`, `podman`.
`/dev/kvm` absent; `/proc/cpuinfo` has no `vmx`/`svm`.
Present: Python 3, `node`, `npm`, `git`, `gh`, `readelf`/`objdump`/`nm`, `su`
(the Unix utility), and the M06 Androguard 4.1.4 venv at
`/home/user/_work/m06/venv`. Conclusion: **runtime work executes on the
project's GitHub Actions emulator runner, not locally.**

## 2. Runner / device (measured, run `42017453045`, `42018369099`)
Evidence: `ANALYSIS/RUNTIME/MISSION_07/ENV/DEVICE_AND_ROOT.txt`,
`ENV/APK_INSTALL.txt`, `ENV/POST_LAUNCH_PROCESS.txt`, `FRIDA/INSTALL.txt`.

| Item | Measured value |
|---|---|
| Workflow | `.github/workflows/mimo-runtime-verification.yml` (`ubuntu-latest`, pinned `reactivecircus/android-emulator-runner@v2.35.0`) |
| ADB | Android Debug Bridge 1.0.41, version 37.0.1-15733141, `/usr/local/lib/android/sdk/platform-tools/adb` |
| Device | `emulator-5554`, `sdk_gphone64_x86_64` / `emu64xa` |
| Android | 16 / API 36, `BE2A.250530.026.F3/13894323:userdebug/dev-keys` |
| `ro.build.type` | `userdebug` |
| `ro.debuggable` / `ro.secure` | `1` / `1` |
| ABI | `ro.product.cpu.abilist=x86_64,arm64-v8a`; `ro.dalvik.vm.native.bridge=libndk_translation.so`; app `primaryCpuAbi=arm64-v8a` (M05) |
| Kernel | `Linux 6.6.66-android15-8-gd0c43a640eab … clang 18.0.0` |
| Memory | `MemTotal: 4013804 kB` |
| Package | `com.getmimo`, `versionName=9.35`, `versionCode=1792759685`, `minSdk=28`, `targetSdk=36`, `dataDir=/data/user/0/com.getmimo`, launcher `com.getmimo/.ui.SplashActivity_default` |
| App process | `pidof com.getmimo` → e.g. `3407`; **Frida process NAME is `Mimo`**, not `com.getmimo`; 125 threads at launch |
| Device binaries | `/system/bin/sqlite3` **present**, `toybox 0.8.12-android`, `/system/bin/strace` **present**, `am`, `dumpsys`, `logcat`, `cmd` present |

## 3. Root and private-data access (measured, not assumed)
`adb root` + `adb wait-for-device` →
`uid=0(root) gid=0(root) groups=… context=u:r:su:s0`.
`/system/xbin/su` exists and `su 0 id` returns uid 0.
SELinux: `getenforce` = `Enforcing`; `setenforce 0` exit 0 → `Permissive`.
`run-as com.getmimo` was attempted **before the APK was installed** and
returned `run-as: unknown package: com.getmimo` — this is NOT evidence that
`run-as` is unavailable for the app; root access made it unnecessary.
Root `cp -a` of `/data/data/com.getmimo/{databases,shared_prefs,files/datastore,no_backup}`
and `adb pull` succeeded (47–95 files per snapshot). `sqlite3 <db> '.backup …'`
on device produced consistent readable copies. `mimo.db` uses
`PRAGMA journal_mode = wal`; `mimo.db-wal` / `mimo.db-shm` captured.

**M07 correction of earlier missions:** prior M03/M05/M06 script headers that
described root/private-DB extraction as forbidden are explicitly reversed by
the mission owner. Root and private sandbox inspection were assessed and are
normal, working techniques here.

## 4. Frida / instrumentation (measured)
* `frida==17.25.2`, `frida-tools==14.11.0` on runner Python 3.14.4.
* `frida-server-17.25.2-android-x86_64.xz` (44,889,284 B → 172,034,312 B
  uncompressed, ELF x86-64 Android 21, NDK r29) pushed to
  `/data/local/tmp/frida-server`; `frida-ps -U` lists `Mimo`.
  **Server must be kept alive by a host-side `adb shell` process**: a bare
  `nohup … &` inside `adb shell` is reaped when that remote shell exits
  (measured run `42018369099`: `frida-ps` worked, attach then failed with
  `frida.ServerNotRunningError`).
* Frida **attach by PID** is required: `dev.get_process('com.getmimo')` fails
  because the process name is `Mimo`; `dev.spawn()` fails with
  `NotSupportedError: need Gadget to attach on jailed Android`.
* **Frida 17 no longer bundles the Java bridge.** `Java.perform` raised
  `ReferenceError: 'Java' is not defined` (run `42019353340`, script line 118;
  confirmed by frida/frida#3473 and the 17.0.0 release notes). Fixed by
  pre-binding the compiled `frida-tools` bridge
  (`ANALYSIS/RUNTIME/MISSION_07/FRIDA/java_bridge_frida17.js`, 237,079 B,
  byte-identical to `frida_tools/bridges/java.js` from 14.11.0) as
  `globalThis.Java` before the agent runs. Afterwards 41 Java hooks installed
  and 914 JSONL events captured (run `42025423068`).
* `Java.enumerateLoadedClassesSync()` reported 36,825 loaded classes, 85
  `com.getmimo.*` classes at attach time.

**Techniques still `UNKNOWN` / not exercised:** Xposed/LSPosed, JVMTI,
explicit JNI/native-library tracing, heap dump tooling (`am dumpheap`),
`strace` syscall capture, instrumented-APK test copies. None was declared
unavailable — they simply were not needed for the measured results so far.

## 5. Genuine network isolation (measured, run `42019353340`)
`ANALYSIS/RUNTIME/MISSION_07/EXPERIMENTS/G_OFFLINE_ISOLATION.txt`:
before `Active default network: 101` with `MOBILE[LTE]` and `WIFI` agents;
after `svc wifi disable`, `svc data disable`,
`cmd connectivity airplane-mode enable`:
```
Active default network: none
connect: Network is unreachable
settings get global airplane_mode_on -> 1
```
`am force-stop com.getmimo` + `am start -n …/.ui.SplashActivity_default`
succeeded offline; UI hierarchies and private DB snapshots were captured.
This satisfies M07's requirement that offline tests verify no active default
network. No reconnect claim is made (M05 observed `svc wifi enable` did not
restore connectivity).

## 6. Evidence paths
`ANALYSIS/RUNTIME/MISSION_07/ENV/`, `FRIDA/`, `TRACES/`, `DB/`, `UI/`,
`EXPERIMENTS/`, `LOGS/`; workflow runs `42017453045` (stage 1),
`42018369099` (stage 1B), `42019353340` (stage 2), `42025423068` (stage 3),
and the stage-4 run recorded in `LOGS/DISPATCH.txt`.
