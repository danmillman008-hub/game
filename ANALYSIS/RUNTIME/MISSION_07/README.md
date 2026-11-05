# MISSION 07 runtime harness (executed on GitHub Actions emulator runner)

| File | Purpose |
|---|---|
| `transfer_apk_m07.sh` | SHA-gated transfer of the ORIGINAL APK (two proven public link-only chunks) |
| `m07_runtime.sh` | stage dispatcher selected by `ANALYSIS/RUNTIME/_DISPATCH_TRIGGER` |
| `m07_stage1_probe.sh` | STAGE 1: root/Frida/private-DB assessment + first deterministic experiment |
| `m07_frida_stage1.js` | Frida hooks + controlled direct invocations of recovered methods |
| `m07_frida_driver.py` | attach/spawn driver, JSONL method trace capture |
| `m07_db_snapshot.py` | SQLite schema / row-level snapshot of pulled private app storage |

Wired into `.github/workflows/mimo-runtime-verification.yml` via the M07 guard in
`ANALYSIS/RUNTIME/runtime_smoke.sh`. M03/M04/M05 evidence paths are untouched.
