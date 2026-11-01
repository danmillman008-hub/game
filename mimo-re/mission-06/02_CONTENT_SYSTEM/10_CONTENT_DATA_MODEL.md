# Mission 6 — Content Data Model

## Scope
Exact field-level contracts for content entities and lesson payloads, including the code-language table
and the executable-lesson payload.

## Method
`tools/extract_class_fields.py` over content classes and DTOs; enum constant enumeration; cross-check
against serializer classes (`*$$serializer`) to confirm field order/optionality.

## Sources
`evidence/CONTENT_MODEL_FIELDS.json`, `evidence/DTO_FIELDS.json`.

## Findings — entities (VERIFIED_STATIC)
| Entity | Fields |
|---|---|
| `TracksJson` | `publishSetVersion: long`, `tracks: List<Track>` |
| `Section` | `index: int`, `name: String`, `description: String`, `tutorials: List`, `hasProgress` (lazy) |
| `SectionJson` | `name`, `description`, `startIndex: int`, `endIndex: int`, `tutorialIds: List` |
| `Chapter` | `id: long`, `title: String`, `type: ChapterType`, `isCompleted: boolean`, `lessons: List<Lesson>` (+ `empty` sentinel `id=-1`) |
| `Lesson` | `id: long`, `title: String`, `contentType: LessonContentType`, `images: List<LessonImage>`, `hardModeSelected: boolean` |
| `LessonIdentifier` | `trackId`, `trackVersion`, `tutorialId`, `chapterId`, `lessonId` (all `long`) |
| `LessonImage` | `id: String` |
| `LessonContentType` | `INTERACTIVE`, `EXECUTABLE_FILES` |

## Findings — executable lesson payload (VERIFIED_STATIC)
| Type | Fields |
|---|---|
| `LessonContent$Executable` | `instructions: String`, `preselectedFileIndex: int`, `files: List<File>`, `empty` sentinel |
| `LessonContent$Executable$File` | `name: String`, `content: String`, `solvedContent: String`, `codeLanguage: CodeLanguage` |
| `ExecuteFilesBody` (request) | `files: List` |
| `ExecuteFilesResponse` (response) | `consoleOutput: String`, `error: String`, `hasPassed: boolean`, `hostedProjectUrl: String`, `tests: List` |

Two consequences that matter for reconstruction: (a) **the solution is shipped to the client** as
`solvedContent` per file — grading of code tasks is therefore *server-executed*, not compared locally;
(b) `hostedProjectUrl` means some tasks run as hosted projects rather than in-process.

## Findings — code languages (VERIFIED_STATIC)
`CodeLanguage` enumerates 24 values: `BASH, CPP, CSHARP, CSS, CSV, GIT, HTML, JAVA, JAVASCRIPT, JSON,
JSX, KOTLIN, LUA, NODE, NONE, PHP, PYTHON, R_LANG, RUBY, SQL, SWIFT, TEXT, TYPESCRIPT` (+ `Companion`),
each carrying `language`, `title`, `extension`, `icon`, `defaultFileName`. The presence of `GIT`, `CSV`
and `NODE` shows the editor is used for shell/git lessons and data-file lessons, not only programming.

## Findings — interactive payload
`LessonContent$Interactive` holds `lessonModules: List<LessonModule>` and a nullable
`hardModeLessonModules` list (see Phase 3). This is the only place where hard mode is expressed in data.

## Evidence labels
All field lists: **VERIFIED_STATIC** (names are author-chosen and survive obfuscation).
Optionality/nullability: **INFERRED** from Kotlin types and serializer presence.

## Limitations
Kotlin default values and `@SerialName` overrides were not extracted; a field's JSON key may differ from
its Kotlin name (`Q-17`).

## Open questions
`Q-15` Track/Tutorial fields; `Q-17` serialised names; `Q-18` whether `tests` in the execution response
is structured (name/passed/message).

## Reproduction
`python3 -c "import json;print(json.load(open('evidence/DTO_FIELDS.json'))['com.getmimo.core.model.lesson.executablefiles.ExecuteFilesResponse'])"`
