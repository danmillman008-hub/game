# mission-08 — deep code coverage & behaviour closure

A reconstruction of Mimo 9.35's *behaviour* (not another inventory), continuing from the verified Mission-7
commit. Everything here is derived from the authorised APK's bytecode and resources; nothing was executed.

## Where to start

| If you want… | Read |
|---|---|
| the honest state of the mission | `STATUS.md` |
| what was wrong in the earlier missions and why | `00_BASELINE/HISTORICAL_FINDINGS_RECONCILIATION.md` |
| every Mission-7 number, recomputed | `00_BASELINE/HISTORICAL_COUNT_AUDIT.md` |
| how the 2,178-class queue was prioritised | `01_DEEP_CLASS_INVESTIGATION/01_PRIORITISATION_METHOD.md` |
| worked per-class records (23 points each) | `01_DEEP_CLASS_INVESTIGATION/04_DEEP_CLASS_INVESTIGATION.md` |
| the typed call graph and its confidence rules | `02_METHOD_RELATIONSHIPS/03_EDGE_CONFIDENCE_MODEL.md` |
| how tokens work in this app | `05_AUTHENTICATION_CLOSURE/01_TOKEN_PROVIDER_AND_LIFECYCLE.md` |
| the interceptor chain | `05_AUTHENTICATION_CLOSURE/02_INTERCEPTOR_CHAIN.md` |
| stage-by-stage narrative | `STAGE_A_REPORT.md` … `STAGE_D_REPORT.md` |

## Directory map

```
00_BASELINE/                 phase 0 — registers, reconciliation, tool status, regression results
01_DEEP_CLASS_INVESTIGATION/ phase 1 — prioritisation, renamed-app register, method status, caveats
02_METHOD_RELATIONSHIPS/     phase 2 — typed edges (gzipped), confidence model, data flow
05_AUTHENTICATION_CLOSURE/   phase 5 — token provider, interceptor chain, session machine
evidence/                    raw dumps cited by the above
tools/                       deterministic builders (see below)
```

`STATUS.md` lists the phases that do not exist yet; nothing is stubbed to look finished.

## Tools

| Tool | Purpose | Verified |
|---|---|---|
| `tools/dex_inspect.py` | per-class methods/instructions/strings; `--scan` literal search; `--scan-methods`; `--queue-csv --coverage` | yes |
| `tools/build_canonical_registers.py` | rebuilds the 39-question and 45-domain registers and the count audit | yes |
| `tools/build_m8_class_investigation.py` | role/priority categorisation of the 2,178 queue | yes |
| `tools/build_renamed_app_register.py` | finds app classes outside the `com.getmimo` namespace (1,148) | yes |
| `tools/build_method_status_register.py` | 11-value method status with caller/callee/test/evidence attributes | yes |
| `tools/build_call_graph.py` | typed call graph with confidence | yes |
| `tools/recover_method_names.py` | recovers original method names from orphan lambda binary names | yes |

All require only `python3` + androguard 4.x (`/tmp/venv`). No JVM, no jadx, no device.

## Reproduction (typical)

```bash
cd mimo-re/mission-08
/tmp/venv/bin/python tools/build_canonical_registers.py
/tmp/venv/bin/python tools/dex_inspect.py --dex-dir /tmp/x --class ku.a --instructions \
    --out evidence/DEX_ku.a_access_token_provider.json
/tmp/venv/bin/python tools/build_call_graph.py --dex-dir /tmp/x --out 02_METHOD_RELATIONSHIPS --scope app
/tmp/venv/bin/python -m pytest ../mission-07/20_TESTS ../mission-06/19_TESTS -q
```

Inputs are the 12-dex set (`/tmp/x`), the decompiled tree (`/tmp/dad`) and the decoded resources (`/tmp/res`);
their regeneration commands are in `../mission-05/21_AUTOMATED_VALIDATION` and
`../mission-07/19_TOOLS/123_REPRODUCIBILITY_COMMANDS.md`.

## Evidence rules used throughout

* a claim cites an instruction, a method and a file — or is labelled `UNKNOWN`/`NOT_RECOVERED`/`BLOCKED`;
* `decompiled` ≠ read, `indexed` ≠ understood, `endpoint` ≠ called;
* merged classes (`47`) are only discussed per method/branch;
* renamed classes (`1,148`) are treated as app code when their code references app types;
* no token, credential or PII value is recorded anywhere.
