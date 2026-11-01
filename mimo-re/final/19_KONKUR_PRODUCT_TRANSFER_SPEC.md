# 19 — Mimo → Konkur transfer specification

Target: an Iranian Konkur (university entrance) app with three modes —
**A. LearnHarness** (direct learning), **B. EPM** (exam centre / آزمون آزمایشی),
**C. Study-plan card path** (مسیر کارت‌محور) — and gamification across all three.

This section is decision-oriented. Every row names the Mimo mechanism, what the user sees, how it
is implemented (evidence class), the Konkur equivalent, and a verdict with reason.

## 1. Master transfer matrix (42 rows)

| Mimo feature | mechanism | user-facing behaviour | internal implementation | Konkur equivalent | Reuse / Adapt / Exclude | Reason |
|---|---|---|---|---|---|---|
| Path list (19 tracks) | JSON manifest `tracks.json` | pick a path, see sections | Track→Section→Tutorial, `startIndex/endIndex` (V) | Subject/field tracks (ریاضی/تجربی/انسانی) | Reuse | Exact fit; sections give O(1) resume |
| Tutorial files | one JSON per tutorial, lazy load | instant chapter open | `assets/lessons-<lang>/tutorial-<id>.json` (V) | Chapter packs per subject/year | Adapt | Konkur content changes yearly ⇒ downloadable packs, not APK-bundled |
| Chapter types Level0–3 | authored label | difficulty feel per chapter | 6 enum values, 11,373 L1 lessons (V) | Topic difficulty band for question bank | Adapt | Keep the label, add calibration from attempt stats |
| Lesson DSL | XML-like closed grammar | prose + code + exercises in one scroll | 3-value `visible-if`, 0 unknown tags (V) | Carousel of concept → example → question | Adapt | Add `<equation>`, `<figure>`, RTL markers, negative-marking |
| Fill-the-gap grading | character offsets into flattened text | tap snippets into gaps | `flat[start:end]`, derived answers (V, 17,526/17,526) | Fill-in-the-formula / choose-the-unit | Reuse | Zero-cost exact grading, works offline |
| Validated input | free text vs. code slice | type the answer | same offsets on `<interaction>` (V) | Short numeric/verbal answer | Adapt | Needs Persian normalisation policy |
| Multi-select | one correct item | tap the right answer(s) | `<item correct>`, exactly one correct (V) | MCQ with 4 options + negative marking | Adapt | Add scoring policy & option-shuffle seed |
| `visible-if` remedial blocks | per-module visibility | extra explanation after a mistake | enum always/wrong/correct (V) | Per-option explanation (پاسخ تشریحی) | Reuse | The single best authoring trick in the app |
| Hints ladder | strings + prompt suggestions | "hint" before solution | `interaction_hint_*`, FirstHint/SecondHint (V) | راهنمای گام‌به‌گام | Reuse | Cheap, high perceived value |
| See solution + diff | replace code, show diff | compare your answer | `CodeSwitch(User|Solved)`, confirm dialog (V) | Show full solution after exam | Adapt | Never allow before attempt in EPM |
| Executable lessons | remote code run | run code, see checks | `POST …/runFiles`, `ExecuteFilesResponse`, MFEL (V/I) | — (no coding in Konkur) | Exclude | Different domain; sandbox cost huge |
| Code playground | saved projects | build & share projects | `/v1/code*`, `hostedFilesUrl` (V) | — | Exclude | Out of scope |
| Autosave | continuous buffer + server save | never lose work | `AutoSaveCodeService`, `savefiles` (V) | autosave answers within a simulation | Reuse pattern | Critical for long EPM sessions |
| Practice hub | re-serve chapters + filters | "practise what you learned" | `PracticeContentResponse(chapterId,trackId,tutorialId)`, stats(duration, chapters) (V) | مرور/تمرین by topic | Adapt | Replace selection with weak-topic engine |
| Smart practice | paid re-drill | "master this chapter" | server-selected, charge modals (V/I) | Adaptive drill set | Adapt | Keep flow, make it free-but-limited |
| Hard mode | parallel lesson bodies | harder variant of a lesson | `hardModeContent` on 6,058 lessons (V) | سخت‌تر toggle | Reuse | Pure authoring, no engine cost |
| Fast mode | skip easy slots on pace | "you're breezing through" | client-side slot filter, 26 strings (V/I) | Compress plan near exam date | Adapt | Trigger by days-remaining, not pace |
| Pacing & ETA | server model | "you'll finish by…" | `TrackEtaResponse(pace, sections)` (V) | Study-plan card deadlines | Adapt | Must be deadline-aware |
| Reactivation flow | goal re-negotiation | "ready to continue?" | 22 strings + goal reset (V) | بعد از وقفه | Reuse | Strong retention device |
| Sparks/XP | display currency + daily goal | XP ring, 42sp counter | token `Sparks`, `daily_goal` (V) | XP per solved question | Reuse | Universal motivator, no economy risk |
| Coins | store currency | buy cosmetics/protection | `/v1/user/coins`, `Coins(coins)` (V) | credits for simulations/PDF | Adapt | Cosmetics don't sell in Iran |
| Keys | daily-refilled gate | "3 keys left today" | `/v1/user/keys`, `/consume` (V) | simulation credits | Adapt | Never gate syllabus content |
| Streak | daily consistency | flame + freeze/repair | `Streak(start)`, challenge wager (V) | روزهای مطالعه | Adapt | Add "days to Konkur" framing |
| Streak wager | stake coins on 7 days | risk mechanic | `streak_challenge_prompt_accept = "Accept for %d"` (V) | optional | Adapt | Effective but gambling-adjacent; review |
| League + promotion/demotion | weekly cohort rank | "you're #4, 2 to promote" | `Leaderboard(thresholds, league, freeze)` (V) | class/school ranking | Adapt | Per-cohort leagues need scale; use class |
| Friends leaderboard | social compare | friends list ranks | `/v1/leaderboards/friends` (V) | هم‌کلاسی | Reuse | Cheap and culturally fine |
| Reward box ritual | choose/open/claim | animated prize | `/v1/user/rewards/next|confirm`, Rive (V) | daily reward → insight | Adapt | Keep moment, drop animation |
| Certificates | per-track completion | downloadable certificate | `/v1/tracks/{id}/certificates` (V) | کارنامه/گواهی آزمون | Adapt | Tie to exam readiness, not attendance |
| Chapter-end screen | progress + upsell + ads | "chapter complete!" | 52 strings, native-ad fallback (V) | end-of-session summary | Reuse | Must add accuracy + time metrics |
| AI tutor chat | streaming chat in lesson | ask for help | SSE `/v1/aiTutor/conversations` (V) | AI assistant for concepts | Adapt | Persian quality, cost, moderation; no expected answers in prompt |
| Instant prompts | pre-composed user messages | "explain this error" | `InstantPrompt$ExplainError`, `…Mistake` (V) | "چرا اشتباه بود؟" | Reuse | Highest-value, lowest-cost AI feature |
| Prompt suggestions | FirstHint/SecondHint | suggested questions | `PromptSuggestions` (V) | step hints | Reuse | — |
| AI quota (5 free) | server-counted freemium | "5 free questions" | `messages/count` + Pro (V) | free AI credits | Adapt | Payment friction in Iran |
| Content experiments | track swap + % rollout | see different course | `ContentExperiment(original, variant, useTheVariant)` (V) | pilot a new bank | Reuse | Essential for content risk management |
| Remote discount engine | fully remote offer object | countdown, banner, CTA | `RemoteConfigDiscount(...)` (V) | campaign pricing | Reuse | Iranian pricing changes weekly |
| Remote config | Firebase RC + `/v2/client-config` | features appear/disappear | 2+1 config planes (V) | self-hosted flags | Adapt | One plane only; Firebase unreliable in IR |
| Developer menu | 55 classes in prod | internal control room | `ui.developermenu.*` (V) | internal console | Adapt | Ship only in internal builds |
| Live content deploy | Pusher + unzip unpublished | authors see changes instantly | `AwesomeModePusherUseCase`, download & unzip (V) | staged publish | Adapt | Needs review gate; wrong key = trust incident |
| Room 3-table progress + outbox | `in_queue`, delete-on-success | progress survives offline | Room + WorkManager (V) | attempts + plan cache | Reuse pattern | Best-in-class minimalism; extend with `question_attempt` |
| Version algebra | publishSet + per-entity version | content fixes don't break progress | `(lessonId, tutorialId, tutorialVersion, publishSetVersion)` (V) | blueprint + pack version | Reuse | Critical for yearly syllabus changes |
| Offline degradation | per-surface offline views | consistent message + refresh | 14 `*_offline_*` strings + `/v1/health/connectivity` (V) | same, with visible sync queue | Adapt | Add queue visibility |
| 305-event analytics catalogue | typed properties | (invisible) | `analytics.properties.*` (V) | Konkur event schema | Reuse as spec | Fastest way to define your own |
| Adjust/RevenueCat/Customer.io | third-party stack | (invisible) | 2,436+315+351 classes (V) | self-hosted equivalents | Exclude | Blocked in Iran / compliance |
| Deep links `/learn/*` | wildcard path | open any learning link | `SplashActivity` router (V) | plan-aware deep links | Adapt | Must be typed and validated |

## 2. Mode-by-mode design consequences

### Mode A — LearnHarness (direct learning)
Adopt the **lesson DSL + offset grading + visible-if remediation** almost unchanged. This is the
cheapest high-fidelity part of Mimo to reproduce: the corpus proves the grammar is small (26
tags, 3 visibility values) and self-consistent. Required additions: `<equation>`, `<figure>`,
RTL text markers, Persian normalisation, and per-option ۳-گزینه‌ای negative marking.

Mode A should be **fully offline-capable** (Konkur's network reality) — which Mimo already is for
interactive lessons; only the executable path forces the network, and Konkur excludes that.

### Mode B — EPM (exam centre)
Mimo has **no exam mode**: no timer, no per-question budget, no negative marking, no
seating/section ordering, no post-exam analytics. Everything here is new work. Three Mimo
mechanisms are still directly reusable:
* **progress triple / version algebra** — an exam is pinned to a blueprint version;
* **attempt accounting** (`tries`, `attempts`) — becomes per-question attempt history;
* **outbox sync** — an exam taken offline must queue its result and hash.

The EPM must add what Mimo never had: timing, scoring policy, question-bank rotation,
answer-key versioning, and integrity (signed bundles).

### Mode C — Study-plan card path (مسیر کارت‌محور)
Mimo's closest analogue is the *pacing/ETA + fast-mode + reactivation* cluster, and it is
insufficient: it has no deadline, no per-topic weakness and no session-length model. Build the
card engine on three inputs Mimo does not collect:
`days_to_exam`, `per-topic accuracy with recency decay`, `available minutes/day`.
Reuse from Mimo: the card visual language (12dp cards, 8/12/16/24 spacing), the daily-goal ring,
and the reactivation copy pattern when a day is missed.

### Gamification across A/B/C
| Mode | Primary currency | Secondary | Avoid |
|---|---|---|---|
| A LearnHarness | sparks/XP + streak | keys-as-credits | league (no cohort) |
| B EPM | rank percentile + accuracy badges | coins | streak wager during exam week |
| C Plan cards | completion of today's card | streak | XP inflation (dilutes signal) |

Rule: **one currency per mode, shared balance**. Mimo's five-currency system works because its
content is endless; Konkur's syllabus is finite, so currency inflation would be visible.

## 3. Completeness matrix (brief → section)

| Required area | Covered in | Status |
|---|---|---|
| Component inventory | 01 | ✅ measured |
| Every screen + states | 02 | ✅ 36 activities/22 modals/87 sheets mapped; 4 unlabelled tab labels UNKNOWN |
| Visual design system | 04 | ✅ 234 colours/300 dimens measured; light/night pairing INFERRED |
| Navigation graph | 03 | ✅ + diagram 03 |
| Curriculum engine | 05 | ✅ full track table |
| Lesson DSL spec | 06 | ✅ formal grammar + counts |
| Validation & execution | 07 | ✅ |
| AI tutor prompts/context | 08 | ✅ structure; model UNKNOWN |
| Practice/difficulty/adaptive | 09 | ✅ 4 mechanisms separated |
| Gamification & events | 10 | ✅ 5 currencies + pipeline |
| Content pipeline | 11 | ✅ versions/packs/live-preview |
| Developer menu | 12 | ✅ 55 classes |
| Room schema & state ownership | 13 | ✅ 3 tables |
| API catalogue | 14 | ✅ 71 endpoints |
| Remote config & A/B | 15 | ✅ 3 planes + keys |
| Offline & sync | 16 | ✅ matrix + outbox |
| Security boundaries | 17 | ✅ |
| 16 architecture diagrams | 18 + `diagrams/` | ✅ sources editable |
| Transfer matrix | 19 (this file) | ✅ 42 rows |
| Evidence + unknowns | 20, 21 | ✅ |

## 4. What must be newly engineered (no Mimo precedent)

1. Exam engine (timer, negative marking, blueprint, rotation, integrity).
2. Weakness model (per-topic accuracy with recency decay) — the core of Mode C.
3. Deadline-aware scheduler and miss-recovery logic.
4. Persian normalisation + RTL math/formula rendering pipeline.
5. Self-hosted analytics/flags/push replacing Firebase/Adjust/Customer.io.
6. Content distribution with signed downloadable packs (Mimo bundles content, so this is new).
7. Payment integration for Iranian gateways with entitlement service (RevenueCat excluded).
8. Question-level versioning and answer-key correction workflow (Mimo versions tutorials, not answers).

## 5. Risk register for the port

| Risk | Severity | Mitigation |
|---|---|---|
| Copying Mimo's *feel* without its content density (19 tracks vs. one syllabus) | High | Design for depth per topic, not breadth of tracks |
| Persian grading normalisation bugs | High | Build a 500-case test corpus before authoring |
| Currency/key economy misread as extortion | High | Never gate exam content; gate simulations |
| AI cost + Persian quality | Medium | Ship instant-prompts only in v1 |
| Content operations without a review gate | High | Staged publish, two-person rule |
| Offline exams producing unverifiable scores | Medium | Signed bundles + result hash |
| Team underestimating the EPM backend | High | It is 60% of the product's engineering |
