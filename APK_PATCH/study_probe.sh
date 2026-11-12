#!/usr/bin/env bash
# Two diagnostic builds: no credentials and network disabled. UI dumps include
# only fresh emulator test data. No device-private state is committed.
set -u
O="$RUNNER_TEMP/study-probe"; mkdir -p "$O"
adb shell svc wifi disable || true; adb shell svc data disable || true
for v in direct_guest unmodified_guest; do
  adb uninstall com.getmimo >/dev/null 2>&1 || true
  adb install -r "$RUNNER_TEMP/$v.apk" >> "$O/summary.txt" 2>&1 || continue
  adb logcat -c
  adb shell monkey -p com.getmimo -c android.intent.category.LAUNCHER 1 >/dev/null 2>&1
  sleep 15
  for i in $(seq -w 0 30); do
    A=$(adb shell dumpsys activity activities | grep topResumedActivity | head -1)
    echo "$v step=$i pid=$(adb shell pidof com.getmimo || true) $A" >> "$O/summary.txt"
    adb shell uiautomator dump /sdcard/study.xml >/dev/null 2>&1 || true
    adb exec-out cat /sdcard/study.xml > "$O/${v}_$i.xml" 2>/dev/null || true
    adb exec-out screencap -p > "$O/${v}_$i.png" 2>/dev/null || true
    if [ "$v" = direct_guest ]; then break; fi
    T=$(python3 ANALYSIS/RUNTIME/MISSION_05/choose_tap.py "$O/${v}_$i.xml" 2>/dev/null | head -1)
    echo "$v step=$i target=$T" >> "$O/summary.txt"
    set -- $T
    if [ "${1:-NONE}" = NONE ] || [ -z "${2:-}" ]; then break; fi
    adb shell input tap "$1" "$2"; sleep 4
  done
  adb logcat -d -b crash -v brief > "$O/${v}_crash.txt" || true
  adb shell am force-stop com.getmimo
  adb shell monkey -p com.getmimo -c android.intent.category.LAUNCHER 1 >/dev/null 2>&1; sleep 12
  echo "$v restart pid=$(adb shell pidof com.getmimo || true) $(adb shell dumpsys activity activities | grep topResumedActivity | head -1)" >> "$O/summary.txt"
  adb shell uiautomator dump /sdcard/study.xml >/dev/null 2>&1 || true
  adb exec-out cat /sdcard/study.xml > "$O/${v}_restart.xml" 2>/dev/null || true
done
cat "$O/summary.txt"
