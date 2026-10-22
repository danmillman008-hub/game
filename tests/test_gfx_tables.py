"""Regression tests for the graphics resource tables.

Locks in the result that all 56 records of table $00A666 decode, that the 13
Kosinski-compressed records are whole-tile aligned and fit in VRAM, and that the
decoder stays byte-exact against decompressions captured from the running ROM.

Run:  python3 -m unittest tests.test_gfx_tables -v
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools.gfx_banks import load_rom                          # noqa: E402
from tools.gfx_assets import parse_table, parse_ram_table, decode_any, TABLE_A, TABLE_B  # noqa: E402

ASSETS = ROOT / "reconstruction" / "gfx" / "assets"
CORPUS = Path("/tmp/s8/decomp.bin")
ROM_SHA256 = "dd44f120446654bb91c448762f3e0cd0d9b034f35d0e3266a4dc34402ada95c0"


class GraphicsTableTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rom = load_rom()
        cls.table_a = parse_table(cls.rom, TABLE_A)
        cls.table_b = parse_ram_table(cls.rom, TABLE_B)

    def test_table_shapes(self):
        self.assertEqual(len(self.table_a), 56, "table $00A666 changed size")
        self.assertEqual(len(self.table_b), 14, "table $00B768 changed size")

    def test_every_record_decodes(self):
        """No record of $00A666 may fail to decode."""
        failures = []
        for e in self.table_a:
            try:
                data, fmt, _ = decode_any(self.rom, e["src"])
            except Exception as exc:                             # noqa: BLE001
                failures.append((hex(e["src"]), str(exc)))
                continue
            self.assertEqual(len(data) % 32, 0,
                             f"${e['src']:06X} ({fmt}) is not a whole number of tiles")
            self.assertIn(fmt, ("bitstream-8192", "kosinski-85A2"))
        self.assertEqual(failures, [], f"records failed to decode: {failures}")

    def test_kosinski_records_fit_vram(self):
        """The 13 Kosinski records must land inside a 64 KB VRAM."""
        n = 0
        for e in self.table_a:
            try:
                _, fmt, _ = decode_any(self.rom, e["src"])
            except Exception:                                    # noqa: BLE001
                continue
            if fmt != "kosinski-85A2":
                continue
            n += 1
            data, _, _ = decode_any(self.rom, e["src"])
            self.assertLessEqual(e["field2"] + len(data), 0x10000,
                                 f"${e['src']:06X} overruns VRAM from ${e['field2']:04X}")
        self.assertEqual(n, 13, "expected 13 Kosinski records in $00A666")

    def test_asset_files_match_decoder(self):
        """Committed .bin files must be what the decoder produces now."""
        missing = [e for e in self.table_a
                   if not (ASSETS / f"{e['index']:02d}_{e['src']:06X}.bin").exists()]
        self.assertEqual(missing, [], "run: python3 tools/gfx_assets.py")
        for e in self.table_a[:8]:                      # sample; full run is gfx_assets.py
            data, _, _ = decode_any(self.rom, e["src"])
            on_disk = (ASSETS / f"{e['index']:02d}_{e['src']:06X}.bin").read_bytes()
            self.assertEqual(data, on_disk, f"stale asset for ${e['src']:06X}")

    def test_index_json_is_consistent(self):
        idx = json.loads((ASSETS / "index.json").read_text())
        self.assertEqual(idx["table_a"]["count"], 56)
        self.assertEqual(len(idx["entries"]), 56)
        self.assertFalse([e for e in idx["entries"] if "error" in e],
                         "index.json still records failures")

    @unittest.skipUnless(CORPUS.exists(), f"no capture at {CORPUS}")
    def test_decoder_still_byte_exact(self):
        """Decoder output vs the ROM's own output, from a live capture."""
        from tools.decomp_corpus import read_corpus
        from tools.sor_gfx_format import decode
        recs = read_corpus(str(CORPUS))
        self.assertGreaterEqual(len(recs), 10)
        for r in recs:
            data, _ = decode(self.rom, r["src"])
            self.assertEqual(data, r["data"],
                             f"decoder diverges from ROM output at ${r['src']:06X}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
