# Reproducing Stage-2 Evidence

## 1. Requirements

| Item | Requirement | Notes |
|---|---|---|
| OS / arch | any Linux x86-64 | tested in this container |
| Python | 3.11 (3.10+ expected) | stdlib only for `tests/test_component_spec.py` |
| `unicorn` | 2.x (tested 2.1.4) | required for ROM-executed tests; those tests **skip** without it |
| `capstone` | 5.x (tested 5.0.7) | only for the disassembly helpers in `work/`; not imported by tests |
| Archive | `Streets-of-Rage_Genesis_EN.zip` in the repo root | never extracted into Git |

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install unicorn capstone
```

## 2. One-command verification

```bash
python3 tools/verify_stage2.py
```

Expected tail:

```
Ran 37 tests in ~7s
OK
Stage-2 evidence -> evidence/stage2/stage2_verification.json
tests: 37 passed, 0 failed, 0 errors, 0 skipped
differential comparisons vs original ROM code: 7740
```

Exit code 0 means every test passed; the JSON bundle records per-test status,
comparison counts, the measured jump profiles and the measured cheat table.

## 3. Separate runs

```bash
python3 -m unittest tests.test_component_spec -v        # 24 spec tests, no emulator
python3 -m unittest tests.test_recovered_behaviour -v    # 5 tests, needs unicorn
python3 -m unittest tests.test_differential_rom -v       # 8 tests, needs unicorn
python3 reconstruction/slice_runner.py reconstruction/scenarios/neutral_jump.json
```

Without `unicorn`, the two ROM-backed modules still *load* but every test is skipped
with an explicit reason — a skip is never reported as a pass.

## 4. Regenerating the extracted tables

```bash
python3 tools/extract_slice_tables.py
```

Writes `components/data/body_boxes.json` including the ROM SHA-256. The file is
committed, so regeneration is only needed if the archive changes.

## 5. Re-running Stage-1 evidence (unchanged)

```bash
python3 tools/verify_sor_forensics.py
```

Still writes `evidence/verification_results.json`. Stage 2 did not modify this tool or
its output.

## 6. Environment pitfalls (each cost real debugging time)

1. **CPU model.** `Uc(UC_ARCH_M68K, UC_MODE_BIG_ENDIAN)` defaults to a model that
   mis-executes `dbra` and `move.w sr`; call
   `ctl_set_cpu_model(UC_CPU_M68K_M68000)` and set `SR = 0x2700`.
2. **Address aliasing.** The 68000 sign-extends 16-bit absolute addresses, so
   `lea $b800.w,a0` yields `0xFFFFB800`, while 32-bit operands use `0x00FFxxxx`.
   Map one host buffer twice with `mem_map_ptr`; mapping two separate regions makes
   the two views diverge silently.
3. **Short absolutes in Python.** `$FF0C` must be addressed as `0x00FFFF0C`, not
   `0x00FF0C` (the latter is ROM address 65,292).
4. **Return sentinel.** `rts` needs a valid stack: write a sentinel long at
   `0x00FFFE00` and use it as `emu_start`'s end address.
5. **Writable ROM.** Unicorn maps the ROM writable by default; a stray write to
   `0x00FF0C` silently corrupts the image for that probe instance.
6. **`capstone` module shadowing.** A helper named `dis.py` breaks `import capstone`
   (circular import via stdlib `dis`); the helper here is `mdis.py`.

## 7. Determinism

All differential tests use seed `20261022`. Every comparison is integer-exact, so
repeated runs are byte-identical. `evidence/stage2/stage2_verification.json` is
regenerated deterministically apart from nothing — it contains no timestamps.

## 8. Known environment limits

* No full-system emulator is used (no VDP/Z80/DMA/controller), by design.
* Ghidra is not available in this container; disassembly uses Capstone, and all
  dynamic confirmation uses Unicorn.
* ROM images are never written outside the ZIP except into the gitignored `work/`
  scratch directory.
