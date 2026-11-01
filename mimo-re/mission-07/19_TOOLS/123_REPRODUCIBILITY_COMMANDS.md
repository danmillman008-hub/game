# Mission 7 — Reproducibility Commands

```bash
# 0. environment
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install androguard==4.1.4 pytest==9.2.0
APK="/tmp/apk/Mimo_9.35 (1).apk"
sha256sum "$APK"   # 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a

# 1. resources (manual ARSC path — the Mission 6 blocker)
cd mimo-re/mission-07
/tmp/venv/bin/python tools/parse_arsc.py --arsc /tmp/res/resources.arsc --out /tmp/arsc_full.json
/tmp/venv/bin/python tools/parse_arsc.py --arsc /tmp/res/resources.arsc --types color,dimen \
    --out evidence/DESIGN_TOKENS_VALUES.json

# 2. class/method universe
/tmp/venv/bin/python tools/build_m7_inventory.py --dex-dir /tmp/x --src /tmp/dad --out-dir 01_CLASS_UNIVERSE

# 3. analytics corpus
grep -rhoE 'new ge\.j\("[a-z0-9_]+"' /tmp/dad | sed 's/.*("//' | sort -u   # 14 events

# 4. DI catalogue
/tmp/venv/bin/python -c "import json,csv;d=json.load(open('../mission-06/evidence/DI_GRAPH.json'));\
print(d['cases'], sum(1 for p in d['providers'] if p['provides']))"

# 5. validation
/tmp/venv/bin/python -m pytest 20_TESTS -q                          # mission 7
/tmp/venv/bin/python -m pytest ../mission-06/19_TESTS -q            # 21
/tmp/venv/bin/python -m pytest ../mission-05/21_AUTOMATED_VALIDATION -q  # 44
/tmp/venv/bin/python -m pytest ../complete-extraction -q            # 23
```
