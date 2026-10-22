# Graphics extraction — status

All claims below are labelled `[ROM]` (read from the cartridge), `[EMU]` (observed by running the
unmodified ROM in an emulator and recording what it did), `[DEMO]` (our code proves the same
bytes), or `[OPEN]` (not established).

## Decoder — solved `[ROM]` `[DEMO]`

| item | value |
|---|---|
| routine | `$008192` (variant entry `$0081A4`) |
| header | `tiles = header & $1FFF`; bit 15 selects the XOR-chain output handler |
| output | `tiles × 32` bytes, 4bpp packed (2 px/byte, high nibble left) |
| table | built by `$8280` into `$FFFFF600`, 256 word slots |
| symbols | (value, count) nibble runs; escape for prefixes `>= $FC` = 6 ones + 3-bit count + 4-bit value |
| implementation | `tools/sor_gfx_format.py` |

## Verification `[EMU]`

The decoder is checked against the ROM's own code, not against how the output looks:

```sh
tools/md_capture/build.sh                      # headless Genesis Plus GX + hooks
tools/md_capture/build/mdcap rom.bin 1600 /tmp/cap events.txt
python3 tools/validate_gfx.py /tmp/cap/decomp.bin
```

Result: **11 captured decompressions, 10 distinct sources, 11 byte-exact reproductions**
(`evidence/gfx_decoder_validation.json`). Two of the streams carry header bit 15 and only match
once the XOR chaining is applied.

## Assets `[ROM]`

* master table `$00A666`: 56 records `{long src, word vram, word flag}`, parsed by
  `tools/gfx_assets.py`.
* 43/56 decode → 5,153 tiles. Raw data in `reconstruction/gfx/assets/*.bin`, provenance in
  `reconstruction/gfx/assets/index.json` (source address, VRAM destination, header, tile count,
  SHA-256).
* contact sheets with the game's own palettes: `reconstruction/gfx/gallery/`
  (`tools/gfx_gallery.py <cram dump>`).
* the second table at `$8672` (31 entries, `tools/gfx_banks.py` → `reconstruction/gfx/banks.json`)
  also decodes completely — 36/36 entries, 9,423 tiles — but it is not the one the game feeds to
  the decompressor during play.

## Open `[OPEN]`

* 13 of the 56 `$00A666` entries do not decode with this format (they fail on the first symbol).
  Candidate causes: a different scheme, a table index we have not found, or non-graphics data.
  Not resolved, not guessed.
* No confirmed mapping yet from a decompressed asset to a VRAM address *as observed during play*:
  searching the captured VRAM dumps for decoded output found no match, while the decompression
  captures themselves are exact. So the pipeline ROM → decoder → bytes is proven, and the
  pipeline bytes → screen is not. This is the next thing to close.
* Sprite composition (which tiles form a frame, anchor points, animation timing) is still
  identified-only; the sprite-list builder around `$00AF46` has not been traced.
* Palettes: CRAM is captured (`fNNNN.cram`), so palette *rows* can be read from the running game,
  but the per-actor/per-stage palette assignment is not yet mapped.

## Reproduce

```sh
python3 tools/gfx_assets.py                 # decode the master table
python3 tools/validate_gfx.py <decomp.bin>  # prove the decoder against the running ROM
SDL_VIDEODRIVER=dummy .venv/bin/python tools/gfx_gallery.py <cram dump>
```
