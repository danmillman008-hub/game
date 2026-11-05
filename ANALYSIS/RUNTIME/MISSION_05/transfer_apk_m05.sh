#!/usr/bin/env bash
# MISSION 05 - re-use the PROVEN M04 transfer path (two link-only Drive chunks),
# but write evidence into MISSION_05/ so M04 deliverables are never overwritten.
# No URL, token or credential value is written to any log or evidence file.
set +e
R=ANALYSIS/RUNTIME/MISSION_05
mkdir -p "$R/LOGS" "$R/SCREENSHOTS" "$R/UI_HIERARCHY"
OUT="${RUNNER_TEMP:-/tmp}/MIMO_ORIGINAL.apk"
LOG="$R/LOGS/APK_TRANSFER.txt"
CFG="$R/TRANSFER_ENDPOINT.txt"
E="$EXPECTED_APK_SHA256"
B="$EXPECTED_APK_BYTES"
D1=$(grep '^DRIVE1=' "$CFG" | cut -d= -f2- | tr -d '\r\n')
D2=$(grep '^DRIVE2=' "$CFG" | cut -d= -f2- | tr -d '\r\n')
P1B=$(grep '^PART1_BYTES=' "$CFG" | cut -d= -f2- | tr -d '\r\n')
P2B=$(grep '^PART2_BYTES=' "$CFG" | cut -d= -f2- | tr -d '\r\n')
{
  echo "MISSION 05 - ORIGINAL APK TRANSFER (runner side, M04 method 2 reused)"
  echo "timestamp_utc=$(date -u +%FT%TZ)"
  echo "run_id=$GITHUB_RUN_ID ref=$GITHUB_REF sha=$GITHUB_SHA"
  echo "expected_sha256=$E expected_bytes=$B"
  echo "method=2 (Google Drive staged binary chunks, link-only temporary)"
  echo "method_1_authenticated_preview=SKIPPED (disproved: e2b-traffic-access-token required)"
  echo "URL values are intentionally never logged."
} > "$LOG" 2>&1
T="$OUT.parts"; mkdir -p "$T"
U1="https://drive.usercontent.google.com/download?id=$D1&export=download&confirm=t"
U2="https://drive.usercontent.google.com/download?id=$D2&export=download&confirm=t"
curl -fsSL --max-time 900 --retry 2 -o "$T/p1" "$U1" >/dev/null 2>&1
E1=$?
curl -fsSL --max-time 900 --retry 2 -o "$T/p2" "$U2" >/dev/null 2>&1
E2=$?
S1=$(stat -c %s "$T/p1" 2>/dev/null || echo 0)
S2=$(stat -c %s "$T/p2" 2>/dev/null || echo 0)
H1=$(sha256sum "$T/p1" 2>/dev/null | cut -d' ' -f1)
H2=$(sha256sum "$T/p2" 2>/dev/null | cut -d' ' -f1)
{
  echo "m2_part1_exit=$E1 bytes=$S1 want=$P1B sha=$H1"
  echo "m2_part2_exit=$E2 bytes=$S2 want=$P2B sha=$H2"
} >> "$LOG" 2>&1
cat "$T/p1" "$T/p2" > "$OUT" 2>/dev/null
SZ=$(stat -c %s "$OUT" 2>/dev/null || echo 0)
A=$(sha256sum "$OUT" 2>/dev/null | cut -d' ' -f1)
{
  echo "downloaded_bytes=$SZ"
  echo "downloaded_sha256=$A"
  echo "expected_sha256=$E"
  echo "expected_bytes=$B"
} > "$R/APK_SHA256.txt" 2>&1
if [ "$SZ" = "$B" ] && [ "$A" = "$E" ] && [ "$S1" = "$P1B" ] && [ "$S2" = "$P2B" ]; then
  echo "result=SHA_MATCH_OK" >> "$R/APK_SHA256.txt"
  echo "TRANSFER_RESULT=SHA_MATCH_OK" >> "$LOG"
  OK=1
else
  echo "result=SHA_MISMATCH" >> "$R/APK_SHA256.txt"
  echo "TRANSFER_RESULT=SHA_MISMATCH -> refusing install" >> "$LOG"
  OK=0
fi
rm -rf "$T" "$CFG"
sed -i -E 's#https?://[^[:space:]]+#<redacted-transfer-url>#g' "$LOG" 2>/dev/null
echo "transfer_ok=$OK" >> "$LOG"
cat "$LOG"
[ "$OK" = "1" ] || exit 1
exit 0
