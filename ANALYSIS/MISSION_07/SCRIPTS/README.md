# MISSION 07 — SCRIPTS

* `build_evidence_database.py` — regenerates `../16_EVIDENCE_DATABASE.json`
  (202 entries) from the workspace; verifies every evidence path exists and
  records a SHA-256 prefix, byte size and status per claim.

Runtime harness scripts live in `ANALYSIS/RUNTIME/MISSION_07/`:
`m07_runtime.sh` (stage dispatcher), `m07_stage1_probe.sh`,
`m07_stage2..6_answers.sh`, `m07_answer_driver.py`, `m07_lesson_plan.py`,
`m07_tap_target.py`, `m05_choose_tap.py`, `m07_db_snapshot.py`,
`m07_frida_driver.py`, `m07_frida_stage1.js`, `m07_frida_stage2.js`,
`m07_snapshot.sh`, `FRIDA/java_bridge_frida17.js`, `transfer_apk_m07.sh`.
