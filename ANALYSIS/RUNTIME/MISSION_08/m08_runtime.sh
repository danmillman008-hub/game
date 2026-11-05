#!/usr/bin/env bash
# MISSION 08 — one broad + one targeted controlled investigation run.
# Reuses the M07-proven setup; the ONLY new runtime component is m08_unified.py.
set +e
R=ANALYSIS/RUNTIME/MISSION_08
M7=ANALYSIS/RUNTIME/MISSION_07
# git does not track empty dirs: create every output dir on the runner first.
mkdir -p "$R"/{ENV,EXPERIMENTS,LOGS,TRACES,TIMELINE,STATE,UI,FRIDA}
APK="${RUNNER_TEMP:-/tmp}/MIMO_ORIGINAL.apk"
E="$EXPECTED_APK_SHA256"
T="$R/EXPERIMENTS/M08_TRACE.txt"
: > "$T"
log(){ echo "[$(date -u +%FT%TZ)] $*" | tee -a "$T"; }
FRIDA_VER=17.25.2
TMP="${RUNNER_TEMP:-/tmp}"
FS="$TMP/frida-server"
FSXZ="$TMP/frida-server.xz"
PHASE=1
grep -q "M08-PHASE-2" ANALYSIS/RUNTIME/_DISPATCH_TRIGGER 2>/dev/null && PHASE=2
grep -q "M08-PHASE-3" ANALYSIS/RUNTIME/_DISPATCH_TRIGGER 2>/dev/null && PHASE=3

log "MISSION 08 START phase=$PHASE run=$GITHUB_RUN_ID sha=$GITHUB_SHA"
A=$(sha256sum "$APK" 2>/dev/null | cut -d' ' -f1)
[ "$A" = "$E" ] || { log "sha_gate=FAIL $A"; exit 1; }
log "sha_gate=SHA_MATCH_OK bytes=$(stat -c %s "$APK")"

adb root >/dev/null 2>&1; sleep 3; adb wait-for-device >/dev/null 2>&1
adb shell setenforce 0 >/dev/null 2>&1
{
  echo "timestamp_utc=$(date -u +%FT%TZ) run_id=$GITHUB_RUN_ID phase=$PHASE"
  echo "root_id=$(adb shell id 2>&1)"
  echo "selinux=$(adb shell getenforce 2>&1)"
  echo "ps_mimo=$(adb shell 'ps -A | grep -E "Mimo|com.getmimo"' 2>&1)"
  echo "pidof=$(adb shell pidof com.getmimo 2>&1)"
} > "$R/ENV/M08_ENV.txt" 2>&1

adb install -r "$APK" > "$R/ENV/M08_INSTALL.txt" 2>&1
adb shell 'mkdir -p /data/data/com.getmimo/shared_prefs; printf "%s\n" "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\" ?>" "<map>" "    <string name=\"experiment_adapted_onboarding_android_local\">original</string>" "</map>" > /data/data/com.getmimo/shared_prefs/experiments.xml; U=$(stat -c %u:%g /data/data/com.getmimo); chown -R $U /data/data/com.getmimo/shared_prefs; chmod 660 /data/data/com.getmimo/shared_prefs/experiments.xml' >> "$R/ENV/M08_INSTALL.txt" 2>&1
adb shell monkey -p com.getmimo -c android.intent.category.LAUNCHER 1 > "$R/ENV/M08_LAUNCH.txt" 2>&1
sleep 18

# ---- Frida 17 + Java bridge: M07 setup with a hard, DIAGNOSED fallback chain.
# Run 42042312640 produced NO Frida method events because the GitHub release
# asset download failed silently and no server binary was pushed. Here every
# step is measured, three independent download paths are tried, and an actual
# attach is verified BEFORE the orchestrator starts.
{
  echo "== host frida =="
  python3 -m pip install --quiet "frida==$FRIDA_VER" "frida-tools==14.11.0" 2>&1 | tail -5
  python3 -c 'import frida;print("frida="+frida.__version__)'
  U="https://github.com/frida/frida/releases/download/$FRIDA_VER/frida-server-$FRIDA_VER-android-x86_64.xz"

  echo "== attempt 1: curl GitHub release asset =="
  rm -f "$FS" "$FSXZ"
  curl -fL --retry 4 --retry-all-errors --retry-delay 3 --max-time 600 -o "$FSXZ" "$U" 2>&1 | tail -4
  echo "curl_exit=${PIPESTATUS[0]} bytes=$(stat -c %s "$FSXZ" 2>/dev/null || echo 0)"

  echo "== attempt 2: python lzma decompression (independent of xz binary) =="
  python3 - "$FSXZ" "$FS" <<'PY'
import sys, lzma, pathlib
src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
try:
    dst.write_bytes(lzma.decompress(src.read_bytes()))
    print("lzma_ok bytes=", dst.stat().st_size)
except Exception as e:
    print("lzma_failed", str(e)[:200])
PY

  echo "== attempt 3: authenticated GitHub API asset (if curl/CDN failed) =="
  if [ ! -s "$FS" ] && [ -n "${GH_TOKEN:-}" ]; then
    AID=$(gh api "repos/frida/frida/releases/tags/$FRIDA_VER" \
      --jq ".assets[] | select(.name==\"frida-server-$FRIDA_VER-android-x86_64.xz\") | .id" 2>/dev/null | head -1)
    echo "asset_id=$AID"
    if [ -n "$AID" ]; then
      gh api "repos/frida/frida/releases/assets/$AID" \
        -H 'Accept: application/octet-stream' > "$FSXZ" 2>/dev/null
      echo "api_asset_bytes=$(stat -c %s "$FSXZ" 2>/dev/null || echo 0)"
      python3 - "$FSXZ" "$FS" <<'PY'
import sys, lzma, pathlib
src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
try:
    dst.write_bytes(lzma.decompress(src.read_bytes()))
    print("api_lzma_ok bytes=", dst.stat().st_size)
except Exception as e:
    print("api_lzma_failed", str(e)[:200])
PY
    fi
  fi
  echo "local_server_file=$(ls -l "$FS" 2>&1)"

  echo "== device install =="
  adb shell 'pkill -f frida-server; rm -f /data/local/tmp/frida-server' 2>&1
  adb push "$FS" /data/local/tmp/frida-server 2>&1 | tail -2
  adb shell chmod 755 /data/local/tmp/frida-server 2>&1
  adb shell '/data/local/tmp/frida-server --version' 2>&1 | head -3
  echo "device_file=$(adb shell 'ls -l /data/local/tmp/frida-server' 2>&1)"
} > "$R/ENV/M08_FRIDA_SETUP.txt" 2>&1

# HOST-SIDE long-lived `adb shell` keeps the server alive (M07 measured fix).
( adb shell /data/local/tmp/frida-server > "$R/LOGS/M08_FRIDA_SERVER.log" 2>&1 ) &
sleep 7
{
  echo "== post-start verification =="
  echo "frida_ps=$(frida-ps -U 2>&1 | grep -i mimo)"
  echo "device_ps=$(adb shell 'ps -A | grep frida' 2>&1)"
  echo "== actual attach preflight =="
  python3 - <<'PY'
import frida, subprocess, json
try:
    out = subprocess.check_output(['adb','shell','pidof','com.getmimo'], timeout=20).decode().strip()
    pid = int(out.split()[0])
    dev = frida.get_usb_device(timeout=30)
    hits = [p for p in dev.enumerate_processes() if p.pid == pid or p.name == 'Mimo']
    s = dev.attach(hits[0].pid)
    print(json.dumps({'attach_ok': True, 'pid': hits[0].pid, 'name': hits[0].name}))
    s.detach()
except Exception as e:
    print(json.dumps({'attach_ok': False, 'error': str(e)[:300]}))
PY
} >> "$R/ENV/M08_FRIDA_SETUP.txt" 2>&1
log "frida_setup_done preflight=$(grep -o 'attach_ok[^}]*' "$R/ENV/M08_FRIDA_SETUP.txt" | tail -1)"

# ---- PHASE 3: skip onboarding by restoring a NATURAL (non-synthetic) state.
# Phase 2's state-aware onboarding stalled on a Compose screen that uiautomator
# cannot expose. Instead of repeating that ineffective approach, restore the
# naturally generated post-onboarding private data from run 42042312640
# (STATE/S1_POST_ONBOARDING). No rows/values are invented; this is tagged
# synthetic=false in the timeline. Room is restored from the sqlite3 .backup
# snapshot so WAL state is consistent.
if [ "$PHASE" = "3" ]; then
  SRC="$R/STATE/S1_POST_ONBOARDING"
  {
    echo "== natural state restore (run 42042312640 / S1_POST_ONBOARDING) =="
    echo "synthetic=false; no seeded learner rows"
    adb shell am force-stop com.getmimo
    adb shell 'rm -rf /sdcard/m08_natural; mkdir -p /sdcard/m08_natural'
    adb push "$SRC/private/databases" /sdcard/m08_natural/ 2>&1 | tail -1
    adb push "$SRC/private/shared_prefs" /sdcard/m08_natural/ 2>&1 | tail -1
    adb push "$SRC/private/files" /sdcard/m08_natural/ 2>&1 | tail -1
    adb push "$SRC/private/no_backup" /sdcard/m08_natural/ 2>&1 | tail -1
    adb push "$SRC/consistent_mimo.db" /sdcard/m08_mimo_consistent.db 2>&1 | tail -1
    adb shell 'rm -rf /data/data/com.getmimo/databases /data/data/com.getmimo/shared_prefs /data/data/com.getmimo/files /data/data/com.getmimo/no_backup; mkdir -p /data/data/com.getmimo; cp -a /sdcard/m08_natural/* /data/data/com.getmimo/; rm -f /data/data/com.getmimo/databases/mimo.db*; cp /sdcard/m08_mimo_consistent.db /data/data/com.getmimo/databases/mimo.db; U=$(stat -c %u:%g /data/data/com.getmimo); chown -R $U /data/data/com.getmimo; chmod 660 /data/data/com.getmimo/shared_prefs/*.xml' 2>&1
    echo "restored_files=$(adb shell 'find /data/data/com.getmimo -type f | wc -l')"
    echo "restored_lesson_progress_rows=$(adb shell 'sqlite3 /data/data/com.getmimo/databases/mimo.db "select count(*) from lesson_progress;"' 2>&1)"
    adb shell monkey -p com.getmimo -c android.intent.category.LAUNCHER 1 2>&1 | tail -2
  } > "$R/ENV/M08_PHASE3_RESTORE.txt" 2>&1
  sleep 16
  # Third-party launcher overlay (observed in phase 2) has a countdown; wait it out.
  sleep 8
  log "phase3_natural_restore_done rows=$(grep restored_lesson_progress_rows "$R/ENV/M08_PHASE3_RESTORE.txt" | tail -1)"
fi

# ---- ONE orchestrator (phase selected by the dispatch marker) ---------------
DUR=660
[ "$PHASE" = "3" ] && DUR=360
python3 "$R/m08_unified.py" --phase "$PHASE" --duration "$DUR" --agent "$R/m08_agent.js" \
  > "$R/LOGS/M08_ORCHESTRATOR.log" 2>&1
log "orchestrator_exit=$? timeline_lines=$(wc -l < "$R/TIMELINE/MIMO_RUNTIME_TIMELINE.jsonl" 2>/dev/null || echo 0)"
tail -40 "$R/LOGS/M08_ORCHESTRATOR.log" >> "$T"

adb logcat -d -t 6000 > "$R/LOGS/M08_LOGCAT.txt" 2>&1
python3 - "$R" "$PHASE" > "$R/LOGS/M08_SUMMARY.json" <<'PY'
import json,sys,pathlib,collections
R=pathlib.Path(sys.argv[1]); phase=sys.argv[2]
p=R/'TIMELINE'/'MIMO_RUNTIME_TIMELINE.jsonl'
by_event=collections.Counter(); by_source=collections.Counter(); by_sub=collections.Counter()
if p.exists():
    for l in p.read_text(errors='replace').splitlines():
        try:o=json.loads(l)
        except:continue
        by_event[o.get('event')]+=1; by_source[o.get('source')]+=1
        if o.get('subsystem'): by_sub[o['subsystem']]+=1
print(json.dumps({'document':'MISSION 08 unified runtime timeline','phase':phase,
 'timeline':str(p),
 'total_events':sum(1 for _ in p.open(errors='replace')) if p.exists() else 0,
 'by_event':dict(by_event),'by_source':dict(by_source),'by_subsystem':dict(by_sub),
 'server_confirmed':0},indent=1))
PY
cat "$R/LOGS/M08_SUMMARY.json"
log "MISSION 08 COMPLETE phase=$PHASE"
exit 0
