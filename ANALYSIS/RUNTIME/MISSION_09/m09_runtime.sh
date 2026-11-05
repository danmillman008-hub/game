#!/usr/bin/env bash
# MISSION 09 — FINAL controlled reconstruction run.
# Technique switch: API-36-safe direct Activity/Fragment hooks + replay of the
# measured 20-tap chain proven in M08 run 42042312640 (no Compose replay, no
# state restore). Original APK stays SHA-verified and unchanged.
set +e
R=ANALYSIS/RUNTIME/MISSION_09
M7=ANALYSIS/RUNTIME/MISSION_07
# git does not track empty dirs: create every output dir on the runner first.
mkdir -p "$R"/{ENV,EXPERIMENTS,LOGS,TRACES,TIMELINE,STATE,UI,FRIDA}
APK="${RUNNER_TEMP:-/tmp}/MIMO_ORIGINAL.apk"
E="$EXPECTED_APK_SHA256"
T="$R/EXPERIMENTS/M09_TRACE.txt"
: > "$T"
log(){ echo "[$(date -u +%FT%TZ)] $*" | tee -a "$T"; }
FRIDA_VER=17.25.2
TMP="${RUNNER_TEMP:-/tmp}"
FS="$TMP/frida-server"
FSXZ="$TMP/frida-server.xz"
PHASE=9
grep -q "M09-PHASE-2" ANALYSIS/RUNTIME/_DISPATCH_TRIGGER 2>/dev/null && PHASE=2

log "MISSION 09 START phase=$PHASE run=$GITHUB_RUN_ID sha=$GITHUB_SHA"
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
} > "$R/ENV/M09_ENV.txt" 2>&1

adb install -r "$APK" > "$R/ENV/M09_INSTALL.txt" 2>&1
adb shell 'mkdir -p /data/data/com.getmimo/shared_prefs; printf "%s\n" "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\" ?>" "<map>" "    <string name=\"experiment_adapted_onboarding_android_local\">original</string>" "</map>" > /data/data/com.getmimo/shared_prefs/experiments.xml; U=$(stat -c %u:%g /data/data/com.getmimo); chown -R $U /data/data/com.getmimo/shared_prefs; chmod 660 /data/data/com.getmimo/shared_prefs/experiments.xml' >> "$R/ENV/M09_INSTALL.txt" 2>&1
adb shell monkey -p com.getmimo -c android.intent.category.LAUNCHER 1 > "$R/ENV/M09_LAUNCH.txt" 2>&1
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
} > "$R/ENV/M09_FRIDA_SETUP.txt" 2>&1

# HOST-SIDE long-lived `adb shell` keeps the server alive (M07 measured fix).
( adb shell /data/local/tmp/frida-server > "$R/LOGS/M09_FRIDA_SERVER.log" 2>&1 ) &
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
} >> "$R/ENV/M09_FRIDA_SETUP.txt" 2>&1
log "frida_setup_done preflight=$(grep -o 'attach_ok[^}]*' "$R/ENV/M09_FRIDA_SETUP.txt" | tail -1)"

# M09: no state restore. Fresh install + measured phase-1 chain (technique switch).

# ---- ONE orchestrator (phase selected by the dispatch marker) ---------------
DUR=720
[ "$PHASE" = "2" ] && DUR=480
python3 "$R/m09_unified.py" --phase "$PHASE" --duration "$DUR" --agent "$R/m09_agent.js" \
  > "$R/LOGS/M09_ORCHESTRATOR.log" 2>&1
log "orchestrator_exit=$? timeline_lines=$(wc -l < "$R/TIMELINE/M09_RUNTIME_TIMELINE.jsonl" 2>/dev/null || echo 0)"
tail -40 "$R/LOGS/M09_ORCHESTRATOR.log" >> "$T"

adb logcat -d -t 6000 > "$R/LOGS/M09_LOGCAT.txt" 2>&1
python3 - "$R" "$PHASE" > "$R/LOGS/M09_SUMMARY.json" <<'PY'
import json,sys,pathlib,collections
R=pathlib.Path(sys.argv[1]); phase=sys.argv[2]
p=R/'TIMELINE'/'M09_RUNTIME_TIMELINE.jsonl'
by_event=collections.Counter(); by_source=collections.Counter(); by_sub=collections.Counter()
if p.exists():
    for l in p.read_text(errors='replace').splitlines():
        try:o=json.loads(l)
        except:continue
        by_event[o.get('event')]+=1; by_source[o.get('source')]+=1
        if o.get('subsystem'): by_sub[o['subsystem']]+=1
print(json.dumps({'document':'MISSION 09 unified runtime timeline','phase':phase,
 'timeline':str(p),
 'total_events':sum(1 for _ in p.open(errors='replace')) if p.exists() else 0,
 'by_event':dict(by_event),'by_source':dict(by_source),'by_subsystem':dict(by_sub),
 'server_confirmed':0},indent=1))
PY
cat "$R/LOGS/M09_SUMMARY.json"
log "MISSION 09 COMPLETE phase=$PHASE"
exit 0
