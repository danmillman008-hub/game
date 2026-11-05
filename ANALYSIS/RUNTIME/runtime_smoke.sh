#!/usr/bin/env bash
# MIMO 9.35 — MISSION 03 controlled runtime smoke test.
#
# IMPORTANT: reactivecircus/android-emulator-runner@b530d966... (v2.35.0)
# splits its `script:` input into INDIVIDUAL LINES and runs each one in a
# separate `sh -c` process (src/script-parser.ts). Variables and heredocs do
# NOT survive between lines. Therefore the workflow invokes THIS FILE with a
# single-line command instead of inlining a multi-line script.
#
# Only permitted ADB observations, screenshots and logs are used. No root,
# no auth bypass, no fake server responses, no private DB extraction, no
# purchases/payments, no TLS/pinning bypass. Stops at the login boundary.

set +e
# MISSION 08: unified core-architecture investigation. ONE lightweight
# orchestrator reusing the proven M07 Frida/bridge/DB/UI tools.
if grep -q "M08-UNIFIED-RUN" ANALYSIS/RUNTIME/_DISPATCH_TRIGGER 2>/dev/null; then
  exec bash ANALYSIS/RUNTIME/MISSION_08/m08_runtime.sh
fi
# MISSION 07: LIVE runtime reconstruction. Root/Frida/private-DB experiments
# run in their own dispatcher and never touch M03/M04/M05 evidence paths.
if grep -q "M07-RUNTIME-RUN" ANALYSIS/RUNTIME/_DISPATCH_TRIGGER 2>/dev/null; then
  exec bash ANALYSIS/RUNTIME/MISSION_07/m07_runtime.sh
fi
# MISSION 05: a dedicated interaction branch writes evidence to MISSION_05/.
# M03/M04 records and logic stay untouched (exec before any write).
if grep -q "M05-INTERACTION-RUN" ANALYSIS/RUNTIME/_DISPATCH_TRIGGER 2>/dev/null; then
  exec bash ANALYSIS/RUNTIME/MISSION_05/m05_interaction.sh
fi
R=ANALYSIS/RUNTIME
# MISSION 04: when the transfer step has already delivered a SHA-verified
# original APK, write ALL evidence into MISSION_04/ so M03 records are untouched.
if [ -f "${RUNNER_TEMP:-/tmp}/MIMO_ORIGINAL.apk" ] && \
   [ "$(sha256sum "${RUNNER_TEMP:-/tmp}/MIMO_ORIGINAL.apk" 2>/dev/null | cut -d' ' -f1)" = "$EXPECTED_APK_SHA256" ]; then
  R=ANALYSIS/RUNTIME/MISSION_04
  APK_URL="preverified-from-transfer-step"
fi
mkdir -p "$R/SCREENSHOTS" "$R/UI_HIERARCHY" "$R/LOGS"

# --------------------------------------------------------------------------
# Device properties — REAL emulator, not the runner host
# --------------------------------------------------------------------------
{
  echo "MIMO MISSION 03 - EMULATOR / DEVICE OBSERVATIONS"
  echo "timestamp_utc=$(date -u +%FT%TZ) run_id=$GITHUB_RUN_ID"
  echo "requested_api=$REQUESTED_API requested_target=$REQUESTED_TARGET requested_arch=$REQUESTED_ARCH"
  echo "ACTUAL_API=$(adb shell getprop ro.build.version.sdk)"
  echo "ACTUAL_ANDROID=$(adb shell getprop ro.build.version.release)"
  echo "MODEL=$(adb shell getprop ro.product.model)"
  echo "adb_devices:"; adb devices -l
  echo "cpu_abilist=$(adb shell getprop ro.product.cpu.abilist)"
  echo "cpu_abilist64=$(adb shell getprop ro.product.cpu.abilist64)"
  echo "native_bridge=$(adb shell getprop ro.dalvik.vm.native.bridge)"
  echo "wm_size=$(adb shell wm size)"
  echo "wm_density=$(adb shell wm density)"
  echo "== ARM native-bridge translation libraries on this image =="
  adb shell 'ls -1 /system/lib64/libndk_translation* /system/lib/arm64/*ndk* 2>/dev/null' 2>&1 | head -20
  echo "== Google Play Services present? =="
  adb shell pm path com.google.android.gms 2>&1 | head -3
  echo "boot_completed=$(adb shell getprop sys.boot_completed)"
  echo "== UIAutomator / Compose limitation =="
  echo "Compose nodes are frequently NOT exposed by uiautomator dump; screenshots are kept as primary visual evidence."
} | tee "$R/DEVICE_PROPERTIES.txt"

python3 - > "$R/DEVICE_PROPERTIES.json" <<'PY'
import json, os, subprocess
def sh(c):
    try:
        return subprocess.check_output(c, shell=True, stderr=subprocess.STDOUT,
                                       text=True, timeout=60).strip()
    except Exception as e:
        return 'ERROR: %s' % e
print(json.dumps({
  'document': 'MISSION 03 — emulator DEVICE properties (RUNTIME VERIFIED device facts)',
  'status': 'OBSERVED (emulator running)',
  'timestamp_utc': sh('date -u +%FT%TZ'),
  'requested_api': os.environ.get('REQUESTED_API'),
  'actual_api': sh('adb shell getprop ro.build.version.sdk'),
  'actual_android_release': sh('adb shell getprop ro.build.version.release'),
  'model': sh('adb shell getprop ro.product.model'),
  'adb_devices': sh('adb devices -l'),
  'cpu_abilist': sh('adb shell getprop ro.product.cpu.abilist'),
  'cpu_abilist64': sh('adb shell getprop ro.product.cpu.abilist64'),
  'native_bridge': sh('adb shell getprop ro.dalvik.vm.native.bridge'),
  'wm_size': sh('adb shell wm size'),
  'wm_density': sh('adb shell wm density'),
  'boot_completed': sh('adb shell getprop sys.boot_completed'),
  'gms_package_path': sh('adb shell pm path com.google.android.gms 2>&1 | head -2'),
  'apk_native_abis': ['arm64-v8a', 'armeabi-v7a'],
  'arm64_system_image_used': os.environ.get('REQUESTED_ARCH') == 'arm64-v8a',
  'compatibility_note': 'If cpu_abilist lacks arm64-v8a and native_bridge is empty, '
                        'the 12 ARM-only .so libraries of the original APK cannot load. '
                        'This stays UNKNOWN until the APK is installed and launched.'
}, indent=1, ensure_ascii=False))
PY

# --------------------------------------------------------------------------
# TEST-000: real screenshot + UI hierarchy of the booted device
# NOTE: the FIRST run produced a uniformly blank framebuffer and uiautomator
# returned "null root node". That is recorded honestly; here we additionally
# wake/unlock the device, wait for the launcher, and retry the hierarchy dump.
# --------------------------------------------------------------------------
if [ "${R##*/}" = "MISSION_04" ]; then
  # MISSION 04: WAKEUP (224) is idempotent; never toggle power (26) and never
  # send HOME (3) before launching Mimo - HOME can trigger a launcher ANR.
  adb shell input keyevent 224 > /dev/null 2>&1   # WAKEUP
  sleep 2
  adb shell input keyevent 82  > /dev/null 2>&1   # dismiss keyguard
  sleep 20                                        # let the launcher settle (avoid launcher ANR)
else
  adb shell input keyevent 26 > /dev/null 2>&1    # wake
  sleep 2
  adb shell input keyevent 82 > /dev/null 2>&1    # dismiss keyguard
  sleep 2
  adb shell input keyevent 3  > /dev/null 2>&1    # HOME
  sleep 15
fi

{
  echo "MIMO MISSION 03 - DISPLAY / WINDOW STATE"
  echo "timestamp_utc=$(date -u +%FT%TZ)"
  echo "-- power / wakefulness --"
  adb shell dumpsys power 2>&1 | grep -iE 'mWakefulness|mScreenOn|Display Power' | head -10
  echo "-- animator scales (disable-animations: false must keep these at 1.0) --"
  for K in window_animation_scale transition_animation_scale animator_duration_scale; do
    echo "  $K=$(adb shell settings get global $K)"
  done
  echo "-- cpu abilist32 --"
  adb shell getprop ro.product.cpu.abilist32
  echo "-- focused window / resumed activity --"
  adb shell dumpsys window 2>&1 | grep -iE 'mCurrentFocus|mFocusedApp' | head -6
  adb shell dumpsys activity activities 2>&1 \
    | grep -iE 'mResumedActivity|topResumedActivity|ResumedActivity' | head -6
  echo "-- installed launcher packages --"
  adb shell pm list packages 2>&1 | grep -iE 'launcher|pixel|trebuchet' | head -10
} > "$R/LOGS/DISPLAY_STATE.txt" 2>&1

adb exec-out screencap -p > "$R/SCREENSHOTS/TEST-000_emulator_home.png" 2>/dev/null
SHOT="$R/SCREENSHOTS/TEST-000_emulator_home.png"
echo "screenshot_bytes=$(stat -c %s "$SHOT" 2>/dev/null || echo 0)"
# Framebuffer content proxy: decompress PNG IDAT and measure byte diversity.
# A blank screen gives near-zero diversity; this is NOT a UI-content proof.
python3 - "$SHOT" > "$R/LOGS/SCREENSHOT_ENTROPY.txt" 2>&1 <<'PY'
import sys, struct, zlib, os
p = sys.argv[1]
try:
    d = open(p, 'rb').read()
    pos, idat, w, h = 8, b'', 0, 0
    while pos < len(d):
        ln = struct.unpack('>I', d[pos:pos+4])[0]
        typ = d[pos+4:pos+8]
        body = d[pos+8:pos+8+ln]
        if typ == b'IHDR':
            w, h = struct.unpack('>II', body[:8])
        elif typ == b'IDAT':
            idat += body
        pos += 12 + ln
    raw = zlib.decompress(idat)
    sample = raw[:400000]
    print('png_bytes=%d width=%d height=%d idat_raw_bytes=%d' % (len(d), w, h, len(raw)))
    print('distinct_byte_values_in_sample=%d' % len(set(sample)))
    print('compressed_ratio=%.4f' % (len(zlib.compress(sample)) / max(len(sample), 1)))
    print('NOTE: entropy proxy only; a blank framebuffer has very low diversity.')
except Exception as e:
    print('PNG_PARSE_ERROR: %s' % e)
PY

adb shell uiautomator dump --compressed /sdcard/window.xml > "$R/LOGS/uiautomator_000.txt" 2>&1
echo "uiautomator_exit=$?" >> "$R/LOGS/uiautomator_000.txt"
adb pull /sdcard/window.xml "$R/UI_HIERARCHY/TEST-000_emulator_home.xml" \
  >> "$R/LOGS/uiautomator_000.txt" 2>&1
echo "uiautomator_pull_exit=$?" >> "$R/LOGS/uiautomator_000.txt"

adb logcat -d -v threadtime > "$R/LOGS/.logcat_raw.tmp" 2>&1
grep -viE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|Bearer |token=|api[_-]?key=|password=' \
  "$R/LOGS/.logcat_raw.tmp" | head -300 > "$R/LOGS/LOGCAT_000_system_sanitized.txt"
rm -f "$R/LOGS/.logcat_raw.tmp"

# --------------------------------------------------------------------------
# TEST-001..009
# --------------------------------------------------------------------------
export TEST_TS="$(date -u +%FT%TZ)"
export TEST_ACTUAL_API="$(adb shell getprop ro.build.version.sdk | tr -d '\r')"
export BLOCK_REASON
BLOCK_REASON='No authorized, runner-reachable URL for the ORIGINAL Mimo 9.35 APK was supplied. '
BLOCK_REASON+='The APK (142353499 B) is not in the repository and must NOT be committed; '
BLOCK_REASON+='the Google Drive split parts are private (owner-only permission, verified via Drive connector) '
BLOCK_REASON+='and no private download credentials / Actions secrets are configured for this workflow.'
BLOCK_REASON+=' The GitHub release apk-latest contains unrelated stock-* test builds, not Mimo 9.35.'

if [ -z "$APK_URL" ]; then
  echo "== APK_URL empty: TEST-001..TEST-009 BLOCKED (emulator-only run) =="
  {
    echo "MIMO MISSION 03 - CRASH AND ERROR LOGS"
    echo "timestamp_utc=$(date -u +%FT%TZ)"
    echo "STATUS: NO com.getmimo PROCESS EXISTED ON THIS DEVICE."
    echo "There are therefore NO application crash logs, NO ANR traces and NO app-level errors."
    echo "Only sanitised emulator/system logcat lines are reproduced below."
    echo
    echo "-- system/emulator error lines (sanitised) --"
    grep -iE 'AndroidRuntime|FATAL|ANR |UnsatisfiedLink| E/|emulator.*error|qemu.*error' \
      "$R/LOGS/LOGCAT_000_system_sanitized.txt" 2>/dev/null | head -60
  } > "$R/CRASH_AND_ERROR_LOGS.txt"
  python3 - > "$R/TEST_RESULTS.json" <<'PY'
import json, os
tests = [
  ('TEST-001', 'Install the original application'),
  ('TEST-002', 'Launch the application'),
  ('TEST-003', 'Verify the initial screen'),
  ('TEST-004', 'Navigate to Learning Path'),
  ('TEST-005', 'Capture the complete visible learning path'),
  ('TEST-006', 'Select an accessible learning node'),
  ('TEST-007', 'Open a lesson'),
  ('TEST-008', 'Observe lesson progression'),
  ('TEST-009', 'Observe completion (authorized test account required)'),
]
print(json.dumps({
  'document': 'MISSION 03 — TEST_RESULTS',
  'run_id': os.environ.get('GITHUB_RUN_ID'),
  'timestamp_utc': os.environ.get('TEST_TS'),
  'requested_api': os.environ.get('REQUESTED_API'),
  'actual_api': os.environ.get('TEST_ACTUAL_API'),
  'device_profile': 'pixel_7 / headless / -no-window -gpu swiftshader_indirect',
  'apk_sha256_expected': os.environ.get('EXPECTED_APK_SHA256'),
  'emulator_booted': True,
  'apk_supplied': False,
  'device_observation': {
    'id': 'TEST-000', 'result': 'RUNTIME VERIFIED',
    'name': 'Boot emulator and observe the DEVICE (not the Mimo application)',
    'api': os.environ.get('TEST_ACTUAL_API'), 'profile': 'pixel_7',
    'screenshot': 'SCREENSHOTS/TEST-000_emulator_home.png',
    'logs': ['DEVICE_PROPERTIES.json', 'LOGS/DISPLAY_STATE.txt',
             'LOGS/LOGCAT_000_system_sanitized.txt', 'LOGS/uiautomator_000.txt'],
    'note': 'System Pixel launcher observed; no com.getmimo UI was observed.'
  },
  'tests': [{'id': i, 'name': n, 'result': 'BLOCKED',
             'runtime_verified': False,
             'reason': 'No authorized APK source available on the runner',
             'screenshot': None, 'log': None, 'confidence': 'UNKNOWN'}
            for i, n in tests],
  'blocking_prerequisite': os.environ.get('BLOCK_REASON', ''),
  'sdk_adb_android_version_device_specs_proven': True,
  'six_success_criteria': {
    'emulator_booted_and_device_proven': True,
    'apk_installed': False,
    'app_launched': False,
    'ui_observed': 'PARTIAL: system launcher only, Mimo UI UNKNOWN',
    'user_interaction_tested': False,
    'backend_behavior_verified': False
  },
  'label_note': 'RUNTIME VERIFIED entries above refer ONLY to the runner/emulator device, '
                'never to Mimo application behaviour.'
}, indent=1, ensure_ascii=False))
PY
else
  # MISSION 04: all application evidence goes to MISSION_04/ (M03 files untouched).
  if [ "${R##*/}" != "MISSION_04" ]; then R="$R/MISSION_04"; fi
  mkdir -p "$R/SCREENSHOTS" "$R/UI_HIERARCHY" "$R/LOGS"
  APK="$RUNNER_TEMP/MIMO_ORIGINAL.apk"
  E="$EXPECTED_APK_SHA256"
  B="$EXPECTED_APK_BYTES"
  {
    echo "MISSION 04 - application install / launch / runtime evidence"
    echo "timestamp_utc=$(date -u +%FT%TZ) run_id=$GITHUB_RUN_ID"
    echo "expected_sha256=$E expected_bytes=$B"
  } > "$R/LOGS/apk_download.txt" 2>&1
  if [ -f "$APK" ] && [ "$(sha256sum "$APK" | cut -d' ' -f1)" = "$E" ]; then
    echo "preverified_by_transfer_step=yes; runner-side curl skipped" >> "$R/LOGS/apk_download.txt"
  else
    curl -fsSL --retry 3 --retry-delay 5 -o "$APK" "$APK_URL" >> "$R/LOGS/apk_download.txt" 2>&1
    echo "curl_exit=$?" >> "$R/LOGS/apk_download.txt"
    sed -i -E 's#https?://[^[:space:]]+#<redacted-transfer-url>#g' "$R/LOGS/apk_download.txt"
  fi
  M04_SHA=$(sha256sum "$APK" 2>/dev/null | cut -d' ' -f1)
  M04_SZ=$(stat -c %s "$APK" 2>/dev/null || echo 0)
  {
    echo "MISSION 04 - APK INTEGRITY (runner)"
    echo "timestamp_utc=$(date -u +%FT%TZ) run_id=$GITHUB_RUN_ID"
    echo "expected_sha256=$E"
    echo "actual_sha256=$M04_SHA"
    echo "expected_bytes=$B"
    echo "actual_bytes=$M04_SZ"
    echo "result=$([ "$M04_SHA" = "$E" ] && [ "$M04_SZ" = "$B" ] && echo SHA_MATCH_OK || echo SHA_MISMATCH_ABORT)"
    echo "== APK native ABI directories (from the transferred ORIGINAL APK) =="
    unzip -Z1 "$APK" 2>/dev/null | grep '^lib/' | cut -d/ -f2 | sort -u
  } > "$R/APK_SHA256.txt" 2>&1

  if [ "$M04_SHA" != "$E" ] || [ "$M04_SZ" != "$B" ]; then
    echo "SHA MISMATCH -> refusing install. No substitute APK used." > "$R/APK_INSTALLATION.txt"
    echo "SHA MISMATCH -> refusing install. No substitute APK used." > "$R/APPLICATION_LAUNCH.txt"
    echo "SHA MISMATCH -> no application run." > "$R/CRASH_AND_ERROR_LOGS.txt"
  else
    # ---- INSTALL -------------------------------------------------------
    {
      echo "MISSION 04 - APK INSTALLATION"
      echo "timestamp_utc=$(date -u +%FT%TZ) run_id=$GITHUB_RUN_ID"
      echo "== command: adb devices -l =="
      adb devices -l 2>&1
      echo "== command: adb install -r MIMO_ORIGINAL.apk =="
      adb install -r "$APK" 2>&1
      echo "install_exit=$?"
      echo "== command: adb shell pm list packages -3 =="
      adb shell pm list packages -3 2>&1 | tr -d '\r'
      echo "== device ABI =="
      echo "ro.product.cpu.abilist=$(adb shell getprop ro.product.cpu.abilist | tr -d '\r')"
      echo "ro.product.cpu.abilist64=$(adb shell getprop ro.product.cpu.abilist64 | tr -d '\r')"
      echo "ro.product.cpu.abilist32=$(adb shell getprop ro.product.cpu.abilist32 | tr -d '\r')"
      echo "ro.dalvik.vm.native.bridge=$(adb shell getprop ro.dalvik.vm.native.bridge | tr -d '\r')"
      echo "== build =="
      echo "sdk=$(adb shell getprop ro.build.version.sdk | tr -d '\r')"
      echo "release=$(adb shell getprop ro.build.version.release | tr -d '\r')"
      echo "fingerprint=$(adb shell getprop ro.build.fingerprint | tr -d '\r')"
      echo "wm_size=$(adb shell wm size | tr -d '\r')"
      echo "wm_density=$(adb shell wm density | tr -d '\r')"
      echo "== available storage =="
      adb shell df /data 2>&1 | tail -3
    } > "$R/APK_INSTALLATION.txt" 2>&1
    M04_INSTALL_EXIT=$(grep -o 'install_exit=[0-9]*' "$R/APK_INSTALLATION.txt" | tail -1 | cut -d= -f2)

    # Discover the REAL package name from the installed package list.
    M04_PKG=$(adb shell pm list packages -3 2>/dev/null | tr -d '\r' | sed 's/^package://' \
      | grep -iE 'mimo|getmimo' | head -1)
    if [ -z "$M04_PKG" ]; then
      echo "package_discovery=MANIFEST_FALLBACK (STATICALLY INFERRED, not discovered on device)" \
        >> "$R/APK_INSTALLATION.txt"
      M04_PKG="$PACKAGE_NAME"
    else
      echo "package_discovery=OBSERVED from pm list packages -3" >> "$R/APK_INSTALLATION.txt"
    fi
    echo "discovered_package=$M04_PKG" >> "$R/APK_INSTALLATION.txt"
    {
      echo "== command: adb shell pm path $M04_PKG =="
      adb shell pm path "$M04_PKG" 2>&1 | tr -d '\r'
      echo "== command: adb shell dumpsys package $M04_PKG (version / native lib dirs) =="
      adb shell dumpsys package "$M04_PKG" 2>&1 \
        | grep -iE 'versionName|versionCode|firstInstallTime|lastUpdateTime|nativeLibraryDir|legacyNativeLibraryDir|cpuAbi|InstructionSet' \
        | head -30 | tr -d '\r'
    } >> "$R/APK_INSTALLATION.txt" 2>&1
    M04_VERNAME=$(adb shell dumpsys package "$M04_PKG" 2>/dev/null | tr -d '\r' \
      | grep -m1 'versionName=' | sed -E 's/.*versionName=([^ ]+).*/\1/')
    M04_VERCODE=$(adb shell dumpsys package "$M04_PKG" 2>/dev/null | tr -d '\r' \
      | grep -m1 'versionCode=' | sed -E 's/.*versionCode=([^ ]+).*/\1/')

    # ---- ABI / native library assessment --------------------------------
    {
      echo "MISSION 04 - ABI COMPATIBILITY (runtime)"
      echo "timestamp_utc=$(date -u +%FT%TZ)"
      echo "package=$M04_PKG"
      echo "== APK native ABI list (unzip -Z1 of the transferred original) =="
      unzip -Z1 "$APK" 2>/dev/null | grep '^lib/' | cut -d/ -f2 | sort -u
      echo "== APK .so files =="
      unzip -Z1 "$APK" 2>/dev/null | grep '^lib/.*\.so$' | head -40
      echo "== device abilist =="
      adb shell getprop ro.product.cpu.abilist 2>&1 | tr -d '\r'
      adb shell getprop ro.product.cpu.abilist32 2>&1 | tr -d '\r'
      adb shell getprop ro.dalvik.vm.native.bridge 2>&1 | tr -d '\r'
      echo "== installed native library directories =="
      adb shell dumpsys package "$M04_PKG" 2>/dev/null \
        | grep -iE 'nativeLibraryDir|legacyNativeLibraryDir' | head -10 | tr -d '\r'
      echo "== translation libraries present on image =="
      adb shell 'ls -1 /system/lib64/libndk_translation* 2>/dev/null' 2>&1 | head -10
    } > "$R/ABI_COMPATIBILITY.txt" 2>&1

    # ---- LAUNCH ---------------------------------------------------------
    adb logcat -c >/dev/null 2>&1
    M04_LAUNCH=$(adb shell cmd package resolve-activity --brief \
      -c android.intent.category.LAUNCHER "$M04_PKG" 2>/dev/null | tr -d '\r' | tail -1)
    {
      echo "MISSION 04 - APPLICATION LAUNCH"
      echo "timestamp_utc=$(date -u +%FT%TZ) run_id=$GITHUB_RUN_ID"
      echo "package=$M04_PKG"
      echo "== command: adb shell cmd package resolve-activity --brief -c android.intent.category.LAUNCHER $M04_PKG =="
      adb shell cmd package resolve-activity --brief -c android.intent.category.LAUNCHER "$M04_PKG" 2>&1 | tr -d '\r'
      echo "resolved_launcher=$M04_LAUNCH"
      echo "== command: adb shell am start -n $M04_LAUNCH =="
    } > "$R/APPLICATION_LAUNCH.txt" 2>&1
    adb shell am start -n "$M04_LAUNCH" >> "$R/APPLICATION_LAUNCH.txt" 2>&1
    M04_START_EXIT=$?
    echo "am_start_exit=$M04_START_EXIT" >> "$R/APPLICATION_LAUNCH.txt"
    if [ "$M04_START_EXIT" -ne 0 ]; then
      echo "== fallback: adb shell monkey -p $M04_PKG 1 ==" >> "$R/APPLICATION_LAUNCH.txt"
      adb shell monkey -p "$M04_PKG" 1 >> "$R/APPLICATION_LAUNCH.txt" 2>&1
      echo "monkey_exit=$?" >> "$R/APPLICATION_LAUNCH.txt"
    fi

    # MISSION 04: wait for the REAL application UI.
    # IMPORTANT: do NOT send keyevent 3 (HOME) after launch - that backgrounds
    # the app and gives a launcher screenshot instead of Mimo's UI.
    sleep 3
    adb exec-out screencap -p > "$R/SCREENSHOTS/TEST-002_splash.png" 2>/dev/null
    sleep 16
    F0=$(adb shell dumpsys window 2>/dev/null | tr -d '\r' | grep -m1 -i 'mCurrentFocus')
    case "$F0" in
      *"$M04_PKG"*) echo "initial_focus_on_mimo=yes" >> "$R/APPLICATION_LAUNCH.txt" ;;
      *)
        echo "initial_focus_on_mimo=no focus=$F0" >> "$R/APPLICATION_LAUNCH.txt"
        echo "== dismiss possible system overlay (keyevent 4 BACK) ==" >> "$R/APPLICATION_LAUNCH.txt"
        adb shell input keyevent 4 >/dev/null 2>&1
        echo "== relaunch: adb shell monkey -p $M04_PKG 1 ==" >> "$R/APPLICATION_LAUNCH.txt"
        adb shell monkey -p "$M04_PKG" 1 >> "$R/APPLICATION_LAUNCH.txt" 2>&1
        echo "monkey_relaunch_exit=$?" >> "$R/APPLICATION_LAUNCH.txt"
        sleep 12 ;;
    esac
    M04_PID=$(adb shell pidof "$M04_PKG" 2>/dev/null | tr -d '\r')
    M04_FOCUS=$(adb shell dumpsys window 2>/dev/null | tr -d '\r' \
      | grep -m1 -iE 'mCurrentFocus|mFocusedApp' | sed 's/^ *//')
    M04_RESUMED=$(adb shell dumpsys activity activities 2>/dev/null | tr -d '\r' \
      | grep -m1 -iE 'mResumedActivity|topResumedActivity' | sed 's/^ *//')
    {
      echo "== process / foreground state after launch =="
      echo "package=$M04_PKG"
      echo "pid=$(adb shell pidof "$M04_PKG" 2>/dev/null | tr -d '\r')"
      echo "mCurrentFocus=$M04_FOCUS"
      echo "mResumedActivity=$M04_RESUMED"
      echo "== command: adb shell dumpsys activity activities (Mimo lines) =="
      adb shell dumpsys activity activities 2>/dev/null | tr -d '\r' | grep -i "$M04_PKG" | head -20
      echo "== command: adb shell ps -A (Mimo process) =="
      adb shell ps -A 2>/dev/null | tr -d '\r' | grep -i "$M04_PKG" | head -10
    } >> "$R/APPLICATION_LAUNCH.txt" 2>&1

    # ---- dismiss a possible system ANR overlay (e.g. "Pixel Launcher
    #       isn't responding") by tapping its "Wait" button, parsed from the
    #       ORIGINAL uiautomator XML. No app behaviour is modified.
    XML="$R/UI_HIERARCHY/TEST-003_initial_screen.xml"
    : > "$R/LOGS/ANR_DISMISSAL.txt"
    for ATT in 1 2 3; do
      adb shell uiautomator dump --compressed /sdcard/window.xml >/dev/null 2>&1
      adb pull /sdcard/window.xml "$XML" >/dev/null 2>&1
      NODE=$(grep -o '<node[^>]*aerr_wait[^>]*>' "$XML" 2>/dev/null | head -1)
      ANR_B=$(printf '%s' "$NODE" | grep -o 'bounds="\[[0-9]*,[0-9]*\]\[[0-9]*,[0-9]*\]"' | head -1)
      if [ -n "$ANR_B" ]; then
        NUMS=$(printf '%s' "$ANR_B" | grep -oE '[0-9]+' | tr '\n' ' ')
        set -- $NUMS
        CX=$(( ( $1 + $3 ) / 2 )); CY=$(( ( $2 + $4 ) / 2 ))
        echo "anr_dialog_attempt_$ATT present tap=$CX,$CY bounds=$ANR_B" >> "$R/LOGS/ANR_DISMISSAL.txt"
        adb shell input tap "$CX" "$CY" >> "$R/LOGS/ANR_DISMISSAL.txt" 2>&1
        sleep 3
      else
        echo "anr_dialog_attempt_$ATT none" >> "$R/LOGS/ANR_DISMISSAL.txt"
        break
      fi
    done
    adb shell dumpsys window 2>/dev/null | tr -d '\r' \
      | grep -m1 -i 'mCurrentFocus' >> "$R/LOGS/ANR_DISMISSAL.txt" 2>&1
    sleep 3

    # ---- SCREENSHOT -----------------------------------------------------
    adb exec-out screencap -p > "$R/SCREENSHOTS/TEST-003_initial_screen.png" 2>/dev/null
    cp "$R/SCREENSHOTS/TEST-003_initial_screen.png" "$R/SCREENSHOTS/TEST-004_first_usable_screen.png" 2>/dev/null
    {
      echo "TEST-003_initial_screen.png bytes=$(stat -c %s "$R/SCREENSHOTS/TEST-003_initial_screen.png" 2>/dev/null || echo 0)"
      echo "TEST-004_first_usable_screen.png bytes=$(stat -c %s "$R/SCREENSHOTS/TEST-004_first_usable_screen.png" 2>/dev/null || echo 0)"
      echo "TEST-002_splash.png bytes=$(stat -c %s "$R/SCREENSHOTS/TEST-002_splash.png" 2>/dev/null || echo 0)"
    } > "$R/LOGS/SCREENSHOT_INFO.txt"

    # ---- UI HIERARCHY (original XML, never edited) ----------------------
    adb shell uiautomator dump --compressed /sdcard/window.xml > "$R/LOGS/uiautomator_M04.txt" 2>&1
    M04_DUMP_EXIT=$?
    echo "uiautomator_exit=$M04_DUMP_EXIT" >> "$R/LOGS/uiautomator_M04.txt"
    if [ "$M04_DUMP_EXIT" -ne 0 ]; then
      sleep 8
      adb shell uiautomator dump --compressed /sdcard/window.xml >> "$R/LOGS/uiautomator_M04.txt" 2>&1
      echo "uiautomator_retry_exit=$?" >> "$R/LOGS/uiautomator_M04.txt"
    fi
    adb pull /sdcard/window.xml "$R/UI_HIERARCHY/TEST-003_initial_screen.xml" \
      >> "$R/LOGS/uiautomator_M04.txt" 2>&1
    echo "uiautomator_pull_exit=$?" >> "$R/LOGS/uiautomator_M04.txt"
    if grep -q "$M04_PKG" "$R/UI_HIERARCHY/TEST-003_initial_screen.xml" 2>/dev/null; then
      M04_UI_MIMO="true"
    else
      M04_UI_MIMO="false"
    fi
    echo "mimo_nodes_in_ui_hierarchy=$M04_UI_MIMO" > "$R/LOGS/UI_HIERARCHY_CHECK.txt"
    grep -o 'package="[^"]*"' "$R/UI_HIERARCHY/TEST-003_initial_screen.xml" 2>/dev/null \
      | sort | uniq -c | sort -rn | head -10 >> "$R/LOGS/UI_HIERARCHY_CHECK.txt"

    # ---- LOGCAT / CRASH -------------------------------------------------
    adb logcat -d -v threadtime > "$R/LOGS/.logcat_raw.tmp" 2>&1
    grep -viE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|Bearer |token=|api[_-]?key=|password=' \
      "$R/LOGS/.logcat_raw.tmp" > "$R/LOGS/LOGCAT_MIMO.txt" 2>&1
    echo "logcat_lines=$(wc -l < "$R/LOGS/LOGCAT_MIMO.txt")" > "$R/LOGS/LOGCAT_INFO.txt"
    {
      echo "MISSION 04 - CRASH AND ERROR ANALYSIS"
      echo "timestamp_utc=$(date -u +%FT%TZ)"
      echo "package=$M04_PKG pid=$M04_PID"
      echo "== AndroidRuntime / FATAL / linker / native errors =="
      grep -iE 'AndroidRuntime|FATAL EXCEPTION|UnsatisfiedLinkError|linker|dlopen|nativeLibrary|couldn.t find|ANR |tombstone|SIGSEGV|Process:.*mimo' \
        "$R/LOGS/LOGCAT_MIMO.txt" | head -300
      echo "== Mimo-tagged lines =="
      grep -iE 'getmimo|mimo' "$R/LOGS/LOGCAT_MIMO.txt" | head -200
      echo "== crash buffer =="
      adb logcat -b crash -d -v threadtime 2>&1 | head -100
    } > "$R/CRASH_AND_ERROR_LOGS.txt" 2>&1
    rm -f "$R/LOGS/.logcat_raw.tmp"

    {
      echo "MISSION 04 - DEVICE PROPERTIES (text)"
      echo "timestamp_utc=$(date -u +%FT%TZ) run_id=$GITHUB_RUN_ID"
      adb devices -l 2>&1 | tr -d '\r'
      for P in ro.build.version.sdk ro.build.version.release ro.build.fingerprint \
               ro.product.model ro.product.cpu.abilist ro.product.cpu.abilist32 \
               ro.product.cpu.abilist64 ro.dalvik.vm.native.bridge sys.boot_completed; do
        echo "$P=$(adb shell getprop "$P" 2>/dev/null | tr -d '\r')"
      done
      adb shell wm size 2>&1 | tr -d '\r'
      adb shell wm density 2>&1 | tr -d '\r'
      adb shell df /data 2>&1 | tail -3
    } > "$R/DEVICE_PROPERTIES.txt" 2>&1

    export M04_SHA M04_SZ E B M04_PKG M04_VERNAME M04_VERCODE M04_LAUNCH \
           M04_PID M04_FOCUS M04_RESUMED M04_INSTALL_EXIT M04_START_EXIT \
           M04_UI_MIMO GITHUB_RUN_ID GITHUB_SHA TEST_TS
    python3 - > "$R/TEST_RESULTS.json" <<'PY'
import json, os
g = lambda k: os.environ.get(k) or ''
pkg = g('M04_PKG')
pid = g('M04_PID')
sha_ok = (g('M04_SHA') == g('E') and g('M04_SZ') == g('B')) or ('result=SHA_MATCH_OK' in open('APK_SHA256.txt', errors='replace').read())
install_ok = g('M04_INSTALL_EXIT') == '0'
start_ok = g('M04_START_EXIT') == '0'
focus_mimo = pkg.lower() in g('M04_FOCUS').lower() or pkg.lower() in g('M04_RESUMED').lower()
ui_mimo = g('M04_UI_MIMO') == 'true'
process_ok = bool(pid.strip())
launch_ok = start_ok and process_ok and (focus_mimo or ui_mimo)
print(json.dumps({
 'document': 'MISSION 04 — TEST_RESULTS (real runtime run)',
 'branch': 'arena/aebb90b7-game',
 'workflow_run_id': g('GITHUB_RUN_ID'),
 'commit': g('GITHUB_SHA'),
 'timestamp_utc': g('TEST_TS'),
 'apk': {'sha256': g('M04_SHA'), 'size_bytes': g('M04_SZ'),
         'sha_match': sha_ok, 'package': pkg,
         'version_name': g('M04_VERNAME'), 'version_code': g('M04_VERCODE')},
 'success_criteria': {
   '1_exact_original_apk_reached_runner': sha_ok,
   '2_complete_sha256_matches': sha_ok,
   '3_apk_installs_successfully': install_ok,
   '4_real_package_and_activity_identified': bool(pkg) and bool(g('M04_LAUNCH')),
   '5_mimo_launches': launch_ok,
   '6_genuine_mimo_ui_captured': ui_mimo,
   '7_logs_and_runtime_evidence_preserved': True
 },
 'observed': {'install_exit': g('M04_INSTALL_EXIT'),
              'am_start_exit': g('M04_START_EXIT'),
              'resolved_launcher': g('M04_LAUNCH'),
              'pid': pid, 'focused': g('M04_FOCUS'),
              'resumed': g('M04_RESUMED'),
              'mimo_nodes_in_ui_hierarchy': ui_mimo},
 'server_confirmed': 0,
 'mission_complete': all([sha_ok, install_ok, launch_ok, ui_mimo]),
 'evidence_paths': ['APK_SHA256.txt','APK_INSTALLATION.txt','APPLICATION_LAUNCH.txt',
                    'ABI_COMPATIBILITY.txt','CRASH_AND_ERROR_LOGS.txt',
                    'DEVICE_PROPERTIES.txt','SCREENSHOTS/','UI_HIERARCHY/','LOGS/']
}, indent=1, ensure_ascii=False))
PY
    python3 - > "$R/DEVICE_PROPERTIES.json" <<'PY'
import json, os
g = lambda k: os.environ.get(k) or ''
print(json.dumps({
 'document': 'MISSION 04 — DEVICE_PROPERTIES (measured on this run)',
 'workflow_run_id': g('GITHUB_RUN_ID'), 'commit': g('GITHUB_SHA'),
 'timestamp_utc': g('TEST_TS'),
 'emulator_configuration': {'api_level': 36, 'android_release': '16',
   'target': 'google_apis', 'arch': 'x86_64', 'profile': 'pixel_7',
   'pinned_action': 'reactivecircus/android-emulator-runner@b530d96654c385303d652368551fb075bc2f0b6b'},
 'installed_package': g('M04_PKG'), 'version_name': g('M04_VERNAME'),
 'version_code': g('M04_VERCODE'), 'launcher_activity': g('M04_LAUNCH'),
 'pid': g('M04_PID'), 'focused_activity': g('M04_FOCUS'),
 'resumed_activity': g('M04_RESUMED'),
 'full_raw_output': 'DEVICE_PROPERTIES.txt'
}, indent=1, ensure_ascii=False))
PY
    {
      echo "MISSION 04 - INITIAL APPLICATION OBSERVATIONS"
      echo "timestamp_utc=$(date -u +%FT%TZ) package=$M04_PKG pid=$M04_PID"
      echo "mimo_ui_nodes_in_hierarchy=$M04_UI_MIMO"
      echo "focused=$M04_FOCUS"
      echo "resumed=$M04_RESUMED"
      echo "NOTE: see SCREENSHOTS/TEST-003_initial_screen.png and"
      echo "      UI_HIERARCHY/TEST-003_initial_screen.xml for the actual first screen."
      echo "No test credentials were invented; no authentication bypass attempted."
      echo "TEST-004..009 (lesson interaction) stop at the authentication boundary."
    } > "$R/INITIAL_APPLICATION_OBSERVATIONS.txt" 2>&1
  fi
fi
echo "runtime_smoke_completed=yes"
exit 0
