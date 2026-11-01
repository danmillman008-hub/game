#!/usr/bin/env python3
"""Stage 9 — derive a screen/modal/fragment inventory from classes + resources.

    python tools/screen_inventory.py EXTRACTED_ASSETS_DIR EVIDENCE_DIR

Reads evidence/components.json (activities/services) and the DEX class list, then
groups UI surfaces: activities, fragments, Modals (ModalData$*), bottom sheets,
dialogs, Compose screens, plus resource string prefixes that name screens.
"""
from __future__ import annotations

import collections
import glob
import json
import os
import re

RES_PREFIXES = ("onboarding", "chapter_end", "lesson", "practice", "streak", "leaderboard",
                "certificate", "upgrade", "paywall", "keys", "reward", "store", "profile",
                "settings", "report_lesson", "ai_tutor", "search", "reactivation", "trial",
                "discount", "widget", "share", "learning_companions", "fast_mode", "hard_mode",
                "see_solution", "interaction_hint", "executable_lesson", "sparks", "league")


def main(assets_dir: str, evidence_dir: str) -> None:
    classes = sorted({l.strip().lstrip("L").rstrip(";").replace("/", ".")
                      for l in open(os.path.join(os.path.dirname(evidence_dir), "data",
                                                 "all-classes.txt")) if l.startswith("L")})
    components = json.load(open(os.path.join(evidence_dir, "components.json")))

    def names(pred):
        return [c for c in classes if pred(c)]

    app = [c for c in classes if c.startswith("com.getmimo.")]
    inv = {
        "activities": [a["name"] for a in components["activities"]],
        "app_activities": [a["name"] for a in components["activities"]
                           if (a["name"] or "").startswith("com.getmimo.")],
        "exported": [a["name"] for a in components["activities"]
                     if str(a.get("exported")).lower() == "true"],
        "fragments": names(lambda c: c.startswith("com.getmimo.") and c.endswith("Fragment")),
        "viewmodels": names(lambda c: c.startswith("com.getmimo.") and c.endswith("ViewModel")),
        "modals": sorted({c.split("$")[1] for c in app
                          if "ui.introduction.ModalData$" in c and "$" in c}),
        "bottom_sheets": names(lambda c: "BottomSheet" in c and c.startswith("com.getmimo.")),
        "dialogs": names(lambda c: c.startswith("com.getmimo.") and "Dialog" in c),
        "compose_screens": names(lambda c: c.startswith("com.getmimo.") and
                                 re.search(r"(Screen|Composable|ScreenKt)$", c) is not None),
        "widgets": names(lambda c: c.startswith("com.getmimo.ui.widget")),
        "nav_classes": names(lambda c: c.startswith("com.getmimo.ui.navigation")),
    }

    # resource string families => screen vocabulary
    xml = open(os.path.join(evidence_dir, "resources-strings.xml"), encoding="utf-8").read()
    keys = re.findall(r'<string name="([^"]+)"', xml)
    fam = collections.Counter()
    for k in keys:
        head = k.split("_")[0]
        if head in RES_PREFIXES:
            fam[head] += 1
    inv["string_families"] = dict(fam.most_common())

    # layouts / navigation resources shipped in the APK
    nav = []
    for p in glob.glob("/tmp/x/meta/res/navigation/*"):
        nav.append(os.path.basename(p))
    inv["navigation_resource_files"] = nav
    layouts = sorted(os.path.basename(p) for p in glob.glob("/tmp/x/meta/res/layout/*")) if os.path.isdir("/tmp/x/meta/res/layout") else []
    inv["layout_files_count"] = len(layouts)
    inv["layout_files_sample"] = layouts[:40]

    json.dump(inv, open(os.path.join(evidence_dir, "screens.json"), "w"), indent=1, ensure_ascii=False)
    print({k: (len(v) if isinstance(v, (list, dict)) else v) for k, v in inv.items()})


if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])
