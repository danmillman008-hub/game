#!/usr/bin/env bash
# Controlled fresh-install comparison. Runs inside android-emulator-runner.
set -u
OUT="$RUNNER_TEMP/startup-probe"; mkdir -p "$OUT"
adb shell svc wifi disable || true
adb shell svc data disable || true
for variant in original resigned repack; do
  echo "===== $variant =====" | tee -a "$OUT/results.txt"
  adb uninstall com.getmimo >/dev/null 2>&1 || true
  if ! adb install -r "$RUNNER_TEMP/$variant.apk" >>"$OUT/results.txt" 2>&1; then
    echo 'INSTALL_FAILED' | tee -a "$OUT/results.txt"; continue
  fi
  adb logcat -c
  adb shell monkey -p com.getmimo -c android.intent.category.LAUNCHER 1 >>"$OUT/results.txt" 2>&1
  for seconds in 3 20 60; do
    if [ "$seconds" = 3 ]; then sleep 3; elif [ "$seconds" = 20 ]; then sleep 17; else sleep 40; fi
    echo "pid=$(adb shell pidof com.getmimo || true)" >>"$OUT/results.txt"
    adb logcat -d -b crash -v brief > "$OUT/${variant}_${seconds}_crash.txt" || true
    adb logcat -d -v brief | grep -E -i -A 12 'FATAL EXCEPTION|ANR in com.getmimo|Process: com.getmimo|VerifyError|Fatal signal|Force finishing|Unable to start activity|com.getmimo.*(crash|died|fatal|error|exception)' > "$OUT/${variant}_${seconds}_errors.txt" || true
    echo "-- after ${seconds}s --" >>"$OUT/results.txt"
    adb shell dumpsys activity activities | grep -E 'mResumedActivity|topResumedActivity|mCurrentFocus' >>"$OUT/results.txt" || true
    adb shell uiautomator dump /sdcard/window.xml >/dev/null 2>&1 || true
    adb exec-out cat /sdcard/window.xml > "$OUT/${variant}_${seconds}.xml" 2>/dev/null || true
    adb exec-out screencap -p > "$OUT/${variant}_${seconds}.png" || true
  done
  # Fresh emulator without personal account: record crash signatures, not full logs.
  adb logcat -d -v brief | grep -E -A 18 'FATAL EXCEPTION|ANR in com.getmimo|Process: com.getmimo' > "$OUT/${variant}_errors.txt" || true
done
cat "$OUT/results.txt"
