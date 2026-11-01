# Mission 8 — Stage C Report (Phase 2: method relationships)

**Status:** complete for the static scope · **Base:** Stage B commit `6cb19df`

## Delivered

| File | Content |
|---|---|
| `02_METHOD_RELATIONSHIPS/01_CALLER_CALLEE_ANALYSIS.md` | 85,724 edges / 138,025 call sites; hubs; token fan-in before/after merged-class correction; non-edges |
| `02_METHOD_RELATIONSHIPS/02_TYPED_GRAPH_EDGES.csv.gz` | the full typed graph (gzipped, 913 KB) with kind, confidence, call-site counts and per-edge evidence text |
| `02_METHOD_RELATIONSHIPS/02_EDGES_FOCUS_EXTRACT.csv` | 741 edges touching the ten focus classes, readable without decompression |
| `02_METHOD_RELATIONSHIPS/03_EDGE_CONFIDENCE_MODEL.md` | nine edge kinds, HIGH/MEDIUM/LOW rules, the merged-class fan-in trap, reflection policy |
| `02_METHOD_RELATIONSHIPS/04_CONTROL_FLOW_AND_ASYNC_ORDERING.md` | synchronous shapes, Flow/listener split, 3 evidenced ordered chains, 5 explicit ordering unknowns |
| `02_METHOD_RELATIONSHIPS/05_DATA_FLOW.md` | DF-01…DF-07 with step-level evidence |
| `02_METHOD_RELATIONSHIPS/06_CALLBACK_AND_FRAMEWORK_ENTRYPOINTS.md` | 327 callback registrations, framework-entry table, why 269 methods have zero callers |
| `02_METHOD_RELATIONSHIPS/07_GRAPH_FINDINGS.md` | 7 established findings, 6 refused claims, downstream consumers |
| `tools/build_call_graph.py` | deterministic extractor |

## Numbers

`platform 24,186 · static 22,373 · virtual 20,800 · direct 15,319 · interface 2,243 · super 475 · callback 327 ·
dynamic 1` — confidence `HIGH 39,935 · MEDIUM 45,407 · LOW 382`.

## Findings worth carrying forward

1. **No app class is invoked statically but missing from the dex** — the "missing owners" of Phase 1 are reached
   only through interfaces/inheritance. Renaming left behaviour intact.
2. **Blocking is rare and concentrated**: two `Tasks.await` sites in the whole app namespace, one of them the
   token provider; everything else composes through Flow (246 `collect`) or Task listeners.
3. **Merged classes poison fan-in statistics** — `ku.a` looks like the most called class in the app until you
   restrict to method `d(Z)`, where the real app fan-in is nine call sites.
4. **Account deletion copies the access token into WorkManager input data** with a `CONNECTED` constraint.
5. **Reflection is entirely library-internal** in the app namespace: no dynamic class resolution to account for.

## Not claimed

No method was promoted to `CALL_GRAPH_TRACED` in this stage (that requires per-method caller *and* callee
enumeration, which Phase 3 performs subsystem by subsystem). No runtime ordering is asserted anywhere.
