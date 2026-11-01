# Phase 1.1 — How the 2,178-class queue is categorised and prioritised

**Input:** `mission-07/01_CLASS_UNIVERSE/04_DEEP_INVESTIGATION_QUEUE.csv` (2,178 rows, unmodified)
**Tool:** `tools/build_m8_class_investigation.py` (deterministic; re-runnable)
**Outputs:** `02_CLASS_CATEGORISATION.csv`, `03_PRIORITISED_QUEUE.json`, `evidence/PHASE1_CLASS_FACTS.jsonl`

Nothing here is decided from a class *name* alone. Each row is built from the class's own DEX
record: superclass, interfaces, field count, method list, instruction count, the packages it actually
invokes, and the string literals it contains.

---

## 1. Role before priority

Mission-7's queue mixes value objects, lambdas and real logic. Priority is therefore assigned in two
steps: **role** (what the class structurally is) first, **domain** (which subsystem it participates in)
second.

| Role | Rule (structural, measured) | Count |
|---|---|---|
| `component` | superclass is `Service`, `Worker`, `CoroutineWorker`, `Application`, `BroadcastReceiver`, `Activity`, `ComponentActivity`, `Fragment` or `ViewModel` | 3 |
| `logic` | has at least one method that is not a getter/setter/`equals`/`hashCode`/`toString`/`copy`/`componentN` **and** either name-suffix is one of `…Repository/DataSource/Interceptor/Client/Api/Mapper/UseCase/Manager/Publisher/Handler/Provider/Coordinator/Engine/Controller/Parser/Renderer/Grader/Checker/Store/Cache` or the body exceeds 40 instructions | 378 |
| `value` | every method is a getter/setter/`equals`/`hashCode`/`toString`/`copy`/`componentN`, or ≤ 40 instructions and no logic suffix | 280 |
| `enum` | superclass is `java.lang.Enum` | 53 |
| `lambda` | name contains `$` (Kotlin lambda / anonymous class) | 1,464 |

## 2. Priority rules (published, applied mechanically)

| Priority | Rule | Count |
|---|---|---|
| **P0** | app-named class, role `logic`/`component`, domain ∈ {auth, learner, lesson, ai, realtime, push, navigation, di} | **45** |
| **P1** | app-named class, role `logic`/`component`, domain ∈ {network, storage, content, subscription, analytics} or otherwise unclassified logic | **84** |
| **P2** | app-named but role `value`/`enum` | **212** |
| **P3** | lambda, library (`androidx`, `com.google`, `kotlin`, `okhttp`, `retrofit2`, `facebook`, `pusher`, `app.rive`, `revenuecat`), obfuscated short name, or class not present in the dex pool | **1,837** |
| | **total** | **2,178** |

`P0 = 45` is small on purpose: a priority that names 500 classes is not a priority. The 45 are the
classes where a behaviour claim must be reconstructable end-to-end.

Of the 45 P0 classes: **43 are `logic`, 2 are `component`** (`NotPremiumNotificationService`,
`MimoFirebaseMessagingService`), and **0 are DEX-only** — the P0 set happens to be fully inside the
1,119 classes that DAD could decompile. That is a property of the queue's selection, not of the app.

## 3. The queue is not the app (measured defect)

Membership test against `02_COMPLETE_CLASS_INVENTORY.csv` (which is byte-identical in content to the
dex pool: 29,454 names, symmetric difference **0**):

| Class | In inventory? | In queue? |
|---|---|---|
| `com.getmimo.data.source.remote.account.AccountRepository` | **no** | no |
| `com.getmimo.ui.authentication.AuthenticationViewModel` | **no** | no |
| `com.getmimo.data.source.local.aitutor.AiTutorRepository` | **no** | no |
| `com.getmimo.data.source.remote.pusher.PusherConnectionManager` | **no** | no |
| `com.getmimo.data.source.remote.keys.DefaultKeysRepository` | **no** | no |
| `com.getmimo.data.notification.MimoFirebaseMessagingService` | yes | yes |
| `com.getmimo.ui.lesson.interactive.base.c` | yes | yes |

The first five are classes whose *lambdas* exist in the dex
(`…AccountRepository$deleteAccount$2`, `…AuthenticationViewModel$firebaseAuthWithFacebook$1`) while the
outer class does not. They are not missing from the extraction: the extraction is complete. They are
**renamed** — the same class exists under a short obfuscated name and references the original name only in
its lambdas' binary names.

Consequence: `com.getmimo.*` is **not** an ownership criterion. Ownership must be decided from evidence
(does the code reference app types?), which is what
`tools/build_renamed_app_register.py` does — it finds **1,148** short-named classes whose instructions
reference `com/getmimo/` types (see `05_RENAMED_APP_LOGIC_REGISTER.csv`).

## 4. What this means for the rest of the mission

1. **Two investigation registers, not one.** `02_CLASS_CATEGORISATION.csv` covers the Mission-7 queue;
   `05_RENAMED_APP_LOGIC_REGISTER.csv` covers the renamed app classes the queue structurally cannot see.
2. **Priority is a claim about behaviour, not about fame.** A P0 class must reach
   `BEHAVIOUR_RECONSTRUCTED` (or be explicitly `BLOCKED` with the reason) by the end of Phase 12.
3. **Domain labels are advisory.** They come from path tokens; a class that is mislabelled as `analytics`
   cannot thereby escape inspection if it turns out to move learner state.
4. **No row is deleted.** A class that turns out to be irrelevant stays in the CSV with its role and an
   explicit reason in Phase 10.

## 5. Reproduction

```bash
cd mimo-re/mission-08
/tmp/venv/bin/python tools/build_m8_class_investigation.py --dex-dir /tmp/x --src-dir /tmp/dad \
  --queue ../mission-07/01_CLASS_UNIVERSE/04_DEEP_INVESTIGATION_QUEUE.csv \
  --out 01_DEEP_CLASS_INVESTIGATION
/tmp/venv/bin/python tools/build_renamed_app_register.py --dex-dir /tmp/x --src-dir /tmp/dad \
  --out 01_DEEP_CLASS_INVESTIGATION
```
