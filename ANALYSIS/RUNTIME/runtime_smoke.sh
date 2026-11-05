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
R=ANALYSIS/RUNTIME
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
adb shell input keyevent 26 > /dev/null 2>&1   # wake
sleep 2
adb shell input keyevent 82 > /dev/null 2>&1   # dismiss keyguard
sleep 2
adb shell input keyevent 3  > /dev/null 2>&1   # HOME
sleep 15

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
  'tests': [{'id': i, 'name': n, 'result': 'BLOCKED',
             'runtime_verified': False,
             'reason': 'No authorized APK source available on the runner',
             'screenshot': None, 'log': None, 'confidence': 'UNKNOWN'}
            for i, n in tests],
  'blocking_prerequisite': os.environ.get('BLOCK_REASON', ''),
  'six_success_criteria': {
    'emulator_booted': True,
    'sdk_adb_android_version_device_specs_proven': True,
    'apk_installed': False, 'app_launched': False,
    'ui_observed': False, 'user_interaction_tested': False,
    'backend_behavior_verified': False
  }
}, indent=1, ensure_ascii=False))
PY
else
  echo "== APK_URL supplied: verifying SHA-256 before install =="
  APK="$RUNNER_TEMP/MIMO_ORIGINAL.apk"
  curl -fL --retry 3 --retry-delay 5 -o "$APK" "$APK_URL" > "$R/LOGS/apk_download.txt" 2>&1
  echo "curl_exit=$? downloaded_bytes=$(stat -c %s "$APK" 2>/dev/null || echo 0)" \
    >> "$R/LOGS/apk_download.txt"
  ACTUAL_SHA=$(sha256sum "$APK" 2>/dev/null | cut -d' ' -f1)
  echo "expected_sha=$EXPECTED_APK_SHA256 actual_sha=$ACTUAL_SHA" > "$R/APK_SHA256.txt"
  if [ "$ACTUAL_SHA" != "$EXPECTED_APK_SHA256" ]; then
    echo "SHA MISMATCH -> refusing install (no substitute APK will be used)" \
      > "$R/APK_INSTALLATION.txt"
    cat "$R/APK_INSTALLATION.txt"
  else
    echo "SHA MATCH -> installing" >> "$R/APK_SHA256.txt"
    adb install -r "$APK" > "$R/APK_INSTALLATION.txt" 2>&1
    echo "install_exit=$?" >> "$R/APK_INSTALLATION.txt"
    adb shell pm path "$PACKAGE_NAME" >> "$R/APK_INSTALLATION.txt" 2>&1
    adb shell dumpsys package "$PACKAGE_NAME" \
      | grep -E 'versionName|versionCode|firstInstallTime|lastUpdateTime' \
      >> "$R/APK_INSTALLATION.txt" 2>&1
    LAUNCH=$(adb shell cmd package resolve-activity --brief \
      -c android.intent.category.LAUNCHER "$PACKAGE_NAME" | tail -1)
    echo "resolved_launcher=$LAUNCH" >> "$R/APK_INSTALLATION.txt"
    adb shell am start -n "$LAUNCH" > "$R/APPLICATION_LAUNCH.txt" 2>&1
    echo "am_start_exit=$?" >> "$R/APPLICATION_LAUNCH.txt"
    sleep 12
    {
      echo "== process / activity state after launch =="
      echo "pid=$(adb shell pidof "$PACKAGE_NAME")"
      adb shell dumpsys activity activities \
        | grep -iE 'mResumedActivity|topResumedActivity|com.getmimo' | head -20
    } >> "$R/APPLICATION_LAUNCH.txt" 2>&1
    adb exec-out screencap -p > "$R/SCREENSHOTS/TEST-003_initial_screen.png" 2>/dev/null
    adb shell uiautomator dump /sdcard/window.xml > "$R/LOGS/uiautomator_003.txt" 2>&1
    adb pull /sdcard/window.xml "$R/UI_HIERARCHY/TEST-003_initial_screen.xml" \
      >> "$R/LOGS/uiautomator_003.txt" 2>&1
    adb logcat -d -v threadtime > "$R/LOGS/.logcat_app_raw.tmp" 2>&1
    grep -viE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|Bearer |token=|api[_-]?key=|password=' \
      "$R/LOGS/.logcat_app_raw.tmp" \
      | grep -iE 'getmimo|AndroidRuntime|FATAL|UnsatisfiedLink|Compose|ANR' \
      | head -300 > "$R/CRASH_AND_ERROR_LOGS.txt"
    rm -f "$R/LOGS/.logcat_app_raw.tmp"
    {
      echo "TEST-004..009 require UI interaction and an authorized test account."
      echo "This workflow stops at the authentication boundary."
      echo "No purchase, payment, TLS bypass, root or private-DB extraction performed."
      echo "A client-side call does not prove server acceptance; a screenshot does not prove backend behaviour."
    } > "$R/LESSON_FLOW_OBSERVATIONS.txt"
  fi
fi

echo "runtime_smoke_completed=yes"
exit 0
