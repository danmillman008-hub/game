"""Extract every graphics asset referenced by the ROM's resource tables.

Two tables are modelled, because the game has two loaders that use two different
compression schemes:

  A) $00A666 - 56 records of 8 bytes: {long source, word field2, word flags}.
     The meaning of `field2` is NOT established: it does not equal the VRAM
     destination the game actually used (0 of the 12 sources we could observe
     matched it), so it is exported verbatim and left unexplained.

  B) $00B768 - records of 8 bytes: {long source, long destination}, loaded by
     $00B748 which calls the Kosinski decompressor at $0085A2 and writes to RAM
     (destinations in the $FF0000 range), not to VRAM.

Source streams are decoded by whichever scheme actually works:
  * the custom bitstream of $008192 (tools/sor_gfx_format.py) - proven byte-exact
    against 11 decompressions captured from the running game
  * Kosinski ($0085A2) - standard algorithm; used by the $B768 loader

Outputs, under reconstruction/gfx/assets/:
    <index>_<src>.bin   decoded 4bpp tile data
    index.json          provenance for every entry
"""
from __future__ import annotations

import hashlib
import json
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.gfx_banks import load_rom                       # noqa: E402
from tools.sor_gfx_format import decode, DecodeError        # noqa: E402
from tools.verify_sor_forensics import kosinski_decompress_py  # noqa: E402

TABLE_A = 0x00A666
TABLE_B = 0x00B768
OUT = ROOT / "reconstruction" / "gfx" / "assets"


def parse_table(rom: bytes, addr: int, count: int | None = None) -> list[dict]:
    """Read {long, word, word} records; stop at the first implausible one."""
    out, a = [], addr
    while a + 8 <= len(rom):
        src, f2, flags = struct.unpack_from(">IHH", rom, a)
        if src >= len(rom) or src < 0x100 or flags > 0x10:
            break
        out.append({"index": len(out), "src": src, "field2": f2,
                    "flags": flags, "table_addr": a})
        a += 8
        if count and len(out) >= count:
            break
    return out


def parse_ram_table(rom: bytes, addr: int) -> list[dict]:
    """Read {long source, long destination} records used by $00B748."""
    out, a = [], addr
    while a + 8 <= len(rom):
        src, dest = struct.unpack_from(">II", rom, a)
        if src >= len(rom) or src < 0x100 or dest < 0x00F00000:
            break
        out.append({"index": len(out), "src": src, "dest_ram": dest, "table_addr": a})
        a += 8
    return out


def decode_any(rom: bytes, src: int) -> tuple[bytes, str, dict]:
    """Decode a source with $8192's scheme, falling back to Kosinski."""
    try:
        data, meta = decode(rom, src)
        return data, "bitstream-8192", meta
    except DecodeError:
        pass
    data, consumed = kosinski_decompress_py(rom, src)
    return data, "kosinski-85A2", {"input_bytes": consumed}


def main() -> int:
    rom = load_rom()
    OUT.mkdir(parents=True, exist_ok=True)
    table_a = parse_table(rom, TABLE_A)
    table_b = parse_ram_table(rom, TABLE_B)

    entries, failures = [], 0
    for e in table_a:
        try:
            data, fmt, meta = decode_any(rom, e["src"])
        except Exception as exc:                        # noqa: BLE001
            failures += 1
            entries.append({**e, "src": f"0x{e['src']:06X}", "error": str(exc)})
            continue
        name = f"{e['index']:02d}_{e['src']:06X}.bin"
        (OUT / name).write_bytes(data)
        entries.append({
            **e, "src": f"0x{e['src']:06X}", "format": fmt,
            "tiles": len(data) // 32, "bytes": len(data),
            "whole_tiles": len(data) % 32 == 0,
            "sha256": hashlib.sha256(data).hexdigest(), "file": name,
        })

    # sources that the RAM loader reaches, with their real (RAM) destinations
    ram_sources = {}
    for b in table_b:
        ram_sources.setdefault(b["src"], []).append(b)

    (OUT / "index.json").write_text(json.dumps({
        "table_a": {
            "address": f"0x{TABLE_A:06X}", "count": len(table_a),
            "record": "long source, word field2, word flags",
            "field2_meaning": "UNRESOLVED - does not equal the observed VRAM destination",
        },
        "table_b": {
            "address": f"0x{TABLE_B:06X}", "count": len(table_b),
            "record": "long source, long RAM destination",
            "loaded_by": "0x00B748 -> jsr 0x0085A2 (Kosinski)",
            "entries": table_b,
        },
        "decoders": {
            "bitstream-8192": "tools/sor_gfx_format.py, byte-exact vs 11 captured runs",
            "kosinski-85A2": "standard Kosinski, see 0x0085A2",
        },
        "entries": entries,
    }, indent=2) + "\n")

    by_fmt = {}
    for e in entries:
        by_fmt[e.get("format", "failed")] = by_fmt.get(e.get("format", "failed"), 0) + 1
    total = sum(e.get("tiles", 0) for e in entries)
    print(f"table A: {len(table_a)} entries, {failures} failures")
    for f, n in sorted(by_fmt.items()):
        print(f"   {f}: {n}")
    print(f"table B: {len(table_b)} entries ({len(ram_sources)} distinct sources, RAM loader)")
    print(f"tiles: {total} ({total*32:,} bytes)")
    print(f"index -> {OUT/'index.json'}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
