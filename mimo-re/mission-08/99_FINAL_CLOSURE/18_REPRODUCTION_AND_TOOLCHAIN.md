# 18 — Reproduction and toolchain

## 1. Environment actually used

| Component | Version | Role |
|---|---|---|
| Python | 3.11 (`/tmp/venv`) | all validation and generation |
| pytest | 9.2.0 | semantic suites |
| androguard + DAD (missions 4–7) | as recorded in `mission-06/00_BASELINE/TOOLS_AND_ENVIRONMENT.json` | produced the committed evidence |
| jadx / apktool / dot / mmdc / adb | **unavailable** at every stage | noted in each mission |
| Runtime | none | no device, no emulator |

## 2. Reproduce the static validation of this package

```bash
cd /home/user/game
python3 -m venv /tmp/venv && /tmp/venv/bin/pip -q install pytest

# every suite, actual counts
for t in mimo-re/mission-05/21_AUTOMATED_VALIDATION \
         mimo-re/mission-06/19_TESTS \
         mimo-re/mission-07/20_TESTS \
         mimo-re/mission-08/04_INTERACTION_ENGINE/tests \
         mimo-re/mission-08/05_LEARNER_MODEL/tests \
         mimo-re/mission-08/06_PERSISTENCE/tests \
         mimo-re/mission-08/07_NETWORKING/tests \
         mimo-re/mission-08/99_FINAL_CLOSURE/tests ; do
  printf '%-58s ' "$(basename $(dirname $t))"; /tmp/venv/bin/python -m pytest -q "$t" | tail -1
done
```

## 3. Reproduce the consolidations (deterministic, no network)

| Deliverable | Source | Method |
|---|---|---|
| `14_ALL_OPEN_QUESTIONS_CLOSURE.json` | 39 canonical + 28 A + 10 Stage-7 A + 13 B + Q-76 | each entry quotes the register text and carries a terminal status |
| `15_FINAL_COVERAGE_MATRIX.csv` | 45-domain register + Stages 2–7 | one row per domain (`tests::test_coverage_covers_all_45_domains`) |
| `16_CONSOLIDATED_EVIDENCE_REGISTER.json` | Stage 7 records + content/lesson/learner/persistence/auth records | every `artifact_ref` resolved by test |
| `03_CLASS_DISPOSITION.csv` | `mission-08/16_FINAL_AUDIT/03_MISSION08_METRICS.json` | counts carried, not recomputed (artifact absent) |
| `08_OFFLINE_CAPABILITY_MATRIX.csv` | Stages 2–7 | 18 feature rows |

## 4. Reproduce an extraction from scratch (requires the artifact)

```bash
# 1. verify the artifact before using it
sha256sum Mimo_9.35.apk   # must equal 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
# 2. tools shipped with this project
python3 mimo-re/tools/dex_inspect.py --help
python3 mimo-re/tools/build_symbol_recovery.py --help
python3 mimo-re/tools/build_call_graph.py --help
# 3. the DEX-level checks that remain blocked are enumerated in 17 §2
```

## 5. Determinism

Every generator used in this mission is a pure function of committed evidence; no network call, no clock dependency, no
random sampling. Re-running §2 on a clean checkout reproduces the same numbers reported in `00`.
