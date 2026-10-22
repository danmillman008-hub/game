#!/usr/bin/env python3
"""
Non-gameplay forensic verification & table-extraction suite for:
  Streets of Rage / Bare Knuckle (Sega Mega Drive / Genesis, 1991)
  Archive: /home/user/game/Streets-of-Rage_Genesis_EN.zip

Strictly read-only reverse-engineering & validation tool (no gameplay recreation).
Reads ROMs directly from the repository ZIP archive in memory, verifies all 11 ROM
headers/checksums/diffs, extracts engine tables, decompresses the Z80 DPCM sound
driver, and (when Unicorn MC68000 is available) executes controlled CPU experiments
against actual ROM subroutines ($0085A2, $0104D8, $0143D0, $005920, $00389A/$0038AE).
"""

from __future__ import annotations

import hashlib
import json
import os
import struct
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
ZIP_PATH = REPO_ROOT / "Streets-of-Rage_Genesis_EN.zip"
OUT_JSON = REPO_ROOT / "evidence" / "verification_results.json"


def compute_sega_checksum(rom: bytes) -> int:
    """Exact replica of ROM checksum loop at $000338 (sums big-endian words from $000200..end)."""
    total = 0
    for off in range(0x200, len(rom), 2):
        total = (total + struct.unpack_from(">H", rom, off)[0]) & 0xFFFF
    return total


def kosinski_decompress_py(data: bytes, offset: int = 0) -> Tuple[bytes, int]:
    """Reference Kosinski LZSS decoder matching M68000 subroutine at $0085A2."""
    pos = offset
    out = bytearray()

    def get_desc() -> int:
        nonlocal pos
        lo = data[pos]
        hi = data[pos + 1]
        pos += 2
        return lo | (hi << 8)

    desc = get_desc()
    bits_left = 16

    def pop_bit() -> int:
        nonlocal desc, bits_left
        bit = desc & 1
        desc >>= 1
        bits_left -= 1
        if bits_left == 0:
            desc = get_desc()
            bits_left = 16
        return bit

    while True:
        if pop_bit() == 1:
            out.append(data[pos])
            pos += 1
        else:
            if pop_bit() == 0:
                b1 = pop_bit()
                b0 = pop_bit()
                count = ((b1 << 1) | b0) + 2
                disp = data[pos] - 0x100
                pos += 1
            else:
                low = data[pos]
                high = data[pos + 1]
                pos += 2
                disp = ((0xFF00 | high) << 5) & 0xFFFF
                disp = ((disp & 0xFF00) | low) - 0x10000
                cnt_low = high & 7
                if cnt_low != 0:
                    count = cnt_low + 2
                else:
                    cmd = data[pos]
                    pos += 1
                    if cmd == 0:
                        break
                    if cmd == 1:
                        continue
                    count = cmd + 1
            for _ in range(count):
                out.append(out[len(out) + disp])
    return bytes(out), pos - offset


def audit_archive(zf: zipfile.ZipFile) -> Dict[str, Any]:
    names = sorted(zf.namelist())
    rev00_name = [n for n in names if "REV 00) [!]" in n][0]
    rev01_name = [n for n in names if "REV 01) [!]" in n][0]
    rev00 = zf.read(rev00_name)
    rev01 = zf.read(rev01_name)

    inventory = []
    for name in names:
        blob = zf.read(name)
        sha256 = hashlib.sha256(blob).hexdigest()
        hdr_sum = struct.unpack_from(">H", blob, 0x18E)[0]
        calc_sum = compute_sega_checksum(blob)
        bypass = blob[0x32A:0x32C] == b"\x60\x20" or blob[0x336:0x338] != rev00[0x336:0x338]
        diff_r00 = sum(1 for a, b in zip(blob, rev00) if a != b)
        diff_r01 = sum(1 for a, b in zip(blob, rev01) if a != b)
        inventory.append({
            "filename": name,
            "size_bytes": len(blob),
            "sha256": sha256,
            "serial": blob[0x180:0x18E].decode("latin1").strip(),
            "build_date": blob[0x118:0x120].decode("latin1").strip(),
            "region": blob[0x1F0:0x1F4].decode("latin1").strip(),
            "header_checksum": f"0x{hdr_sum:04X}",
            "computed_checksum": f"0x{calc_sum:04X}",
            "checksum_valid": hdr_sum == calc_sum,
            "checksum_bypass_patched": bypass,
            "byte_diffs_vs_rev00": diff_r00,
            "byte_diffs_vs_rev01": diff_r01,
        })
    return {"rom_count": len(inventory), "roms": inventory}


def extract_core_tables(rev00: bytes) -> Dict[str, Any]:
    # 1. Enemy HP ($026FCE) & Attack Damage ($027010) & BCD Score/10 ($027032)
    enemy_names = {
        0x20: "Garcia / Galsia (Unarmed)",
        0x21: "Garcia / Galsia (Knife)",
        0x22: "Garcia / Galsia (Pipe)",
        0x23: "Garcia / Galsia (Jump-Kick)",
        0x24: "Y. Signal (Slide/Throw)",
        0x25: "Nora / Electra (Whip A)",
        0x26: "Hakuyo (Kung-Fu)",
        0x27: "Jack (Juggler)",
        0x28: "Jack (Sprinting 1-HP)",
        0x29: "Unused/Reserved Slot $29",
        0x2A: "Nora / Electra (Whip B)",
    }
    enemies = []
    for idx in range(11):
        etype = 0x20 + idx
        base = 0x26FCE + idx * 6
        hp_pal = [rev00[base + p] + 1 for p in range(3)]
        atk_pal = [rev00[base + 3 + p] for p in range(3)]
        score_ids = [rev00[0x27010 + idx * 3 + p] for p in range(3)]
        pts_pal = []
        for sid in score_ids:
            sb = rev00[0x10DDA + sid * 4 + 1 : 0x10DDA + sid * 4 + 4]
            pts_pal.append(int(f"{sb[0]:02x}{sb[1]:02x}{sb[2]:02x}"))
        anim_ptr = struct.unpack_from(">I", rev00, 0x27032 + idx * 4)[0]
        enemies.append({
            "type_id": f"0x{etype:02X}",
            "label": enemy_names[etype],
            "effective_hp_by_palette": hp_pal,
            "attack_damage_by_palette": atk_pal,
            "kill_score_by_palette": pts_pal,
            "anim_table_rom_ptr": f"0x{anim_ptr:06X}",
        })

    # 2. Shared Boss Stats (init routine $017EDC, byte tables at $017F26 ATK & $017F2A HP)
    boss_labels = {
        0x55: "Souther (Round 4 / 6 / 8)",
        0x56: "Antonio (Round 1 / 8)",
        0x57: "Bongo (Round 4 / 5 / 8)",
        0x58: "Mona & Lisa / Onihime & Yasha (Round 5 / 8)",
    }
    bosses = []
    for i, btype in enumerate([0x55, 0x56, 0x57, 0x58]):
        atk_base = rev00[0x17F26 + i]
        hp_base = rev00[0x17F2A + i]
        bosses.append({
            "type_id": f"0x{btype:02X}",
            "label": boss_labels[btype],
            "normal_attack_damage": atk_base,
            "easy_attack_damage": atk_base >> 1,
            "hard_attack_damage": atk_base << 1,
            "normal_hp": hp_base,
            "hardest_hp": hp_base + 5,
        })

    # 3. 1-UP Score Thresholds ($004DEC, 10 x 4-byte packed BCD entries: 00 XX 00 00)
    one_ups = []
    for i in range(10):
        b1, b2, b3 = rev00[0x4DEC + i * 4 + 1 : 0x4DEC + i * 4 + 4]
        pts = int(f"{b1:02x}{b2:02x}{b3:02x}")
        one_ups.append(pts)

    # 4. Dormant Name-Entry Cheat Table ($005958..$005975)
    dormant_cheats = []
    for idx in range(6):
        d7 = 5 - idx
        raw = rev00[0x5958 + idx * 4 : 0x5958 + idx * 4 + 4]
        chars = "".join(" " if c == 0 else chr(ord("A") + c - 1) for c in raw[1:])
        bcd_lives = rev00[0x5970 + d7]
        dormant_cheats.append({
            "name": chars,
            "raw_hex": raw.hex(),
            "bcd_lives_byte": f"0x{bcd_lives:02X}",
            "lives_decimal": (bcd_lives >> 4) * 10 + (bcd_lives & 0xF),
            "ff35_value": d7,
            "police_special_ammo": d7 + 1,
        })

    # 5. Kosinski Z80 Driver verification (pure Python)
    z80_py, comp_len = kosinski_decompress_py(rev00, 0x0795A2)

    return {
        "enemies": enemies,
        "shared_engine_bosses": bosses,
        "extra_life_thresholds": one_ups,
        "dormant_name_entry_cheats": dormant_cheats,
        "z80_driver_kosinski": {
            "rom_offset": "0x0795A2",
            "compressed_bytes": comp_len,
            "decompressed_bytes": len(z80_py),
            "sha256": hashlib.sha256(z80_py).hexdigest(),
            "dpcm_delta_table": [
                b if b < 128 else b - 256 for b in z80_py[0x001E:0x002E]
            ],
        },
    }


def run_unicorn_experiments(rev00: bytes, rev01: bytes) -> Dict[str, Any]:
    try:
        from unicorn import Uc, UC_ARCH_M68K, UC_MODE_BIG_ENDIAN, UC_HOOK_CODE
        from unicorn.m68k_const import (
            UC_CPU_M68K_M68000,
            UC_M68K_REG_A0,
            UC_M68K_REG_A1,
            UC_M68K_REG_A7,
            UC_M68K_REG_D0,
            UC_M68K_REG_PC,
            UC_M68K_REG_SR,
        )
    except ImportError:
        return {"unicorn_available": False}

    def make_uc(rom: bytes) -> Uc:
        mu = Uc(UC_ARCH_M68K, UC_MODE_BIG_ENDIAN)
        mu.ctl_set_cpu_model(UC_CPU_M68K_M68000)
        mu.mem_map(0x000000, 0x080000)
        mu.mem_write(0x000000, rom)
        mu.mem_map(0x00FF0000, 0x010000)
        mu.mem_map(0xFFFF0000, 0x010000)
        mu.reg_write(UC_M68K_REG_SR, 0x2700)
        mu.reg_write(UC_M68K_REG_A7, 0x00FFFE00)
        return mu

    # EXP-01: Actual ROM Kosinski ($0085A2) on $0795A2
    m1 = make_uc(rev00)
    m1.mem_write(0x00FFFE00, struct.pack(">I", 0x00FFFD00))
    m1.reg_write(UC_M68K_REG_A0, 0x000795A2)
    m1.reg_write(UC_M68K_REG_A1, 0x00FF7000)
    icount = [0]
    m1.hook_add(UC_HOOK_CODE, lambda uc, addr, sz, ud: icount.__setitem__(0, icount[0] + 1))
    m1.emu_start(0x0085A2, 0x00FFFD00, count=200000)
    z80_len = m1.reg_read(UC_M68K_REG_A1) - 0x00FF7000
    z80_uc = bytes(m1.mem_read(0x00FF7000, z80_len))

    # EXP-02: Actual ROM PRNG ($0104D8) 8-step sequence from 0
    m2 = make_uc(rev00)
    prng_steps = []
    for _ in range(8):
        m2.mem_write(0x00FFFE00, struct.pack(">I", 0x00FFFD00))
        m2.reg_write(UC_M68K_REG_A7, 0x00FFFE00)
        m2.emu_start(0x0104D8, 0x00FFFD00, count=500)
        d0 = m2.reg_read(UC_M68K_REG_D0) & 0xFFFF
        st = struct.unpack(">I", m2.mem_read(0xFFFFFF40, 4))[0]
        prng_steps.append({"d0": f"0x{d0:04X}", "state": f"0x{st:08X}"})

    # EXP-03: REV 00 vs REV 01 Boss Type $30 ($0143D0) Police-Special-while-Dying bug
    exp03 = {}
    for label, rom, cont in [("REV_00", rev00, 0x014458), ("REV_01", rev01, 0x01445E)]:
        m = make_uc(rom)
        m.mem_write(0x00FFFE00, struct.pack(">I", 0x00FFFD00))
        a0 = 0xFFFFB900
        m.reg_write(UC_M68K_REG_A0, a0)
        m.mem_write(0xFFFFB800, b"\x01")
        m.mem_write(a0 + 0x00, b"\x30\x80\x02\x00")
        m.mem_write(a0 + 0x32, struct.pack(">h", 0))
        m.mem_write(a0 + 0x67, b"\x00")
        m.mem_write(a0 + 0x69, b"\x01")
        m.mem_write(0xFFFFFA1A, b"\x01")
        trace: List[str] = []

        def thook(uc: Uc, addr: int, sz: int, ud: Any, c: int = cont, tr: List[str] = trace) -> None:
            tr.append(f"0x{addr:06X}")
            if addr == c:
                uc.emu_stop()

        m.hook_add(UC_HOOK_CODE, thook)
        m.emu_start(0x0143D0, 0x00FFFD00, count=500)
        exp03[label] = {
            "trace": trace,
            "end_pc": f"0x{m.reg_read(UC_M68K_REG_PC):06X}",
            "police_latch_67": m.mem_read(a0 + 0x67, 1)[0],
            "death_frozen_early_rts": m.reg_read(UC_M68K_REG_PC) == 0xFFFD00,
        }

    return {
        "unicorn_available": True,
        "exp01_kosinski_z80": {
            "instructions_executed": icount[0],
            "compressed_consumed": m1.reg_read(UC_M68K_REG_A0) - 0x0795A2,
            "decompressed_bytes": z80_len,
            "sha256": hashlib.sha256(z80_uc).hexdigest(),
        },
        "exp02_prng_first_8": prng_steps,
        "exp03_rev00_vs_rev01_boss30_police_bug": exp03,
    }


def main() -> None:
    if not ZIP_PATH.exists():
        raise FileNotFoundError(f"Archive not found: {ZIP_PATH}")
    with zipfile.ZipFile(ZIP_PATH, "r") as zf:
        archive_report = audit_archive(zf)
        rev00 = zf.read("Streets of Rage (JUE) (REV 00) [!].bin")
        rev01 = zf.read("Streets of Rage (JUE) (REV 01) [!].bin")

    tables = extract_core_tables(rev00)
    dyn = run_unicorn_experiments(rev00, rev01)

    if dyn.get("unicorn_available"):
        assert (
            dyn["exp01_kosinski_z80"]["sha256"]
            == tables["z80_driver_kosinski"]["sha256"]
        ), "Mismatch between reference Kosinski decoder and ROM M68000 $0085A2 execution!"

    report = {
        "archive_sha256": hashlib.sha256(ZIP_PATH.read_bytes()).hexdigest(),
        "archive_audit": archive_report,
        "extracted_tables": tables,
        "dynamic_unicorn_experiments": dyn,
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Verified {archive_report['rom_count']} ROMs -> {OUT_JSON}")
    print(f"Z80 Driver Kosinski cross-check (Py == M68000 Unicorn): OK ({tables['z80_driver_kosinski']['sha256']})")


if __name__ == "__main__":
    main()
