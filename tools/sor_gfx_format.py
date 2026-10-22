"""Decompressor for Streets of Rage (Genesis) graphics banks.

Derived by hand from the ROM's own routine at $008192 (Mega Drive, REV 00):

  $008192  movem.l ...              entry
  $0081B2  move.w (a0)+,d2          header word
  $0081B4  lsl.w #1,d2 ; bcc       bit 15 -> select output handler variant
  $0081BC  lsl.w #2,d2             d2 = header*8 = number of 4-byte chunks
  $0081BE  movea.w d2,a5           a5 = chunk counter
  $0081C6  bsr.w $8280             build code table at $F600 (256 word entries)
  $0081DC  .. $8226                decode loop
  $008228  .. $8252                escape path for 8-bit prefixes >= $FC

Output unit is a nibble (one 4bpp pixel), packed by `lsl.l #4,d4 / or.b`
into a 32-bit accumulator which is flushed every 8 nibbles = 4 bytes.
So the tile data is nibble-packed: four bytes per 8-pixel row, high nibble
first. Confirmed independently against live VRAM (tools/gfx_render.py).

Symbol alphabet (built by $8280):
    record = [A][B][prefix...]
    A has bit7 set and starts a new value group; value = A & $0F
    B supplies length = B & $0F and count = (B & $70) >> 4
    a record with bit7 clear in B continues the current A group
    B == $FF terminates the table
    table index = prefix << (8 - length); the entry is written into
    (1 << (8 - length)) consecutive word slots
"""
from __future__ import annotations

import struct

TABLE_BASE = 0x8254          # handler table (variant 0 / variant 1)
CODE_TABLE_ADDR = 0x8254


class DecodeError(Exception):
    pass


def build_table(data: bytes, pos: int) -> tuple[list[tuple[int, int, int] | None], int]:
    """Build the 256-entry prefix table the way $8280 does."""
    table: list[tuple[int, int, int] | None] = [None] * 256
    value = None
    while True:
        if pos >= len(data):
            raise DecodeError("table ran past end of data")
        a = data[pos]; pos += 1
        if a == 0xFF:
            return table, pos
        value = a & 0x0F
        while True:
            if pos >= len(data):
                raise DecodeError("table ran past end of data")
            b = data[pos]
            if b >= 0x80:            # $828E: next byte starts a new A group
                break
            pos += 1
            length = b & 0x0F
            count = (b & 0x70) >> 4
            if pos >= len(data):
                raise DecodeError("table has no prefix byte")
            prefix = data[pos]; pos += 1
            slack = 8 - length
            start = prefix << slack
            slots = 1 << slack
            if start + slots > 256:
                raise DecodeError(f"code table overflow at prefix ${prefix:02X} len={length}")
            for k in range(slots):
                slot = start + k
                if table[slot] is not None:
                    raise DecodeError(f"code table overlap at slot ${slot:02X}")
                table[slot] = (length, count, value)


def decode(data: bytes, start: int = 0) -> tuple[bytes, dict]:
    """Decompress one bank starting at `start` inside `data`."""
    if start + 2 > len(data):
        raise DecodeError("no header")
    header = struct.unpack_from(">H", data, start)[0]
    variant = 1 if header & 0x8000 else 0
    tiles = (header << 3 & 0xFFFF) >> 3       # $81B4/$81BC: header & $1FFF
    chunks = tiles * 8                        # 4-byte chunks

    pos = start + 2
    table, pos = build_table(data, pos)
    table_gaps = sum(1 for e in table if e is None)

    # Simple MSB-first bit reader over the stream that follows the code table.
    # This is equivalent to the routine's 16-bit sliding window ($81DC-$8252)
    # and, unlike an incremental re-implementation, cannot drift on a refill.
    bitpos = pos * 8

    def peek(nbits: int) -> int:
        val = 0
        for i in range(nbits):
            bidx = bitpos + i
            byte = data[bidx >> 3] if (bidx >> 3) < len(data) else 0
            val = (val << 1) | ((byte >> (7 - (bidx & 7))) & 1)
        return val

    out = bytearray()
    acc = 0
    remain = 8
    symbols = 0

    while len(out) < chunks * 4:
        symbols += 1
        pk = peek(8)
        if pk >= 0xFC:                          # $81E4 -> escape path $8228
            bitpos += 6
            payload = peek(7)
            bitpos += 7
            count = (payload & 0x70) >> 4
            value = payload & 0x0F
        else:
            entry = table[pk]
            if entry is None:
                raise DecodeError(f"unassigned prefix ${pk:02X} at output byte {len(out)}")
            length, count, value = entry
            bitpos += length
        for _ in range(count + 1):
            acc = ((acc << 4) | value) & 0xFFFFFFFF
            remain -= 1
            if remain == 0:
                out += acc.to_bytes(4, "big")
                acc = 0
                remain = 8
                if len(out) >= chunks * 4:
                    break

    pos = (bitpos + 7) >> 3
    # Header bit 15 also switches the output handler to the "eor.l d4,d2"
    # variant ($825E / $8274): each 32-bit output long is XOR-chained with the
    # previous one, starting from zero. Verified against 3 captured streams.
    if variant:
        chained = bytearray()
        prev = 0
        for i in range(0, len(out) - 3, 4):
            acc = struct.unpack_from(">I", out, i)[0]
            prev ^= acc
            chained += struct.pack(">I", prev)
        out = chained

    return bytes(out), {
        "header": header, "variant": variant, "tiles": tiles, "xor_chain": bool(variant),
        "bytes": len(out), "symbols": symbols, "input_bytes": pos - (start + 2),
        "table_gaps": table_gaps, "end_pos": pos,
    }
