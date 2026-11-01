# 05 — Course, track and curriculum engine

All numbers are measured over the bundled English pack (`evidence/tracks.csv`,
`evidence/tutorials.csv`, `evidence/lessons.csv`, `evidence/content-deep.json`).
The same structure exists in 9 more languages at `publishSetVersion 753`.

## 1. The five-level content model

```
PublishSet (per language, version 753)
└── Track           19      (id, title, onboardingCategory, isNew, version, sections[])
    └── Section      249 total (name, startIndex, endIndex, tutorialIds[])
        └── Tutorial 1,029   (id, version 1..161, type, codeLanguage, chapters[])
            └── Chapter 1,947 (id, type, lessons[])
                └── Lesson 18,272 (id, contentType, interactiveContent | executableContent)
```

Verified invariants (`tools/content_deep.py`, all clean):
* `sections[].startIndex` is exactly the running sum of previous section lengths — **0
  mismatches in 249 sections**.
* Every `tutorialIds[]` entry resolves to a shipped tutorial file — **0 dangling references**.
* **0 orphan tutorial files**, **0 duplicate tutorial/chapter/lesson ids**.
* 1,029 tutorials are referenced by 19 tracks with **reuse**: tracks share tutorials
  (e.g. HTML/CSS/JS tutorials appear both standalone and inside Full-Stack and Front-End).

## 2. Track inventory (measured)

| id | Title | onboardingCategory | v | sections | tutorials | chapters | lessons |
|---|---|---|---|---|---|---|---|
| 50 | Full-Stack Developer | build | 501 | 20 | 492 | 929 | 8,610 |
| 125 | Python | none | 121 | 14 | 101 | 150 | 2,100 |
| 145 | SQL | none | 82 | 6 | 47 | 91 | 935 |
| 197 | JavaScript | build | 55 | 16 | 113 | 199 | 2,483 |
| 194 | HTML | build | 62 | 5 | 28 | 45 | 540 |
| 214 | Swift | none | 16 | 7 | 43 | 57 | 833 |
| 219 | Front-End Developer | none | 82 | 15 | 376 | 716 | 6,635 |
| 225 | CSS | none | 26 | 4 | 66 | 107 | 1,362 |
| 226 | Python Developer | none | 38 | 11 | 180 | 352 | 3,156 |
| 228 | TypeScript | none | 12 | 4 | 23 | 26 | 316 |
| 236 | Back-End Developer | none | 23 | 9 | 208 | 370 | 3,872 |
| 240 | AI-supported learning | none | 10 | 1 | 25 | 31 | 327 |
| 243 | React | none | 19 | 3 | 42 | 92 | 1,067 |
| 249 | Vibe Coding Your Game | none | 13 | 3 | 9 | 9 | 113 |
| 262 | Game Development | none | 5 | 12 | 219 | 504 | 4,542 |
| 271 | Onboarding Lessons Experiment | none | 6 | 3 | 3 | 3 | 18 |
| 272 | Python Onboarding Test | none | 5 | 2 | 2 | 2 | 13 |
| 273 | How AI Works | none | 6 | 5 | 14 | 15 | 133 |
| 274 | Automating Tasks with AI | none | 3 | 4 | 11 | 11 | 128 |

Three structural lessons:
1. **Tracks are containers, not curricula.** Full-Stack is 492 tutorials but only 929 chapters
   — it is a *sequence of tutorials*, so "path" means playlist, not monolithic course.
2. **Two tracks (271, 272) are experiment scaffolding shipped to users** — tiny, hidden,
   `startIndex`-consistent. They are how content experiments are A/B'd on real devices.
3. **`onboardingCategory` only distinguishes `build` vs `none`** — i.e. server tagging for the
   onboarding question "do you want to build something?", not a taxonomy.

## 3. Tutorial taxonomy

| Type | Count | Meaning (I, from name + usage) |
|---|---|---|
| `course` | 507 | normal teaching sequence |
| `practiceRequired` | 157 | must be done to unlock progression |
| `practiceOptional` | 134 | skippable reinforcement |
| `guidedProjectOptional` | 117 | project, optional |
| `guidedProject` | 74 | project, required |
| `challenges` | 40 | challenge set |

`codeLanguage` distribution: `javascript` 283, `python` 195, `css` 169, `html` 139, `sql` 64,
`node` 47, `jsx` 46, `swift` 43, `typescript` 23, `none` 19, `bash` 1.
Tutorial `version` ranges 1…161 (independent per tutorial) — content is versioned per entity,
not per pack, which is what allows a single-track hotfix.

Chapters per tutorial: 1 (670), 2 (163), 3 (119), 4 (38), 5 (5), 10 (6). Mean lessons per
chapter **9.38**, median **10**, max **28**.

## 4. Chapter types = the difficulty ladder (verified counts, by lessons)

| Chapter type | Lessons | Share | Reading |
|---|---|---|---|
| `practiceLevel1` | 11,373 | 62% | default teaching chapter |
| `practiceLevel3` | 4,096 | 22% | hardest practice — notably *more* common than level 2 |
| `practiceLevel2` | 2,362 | 13% | mid |
| `challengeLevel2` | 382 | 2.1% | timed/challenge chapter |
| `challengeLevel0` | 45 | 0.2% | entry challenge |
| `challengeLevel1` | 14 | 0.08% | — |

The `Level0..3` naming is the only explicit difficulty axis in the content model. The skew
towards `practiceLevel3` is deliberate: chapters are authored at the difficulty they will be
*served* at, and lower levels exist mainly for remedial or onboarding paths.

## 5. Lesson inventory

* `contentType`: `interactive` 14,248 (78%), `executableFiles` 4,024 (22%).
* Hard-mode variants: **6,058 lessons** carry `hardModeContent` (all interactive; gated by
  `experiment_hardmode_v2_android`).
* Assessed blocks: **13,027** (8,276 `<interaction>` + 4,751 `<selection>`); modules with
  `visible-if="wrong"`: 13,043; `visible-if="correct"`: 143 (feedback only).
* Executable lessons contain **6,746 files** total, 293 with an intentionally empty starter
  file, 269 SQL/database lessons, 85 with HTTP options.
* 42 executable lessons have **no** `solvedContent` on any file — the only integrity deviation
  found in the whole corpus (`content-deep.json → issues.executable_without_solution`); these
  cannot show "see solution".

## 6. How the curriculum is resolved at runtime (V literals + I sequencing)

1. **Pack selection** by locale (`assets/lessons-<lang>`), 10 packs; missing locale ⇒ English (I).
2. **Tracks manifest** `tracks.json` parsed into `TracksJson` (`publishSetVersion` field, V).
3. **Path choice** in onboarding writes a `trackId`; the "adapted" experiment
   (`experiment_adapted_onboarding_android`) may write a *server-composed* variant track (I).
4. **Tutorial file** loaded lazily per `tutorialId`; chapters inside are pre-indexed; the app
   shows one chapter at a time in `ChapterActivity`.
5. **Resume** is computed from `lesson_progress` (Room) ordered by `startedAt`/`completedAt`,
   scoped by `(tutorialId, tutorialVersion, publishSetVersion)` (V schema).
6. **Completion** writes `chapter_completions` / `tutorial_completions`; the path card and the
   certificate percentage read from those tables (V schema + `certificate_upselling_closer_to_certificate`).
7. **ETA** is server-computed: `TrackEtaResponse(trackEstimatedCompletionAt,
   currentPaceMinutesPerDay, sections[SectionEta(sectionIndex…)])` (V contract) and rendered on
   chapter end (`chapter_end_progress_eta_quarter_*`, `…_half_*`, `…_three_left_*`, V strings).

## 7. Reuse notes for a Konkur curriculum

* Keep **track → section → tutorial → chapter → lesson** with `startIndex/endIndex` sections:
  it is what makes "your plan changed, resume where you were" cheap.
* Keep the **version triple** on progress rows; drop the per-tutorial `version` only if you
  never hotfix a single tutorial (you will).
* Konkur needs a **sixth level** Mimo lacks: *exam blueprint* (topic weights per subject per
  year) above tracks. Mimo's `Level0..3` cannot express "this chapter is worth 4% of the exam".
* Replace `onboardingCategory` with a **goal/field taxonomy** (رشته: ریاضی/تجربی/انسانی) and
  a **time-to-exam** attribute; Mimo has no notion of a deadline, which is the core difference
  between habit learning and exam preparation.
