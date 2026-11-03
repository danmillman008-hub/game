#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static UI extraction for Hamdars 7.4.4 and Hadaf Plus 2.0.2 (both Flutter).

Everything is read straight from the APK bytes. Text assets are copied verbatim;
binary assets are hashed and catalogued. The Dart AOT snapshot (libapp.so) is
mined for class/route/endpoint/Persian strings — never decompiled, only strings.

Usage: python3 extract_source_apps.py <apk-dir> <out-dir>
"""
from __future__ import annotations
import csv, hashlib, json, re, sys, zipfile
from collections import Counter
from pathlib import Path

from loguru import logger
logger.remove()
from androguard.core.axml import AXMLPrinter

APKS = {
    "hamdars": "هم\u200cدرس_7.4.4.apk",
    "hadaf_plus": "Hadaf Plus_2.0.2.apk",
}
TEXT_EXT = {".svg", ".json", ".css", ".js", ".html", ".frag", ".txt", ".xml", ".md", ".z", ".bin"}
FA = "assets/flutter_assets/"


def sha(b):
    return hashlib.sha256(b).hexdigest()


def decode_axml(b):
    try:
        return str(AXMLPrinter(b).get_xml_obj().decode("utf-8", "replace")), None
    except Exception as e:
        try:
            return AXMLPrinter(b).get_xml().decode("utf-8", "replace"), None
        except Exception as e2:
            return None, str(e2)[:200]


def run(apk_dir: Path, out: Path, slug: str, name: str):
    apk = apk_dir / name
    root = out / slug
    root.mkdir(parents=True, exist_ok=True)
    z = zipfile.ZipFile(apk)
    names = z.namelist()
    raw = apk.read_bytes()
    meta = {
        "apk": name,
        "sha256": sha(raw),
        "size_bytes": len(raw),
        "zip_entries": len(names),
        "dex": [n for n in names if n.endswith(".dex")],
        "native_libs": [n for n in names if n.endswith(".so")],
        "flutter": any(n.startswith(FA) for n in names),
        "res_entries": sum(1 for n in names if n.startswith("res/")),
        "flutter_assets": sum(1 for n in names if n.startswith(FA)),
    }
    # ---- APK census (every member) -----------------------------------------
    census = []
    text_written = 0
    for n in names:
        info = z.getinfo(n)
        b = z.read(n)
        ext = Path(n).suffix.lower()
        is_text = (n.startswith(FA) and ext in TEXT_EXT) or n.endswith(
            ("AndroidManifest.xml", "resources.arsc"))
        dest = ""
        if is_text and n.startswith(FA):
            dest = "flutter_assets/" + n[len(FA):]
            p = root / dest
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(b)
            text_written += 1
        census.append({
            "path": n, "size": info.file_size, "compressed": info.compress_size,
            "crc32": "%08x" % info.CRC, "sha256": sha(b),
            "ext": ext, "text_copied": "yes" if dest else "no",
            "deliverable": dest or "APK_CENSUS.csv (hash only)",
        })
    with (root / "APK_CENSUS.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(census[0].keys()))
        w.writeheader(); w.writerows(census)

    # ---- manifest ----------------------------------------------------------
    if "AndroidManifest.xml" in names:
        xml, err = decode_axml(z.read("AndroidManifest.xml"))
        (root / "manifest").mkdir(exist_ok=True)
        (root / "manifest/AndroidManifest.xml").write_text(xml or "", encoding="utf-8")
        meta["manifest_decode_error"] = err
        if xml:
            m = re.search(r'package="([^"]+)"', xml)
            meta["package"] = m.group(1) if m else None
            meta["activities"] = len(re.findall(r"<activity\b", xml))
            meta["permissions"] = re.findall(r'android:name="android.permission.([A-Z_]+)"', xml)
            meta["manifest_themes"] = sorted(set(re.findall(r'android:theme="([^"]+)"', xml)))[:20]
    # ---- Android resource XML (AXML) --------------------------------------
    resroot = root / "res"
    errs = []
    for n in names:
        if n.startswith("res/") and n.endswith(".xml"):
            xml, err = decode_axml(z.read(n))
            if err:
                errs.append([n, err])
            if xml:
                p = resroot / n[4:]
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(xml, encoding="utf-8")
    meta["res_xml_decoded"] = sum(1 for n in names if n.startswith("res/") and n.endswith(".xml")) - len(errs)
    meta["res_xml_errors"] = errs[:20]
    (root / "RES_ERRORS.json").write_text(json.dumps(errs, ensure_ascii=False, indent=2), encoding="utf-8")

    # ---- Dart AOT snapshot strings ----------------------------------------
    lib = next((n for n in names if n.endswith("libapp.so") and "arm64" in n), None)
    dart_dir = root / "dart"
    dart_dir.mkdir(exist_ok=True)
    strings = set()
    if lib:
        b = z.read(lib)
        meta["dart_snapshot"] = lib
        meta["dart_snapshot_bytes"] = len(b)
        for m in re.finditer(rb"[ -~]{5,}", b):
            strings.add(m.group().decode("ascii", "ignore"))
        for m in re.finditer(rb"(?:[\xd8-\xdb][\x80-\xbf]|\x20){5,}", b):
            try:
                s = m.group().decode("utf-8", "ignore").strip()
                if s and re.search(r"[\u0600-\u06ff]", s):
                    strings.add(s)
            except Exception:
                pass
    allstr = sorted(strings)
    (dart_dir / "STRINGS_ALL.txt").write_text("\n".join(allstr), encoding="utf-8")
    meta["dart_strings"] = len(allstr)

    def dump(fn, pattern, flags=re.I):
        rx = re.compile(pattern, flags)
        hits = sorted({s.strip() for s in allstr if rx.search(s)})
        (dart_dir / fn).write_text("\n".join(hits), encoding="utf-8")
        return len(hits)

    meta["dart_ui_classes"] = dump(
        "UI_CLASS_NAMES.txt",
        r"^[A-Z][A-Za-z0-9_$.]*(Screen|Widget|View|Page|Cubit|State|Bar|Sheet|Dialog|Button|Card|Model|Binding|Repository|Datasource)$")
    meta["dart_endpoints"] = dump("ENDPOINTS.txt", r"^/[A-Za-z][A-Za-z0-9_/?=&.%-]{2,}$")
    meta["dart_routes"] = dump("ROUTES.txt", r"^/[a-z][a-z0-9_/-]{2,}$")
    meta["dart_persian"] = dump("PERSIAN_STRINGS.txt", r"[\u0600-\u06ff]")
    meta["dart_exam"] = dump("EXAM_STRINGS.txt", r"exam|question|quiz|wrong|mistake|weak|score|timer|result|answer|difficult", re.I)
    meta["dart_ai"] = dump("AI_STRINGS.txt", r"ai.?chat|chatbot|gpt|prompt|tutor|advisor|counsel|magic|robot", re.I)

    # ---- helpcenter lessons (the UX documentation shipped in Hamdars) ------
    lessons_p = root / "flutter_assets/assets/helpcenter/lessons.json"
    if lessons_p.is_file():
        d = json.loads(lessons_p.read_text(encoding="utf-8"))
        lines = ["# مستند UX/UI درون اپ — helpcenter/lessons.json", "",
                 "version=%s generated=%s" % (d.get("version"), d.get("generated")), "",
                 "## بخشها", ""]
        for s in d.get("sections", []):
            lines.append("- `%s` — %s (icon: %s)" % (s.get("key"), s.get("name"), s.get("icon")))
        lines += ["", "## درسها (همه)", ""]
        for les in d.get("lessons", []):
            lines.append("### %s — %s" % (les.get("id"), les.get("title")))
            lines.append("section=`%s` screen=`%s` priority=`%s`" % (
                les.get("section"), les.get("screen"), les.get("priority")))
            for i, st in enumerate(les.get("steps", []), 1):
                t = st.get("target", {})
                lines.append("%d. %s" % (i, st.get("caption", "")))
                if st.get("image"):
                    lines.append("   - تصویر: `%s`  ناحیهٔ هدف: x=%s y=%s w=%s h=%s" % (
                        st.get("image"), t.get("x"), t.get("y"), t.get("w"), t.get("h")))
            lines.append("")
        (root / "HELP_CENTER_UX.md").write_text("\n".join(lines), encoding="utf-8")
        meta["helpcenter_sections"] = len(d.get("sections", []))
        meta["helpcenter_lessons"] = len(d.get("lessons", []))
        meta["helpcenter_steps"] = sum(len(l.get("steps", [])) for l in d.get("lessons", []))
        meta["helpcenter_screenshots"] = sum(1 for n in names if "helpcenter/shots/" in n)

    # ---- asset folder census ----------------------------------------------
    folders = Counter()
    for n in names:
        if n.startswith(FA + "assets/"):
            rel = n[len(FA + "assets/"):]
            folders["/".join(rel.split("/")[:2])] += 1
    with (root / "ASSET_FOLDERS.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f); w.writerow(["folder", "count"])
        for k, v in folders.most_common(): w.writerow([k, v])
    meta["asset_folders"] = dict(folders.most_common(20))
    meta["text_assets_copied"] = text_written
    (root / "META.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(slug, json.dumps({k: v for k, v in meta.items() if not isinstance(v, (list, dict)) or len(str(v)) < 120}, ensure_ascii=False))
    return meta


def main():
    apk_dir, out = Path(sys.argv[1]), Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    metas = {}
    for slug, name in APKS.items():
        metas[slug] = run(apk_dir, out / "SOURCE_APPS", slug, name)
    (out / "SOURCE_APPS/ALL_META.json").write_text(
        json.dumps(metas, ensure_ascii=False, indent=2), encoding="utf-8")
    print("DONE")


if __name__ == "__main__":
    main()
