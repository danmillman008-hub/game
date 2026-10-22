#!/usr/bin/env python3
"""Stage-2 verification entry point.

Runs the whole Stage-2 test suite (specification tests, ROM-confirmed behaviour
tests and differential tests against the original M68000 code), then writes a
machine-readable evidence bundle to evidence/stage2/stage2_verification.json.

Requires: unicorn (for the differential tests). Without it, those tests are
skipped and the bundle records that fact instead of claiming a pass.

    python3 tools/verify_stage2.py
"""
from __future__ import annotations

import collections
import hashlib
import json
import sys
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))

OUT = ROOT / "evidence" / "stage2" / "stage2_verification.json"
MODULES = ["tests.test_component_spec", "tests.test_recovered_behaviour", "tests.test_differential_rom"]


class RecordingResult(unittest.TextTestResult):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.records = []
        self.skips = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.records.append({"test": test.id(), "status": "PASS"})

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.records.append({"test": test.id(), "status": "FAIL", "detail": self._fmt(err)})

    def addError(self, test, err):
        super().addError(test, err)
        self.records.append({"test": test.id(), "status": "ERROR", "detail": self._fmt(err)})

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self.records.append({"test": test.id(), "status": "SKIP", "detail": reason})
        self.skips.append(reason)

    @staticmethod
    def _fmt(err):
        import traceback
        return "".join(traceback.format_exception(*err))[-2000:]


def main() -> int:
    loader = unittest.TestLoader()
    suite = unittest.TestSuite(loader.loadTestsFromName(m) for m in MODULES)
    runner = unittest.TextTestRunner(verbosity=2, resultclass=RecordingResult, stream=sys.stdout)
    result = runner.run(suite)

    import tests.test_differential_rom as diff
    from components.sor_engine import BoxTables
    import rom_oracle

    oracle = None
    jump = {}
    cheat = {}
    if not result.skips:
        oracle = rom_oracle.Oracle()
        for v, kind in ((-0x78000, "neutral"), (-0x78000, "directional"),
                        (-0x88000, "neutral"), (-0x88000, "directional"),
                        (-0x98000, "neutral"), (-0x98000, "directional")):
            ys, _ = oracle.jump_profile(v, kind)
            air = 0
            for y in ys:
                if y < 0:
                    air += 1
                elif air:
                    break
            jump[f"{v/65536:+.1f}/{kind}"] = {"airtime_ticks": air, "apex_px": min(ys) / 65536}
        for name, code in (("MOM", b"\x00\x0d\x0f\x0d"), ("SUN", b"\x00\x13\x15\x0e"),
                           ("UDI", b"\x00\x15\x04\x09"), ("BO ", b"\x00\x02\x0f\x00"),
                           ("ORE", b"\x00\x0f\x12\x05"), ("   ", b"\x00\x00\x00\x00"),
                           ("AXL", b"\x00\x01\x18\x0c")):
            stock, lives = oracle.cheat(code)
            cheat[name] = {"ff35": stock, "lives_bcd": lives}

    with zipfile.ZipFile(ROOT / "Streets-of-Rage_Genesis_EN.zip") as zf:
        rom = zf.read("Streets of Rage (JUE) (REV 00) [!].bin")
    t = BoxTables.load()
    doc = {
        "stage": 2,
        "rom": {
            "file": "Streets of Rage (JUE) (REV 00) [!].bin",
            "sha256": hashlib.sha256(rom).hexdigest(),
            "size": len(rom),
        },
        "components_under_test": ["sor_engine.kinematics", "sor_engine.boxes",
                                  "sor_engine.projection", "sor_engine.fixed"],
        "tables": {
            "z_pairs": len(t.z_pairs), "box_records": len(t.records),
            "z_pairs_sha256": hashlib.sha256(json.dumps(t.z_pairs).encode()).hexdigest(),
            "box_records_sha256": hashlib.sha256(json.dumps(t.records).encode()).hexdigest(),
        },
        "tests": {
            "total": result.testsRun,
            "passed": sum(1 for r in result.records if r["status"] == "PASS"),
            "failed": sum(1 for r in result.records if r["status"] == "FAIL"),
            "errors": sum(1 for r in result.records if r["status"] == "ERROR"),
            "skipped": sum(1 for r in result.records if r["status"] == "SKIP"),
            "records": result.records,
        },
        "differential_comparisons": dict(diff.COMPARISONS),
        "differential_total": sum(diff.COMPARISONS.values()),
        "measured_jump_profiles": jump,
        "measured_cheat_table": cheat,
        "reproduce": "python3 tools/verify_stage2.py",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8")
    print(f"\nStage-2 evidence -> {OUT}")
    print(f"tests: {doc['tests']['passed']} passed, {doc['tests']['failed']} failed, "
          f"{doc['tests']['errors']} errors, {doc['tests']['skipped']} skipped")
    print(f"differential comparisons vs original ROM code: {doc['differential_total']}")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
