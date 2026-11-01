# 01 — Target and repository baseline

## 1. Target artifact

| Property | Value | Source |
|---|---|---|
| Package | Mimo learning app, version 9.35 | `APK_MANIFEST` |
| SHA-256 | `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` | `mission-06/00_BASELINE/APK_MANIFEST.json` |
| DEX files | 13 (8 tiny stubs + 5 real; `classes.dex` 16.2 MB) | `DEX_HASHES.json` |
| `classes.dex` | `2f2c0c618f89c6d6cadf7acf93f48eb9572c66f6b68d7dba03a36c0487f6a115` | same |
| `classes2.dex` | `1e0e36c027fd5900c25e32f6b20465d0cb5573176de1a51689a261736a395f80` | same |
| Present in this environment | **no** | see §4 |

Artifact identity is used only as a join key for evidence. Signature/repackaging questions are out of scope by the
user's standing instruction and are not investigated here.

## 2. Repository baseline

| Item | Value |
|---|---|
| Branch | `arena/ecb8af07-game` (fixed for this session) |
| Remote | `https://github.com/danmillman008-hub/game.git` |
| Remote HEAD at mission start | `eeecd4aa9825` (= Stage 7) |
| Checkpoints | Stage 1 `752add7` · 2 `fc11272` · 3 `7e75056` · 4 `df259d7` · 5 `a3e7d1b` · 6 `8049767` · 7 `eeecd4a` |
| Mission base | `8ea70cca549c95a7c32faec909f9f5d4d871ad6c` |

## 3. Repository recovery performed at the start of this mission

The sandbox had been rebuilt again: `.git` matched the base commit while the working tree contained the whole
`mimo-re/` tree as untracked content. Recovery was non-destructive and verified before any change:

```text
git fetch origin arena/ecb8af07-game          → FETCH_HEAD = eeecd4a
git add -A ; git diff --cached --stat FETCH_HEAD
    → empty output  ⇒ staged tree is byte-identical to the remote tree
git reset --mixed FETCH_HEAD                  → HEAD = eeecd4a, index = tree, working tree untouched
git status --porcelain                        → empty
```

No reset `--hard`, no force push, no history rewrite, no file deletion. `git rev-parse HEAD` and
`git ls-remote origin arena/ecb8af07-game` both report `eeecd4a` before this mission's work began.

## 4. Artifact availability (the declared limitation)

| Question | Answer |
|---|---|
| APK in workspace? | no (`find /` over the workspace finds only an unrelated `ttac-4.3.6.apk` from the repository root) |
| DEX in workspace? | no |
| Decompiled `/tmp/dad`? | no (ephemeral) |
| Reachable hosts | `github.com` 200, `api.github.com` 200, `pypi.org` 200, `registry.npmjs.org` 200 |
| Blocked hosts tested | `apkpure.com` 000, `ghproxy.net` 000, `raw.githubusercontent.com` 000 |
| GitHub releases of this repo | one pre-release (`apk-latest`), asset `ttac-4.3.6.apk` — **not** the Mimo artifact |
| Git LFS | none |

**Consequence:** no new DEX instruction can be read. All mission-99 claims are (a) previously committed
`VERIFIED_STATIC` evidence, or (b) new cross-artifact reconciliation of that evidence. Eight questions are
`BLOCKED_BY_ENVIRONMENT` for exactly this reason and no other.

## 5. Analysis environment used in this mission

| Item | Version / value |
|---|---|
| Python | 3.11 (`/tmp/venv`) |
| pytest | 9.2.0 |
| APK/DEX tooling | none available (no artifact) |
| Evidence tooling used earlier | androguard + DAD (missions 4–7), committed outputs |
| Runtime tooling | none (no emulator, no adb, no device) |
