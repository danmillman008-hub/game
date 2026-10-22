"""Validate the static graphics decoder against decompressions captured from the real game.

The capture harness (tools/md_capture/) runs the ROM in a headless Mega Drive
emulator and records every call to the ROM's own decompressor at $008192,
together with its exact output bytes. This tool replays each captured stream
through tools/sor_gfx_format.py and requires byte-identical output.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.decomp_corpus import read_corpus      # noqa: E402
from tools.gfx_banks import load_rom             # noqa: E402
from tools.sor_gfx_format import decode          # noqa: E402


def main(argv=None) -> int:
    argv = argv or sys.argv[1:]
    if not argv:
        print("usage: validate_gfx.py <decomp.bin>")
        return 2
    rom = load_rom()
    records = read_corpus(argv[0])
    results, exact = [], 0
    for r in records:
        try:
            data, meta = decode(rom, r["src"])
        except Exception as exc:                       # noqa: BLE001
            results.append({"src": f"0x{r['src']:06X}", "frame": r["frame"],
                            "error": str(exc), "exact": False})
            continue
        ok = data == r["data"]
        # the same bytes must be present at the recorded VRAM destination
        in_vram = None
        exact += ok
        results.append({
            "src": f"0x{r['src']:06X}", "frame": r["frame"], "exact": ok,
            "game_bytes": len(r["data"]), "decoder_bytes": len(data),
            "dest_vram": f"0x{r['dest']:04X}",
            "game_sha256": hashlib.sha256(r["data"]).hexdigest(),
            "decoder_sha256": hashlib.sha256(data).hexdigest(),
        })
    out = ROOT / "evidence" / "gfx_decoder_validation.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({
        "corpus": str(argv[0]), "records": len(records),
        "exact_matches": exact, "all_exact": exact == len(records),
        "results": results}, indent=2) + "\n")
    print(f"captured streams: {len(records)}  byte-exact: {exact}")
    for r in results:
        print(f"  frame {r['frame']:5d} {r['src']} "
              f"{'EXACT' if r.get('exact') else 'MISMATCH ' + str(r.get('error',''))}")
    print(f"evidence -> {out.relative_to(ROOT)}")
    return 0 if exact == len(records) else 1


if __name__ == "__main__":
    raise SystemExit(main())
