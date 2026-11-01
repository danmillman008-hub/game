# 00 — Executive summary

**Subject:** Mimo (`com.getmimo`) 9.35, versionCode 1792759685, APK 142,353,499 bytes,
`sha256 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`.
**Scope:** static, offline reverse engineering of the shipped artefact only. No server was
contacted, no account was used, no protection was circumvented.
**Method:** Android resource/DEX analysis (Androguard 4.1.4 + targeted binary parsers in
`tools/`), plus at-scale analysis of the 10 bundled curriculum packs. JADX/JDK 17 (the
`morluto/rea` default path) is **not available in this environment**; the consequence is
recorded in §21 and in every section that depends on bytecode-level control flow.

## 1. What Mimo is, mechanically

Mimo is a **content-driven mobile learning client for a server-authored curriculum**. The app
itself contains almost no course design: it ships 19 learning paths, 1,029 tutorials,
1,947 chapters and 18,272 lesson slots per language pack, all as JSON + an XML-like
lesson markup language, and renders them with a small number of specialised lesson engines
(interactive markup player, executable-code player, quiz/selection player). Everything that
looks like "curriculum intelligence" — which lesson comes next, whether an answer is right,
how many keys you have left, which experiment you are in — is decided by a mix of client
rules and server responses, and this report separates the two in every case.

## 2. Ten findings that determine any reuse

| # | Finding | Evidence class | Why it matters |
|---|---------|----------------|----------------|
| 1 | The lesson format is a **closed XML-like DSL** with a 3-value visibility enum (`always` / `wrong` / `correct`); 0 unknown tags and 0 unknown attributes across 18,272 lessons. | VERIFIED STATIC | The DSL is small enough to reimplement, and its closedness is what makes an engine feasible. |
| 2 | Answer validation for fill-the-gap uses **character offsets into a flattened code string** (`startIndex`/`endIndex`): 17,526/17,526 ranges are in bounds under the rule "concatenate `<text value>`; `<text type="break">` = `\n`". | VERIFIED STATIC | This is the single most reused mechanism: a correct model of `flatten()` gives exact answer checking with no fuzzy matching. |
| 3 | Executable lessons are graded **server-side**: `POST …/runFiles` returns `ExecuteFilesResponse(hasPassed, hostedProjectUrl, consoleOutput, error, tests[ExecuteLessonTestCase(hasPassed, description, error)])`, rendered as `%d/%d checks passed` and `Condition %d`. | VERIFIED STATIC (contract) / INFERRED (grading implementation) | Client-side grading cannot be reproduced offline; any transfer must own an executor + test runner. |
| 4 | The AI tutor is a **streaming chat** (`POST /v1/aiTutor/conversations`, `Accept: text/event-stream`) with two prompt shapes (`SystemMessage$Interactive`, `SystemMessage$Executable`) that inject lesson context and `expectedAnswer` inside `{{{ … }}}` fences; first 5 questions free, gated by `feature_flag_ai_tutor_android`. | VERIFIED STATIC (prompts, transport, quota) / INFERRED (model, server policy) | Prompt architecture can be reused directly; the model is server-side and unknowable from the APK. |
| 5 | Gamification is a **closed economy of five currencies** — XP (sparks), coins, keys, streak (with freeze/repair/challenge) and league rank — each with its own server endpoint and its own local projection. | VERIFIED STATIC | Cheap to copy conceptually, expensive to balance; the report gives the exact formulas that are observable and marks the rest unknown. |
| 6 | Progress state is a **Room database plus an outbound queue** (`lesson_progress.in_queue`, `LessonProgressQueue`, WorkManager). Content identity is `(lessonId, tutorialVersion, publishSetVersion)`. | VERIFIED STATIC | Explains how the app survives content updates; the version triple is the key transferable design idea. |
| 7 | Content ships **per language** as independent packs (`assets/lessons-<lang>/`), all at `publishSetVersion 753`; 6 of 10 packs have 1,029 tutorials, 4 have 1,031. | VERIFIED STATIC | Pack-level distribution + a global publish-set version is the whole content pipeline in two sentences. |
| 8 | A **55-class Developer Menu** is present in the production build (live content download, remote-config override, fake leaderboards/streak, discount forcing, experiment switching, modal gallery). | VERIFIED STATIC | Highest-value operational tool in the app, and a security note: it is reachable only from debug-gated UI paths (none exported), but the code and its network hooks ship. |
| 9 | The API surface is ~71 path literals **declared as Retrofit annotations** — provable because none of them has any `const-string` reference in any of the 12 DEX files. | VERIFIED STATIC (paths) / INFERRED (verbs, payloads) | Gives a near-complete endpoint catalogue with high confidence on paths and low confidence on methods. |
| 10 | 55 MB of obfuscation: 29,454 classes of which only 3,133 keep `com.getmimo` names; the DSL parser, executor glue and many view models are repackaged to single letters. | VERIFIED STATIC | Sets the resolution ceiling of this whole exercise: behaviour is recoverable from literals + contracts, not from readable control flow. |

## 3. The five engines, in one line each

1. **Curriculum engine** — manifest of paths → sections → tutorial IDs (`startIndex`/`endIndex`
   per section, verified consistent in all 19 paths), tutorial files loaded lazily from the
   language pack, chapters typed `practiceLevel1..3` / `challengeLevel0..2`.
2. **Lesson DSL engine** — markup parsed into modules (`<p>`, `<code>`, `<interaction>`,
   `<selection>`, `<output>`, `<database>`), each module carrying a visibility rule and,
   for assessed modules, an answer model.
3. **Validation/execution engine** — two grading paths: local offset matching for interactive
   lessons, remote file execution for executable lessons with per-test feedback.
4. **Progression/economy engine** — sparks → daily goal → coins → store; keys gate lessons;
   streak/challenge/league/leaderboard drive retention; all server-authoritative with local
   optimistic projection.
5. **Content operations engine** — publish sets + language packs + `DeveloperMenu` live
   preview over Pusher, with experiments able to swap a whole track for a variant.

## 4. Architecture in one paragraph

Orbit-MVI + Redux-Kotlin over a Room cache, with Retrofit/kotlinx.serialization transport,
WorkManager for deferred progress sync, a Jetpack-Compose layer that coexists with 809 XML
layouts and 55 Activities, Firebase (Auth, Messaging, Remote Config, In-App Messaging),
RevenueCat for entitlements, Adjust + Mixpanel for attribution/analytics, Customer.io for
lifecycle messaging, Glance for the streak widget, and Rive for the streak/chapter-end
animations. The app is a **thin, heavily instrumented client for a fat content-and-economy
backend**; that single sentence is the most important architectural fact for anyone porting it.

## 5. What transfers to a Konkur (Iranian university-entrance) product

Transfer is **not** about copying screens. Three mechanisms carry most of the value:

* **The lesson DSL + offset validation** (Mode A: direct learning) — because it makes
  authoring cheap and grading exact without a code sandbox.
* **The curriculum/publish-set model** (all three modes) — because an exam product lives or
  dies on content versioning and on being able to re-plan a study path mid-course.
* **The economy-with-server-authority pattern** (gamification across A/B/C) — because
  Iranian users are extremely price- and value-sensitive; keys/coins/streak translate well,
  while leagues and social features need different framing for the Konkur audience.

Section 19 gives the full 40-row transfer matrix with `Reuse / Adapt / Exclude` verdicts.
Items to **exclude** outright: the AI tutor's free-text chat in its current form (cost +
moderation + Persian quality risk), the entire paid-store/RevenueCat subtree (no IAP channel),
Adjust/Facebook attribution (blocked/unusable), and the code-execution engine (Konkur is
not a programming exam).

## 6. Confidence statement

* Paths, screens, tokens, content structure, DSL grammar, data contracts, Room schema,
  endpoint literals: **VERIFIED STATIC** and reproducible with `tools/`.
* Control flow inside obfuscated classes, server-side algorithms, prompt injection order,
  rate limits, paywall economics: **INFERRED** or **UNKNOWN**, labelled as such in place.
* Zero findings here come from runtime observation; §21 lists the 12 questions that a
  rooted-device or instrumented run would answer in an hour, and that this analysis cannot.

## 7. How to read this report

`01`→`18` are descriptive and build up the system bottom-up (inventory → screens → design →
curriculum → DSL → validation → tutor → difficulty → economy → content ops → dev menu →
persistence → API → config → offline → security → architecture). `19` is the product-decision
document. `20` is the evidence index, `21` the honest list of what is not known.
