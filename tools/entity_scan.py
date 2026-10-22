"""Locate per-entity state fields in work RAM by differential experiment.

Method: two runs that are identical except for one held direction. Ground truth
for "the player moved" comes from the sprite table; candidate RAM locations are
then scored by how well their low-16-bit value tracks a sprite x coordinate,
allowing the fixed-point scale the game uses to be discovered rather than
assumed.

Usage:
    python3 tools/entity_scan.py <run_off>/ <run_on>/ <first_frame> <last_frame> [--dump-from N]
"""
from __future__ import annotations

import argparse
import json
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.frame_state import ram_at          # noqa: E402
from tools.sat_log import read_frames, entries  # noqa: E402


def moving_sprites(off_dir: Path, on_dir: Path, frame0: int, frame1: int, dump_from: int):
    """Sprites whose (x, y, tile) differ between the two runs at frame1."""
    a = {f["frame"]: f for f in read_frames(str(off_dir / "frames.bin"))}
    b = {f["frame"]: f for f in read_frames(str(on_dir / "frames.bin"))}
    ea = {e["idx"]: e for e in entries(a[frame1]["sat"])}
    eb = {e["idx"]: e for e in entries(b[frame1]["sat"])}
    out = []
    for idx in sorted(ea):
        if ea[idx]["tile"] and eb[idx]["tile"]:
            if (ea[idx]["x"], ea[idx]["y"], ea[idx]["tile"]) != (eb[idx]["x"], eb[idx]["y"], eb[idx]["tile"]):
                out.append((idx, ea[idx], eb[idx]))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("off_dir")
    ap.add_argument("on_dir")
    ap.add_argument("first", type=int)
    ap.add_argument("last", type=int)
    ap.add_argument("--dump-from", type=int, default=0)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    off_dir, on_dir = Path(args.off_dir), Path(args.on_dir)
    frames = list(range(args.first, args.last + 1, max(1, (args.last - args.first) // 12 or 1)))
    rel = [f - args.dump_from for f in frames]

    print("sprites that differ at the last frame (off vs on):")
    for idx, ea, eb in moving_sprites(off_dir, on_dir, frames[0], frames[-1], args.dump_from):
        print(f"  #{idx:2d} off x={ea['x']:3d} y={ea['y']:3d} tile=${ea['tile']:03X}"
              f" | on x={eb['x']:3d} y={eb['y']:3d} tile=${eb['tile']:03X}")

    # candidate RAM words: value series in the "on" run, scored against a linear ramp
    series = {}
    for name, d in (("off", off_dir), ("on", on_dir)):
        series[name] = [ram_at(str(d / "ram.bin"), r) for r in rel]

    rows = []
    for addr in range(0, 0x10000, 2):
        vals = [struct.unpack_from(">h", r, addr)[0] for r in series["on"]]
        offs = [struct.unpack_from(">h", r, addr)[0] for r in series["off"]]
        if vals == offs:
            continue
        span = max(vals) - min(vals)
        if span == 0:
            continue
        # monotonicity: how consistently the series moves one way
        steps = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
        pos = sum(1 for s in steps if s > 0)
        neg = sum(1 for s in steps if s < 0)
        mono = max(pos, neg) / max(1, len(steps))
        rows.append({"addr": addr, "on": vals, "off": offs, "span": span, "mono": round(mono, 2)})

    rows.sort(key=lambda r: (-r["mono"], -r["span"]))
    print(f"\n{len(rows)} words differ; most consistent movers (mono=1.0 means always one direction):")
    for r in rows[:20]:
        print(f"  ${r['addr']:04X} mono={r['mono']:.2f} span={r['span']:5d} on={r['on'][:6]} off={r['off'][:6]}")

    if args.out:
        Path(args.out).write_text(json.dumps({"frames": frames, "dump_from": args.dump_from,
                                              "candidates": rows[:200]}, indent=2) + "\n")
        print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
