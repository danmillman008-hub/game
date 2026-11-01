# Mission 7 — Tool Test Results

| Tool | Test | Result |
|---|---|---|
| `parse_arsc.py` | decodes `resources.arsc` without exceptions; reports 21 type tables | PASS |
| `parse_arsc.py` | colour/dimen extraction yields >0 values (1,198 / 1,401) | PASS |
| `parse_arsc.py` | handles sparse + offset16 type chunks (APK uses them; first version crashed) | PASS |
| `parse_arsc.py` | deterministic: two runs byte-identical | PASS |
| `build_m7_inventory.py` | 29,454 classes, 3,284 decompiled, 15,087 methods | PASS |
| `build_m7_inventory.py` | kind classification totals equal class count | PASS (asserted in suite) |
| `build_m7_inventory.py` | deterministic | PASS |
| inherited `decompile_apk.py` | 7 additional classes decompiled (`ri.a`, `ri.c`, `ge.j`, FCM/Pusher batch) | PASS |

## Fix history (recorded, not hidden)
`parse_arsc.py` v0.1 crashed on `struct.unpack_from` past EOF because it assumed 32-bit entry offsets. Android 12+
tables use **FLAG_SPARSE (0x01)** and **FLAG_OFFSET16 (0x02)**; v1.0 implements both and bounds-checks each entry.
This is the kind of correction the brief asks to record rather than retro-edit.
