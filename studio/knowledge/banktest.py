#!/usr/bin/env python3
"""Offline tests for the bank. No network: `live()` is monkeypatched.

Proves the two things that matter:
  * the validator actually rejects broken entries (a bank that accepts anything is a lie)
  * drift detection catches a star change, a licence change, a deleted repo, and that
    --update only writes when asked

    python3 studio/knowledge/banktest.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import bank as B  # noqa: E402

fails = 0


def check(label: str, cond: bool, detail: str = "") -> None:
    global fails
    print(f"  [{'ok  ' if cond else 'FAIL'}] {label}{(' — ' + detail) if detail else ''}")
    fails += 0 if cond else 1


def entry(**kw) -> dict:
    e = {"repo": "a/b", "url": "https://github.com/a/b", "gap": "lipsync",
         "verdict": "take", "note": "n", "stars": 1, "license": "MIT",
         "pushed_at": "2026-01-01", "archived": False}
    e.update(kw)
    return e


def t_real_bank() -> None:
    print("the real bank")
    data = B.load()
    problems = B.check(data)
    check("bank validates", not problems, "; ".join(problems[:3]))
    check("has entries", len(data["repos"]) >= 30, str(len(data["repos"])))
    check("every entry has live numbers", all(
        e.get("stars") is not None or e.get("missing") for e in data["repos"]))
    check("no duplicate repos",
          len({e["repo"] for e in data["repos"]}) == len(data["repos"]))
    check("verdicts are the three known ones",
          {e["verdict"] for e in data["repos"]} <= set(B.VERDICTS))


def t_validator() -> None:
    print("validator rejects")
    base = {"repos": [entry()]}
    check("good entry passes", B.check(base) == [])
    check("missing note", B.check({"repos": [entry(note="")]}) != [])
    check("duplicate", B.check({"repos": [entry(), entry()]}) != [])
    check("unknown gap", B.check({"repos": [entry(gap="nope")]}) != [])
    check("unknown verdict", B.check({"repos": [entry(verdict="maybe")]}) != [])
    check("url/repo mismatch", B.check({"repos": [entry(url="https://github.com/x/y")]}) != [])
    check("missing url", B.check({"repos": [entry(url="")]}) != [])


def t_export() -> None:
    print("export")
    data = {"verified_on": "2026-10-30", "repos": [
        entry(repo="a/beta", stars=10, verdict="take", note="first"),
        entry(repo="a/alpha", stars=99, verdict="avoid", note="second"),
    ]}
    md = B.export_md(data)
    check("every repo appears", "a/beta" in md and "a/alpha" in md)
    check("sorted by stars", md.index("a/alpha") < md.index("a/beta"))
    check("verdict rendered", "نگیر" in md and "بگیر" in md)
    check("date stamped", "2026-10-30" in md)


def t_stats() -> None:
    print("stats")
    data = {"repos": [entry(repo="a/1", verdict="take"), entry(repo="a/2", verdict="avoid"),
                      entry(repo="a/3", verdict="study", gap="g-sound")]}
    s = B.stats(data)
    import re
    check("counts takes", bool(re.search(r"take\s+1\b", s)), s.splitlines()[2])
    check("counts avoids", bool(re.search(r"avoid\s+1\b", s)), s.splitlines()[4])
    check("lists gaps", "g-sound" in s)


def t_verify() -> None:
    print("drift detection (mocked API)")
    data = {"repos": [entry(repo="a/same"), entry(repo="a/changed"),
                      entry(repo="a/gone"), entry(repo="a/lic")]}
    reply = {
        "a/same": {"stars": 1, "license": "MIT", "pushed_at": "2026-01-01", "archived": False},
        "a/changed": {"stars": 500, "license": "MIT", "pushed_at": "2026-01-01", "archived": False},
        "a/lic": {"stars": 1, "license": "GPL-3.0", "pushed_at": "2026-01-01", "archived": False},
    }

    def fake_live(repo, token=None):
        if repo not in reply:
            import urllib.error
            raise urllib.error.HTTPError(repo, 404, "gone", None, None)
        return reply[repo]

    B.live, B.time.sleep = fake_live, lambda s: None
    drift = B.verify(data, update=False)
    check("no drift for unchanged", not any("a/same" in d for d in drift))
    check("star drift found", any("a/changed: stars 1 -> 500" in d for d in drift))
    check("licence drift found", any("a/lic" in d and "GPL-3.0" in d for d in drift))
    check("404 reported as gone", any("a/gone: GONE" in d for d in drift))
    check("update=False writes nothing",
          data["repos"][1]["stars"] == 1)

    B.save = lambda d, path=None: None          # never touch the real file in a test
    data2 = json.loads(json.dumps({**data, "repos": [entry(repo="a/changed")]}))
    B.verify(data2, update=True)
    check("update=True applies the new number", data2["repos"][0]["stars"] == 500)
    check("update=True stamps verified_on", bool(data2.get("verified_on")))


def main() -> int:
    print("bank tests\n")
    for fn in (t_real_bank, t_validator, t_export, t_stats, t_verify):
        fn()
        print()
    print("FAILED" if fails else "ALL OK")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
