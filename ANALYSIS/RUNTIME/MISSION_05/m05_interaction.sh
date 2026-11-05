#!/usr/bin/env bash
# MISSION 05 - controlled RUNTIME interaction on the ORIGINAL Mimo 9.35.
# Reuses the proven M04 launch procedure, then taps through real onboarding /
# learning states, capturing ORIGINAL PNG + uiautomator XML at every state.
# Stops at the authentication boundary. No invented credentials, no auth bypass,
# no fake server responses, no root, no private DB extraction, no purchases.
set +e
R=ANALYSIS/RUNTIME/MISSION_05
APK="${RUNNER_TEMP:-/tmp}/MIMO_ORIGINAL.apk"
mkdir -p "$R/SCREENSHOTS" "$R/UI_HIERARCHY" "$R/LOGS" "$R/RUNTIME"
TRACE="$R/LOGS/INTERACTION_TRACE.txt"
STATES="$R/RUNTIME/STATES.jsonl"
: > "$TRACE"; : > "$STATES"
TS=$(date -u +%FT%TZ)
log(){ echo "[$(date -u +%FT%TZ)] $*" | tee -a "$TRACE"; }
log "MISSION 05 runtime interaction START run_id=$GITHUB_RUN_ID sha=$GITHUB_SHA ts=$TS"

# ---- 0. SHA gate ---------------------------------------------------------
E="${EXPECTED_APK_SHA256:-48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a}"
B="${EXPECTED_APK_BYTES:-142353499}"
A=$(sha256sum "$APK" 2>/dev/null | cut -d' ' -f1)
SZ=$(stat -c %s "$APK" 2>/dev/null || echo 0)
log "apk_sha=$A bytes=$SZ expected_sha=$E expected_bytes=$B"
if [ "$A" != "$E" ] || [ "$SZ" != "$B" ]; then
  log "SHA_MISMATCH -> refusing install; no substitute APK used."
  exit 1
fi
log "sha_gate=SHA_MATCH_OK"

# ---- 1. Device + install (real package discovery, no guessing) -----------
{
  echo "MISSION 05 - DEVICE / INSTALL"
  echo "timestamp_utc=$TS run_id=$GITHUB_RUN_ID"
  adb devices -l 2>&1 | tr -d '\r'
  for P in ro.build.version.sdk ro.build.version.release ro.build.fingerprint \
           ro.product.model ro.product.cpu.abilist ro.dalvik.vm.native.bridge; do
    echo "$P=$(adb shell getprop "$P" 2>/dev/null | tr -d '\r')"
  done
  echo "== adb install -r MIMO_ORIGINAL.apk =="
  adb install -r "$APK" > /tmp/m05_install.out 2>&1
  echo "install_exit=$?"
  cat /tmp/m05_install.out | tr -d '\r'
  echo "== pm list packages -3 =="
  adb shell pm list packages -3 2>&1 | tr -d '\r'
  echo "== pm path / version =="
  adb shell dumpsys package com.getmimo 2>/dev/null | tr -d '\r' \
    | grep -iE 'versionName|versionCode|primaryCpuAbi|nativeLibraryDir' | head -10
} > "$R/DEVICE_PROPERTIES.txt" 2>&1
PKG=$(adb shell pm list packages -3 2>/dev/null | tr -d '\r' | grep -i '^package:.*mimo' | head -1 | cut -d: -f2)
[ -z "$PKG" ] && PKG=com.getmimo
log "discovered_package=$PKG"

# ---- 2. Launch (M04 procedure, no HOME after launch) ---------------------
adb logcat -c >/dev/null 2>&1
LAUNCH=$(adb shell cmd package resolve-activity --brief -c android.intent.category.LAUNCHER "$PKG" 2>/dev/null | tr -d '\r' | tail -1)
log "resolved_launcher=$LAUNCH"
adb shell am start -n "$LAUNCH" >> "$R/LOGS/APPLICATION_LAUNCH.txt" 2>&1
log "am_start_exit=$?"
sleep 3
adb exec-out screencap -p > "$R/SCREENSHOTS/TEST-002_splash.png" 2>/dev/null
sleep 16
F0=$(adb shell dumpsys window 2>/dev/null | tr -d '\r' | grep -m1 -i 'mCurrentFocus')
case "$F0" in
  *"$PKG"*) log "initial_focus_on_mimo=yes" ;;
  *) log "initial_focus_on_mimo=no focus=$F0"
     adb shell input keyevent 4 >/dev/null 2>&1
     adb shell monkey -p "$PKG" 1 >/dev/null 2>&1
     sleep 12 ;;
esac
# dismiss a possible system ANR dialog by tapping its real "Wait" bounds
for ATT in 1 2 3; do
  adb shell uiautomator dump --compressed /sdcard/window.xml >/dev/null 2>&1
  adb pull /sdcard/window.xml "$R/UI_HIERARCHY/.anr.xml" >/dev/null 2>&1
  NODE=$(grep -o '<node[^>]*aerr_wait[^>]*>' "$R/UI_HIERARCHY/.anr.xml" 2>/dev/null | head -1)
  ANR_B=$(printf '%s' "$NODE" | grep -o 'bounds="\[[0-9]*,[0-9]*\]\[[0-9]*,[0-9]*\]"' | head -1)
  if [ -n "$ANR_B" ]; then
    NUMS=$(printf '%s' "$ANR_B" | grep -oE '[0-9]+' | tr '\n' ' '); set -- $NUMS
    CX=$(( ( $1 + $3 ) / 2 )); CY=$(( ( $2 + $4 ) / 2 ))
    log "anr_dialog_attempt_$ATT present tap=$CX,$CY"
    adb shell input tap "$CX" "$CY" >/dev/null 2>&1; sleep 3
  else
    log "anr_dialog_attempt_$ATT none"; break
  fi
done
rm -f "$R/UI_HIERARCHY/.anr.xml"
log "pid=$(adb shell pidof "$PKG" 2>/dev/null | tr -d '\r')"

# ---- 3. State capture helper ---------------------------------------------
LAST_XML=""
NO_CHANGE=0
AVOID=""
capture(){
  N="$1"; LABEL="$2"
  XML="$R/UI_HIERARCHY/$N.xml"
  PNG="$R/SCREENSHOTS/$N.png"
  timeout 60 adb shell uiautomator dump --compressed /sdcard/window.xml >"$R/LOGS/uiautomator_$N.txt" 2>&1
  D=$?
  if [ "$D" -ne 0 ]; then sleep 4; timeout 60 adb shell uiautomator dump --compressed /sdcard/window.xml >>"$R/LOGS/uiautomator_$N.txt" 2>&1; fi
  adb pull /sdcard/window.xml "$XML" >/dev/null 2>&1
  timeout 60 adb exec-out screencap -p > "$PNG" 2>/dev/null
  FOCUS=$(adb shell dumpsys window 2>/dev/null | tr -d '\r' | grep -m1 -i 'mCurrentFocus' | sed 's/^ *//')
  RESUMED=$(adb shell dumpsys activity activities 2>/dev/null | tr -d '\r' | grep -m1 -iE 'mResumedActivity|topResumedActivity' | sed 's/^ *//')
  TEXTS=$(grep -o 'text="[^"]*"' "$XML" 2>/dev/null | grep -v 'text=""' | sed 's/text=//' | tr '\n' '|' | cut -c1-600)
  MIMO_NODES=$(grep -o 'package="[^"]*"' "$XML" 2>/dev/null | grep -c "$PKG" 2>/dev/null); MIMO_NODES=${MIMO_NODES:-0}
  H=$(sha256sum "$XML" 2>/dev/null | cut -d' ' -f1)
  PIDS=$(adb shell pidof "$PKG" 2>/dev/null | tr -d '\r')
  {
    echo "step=$N label=$LABEL timestamp=$(date -u +%FT%TZ)"
    echo "  uiautomator_exit=$D xml_sha=$H png_bytes=$(stat -c %s "$PNG" 2>/dev/null || echo 0)"
    echo "  pid=$PIDS mimo_nodes=$MIMO_NODES"
    echo "  focus=$FOCUS"
    echo "  resumed=$RESUMED"
    echo "  texts=$TEXTS"
  } >> "$TRACE"
  python3 - "$N" "$LABEL" "$H" "$D" "$MIMO_NODES" "$PIDS" "$FOCUS" "$RESUMED" "$TEXTS" <<'PY' >> "$STATES"
import json,sys
n,l,h,d,m,p,f,r,t=sys.argv[1:10]
print(json.dumps(dict(step=n,label=l,xml_sha256=h,uiautomator_exit=d,
                      mimo_nodes=int(m or 0),pid=p,focus=f,resumed=r,texts=t),ensure_ascii=False))
PY
  if [ "$H" = "$LAST_XML" ] && [ -n "$H" ]; then NO_CHANGE=$((NO_CHANGE+1)); else NO_CHANGE=0; fi
  LAST_XML="$H"
  echo "$XML"
}

# ---- 4. Baseline + bounded real interaction chain ------------------------
BASE=$(capture STEP-00 "onboarding_baseline")
MAX=16
for I in $(seq 1 $MAX); do
  N=$(printf 'STEP-%02d' "$I")
  TAP=$(python3 ANALYSIS/RUNTIME/MISSION_05/choose_tap.py "$BASE" "$AVOID" 2>/dev/null | head -1)
  log "$N choose_tap=$TAP"
  case "$TAP" in
    NONE*|'') log "$N stop_reason=$TAP"; break ;;
  esac
  X=$(printf '%s' "$TAP" | awk '{print $1}')
  Y=$(printf '%s' "$TAP" | awk '{print $2}')
  TXT=$(printf '%s' "$TAP" | awk '{print $3}')
  log "$N action=input_tap x=$X y=$Y target=$TXT"
  adb shell input tap "$X" "$Y" >> "$TRACE" 2>&1
  AVOID="${AVOID:+$AVOID;}$X,$Y"
  sleep 4
  BASE=$(capture "$N" "after_tap_$I")
  if [ "$NO_CHANGE" -ge 2 ]; then log "$N stop_reason=two_identical_consecutive_hierarchies"; break; fi
done
log "interaction_chain_finished steps_captured=$(grep -c '^step=' "$TRACE")"

# ---- 5. Bounded offline dependency probe ---------------------------------
log "OFFLINE_PHASE begin: isolate network, then COLD START the real app offline"
{
  echo "MISSION 05 - OFFLINE PHASE (client-side dependency probe)"
  echo "timestamp_utc=$(date -u +%FT%TZ) package=$PKG"
  echo "== ping BEFORE isolation =="
  adb shell ping -c 1 -W 2 8.8.8.8 2>&1 | tr -d '\r' | head -6
  echo "== active network BEFORE =="
  adb shell dumpsys connectivity 2>/dev/null | tr -d '\r' | grep -m2 -E 'Active default network|NetworkAgentInfo\{network' | cut -c1-200
  echo "== adb shell svc wifi disable =="
  adb shell svc wifi disable 2>&1 | tr -d '\r'; echo "wifi_disable_exit=$?"
  echo "== adb shell svc data disable =="
  adb shell svc data disable 2>&1 | tr -d '\r'; echo "data_disable_exit=$?"
  sleep 2
  echo "== ping AFTER isolation =="
  adb shell ping -c 1 -W 2 8.8.8.8 2>&1 | tr -d '\r' | head -6
  echo "== active network AFTER =="
  adb shell dumpsys connectivity 2>/dev/null | tr -d '\r' | grep -m2 -E 'Active default network|NetworkAgentInfo\{network' | cut -c1-200
} > "$R/LOGS/OFFLINE_PHASE.txt" 2>&1
adb logcat -d -v threadtime > "$R/LOGS/LOGCAT_ONLINE.txt" 2>&1
echo "online_logcat_lines=$(wc -l < "$R/LOGS/LOGCAT_ONLINE.txt")" >> "$R/LOGS/OFFLINE_PHASE.txt"
adb logcat -c >/dev/null 2>&1
log "OFFLINE cold start: am force-stop + am start -n $LAUNCH"
adb shell am force-stop "$PKG" >> "$R/LOGS/OFFLINE_PHASE.txt" 2>&1
adb shell am start -n "$LAUNCH" >> "$R/LOGS/OFFLINE_PHASE.txt" 2>&1
log "offline_am_start_exit=$?"
sleep 18
# dismiss a system ANR overlay if one appeared during the cold start
for ATT in 1 2; do
  adb shell uiautomator dump --compressed /sdcard/window.xml >/dev/null 2>&1
  adb pull /sdcard/window.xml "$R/UI_HIERARCHY/.anr2.xml" >/dev/null 2>&1
  NODE=$(grep -o '<node[^>]*aerr_wait[^>]*>' "$R/UI_HIERARCHY/.anr2.xml" 2>/dev/null | head -1)
  ANR_B=$(printf '%s' "$NODE" | grep -o 'bounds="\[[0-9]*,[0-9]*\]\[[0-9]*,[0-9]*\]"' | head -1)
  if [ -n "$ANR_B" ]; then
    NUMS=$(printf '%s' "$ANR_B" | grep -oE '[0-9]+' | tr '\n' ' '); set -- $NUMS
    CX=$(( ( $1 + $3 ) / 2 )); CY=$(( ( $2 + $4 ) / 2 ))
    log "offline_anr_dialog_attempt_$ATT tap=$CX,$CY"; adb shell input tap "$CX" "$CY" >/dev/null 2>&1; sleep 3
  else break; fi
done
rm -f "$R/UI_HIERARCHY/.anr2.xml"
OFFBASE=$(capture OFFLINE-00 "cold_start_with_network_disabled")
OFFAVOID=""
for J in 1 2 3; do
  ON=$(printf 'OFFLINE-%02d' "$J")
  TAP2=$(python3 ANALYSIS/RUNTIME/MISSION_05/choose_tap.py "$OFFBASE" "$OFFAVOID" 2>/dev/null | head -1)
  log "$ON choose_tap=$TAP2"
  case "$TAP2" in
    NONE*|'') log "$ON stop_reason=$TAP2"; break ;;
  esac
  X2=$(printf '%s' "$TAP2" | awk '{print $1}'); Y2=$(printf '%s' "$TAP2" | awk '{print $2}')
  log "$ON action=input_tap x=$X2 y=$Y2 target=$(printf '%s' "$TAP2" | awk '{print $3}')"
  adb shell input tap "$X2" "$Y2" >> "$TRACE" 2>&1
  OFFAVOID="${OFFAVOID:+$OFFAVOID;}$X2,$Y2"
  sleep 4
  OFFBASE=$(capture "$ON" "offline_after_tap_$J")
done
{
  echo "== restore =="
  adb shell svc wifi enable 2>&1 | tr -d '\r'
  adb shell svc data enable 2>&1 | tr -d '\r'
  echo "restore_done=$(date -u +%FT%TZ)"
  echo "== ping AFTER restore =="
  adb shell ping -c 1 -W 2 8.8.8.8 2>&1 | tr -d '\r' | head -6
} >> "$R/LOGS/OFFLINE_PHASE.txt" 2>&1

# ---- 6. logs + summary ----------------------------------------------------
adb logcat -d -v threadtime > "$R/LOGS/.raw.tmp" 2>&1
grep -viE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|Bearer |token=|api[_-]?key=|password=' \
  "$R/LOGS/.raw.tmp" > "$R/LOGS/LOGCAT_MIMO.txt" 2>&1
rm -f "$R/LOGS/.raw.tmp"
{
  echo "MISSION 05 - CRASH / ERROR / NETWORK OBSERVATIONS"
  echo "timestamp_utc=$(date -u +%FT%TZ) package=$PKG"
  echo "== FATAL / ANR / linker =="
  grep -iE 'FATAL EXCEPTION|ANR |UnsatisfiedLinkError|dlopen|linker|tombstone|SIGSEGV' "$R/LOGS/LOGCAT_MIMO.txt" | head -200
  echo "== network / connectivity / offline hints =="
  grep -iE 'offline|network|UnknownHost|failed to connect|IOException|ConnectException|no route|ENETUNREACH|socket' "$R/LOGS/LOGCAT_MIMO.txt" | head -200
  echo "== Mimo-tagged lines (head) =="
  grep -iE 'getmimo|mimo' "$R/LOGS/LOGCAT_MIMO.txt" | head -160
  echo "== crash buffer =="
  adb logcat -b crash -d -v threadtime 2>&1 | head -120
} > "$R/CRASH_AND_ERROR_LOGS.txt" 2>&1
python3 - "$R" "$TS" "$PKG" "$LAUNCH" "$GITHUB_RUN_ID" "$GITHUB_SHA" <<'PY'
import json,sys,os,glob
R,ts,pkg,launch,rid,sha=sys.argv[1:7]
steps=[]
for line in open(os.path.join(R,'RUNTIME/STATES.jsonl'),errors='replace'):
    line=line.strip()
    if line:
        try: steps.append(json.loads(line))
        except Exception: pass
pngs=sorted(glob.glob(os.path.join(R,'SCREENSHOTS/*.png')))
xmls=sorted(glob.glob(os.path.join(R,'UI_HIERARCHY/*.xml')))
out=dict(document='MISSION 05 — runtime interaction summary',
         workflow_run_id=rid,commit=sha,branch='arena/aebb90b7-game',timestamp_utc=ts,
         package=pkg,resolved_launcher=launch,
         states_captured=len(steps),screenshots=len(pngs),ui_hierarchy_files=len(xmls),
         screenshots_bytes={os.path.basename(p):os.path.getsize(p) for p in pngs},
         states=steps,
         evidence_paths=['LOGS/INTERACTION_TRACE.txt','RUNTIME/STATES.jsonl','SCREENSHOTS/','UI_HIERARCHY/','LOGS/LOGCAT_MIMO.txt','CRASH_AND_ERROR_LOGS.txt','LOGS/OFFLINE_PHASE.txt'],
         boundary='stops at authentication boundary; no credentials, no auth bypass, no fake server responses',
         classification='VERIFIED_RUNTIME for captured states; interpretation is INFERRED')
open(os.path.join(R,'RUNTIME/INTERACTION_SUMMARY.json'),'w').write(json.dumps(out,indent=1,ensure_ascii=False))
print('summary_states=%d pngs=%d xmls=%d'%(len(steps),len(pngs),len(xmls)))
PY
log "MISSION 05 runtime interaction END"
exit 0
