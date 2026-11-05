#!/usr/bin/env bash
# MISSION 07 - transfer the ORIGINAL APK to the GitHub Actions runner.
# Reuses the PROVEN M04/M05 path: two public link-only Drive chunks staged in
# the authorized workspace. Original APK and its SHA-256 are unchanged.
# No URL, token or credential value is ever logged or committed.
set +e
R=ANALYSIS/RUNTIME/MISSION_07
mkdir -p "$R/LOGS"
OUT="${RUNNER_TEMP:-/tmp}/MIMO_ORIGINAL.apk"
LOG="$R/LOGS/APK_TRANSFER.txt"
E="$EXPECTED_APK_SHA256"
B="$EXPECTED_APK_BYTES"
# IDs were already public in git history from M04/M05; no new exposure.
D1='1xiEGAOyQ543m7PhEA--zvw5C2uYe9xxq'
D2='16Qb6Rbu2S1uP7bTbrzAKvUxpJSILzn5E'
P1B=71176749
P2B=71176750
{
  echo "MISSION 07 - ORIGINAL APK TRANSFER (runner side)"
  echo "timestamp_utc=$(date -u +%FT%TZ)"
  echo "run_id=$GITHUB_RUN_ID ref=$GITHUB_REF sha=$GITHUB_SHA"
  echo "expected_sha256=$E expected_bytes=$B"
  echo "method=2 (two public link-only Drive chunks; SHA gate enforced)"
  echo "URL values are intentionally never logged."
} > "$LOG" 2>&1
T="$OUT.parts"; mkdir -p "$T"
U1="https://drive.usercontent.google.com/download?id=$D1&export=download&confirm=t"
U2="https://drive.usercontent.google.com/download?id=$D2&export=download&confirm=t"
curl -fsSL --max-time 900 --retry 2 -o "$T/p1" "$U1" >/dev/null 2>&1; E1=$?
curl -fsSL --max-time 900 --retry 2 -o "$T/p2" "$U2" >/dev/null 2>&1; E2=$?
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
  echo "downloaded_bytes=$SZ"; echo "downloaded_sha256=$A"
  echo "expected_sha256=$E"; echo "expected_bytes=$B"
} > "$R/LOGS/APK_SHA256.txt" 2>&1
if [ "$SZ" = "$B" ] && [ "$A" = "$E" ] && [ "$S1" = "$P1B" ] && [ "$S2" = "$P2B" ]; then
  echo "result=SHA_MATCH_OK" >> "$R/LOGS/APK_SHA256.txt"
  echo "TRANSFER_RESULT=SHA_MATCH_OK" >> "$LOG"; OK=1
else
  echo "result=SHA_MISMATCH" >> "$R/LOGS/APK_SHA256.txt"
  echo "TRANSFER_RESULT=SHA_MISMATCH -> refusing install" >> "$LOG"; OK=0
fi
rm -rf "$T"
sed -i -E 's#https?://[^[:space:]]+#<redacted-transfer-url>#g' "$LOG" 2>/dev/null
echo "transfer_ok=$OK" >> "$LOG"
cat "$LOG"
[ "$OK" = "1" ] || exit 1
exit 0
