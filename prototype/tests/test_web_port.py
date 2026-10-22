"""The browser build: numerical conformance with the Python reference, and a
headless run of the built HTML file.

These tests need `node` (checked here); everything else in the suite does not.
If node is missing they are reported as skipped, never silently passed.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import unittest
from pathlib import Path

from . import support  # noqa: F401

ROOT = Path(__file__).resolve().parents[2]
WEB = ROOT / "prototype" / "web"
PAGE = ROOT / "prototype" / "release" / "index.html"

NODE = shutil.which("node")
needs_node = unittest.skipIf(NODE is None, "node is not installed")


def run_node(script, *args, timeout=300):
    proc = subprocess.run([NODE, str(WEB / script), *map(str, args)],
                          capture_output=True, text=True, timeout=timeout)
    return proc


@needs_node
class TestConformance(unittest.TestCase):
    """The JS port must compute exactly what the Python game computes."""

    @classmethod
    def setUpClass(cls):
        from prototype.tools import web_conformance
        cls.mod = web_conformance

    def test_recorded_encounter_matches_frame_by_frame(self):
        report = self.mod.compare("recorded", self.mod.recorded_commands())
        self.assertTrue(report["ok"], json.dumps(report.get("first_mismatch"), indent=2)[:3000])
        self.assertEqual(report["frames_py"], 875)
        self.assertEqual(report["final_state"], "victory")
        self.assertEqual(report["kills"], 3)

    def test_passive_run_matches(self):
        report = self.mod.compare("passive", self.mod.passive_commands())
        self.assertTrue(report["ok"], json.dumps(report.get("first_mismatch"), indent=2)[:3000])
        self.assertEqual(report["final_state"], "defeat")
        self.assertEqual(report["frames_py"], 1025)

    def test_synthetic_run_matches(self):
        report = self.mod.compare("synthetic", self.mod.synthetic_commands(800))
        self.assertTrue(report["ok"], json.dumps(report.get("first_mismatch"), indent=2)[:3000])
        self.assertGreater(report["frames_py"], 700)

    def test_rom_table_is_embedded_verbatim(self):
        """The JS build must carry the ROM-derived tables, not a rounded copy."""
        import json as _json
        doc = _json.loads((ROOT / "components" / "data" / "body_boxes.json").read_text())
        proc = run_node("tables.js")
        self.assertEqual(proc.returncode, 0, proc.stderr[-800:])
        got = _json.loads(proc.stdout)
        self.assertEqual(got["z_table"], doc["z_table"]["values"])
        self.assertEqual(got["body_box_table"], doc["body_box_table"]["values"])

    def test_body_box_anchors_in_js(self):
        """Same regression anchors as the Python/C suite."""
        proc = run_node("anchors.js")
        self.assertEqual(proc.returncode, 0, proc.stderr[-800:])
        got = json.loads(proc.stdout)
        self.assertEqual(got["player_100_60"], [97, 111, 52, 68, -42, 0])
        self.assertEqual(got["enemy_200_60"], [197, 207, 52, 68, -50, 0])


@needs_node
class TestRendererSmoke(unittest.TestCase):
    def test_renderer_runs_in_every_state(self):
        proc = run_node("render_smoke.js")
        self.assertEqual(proc.returncode, 0, proc.stdout[-800:] + proc.stderr[-800:])
        report = json.loads(proc.stdout)
        self.assertTrue(report["ok"])
        self.assertGreater(report["results"]["play"]["calls"], 1000)
        self.assertEqual(report["results"]["title"]["size"], [384, 240])


@needs_node
class TestBuiltPage(unittest.TestCase):
    """The shipped HTML must work as a file: no server, no network, no assets."""

    def test_page_is_self_contained(self):
        html = PAGE.read_text(encoding="utf-8")
        self.assertIn('<canvas id="game" width="384" height="240">', html)
        self.assertIn("NeonAlley", html)
        for pattern in (r"<script[^>]+src=", r"<link[^>]+href=", r"https?://",
                        r"\bfetch\(", r"XMLHttpRequest"):
            self.assertIsNone(re.search(pattern, html), f"external reference: {pattern}")

    def test_page_plays_headlessly(self):
        proc = run_node("page_smoke.js")
        self.assertEqual(proc.returncode, 0, proc.stdout[-1500:] + proc.stderr[-1500:])
        report = json.loads(proc.stdout)
        self.assertTrue(report["ok"])
        self.assertEqual(report["boot"]["state"], "title")
        self.assertEqual(report["boot"]["canvas"], [384, 240])
        self.assertEqual(report["start"]["state"], "play")
        self.assertGreater(report["walk"]["moved"], 50)
        self.assertEqual(report["punch"]["attack"], "punch")
        self.assertTrue(report["jump"]["airborne"])
        self.assertIn(report["finished"]["state"], ("victory", "defeat"))
        self.assertEqual(report["restart"]["hp"], 80)
        self.assertGreater(report["drawCalls"], 10000)


if __name__ == "__main__":
    unittest.main()
