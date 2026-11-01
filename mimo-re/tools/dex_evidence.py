#!/usr/bin/env python3
"""Stage 5 — per-class DEX evidence for the application package.

Recovers, without a Java decompiler:
  * class -> string-literal map (responsibility evidence)
  * data contracts from Kotlin `toString()` field templates ("Name(field=")
  * feature -> classes index (literal based)
  * method-level literals for parser / lesson-player / executor classes
  * class-level annotation type names (framework identification)

Usage:
    python tools/dex_evidence.py EXTRACTED_DIR OUT_DIR [PACKAGE_PREFIX]

Writes: class-strings.json.gz, data-contracts.json, feature-evidence.json,
        method-literals.json, annotations.json, dex-inventory.json
"""
from __future__ import annotations

import collections
import glob
import gzip
import json
import os
import re
import sys

# feature -> literal patterns (substring match, case-insensitive where noted)
FEATURES = {
    "lesson_player": ["interactiveContent", "lessonBundle", "LessonDescriptionView", "InteractionKeyboard"],
    "interaction_fill_the_gap": ["fillTheGap", "FillTheGap"],
    "interaction_validated_input": ["validatedInput", "ValidatedInput"],
    "interaction_selection": ["selection", "SelectionItem", "correct=\"true\""],
    "interaction_spell": ["Spell"],
    "module_visibility": ["visible-if", "ModuleVisibility"],
    "lesson_completion": ["lesson_passed", "finish_lesson", "LessonProgress", "is_practice_progress"],
    "executable_run": ["runFiles", "ExecuteFilesResponse", "hasPassed", "hostedProjectUrl"],
    "challenge_checks": ["ChallengeTestCase", "requirement=", "ltc_challenges"],
    "code_diff": ["CodeSwitch", "solvedContentForLineHighlight", "IncorrectSolutionException"],
    "code_playground": ["CodePlaygroundExecution", "code/runfiles", "playground"],
    "autosave": ["AutoSaveCodeService", "savefiles", "savedFiles"],
    "ai_tutor": ["aiTutor", "personal coding tutor", "expectedAnswer", "ai_tutor"],
    "practice": ["practice/statistics", "PracticeContent", "practice_tab", "isPractice"],
    "smart_practice": ["SmartPracticeCharged", "SmartPracticeMastered"],
    "hard_mode": ["hardModeContent", "hard_mode", "hardModeSelected"],
    "fast_mode": ["fast_mode", "fastMode"],
    "pacing": ["pacingmechanic", "ShowPacingDialog"],
    "eta": ["TrackEta", "/eta", "SectionEta"],
    "streak": ["streak", "StreakFreeze", "streak_repair", "streak_challenge"],
    "sparks_xp": ["Sparks", "sparksGoal", "rewardedSparksForCorrectAnswer", "daily_goal"],
    "coins": ["/v1/user/coins", "userCoins", "dailyGoalCoinsReward"],
    "rewards": ["/v1/user/rewards", "reward_box", "RewardScreen"],
    "keys": ["/v1/user/keys", "keysRemaining", "keys_left_today"],
    "league": ["LeaderboardLeague", "league_protection", "leaderboard_league_name"],
    "leaderboard": ["/v1/leaderboards", "LeaderboardRank"],
    "certificates": ["/certificates", "CertificateActivity", "ProfessionalCertificate"],
    "onboarding": ["onboarding_", "OnboardingActivity", "onboarding_select_track"],
    "paywall": ["PaywallActivity", "paywall", "revenuecatui"],
    "store_iap": ["/v1/products", "/v2/purchase", "SubscriptionTier", "EntitlementType"],
    "discount": ["RemoteConfigDiscount", "discount_drawer", "last_call_discount"],
    "trial": ["trial_reminder", "free_trial", "trial_started"],
    "content_experiment": ["ContentExperiment", "variantTrackId", "originalTrackId"],
    "ab_testing": ["abt", "ABTestConfig", "experiment_variant"],
    "remote_config": ["remoteconfig", "RemoteConfig", "client-config", "/v1/config/"],
    "dev_menu": ["developermenu", "DeveloperMenu", "dev_menu"],
    "live_preview": ["live_preview", "LivePreview", "unpublished"],
    "awesome_mode": ["AwesomeMode", "pusher", "Pusher"],
    "offline_queue": ["in_queue", "ProgressQueue", "queue"],
    "notifications": ["FirebaseMessagingService", "notification", "deviceTokens"],
    "in_app_messaging": ["customerio", "CustomerIo", "gist"],
    "widget": ["MimoStreak", "Glance", "Widget"],
    "deep_links": ["deeplink", "getmimo.com/learn", "continuelearning"],
    "share": ["share_to_stories", "SharePromoLink", "promo_link_shared"],
    "report_lesson": ["report_lesson", "ReportLesson"],
    "search": ["search_tracks", "search_v2", "TrackSearch"],
    "profile": ["public_profile", "PublicProfile", "profile_tab"],
    "analytics": ["mixpanel", "Mixpanel", "SuperProperty", "track("],
    "adjust_attribution": ["adjust", "Adjust"],
    "auth": ["/auth/token", "AuthenticationActivity", "signInWithCredential"],
    "room_db": ["chapter_completions", "lesson_progress", "tutorial_completions"],
    "saved_code": ["savedCode", "/v1/code", "remix"],
    "coding_keyboard": ["CodingKeyboard", "codingkeyboard"],
    "code_editor": ["codeeditor", "CodeFileNaming", "AutoCompletion"],
    "webview_lesson": ["lesson-webview", "WebViewLessonScrollView", "bootstrapScript"],
    "database_lesson": ["sourceDatabaseTables", "DatabaseView", "TableOutput"],
}

HEAD_RE = re.compile(r"^([A-Za-z_$][A-Za-z0-9_$.]*)\(([A-Za-z_][A-Za-z0-9_$]*)=")
FMID_RE = re.compile(r"^(?:, )?([A-Za-z_][A-Za-z0-9_$]*)=$")


def main(extracted: str, out_dir: str, prefix: str = "Lcom/getmimo/") -> None:
    os.makedirs(out_dir, exist_ok=True)
    from loguru import logger
    logger.remove()
    from androguard.core.dex import DEX

    dex_files = sorted(glob.glob(os.path.join(extracted, "*.dex")))
    if not dex_files:
        sys.exit(f"no .dex files under {extracted}")
    inventory, class_strings, contracts, method_literals, annotations = [], {}, {}, {}, {}
    dexes = []
    for path in dex_files:
        data = open(path, "rb").read()
        if len(data) < 0x70:
            inventory.append({"file": os.path.basename(path), "size": len(data), "classes": 0, "note": "stub"})
            continue
        dex = DEX(data)
        classes = list(dex.get_classes())
        inventory.append({"file": os.path.basename(path), "size": len(data), "classes": len(classes)})
        dexes.append((os.path.basename(path), classes))

    for _, classes in dexes:
        for cls in classes:
            name = cls.get_name()
            if not name.startswith(prefix):
                continue
            anns = []
            try:
                for a in (cls.get_annotations() or []):
                    try:
                        anns.append(a.get_name())
                    except Exception:
                        anns.append(str(a))
            except Exception:
                pass
            if anns:
                annotations[name] = sorted(set(anns))
            lits, methods = set(), {}
            for m in cls.get_methods():
                code = m.get_code()
                if not code:
                    continue
                found = []
                for ins in code.get_bc().get_instructions():
                    n = ins.get_name()
                    if n.startswith("const-string"):
                        try:
                            s = ins.get_raw_string()
                        except Exception:
                            continue
                        if s and len(s) >= 4:
                            found.append(s)
                if found:
                    lits.update(found)
                    key = f"{m.get_name()}{m.get_descriptor()}"
                    methods[key] = sorted(set(found))
            if lits:
                class_strings[name[1:-1].replace("/", ".")] = sorted(lits)
            if methods:
                simple = name.rsplit("/", 1)[-1].rstrip(";")
                if any(tok in name for tok in ("lessonparser", "ui/lesson", "content/model", "core/model/lesson")):
                    method_literals[name[1:-1].replace("/", ".")] = methods
            # data contracts from Kotlin toString() templates:
            #   "Name(" then ", fieldA=" / ", fieldB=" ... (order = declaration order)
            toks = []
            for m in cls.get_methods():
                code = m.get_code()
                if not code:
                    continue
                for ins in code.get_bc().get_instructions():
                    if ins.get_name().startswith("const-string"):
                        try:
                            toks.append(ins.get_raw_string())
                        except Exception:
                            pass
            head = None
            for t in toks:
                fm = HEAD_RE.match(t)
                if fm:
                    head = fm.group(1)
                    first = [fm.group(2)]
                    break
            if head:
                fields = list(first)
                for t in toks:
                    fm = FMID_RE.match(t)
                    if fm and fm.group(1) not in fields:
                        fields.append(fm.group(1))
                contracts[name[1:-1].replace("/", ".")] = {"type": head, "fields": fields}

    # feature index
    feature_evidence = collections.defaultdict(list)
    lower_map = {cls: [s.lower() for s in strs] for cls, strs in class_strings.items()}
    for cls, strs in class_strings.items():
        text = lower_map[cls]
        for feat, pats in FEATURES.items():
            hits = []
            for p in pats:
                pl = p.lower()
                for s, sl in zip(strs, text):
                    if pl in sl:
                        hits.append(s)
                        break
            if hits:
                feature_evidence[feat].append({"class": cls, "literals": sorted(set(hits))[:6]})
    for feat in feature_evidence:
        feature_evidence[feat].sort(key=lambda x: x["class"])

    json.dump(inventory, open(os.path.join(out_dir, "dex-inventory.json"), "w"), indent=1)
    with gzip.open(os.path.join(out_dir, "class-strings.json.gz"), "wt", encoding="utf-8") as fh:
        json.dump(class_strings, fh, ensure_ascii=False, sort_keys=True)
    json.dump(contracts, open(os.path.join(out_dir, "data-contracts.json"), "w"), indent=1, ensure_ascii=False)
    json.dump({k: v for k, v in feature_evidence.items()},
              open(os.path.join(out_dir, "feature-evidence.json"), "w"), indent=1, ensure_ascii=False)
    json.dump(method_literals, open(os.path.join(out_dir, "method-literals.json"), "w"), indent=1, ensure_ascii=False)
    json.dump(annotations, open(os.path.join(out_dir, "annotations.json"), "w"), indent=1, ensure_ascii=False)

    print(f"dex files: {len(inventory)} | app classes with literals: {len(class_strings)} | "
          f"data contracts: {len(contracts)} | features indexed: {len(feature_evidence)} | "
          f"classes with class-annotations: {len(annotations)}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "evidence",
         sys.argv[3] if len(sys.argv) > 3 else "Lcom/getmimo/")
