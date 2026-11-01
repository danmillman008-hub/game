# Phase 1.7 — Method-body investigation: Java, DEX, and when neither is enough

## 1. Why a second source is mandatory

| Measurement | Value |
|---|---|
| queue classes with a decompiled `.java` | 1,119 |
| queue classes **without** any `.java` (DEX-only) | **1,059 (48.6 %)** |
| decompiled files in `/tmp/dad` | 3,284 |
| decompiled files containing syntactically invalid fragments (`= ;`) | **431 (13.1 %)** |

The second row means half the queue has no readable body through the decompiler. The last row means a further
seventh of the *available* bodies cannot be trusted as Java: DAD emits statements such as

```java
public j(byte p8) {
    this.a = p8;
    switch (p8) {
        case 13:
            f9.j v3_1 = ;            // <- unparseable: the assignment target is missing
            long[] v8_21 = java.util.Collections.EMPTY_LIST;
            v3_1.b = v8_21;
```

For merged/tagged classes the decompiled output is *indicative but not authoritative*. Mission-8 therefore treats
`decompiled_java` and `dex_instructions` as two sources with different failure modes, and records which one each
claim rests on (`06_METHOD_STATUS_REGISTER.csv`, column `source_basis`).

## 2. Reading a body at DEX level

`tools/dex_inspect.py --class <name> [--instructions]` prints, per method: descriptor, register count,
instruction count, every `const-string`, every `invoke-*` target with its invoke kind, and every field access.
That is enough to reconstruct data flow for straight-line methods, which is most of the interesting ones.

Worked example — `ku.a.d(Z)Ljava/lang/String;`, 83 instructions, abbreviated to the decision skeleton:

| Instruction | Reading |
|---|---|
| `iget-object v6 … Lku/a;->a Ljava/lang/Object;` + `check-cast … FirebaseAuth` | the field holds a `FirebaseAuth` |
| `iget-object v6 … FirebaseAuth;->f Lcom/google/firebase/auth/FirebaseUser;` | current user |
| `if-eqz v6, +096h` … `const-string "There is no Firebase user!"` … `return-object v0` | null-user exit path |
| `FirebaseAuth;->c(FirebaseUser; Z)Task` with `const/4 v0, 0` | `getAccessToken(false)` |
| `const-string "exp"` → `vu/d;->b Ljava/util/Map;->get` → `check-cast Integer` | read the JWT `exp` claim |
| `new-instance Lorg/joda/time/DateTime;` + `div-long 1000` | compare `exp` (seconds) with `now` (ms / 1000) |
| `if-gez v0, +021h` | fresh token ⇒ skip refresh |
| `FirebaseAuth;->c(FirebaseUser; Z=true)` → `vu/d;->a Ljava/lang/String;` | forced refresh, read token |
| `const-string "Token doesn't exist!"` → `IllegalStateException` → `AccessTokenUnavailableException` | failure type |

No decompiler was used for this method, and none could have been: DAD produced no file for `ku.a`.

## 3. What the DEX path cannot give

* local variable names and types (register numbers and `check-cast` hints only),
* control-flow structure beyond jump offsets (`if-*`, `goto`, `packed-switch`),
* precise try/catch ranges (catch handlers appear in the instruction stream as `move-exception` blocks),
* Kotlin-level constructs (coroutine state machines appear as generated `invokeSuspend` continuations),
* constant-folding the decompiler performed (e.g. `d(0)` for a boolean `false` argument is a decompiler
  rendering; at DEX level it is `const/4 vX, 0`).

The last point is a real trap that already bit Mission-7-adjacent reasoning: a `0` argument is not always an
`int` zero.

## 4. How a body is classified

The 11-value scale is applied **per method** (`06_METHOD_STATUS_REGISTER.csv`), not per class:

| Status | Meaning in practice here |
|---|---|
| `SIGNATURE_ONLY` | abstract/interface or no code object (21 methods in the current register) |
| `BODY_PRESENT_NOT_READ` | code exists; not read in the current phase (561) |
| `JAVA_INSPECTED` | decompiled Java read (2) |
| `DEX_INSPECTED` | instruction stream read (44) |
| `JAVA_AND_DEX_CROSS_CHECKED` | both read and consistent (0 so far — this is deliberate: a class is promoted only when both sources were compared) |
| `BEHAVIOUR_RECONSTRUCTED` | one-sentence responsibility + inputs/outputs/effects (9) |
| `CALL_GRAPH_TRACED` | callers/callees enumerated with evidence (0 so far) |
| `TEST_DERIVED` | a semantic test encodes the behaviour (Phase 13) |
| `RUNTIME_TESTED` | never, in this environment |
| `BLOCKED` | with a reason (none assigned in Phase 1) |

Register totals: 637 methods across 61 classes (45 P0 + 16 hand-picked renamed/app classes).

## 5. Merged classes: investigate the branch, not the class

47 classes were measured to carry a tag-byte constructor with a switch
(`evidence/MERGED_CLASS_REGISTER.json`). For those, a body statement is only valid if it names the tag branch:

* ✅ `f9.j.<init>(B)` **branch 17** creates two `ConcurrentHashMap`s and registers a constant list.
* ❌ "`f9.j` is a Pusher channel registry" — unsupported: the constants it registers come from `m50.g`/`m50.i`,
  which are *not* Pusher types (they are expression/operator helpers), so even the branch-level reading must stop
  at what is actually proven.

An earlier draft of this phase nearly recorded that inference; it was dropped because the evidence did not
support it. That is the intended behaviour of Rule 5.

## 6. Reproduction

```bash
# whole-class instruction dump
/tmp/venv/bin/python tools/dex_inspect.py --dex-dir /tmp/x --class ku.a --instructions \
    --out evidence/DEX_ku.a_access_token_provider.json

# method register
/tmp/venv/bin/python tools/build_method_status_register.py --dex-dir /tmp/x --src-dir /tmp/dad \
    --classes-file 01_DEEP_CLASS_INVESTIGATION/evidence/STATUS_TARGET_CLASSES.txt \
    --overrides 01_DEEP_CLASS_INVESTIGATION/evidence/METHOD_STATUS_OVERRIDES.json \
    --out 01_DEEP_CLASS_INVESTIGATION
```
