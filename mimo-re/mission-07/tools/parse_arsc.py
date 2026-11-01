#!/usr/bin/env python3
"""MISSION-07 — manual ARSC (resources.arsc) decoder.

Why: androguard 4.1.4 cannot expose colour/dimen/style values for this APK
(`get_color_resources` returns raw bytes; `resource_configs` has 1 entry).
This tool parses the binary tables directly (struct-level), which is a
technically different path and yields name -> value per configuration.

Usage:
  parse_arsc.py --arsc /tmp/res/resources.arsc --out /tmp/arsc_full.json [--types color,dimen,string]
"""
from __future__ import annotations

import argparse
import json
import struct
import sys

RES_STRING_POOL = 0x0001
RES_TABLE = 0x0002
RES_TABLE_PACKAGE = 0x0200
RES_TABLE_TYPE = 0x0201
RES_TABLE_TYPE_SPEC = 0x0202

VALUE_TYPES = {
    0x00: "null", 0x01: "reference", 0x02: "attribute", 0x03: "string",
    0x04: "float", 0x05: "dimension", 0x06: "fraction", 0x07: "dynamic_reference",
    0x08: "dynamic_attribute", 0x10: "int_dec", 0x11: "int_hex", 0x12: "int_boolean",
    0x1C: "color_argb8", 0x1D: "color_rgb8", 0x1E: "color_argb4", 0x1F: "color_rgb4",
}


class Pool:
    def __init__(self, buf: bytes, off: int):
        (self.type, hsize, size, self.count, self.styles, self.flags,
         self.strings_start, self.styles_start) = struct.unpack_from("<HHIIIIII", buf, off)
        self.utf8 = bool(self.flags & 0x100)
        self.offsets = list(struct.unpack_from("<%dI" % self.count, buf, off + hsize))
        self.base = off
        self._buf = buf

    def get(self, i: int) -> str:
        if i < 0 or i >= self.count:
            return ""
        p = self.base + self.strings_start + self.offsets[i]
        b = self._buf
        if self.utf8:
            n = b[p]
            p += 2 if n & 0x80 else 1
            n = ((n & 0x7F) << 8) | b[p] if n & 0x80 else n
            if n & 0x80:
                n = ((n & 0x7F) << 8) | b[p]
                p += 1
                n = ((n & 0x7F) << 8) | b[p]
            p += 1
            return b[p:p + n * 1].decode("utf-8", "replace") if False else b[p:p + n].decode("utf-8", "replace")
        n = struct.unpack_from("<H", b, p)[0]
        p += 2
        if n & 0x8000:
            n = ((n & 0x7FFF) << 16) | struct.unpack_from("<H", b, p)[0]
            p += 2
        return b[p:p + n * 2].decode("utf-16-le", "replace")


def parse(arsc: bytes):
    rtype, hsize, size = struct.unpack_from("<HHI", arsc, 0)
    assert rtype == RES_TABLE, "not a resource table"
    pos = hsize
    gpool = None
    packages = []
    while pos < size:
        ctype = struct.unpack_from("<H", arsc, pos)[0]
        chdr, csize = struct.unpack_from("<HI", arsc, pos + 2)
        if ctype == RES_STRING_POOL and gpool is None:
            gpool = Pool(arsc, pos)
        elif ctype == RES_TABLE_PACKAGE:
            pid = struct.unpack_from("<I", arsc, pos + 8)[0]
            name = arsc[pos + 12:pos + 12 + 256].decode("utf-16-le", "replace").split("\x00")[0]
            type_off, last_t, key_off = struct.unpack_from("<III", arsc, pos + 268)
            types = Pool(arsc, pos + type_off)
            keys = Pool(arsc, pos + key_off)
            packages.append({"id": pid, "name": name, "types": types, "keys": keys, "pos": pos,
                             "hdr": chdr, "size": csize})
        pos += csize if csize else chdr
    return gpool, packages


def iter_entries(arsc: bytes, pkg: dict):
    start = pkg["pos"] + pkg["hdr"]
    end = pkg["pos"] + pkg["size"]
    specs = {}
    pos = start
    while pos < end:
        ctype = struct.unpack_from("<H", arsc, pos)[0]
        chdr, csize = struct.unpack_from("<HI", arsc, pos + 2)
        if csize == 0:
            break
        if ctype == RES_TABLE_TYPE_SPEC:
            tid = arsc[pos + 8]
            n = struct.unpack_from("<I", arsc, pos + 12)[0]
            specs[tid] = list(struct.unpack_from("<%dI" % n, arsc, pos + 16))
        elif ctype == RES_TABLE_TYPE:
            tid = arsc[pos + 8]
            tflags = arsc[pos + 9]
            entry_count, entries_start = struct.unpack_from("<II", arsc, pos + 12)
            cfg_size = struct.unpack_from("<I", arsc, pos + 20)[0]
            cfg = arsc[pos + 20:pos + 20 + cfg_size]
            config = describe_config(cfg)
            sparse = bool(tflags & 0x01)
            offset16 = bool(tflags & 0x02)
            pairs = []
            if sparse:
                for i in range(entry_count):
                    idx, off = struct.unpack_from("<HH", arsc, pos + chdr + i * 4)
                    pairs.append((idx, off * 4))
            elif offset16:
                offs = struct.unpack_from("<%dH" % entry_count, arsc, pos + chdr)
                pairs = [(i, o * 4) for i, o in enumerate(offs) if o != 0xFFFF]
            else:
                offs = struct.unpack_from("<%dI" % entry_count, arsc, pos + chdr)
                pairs = [(i, o) for i, o in enumerate(offs) if o != 0xFFFFFFFF]
            for i, o in pairs:
                if pos + entries_start + o + 8 > len(arsc):
                    continue
                ep = pos + entries_start + o
                esize, flags = struct.unpack_from("<HH", arsc, ep)
                if flags & 0x0001:  # complex/bag entry
                    n = struct.unpack_from("<I", arsc, ep + 12)[0]
                    yield (tid, i, config, {"complex": True, "count": n})
                else:
                    vsize, res0, vtype, vdata = struct.unpack_from("<HBBI", arsc, ep + esize)
                    yield (tid, i, config, {"size": vsize, "type": vtype, "data": vdata})
        pos += csize


def describe_config(cfg: bytes) -> str:
    if len(cfg) < 64:
        return "default"
    size, mcc, mnc = struct.unpack_from("<H", cfg, 0)[0], struct.unpack_from("<H", cfg, 2)[0], struct.unpack_from("<H", cfg, 4)[0]
    lang = cfg[8:10].decode("ascii", "replace").strip("\x00")
    region = cfg[10:12].decode("ascii", "replace").strip("\x00")
    screen_type, ui_mode = cfg[24], cfg[25]
    sdk = struct.unpack_from("<H", cfg, 24 + 2 * 0)[0]
    sdkv = struct.unpack_from("<H", cfg, 26)[0] if len(cfg) >= 28 else 0
    night = cfg[29] if len(cfg) > 29 else 0
    dpi = struct.unpack_from("<H", cfg, 20)[0] if len(cfg) >= 22 else 0
    parts = []
    if lang or region:
        parts.append(f"{lang}-{region}")
    if sdkv:
        parts.append(f"v{sdkv}")
    if night & 0x30:
        parts.append("night" if (night & 0x30) == 0x20 else "notnight")
    if dpi:
        parts.append(f"dpi{dpi}")
    return ",".join(parts) or "default"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arsc", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--types", default="")
    a = ap.parse_args()
    data = open(a.arsc, "rb").read()
    gpool, packages = parse(data)
    wanted = {t.strip() for t in a.types.split(",") if t.strip()}
    out = {"global_strings": gpool.count if gpool else 0, "packages": [], "resources": {}}
    for pkg in packages:
        type_names = [pkg["types"].get(i) for i in range(pkg["types"].count)]
        out["packages"].append({"id": pkg["id"], "name": pkg["name"], "types": type_names})
        for tid, idx, cfg, val in iter_entries(data, pkg):
            tname = type_names[tid - 1] if 0 < tid <= len(type_names) else f"type{tid}"
            if wanted and tname not in wanted:
                continue
            key = pkg["keys"].get(idx)
            rid = (pkg["id"] << 24) | (tid << 16) | idx
            rec = {"id": f"0x{rid:08x}", "key": key, "config": cfg}
            if val.get("complex"):
                rec["complex"] = True
            else:
                rec["value_type"] = VALUE_TYPES.get(val["type"], f"0x{val['type']:02x}")
                if val["type"] == 0x03 and gpool:
                    rec["value"] = gpool.get(val["data"])
                elif val["type"] in (0x1C, 0x1D, 0x1E, 0x1F):
                    rec["value"] = f"#{val['data']:08x}"
                elif val["type"] == 0x05:
                    rec["value"] = f"{val['data'] / 10000.0}dp" if val["data"] else "0dp"
                else:
                    rec["value"] = val["data"]
            out["resources"].setdefault(tname, {}).setdefault(key, []).append(rec)
    json.dump(out, open(a.out, "w", encoding="utf-8"), indent=1)
    print("packages:", [p["name"] for p in packages])
    print("types:", {k: len(v) for k, v in out["resources"].items()})
    return 0


if __name__ == "__main__":
    sys.exit(main())
