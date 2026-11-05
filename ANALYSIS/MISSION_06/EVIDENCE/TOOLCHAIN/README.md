# MISSION 06 — reproducible toolchain scripts

Copy of every Python script used during M06 (scratch dir `/home/user/_work/m06/`).
Run with `/home/user/_work/m06/venv/bin/python` (Androguard 4.1.4). All scripts read only
`ANALYSIS/_INPUT/classes*.dex` and the unchanged original APK; none modify them.

| Script | Purpose |
|---|---|
| `m06_dex.py` | read-only 12-DEX harness: class/method/field/string/xref cache, disassembly, caller/callee queries (corrected descriptor regex) |
| `export_catalog.py` / `map_methods.py` | `SCHEMAS/OBFUSCATION_MAP.json`, `METHOD_CATALOG_MIMO.json`, `CLASS_CATALOG_MIMO.json`, `METHOD_NAME_MAP.json` |
| `export_disasm.py`, `export_disasm2.py`, `export_disasm3.py` | first three batches of full class disassembly dumps |
| `regenerate_all.py` | **final authoritative** regeneration of all 82 dumps + `INDEX.json` + both catalogs with the corrected xref cache |
| `digest.py`, `algo_view.py` | long-method disassembly digests |
| `call_graphs.py` | 9 real BFS call graphs (`.mmd` + `.json`) |
| `write_diagrams.py`, `write_dossiers.py`, `write_docs_1.py`…`write_docs_3.py`, `write_evidence_db.py`, `write_support.py` | deliverable generators |

Known limitations are recorded in `../DEOBFUSCATION_NOTES.md` and
`../../17_CORRECTIONS_AND_LIMITATIONS.md`. `SERVER CONFIRMED = 0`.
