"""Extract every graphics asset listed in the ROM's master graphics table.

The table lives at $00A666 and holds 8-byte records:

    long  source address in ROM
    word  destination VRAM byte address
    word  bank/flag field

Each source is a stream in the format implemented by tools/sor_gfx_format.py
(decoder derived from $008192, byte-exact against 11 decompressions captured
from the running game).

Outputs (under reconstruction/gfx/assets/):
    <index>_<src>.bin   decoded 4bpp tile data
    index.json          provenance: index, src, vram, flags, tiles, sha256
"""
from __future__ import annotations

import hashlib
import json
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.gfx_banks import load_rom          # noqa: E402  (ROM access)
from tools.sor_gfx_format import decode, DecodeError  # noqa: E402

TABLE_ADDR = 0x00A666
OUT = ROOT / "reconstruction" / "gfx" / "assets"


def parse_asset_table(rom: bytes) -> list[dict]:
    out, addr = [], TABLE_ADDR
    while addr + 8 <= len(rom):
        src, vram, flag = struct.unpack_from(">IHH", rom, addr)
        if src >= len(rom) or src < 0x100 or flag > 0x10:
            break
        out.append({"index": len(out), "src": src, "vram": vram, "flag": flag,
                    "table_addr": addr})
        addr += 8
    return out


def main() -> int:
    rom = load_rom()
    entries = parse_asset_table(rom)
    OUT.mkdir(parents=True, exist_ok=True)
    index, failures = [], 0
    for e in entries:
        try:
            data, meta = decode(rom, e["src"])
        except DecodeError as exc:
            failures += 1
            index.append({**e, "error": str(exc)})
            continue
        name = f"{e['index']:02d}_{e['src']:06X}.bin"
        (OUT / name).write_bytes(data)
        index.append({
            **e, "src": f"0x{e['src']:06X}", "vram": f"0x{e['vram']:04X}",
            "header": meta["header"], "variant": meta["variant"],
            "tiles": meta["tiles"], "bytes": len(data),
            "stream_bytes": meta["input_bytes"],
            "sha256": hashlib.sha256(data).hexdigest(), "file": name,
        })
    (OUT / "index.json").write_text(json.dumps({
        "table": f"0x{TABLE_ADDR:06X}", "count": len(entries),
        "decoder": "tools/sor_gfx_format.py ($008192)",
        "note": "identical sources may appear with different VRAM destinations",
        "entries": index}, indent=2) + "\n")
    total_tiles = sum(e.get("tiles", 0) for e in index)
    print(f"assets: {len(entries)}  decoded: {len(entries)-failures}  failed: {failures}")
    print(f"tiles: {total_tiles}  ({total_tiles*32:,} bytes)")
    print(f"index -> {OUT/'index.json'}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
