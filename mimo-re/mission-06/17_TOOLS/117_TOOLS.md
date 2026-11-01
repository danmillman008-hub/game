# Mission 6 — Tools

Seven deterministic CLI tools. None performs network calls, none mutates an input artifact, all emit
JSON/CSV with stable ordering. Run with the mission virtualenv (`/tmp/venv/bin/python`, Python 3.11.2,
androguard 4.1.4).

| Tool | Purpose | Input | Output | Network | Mutates input |
|---|---|---|---|---|---|
| `build_baseline.py` | APK identity, dex hashes, environment snapshot | APK path | `00_BASELINE/*.json` | no | no |
| `extract_resources.py` | zip inventory + `res/` + AXML manifest summary | APK path | `evidence/RESOURCES.json`, `00_BASELINE/APK_MANIFEST.json` | no | no |
| `build_class_inventory.py` | class/method inventory over all dex | APK path | `06_CLASS_METHOD_INVENTORY.csv` | no | no |
| `extract_parser_grammar.py` | per-parser tag/attribute/child extraction | decompiled `te/*` sources | `evidence/PARSER_GRAMMAR.json` | no | no |
| `extract_event_candidates.py` | analytics-name candidate extraction | dex strings | `evidence/EVENT_CANDIDATES*.{csv,json}` | no | no |
| `extract_di_graph.py` | DI `when`-branch extraction (base URLs) | decompiled `ae/m` | `evidence/DI_GRAPH.json` | no | no |
| `extract_class_fields.py` | Kotlin data-class field dump (content models, DTOs) | decompiled sources + DTO csv | `evidence/{CONTENT_MODEL_FIELDS,DTO_FIELDS}.json` | no | no |

## Interface conventions
- `--out PATH` is mandatory for extractors; output is `json.dump(..., indent=1, sort_keys=…)` or CSV with a
  fixed header, so repeated runs are byte-identical for identical inputs.
- Exit code 0 on success; a missing optional class is reported as `{"found": false}` rather than an error
  (partial knowledge must be representable).
- No tool reads the network, writes outside its `--out`, or rewrites decompiled sources.

## Provenance
APK sha256 `48ce1740…`, md5 `f9cef2d8…` (see `00_BASELINE/APK_MANIFEST.json`). Decompiler: androguard 4.1.4
in-process DAD (`/tmp/dad`), because JADX/`java` are unavailable (`15_RUNTIME/95_RUNTIME_PREREQUISITES.md`).

## Limitations (per tool)
- `extract_parser_grammar.py`: reads `require()`/`getAttributeValue()` call sites; loop structure is not
  recovered, so repetition is marked, not proven.
- `extract_class_fields.py`: `private final` fields only — properties, constants and `@SerialName`
  overrides are missed; 11/50 DTOs returned no fields for that reason.
- `extract_di_graph.py`: parses the `when` arms textually; arms producing objects without `new` are
  captured only as numbers.
- `build_class_inventory.py`: memory-heavy on 12 dex (~2.7 GB RSS observed); run once, not per class.
- `extract_event_candidates.py`: cannot bind a literal to an emitter (that is `U-20`).

## Tests
`19_TESTS/test_mission06_semantics.py` (21 tests) validates consistency between these outputs and the
documents; see `20_FINAL_AUDIT/119_FINAL_REPRODUCIBILITY_REPORT.md` for the full command sequence.
