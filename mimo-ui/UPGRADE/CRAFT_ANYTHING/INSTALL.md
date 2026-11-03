# نصب لایهٔ عاملی craft-anything

- منبع: `https://github.com/storytold/craft-anything.git` (v0.3.0)، کلون در `/home/user/_work/craft-anything`.
- وندورشده در `upstream_docs/`: `README.md`, `AGENTS.md`, `CLAUDE.md`, `ATTRIBUTION.md`, `NOTICE`, `LICENSE-MIT`, `LICENSE-APACHE`, `docs/tools.md`, `docs/pitfalls.md`, `docs/extending.md`, `docs/STATUS.md`, `docs/ROADMAP.md`, `docs/schemas/*.json`.
- آداپتور قابلاجرا: `craft_adapter.py` (۳۳ شناسه ابزار، قرارداد شواهد، deep mode، بدون وابستگی خارجی).
- workspace: `workspace/craft.json`, `investigation.cany.json`, `plan.json`, `unknowns.json`, `brief.md`.
- خروجی: `../CATALOGS/EVIDENCE_LEDGER.json` (۱۳ رکورد: ۳ target + ۱۰ finding).
- محدودیت: باینری native بهدلیل محدودیت egress و نبود Rust نصب نشد؛ جزئیات در `../01_CRAFT_ANYTHING_INSTALL.md`.

اجرا:
```
python3 craft_adapter.py doctor
python3 craft_adapter.py core-evidence-show
python3 craft_adapter.py core-plan-update --phase P0 --status DONE
```
