# Phase 2.3 — Edge types and the confidence model

An edge is recorded **only** when an instruction in the caller's body names the callee. There is no
name-based inference anywhere in `tools/build_call_graph.py`; a class called `…Repository` does not thereby
become "a repository that the ViewModel calls".

## 1. Edge kinds

| Kind | How it is detected | Meaning |
|---|---|---|
| `direct` | opcode `invoke-direct[/range]` | constructor or private call — target is unambiguous |
| `virtual` | `invoke-virtual[/range]` | dynamic dispatch; the callee may be a subclass override |
| `interface` | `invoke-interface[/range]` | call through an interface; implementation unknown from the call site |
| `static` | `invoke-static[/range]` | utility/companion call |
| `super` | `invoke-super[/range]` | superclass implementation |
| `callback` | invoke whose **target method name** matches `set*Listener`, `add*Listener`, `addObserver`, `addCallback`, `subscribe*`, `register*`, `addOn*Listener`, `observe*`, `collect*` | the call *registers* behaviour; the actual invocation happens later in framework code |
| `framework` | callee method name is an Android lifecycle entry point (`onCreate`, `onStartCommand`, `doWork`, `onMessageReceived`, `run`, `invokeSuspend`, …) | invoked by the platform |
| `platform` | callee class is in `java.*`, `javax.*`, `android.*`, `androidx.*`, `kotlin.*`, `org.json.*`, … | body not in the APK by design |
| `dynamic` | callee class is **not** in the dex set and is not a platform namespace | genuinely unresolved target |

## 2. Confidence

| Confidence | Rule | Count (app-scope graph) |
|---|---|---|
| `HIGH` | `direct`/`static`/`interface` edge, callee class present in the dex, callee method matched by descriptor | 39,935 |
| `MEDIUM` | `virtual`/`super` edge, or `platform` edge (the class exists on the device but not in the APK) | 45,407 |
| `LOW` | `callback` edges, `dynamic` edges, and any edge whose callee class is absent | 382 |

`MEDIUM` is not a hedge: a `virtual` edge means "this call site can reach this method", not "this method runs".
`LOW` on `callback` edges is deliberate: `addListener(x)` proves the object is handed to the framework, not that
it is invoked, and never proves when.

## 3. Two structural traps this model exists to prevent

### 3.1 Merged classes make fan-in meaningless

`ku.a` receives 60+ static call sites from `com.google.android.gms.*`, `androidx.datastore.*`, `coil3.*`,
`com.facebook.*`, `com.revenuecat.*`, `io.grpc.*`. None of those are "Mimo calling its token provider": they are
calls to *unrelated methods* that the build fused into the same `class_def` (see
`01_DEEP_CLASS_INVESTIGATION/09_…CAVEATS.md` §1). The app-relevant call sites into `ku.a` are the eight listed in
`07_GRAPH_FINDINGS.md` §3, each identified by *method* `d(Z)Ljava/lang/String;`, not by class.

**Rule:** fan-in/fan-out statistics are only reported per `(class, method)` pair, never per class, and merged
classes are excluded from hub rankings.

### 3.2 Platform edges are not gaps

24,186 of the 85,724 edges point at `java.*`/`android.*`/`kotlin.*` classes. Their bodies are not in the APK
because they are not part of the app. They are kept because they carry data-flow information (e.g.
`StringBuilder.append` chains around a `"Bearer "` prefix), but they can never be resolved further and must not
appear in completeness denominators.

## 4. Reflection

Reflection is recorded as a *signal on the calling method*, never as an invented edge. The scan looks for
`Class.forName`, `Class.getDeclaredMethod`, `Class.getMethod`, `Method.invoke`,
`Proxy.newProxyInstance`, `Constructor.newInstance` and `kotlin/reflect/` type references: **20,599 sites**,
dominated by Gson, Kotlin reflection and Firebase internals. No site in the app namespace was found that resolves
a Mimo class dynamically, so no `reflection` edge exists in the graph.

## 5. What an edge deliberately does not claim

* that the callee executes at runtime (no execution occurred),
* that the call happens on a particular thread,
* that a callback registered at time *t* is invoked at time *t+n*,
* that the observed call site is the only way the callee can be reached (framework entry points, DI, reflection
  and dynamic dispatch are all outside a static call graph).

## 6. Reproduction

```bash
cd mimo-re/mission-08
/tmp/venv/bin/python tools/build_call_graph.py --dex-dir /tmp/x --out 02_METHOD_RELATIONSHIPS --scope app
gunzip -k 02_METHOD_RELATIONSHIPS/02_TYPED_GRAPH_EDGES.csv.gz   # full 85,724-row graph
```
