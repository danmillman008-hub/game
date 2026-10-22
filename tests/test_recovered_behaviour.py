"""Re-verification of two earlier findings that the Stage-1 tool claimed but did
not implement (EXP-04 name-entry cheat, EXP-05 jump trajectories).

These tests execute the original ROM routines. They exist because the Stage-1
README/coverage matrix described five dynamic experiments while the committed
verification tool only implemented three.

Run: python3 -m unittest tests.test_recovered_behaviour -v
"""
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))

from components.sor_engine import (  # noqa: E402
    Actor, clamp_terminal_velocity, directional_gravity, integrate, neutral_gravity,
)

HAS_UNICORN = importlib.util.find_spec("unicorn") is not None

try:
    from rom_oracle import Oracle
    _ERR = None
except Exception as exc:  # pragma: no cover
    Oracle = None
    _ERR = exc

# Codes are 4 bytes: leading 0, then 1-based A=1..Z=26 (measured, not assumed).
CODES = {
    "MOM": (b"\x00\x0d\x0f\x0d", 5, 0x90),
    "SUN": (b"\x00\x13\x15\x0e", 4, 0x49),
    "UDI": (b"\x00\x15\x04\x09", 3, 0x09),
    "BO ": (b"\x00\x02\x0f\x00", 2, 0x07),
    "ORE": (b"\x00\x0f\x12\x05", 1, 0x01),
    "   ": (b"\x00\x00\x00\x00", 0, 0x00),
}

# Measured with the ROM (see DIFFERENTIAL_VALIDATION.md D9). The Stage-1 dossier
# listed 18/20/22 and 20/23/25 ticks with a 34.875/44.219/54.656 px apex; those
# numbers assume position was integrated before gravity and do not match the ROM.
# Airtime measured by executing the ROM's gravity+clamp+integrate chain per frame.
# The Stage-1 dossier listed 18/20/22 and 20/23/25 ticks with a 34.875/44.219/
# 54.656 px apex; those assume position is integrated *before* gravity and do not
# match the ROM, which applies gravity in the state handler first ($001FDC).
JUMP_TABLE = {
    (-0x78000, "neutral"): 15,
    (-0x78000, "directional"): 17,
    (-0x88000, "neutral"): 17,
    (-0x88000, "directional"): 20,
    (-0x98000, "neutral"): 19,
    (-0x98000, "directional"): 22,
}


@unittest.skipUnless(HAS_UNICORN and Oracle is not None, "unicorn not installed: ROM oracle unavailable")
class RecoveredBehaviour(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = Oracle()

    def test_cheat_table(self):
        for name, (code, stock, lives) in CODES.items():
            got = self.o.cheat(code)
            self.assertEqual(got, (stock, lives), f"code {name!r}")

    def test_cheat_rejects_unknown_code(self):
        # 'AXL' is not in the table: the sentinels must survive untouched.
        self.assertEqual(self.o.cheat(b"\x00\x01\x18\x0c"), (0xEE, 0xEE))

    def test_cheat_p2_uses_different_globals(self):
        self.assertEqual(self.o.cheat(CODES["MOM"][0], player1=False), (5, 0x90))

    def test_jump_airtime_and_apex(self):
        for (vy0, kind), air in JUMP_TABLE.items():
            ys, _ = self.o.jump_profile(vy0, kind)
            measured = 0
            for y in ys:
                if y < 0:
                    measured += 1
                elif measured:
                    break
            self.assertEqual(measured, air, f"airtime v0={vy0/65536} {kind}")
            a = Actor(vy=vy0)
            g = neutral_gravity if kind == "neutral" else directional_gravity
            comp = []
            for _ in range(60):
                g(a)
                clamp_terminal_velocity(a)
                integrate(a)
                comp.append(a.y)
            self.assertEqual(min(comp), min(ys), f"apex v0={vy0/65536} {kind}")

    def test_component_matches_rom_for_sixty_frames(self):
        for vy0 in (-0x78000, -0x88000, -0x98000):
            for kind in ("neutral", "directional"):
                ys, vys = self.o.jump_profile(vy0, kind)
                a = Actor(vy=vy0)
                g = neutral_gravity if kind == "neutral" else directional_gravity
                for i in range(60):
                    g(a)
                    clamp_terminal_velocity(a)
                    integrate(a)
                    self.assertEqual(a.y, ys[i], f"y v0={vy0/65536} {kind} frame {i}")
                    self.assertEqual(a.vy, vys[i], f"vy v0={vy0/65536} {kind} frame {i}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
