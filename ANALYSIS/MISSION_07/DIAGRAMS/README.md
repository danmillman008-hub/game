# MISSION 07 — DIAGRAMS (Mermaid)

| file | subject |
|---|---|
| `01_runtime_pipeline.mmd` | APK → emulator → root/Frida/SQLite → reports |
| `02_answer_state_machine.mmd` | slide → WebView wrong → correct → offline queue deletion |
| `03_room_state.mmd` | `mimo.db` tables and measured row counts |
| `04_offline_queue.mmd` | sequence: `U/H/e0/queue_store` → offline `NoConnectionException` → `DELETE … in_queue=1` |
| `05_instrumentation.mmd` | Java bridge, 42 hooks, SQL/SQLiteStatement/LiveData, E1–E6 |

All diagrams are derived from `VERIFIED_RUNTIME` / `VERIFIED_STATIC` evidence;
no server component is drawn (`SERVER CONFIRMED = 0`).
