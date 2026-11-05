#!/usr/bin/env bash
# =============================================================================
# MISSION 07 / STAGE 1 — LIVE RUNTIME ENVIRONMENT ASSESSMENT + FIRST
# DETERMINISTIC EXPERIMENT.
#
# H1: On the controlled Android 16 google_apis emulator, `adb root` yields UID 0
#     and read access to /data/data/com.getmimo, and a Frida server can attach
#     to the ORIGINAL app process to execute/hook its Java methods.
# H2: The statically recovered validators (qm.i.a, km.f.b,
#     LessonProgress.isSolvedCorrectly, network.a, te.c.b, gm.h.a) return the
#     predicted values when directly invoked at runtime with controlled inputs.
#
# Test state: fresh AVD, original APK SHA-verified, app installed but not yet
# onboarded. Capture pre-launch state, launch, one deterministic tap, capture
# post state + DB + runtime method results.
# =============================================================================
set +e
R=ANALYSIS/RUNTIME/MISSION_07
mkdir -p "$R"/{ENV,DB,FRIDA,LOGS,TRACES,UI,EXPERIMENTS}
APK="${RUNNER_TEMP:-/tmp}/MIMO_ORIGINAL.apk"
FRIDA_VER=17.25.2
SDK="${ANDROID_HOME:-${ANDROID_SDK_ROOT:-/usr/local/lib/android/sdk}}"
E="$EXPECTED_APK_SHA256"

echo "MISSION 07 STAGE 1 start $(date -u +%FT%TZ) run=$GITHUB_RUN_ID sha=$GITHUB_SHA" | tee "$R/LOGS/STAGE1_START.txt"

# ---- 0. SHA gate -----------------------------------------------------------
A=$(sha256sum "$APK" 2>/dev/null | cut -d' ' -f1)
S=$(stat -c %s "$APK" 2>/dev/null || echo 0)
{
  echo "apk_sha256=$A expected=$E"; echo "apk_bytes=$S expected=$EXPECTED_APK_BYTES"
} > "$R/LOGS/APK_SHA256.txt" 2>&1
if [ "$A" != "$E" ]; then echo "sha_gate=FAIL refusing runtime work" | tee -a "$R/LOGS/APK_SHA256.txt"; exit 1; fi
echo "sha_gate=SHA_MATCH_OK" >> "$R/LOGS/APK_SHA256.txt"

# ---- 1. Runtime environment / root assessment (actually attempted) ---------
{
  echo "MISSION 07 - RUNTIME ENVIRONMENT ASSESSMENT (device)"
  echo "timestamp_utc=$(date -u +%FT%TZ)"
  echo "run_id=$GITHUB_RUN_ID run_attempt=$GITHUB_RUN_ATTEMPT ref=$GITHUB_REF sha=$GITHUB_SHA"
  echo "== adb =="; "$SDK/platform-tools/adb" version | head -3
  echo "== device identity =="
  adb devices -l
  for P in ro.build.version.sdk ro.build.version.release ro.build.fingerprint ro.build.type \
           ro.debuggable ro.secure ro.product.cpu.abilist ro.dalvik.vm.native.bridge \
           selinux.getenforce sys.boot_completed; do
    echo "$P=$(adb shell getprop "$P" 2>&1)"
  done
  echo "== ROOT: adb root =="; adb root 2>&1; sleep 3; adb wait-for-device 2>&1
  echo "== ROOT: post-root identity =="
  adb shell id 2>&1
  adb shell 'ls -ld /data /data/data /data/data/com.getmimo 2>&1' 2>&1
  echo "== ROOT: su binary / setenforce =="
  adb shell 'command -v su; su 0 id' 2>&1 | head -6
  adb shell getenforce 2>&1
  adb shell setenforce 0 2>&1; echo "setenforce_exit=$?"
  adb shell getenforce 2>&1
  echo "== ROOT: run-as (app is debuggable=false) =="
  adb shell run-as com.getmimo id 2>&1 | head -5
  echo "== device sqlite3 / toybox =="
  adb shell 'command -v sqlite3; toybox --version; ls /system/bin/sqlite3 2>&1' 2>&1 | head -8
  echo "== process inspection =="
  adb shell 'ps -A | head -5' 2>&1
  echo "== available instrumentation-relevant binaries =="
  adb shell 'command -v am; command -v dumpsys; command -v logcat; command -v cmd; command -v gdbserver; command -v strace' 2>&1
  echo "== kernel / memory =="; adb shell 'cat /proc/version; head -3 /proc/meminfo' 2>&1
} > "$R/ENV/DEVICE_AND_ROOT.txt" 2>&1
cat "$R/ENV/DEVICE_AND_ROOT.txt"

# ---- 2. Install the ORIGINAL APK (fresh AVD) -------------------------------
{
  echo "== install =="; adb install -r "$APK" 2>&1
  echo "install_exit=$?"
  echo "== package =="; adb shell pm path com.getmimo 2>&1
  adb shell dumpsys package com.getmimo 2>&1 | grep -E 'versionName|versionCode|firstInstallTime|lastUpdateTime|dataDir|debuggable|allowBackup' | head -20
  echo "== launcher =="; adb shell cmd package resolve-activity --brief -c android.intent.category.LAUNCHER com.getmimo 2>&1 | tail -3
} > "$R/ENV/APK_INSTALL.txt" 2>&1
cat "$R/ENV/APK_INSTALL.txt"

# ---- 3. PRE-LAUNCH private sandbox snapshot --------------------------------
adb shell 'echo "== FULL SANDBOX TREE =="; find /data/data/com.getmimo -maxdepth 3 2>&1 | head -120; echo "== SELECTED COPY =="; mkdir -p /sdcard/m07_pre; for d in databases shared_prefs files datastore no_backup; do if [ -e /data/data/com.getmimo/$d ]; then cp -a /data/data/com.getmimo/$d /sdcard/m07_pre/ 2>/dev/null; fi; done; echo copy_exit=$?; find /sdcard/m07_pre -maxdepth 2 | head -80' > "$R/ENV/PRELAUNCH_TREE.txt" 2>&1
mkdir -p "$R/DB/PRE_LAUNCH"
adb pull /sdcard/m07_pre "$R/DB/PRE_LAUNCH" </dev/null >/dev/null 2>&1
python3 "$R/m07_db_snapshot.py" "$R/DB/PRE_LAUNCH/m07_pre" "A_FRESH_BEFORE_LAUNCH" "$R/DB/SNAPSHOT_A.json" 2>&1 | tee "$R/LOGS/DB_SNAPSHOT_A.txt"

# ---- 4. Launch app ---------------------------------------------------------
adb logcat -c 2>/dev/null
adb shell monkey -p com.getmimo -c android.intent.category.LAUNCHER 1 </dev/null > "$R/LOGS/LAUNCH.txt" 2>&1
sleep 22
{
  echo "== process =="; adb shell 'pidof com.getmimo; ps -A | grep mimo' 2>&1
  echo "== resumed activity =="; adb shell dumpsys activity activities 2>&1 | grep -E 'mResumedActivity|topResumedActivity|mCurrentFocus' | head -5
  echo "== threads =="; PID=$(adb shell pidof com.getmimo | tr -d '\r'); echo "pid=$PID"; adb shell "ls /proc/$PID/task 2>/dev/null | wc -l" 2>&1
} > "$R/ENV/POST_LAUNCH_PROCESS.txt" 2>&1
cat "$R/ENV/POST_LAUNCH_PROCESS.txt"
adb shell uiautomator dump /sdcard/m07_step00.xml </dev/null >/dev/null 2>&1
adb pull /sdcard/m07_step00.xml "$R/UI/STEP-00.xml" </dev/null >/dev/null 2>&1
adb exec-out screencap -p > "$R/UI/STEP-00.png" 2>/dev/null || true

# ---- 5. Frida server installation (actually attempted) --------------------
{
  echo "MISSION 07 - FRIDA INSTALLATION"
  echo "timestamp_utc=$(date -u +%FT%TZ)"
  echo "== host python / pip =="; python3 --version; python3 -m pip --version
  python3 -m pip install --quiet "frida==$FRIDA_VER" "frida-tools" 2>&1 | tail -8
  echo "pip_exit=$?"
  python3 -c 'import frida; print("frida_python_version="+frida.__version__)' 2>&1
  echo "== download frida-server =="
  U="https://github.com/frida/frida/releases/download/$FRIDA_VER/frida-server-$FRIDA_VER-android-x86_64.xz"
  curl -fL --retry 2 --max-time 600 -o "${RUNNER_TEMP:-/tmp}/frida-server.xz" "$U" 2>&1 | tail -3
  echo "curl_exit=$? bytes=$(stat -c %s "${RUNNER_TEMP:-/tmp}/frida-server.xz" 2>/dev/null || echo 0)"
  xz -dkf "${RUNNER_TEMP:-/tmp}/frida-server.xz" 2>&1; echo "xz_exit=$?"
  FS="${RUNNER_TEMP:-/tmp}/frida-server"
  ls -l "$FS" 2>&1
  echo "== push + start as root =="
  adb push "$FS" /data/local/tmp/frida-server 2>&1
  adb shell chmod 755 /data/local/tmp/frida-server 2>&1
  adb shell 'getprop ro.product.cpu.abi; file /data/local/tmp/frida-server 2>/dev/null' 2>&1
  adb shell 'pkill -f frida-server 2>/dev/null; nohup /data/local/tmp/frida-server >/data/local/tmp/frida-server.log 2>&1 & echo started=$!' 2>&1
  sleep 5
  adb shell 'ps -A | grep frida' 2>&1
  adb shell 'cat /data/local/tmp/frida-server.log' 2>&1 | head -20
  echo "== frida-ps -U =="
  frida-ps -U 2>&1 | head -25
  echo "frida_ps_exit=$?"
} > "$R/FRIDA/INSTALL.txt" 2>&1
cat "$R/FRIDA/INSTALL.txt"

# ---- 6. Deterministic experiment: direct runtime method invocation --------
# Keep the Frida session alive for 50 s while one controlled UI tap executes.
python3 "$R/m07_frida_driver.py" "$R/m07_frida_stage1.js" "$R/TRACES/STAGE1_FRIDA.jsonl" 50 \
  > "$R/FRIDA/DRIVER.log" 2>&1 &
DRIVER_PID=$!
sleep 12
# One controlled operation: STEP-01 "Get started" tap (exact M05 run-003 coords).
adb shell input tap 540 2049 </dev/null > "$R/EXPERIMENTS/E1_TAP_01.txt" 2>&1
sleep 8
adb shell uiautomator dump /sdcard/m07_step01.xml </dev/null >/dev/null 2>&1
adb pull /sdcard/m07_step01.xml "$R/UI/STEP-01.xml" </dev/null >/dev/null 2>&1
wait "$DRIVER_PID" 2>/dev/null
cat "$R/FRIDA/DRIVER.log" | tail -60
echo "frida_messages=$(wc -l < "$R/TRACES/STAGE1_FRIDA.jsonl" 2>/dev/null || echo 0)" | tee "$R/LOGS/FRIDA_MESSAGE_COUNT.txt"

# ---- 7. POST-LAUNCH private sandbox snapshot + real SQLite ----------------
adb shell 'echo "== FULL SANDBOX TREE =="; find /data/data/com.getmimo -maxdepth 3 2>&1 | head -140; echo "== SELECTED COPY =="; mkdir -p /sdcard/m07_post; for d in databases shared_prefs files datastore no_backup; do if [ -e /data/data/com.getmimo/$d ]; then cp -a /data/data/com.getmimo/$d /sdcard/m07_post/ 2>/dev/null; fi; done; echo copy_exit=$?; find /sdcard/m07_post -maxdepth 2 | head -100' > "$R/ENV/POSTLAUNCH_TREE.txt" 2>&1
mkdir -p "$R/DB/POST_LAUNCH"
adb pull /sdcard/m07_post "$R/DB/POST_LAUNCH" </dev/null >/dev/null 2>&1
python3 "$R/m07_db_snapshot.py" "$R/DB/POST_LAUNCH/m07_post" "B_AFTER_LAUNCH_AND_ONE_TAP" "$R/DB/SNAPSHOT_B.json" 2>&1 | tee "$R/LOGS/DB_SNAPSHOT_B.txt"
# Consistent, root-level SQLite .backup of every database (device sqlite3 CLI is
# present and measured). This avoids reading a torn WAL/journal copy.
mkdir -p "$R/DB/CONSISTENT_BACKUPS"
{
  echo "MISSION 07 - device SQLite inventory + consistent backups"
  adb shell 'ls -la /data/data/com.getmimo/databases/' 2>&1
  for F in $(adb shell 'ls /data/data/com.getmimo/databases/' 2>/dev/null | tr -d '\r'); do
    case "$F" in *-wal|*-shm|*-journal) continue;; esac
    echo "--- $F ---"
    adb shell "sqlite3 /data/data/com.getmimo/databases/$F '.backup /sdcard/m07_consistent.db'" 2>&1
    echo "backup_exit=$?"
    adb pull /sdcard/m07_consistent.db "$R/DB/CONSISTENT_BACKUPS/$F" </dev/null 2>&1 | tail -2
    adb shell "sqlite3 /data/data/com.getmimo/databases/$F 'SELECT type,name,sql FROM sqlite_master ORDER BY type,name;'" 2>&1 | head -60
  done
} > "$R/DB/DEVICE_SQLITE_INVENTORY.txt" 2>&1
python3 "$R/m07_db_snapshot.py" "$R/DB/CONSISTENT_BACKUPS" "B_CONSISTENT_SQLITE_BACKUP" "$R/DB/SNAPSHOT_B_CONSISTENT.json" 2>&1 | tee -a "$R/LOGS/DB_SNAPSHOT_B.txt"
{
  echo "== WAL / SHM files present =="
  find "$R/DB/POST_LAUNCH" -type f | grep -E '\-wal|\-shm|\.journal' | head -30
  echo "== DataStore / SharedPreferences raw text (first 200 lines) =="
  for F in $(find "$R/DB/POST_LAUNCH" -type f \( -path '*shared_prefs*' -o -path '*datastore*' -o -name '*.preferences_pb' \) | head -20); do
    echo "--- $F ($(stat -c %s "$F") bytes) ---"; strings "$F" 2>/dev/null | head -40
  done
} > "$R/DB/PREFS_AND_DATASTORE.txt" 2>&1

# ---- 8. Logcat + summary ---------------------------------------------------
adb logcat -d -t 4000 > "$R/LOGS/LOGCAT_STAGE1.txt" 2>&1
python3 - > "$R/LOGS/STAGE1_SUMMARY.json" <<'PY'
import json, pathlib, re
R=pathlib.Path('ANALYSIS/RUNTIME/MISSION_07')
def txt(p):
    try: return (R/p).read_text(errors='replace')
    except Exception: return ''
def has(p,s): return s in txt(p)
env=txt('ENV/DEVICE_AND_ROOT.txt'); ins=txt('FRIDA/INSTALL.txt')
tr=txt('TRACES/STAGE1_FRIDA.jsonl')
print(json.dumps({
 'document':'MISSION 07 STAGE 1 — runtime environment + first deterministic experiment',
 'classification':'VERIFIED_RUNTIME (measurements) / INFERRED (interpretation)',
 'apk_sha256':'48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a',
 'hypotheses':{
   'H1_root_adb':'adb root succeeded' if re.search(r'^uid=0\(', env, re.M) else 'UNKNOWN',
   'H1_private_sandbox':'readable' if 'm07_post' in txt('ENV/POSTLAUNCH_TREE.txt') else 'UNKNOWN',
   'H1_frida_attach':'ok' if 'script loaded' in txt('FRIDA/DRIVER.log') else 'UNKNOWN',
   'H1_frida_ps':'ok' if 'frida_ps_exit=0' in ins else 'UNKNOWN'},
 'counts':{'frida_messages':len(tr.splitlines()),
           'frida_calls':tr.count('"kind":"call"'),
           'frida_entries':tr.count('"kind":"entry"'),
           'frida_hook_installed':tr.count('"kind":"hook_installed"'),
           'frida_errors':tr.count('"kind":"call_error"')+tr.count('"kind":"experiment_error"')+tr.count('"kind":"hook_error"')},
 'evidence_files':[str(p) for p in sorted(R.rglob('*')) if p.is_file()],
 'server_confirmed':0
}, indent=1, ensure_ascii=False))
PY
echo "MISSION 07 STAGE 1 complete $(date -u +%FT%TZ)" | tee -a "$R/LOGS/STAGE1_START.txt"
