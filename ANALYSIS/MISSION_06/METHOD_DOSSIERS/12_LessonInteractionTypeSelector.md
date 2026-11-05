# Lgm/h — interaction/renderer selection

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/LessonInteractionTypeMapper.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC
`Lgm/h;-><clinit>` creates `Regex("<\\s*body[^>]*>(.*?)<\\s*/\\s*body>")` (extracts the
HTML body before the XmlPullParser stage). `Lgm/h;->a(List) : LessonInteractionType`
@12460480, 437 instructions, dispatches on `LessonModule` instance types.

### Nine renderer types (all recovered; M05 knew only 6)
`LessonInteractionType` subclasses, each carrying `a:String interactionTypeName`:
| Type | Marker string | Trigger |
|---|---|---|
| `InteractiveWebView` | `interactive_webview` | `LessonModule$Webview` |
| `FillTheGap` | `fill_the_gap` | `Interaction$FillTheGap` |
| `Spell` | `spell` | `Interaction$Spell` |
| `Selection` | `selection` | `Interaction$Selection` |
| `ValidatedInput` | `validated_input` | `Interaction$ValidatedInput` |
| `SingleChoice` | (selection variant) | `LessonModule$Selection` |
| `MultipleChoice` | `multiple_choice` | `LessonModule$Selection` |
| `Reveal` | — | `LessonModule$Code` present |
| `None` | — | no code / no interaction |

Also reads `Interaction.a:Z (isDefault)` and checks `LessonModule$Paragraph` instances to
choose `slide` vs other layouts.

## Callers — VERIFIED_STATIC
`Lcom/getmimo/ui/lesson/interactive/d;->E(LessonContent$Interactive, LessonBundle)V`
(InteractiveLessonViewModel) and
`Lcom/getmimo/interactors/chapter/c;->a(LessonBundle, cont)V` (GetLessonContentType).
`d->E` also handles `hardModeLessonModules` / `getHasDifferentHardModeContent()` /
`hardModeModulesOrDefault()` and posts `Lgm/g` (type + content + bundle + index) to LiveData.

## Remaining uncertainty
- Exact `SingleChoice` vs `MultipleChoice` predicate = `UNKNOWN`.
- `Reveal` vs `None` full condition chain = `UNKNOWN` (437-insn method).
