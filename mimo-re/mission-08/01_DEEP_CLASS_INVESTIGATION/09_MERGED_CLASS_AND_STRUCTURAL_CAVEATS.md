# Phase 1.9 — Structural caveats that constrain every later claim

Three properties of this build's bytecode invalidate ordinary reasoning about "classes". They are measured,
not assumed, and each one carries a rule for later phases.

---

## 1. Merged classes: one `class_def` ≠ one original class

**Measurement.** 47 classes have a constructor taking a single `byte` whose body switches on that byte
(`evidence/MERGED_CLASS_REGISTER.json`). Examples: `ku.a` (22 methods spanning Firebase auth, RevenueCat,
Facebook and Coil), `f9.j` (64 methods, tag branches 13 and 17), `a4.i` (39 methods, interfaces
`okhttp3.Callback`, `au.c`, `a90.p`), `cc.b` (62 methods), `di.a` (40 methods).

**Rule.** A behaviour statement about a merged class must name the method (and, where the constructor is
tag-switched, the branch). Otherwise it is `INFERRED` at best and must not be used as an architectural fact.

**Consequence for the class universe.** The Mission-7 counts (29,454 / 3,133 / 1,563 / 13,113 …) are counts of
`class_def` objects, not of original classes. They stay correct as *bytecode* counts and must never be quoted as
"the app has N classes".

---

## 2. Renamed app logic: 1,148 classes hide outside the app namespace

**Measurement.** 1,148 short-named classes contain instructions referencing `Lcom/getmimo/…` types
(`05_RENAMED_APP_LOGIC_REGISTER.csv`); only 36 of them have decompiled Java.

**Evidence that this is renaming, not library code:** `np.b implements np.d` and holds a state flow
(`ya0.c`) that `com.getmimo.data.source.remote.account.a` casts to and collects from; `ku.a` returns
`com.getmimo.data.source.remote.authentication.AccessTokenUnavailableException`; `ri.c` holds
`com.getmimo.network.NetworkState`.

**Rule.** When a behaviour question names an app concept, the search must include the renamed register, not only
`com.getmimo.*`. Phase 3 subsystem dossiers must state which renamed classes they had to pull in.

---

## 3. Orphan lambdas: 1,379 app-named classes whose owner is gone

**Measurement.** Of 2,095 `com.getmimo.*` classes containing `$`, **1,379** have no immediate outer class in the
dex set (e.g. `com.getmimo.App$onCreate$1` exists, `com.getmimo.App` does not;
`com.getmimo.data.source.remote.account.AccountRepository$deleteAccount$2` exists,
`…AccountRepository` does not).

**Consequence.** These are *not* extraction gaps — the extraction is complete (symmetric difference with the dex
set is zero). They are view-models, repositories and UI classes that were renamed while their lambdas' binary
names kept the original text.

**Rule.** An orphan lambda is evidence about the *existence and behaviour of a renamed class*, never about a
class that "is missing from the APK". Missing outer classes must be reported as `RENAMED_OUT_OF_NAMESPACE`,
not as `NOT_RECOVERED`, unless the lambda's callee chain cannot be resolved at all.

---

## 4. Decompiler corruption: 431 of 3,284 Java files are not valid Java

Statements of the form `f9.j v3_1 = ;` appear in 431 files (13.1 %). Any claim resting on such a file must be
re-derived from DEX before it may be labelled `BEHAVIOUR_RECONSTRUCTED`.

---

## 5. What this means for "complete coverage" (Phase 10)

The 29,454 `class_def`s can be partitioned exhaustively, but the partition is not the interesting claim. The
interesting claim is: *every app-behaviour question in the register is answered or explicitly blocked with a
reason*. These caveats exist so that Phase 10's stop rule cannot be satisfied by counting bytes:

| Bucket | Population | Phase-10 obligation |
|---|---|---|
| inspected app logic (named + renamed) | ≤ 2,186 classes | behaviour or explicit exclusion per class |
| orphan lambdas | 1,379 | map to the renamed owner or mark `GLUE_ONLY` |
| merged classes | 47 | per-branch treatment |
| library / framework | ~25,000 | exclusion classes with a stated criterion, not a count alone |
| blocked | any | reason + what would unblock it |
