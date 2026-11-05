# MISSION 06 — EVIDENCE

All files here are derived **read-only** from the 12 original `ANALYSIS/_INPUT/classes*.dex`
and the unchanged APK (SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`).

| Path | Content |
|---|---|
| `DISASM/` | 82 verbatim Androguard 4.1.4 class disassemblies + `INDEX.json`; every method header carries DEX file, code offset, instruction count, corrected caller/callee counts and xref lists |
| `VALIDATION_RAW_DISASM.txt` | long-method answer-validator disassembly (fillTheGap, selection, spell, validatedInput) |
| `VALIDATEDINPUT_SETUP_DISASM.txt` | `setupViews$2`, `Lqm/d.E`, `qm/i.a` normalizer |
| `ALGORITHM_DIGEST.txt` | progress queue, completion, path-banner, network, chapter-end, executable-lesson methods |
| `DSL_PARSER_DISASM.txt` | `Lte/c`, `Lte/a..g`, `Lgm/h` disassembly |
| `MODEL_FACTS.txt`, `PARSER_AND_STATE_FACTS.txt` | recovered field/enum/state tables |
| `PATH_STATE_DISASM.txt` | `GetPathMapState$invoke$3`, `Lcc/b.y` |
| `INTERACTION_SELECTOR_DISASM.txt` | `Lgm/h.a` and related |
| `DEX_STRING_INDEX.txt` | 565-line string-constant index (content/network/native/executable) |
| `DEOBFUSCATION_NOTES.md` | R8 name recovery, smob decoys, method-name-map caveats |
| `M06_DEX_HARNESS.py`, `M06_EXPORT_CATALOG.py`, `M06_METHOD_NAME_MAP.py` | reproducible toolchain (Androguard venv required) |
| `TOOLCHAIN/` | full script set actually used: `m06_dex.py`, `export_catalog.py`, `map_methods.py`, `export_disasm*.py`, `digest.py`, `algo_view.py`, `regenerate_all.py`, `call_graphs.py`, `write_*.py` |

`SERVER CONFIRMED = 0`. No server responses, no private app databases, no emulator
screenshots were added here. Runtime evidence from M05 is cross-referenced in
`RUNTIME_EVIDENCE/` and `EVIDENCE_DATABASE.json`.
