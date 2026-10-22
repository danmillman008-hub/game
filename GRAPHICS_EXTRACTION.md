# Graphics extraction — status

Every claim is labelled: `[ROM]` read from the cartridge, `[EMU]` observed by running the
unmodified ROM in an emulator, `[TEST]` reproduced by our own code, `[OPEN]` not established.

## The ROM has two decompressors `[ROM]`

| routine | scheme | used by | destination |
|---|---|---|---|
| `$008192` (alt entry `$0081A4`) | custom bitstream | loader at `$008642` | VRAM |
| `$0085A2` | **Kosinski** | loader at `$00B748` | RAM (`$FF0000`-range) |

`$0085A2` matches the classic Kosinski algorithm instruction for instruction: bit-stream
refill, `1` = literal byte, `01` = 8-bit-offset match, `00` = wider match with a 3-bit length,
length byte `0` = end and `1` = restart the bit stream.

## Decoder `$008192` `[ROM]` `[TEST]`

| item | value |
|---|---|
| header word | `tiles = header & $1FFF` |
| header bit 15 | selects the XOR-chain output handler (`$825E`/`$8274`) |
| output | `tiles × 32` bytes, 4bpp packed (2 px/byte, high nibble left) |
| table | built by `$8280` into `$FFFFF600`, 256 word slots |
| symbols | (value, count) nibble runs; prefix `>= $FC` escapes to 6 ones + 3-bit count + 4-bit value |
| implementation | `tools/sor_gfx_format.py` |

## Verification `[EMU]` `[TEST]`

The decoder is checked against the ROM's own code, not against how the output looks:

```sh
tools/md_capture/build.sh                        # headless Genesis Plus GX + observation hooks
tools/md_capture/build/mdcap rom.bin 1950 /tmp/cap events.txt
python3 tools/validate_gfx.py /tmp/cap/decomp.bin        # decoder vs the game's own output
python3 tools/validate_vram_path.py /tmp/cap             # decoder output vs VRAM contents
```

* `validate_gfx.py` — **11/11 captured decompressions byte-exact** (10 distinct sources).
* `validate_vram_path.py` — **11/11 decode to the exact bytes found in VRAM at the address the
  game was writing to when it called `$008192`**, in a VRAM image captured after the call.

That second check is the one that closes the loop: it proves the bytes we produce are the bytes
the console stored. Two of the streams only match once the XOR chaining is applied.

## Asset tables `[ROM]`

### `$00A666` — 56 records `[ROM]` `[TEST]`

Records are 8 bytes: `{long source, word field2, word flags}`.

* **56/56 decode** → 6,613 tiles (211,616 bytes).
  * 43 use the `$008192` bitstream.
  * 13 use Kosinski; all 13 yield whole 32-byte tiles and fit inside VRAM.
* **`field2` is not the VRAM destination.** Every source we could observe at runtime (12 of them)
  decompressed somewhere else: 0/12 matched. `field2` is exported verbatim and its meaning is
  listed as unresolved rather than guessed.

### `$00B768` — 14 records `[ROM]`

`{long source, long RAM destination}`, loaded by `$00B748` via `jsr $0085A2` (Kosinski).
Destinations are in the `$FF0000` range, so this path stages tiles in RAM rather than VRAM.

## What is proven end-to-end

```
ROM stream --[$008192 / $0085A2]--> decoded bytes --[DMA]--> VRAM  [EMU][TEST]
```

The first arrow is byte-exact for 11 live captures; the second is confirmed for the same 11.

## Open `[OPEN]`

* Meaning of `field2` in `$00A666`.
* Which loader the 13 Kosinski entries in `$00A666` go through at runtime — they are *also* in
  the `$B768` RAM table, so the `$A666` record may describe a different use of the same stream.
  Not yet traced.
* Sprite composition: which tiles form a frame, anchors, per-frame offsets, animation timing.
  The sprite-list builder near `$00AF46` has not been traced.
* Palette assignment per actor/stage. CRAM is captured per frame, so palette *rows* are readable
  from the running game, but the assignment logic is not mapped.
* `tools/vdp_render.py` reproduces one captured frame **pixel-exactly (0/71,680 differ)** but not
  gameplay frames, which use scroll/window effects that an end-of-frame state snapshot cannot
  reproduce. Until that is fixed, the emulator's own frames are the rendering reference.

## Reproduce

```sh
python3 tools/gfx_assets.py                    # decode both tables
python3 tools/validate_gfx.py <decomp.bin>     # decoder vs the running ROM
python3 tools/validate_vram_path.py <capture>  # decoder output vs VRAM
SDL_VIDEODRIVER=dummy .venv/bin/python tools/gfx_gallery.py <frame>.cram
```
