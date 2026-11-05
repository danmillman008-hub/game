# XML DSL parser (`Lte/c` and module parsers)

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/DSL_LessonParser.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC — technology recovered
The lesson DSL is **XML-like text parsed with `org.xmlpull.v1.XmlPullParser`**, not a regex
and not a JSON sub-schema. `Lte/c;->b(String) : ArrayList<LessonModule>` @14378108,
400 instructions:

```
val factory = XmlPullParserFactory.newInstance()
factory.setNamespaceAware(true)
val p = factory.newPullParser()
p.setInput(StringReader(html))
val modules = ArrayList<LessonModule>()
while (p.next() !in (END_DOCUMENT, ...)) {
    when (p.name) {
      "p"        -> modules += Lte/d.a(p)      // LessonModule$Paragraph
      "code"     -> modules += Lte/a.a(p)      // LessonModule$Code
      "selection"-> modules += Lte/e.a(p)      // LessonModule$Selection
      "img"      -> modules += Lte/c.a(p)      // LessonModule$Image
      "webview"  -> modules += Lte/g.a(p)      // LessonModule$Webview
      "database" -> modules += Lte/b.a(p)      // LessonModule$Database
      "html","body" -> skip
      else       -> log("skipping <tag>") + skip
    }
}
```
Per-module `try/catch` logs `"could not parse <x> module for lesson <id>"` and emits
analytics `xml_parse_error_module` / `xml_parse_error_skipped` via `Lpe/a.b`.

### Module parsers (verified signatures)
| Class | Method | Output | insns |
|---|---|---|---|
| `Lte/a;` | `a(XmlPullParser)` | `LessonModule$Code` | 490 |
| `Lte/a;` | `b(XmlPullParser)` | `SpannableStringBuilder` (inline `<text value=... type=.../>`) | 97 |
| `Lte/d;` | `a(XmlPullParser)` | `LessonModule$Paragraph` | 291 |
| `Lte/d;` | `c/d/e(XmlPullParser)` | attribute/visibility extraction | 105/43/65 |
| `Lte/e;` | `a(XmlPullParser)` | `LessonModule$Selection` | 288 |
| `Lte/b;` | `a(XmlPullParser)` | `LessonModule$Database` | 92 |
| `Lte/f;` | `a(XmlPullParser)` | `Table` | 176 |
| `Lte/g;` | `a(XmlPullParser)` | `LessonModule$Webview` | 228 |

### Verified tag/attribute vocabulary (DEX string constants)
`p`, `code`, `content`, `text`, `value`, `type`, `option`, `interaction`, `selection`,
`output`, `webview`, `visible-if`, `correct`, `always`, `wrong`, `strong`, `br`, `src`,
`startIndex`, `endIndex`, `version`, `style`, `codelang`, `name`.
`ModuleVisibility` enum: `ALWAYS("always")`, `CORRECT("correct")`, `WRONG("wrong")`
(`<clinit>` @`EVIDENCE/DISASM/ModuleVisibility.smali.txt`).
`ParserModule` enum: `CODE`, `PARAGRAPH`, `SELECTION`.
`Interaction` subclasses: `FillTheGap{c:List<Option>}`, `Selection{c,d,e}`,
`Spell{c,d}`, `ValidatedInput{c,d,e,f}`.
`LessonModule` subclasses: `Code`, `Paragraph`, `Image`, `Webview`, `Selection`, `Database`.

## Original shipped samples
`SAMPLES/ORIGINAL_*.json` are byte-exact APK members (`MANIFEST.json` has SHA-256).
`ORIGINAL_testdata_127-0-1.html` contains a `spell` interaction (v753 English curriculum
contains no `spell` tag in the sampled set).

## Remaining uncertainty
- Full 490-instruction `Lte/a.a` (option/offset/interaction construction) is only
  partially decoded = `UNKNOWN` in detail; its inputs/outputs are verified.
- `Tag` and `Attribute` enum ordinal→string tables are not completely enumerated = `INFERRED`.
