"""Graphics-bank extraction from the ROM (Stage 4).

The game loads its graphics through one routine at $008642:

    lea.l  $8672(pc),a1          ; a1 = offset table
    add.w  d0,d0                 ; bank index
    move.w (a1,d0.w),d0
    lea.l  (a1,d0.w),a1          ; descriptor for this bank
    move.w (a1)+,d1              ; count-1  (dbra)
.loop:
    movea.l (a1)+,a0             ; source pointer (68k address space = ROM offset)
    moveq  #0,d0
    move.w (a1)+,d0              ; VRAM destination
    lsl.l  #2,d0 / lsr.w #2,d0   ; (pure VRAM addressing dance)
    ori.w  #$4000,d0
    swap   d0
    move.l d0,$C00004            ; VDP control: write to VRAM
    bsr.w  $8192                 ; Kosinski decompressor (variant A)
    dbra   d1,.loop

So each bank is a list of (compressed source, VRAM address) pairs. This module
parses that table and decompresses every bank with the Kosinski decoder the
project already validated against the ROM's own $0085A2 routine.

Usage:
    python tools/gfx_banks.py            # inventory + decompress everything
    python tools/gfx_banks.py --table    # just print the parsed table
"""
from __future__ import annotations

import argparse
import hashlib
import json
import struct
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROM_ZIP = ROOT / "Streets-of-Rage_Genesis_EN.zip"
ROM_NAME = "Streets of Rage (JUE) (REV 00) [!].bin"
ROM_SHA256 = "dd44f120446654bb91c448762f3e0cd0d9b034f35d0e3266a4dc34402ada95c0"

TABLE_ADDR = 0x8672          # from `lea.l $8672(pc),a1` at $008642
DATA_DIR = ROOT / "reconstruction" / "gfx"

sys.path.insert(0, str(ROOT))
from tools.sor_gfx_format import decode as decode_gfx  # noqa: E402  (derived from $008192)


def load_rom() -> bytes:
    with zipfile.ZipFile(ROM_ZIP) as z:
        rom = z.read(ROM_NAME)
    digest = hashlib.sha256(rom).hexdigest()
    if digest != ROM_SHA256:
        raise SystemExit(f"ROM hash mismatch: {digest}")
    return rom


def _w(rom, off):
    return struct.unpack_from(">H", rom, off)[0]


def _l(rom, off):
    return struct.unpack_from(">I", rom, off)[0]


def parse_table(rom: bytes, max_banks: int = 64) -> list[dict]:
    """Return [{index, descriptor, entries:[{src, vram}]}]."""
    banks = []
    for idx in range(max_banks):
        rel = _w(rom, TABLE_ADDR + 2 * idx)
        desc = TABLE_ADDR + rel
        if not (TABLE_ADDR <= desc < 0x10000):
            break                       # left the loader's own code/data area
        count = _w(rom, desc) + 1
        if count > 32:
            break
        entries, p, ok = [], desc + 2, True
        for _ in range(count):
            src = _l(rom, p)
            vram = _w(rom, p + 4)
            p += 6
            if not (0x200 <= src < len(rom)) or (vram & 0x7FFF) > 0x8000:
                ok = False
                break
            entries.append({"src": src, "vram": vram})
        if not ok or not entries:
            break
        banks.append({"index": idx, "descriptor": desc, "count": count, "entries": entries})
    return banks


def extract(rom: bytes, banks: list[dict]) -> list[dict]:
    """Decompress every entry; derive the VRAM byte range each one covers."""
    out = []
    for bank in banks:
        parts = []
        for k, e in enumerate(bank["entries"]):
            data, meta = decode_gfx(rom, e["src"])
            part = {
                "index": k,
                "src": e["src"],
                "vram": e["vram"],
                "compressed_bytes": meta["end_pos"] - e["src"],
                "stream_bytes": meta["input_bytes"],
                "decompressed_bytes": len(data),
                "tiles": len(data) // 32,
                "symbols": meta["symbols"],
                "table_gaps": meta["table_gaps"],
                "sha256": hashlib.sha256(data).hexdigest(),
                "data": data,
            }
            parts.append(part)
        total = sum(p["decompressed_bytes"] for p in parts)
        out.append({"index": bank["index"], "entries": parts, "total_bytes": total,
                    "total_tiles": total // 32})
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--table", action="store_true")
    ap.add_argument("--json", default=str(DATA_DIR / "banks.json"))
    args = ap.parse_args(argv)

    rom = load_rom()
    banks = parse_table(rom)
    print(f"ROM ok ({len(rom)} bytes, sha256 {ROM_SHA256[:16]}…)")
    print(f"graphics bank table at ${TABLE_ADDR:06X}: {len(banks)} banks")
    for b in banks:
        print(f"  bank {b['index']:2d}  descriptor ${b['descriptor']:06X}  {b['count']} entr"
              f"{'y' if b['count'] == 1 else 'ies'}")
        for e in b["entries"]:
            print(f"      src ${e['src']:06X} -> VRAM ${e['vram']:04X}")
    if args.table:
        return 0

    data = extract(rom, banks)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    raw_dir = DATA_DIR / "raw"
    raw_dir.mkdir(exist_ok=True)
    inventory = []
    for bank in data:
        for part in bank["entries"]:
            name = f"bank{bank['index']:02d}_{part['index']}_vram{part['vram']:04X}.tiles"
            (raw_dir / name).write_bytes(part["data"])
            inventory.append({
                "bank": bank["index"], "entry": part["index"],
                "src": f"0x{part['src']:06X}", "vram": f"0x{part['vram']:04X}",
                "compressed_bytes": part["compressed_bytes"],
                "stream_bytes": part["stream_bytes"],
                "decompressed_bytes": part["decompressed_bytes"],
                "tiles": part["tiles"], "symbols": part["symbols"],
                "table_gaps": part["table_gaps"],
                "sha256": part["sha256"], "file": name,
            })
    Path(args.json).write_text(json.dumps({
        "rom": {"name": ROM_NAME, "sha256": ROM_SHA256, "size": len(rom)},
        "table_addr": f"0x{TABLE_ADDR:06X}",
        "loader": "0x008642 -> bsr.w $008192 (game-specific Huffman/RLE, see tools/sor_gfx_format.py)",
        "banks": len(data),
        "entries": len(inventory),
        "total_bytes": sum(i["decompressed_bytes"] for i in inventory),
        "total_tiles": sum(i["tiles"] for i in inventory),
        "items": inventory,
    }, indent=1))
    print(f"\nentries decompressed: {len(inventory)}")
    print(f"total decompressed   : {sum(i['decompressed_bytes'] for i in inventory):,} bytes "
          f"({sum(i['tiles'] for i in inventory):,} tiles)")
    print(f"inventory -> {Path(args.json).relative_to(ROOT)}")
    print(f"raw tiles -> {raw_dir.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
