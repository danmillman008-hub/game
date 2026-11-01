# 11 — Content authoring, publishing and distribution

## 1. The distribution model, in one paragraph

Content is **not** fetched at runtime in normal use: ten complete curriculum packs ship inside
`assets/`, one per language, each ~57–64 MB. The APK is therefore a *content distribution
vehicle*, and the server's authority over content is exercised through **versions** (a pack
publish-set version, a per-tutorial version, a per-track version) rather than through delivery.
Updates arrive with app updates, plus a developer-only live channel (§12).

## 2. Pack inventory (V, measured)

| Pack | Size (approx.) | Tracks | Tutorial files | Lesson slots | `publishSetVersion` |
|---|---|---|---|---|---|
| `lessons-en` | 57 MB | 19 | 1,029 | 18,272 | 753 |
| `lessons-de` | 64 MB | 19 | 1,029 | 18,272 | 753 |
| `lessons-fr` | 63 MB | 19 | 1,029 | 18,272 | 753 |
| `lessons-es` | 64 MB | 19 | 1,029 | 18,272 | 753 |
| `lessons-it` | 64 MB | 19 | **1,031** | **18,289** | 753 |
| `lessons-pt` | 63 MB | 19 | 1,029 | 18,272 | 753 |
| `lessons-pl` | 63 MB | 19 | **1,031** | 18,289 | 753 |
| `lessons-ru` | 64 MB | 19 | 1,029 | 18,272 | 753 |
| `lessons-tr` | 63 MB | 19 | **1,031** | 18,289 | 753 |
| `lessons-id` | 62 MB | 19 | **1,031** | 18,289 | 753 |
| `lessons-common` | 6.5 MB | — | shared assets (images, snippets, `styles/`, `beautify/`, `prettier/`, `highlight.min.js`, `lesson-webview.js`) |

Four locales carry **2 extra tutorials and 17 extra lessons** (it, pl, tr, id). This is the most
informative fact in the whole content system: it proves the pack set is **not built from one
master with translations**, but from a CMS that can ship per-locale content, with the same
publish-set number covering divergent pack contents. `publishSetVersion` is therefore a *schema/
contract* version, not a content hash.

## 3. Versioning layers (V)

| Layer | Field | Range observed | Purpose |
|---|---|---|---|
| Publish set | `publishSetVersion` in `tracks.json` + every progress row | 753 | contract version shared by client and all packs |
| Track | `Track.version` | 3 … 501 | per-path revision (Full-Stack = 501) |
| Tutorial | `Tutorial.version` | 1 … 161 | per-entity revision ⇒ single-tutorial hotfix |
| Lesson | identity only (`lessonId`) | 18,272 ids | no version; lessons are immutable-by-id in practice (I) |
| Chapter | identity only (`chapterId`) | 1,947 ids | — |
| Code block | `version` on `<code>` | 14,469 occurrences | proves even *markup blocks* are versioned |

**The progress triple** `(lessonId, tutorialId, tutorialVersion, publishSetVersion)` in
`lesson_progress` is what makes this safe: a progress row records which content revision it was
earned against, so a content update can decide to re-ask, keep, or grandfather a completed
lesson.

## 4. Authoring and publishing pipeline (reconstructed, mostly I)

```mermaid
graph LR
  A[Authoring CMS<br/>UNKNOWN vendor] --> B[Lesson markup + JSON export]
  B --> C[Automated validation<br/>schema + offset + referential checks]
  C --> D{Publish set}
  D --> E[Bundle into assets/lessons-&lt;lang&gt;/]
  D --> F[Server-side pack for live/preview]
  F --> G[Developer Menu: downloadAndUnzipUnpublishedPackage]
  F --> H[/v1/tutorials/drafts/.../render]
  E --> I[App release]
  G --> J[Pusher event → device reloads lesson]
  H --> K[Author sees rendered lesson on device]
```
Evidence for each box:
* `B` — the format is the DSL of §06 + JSON envelope; `C` — the corpus passes 8 classes of
  automated checks with 1 deviation in 18,272 lessons (42 solution-less executable lessons), so
  a validator exists (I, but the cleanliness is strong evidence).
* `F/H` — endpoint `/v1/tutorials/drafts/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/render`
  (V) is a **server-side renderer for draft lessons**: authoring output can be rendered without
  a release.
* `G/J` — `DeveloperMenuViewModel$downloadAndUnzipUnpublishedPackage`, modal
  `DeveloperMenuDownloadLiveContent`, `DeveloperMenuLiveDeploymentError`, and Pusher
  subscription literals (`AwesomeMode*`) (V). *Live deploys reach devices over a push channel*,
  which is why the dev menu has a "live deployment error" modal.
* `I` — assets are inside the APK; there is no content CDN endpoint in the 71-endpoint
  catalogue (V negative finding: **no content download endpoint exists**).

## 5. Content QA facts worth copying

* Referential integrity is enforced structurally: `sections[].startIndex` matches the running
  sum in all 249 sections, so "resume at section k" is O(1).
* Reuse is explicit: 1,029 tutorials serve 19 tracks; the shared tutorials are authored once.
* Localisation is per-pack, not per-string: a lesson is translated as a whole document,
  including its `visible-if="wrong"` remediation copy — which is why remediation quality varies
  by language (I).
* The single deviation class (42 executable lessons without `solvedContent`) shows the validator
  does **not** require a solution to exist, only that referenced things resolve.

## 6. Konkur transfer

| Mimo idea | Konkur form | Note |
|---|---|---|
| Pack per language inside APK | Pack per **subject × exam year** (e.g. `riazi-1404`) | Konkur content changes yearly; bundles must be hot-swappable without app update ⇒ invert Mimo: download packs |
| `publishSetVersion` as contract | `blueprintVersion` + `packVersion` | Blueprint (topic weights) changes more often than content |
| Per-tutorial version + progress triple | Same, plus **question-level** version | Question banks get corrected constantly (typos, wrong keys) |
| Draft render endpoint | Author preview in the admin panel | Needed for Persian formula rendering QA |
| Live push deploys to dev builds | Same, but staged: draft → review → publish | A wrong key in an exam app is a credibility event |
| `lessons-common` shared assets | Shared figure/formula library | — |

The pipeline Mimo has is *app-release-coupled* and therefore unsuitable for Konkur. What should
survive is the **version algebra** (publish set + per-entity version + progress triple), because
that is what lets you fix a bad answer key without losing users' progress.
