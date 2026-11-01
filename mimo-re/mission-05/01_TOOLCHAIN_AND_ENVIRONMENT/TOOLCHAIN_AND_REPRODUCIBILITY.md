# Mission 5 — Toolchain and Reproducibility Manifest (Phase 1)

## Scope
Document every tool actually used, the tool that could not be obtained, the commands, the input
hashes and the output hashes, so that any third party can repeat the extraction.

## Method
`which`/`--version` probes for every candidate tool; PyPI installation inside `/tmp/venv`;
execution of the mission-05 tools with `--help` and real runs; `sha256sum` over dex inputs
(recorded inside each manifest).

## Sources
- `evidence/DECOMPILE_MANIFEST_APP.json`, `..._BATCH1.json`, `..._BATCH2.json`,
  `..._ANALYTICS.json`, `..._GHOST_SDK.json` (each embeds per-dex SHA-256, versions, timings, peak RSS).
- `evidence/ANNOTATIONS_V2.json`, `evidence/API_CATALOG_V2.json` (summaries of the two new tools).

## Findings — available
| Tool | Version | Role |
|---|---|---|
| python | 3.11.2 | runtime |
| androguard | 4.1.4 (`/tmp/venv`) | DEX parsing, DAD decompiler, xrefs |
| pytest | (venv) | validation suite |
| `nm`, `readelf`, `objdump`, `strings` (binutils) | system | native `.so` inspection |
| `git`, `gh` | system | VCS / PR |

## Findings — unavailable (distinguished from impossible)
| Tool | Status | Consequence |
|---|---|---|
| JDK / `java` / `javac` | **unavailable** | no JADX, no apktool, no baksmali/aapt2 |
| JADX 1.5.1 | **unavailable** — release-asset host aborts TLS from this sandbox | replaced by in-process androguard DAD |
| `dot` (graphviz), `mmdc` (mermaid-cli) | **unavailable** | diagrams stay editable sources (Mermaid/DOT/JSON), no rendered bitmaps |
| emulator / `adb` / physical device | **unavailable** | every runtime claim is BLOCKED, never "verified at runtime" |

The absence of a JDK is **not** a blocker for Java-level reading: the DAD decompiler reconstitutes
Java-like source in-process. It *is* a blocker for smali-grade fidelity (`baksmali`), for resource
decoding (`aapt2`) and for anything requiring the app to execute.

## Findings — new tools authored in this mission
| Tool | Purpose | Determinism |
|---|---|---|
| `tools/decompile_apk.py` | batch DAD decompilation to an **out-of-repo** directory; emits class inventory + manifest (dex sha256, versions, timings, RSS) | sorted output, no timestamps inside sources |
| `tools/find_refs.py` | instruction-level xref: descriptor substrings **and** `const-string` literals → class/method/offset | deterministic ordering |
| `tools/extract_annotations_v2.py` | corrected DEX annotation extractor (class/field/method/**parameter**) | sorted rows |
| `tools/build_api_catalog_v2.py` | joins annotations + descriptors + signatures + parameter bindings into an API catalogue with verb evidence | sorted rows |
| `tools/build_dto_catalog.py` | expands every referenced DTO into its field list | sorted rows |
| `tools/build_report.py` | deterministic HTML index over the mission's documents and evidence | sorted, no timestamps |

Defect fixed: mission-04's parameter-annotation pass fed an `annotation_set_ref_list` offset to the
`annotation_set_item` reader, producing 162 garbage rows. `extract_annotations_v2.py` parses the
reference list correctly → **105 valid parameter-annotation rows** (`evidence/ANNOTATIONS_V2.csv`).

## Findings — decompilation coverage this mission
| Batch | Classes | With source | Methods | Source bytes | Time | Peak RSS | Manifest |
|---|---|---|---|---|---|---|---|
| app (`Lcom/getmimo`) | 3,133 | 3,133 | 12,851 | 8,121,129 | 51.7 s | 2,752 MB | `DECOMPILE_MANIFEST_APP.json` |
| obfuscated batch 1 (`te/`, `ku/`, `dh/`, `hg/`, `ie0/`) | 42 | 42 | 88 | 78,401 | 36.7 s | 2,577 MB | `..._BATCH1.json` |
| obfuscated batch 2 (`qm/ gm/ im/ nm/ pm/ cg/ th/ ie0/ ka0/ jm/ ze/ v80/ dh/ hg/`) | 129 | 129 | 444 | 253,574 | 35.2 s | 2,581 MB | `..._BATCH2.json` |
| analytics nested types | 13 | 13 | 55 | 36,102 | 35.6 s | 2,575 MB | `..._ANALYTICS.json` |
| `bin/ghost` native bridge | 6 | 6 | 51 | 15,223 | 35.4 s | 2,575 MB | `..._GHOST_SDK.json` |
| **total** | **3,323** | **3,323** | **13,489** | **8,504,429** | — | — | — |

Decompiled Java is deliberately written to `/tmp/dad`, **outside** the repository (RULE 6): only
derived inventories, manifests and catalogues are committed.

## Evidence labels
Tool availability, versions, hashes, timings, and the counts above: **VERIFIED_STATIC**.
"JADX would produce more faithful output" is **INFERRED_HIGH** (general property of DAD vs JADX).

## Limitations
- DAD output is pseudo-Java: it drops modifiers it cannot reconstruct, reuses local names across
  branches, and prints placeholders such as `v0_1 = ;`. Every load-bearing claim in this mission was
  therefore cross-checked against **string literals, method descriptors, annotations or second call
  sites**, not against the shape of the pseudo-Java alone.
- `DvClass.process()` swallows per-method failures, so "with source" means *a class file was
  emitted*, not *every method rendered*.
- xref readiness costs ~35 s per DEX load; batching is mandatory (peak RSS ~2.6 GB).

## Unresolved
- No smali-level verification (baksmali impossible without a JDK). Register: `UNRESOLVED_REGISTER.csv` #U-04.
- No resource-table decoding (strings/themes) — limits the UI matrix to code-visible state.

## Reproduction
```bash
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install androguard==4.1.4 pytest
/tmp/venv/bin/python tools/decompile_apk.py --dex-dir /tmp/x --out /tmp/dad \
  --filter 'Lcom/getmimo' --inventory evidence/CLASS_INVENTORY_APP.csv \
  --manifest evidence/DECOMPILE_MANIFEST_APP.json
/tmp/venv/bin/python tools/extract_annotations_v2.py --dex-dir /tmp/x \
  --csv evidence/ANNOTATIONS_V2.csv.gz.gz --json evidence/ANNOTATIONS_V2.json
/tmp/venv/bin/python tools/build_api_catalog_v2.py --annotations evidence/ANNOTATIONS_V2.csv \
  --csv evidence/API_CATALOG_V2.csv --json evidence/API_CATALOG_V2.json
```
Expected: 3,133 classes / 12,851 methods; 62 endpoints with verbs `GET 28 · POST 24 · PATCH 4 · DELETE 4 · PUT 2`.
