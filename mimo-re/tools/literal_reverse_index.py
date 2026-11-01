#!/usr/bin/env python3
"""Stage 6 — literal -> declaring classes reverse index (all DEX classes).

Because Mimo's release build repackages most implementation classes into
single-letter names (R8), class names alone are weak evidence. This tool maps a
curated set of high-value literals (API paths, model/toString templates, feature
keys, DAO SQL) back to the classes that reference them, including obfuscated ones.

Usage:
    python tools/literal_reverse_index.py EXTRACTED_DIR OUT_JSON [extra_literals.txt]
"""
from __future__ import annotations

import collections
import glob
import json
import os
import sys

CURATED = [
    # transport / endpoints
    "runFiles", "runfiles", "/v1/", "/v2/client-config", "/v1/config/", "/v1/user/keys",
    "/v1/user/coins", "/v1/user/rewards", "/v1/leaderboards", "/v1/aiTutor", "/v1/practice",
    "/v1/tracks", "/v1/tutorials", "pusher", "/v1/code", "subscribers", "receipts",
    # data contracts
    "ExecuteFilesResponse", "ExecuteLessonResponse", "ExecuteLessonTestCase", "ChallengeTestCase",
    "RunSuccessful", "hostedProjectUrl", "consoleOutput", "hasPassed", "expectedAnswer",
    "ContentExperiment", "variantTrackId", "originalTrackId", "publishSetVersion",
    "AnswersInChapter", "LessonProgress", "chapter_completions", "lesson_progress",
    "tutorial_completions", "in_queue", "is_practice_progress",
    # lesson DSL / parser
    "interactiveContent", "executableContent", "hardModeContent", "visible-if", "fillTheGap",
    "validatedInput", "startIndex", "endIndex", "solvedContent", "preselectedFileIndex",
    "hasVisualOutput", "sourceDatabaseTables", "solutionDatabaseTables", "bootstrapScript",
    "interaction_hint", "see_solution", "lesson_try_again",
    # AI tutor
    "personal coding tutor", "ai_tutor", "SystemMessage", "FollowupMessage", "FinishReason",
    # gamification
    "Sparks", "sparks", "streak", "Streak", "coins", "Coins", "keysRemaining", "Reward",
    "Leaderboard", "league", "daily_goal", "freeze", "repair",
    # content ops
    "live_preview", "unpublished", "AwesomeMode", "abt", "experiment_variant", "remoteconfig",
    "RemoteConfig", "developermenu", "developer_menu",
    # infra
    "Mixpanel", "mixpanel", "CustomerIo", "customerio", "Adjust", "RevenueCat", "glance",
]


def main(extracted: str, out_json: str, extra: str | None = None) -> None:
    from loguru import logger
    logger.remove()
    from androguard.core.dex import DEX

    literals = list(CURATED)
    if extra and os.path.exists(extra):
        literals += [l.strip() for l in open(extra) if l.strip()]
    index = collections.defaultdict(set)
    dex_files = sorted(glob.glob(os.path.join(extracted, "*.dex")))
    if not dex_files:
        sys.exit(f"no .dex under {extracted}")
    for path in dex_files:
        data = open(path, "rb").read()
        if len(data) < 0x70:
            continue
        dex = DEX(data)
        for cls in dex.get_classes():
            name = cls.get_name()[1:-1].replace("/", ".")
            for m in cls.get_methods():
                code = m.get_code()
                if not code:
                    continue
                for ins in code.get_bc().get_instructions():
                    if not ins.get_name().startswith("const-string"):
                        continue
                    try:
                        s = ins.get_raw_string()
                    except Exception:
                        continue
                    if not s:
                        continue
                    for lit in literals:
                        if lit in s:
                            index[lit].add(name)
    out = {k: sorted(v) for k, v in sorted(index.items())}
    json.dump(out, open(out_json, "w"), indent=1, ensure_ascii=False)
    print(f"literals indexed: {len(out)} / {len(literals)} | "
          f"total (literal,class) pairs: {sum(len(v) for v in out.values())}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
