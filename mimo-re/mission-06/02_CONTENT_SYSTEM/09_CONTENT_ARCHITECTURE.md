# Mission 6 — Content Architecture

## Scope
The real hierarchy of Mimo's educational content as represented in code and shipped data: which
entities exist, how they nest, and what identifies each level.

## Method
Field extraction over the 64 classes in `com.getmimo.data.content.model.track` (`tools/extract_class_fields.py`),
cross-read with the shipped corpus (`assets/lessons-en/tracks/`, 10,327 JSON documents) and the mission-04
census.

## Sources
`evidence/CONTENT_MODEL_FIELDS.json`, `evidence/DTO_FIELDS.json`, mission-04 corpus census (frozen).

## Findings — hierarchy (VERIFIED_STATIC)
```
Track (program)
 └─ Section            { index, name, description, tutorials[], hasProgress }
     └─ Tutorial       (identified by tutorialIds ranges in the section delta form)
         └─ Chapter    { id, title, type, isCompleted, lessons[] }
             └─ Lesson { id, title, contentType, images[], hardModeSelected }
                 └─ LessonContent = Interactive | Executable
                     ├─ Interactive: modules[] (see Phase 3 DSL)
                     └─ Executable: { instructions, preselectedFileIndex, files[] }
                          └─ File { name, content, solvedContent, codeLanguage }
```
**Four levels are real code entities** (Section, Chapter, Lesson, LessonContent); "program", "course",
"unit", "module" and "exercise" are *not* separate classes in this build. The word "tutorial" appears as
an id in `LessonIdentifier` and in `SectionJson.tutorialIds`, i.e. tutorials are a **grouping level
between section and chapter that is represented by identifier ranges rather than by a rich object**.

`SectionJson` is the wire/delta form: `{ name, description, startIndex, endIndex, tutorialIds[] }` — a
section declares *index bounds*, not embedded objects. That is how sections are versioned cheaply.

## Findings — identifiers (VERIFIED_STATIC)
`LessonIdentifier { trackId, trackVersion, tutorialId, chapterId, lessonId }` — a **5-part composite
key**. Note `trackVersion` is part of the lesson identity, so the same lesson id can exist at several
versions simultaneously; progress rows, however, key on `(lessonId, tutorialId)` only (see Phase 6),
which means **progress is version-agnostic while content addressing is version-aware**.

`TracksJson { publishSetVersion, tracks[] }` — a content pack is a versioned bundle of tracks.

## Findings — chapter kinds (VERIFIED_STATIC)
`ChapterType` enumerates `NONE, QUIZ, PRACTICE_LEVEL_1..3, CHALLENGE_DIFFICULTY_0..4` (+ display
`typeName`). So the product has quiz chapters, three practice levels and five challenge difficulties —
these are *chapter-level* modifiers, not separate lesson types.

## Findings — locales (VERIFIED_STATIC, with caveat)
`ContentLocale` enumerates only `IT, PL, PT, RU, TR` in the recovered DEX, while the manifest's fused
dynamic modules list `content_de, content_es, content_fr, content_id, content_it, …`. Interpretation:
locale content ships as **dynamic feature modules**, and the enum in the base DEX is partial (or the
modded build stripped constants). Open question `Q-14`; do not conclude "Mimo has five locales".

## Evidence labels
Hierarchy, fields, key composition, chapter kinds: **VERIFIED_STATIC**. "Tutorials are a grouping level
rather than an entity": **INFERRED_HIGH**.

## Limitations
The corpus census is frozen mission-04 data (re-used, not re-derived). `Track` and `Tutorial` field
lists were not extracted because those classes were not recovered as source in the analysed batches.

## Open questions
`Q-14` full locale set; `Q-15` `Track`/`Tutorial` field sets; `Q-16` whether `hasProgress` is computed
client- or server-side (it is a lazy delegate).

## Reproduction
```bash
/tmp/venv/bin/python tools/extract_class_fields.py \
  --classes com.getmimo.data.content.model.track.{TracksJson,Section,SectionJson,Chapter,Lesson,LessonIdentifier} \
  --out /tmp/x.json
```
