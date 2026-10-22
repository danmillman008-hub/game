"""Minimal binary PPM (P6) reader and image comparison helpers."""
from __future__ import annotations

from pathlib import Path


def read_ppm(path) -> tuple[int, int, bytes]:
    data = Path(path).read_bytes()
    if not data.startswith(b"P6"):
        raise ValueError(f"{path}: not a P6 PPM")
    fields, pos = [], 2
    while len(fields) < 3:
        while data[pos:pos + 1].isspace():
            pos += 1
        if data[pos:pos + 1] == b"#":
            while data[pos:pos + 1] not in (b"\n", b""):
                pos += 1
            continue
        start = pos
        while not data[pos:pos + 1].isspace():
            pos += 1
        fields.append(int(data[start:pos]))
    pos += 1
    w, h, _maxval = fields
    return w, h, data[pos:pos + w * h * 3]


def compare(a: tuple[int, int, bytes], b: tuple[int, int, bytes]) -> dict:
    """Pixel comparison of two PPM images of equal size."""
    (wa, ha, pa), (wb, hb, pb) = a, b
    if (wa, ha) != (wb, hb):
        raise ValueError(f"size mismatch: {wa}x{ha} vs {wb}x{hb}")
    total = wa * ha
    diff = 0
    rows = [0] * ha
    cols = [0] * wa
    for i in range(total):
        j = i * 3
        if pa[j:j + 3] != pb[j:j + 3]:
            diff += 1
            rows[i // wa] += 1
            cols[i % wa] += 1
    return {"width": wa, "height": ha, "compared": total, "different": diff,
            "ratio": diff / total if total else 0.0,
            "rows": rows, "cols": cols}
