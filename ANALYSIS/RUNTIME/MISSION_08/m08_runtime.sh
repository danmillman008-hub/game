#!/usr/bin/env bash
# MISSION 08 — ONE broad controlled investigation run.
# Reuses the M07-proven setup verbatim; only the orchestrator is new.
set +e
R=ANALYSIS/RUNTIME/MISSION_08
M7=ANALYSIS/RUNTIME/MISSION_07
APK="${RUNNER_TEMP:-/tmp}/MIMO_ORIGINAL.apk"
E="$EXPECTED_APK_SHA256"
T="$R/EXPERIMENTS/M08_TRACE.txt"
: > "$T"
log(){ echo "[$(date -u +%FT%TZ)] $*" | tee -a "$T"; }
FRIDA_VER=17.25.2

log "MISSION 08 START run=$GITHUB_RUN_ID sha=$GITHUB_SHA"
A=$(sha256sum "$APK" 2>/dev/null | cut -d' ' -f1)
[ "$A" = "$E" ] || { log "sha_gate=FAIL $A"; exit 1; }
log "sha_gate=SHA_MATCH_OK bytes=$(stat -c %s "$APK")"

adb root >/dev/null 2>&1; sleep 3; adb wait-for-device >/dev/null 2>&1
adb shell setenforce 0 >/dev/null 2>&1
{
  echo "timestamp_utc=$(date -u +%FT%TZ) run_id=$GITHUB_RUN_ID"
  echo "root_id=$(adb shell id 2>&1)"
  echo "selinux=$(adb shell getenforce 2>&1)"
  echo "ps_mimo=$(adb shell 'ps -A | grep -E "Mimo|com.getmimo"' 2>&1)"
  echo "pidof=$(adb shell pidof com.getmimo 2>&1)"
} > "$R/ENV/M08_ENV.txt" 2>&1

adb install -r "$APK" > "$R/ENV/M08_INSTALL.txt" 2>&1
adb shell 'mkdir -p /data/data/com.getmimo/shared_prefs; printf "%s\n" "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\" ?>" "<map>" "    <string name=\"experiment_adapted_onboarding_android_local\">original</string>" "</map>" > /data/data/com.getmimo/shared_prefs/experiments.xml; U=$(stat -c %u:%g /data/data/com.getmimo); chown -R $U /data/data/com.getmimo/shared_prefs; chmod 660 /data/data/com.getmimo/shared_prefs/experiments.xml' >> "$R/ENV/M08_INSTALL.txt" 2>&1
adb shell monkey -p com.getmimo -c android.intent.category.LAUNCHER 1 > "$R/ENV/M08_LAUNCH.txt" 2>&1
sleep 18

# ---- Frida 17 + Java bridge (M07 setup, unchanged) -------------------------
{
  python3 -m pip install --quiet "frida==$FRIDA_VER" "frida-tools==14.11.0" 2>&1 | tail -5
  python3 -c 'import frida;print("frida="+frida.__version__)'
  U="https://github.com/frida/frida/releases/download/$FRIDA_VER/frida-server-$FRIDA_VER-android-x86_64.xz"
  curl -fL --retry 2 --max-time 600 -o "${RUNNER_TEMP:-/tmp}/frida-server.xz" "$U" >/dev/null 2>&1
  xz -dkf "${RUNNER_TEMP:-/tmp}/frida-server.xz" >/dev/null 2>&1
  adb push "${RUNNER_TEMP:-/tmp}/frida-server" /data/local/tmp/frida-server 2>&1 | tail -1
  adb shell chmod 755 /data/local/tmp/frida-server
  frida-ps -U 2>&1 | grep -i mimo
} > "$R/ENV/M08_FRIDA_SETUP.txt" 2>&1
( adb shell /data/local/tmp/frida-server > "$R/LOGS/M08_FRIDA_SERVER.log" 2>&1 ) &
sleep 6
frida-ps -U | grep -i mimo >> "$R/ENV/M08_FRIDA_SETUP.txt" 2>&1
log "frida_setup_done"

# ---- optional tool probe (adopt only with demonstrated advantage) ----------
{
  echo "== UI automation tool assessment =="
  python3 -m pip install --quiet uiautomator2 2>&1 | tail -3
  timeout 45 python3 - <<'PY' 2>&1
try:
    import uiautomator2 as u2
    d = u2.connect()
    print("uiautomator2_available=True app_current=", d.app_current())
except Exception as e:
    print("uiautomator2_available=False error=", str(e)[:200])
PY
  echo "decision: existing adb uiautomator dump + dumpsys + Frida lifecycle hooks already give activity/fragment/state; no new device-side server adopted"
} > "$R/ENV/M08_TOOL_ASSESSMENT.txt" 2>&1

# ---- ONE orchestrator ------------------------------------------------------
python3 "$R/m08_unified.py" --duration 720 --agent "$R/m08_agent.js" \
  > "$R/LOGS/M08_ORCHESTRATOR.log" 2>&1
log "orchestrator_exit=$? timeline_lines=$(wc -l < "$R/TIMELINE/MIMO_RUNTIME_TIMELINE.jsonl" 2>/dev/null || echo 0)"
tail -30 "$R/LOGS/M08_ORCHESTRATOR.log" >> "$T"

adb logcat -d -t 6000 > "$R/LOGS/M08_LOGCAT.txt" 2>&1
python3 - "$R" > "$R/LOGS/M08_SUMMARY.json" <<'PY'
import json,sys,pathlib,collections
R=pathlib.Path(sys.argv[1])
p=R/'TIMELINE'/'MIMO_RUNTIME_TIMELINE.jsonl'
c=collections.Counter(); sub=collections.Counter(); tags=collections.Counter()
if p.exists():
    for l in p.read_text(errors='replace').splitlines():
        try:o=json.loads(l)
        except:continue
        c[o.get('source')]+=1; c[o.get('event')]+=1
        if o.get('subsystem'):sub[o['subsystem']]+=1
        if o.get('tag'):tags[o['tag']]+=1
print(json.dumps({'document':'MISSION 08 unified runtime timeline','timeline':str(p),
 'total_events':sum(1 for _ in p.open(errors='replace')) if p.exists() else 0,
 'sources':dict(c),'subsystems':dict(sub),'tags':dict(tags),'server_confirmed':0},indent=1))
PY
cat "$R/LOGS/M08_SUMMARY.json"
log "MISSION 08 COMPLETE"
