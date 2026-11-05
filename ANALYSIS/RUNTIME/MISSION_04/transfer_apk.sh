#!/usr/bin/env bash
# MISSION 04 - transfer the ORIGINAL APK to the runner and verify its SHA-256.
# Method 1: temporary authenticated HTTP endpoint in the authorized workspace.
# Method 2: two sub-100MB chunks staged in Google Drive (link-only, temporary).
# No URL, token or credential value is written to any log or evidence file.
set +e
R=ANALYSIS/RUNTIME/MISSION_04
mkdir -p "$R/LOGS" "$R/SCREENSHOTS" "$R/UI_HIERARCHY"
OUT="${RUNNER_TEMP:-/tmp}/MIMO_ORIGINAL.apk"
LOG="$R/LOGS/APK_TRANSFER.txt"
CFG="$R/TRANSFER_ENDPOINT.txt"
E="$EXPECTED_APK_SHA256"
B="$EXPECTED_APK_BYTES"
PREVIEW=$(grep '^PREVIEW=' "$CFG" | cut -d= -f2- | tr -d '\r\n')
D1=$(grep '^DRIVE1=' "$CFG" | cut -d= -f2- | tr -d '\r\n')
D2=$(grep '^DRIVE2=' "$CFG" | cut -d= -f2- | tr -d '\r\n')
P1B=$(grep '^PART1_BYTES=' "$CFG" | cut -d= -f2- | tr -d '\r\n')
P2B=$(grep '^PART2_BYTES=' "$CFG" | cut -d= -f2- | tr -d '\r\n')

{
  echo "MISSION 04 - ORIGINAL APK TRANSFER (runner side)"
  echo "timestamp_utc=$(date -u +%FT%TZ)"
  echo "run_id=$GITHUB_RUN_ID ref=$GITHUB_REF sha=$GITHUB_SHA"
  echo "expected_sha256=$E expected_bytes=$B"
  echo "URL values are intentionally never logged."
  echo
} > "$LOG" 2>&1

verify() {
  SZ=$(stat -c %s "$OUT" 2>/dev/null || echo 0)
  A=$(sha256sum "$OUT" 2>/dev/null | cut -d' ' -f1)
  echo "downloaded_bytes=$SZ" >> "$LOG"
  echo "downloaded_sha256=$A" >> "$LOG"
  if [ "$SZ" = "$B" ] && [ "$A" = "$E" ]; then
    echo "TRANSFER_RESULT=SHA_MATCH_OK" >> "$LOG"
    return 0
  fi
  echo "TRANSFER_RESULT_NOT_YET_VERIFIED (bytes=$SZ sha=$A)" >> "$LOG"
  return 1
}

redact() {
  sed -i -E 's#https?://[^[:space:]]+#<redacted-transfer-url>#g' "$1" 2>/dev/null
}

# ---------------------------------------------------------------- METHOD 1
echo "== METHOD 1: temporary authenticated HTTP endpoint ==" >> "$LOG"
for VARIANT in plain noproxy browser; do
  case "$VARIANT" in
    plain)   OPTS="" ;;
    noproxy) OPTS="--noproxy *" ;;
    browser) OPTS="-H User-Agent:Mozilla/5.0 -H Accept:*/*" ;;
  esac
  # shellcheck disable=SC2086
  curl -sS $OPTS --max-time 45 -D "$R/LOGS/m1_headers_$VARIANT.txt" \
       -o "$R/LOGS/m1_body_$VARIANT.txt" "$PREVIEW/health" >/dev/null 2>&1
  ST=$(head -1 "$R/LOGS/m1_headers_$VARIANT.txt" 2>/dev/null | tr -d '\r')
  echo "m1_health[$VARIANT]=$ST" >> "$LOG"
  echo "m1_first_headers[$VARIANT]:" >> "$LOG"
  grep -iE '^(server|via|x-|location|content-type|www-authenticate|set-cookie)' \
    "$R/LOGS/m1_headers_$VARIANT.txt" 2>/dev/null | sed -E 's/(cookie|token|sig)=[^ ;]+/\1=<redacted>/Ig' | head -8 >> "$LOG"
  echo "m1_body_prefix[$VARIANT]:" >> "$LOG"
  head -c 300 "$R/LOGS/m1_body_$VARIANT.txt" 2>/dev/null | tr -d '\000' >> "$LOG"
  echo >> "$LOG"
  if echo "$ST" | grep -q ' 200'; then
    echo "m1: health OK via $VARIANT -> full download" >> "$LOG"
    # shellcheck disable=SC2086
    curl -fsSL $OPTS --max-time 900 --retry 1 -o "$OUT" "$PREVIEW/apk" >> "$LOG" 2>&1
    echo "m1_full_exit=$? bytes=$(stat -c %s "$OUT" 2>/dev/null || echo 0)" >> "$LOG"
    if verify; then break; fi
    echo "m1: full transfer incomplete -> chunked fallback" >> "$LOG"
    rm -f "$OUT"
    N=$(curl -sS $OPTS --max-time 60 "$PREVIEW/count" 2>>"$LOG" | tr -d '\r\n')
    echo "m1_chunk_count=$N" >> "$LOG"
    case "$N" in ''|*[!0-9]*) echo "m1: invalid chunk count" >> "$LOG" ;; *)
      i=0
      while [ "$i" -lt "$N" ]; do
        curl -fsSL $OPTS --max-time 300 --retry 2 -o "$OUT.part$i" "$PREVIEW/part/$i" >> "$LOG" 2>&1
        CE=$?; CS=$(stat -c %s "$OUT.part$i" 2>/dev/null || echo 0)
        echo "m1_chunk_$i exit=$CE bytes=$CS" >> "$LOG"
        [ "$CE" -eq 0 ] && [ "$CS" -gt 0 ] || break
        cat "$OUT.part$i" >> "$OUT"; rm -f "$OUT.part$i"; i=$((i+1))
      done
      if verify; then break; fi ;;
    esac
  fi
done

# ---------------------------------------------------------------- METHOD 2
if ! grep -q 'TRANSFER_RESULT=SHA_MATCH_OK' "$LOG"; then
  echo >> "$LOG"
  echo "== METHOD 2: Google Drive staged chunks (link-only, temporary) ==" >> "$LOG"
  rm -f "$OUT" "$OUT.p1" "$OUT.p2"
  fetch_part() {
    ID="$1"; DEST="$2"; WANT="$3"; TAG="$4"
    for HOST in drive.usercontent.google.com drive.google.com; do
      if [ "$HOST" = "drive.usercontent.google.com" ]; then
        U="https://$HOST/download?id=$ID&export=download&confirm=t"
      else
        U="https://$HOST/uc?export=download&id=$ID&confirm=t"
      fi
      curl -fsSL --max-time 900 --retry 2 -o "$DEST" "$U" >> "$LOG" 2>&1
      CE=$?; CS=$(stat -c %s "$DEST" 2>/dev/null || echo 0)
      echo "m2_${TAG}_host=$HOST exit=$CE bytes=$CS want=$WANT" >> "$LOG"
      if [ "$CE" -eq 0 ] && [ "$CS" = "$WANT" ]; then return 0; fi
      # An HTML virus-scan interstitial means the confirm token must be parsed.
      if head -c 200 "$DEST" 2>/dev/null | grep -qi '<html\|<!doctype'; then
        echo "m2_${TAG}_interstitial=HTML (not binary)" >> "$LOG"
      fi
    done
    return 1
  }
  if fetch_part "$D1" "$OUT.p1" "$P1B" part1 && fetch_part "$D2" "$OUT.p2" "$P2B" part2; then
    cat "$OUT.p1" "$OUT.p2" > "$OUT"
    echo "m2_concat_bytes=$(stat -c %s "$OUT" 2>/dev/null || echo 0)" >> "$LOG"
    echo "m2_part1_sha=$(sha256sum "$OUT.p1" | cut -d' ' -f1)" >> "$LOG"
    echo "m2_part2_sha=$(sha256sum "$OUT.p2" | cut -d' ' -f1)" >> "$LOG"
    verify
  else
    echo "m2: could not retrieve both binary chunks" >> "$LOG"
  fi
  rm -f "$OUT.p1" "$OUT.p2"
fi

# ---------------------------------------------------------------- FINAL
if ! grep -q 'TRANSFER_RESULT=SHA_MATCH_OK' "$LOG"; then
  echo "TRANSFER_RESULT=FAILED_ALL_METHODS" >> "$LOG"
  echo "expected_sha256=$E actual_sha256=$(sha256sum "$OUT" 2>/dev/null | cut -d' ' -f1) size=$(stat -c %s "$OUT" 2>/dev/null || echo 0)" > "$R/APK_SHA256.txt"
else
  {
    echo "expected_sha256=$E"
    echo "actual_sha256=$(sha256sum "$OUT" | cut -d' ' -f1)"
    echo "size_bytes=$(stat -c %s "$OUT")"
    echo "timestamp_utc=$(date -u +%FT%TZ)"
    echo "result=SHA_MATCH_OK"
  } > "$R/APK_SHA256.txt"
fi
rm -f "$CFG" "$R/LOGS/m1_headers_"* "$R/LOGS/m1_body_"*
for F in "$LOG" "$R/LOGS/TRANSFER_DIAG.txt"; do [ -f "$F" ] && redact "$F"; done
cat "$LOG" | tail -80
grep -q 'TRANSFER_RESULT=SHA_MATCH_OK' "$LOG" || exit 1
echo "transfer_verified=yes"
