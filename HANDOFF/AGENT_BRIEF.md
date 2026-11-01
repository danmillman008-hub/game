# AGENT_BRIEF — what you are building, and the rules that keep it honest

## 1. Mission

Build an independent project at `mimo/` (inside this repository) that implements an **offline learning engine** whose
behaviour is derived from the Mimo reconstruction in `HANDOFF/` + `mimo-re/`. The engine must:

1. load a content pack from local assets;
2. parse lesson documents with the recovered DSL grammar;
3. render every module type;
4. accept the nine interaction types;
5. grade with the recovered algorithm (including the three-way verdict);
6. produce the three feedback states and apply visibility gating;
7. persist learner state locally with the recovered entity/queue semantics **plus** the declared additions;
8. expose an acceptance-test entry point that reproduces `HANDOFF/data/*_vectors.json`.

## 2. Non-negotiables

| Rule | Meaning |
|---|---|
| **No invention** | every behaviour you implement must cite a spec clause (`02`–`09`) which cites an evidence artifact. If you need something the specs do not define, add it to `mimo/OPEN_QUESTIONS.md` and to `HANDOFF/12_DELTA_REGISTER.md` as an `ADD-*`, do not silently guess. |
| **Static ≠ runtime** | the reconstruction is `VERIFIED_STATIC`. Nothing has been executed. Your implementation is the first execution of these rules; where your tests disagree with the vectors, the vectors win (they are derived from bytecode) and you must record the discrepancy. |
| **Keep the deltas visible** | `12_DELTA_REGISTER.md` lists 45 domain decisions and 8 additions. Do not implement a `DROP` domain by accident and do not skip an `ADD` domain. |
| **No Mimo assets in Git** | original lesson content, images, fonts, animations and the APK itself must never be committed. Use synthetic fixtures derived from `HANDOFF/data/` vectors. |
| **No credentials** | no Firebase project, no tokens, no calls to `api.mimo.org`. The sync layer is optional and, if built, must be pointed at a local mock. |
| **Traceability is mandatory** | every module in `mimo/` carries a header comment naming the spec clause(s) it implements, e.g. `// spec: 04 §3 ValidatedInput verdict`. |

## 3. What you may copy literally

* the grading algorithm (`04_SPEC_INTERACTION_AND_GRADING.md` §2–§4) — it is a closed-form function;
* the outbox state machine (`05_SPEC_LEARNER_MODEL.md` §4) — four statements;
* the schema (`06_SPEC_STORAGE.md` §1) — three tables;
* the grammar (`data/dsl_grammar.ebnf`) — treat it as the contract.

## 4. What you must not copy

* Mimo's UI, branding, illustrations, Rive animations, copy text, icons, sounds;
* Mimo lesson/question content;
* Mimo's server-owned rules (completion, coins, streaks, ETA, leagues);
* Mimo's obfuscated class names (use the glossary's *meanings*, not the identifiers).

## 5. Definition of done

`mimo/` is done when all of the following hold and are demonstrable in one command (`mimo/bin/verify`):

1. `HANDOFF/tools/verify_handoff.py` still passes (you did not break the evidence layer);
2. the acceptance suite in `HANDOFF/11_ACCEPTANCE_TESTS.md` passes against your engine;
3. every `KEEP` / `KEEP_WITH_CHANGES` domain in `spec_deltas.json` has a module that names its spec clause;
4. every `ADD-*` has an implementation and a test;
5. `mimo/TRACEABILITY.md` maps each of your modules to spec clauses, and each spec clause to the evidence artifact;
6. a cold start with the network off renders a track, opens a lesson, grades an answer and persists progress across a
   restart — demonstrated by an automated test, not by a screenshot.

## 6. If you get stuck

Read `13_KNOWN_UNKNOWNS.md` first: 8 questions are explicitly blocked (artifact unavailable) and 24 are partial. If your
blocker is on that list, you are allowed to make a documented decision — mark it `DECIDED_IN_MIMO_BUILD` in
`mimo/OPEN_QUESTIONS.md` with the clause you relaxed. If your blocker is **not** on the list, go back to `14_TRACEABILITY.md`;
the answer is almost always in an artifact you have not opened yet.
