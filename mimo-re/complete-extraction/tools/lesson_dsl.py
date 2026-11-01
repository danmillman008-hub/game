#!/usr/bin/env python3
"""Reference implementation of the Mimo lesson DSL (parser + grader + validator).

Scope: interactive lessons only (interactiveContent / hardModeContent).
Design goals
  * tolerant tokenizer for the 27 observed tags
  * exact token-stream indexing (startIndex/endIndex refer to <text> nodes)
  * deterministic grading for fillTheGap, validatedInput, selection
  * static validation of index bounds and answer well-formedness

No network, no APK access. Pure stdlib.
"""
from __future__ import annotations
import html as htmllib
import re
from dataclasses import dataclass, field
from typing import Any

TAG_OPEN = re.compile(r"<\s*([A-Za-z][A-Za-z0-9]*)")
ATTR = re.compile(r"([A-Za-z_][A-Za-z0-9_:-]*)\s*=\s*\"([^\"]*)\"")
VOID = {"br", "img", "hr", "input"}

# ---------------------------------------------------------------- data classes
@dataclass
class Token:
    value: str = ""
    kind: str = "text"          # "text" | "break"
    cls: str | None = None
    def text(self) -> str:
        return "\n" if self.kind == "break" else self.value

@dataclass
class Gap:
    start: int
    end: int
    distractors: list[str] = field(default_factory=list)
    def answer(self, source: str) -> str:
        return source[self.start:self.end]

@dataclass
class ValidatedInput:
    start: int
    end: int
    def answer(self, source: str) -> str:
        return source[self.start:self.end]

@dataclass
class CodeBlock:
    name: str
    codelang: str
    version: str
    visible_if: str
    tokens: list[Token] = field(default_factory=list)
    gaps: list[Gap] = field(default_factory=list)
    distractors: list[str] = field(default_factory=list)
    inputs: list[ValidatedInput] = field(default_factory=list)
    def source(self) -> str:
        return "".join(t.text() for t in self.tokens)

@dataclass
class Selection:
    items: list[tuple[int, bool, str]] = field(default_factory=list)
    iscode: bool = False
    multiple: bool = True
    def correct_values(self) -> set[int]:
        return {v for v, c, _ in self.items if c}

@dataclass
class LessonDoc:
    code_blocks: list[CodeBlock] = field(default_factory=list)
    selections: list[Selection] = field(default_factory=list)
    paragraphs: list[tuple[str, str]] = field(default_factory=list)   # (visible_if, text)
    webviews: list[dict[str, str]] = field(default_factory=list)
    databases: list[dict[str, Any]] = field(default_factory=list)
    images: list[str] = field(default_factory=list)
    problems: list[str] = field(default_factory=list)

# ---------------------------------------------------------------- parsing
def _attrs(chunk: str) -> dict[str, str]:
    return {k: v for k, v in ATTR.findall(chunk)}

def _tag_chunk(s: str, i: int) -> str:
    j = s.find(">", i)
    return s[i: j + 1] if j != -1 else s[i: i + 500]

def _parse_tokens(body: str) -> list[Token]:
    toks: list[Token] = []
    for m in re.finditer(r"<text\b([^>]*)/?>", body):
        a = _attrs(m.group(1))
        if a.get("type") == "break":
            toks.append(Token(kind="break"))
        else:
            toks.append(Token(value=htmllib.unescape(a.get("value", "")), cls=a.get("class")))
    return toks

def _parse_content_fragment(frag: str) -> str:
    return "".join(t.text() for t in _parse_tokens(frag))

def parse(doc_html: str) -> LessonDoc:
    doc = LessonDoc()
    if not isinstance(doc_html, str):
        doc.problems.append("not-a-string")
        return doc
    for m in re.finditer(r"<code\b([^>]*)>(.*?)</code>", doc_html, re.S):
        a = _attrs(m.group(1))
        body = m.group(2)
        if "codelang" not in a and "name" not in a:
            continue  # inline <code>…</code> in prose
        cb = CodeBlock(
            name=a.get("name", ""), codelang=a.get("codelang", ""),
            version=a.get("version", ""), visible_if=a.get("visible-if", "always"),
        )
        # 1) isolate the interactions section: <code> may emit it BEFORE or AFTER <content>
        inter_html = ""
        body_wo = body
        im_all = re.search(r"<interactions>(.*?)</interactions>", body, re.S)
        if im_all:
            inter_html = im_all.group(1)
            body_wo = body[:im_all.start()] + body[im_all.end():]
        # 2) the block's own content is the only <content> left outside interactions
        cm = re.search(r"<content>(.*?)</content>", body_wo, re.S)
        cb.tokens = _parse_tokens(cm.group(1) if cm else "")
        # 3) interactions: each <option start end/> is one gap; correct="false" is a distractor
        for im in re.finditer(r"<interaction\b([^>]*?)(/?)>", inter_html):
            ia = _attrs(im.group(1))
            itype = ia.get("type", "")
            if itype == "validatedInput":
                cb.inputs.append(ValidatedInput(int(ia.get("startIndex", -1)), int(ia.get("endIndex", -1))))
                continue
            if itype != "fillTheGap":
                continue
            opts = re.search(r"<options>(.*?)</options>", inter_html[im.end():], re.S)
            if not opts:
                doc.problems.append(f"fillTheGap-without-options:{cb.name}")
                continue
            for om in re.finditer(r"<option\b([^>]*?)(/>|>(.*?)</option>)", opts.group(1), re.S):
                oa = _attrs(om.group(1))
                if "startIndex" in oa and "endIndex" in oa:
                    cb.gaps.append(Gap(int(oa["startIndex"]), int(oa["endIndex"])))
                elif oa.get("correct") == "false":
                    inner = om.group(3) or ""
                    c = re.search(r"<content>(.*?)</content>", inner, re.S)
                    cb.distractors.append(_parse_content_fragment(c.group(1) if c else inner))
        doc.code_blocks.append(cb)
    for m in re.finditer(r"<selection\b([^>]*)>(.*?)</selection>", doc_html, re.S):
        sa = _attrs(m.group(1))
        sel = Selection(iscode=sa.get("iscode") == "true", multiple=sa.get("multiple") == "multiple")
        for im in re.finditer(r"<item\b([^>]*)>(.*?)</item>", m.group(2), re.S):
            ia = _attrs(im.group(1))
            sel.items.append((int(ia.get("value", -1)), ia.get("correct") == "true", im.group(2)))
        doc.selections.append(sel)
    for m in re.finditer(r"<p\b([^>]*)>(.*?)</p>", doc_html, re.S):
        doc.paragraphs.append((_attrs(m.group(1)).get("visible-if", "always"), m.group(2)))
    for m in re.finditer(r"<webview\b([^>]*)/?>", doc_html):
        doc.webviews.append(_attrs(m.group(1)))
    for m in re.finditer(r"<database\b([^>]*)>", doc_html):
        a = _attrs(m.group(1))
        tail = doc_html[m.end():]
        tables = []
        for tm in re.finditer(r"<table\b([^>]*)>(.*?)</table>", tail, re.S):
            ta = _attrs(tm.group(1))
            headers = [htmllib.unescape(x) for x in re.findall(r"<header\b[^>]*content=\"([^\"]*)\"", tm.group(2))]
            rows = []
            for rm in re.finditer(r"<row>(.*?)</row>", tm.group(2), re.S):
                rows.append([htmllib.unescape(x) for x in re.findall(r"<data\b[^>]*content=\"([^\"]*)\"", rm.group(1))])
            tables.append({"name": ta.get("name", ""), "headers": headers, "rows": rows})
        doc.databases.append({"bootstrapScript": htmllib.unescape(a.get("bootstrapScript", "")), "tables": tables})
    for m in re.finditer(r"<img\b([^>]*)/?>", doc_html):
        doc.images.append(_attrs(m.group(1)).get("src", ""))
    return doc

# ---------------------------------------------------------------- validation
def validate(doc: LessonDoc) -> list[str]:
    """Static checks an authoring pipeline must enforce before publish."""
    issues: list[str] = []
    for cb in doc.code_blocks:
        n = len(cb.tokens)
        src_len = len(cb.source())
        for g in cb.gaps:
            if not (0 <= g.start < g.end <= src_len):
                issues.append(f"gap-out-of-range:{cb.name}:{g.start}:{g.end}:n={src_len}")
            if g.end - g.start > 80:
                issues.append(f"gap-too-wide:{cb.name}:{g.end - g.start}")
        for v in cb.inputs:
            if not (0 <= v.start < v.end <= src_len):
                issues.append(f"input-out-of-range:{cb.name}:{v.start}:{v.end}:n={src_len}")
        if not cb.tokens:
            issues.append(f"empty-code-block:{cb.name}")
        if not cb.name:
            issues.append("code-block-without-name")
        if not cb.codelang:
            issues.append(f"code-block-without-lang:{cb.name}")
        if not cb.gaps and not cb.inputs and cb.visible_if != "always":
            issues.append(f"interactive-code-without-interaction:{cb.name}")
    for i, sel in enumerate(doc.selections):
        vals = [v for v, _, _ in sel.items]
        if len(set(vals)) != len(vals):
            issues.append(f"selection-duplicate-values:{i}")
        if sum(1 for _, c, _ in sel.items if c) == 0:
            issues.append(f"selection-without-correct:{i}")
        if not sel.multiple and sum(1 for _, c, _ in sel.items if c) > 1:
            issues.append(f"single-select-with-multiple-correct:{i}")
    for i, w in enumerate(doc.webviews):
        if "content" not in w:
            issues.append(f"webview-without-content:{i}")
    return issues

# ---------------------------------------------------------------- grading
def grade_gap(cb: CodeBlock, answers: dict[int, str]) -> dict[str, Any]:
    """answers: gap index -> learner string (chips or typed text)."""
    out = {"ok": True, "detail": []}
    src = cb.source()
    for i, g in enumerate(cb.gaps):
        expected = g.answer(src)
        got = answers.get(i)
        if got is None:
            out["ok"] = False
            out["detail"].append({"gap": i, "status": "unanswered", "expected": expected})
        elif got.strip() == expected.strip():
            out["detail"].append({"gap": i, "status": "correct"})
        else:
            out["ok"] = False
            out["detail"].append({"gap": i, "status": "wrong", "expected": expected, "got": got})
    for i, v in enumerate(cb.inputs):
        expected = v.answer(src)
        key = 1000 + i
        got = answers.get(key)
        if got is None:
            out["ok"] = False
            out["detail"].append({"input": i, "status": "unanswered", "expected": expected})
        elif got.strip() == expected.strip():
            out["detail"].append({"input": i, "status": "correct"})
        else:
            out["ok"] = False
            out["detail"].append({"input": i, "status": "wrong", "expected": expected, "got": got})
    return out

def grade_selection(sel: Selection, chosen: set[int]) -> bool:
    return chosen == sel.correct_values()

def visible_paragraphs(doc: LessonDoc, state: str) -> list[str]:
    """state ∈ {unanswered, wrong, correct}; mirrors visible-if semantics."""
    if state == "unanswered":
        return [t for vif, t in doc.paragraphs if vif == "always"]
    return [t for vif, t in doc.paragraphs if vif in ("always", state)]

# ---------------------------------------------------------------- corpus validation CLI
def validate_corpus(packdir: str) -> dict:
    """Walk a language pack and validate every interactive lesson document."""
    import glob, json as _json, os, statistics
    stats = {"documents": 0, "code_blocks": 0, "gaps": 0, "distractors": 0,
             "validated_inputs": 0, "selections": 0, "databases": 0, "webviews": 0,
             "issues": {}, "issue_samples": [], "gap_width_chars": {"median": 0, "p95": 0, "max": 0},
             "gaps_per_block": {}}
    widths, per_block = [], []
    for path in sorted(glob.glob(os.path.join(packdir, "tutorial-*.json"))):
        doc = _json.load(open(path, encoding="utf-8"))
        tuts = doc.get("tutorials") or ([doc["tutorial"]] if isinstance(doc.get("tutorial"), dict) else [])
        for t in tuts:
            for ch in t.get("chapters", []):
                for les in ch.get("lessons", []):
                    for fld in ("interactiveContent", "hardModeContent"):
                        c = les.get(fld)
                        if not isinstance(c, str) or not c:
                            continue
                        stats["documents"] += 1
                        d = parse(c)
                        stats["code_blocks"] += len(d.code_blocks)
                        stats["gaps"] += sum(len(cb.gaps) for cb in d.code_blocks)
                        stats["distractors"] += sum(len(cb.distractors) for cb in d.code_blocks)
                        stats["validated_inputs"] += sum(len(cb.inputs) for cb in d.code_blocks)
                        stats["selections"] += len(d.selections)
                        stats["databases"] += len(d.databases)
                        stats["webviews"] += len(d.webviews)
                        for cb in d.code_blocks:
                            per_block.append(len(cb.gaps))
                            widths.extend(g.end - g.start for g in cb.gaps)
                        for iss in validate(d):
                            key = iss.split(":")[0]
                            stats["issues"][key] = stats["issues"].get(key, 0) + 1
                            if len(stats["issue_samples"]) < 12:
                                stats["issue_samples"].append({"lesson": les.get("id"), "field": fld, "issue": iss})
    if widths:
        widths.sort()
        stats["gap_width_chars"] = {"median": statistics.median(widths),
                                    "p95": widths[int(len(widths) * 0.95)], "max": max(widths)}
    import collections
    stats["gaps_per_block"] = dict(collections.Counter(per_block).most_common())
    return stats


if __name__ == "__main__":
    import sys, json
    if len(sys.argv) >= 3 and sys.argv[1] == "--validate-corpus":
        out = validate_corpus(sys.argv[2])
        if len(sys.argv) >= 4:
            json.dump(out, open(sys.argv[3], "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print(json.dumps({k: v for k, v in out.items() if k != "issue_samples"}, indent=1, ensure_ascii=False)[:2000])
