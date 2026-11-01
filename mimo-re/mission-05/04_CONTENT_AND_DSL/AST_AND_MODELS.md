# Mission 5 — AST Node Model (JSON Schema, editable)

## Scope
Machine-checkable description of the parsed lesson AST: every node type, its fields and their
provenance. Intended to be usable as a validation schema for a third-party reimplementation
(specification only — no implementation is shipped).

## Method
Enumerated the 41 classes in `com.getmimo.data.content.lessonparser.interactive.model`, read their
field sets from the decompiled constructors (field names survive as obfuscated single letters; their
*types* and *use sites* identify them), and mapped each to the grammar production in
`DSL_GRAMMAR.md`.

## Sources
`LessonModule` (+`$Code`, `$Paragraph`, `$Selection`, `$Image`, `$Webview`, `$Database`),
`Interaction` (+`$FillTheGap`, `$Selection`, `$Spell`, `$ValidatedInput`), `Output`
(+`$ConsoleOutput`, `$TableOutput`), `Table`, `Table$Row`, `Table$Row$Header`, `Table$Row$Data`,
`Option`, `SelectionItem`, `CollapsibleLine`, `Attribute`, `AttributeType`, `ModuleVisibility`,
`WebviewType`, `Tag`.

## Findings — schema
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "mimo.interactive.lesson.schema.json",
  "title": "Mimo interactive lesson AST",
  "type": "object",
  "required": ["modules"],
  "properties": {
    "modules": { "type": "array", "items": { "$ref": "#/$defs/Module" } }
  },
  "$defs": {
    "Visibility": { "enum": ["ALWAYS", "CORRECT", "WRONG"] },
    "WebviewKind": { "enum": ["BROWSER", "EMBEDDED", "INTERACTIVE", "UNLOCK"] },
    "Module": {
      "oneOf": [
        { "$ref": "#/$defs/CodeModule" },
        { "$ref": "#/$defs/ParagraphModule" },
        { "$ref": "#/$defs/SelectionModule" },
        { "$ref": "#/$defs/ImageModule" },
        { "$ref": "#/$defs/WebviewModule" },
        { "$ref": "#/$defs/DatabaseModule" }
      ]
    },
    "Common": {
      "type": "object",
      "required": ["name", "visibility"],
      "properties": {
        "name": { "type": "string" },
        "visibility": { "$ref": "#/$defs/Visibility" }
      }
    },
    "CodeModule": {
      "allOf": [{ "$ref": "#/$defs/Common" }],
      "properties": {
        "kind": { "const": "CODE" },
        "content": { "type": "string", "description": "source text; index space for interactions" },
        "codelang": { "type": "string", "description": "CodeLanguage.fromString, default 'none'" },
        "interactions": { "type": "array", "items": { "$ref": "#/$defs/Interaction" } },
        "output": { "$ref": "#/$defs/Output" },
        "collapsibleLines": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["startLineIndex", "endLineIndex"],
            "properties": { "startLineIndex": { "type": "integer" }, "endLineIndex": { "type": "integer" } }
          }
        }
      },
      "required": ["kind", "content", "interactions"]
    },
    "Interaction": {
      "type": "object",
      "required": ["type", "isDefault", "startIndex", "endIndex"],
      "properties": {
        "type": { "enum": ["FILL_THE_GAP", "SELECTION", "SPELL", "VALIDATED_INPUT"] },
        "isDefault": { "type": "boolean", "default": false },
        "startIndex": { "type": "integer", "minimum": 0 },
        "endIndex": { "type": "integer", "minimum": 0 }
      },
      "if": { "properties": { "type": { "enum": ["FILL_THE_GAP", "SELECTION", "SPELL"] } } },
      "then": { "properties": { "options": { "type": "array", "items": { "$ref": "#/$defs/Option" } } } },
      "else": { "properties": { "expected": { "type": "string" } } }
    },
    "Option": {
      "type": "object",
      "properties": {
        "isCorrect": { "type": "boolean" },
        "label": { "type": "string" },
        "spanStart": { "type": "integer", "description": "Option.c — styled-text start" },
        "spanEnd": { "type": "integer", "description": "Option.d — styled-text end" }
      },
      "required": ["isCorrect", "label"]
    },
    "Output": {
      "oneOf": [
        { "type": "object", "required": ["kind", "text"],
          "properties": { "kind": { "const": "CONSOLE" }, "text": { "type": "string" } } },
        { "type": "object", "required": ["kind", "table"],
          "properties": { "kind": { "const": "TABLE" }, "table": { "$ref": "#/$defs/Table" } } }
      ]
    },
    "Table": { "type": "object", "properties": { "rows": { "type": "array", "items": { "$ref": "#/$defs/Row" } } } },
    "Row": {
      "type": "object",
      "required": ["kind"],
      "properties": { "kind": { "enum": ["HEADER", "DATA"] }, "cells": { "type": "array", "items": { "type": "string" } } }
    },
    "ParagraphModule":  { "allOf": [{ "$ref": "#/$defs/Common" }], "properties": { "kind": { "const": "PARAGRAPH" }, "text": { "type": "string" } } },
    "SelectionModule":  { "allOf": [{ "$ref": "#/$defs/Common" }], "properties": { "kind": { "const": "SELECTION" }, "items": { "type": "array", "items": { "$ref": "#/$defs/Option" } } } },
    "ImageModule":      { "allOf": [{ "$ref": "#/$defs/Common" }], "properties": { "kind": { "const": "IMAGE" }, "source": { "type": "string" } } },
    "WebviewModule":    { "allOf": [{ "$ref": "#/$defs/Common" }], "properties": { "kind": { "const": "WEBVIEW" }, "webviewType": { "$ref": "#/$defs/WebviewKind" } } },
    "DatabaseModule":   { "allOf": [{ "$ref": "#/$defs/Common" }], "properties": { "kind": { "const": "DATABASE" } } }
  }
}
```

## Findings — field provenance
| AST field | Source field(s) | Confidence |
|---|---|---|
| `content` | `LessonModule$Code` ctor arg 1 | VERIFIED_STATIC |
| `interactions` | `LessonModule$Code` ctor arg 2 | VERIFIED_STATIC |
| `output` | ctor arg 3 | VERIFIED_STATIC |
| `visibility` | ctor arg 4 (`ModuleVisibility`) | VERIFIED_STATIC |
| `codelang` | ctor arg 5 (`CodeLanguage`) | VERIFIED_STATIC |
| `name` | ctor arg 6 | VERIFIED_STATIC |
| `collapsibleLines` | ctor arg 7 | VERIFIED_STATIC |
| `Option.isCorrect/label/spanStart/spanEnd` | `Option.a/b/c/d` | VERIFIED_STATIC (span semantics from render sites) |
| `Interaction.isDefault/startIndex/endIndex` | `Interaction.a/.b/.c` + parser attributes | VERIFIED_STATIC |
| `kind` discriminators | subclass identity | VERIFIED_STATIC |

The constructor argument order above is itself evidence: it is the order in which `te.a` pushes the
parsed values, which is why `output` precedes `visibility`.

## Evidence labels
- Node inventory and field names/types: **VERIFIED_STATIC**.
- Field *semantics* for `content`/span/index fields: **VERIFIED_STATIC** (use sites read).
- `Paragraph/Selection/Image/Webview/Database` payload fields: **INFERRED_MEDIUM** (classes and
  discriminators verified; payload fields not individually re-read this mission).

## Limitations
The schema is a *normalised* AST, not a serialisation format: Mimo never emits this JSON. It exists
so a spec consumer can validate parsed content without copying Mimo's obfuscated class layout.

## Unresolved
Payload field sets of the five non-code modules (`U-01`), and whether `DatabaseModule` carries a
schema/seed payload (`U-03`).

## Reproduction
`ls /tmp/dad | grep lessonparser.interactive.model` → 41 classes; then read each constructor.
