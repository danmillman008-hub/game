#!/usr/bin/env bash
# =============================================================================
# MISSION 07 / STAGE 2 — REAL ANSWER VALIDATION + ROOM STATE FORENSICS
#
# H: a wrong tap (Q) and a correct tap (D) in the shipped lesson 151403 execute
#    different runtime paths (onLessonRun$1 -> X/V), produce distinct feedback
#    LiveData objects, and write distinct `lesson_progress` rows into mimo.db.
#    A cold start with NO network restores that local state.
#
# Prepared state: fresh AVD, ORIGINAL APK SHA-gated, onboarding experiment
# seeded to "original", app never answered before. Comparable states A..I.
# One controlled operation per snapshot. No server reconstruction.
# =============================================================================
set +e
R=ANALYSIS/RUNTIME/MISSION_07
mkdir -p "$R"/{ENV,DB,FRIDA,LOGS,TRACES,UI,EXPERIMENTS}
APK="${RUNNER_TEMP:-/tmp}/MIMO_ORIGINAL.apk"
E="$EXPECTED_APK_SHA256"
T="$R/EXPERIMENTS/STAGE2_TRACE.txt"
: > "$T"
log(){ echo "[$(date -u +%FT%TZ)] $*" | tee -a "$T"; }
SDK="${ANDROID_HOME:-${ANDROID_SDK_ROOT:-/usr/local/lib/android/sdk}}"
FRIDA_VER=17.25.2

log "MISSION 07 STAGE 2 START run=$GITHUB_RUN_ID sha=$GITHUB_SHA"
A=$(sha256sum "$APK" 2>/dev/null | cut -d' ' -f1)
[ "$A" = "$E" ] || { log "sha_gate=FAIL $A"; exit 1; }
log "sha_gate=SHA_MATCH_OK bytes=$(stat -c %s "$APK")"

# ---- root + environment (measured, not assumed) ---------------------------
adb root >/dev/null 2>&1; sleep 3; adb wait-for-device >/dev/null 2>&1
adb shell setenforce 0 >/dev/null 2>&1
{
  echo "timestamp_utc=$(date -u +%FT%TZ) run_id=$GITHUB_RUN_ID"
  echo "root_id=$(adb shell id 2>&1)"; echo "selinux=$(adb shell getenforce 2>&1)"
  adb shell getprop ro.build.fingerprint; adb shell getprop ro.product.cpu.abilist
  adb shell 'command -v sqlite3; command -v strace'
} > "$R/ENV/STAGE2_ROOT.txt" 2>&1

# ---- install original, seed deterministic onboarding experiment ------------
adb install -r "$APK" > "$R/ENV/STAGE2_INSTALL.txt" 2>&1
# Root-controlled state preparation: pin the local onboarding experiment to the
# "original" branch observed in M05 run 42003884423 (avoids A/B drift).
adb shell 'mkdir -p /data/data/com.getmimo/shared_prefs; printf "%s\n" "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\" ?>" "<map>" "    <string name=\"experiment_adapted_onboarding_android_local\">original</string>" "</map>" > /data/data/com.getmimo/shared_prefs/experiments.xml; U=$(stat -c %u:%g /data/data/com.getmimo); chown -R $U /data/data/com.getmimo/shared_prefs; chmod 660 /data/data/com.getmimo/shared_prefs/experiments.xml' >> "$R/ENV/STAGE2_INSTALL.txt" 2>&1
adb shell cat /data/data/com.getmimo/shared_prefs/experiments.xml >> "$R/ENV/STAGE2_INSTALL.txt" 2>&1
adb shell monkey -p com.getmimo -c android.intent.category.LAUNCHER 1 > "$R/LOGS/STAGE2_LAUNCH.txt" 2>&1
sleep 20
log "launch_pid=$(adb shell pidof com.getmimo | tr -d '\r')"
bash "$R/m07_snapshot.sh" A_BEFORE_ONBOARDING >/dev/null 2>&1
log "snapshot=A_BEFORE_ONBOARDING"

# ---- Frida server (measured install; attach by PID) ------------------------
{
  python3 -m pip install --quiet "frida==$FRIDA_VER" "frida-tools==14.11.0" 2>&1 | tail -5
  python3 -c 'import frida;print("frida="+frida.__version__)'
  U="https://github.com/frida/frida/releases/download/$FRIDA_VER/frida-server-$FRIDA_VER-android-x86_64.xz"
  curl -fL --retry 2 --max-time 600 -o "${RUNNER_TEMP:-/tmp}/frida-server.xz" "$U" >/dev/null 2>&1
  xz -dkf "${RUNNER_TEMP:-/tmp}/frida-server.xz" >/dev/null 2>&1
  adb push "${RUNNER_TEMP:-/tmp}/frida-server" /data/local/tmp/frida-server 2>&1 | tail -1
  adb shell chmod 755 /data/local/tmp/frida-server
  adb shell '/data/local/tmp/frida-server --help' 2>&1 | head -20
  sleep 3
  adb shell 'ps -A | grep frida' 2>&1
  frida-ps -U 2>&1 | grep -i mimo
} > "$R/FRIDA/STAGE2_SETUP.txt" 2>&1
log "frida_setup_done"

# frida-server is kept alive by a HOST-SIDE `adb shell` process (a bare
# `nohup ... &` inside adb shell is reaped when that shell session exits).
( adb shell /data/local/tmp/frida-server > "$R/FRIDA/STAGE2_SERVER.log" 2>&1 ) &
FS_HOST_PID=$!
sleep 6
frida-ps -U | grep -i mimo >> "$R/FRIDA/STAGE2_SETUP.txt" 2>&1
python3 "$R/m07_frida_driver.py" "$R/m07_frida_stage2.js" "$R/TRACES/STAGE2_ONLINE.jsonl" 300 \
  > "$R/FRIDA/STAGE2_ONLINE_DRIVER.log" 2>&1 &
DRIVER=$!
sleep 10

# ---- deterministic bounded onboarding chain (M05 run-003 replay) -----------
# choose_tap.py is the SAME chooser used by M05 run 42003884423. A bounded loop
# plus "two identical consecutive hierarchies" stop rule reproduces STEP-01..24.
AVOID=""
STATE="$R/LOGS/.stage2_state"; : > "$STATE"
BASE="$R/UI/A_BEFORE_ONBOARDING.xml"
LESSON_REACHED=0
for I in $(seq 1 34); do
  N=$(printf 'NAV-%02d' "$I")
  adb shell uiautomator dump /sdcard/m07_nav.xml </dev/null >/dev/null 2>&1
  adb pull /sdcard/m07_nav.xml "$R/UI/$N.xml" </dev/null >/dev/null 2>&1
  BASE="$R/UI/$N.xml"
  # Detect the shipped lesson by its three clickable 1-letter options + CTA.
  OPTS=$(python3 ANALYSIS/RUNTIME/MISSION_05/lesson_options.py "$BASE" 2>/dev/null | grep -c OPTION)
  if [ "$OPTS" -ge 3 ]; then log "$N lesson_reached options=$OPTS"; LESSON_REACHED=1; break; fi
  TAP=$(python3 "$R/m07_tap_target.py" "$BASE" "" "$AVOID" 2>/dev/null | head -1)
  log "$N choose_tap=$TAP"
  case "$TAP" in NONE*|'') log "$N stop_reason=$TAP"; sleep 4; continue;; esac
  X=$(printf '%s' "$TAP" | awk '{print $1}'); Y=$(printf '%s' "$TAP" | awk '{print $2}')
  log "$N action=input_tap x=$X y=$Y target=$(printf '%s' "$TAP" | awk '{print $3}')"
  adb shell input tap "$X" "$Y" </dev/null >> "$T" 2>&1
  AVOID="$X,$Y"
  sleep 3
  NH=$(sha256sum "$BASE" 2>/dev/null | cut -d' ' -f1)
  PH=$(head -1 "$STATE" 2>/dev/null)
  if [ "$NH" = "$PH" ]; then NC=$(( $(tail -1 "$STATE" 2>/dev/null || echo 0) + 1 )); else NC=0; AVOID=""; fi
  printf '%s\n%s\n' "$NH" "$NC" > "$STATE"
  if [ "$NC" -ge 4 ]; then log "$N stop_reason=four_identical_hierarchies"; break; fi
done
log "onboarding_finished lesson_reached=$LESSON_REACHED"
bash "$R/m07_snapshot.sh" C_LESSON_BEFORE_ANSWER >/dev/null 2>&1
log "snapshot=C_LESSON_BEFORE_ANSWER"
python3 ANALYSIS/RUNTIME/MISSION_05/lesson_options.py "$R/UI/C_LESSON_BEFORE_ANSWER.xml" > "$R/EXPERIMENTS/C_LESSON_OPTIONS.txt" 2>&1
cat "$R/EXPERIMENTS/C_LESSON_OPTIONS.txt" >> "$T"

# ---- E1: one controlled WRONG answer (Q) ----------------------------------
QX=$(awk '$3=="OPTION"&&$4=="Q"{print $1}' "$R/EXPERIMENTS/C_LESSON_OPTIONS.txt" | head -1)
QY=$(awk '$3=="OPTION"&&$4=="Q"{print $2}' "$R/EXPERIMENTS/C_LESSON_OPTIONS.txt" | head -1)
if [ -n "$QX" ]; then
  log "E1_WRONG action=input_tap x=$QX y=$QY option=Q"
  adb shell input tap "$QX" "$QY" </dev/null >> "$T" 2>&1
  sleep 6
  bash "$R/m07_snapshot.sh" D_AFTER_WRONG >/dev/null 2>&1
  log "snapshot=D_AFTER_WRONG"
else log "E1_WRONG skipped: no Q option"; fi

# ---- E2: one controlled CORRECT answer (D) -------------------------------
DX=$(awk '$3=="OPTION"&&$4=="D"{print $1}' "$R/EXPERIMENTS/C_LESSON_OPTIONS.txt" | head -1)
DY=$(awk '$3=="OPTION"&&$4=="D"{print $2}' "$R/EXPERIMENTS/C_LESSON_OPTIONS.txt" | head -1)
if [ -n "$DX" ]; then
  log "E2_CORRECT action=input_tap x=$DX y=$DY option=D"
  adb shell input tap "$DX" "$DY" </dev/null >> "$T" 2>&1
  sleep 6
  bash "$R/m07_snapshot.sh" E_AFTER_CORRECT >/dev/null 2>&1
  log "snapshot=E_AFTER_CORRECT"
else log "E2_CORRECT skipped: no D option"; fi

# ---- E3: advance to next lesson (Continue CTA) ----------------------------
CX=$(awk '$3=="CTA"{print $1}' "$R/EXPERIMENTS/C_LESSON_OPTIONS.txt" | head -1)
CY=$(awk '$3=="CTA"{print $2}' "$R/EXPERIMENTS/C_LESSON_OPTIONS.txt" | head -1)
if [ -n "$CX" ]; then
  log "E3_CONTINUE action=input_tap x=$CX y=$CY cta=Continue"
  adb shell input tap "$CX" "$CY" </dev/null >> "$T" 2>&1
  sleep 7
  bash "$R/m07_snapshot.sh" F_AFTER_CONTINUE >/dev/null 2>&1
  log "snapshot=F_AFTER_CONTINUE"
fi

# ---- collect online Frida session ------------------------------------------
wait "$DRIVER" 2>/dev/null
log "online_frida_messages=$(wc -l < "$R/TRACES/STAGE2_ONLINE.jsonl" 2>/dev/null || echo 0)"
adb logcat -d -t 6000 > "$R/LOGS/STAGE2_ONLINE_LOGCAT.txt" 2>&1

# ---- G: genuine offline + force-stop restoration --------------------------
{
  echo "MISSION 07 STAGE 2 — OFFLINE / RESTORATION PROBE"
  echo "timestamp_utc=$(date -u +%FT%TZ)"
  echo "== network BEFORE =="; adb shell dumpsys connectivity 2>/dev/null | tr -d '\r' | grep -m3 -E 'Active default network|NetworkAgentInfo' | cut -c1-220
  adb shell svc wifi disable 2>&1 | tr -d '\r'
  adb shell svc data disable 2>&1 | tr -d '\r'
  adb shell cmd connectivity airplane-mode enable 2>&1 | tr -d '\r'
  sleep 4
  echo "== network AFTER (isolation proof) =="
  adb shell dumpsys connectivity 2>/dev/null | tr -d '\r' | grep -m3 -E 'Active default network|NetworkAgentInfo' | cut -c1-220
  echo "== ping AFTER =="; adb shell ping -c 1 -W 2 8.8.8.8 2>&1 | tr -d '\r' | head -5
  echo "== getprop airplane =="; adb shell settings get global airplane_mode_on 2>&1
} > "$R/EXPERIMENTS/G_OFFLINE_ISOLATION.txt" 2>&1
bash "$R/m07_snapshot.sh" G_BEFORE_FORCESTOP >/dev/null 2>&1
log "snapshot=G_BEFORE_FORCESTOP"
adb shell am force-stop com.getmimo >> "$R/EXPERIMENTS/G_OFFLINE_ISOLATION.txt" 2>&1
sleep 3
adb shell am start -n com.getmimo/.ui.SplashActivity_default >> "$R/EXPERIMENTS/G_OFFLINE_ISOLATION.txt" 2>&1
sleep 20
# The same host-side frida-server is still alive across app force-stop.
frida-ps -U | grep -i mimo >> "$R/FRIDA/STAGE2_SETUP.txt" 2>&1
python3 "$R/m07_frida_driver.py" "$R/m07_frida_stage2.js" "$R/TRACES/STAGE2_OFFLINE.jsonl" 100 \
  > "$R/FRIDA/STAGE2_OFFLINE_DRIVER.log" 2>&1 &
DRIVER2=$!
sleep 8
bash "$R/m07_snapshot.sh" H_OFFLINE_COLD_START >/dev/null 2>&1
log "snapshot=H_OFFLINE_COLD_START"
# bounded offline navigation: Skip / practice / Start practicing / lesson
AVOID=""
for I in $(seq 1 8); do
  N=$(printf 'OFFNAV-%02d' "$I")
  adb shell uiautomator dump /sdcard/m07_nav.xml </dev/null >/dev/null 2>&1
  adb pull /sdcard/m07_nav.xml "$R/UI/$N.xml" </dev/null >/dev/null 2>&1
  TAP=$(python3 "$R/m07_tap_target.py" "$R/UI/$N.xml" "" "$AVOID" 2>/dev/null | head -1)
  log "$N choose_tap=$TAP"
  case "$TAP" in NONE*|'') break;; esac
  X=$(printf '%s' "$TAP" | awk '{print $1}'); Y=$(printf '%s' "$TAP" | awk '{print $2}')
  adb shell input tap "$X" "$Y" </dev/null >> "$T" 2>&1
  AVOID="$X,$Y"; sleep 4
done
bash "$R/m07_snapshot.sh" I_OFFLINE_RESTORED >/dev/null 2>&1
log "snapshot=I_OFFLINE_RESTORED"
wait "$DRIVER2" 2>/dev/null
adb logcat -d -t 6000 > "$R/LOGS/STAGE2_OFFLINE_LOGCAT.txt" 2>&1

# ---- summary ---------------------------------------------------------------
python3 - "$R" > "$R/LOGS/STAGE2_SUMMARY.json" <<'PY'
import json,pathlib,sys,os
R=pathlib.Path(sys.argv[1])
def n(p):
    try:return sum(1 for _ in (R/p).open(errors='replace'))
    except Exception:return 0
def j(p):
    try:return json.loads((R/p).read_text(errors='replace'))
    except Exception:return {}
snaps={}
for f in sorted((R/'DB').glob('SNAPSHOT_*.json')):
    d=j('DB/'+f.name)
    snaps[f.stem.replace('SNAPSHOT_','')]={
      'files':len(d.get('files',[])),'databases':len(d.get('databases',[])),
      'tables':[(x['path'],[(t.get('name'),t.get('row_count')) for t in x.get('tables',[])]) for x in d.get('databases',[])]}
print(json.dumps({'document':'MISSION 07 STAGE 2 — real answer validation + Room state forensics',
 'classification':'VERIFIED_RUNTIME (measurements); interpretation INFERRED',
 'apk_sha256':'48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a',
 'online_frida_messages':n('TRACES/STAGE2_ONLINE.jsonl'),
 'offline_frida_messages':n('TRACES/STAGE2_OFFLINE.jsonl'),
 'snapshots':snaps,'server_confirmed':0}, indent=1, ensure_ascii=False))
PY
cat "$R/LOGS/STAGE2_SUMMARY.json"
log "MISSION 07 STAGE 2 COMPLETE"
