"""Apply the two small source patches the capture harness needs to Genesis Plus GX.

The patches only add observation hooks; they do not change emulated behaviour.

  1. core/vdp_ctrl.c  - divert VDP data-port writes into a buffer while a capture
                        is active (used to record the decompressor's output).
  2. core/debug/cpuhook.h - make the `cpu_hook` pointer an extern declaration so
                        it can be defined once by decomp_hook.c.

Run:  python3 patches/gpgx_capture_hooks.py /path/to/Genesis-Plus-GX
"""
from __future__ import annotations

import sys
from pathlib import Path

HOOK = '''  if (md_capture_active) { *md_capture_ptr++ = (data >> 8) & 0xFF; *md_capture_ptr++ = data & 0xFF; md_capture_len += 2; return; }

'''

GLOBALS = '''
/* capture hooks: see tools/md_capture (inactive unless a harness enables them) */
int md_capture_active = 0;
unsigned char *md_capture_ptr = 0;
unsigned md_capture_len = 0;
'''


def patch_vdp(root: Path) -> bool:
    path = root / "core" / "vdp_ctrl.c"
    src = path.read_text()
    if "md_capture_active" in src:
        print("vdp_ctrl.c: already patched")
        return True
    changed = False
    for fn in ("vdp_68k_data_w_m4", "vdp_68k_data_w_m5"):
        old = "static void %s(unsigned int data)\n{\n  /* Clear pending flag */\n  pending = 0;\n" % fn
        new = "static void %s(unsigned int data)\n{\n" % fn + HOOK + \
              "  /* Clear pending flag */\n  pending = 0;\n"
        if old in src:
            src = src.replace(old, new, 1)
            changed = True
        else:
            print(f"vdp_ctrl.c: pattern for {fn} not found")
    if changed:
        marker = "static void vdp_68k_data_w_m4(unsigned int data);"
        src = src.replace(marker, GLOBALS + "\n" + marker, 1)
        path.write_text(src)
        print("vdp_ctrl.c: patched")
    return changed


def patch_cpuhook(root: Path) -> bool:
    path = root / "core" / "debug" / "cpuhook.h"
    src = path.read_text()
    if "extern void (*cpu_hook)" in src:
        print("cpuhook.h: already patched")
        return True
    old = "void (*cpu_hook)(hook_type_t type, int width, unsigned int address, unsigned int value);"
    new = "extern " + old
    if old not in src:
        print("cpuhook.h: pattern not found")
        return False
    path.write_text(src.replace(old, new, 1))
    print("cpuhook.h: patched")
    return True


def main(argv) -> int:
    if not argv:
        print(__doc__)
        return 2
    root = Path(argv[0])
    ok = patch_vdp(root) and patch_cpuhook(root)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
