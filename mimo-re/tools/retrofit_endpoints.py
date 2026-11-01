#!/usr/bin/env python3
"""Stage 7 — extract Retrofit endpoint declarations from DEX annotations.

Endpoint paths in Mimo live in *annotation values* (retrofit2.http.*), not in
`const-string` instructions, so a string scan cannot prove the HTTP verb.
This tool parses the DEX `annotations_directory` structures directly:

    annotations_directory_item -> annotated_methods[] -> annotation_set_item
      -> annotation_item -> encoded_annotation -> encoded_value(string)

Usage:
    python tools/retrofit_endpoints.py EXTRACTED_DIR OUT_JSON
"""
from __future__ import annotations

import glob
import json
import os
import struct
import sys

# encoded_value types (DEX spec): value_type = b0 & 0x1f, value_arg = b0 >> 5
V_STRING = 0x17
V_TYPE = 0x18
V_ARRAY = 0x1c
V_ANNOTATION = 0x1d
V_NULL = 0x1e
V_BOOLEAN = 0x1f
V_REF = {0x15, 0x16, 0x19, 0x1a, 0x1b}   # method_type/method_handle/field/method/enum


def uleb(b: bytes, o: int):
    r = s = 0
    while True:
        x = b[o]; o += 1
        r |= (x & 0x7F) << s
        if not x & 0x80:
            return r, o
        s += 7


class Dex:
    def __init__(self, buf: bytes):
        self.b = buf
        self.string_ids_size, self.string_ids_off = struct.unpack_from("<II", buf, 0x38)
        self.type_ids_size, self.type_ids_off = struct.unpack_from("<II", buf, 0x40)
        self.class_defs_size, self.class_defs_off = struct.unpack_from("<II", buf, 0x60)
        self._strings: dict[int, str] = {}
        self._types: dict[int, str] = {}

    def string(self, idx: int) -> str:
        if idx not in self._strings:
            off = struct.unpack_from("<I", self.b, self.string_ids_off + 4 * idx)[0]
            _, start = uleb(self.b, off)
            end = self.b.index(b"\x00", start)
            self._strings[idx] = self.b[start:end].decode("utf-8", "replace")
        return self._strings[idx]

    def type_name(self, idx: int) -> str:
        if idx not in self._types:
            sidx = struct.unpack_from("<I", self.b, self.type_ids_off + 4 * idx)[0]
            self._types[idx] = self.string(sidx)
        return self._types[idx]

    def encoded_value(self, o: int):
        b0 = self.b[o]; o += 1
        tag, arg = b0 & 0x1F, b0 >> 5
        if tag == V_STRING:
            idx, o = uleb(self.b, o); return self.string(idx), o
        if tag == V_TYPE:
            idx, o = uleb(self.b, o); return self.type_name(idx), o
        if tag in V_REF:
            return f"ref@{struct.unpack_from('<I', self.b, o)[0]:#x}", o + 4
        if tag == V_ARRAY:
            size, o = uleb(self.b, o); out = []
            for _ in range(size):
                v, o = self.encoded_value(o); out.append(v)
            return out, o
        if tag == V_ANNOTATION:
            return self.encoded_annotation(o)
        if tag == V_NULL:
            return None, o
        if tag == V_BOOLEAN:
            return bool(arg), o
        if tag == 0x00:                      # byte
            return self.b[o] - 256 if self.b[o] > 127 else self.b[o], o + 1
        if tag in (0x02, 0x03):              # short / char
            return struct.unpack_from("<h", self.b, o)[0], o + 2
        if tag == 0x04:                      # int
            return struct.unpack_from("<i", self.b, o)[0], o + 4
        if tag == 0x06:                      # long
            return struct.unpack_from("<q", self.b, o)[0], o + 8
        if tag == 0x10:                      # float
            return struct.unpack_from("<f", self.b, o)[0], o + 4
        if tag == 0x11:                      # double
            return struct.unpack_from("<d", self.b, o)[0], o + 8
        raise ValueError(f"unsupported encoded_value tag {tag:#x} arg {arg}")

    def encoded_annotation(self, o: int):
        type_idx, o = uleb(self.b, o)
        size, o = uleb(self.b, o)
        elements = {}
        for _ in range(size):
            name_idx, o = uleb(self.b, o)
            value, o = self.encoded_value(o)
            elements[self.string(name_idx)] = value
        return {"type": self.type_name(type_idx), "elements": elements}, o

    def annotation_at(self, off: int):
        vis = self.b[off]
        ann, _ = self.encoded_annotation(off + 1)
        ann["visibility"] = vis
        return ann

    def annotation_set(self, off: int):
        size = struct.unpack_from("<I", self.b, off)[0]
        out = []
        for i in range(size):
            a_off = struct.unpack_from("<I", self.b, off + 4 + 4 * i)[0]
            out.append(self.annotation_at(a_off))
        return out


def main(extracted: str, out_json: str) -> None:
    rows, classes_seen = [], 0
    for path in sorted(glob.glob(os.path.join(extracted, "*.dex"))):
        buf = open(path, "rb").read()
        if len(buf) < 0x70:
            continue
        dex = Dex(buf)
        for i in range(dex.class_defs_size):
            base = dex.class_defs_off + 32 * i
            class_idx, _, _, _, _, ann_off, _, _ = struct.unpack_from("<IIIIIIII", buf, base)
            classes_seen += 1
            if not ann_off:
                continue
            o = ann_off + 4                     # skip class_annotations_off
            fields_size = struct.unpack_from("<I", buf, o)[0]; o += 4 + 8 * fields_size
            methods_size = struct.unpack_from("<I", buf, o)[0]; o += 4
            for j in range(methods_size):
                method_idx, a_off = struct.unpack_from("<II", buf, o + 8 * j)
                for ann in dex.annotation_set(a_off):
                    t = ann["type"]
                    if "retrofit2/http/" not in t:
                        continue
                    rows.append({
                        "dex": os.path.basename(path),
                        "class": dex.type_name(class_idx),
                        "verb": t.rsplit("/", 1)[-1].rstrip(";"),
                        "value": ann["elements"].get("value"),
                        "hasBody": ann["elements"].get("hasBody"),
                        "class_annotation_names": [a["type"] for a in dex.annotation_set(struct.unpack_from("<I", buf, ann_off)[0])] if struct.unpack_from("<I", buf, ann_off)[0] else [],
                    })
    json.dump(rows, open(out_json, "w"), indent=1, ensure_ascii=False)
    print(f"classes scanned: {classes_seen} | retrofit annotations found: {len(rows)}")
    for r in rows[:10]:
        print(" ", r["verb"], r["value"], "->", r["class"])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
