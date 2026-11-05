#!/usr/bin/env bash
# MISSION 07 dispatcher. The emulator action runs ONE line:
#   bash ANALYSIS/RUNTIME/MISSION_07/m07_runtime.sh
# Stage is selected by the marker in ANALYSIS/RUNTIME/_DISPATCH_TRIGGER.
set +e
T=ANALYSIS/RUNTIME/_DISPATCH_TRIGGER
R=ANALYSIS/RUNTIME/MISSION_07
mkdir -p "$R/LOGS"
echo "M07 dispatcher $(date -u +%FT%TZ) run=$GITHUB_RUN_ID sha=$GITHUB_SHA marker=$(tr '\n' ' ' < "$T")" | tee "$R/LOGS/DISPATCH.txt"
if grep -q 'M07-STAGE-1' "$T"; then
  exec bash "$R/m07_stage1_probe.sh"
fi
echo "M07 dispatcher: no recognised stage; recording marker only" | tee -a "$R/LOGS/DISPATCH.txt"
exit 0
