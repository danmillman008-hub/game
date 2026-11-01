# 21 — Unknowns, limits of method, and what would close them

This file exists so that nothing in this report can be mistaken for more than it is. Every item
below is something a competent reader might expect to find and will not.

## 1. Method limits (structural)

| Limit | Cause | Consequence |
|---|---|---|
| No bytecode decompilation | no JDK 17 / JADX in the analysis environment (`morluto/rea` default path unavailable) | control flow inside methods is not readable; findings rest on literals, class names, `toString` templates and resource data |
| Obfuscation | Smob v4.6 + R8 repackaging to single letters | 26,321 of 29,454 classes are unnamed; the DSL parser, several view models and the executor glue are among them |
| No runtime observation | mission rules: static analysis only, no account, no instrumented device | all server behaviour is inferred from client contracts |
| No server access | same | response bodies, algorithms, thresholds and prices are unknown |
| Annotation parsing | hand-written DEX annotation parser failed on malformed alignment | HTTP **verbs** remain inferred, not verified (paths are verified) |

## 2. Product/behaviour unknowns (12 questions a one-hour instrumented run would answer)

1. **Remote-config precedence** between Firebase RC, `/v2/client-config` and content experiments
   when they disagree. (Most important open question in §15.)
2. **Where streak state lives**: no streak endpoint exists in the 71 paths; it arrives inside the
   progress response, `/v2/client-config`, or `/v1/user/activity` — unknown which.
3. **The exact fast-mode trigger** (pace threshold, window, persistence).
4. **Smart-practice selection algorithm** and its price (coins? keys? Pro?).
5. **Whether `fillTheGap` accepts typed input** and what the "partial match" tolerance is in
   `validated_input_partial_match_feedback_text_the_correct_answer_is`.
6. **Whether content packs are integrity-signed** before the live-preview unzip renders them.
7. **Whether certificate generation is triggered server-side on completion** or on demand.
8. **Which languages get the 2 extra tutorials** (it/pl/tr/id measured) and why — localisation
   policy or experiment?
9. **The AI tutor's model, temperature, and system-prompt ordering** (only the injected
   fragments are visible, not the final assembled prompt).
10. **Whether `isPro` UI state is ever used without a server entitlement check** (the dev menu can
    fake it, but production paths were not traced).
11. **The content experiment `visibilityPercentage` bucket source** (device id? account id? random
    per install?).
12. **Whether the 42 solution-less executable lessons are intentional** (e.g. free-form projects)
    or a content defect.

## 3. Screens/UI unknowns

* Bottom-navigation **tab labels** are not app strings (icon-only or server-provided) ⇒ tab
  composition is inferred from `NavigationBar` behaviour, not read.
* `Compose` screens are unenumerable at scale: only 4 name-visible composables; the rest are
  lambdas inside obfuscated classes.
* Exact **lesson chrome layout** (editor heights, console split) is only partly derivable from
  809 layouts + dimens; no rendering was done.
* Onboarding **step order** is derived from fragment names + string families + a single
  navigation graph whose edges were not decompiled. It is plausible, not proven.

## 4. Data unknowns

* Full field lists for most of the 265 recovered contracts are **partial**: `toString` templates
  only carry fields that are printed, and nested/value-class fields may be omitted.
* Room entity **column types on disk** (affinity, indices) are known from `CREATE TABLE` only;
  no indices are declared beyond primary keys.
* Actual **publish-set history** (753 now; previous values, migration rules) is unknown.
* **Server-side test generation** for executable lessons: `solvedContent` is the input, but the
  transformation into `tests[]` is server code.

## 5. Claims deliberately NOT made

* No claim that Mimo uses Hilt/Dagger — only `*_Factory` naming exists, which is insufficient.
* No claim about certificate pinning being configured.
* No claim about Play Integrity/SafetyNet usage (`IntegrityManager` literals unattributed).
* No claim that `avd_*` strings indicate vendor tooling (they are playback-service defaults).
* No claim about prompt content beyond the fragments quoted; no reconstruction of the full
  system prompt.
* No server behaviour asserted as fact anywhere; inferences are labelled `(I)`.

## 6. What would raise confidence

| Goal | Method | Effort |
|---|---|---|
| Read control flow | JDK 17 + JADX on the 12 DEX files (the `rea` default) | hours |
| Verify verbs + bodies | Instrument a proxy on a rooted test device with a consented account | hours |
| Verify prompts | Extract the assembled request body from the SSE call | minutes-hours |
| Verify tab set + layouts | Screenshot pass over 20 flows | hours |
| Verify economy math | Controlled play with dev-menu overrides | days |
| Verify content pipeline | Author a test lesson and observe live deploy | hours (needs authoring access) |
