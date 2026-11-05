# MIMO 9.35 — MISSION 09 REPRODUCTION GUIDE

**Document:** `MISSION_09_REPRODUCTION_GUIDE.md` · **Mission:** MISSION 09 (final reconstruction) · **Branch:** `arena/aebb90b7-game`
**Target APK:** `com.getmimo` 9.35, `versionCode=1792759685`, 142,353,499 B, SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` — unchanged.
**SERVER CONFIRMED = 0.** Classification vocabulary: `VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_ASSET`, `VERIFIED_DATABASE`, `VERIFIED_NETWORK_OBSERVATION`, `INFERRED`, `UNKNOWN`, `SERVER_DEPENDENT`.
Evidence codes resolve in `COMPLETE_EVIDENCE_DATABASE.json` / `COMPLETE_SYSTEM_MAP.json -> evidence_index`.

---


## 1. Prerequisites

* Original APK `MIMO_ORIGINAL.apk`, 142,353,499 B,
  SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` — **never modified**.
* GitHub Actions runner with the pinned Android 16 / API 36 emulator
  (`sdk_gphone64_x86_64`), KVM, `adb root`, Frida 17.25.2, Python 3.11, Node.
* Branch `arena/aebb90b7-game`. Runtime facts can ONLY be produced on the runner; the
  local sandbox has no emulator/ADB/SDK/KVM.

## 2. Reproducing the static deliverables locally (no emulator required)

```bash
cd /home/user/game
git checkout arena/aebb90b7-game

# 2a. Extract the shipped curriculum assets READ-ONLY from the original APK.
#     Nothing is written back into the APK.
unzip -q MIMO_ORIGINAL.apk 'assets/lessons-*/tracks/*' -d /home/user/_work/_analysis/mimo_assets/
#     Result: /home/user/_work/_analysis/mimo_assets/assets/lessons-<locale>/tracks/
#     10 locales, 10,298 tutorial-*.json + 10 tracks.json.

# 2b. Build the normalized curriculum graph + integrity audit.
M09_ASSET_ROOT=/home/user/_work/_analysis/mimo_assets/assets \
  python3 ANALYSIS/RUNTIME/MISSION_09/m09_curriculum.py
#     -> ANALYSIS/MISSION_09/COMPLETE_CURRICULUM_GRAPH.json

# 2c. Build all other deliverables from the workspace evidence.
python3 ANALYSIS/RUNTIME/MISSION_09/m09_build.py
#     Reads M05/M06/M07/M08 reports, DEX catalogs, endpoint JSON, M08 raw timelines,
#     and ANALYSIS/RUNTIME/MISSION_09/TIMELINE/M09_RUNTIME_TIMELINE.jsonl.
```

If the asset tree is unavailable, `m09_curriculum.py` writes a **DEGRADED** graph that
explicitly says so rather than inventing nodes. If M09 raw runtime evidence is absent,
`m09_build.py` marks M09 experiments `PENDING` rather than fabricating results.

## 3. Reproducing the controlled runtime run

1. `ANALYSIS/RUNTIME/_DISPATCH_TRIGGER` must contain **both**
   `M07-RUNTIME-RUN-009` (so workflow step 100 selects `transfer_apk_m07.sh`)
   and `M09-UNIFIED-RUN-001`. Do not change the workflow YAML or the APK.
2. `ANALYSIS/RUNTIME/runtime_smoke.sh` dispatches on `M09-UNIFIED-RUN` **before** the
   M08/M07/M05 guards; it `exec`s `ANALYSIS/RUNTIME/MISSION_09/m09_runtime.sh`.
3. `m09_runtime.sh` sets `PHASE=9`, verifies `sha_gate=SHA_MATCH_OK`, starts Frida 17.25.2
   from the GitHub release asset (authenticated API fallback), installs the Java bridge,
   attaches by PID via a host-side long-lived `adb shell`, and runs
   `python3 ANALYSIS/RUNTIME/MISSION_09/m09_unified.py --phase 9 --duration 720`.
4. `m09_agent.js` avoids the API-36 `Java.registerClass` failure: it hooks
   `android.app.Activity` lifecycle methods, `androidx.fragment.app.Fragment`, WebView
   load/evaluate/override methods, plus 63 curated `com.getmimo` methods.
5. `m09_unified.py` runs EXP-M09-001..005: measured 20-tap onboarding chain, explicit
   MainActivity fallback, four-tab route tour, lesson-entry matrix, offline
   cold-start queue observation, and instrumentation proof.
6. One controlled emulator owner; no parallel experiments; no state restore.

Mission 09 run ID: **`42077425594`** (SUCCESS). M08 runs: `42042312640`, `42046336206`,
`42049141553`, `42050715150`.

## 4. What the M09 run actually produced (read this before repeating anything)

| Result | Value |
|---|---|
| `sha_gate` | `SHA_MATCH_OK bytes=142353499` |
| Frida preflight | `attach_ok=true, pid=3348, name="Mimo"` |
| Instrumentation proof | `server_active=true, attach_ok=true, 181 hooks, 28 nav, 72 entry, 0 webview, real_target_method_executed=true` |
| Timeline | 691 events in `ANALYSIS/RUNTIME/MISSION_09/TIMELINE/M09_RUNTIME_TIMELINE.jsonl` |
| Onboarding chain | `reached=false` (stalled at step 4 of 20 on this build's question set) |
| MainActivity | `reached=true` via **explicit intent** fallback, not natural onboarding |
| Route tour | Learn -> MainActivity (`Full-Stack Developer`, `1. Intro to Web Development`); Practice/Leaderboard/Profile resumed an incomplete `OnboardingActivity` back stack -> screen contents UNKNOWN |
| Lesson matrix | `lesson_matrix_not_executed` (ChapterActivity not reached) -> recorded as UNKNOWN, no answers guessed |
| Offline | `Active default network: none` -> cold start `IntroSlidesActivity` -> reconnect `102` |
| Queue | `before={}, after={}` (no queued rows existed); **startup SQL captured `DELETE FROM lesson_progress WHERE in_queue = 1`** |
| Server | `server_confirmed=0`; 17 `net` events, all third-party or bundled `jar:file:` resources |

**Do NOT repeat** the fixed 20-tap chain, natural-state restore, reflection-based
`hookClass()`, API-36 `Java.registerClass`, or the silent Frida download chain — all are
documented dead ends in `FINAL_UNKNOWN_REGISTER.md` and `COMPLETE_EVIDENCE_DATABASE.json`.

## 5. Redaction

Raw third-party tokens (`access_token`, `auth_token`, `api_key`, RevenueCat
`/v1/subscribers/<id>`) captured by the URL hook are scrubbed in the M09 raw timeline,
M09 traces and all 19 deliverables by the `redact()` function in `m09_build.py`.
No credential value appears in any deliverable. Original M05/M06/M07/M08 evidence files
are left untouched.

## 6. Validation commands

```bash
# JSON
python3 - <<'PY'
import json,glob
for p in glob.glob('ANALYSIS/MISSION_09/*.json'):
    json.load(open(p)); print('OK',p)
# JSONL
for p in glob.glob('ANALYSIS/MISSION_09/*.jsonl'):
    for i,l in enumerate(open(p),1):
        if l.strip(): json.loads(l)
    print('OK',p)
PY
# secret scan (must be empty)
grep -rE 'access_token=<redacted> ANALYSIS/MISSION_09/ || echo CLEAN
# APK integrity
sha256sum MIMO_ORIGINAL.apk
git status --short
```
