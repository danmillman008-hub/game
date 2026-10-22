"""Body-box construction and AABB overlap (Stage-2 slice).

$004140 builds **two** 12-byte AABBs on the player path, one after the other:

    +$64  indexed by +$02 (sprite tile width)
    +$70  indexed by +$03 (sprite tile height)

Both use the same two ROM tables, and both are stored as six *words*:

    x1, x2, z1, z2, y1, y2      (integer pixels, world space)

Each table record supplies a corner plus an extent for X and Y and a z-index;
the z-table supplies a corner plus an extent for Z. Extents are **cumulative**
(x2 = x1 + extent), not absolute offsets:

    x1 = X_hi + b0        x2 = x1 + b1
    z1 = Z_hi + z[b2][0]  z2 = z1 + z[b2][1]
    y1 = Y_hi + b3        y2 = y1 + b4

The ROM's own arithmetic is 16-bit throughout (``move.w``/``add.w``), so results
wrap at 16 bits; :func:`s16` reproduces that.

Degenerate cases (all measured, see DIFFERENTIAL_VALIDATION.md D4):
  * index 0 in the +$64 build -> all six words = $0010, unless the record is the
    P1 base $FFFFB800, in which case all six = 0;
  * the +$70 build with index 0 -> all six = 0, unless bit1 of +$4B
    ("invulnerable") is set, in which case it uses the +$64 rule.
"""

from __future__ import annotations

from dataclasses import dataclass

from .actor import Actor
from .fixed import hi16, s16

P1_BASE_ADDRESS = 0xB800


@dataclass(frozen=True)
class Box:
    x1: int
    x2: int
    z1: int
    z2: int
    y1: int
    y2: int

    def as_tuple(self) -> tuple[int, int, int, int, int, int]:
        return (self.x1, self.x2, self.z1, self.z2, self.y1, self.y2)

    @classmethod
    def filled(cls, word: int) -> "Box":
        w = s16(word)
        return cls(w, w, w, w, w, w)


class BoxTables:
    """The two ROM tables, loaded from components/data/body_boxes.json."""

    def __init__(self, z_pairs: list[list[int]], records: list[list[int]]):
        self.z_pairs = [tuple(p) for p in z_pairs]
        self.records = [tuple(r) for r in records]

    @classmethod
    def load(cls, path=None) -> "BoxTables":
        import json
        from pathlib import Path
        path = Path(path) if path else Path(__file__).resolve().parent.parent / "data" / "body_boxes.json"
        doc = json.loads(path.read_text(encoding="utf-8"))
        return cls(doc["z_table"]["values"], doc["body_box_table"]["values"])

    def build(self, a: Actor, index: int) -> Box:
        b0, b1, b2, b3, b4 = self.records[index]
        x1 = s16(hi16(a.x) + b0)
        y1 = s16(hi16(a.y) + b3)
        zc, ze = self.z_pairs[b2]
        z1 = s16(hi16(a.z) + zc)
        return Box(
            x1=x1, x2=s16(x1 + b1),
            z1=z1, z2=s16(z1 + ze),
            y1=y1, y2=s16(y1 + b4),
        )


def build_player_boxes(a: Actor, tables: BoxTables, at_p1_base: bool = False) -> tuple[Box, Box]:
    """$004140 exactly, returning (primary +$64, secondary +$70)."""
    null_word = 0x0000 if at_p1_base else 0x0010

    primary = (tables.build(a, a.sprite_w) if a.sprite_w
               else Box.filled(null_word))

    if a.flags_4b & 0x02:
        secondary = Box.filled(null_word)
    elif a.sprite_h:
        secondary = tables.build(a, a.sprite_h)
    else:
        secondary = Box.filled(0x0000)
    return primary, secondary


def aabb_overlap(a: Box, b: Box) -> bool:
    """$00450C box predicate. Inclusive on every axis, evaluated Z, X, Y.

    The ROM compares A's *primary* box against B's *secondary* box; the caller
    invokes it in both directions, so this predicate is kept symmetric-agnostic
    and the direction is the caller's choice.
    """
    return (a.z1 <= b.z2 and a.z2 >= b.z1
            and a.x1 <= b.x2 and a.x2 >= b.x1
            and a.y1 <= b.y2 and a.y2 >= b.y1)
