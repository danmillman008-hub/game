#!/usr/bin/env python3
"""Extract the data tables used by the Stage-2 vertical slice from the original
ROM (inside the repository ZIP) into a provenance-stamped JSON config.

Read-only with respect to the archive. Writes components/data/body_boxes.json.
"""
from __future__ import annotations

import hashlib
import json
import struct
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZIP = ROOT / "Streets-of-Rage_Genesis_EN.zip"
ROM_NAME = "Streets of Rage (JUE) (REV 00) [!].bin"
OUT = ROOT / "components" / "data" / "body_boxes.json"

Z_TABLE = 0x1AB8E      # 13 x 2 signed bytes  (z corner, z extent)
BOX_TABLE = 0x1ABA8    # 32 x 5 signed bytes  (x corner, x extent, z index, y corner, y extent)
Z_COUNT = 13
BOX_COUNT = 32


def signed(b: int) -> int:
    return b - 256 if b > 127 else b


def main() -> None:
    with zipfile.ZipFile(ZIP) as zf:
        rom = zf.read(ROM_NAME)
    z = [[signed(b) for b in rom[Z_TABLE + 2 * i: Z_TABLE + 2 * i + 2]] for i in range(Z_COUNT)]
    boxes = [[signed(b) for b in rom[BOX_TABLE + 5 * i: BOX_TABLE + 5 * i + 5]] for i in range(BOX_COUNT)]
    doc = {
        "provenance": {
            "rom_file": ROM_NAME,
            "rom_sha256": hashlib.sha256(rom).hexdigest(),
            "rom_size": len(rom),
            "archive_sha256": hashlib.sha256(ZIP.read_bytes()).hexdigest(),
            "derived_by": "tools/extract_slice_tables.py",
            "note": "Signed-byte values exactly as stored; no interpretation applied.",
        },
        "z_table": {
            "rom_offset": f"0x{Z_TABLE:06X}", "count": Z_COUNT,
            "layout": "pairs [z_corner, z_extent]",
            "values": z,
            "consumers": ["$004140 body-box builder", "$00AB24 attack-shape walker"],
        },
        "body_box_table": {
            "rom_offset": f"0x{BOX_TABLE:06X}", "count": BOX_COUNT,
            "layout": "[x_corner, x_extent, z_index, y_corner, y_extent]",
            "values": boxes,
            "consumers": ["$004140 body-box builder", "$00AB24 for type $58"],
        },
        "engine_constants": {
            "gravity_neutral": "0x0000E800", "gravity_directional_descent": "0x00008800",
            "gravity_soft": "0x00003800", "vy_terminal_player": "0x000C0000",
            "air_accel": "0x00006000", "air_vx_clamp": "0x00038000",
            "screen_x_bias": "0x0080", "screen_y_bias": "0x0080",
            "cull_left_wide": "0xFF80", "cull_left_narrow": "0xFC80",
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
