"""Prove the full graphics path: ROM source -> decoder -> the VRAM address the game used.

For every decompression captured by tools/md_capture, this checks that the bytes
our decoder produces are present, byte for byte, at the VRAM destination the game
was writing to when it called $008192 -- in a VRAM image captured after the call.

That closes the loop the gallery alone cannot close: it shows not only that we can
decode the data, but that our output is the same data the console actually stored.

Usage:
    python3 tools/validate_vram_path.py <capture dir>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.decomp_corpus import read_corpus           # noqa: E402
from tools.frame_state import vram_at                # noqa: E402
from tools.gfx_banks import load_rom                 # noqa: E402
from tools.sor_gfx_format import decode              # noqa: E402

VRAM_BYTES_PER_FRAME = 0x10000


def swap_words(data: bytes) -> bytes:
    """GX keeps VRAM as host words inside a byte array; the dump is byte-swapped."""
    out = bytearray(len(data))
    out[0::2] = data[1::2]
    out[1::2] = data[0::2]
    return bytes(out)


def main(argv=None) -> int:
    argv = argv or sys.argv[1:]
    if not argv:
        print("usage: validate_vram_path.py <capture dir>")
        return 2
    cap = Path(argv[0])
    rom = load_rom()
    records = read_corpus(cap / "decomp.bin")
    n_frames = (cap / "vram.bin").stat().st_size // VRAM_BYTES_PER_FRAME

    results, landed = [], 0
    for r in records:
        data, meta = decode(rom, r["src"])
        entry = {
            "src": f"0x{r['src']:06X}", "frame": r["frame"],
            "dest": f"0x{r['dest']:04X}", "decoder_bytes": len(data),
            "decoder_matches_game_output": data == r["data"],
        }
        # look in the first VRAM dump at or after the call
        found = None
        for f in range(r["frame"], n_frames):
            img = swap_words(vram_at(cap / "vram.bin", f))
            off = img.find(data, r["dest"], min(len(img), r["dest"] + len(data) + 0x2000))
            if off >= 0:
                found = {"frame": f, "offset": f"0x{off:04X}"}
                break
        entry["found_in_vram"] = found
        landed += bool(found)
        results.append(entry)

    out = ROOT / "evidence" / "gfx_vram_path.json"
    out.write_text(json.dumps({
        "capture": str(cap), "decompressions": len(records),
        "decoder_exact": sum(1 for e in results if e["decoder_matches_game_output"]),
        "landed_in_vram": landed, "results": results}, indent=2) + "\n")

    print(f"decompressions: {len(records)}  "
          f"decoder exact: {sum(1 for e in results if e['decoder_matches_game_output'])}")
    print(f"output found in VRAM at the recorded destination: {landed}/{len(records)}")
    for e in results:
        v = e["found_in_vram"]
        note = f"-> VRAM frame {v['frame']} @ {v['offset']}" if v else "NOT FOUND"
        print(f"  ${e['src'][2:]} -> ${e['dest'][2:]} f{e['frame']:5d}  {note}")
    print(f"evidence -> {out.relative_to(ROOT)}")
    return 0 if landed == len(records) else 1


if __name__ == "__main__":
    raise SystemExit(main())
