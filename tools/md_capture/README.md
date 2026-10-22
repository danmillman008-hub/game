# Mega Drive capture harness

A headless build of [Genesis Plus GX](https://github.com/libretro/Genesis-Plus-GX)
plus a small frontend, used as a **measuring instrument**: it runs the original
ROM so that the game's own decompressor (`$008192`) can be observed, and records
the exact bytes it produces.

This is how the graphics decoder in `tools/sor_gfx_format.py` was verified:
every captured stream is replayed through the Python decoder and must match
byte for byte (`tools/validate_gfx.py`).

## Build

```sh
tools/md_capture/build.sh              # downloads + builds (needs network once)
tools/md_capture/build.sh /path/to/gpgx   # or reuse an existing checkout
```

Produces `tools/md_capture/build/mdcap`.

## Run

```sh
# run 1600 frames with scripted button presses, capture every decompression
tools/md_capture/build/mdcap rom.bin 1600 /tmp/cap events.txt

# events.txt: "<frame> <BUTTON>"  START/A/B/C/UP/DOWN/LEFT/RIGHT (held 4 frames)
#   300 START
#   420 START
```

Outputs in the target directory:

| file | contents |
|---|---|
| `decomp.bin` | records of every `$008192` call: `u32 frame, u32 src, u32 len, bytes` |
| `fNNNN.ppm` | screen snapshot every 100 frames |
| `fNNNN.vram` | 64 KB VRAM dump (raw bytes, word = 2 bytes big-endian) |
| `fNNNN.cram` | 128 words of CRAM (first 64 = the four palettes) |
| `final.*` | same, at the end of the run |

Read the capture with `tools/decomp_corpus.py`, validate with
`tools/validate_gfx.py`, and reconstruct memory images with
`tools/vdp_capture.py`.

## What is patched

`patches/gpgx_capture_hooks.py` applies two observation-only hooks:

* `core/vdp_ctrl.c` — while a capture is active, VDP data-port writes are copied
  to a buffer instead of the VRAM FIFO (so the decompressor's output can be read
  back without waiting for a FIFO flush);
* `core/debug/cpuhook.h` — `cpu_hook` becomes an `extern` declaration so the
  frontend can own it.

Emulated behaviour is unchanged, and the ROM file is never modified.
