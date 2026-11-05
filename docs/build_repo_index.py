#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate REPO_INDEX.json from git + filesystem facts (no dependencies).

Usage: python3 docs/build_repo_index.py
Keeps the machine-readable handoff in sync with the checkout.
"""
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
import os
os.chdir(ROOT)

def nfiles(p: str) -> int:
    """Count files safely; some vendored test fixtures have >255-char names."""
    n = 0
    for dirpath, dirnames, filenames in os.walk(p, onerror=lambda e: None):
        if '.git' in dirnames:
            dirnames.remove('.git')
        n += len(filenames)
    return n

def tracked(p: str) -> int:
    out = subprocess.check_output(['git', 'ls-files', '--', p], text=True).strip()
    return len(out.split('\n')) if out else 0

commits = subprocess.check_output(
    ['git', 'log', '--pretty=format:%h'], text=True).strip().split('\n')
head = commits[0]

idx = {
 "schemaVersion": "1.0",
 "generatedAt": "2026-11-05",
 "purpose": "Canonical machine-readable handoff for the whole repository. Any agent must parse this first, then follow readOrder.",
 "repository": {"name": "danmillman008-hub/game", "branch": "arena/aebb90b7-game",
   "head": "9179b8c4", "headMeaning": "product state described by this handoff; intentionally stable, not the live HEAD",
   "headSubject": "Rebuild the content layer on the measured Mimo 9.35 lesson model",
   "commitCount": len(commits), "firstCommit": "8ea70cca",
   "baselineHead": "9179b8c4", "baselineCommitCount": 137,
   "baselineNote": "The handoff describes the repository at 9179b8c4 (137 commits). Later commits update docs/04_CURRENT_STATE.md; re-run this generator to refresh counts.",
   "firstCommitDate": "2026-10-24", "lastCommitDate": "2026-11-05",
   "baselineTrackedFiles": 13616,
   "note": "Tracked-file count measured at 9179b8c4, before the root handoff docs were added."},
 "language": "fa", "answerLanguage": "fa",
 "readOrder": ["README.md", "AGENTS.md", "docs/00_START_HERE.md", "docs/01_CHRONOLOGY.md",
   "docs/02_DECISIONS.md", "docs/03_ERRORS_AND_DEAD_ENDS.md", "docs/04_CURRENT_STATE.md",
   "docs/05_ROADMAP.md", "docs/06_EVIDENCE_INDEX.md", "docs/07_GLOSSARY.md",
   "docs/08_HANDOFF_PROMPT.md", "docs/09_COMMIT_LOG.md", "REPO_INDEX.json"],
 "documents": [
   {"path": "README.md", "role": "human + agent entry point"},
   {"path": "AGENTS.md", "role": "hard operating contract for every AI agent"},
   {"path": "docs/00_START_HERE.md", "role": "5-minute orientation, 3 layers, source-of-truth ladder"},
   {"path": "docs/01_CHRONOLOGY.md", "role": "origin, all phases, M02-M09, two rejected builds, 137 commits"},
   {"path": "docs/02_DECISIONS.md", "role": "active constraints, superseded decisions, v12.5-fa notes, honesty vocabulary"},
   {"path": "docs/03_ERRORS_AND_DEAD_ENDS.md", "role": "failures, bugs, dead ends, user-rejected outputs"},
   {"path": "docs/04_CURRENT_STATE.md", "role": "exact tree, commands, numbers, honest flags, has/has-not table"},
   {"path": "docs/05_ROADMAP.md", "role": "R1-R16 ordered remaining work + definition of done"},
   {"path": "docs/06_EVIDENCE_INDEX.md", "role": "claim -> evidence file map"},
   {"path": "docs/07_GLOSSARY.md", "role": "terminology"},
   {"path": "docs/08_HANDOFF_PROMPT.md", "role": "copy-paste prompt for the next agent"},
   {"path": "docs/09_COMMIT_LOG.md", "role": "full 137-commit log"},
   {"path": "docs/10_FILE_MAP.md", "role": "file-by-file map of every module, tool and evidence tree"},
   {"path": "docs/verify_docs.py", "role": "link/index/CJK integrity checker"},
   {"path": "docs/build_repo_index.py", "role": "regenerates this file"},
   {"path": "CLAUDE.md", "role": "pointer to AGENTS.md for Claude-family agents"},
   {"path": "GEMINI.md", "role": "pointer to AGENTS.md for Gemini-family agents"},
   {"path": ".github/copilot-instructions.md", "role": "pointer to AGENTS.md for GitHub Copilot"}],
 "layers": {
   "evidence": {"path": "ANALYSIS/", "files": nfiles("ANALYSIS"), "tracked": tracked("ANALYSIS"),
     "description": "Mimo 9.35 reverse engineering: DECOMPILED, GHIDRA, RUNTIME, MISSION_05..09, API surfaces, unknowns register",
     "authoritative": True, "serverConfirmed": 0},
   "design": {"path": "mimo-ui/", "files": nfiles("mimo-ui"), "tracked": tracked("mimo-ui"),
     "description": "0-100 UI extraction plus 12 archived design rounds; approved prototype is mimo-ui/UPGRADE/DESIGN/index.html v12.5-fa",
     "authoritative": True,
     "prototypeSha256": "c356068daa5ccafbee46599897ad18bdf1e4f91f1ca23f36b1b8bd153dbfdb78"},
   "product": {"path": "app/", "files": nfiles("app"), "tracked": tracked("app"),
     "description": "offline application: content contract, engines, native shell, tests, tools, docs, generated dist/",
     "authoritative": True}},
 "phases": [
   {"id": "P0", "date": "2026-10-24", "commit": "8ea70cca", "name": "Initial upload", "status": "archived", "note": "raw zip/html/apk, no project code"},
   {"id": "P1", "date": "2026-11-03", "commits": ["dec73267", "0e634722"], "name": "Mimo 9.35 UI reverse engineering + Konkur plan + design v2..v11.1", "status": "archived"},
   {"id": "P2", "date": "2026-11-04", "commits": ["832edf04", "8ef46856", "231490d2", "966394f5"], "name": "Deep static decode, Ghidra/JADX proxy, v12..v12.5-fa final prototype", "status": "approved"},
   {"id": "P3", "date": "2026-11-05", "name": "Runtime missions M02..M09", "status": "closed-with-unknowns",
     "commits": {"M02": "907d8b01", "M03": "14e7fc66", "M04": "d0714b40", "M05": "d0714b40", "M06": "cfc8ea41", "M07": "477d3195", "M08": "67353077", "M09": "2ea6b0ff"},
     "result": "46 screens/45 edges, 181 hooks/72 entries, 10,298 tutorial JSON files, curriculum graph, no server confirmation"},
   {"id": "P4", "date": "2026-11-05", "commits": ["057716bc", "3eed9da3", "15ef9389"], "name": "Independent offline app shell + phase 2", "status": "superseded-as-product"},
   {"id": "P5", "date": "2026-11-05", "commits": ["00ca5d3d", "986e7c08"], "name": "Mimo information form + pedagogy + full-book OCR (848/848) + word boxes", "status": "ocr-complete-content-open"},
   {"id": "P6", "date": "2026-11-05", "commits": ["543a20ba", "7ad687b9"], "name": "First one-click output (REJECTED by user) + Hadaf Plus AI API audit", "status": "output-rejected-audit-valid"},
   {"id": "P7a", "date": "2026-11-05", "commit": "2042db0d", "name": "Rebuild 1: native M09 navigation", "status": "current"},
   {"id": "P7b", "date": "2026-11-05", "commit": "9179b8c4", "name": "Rebuild 2: measured-Mimo structured content layer", "status": "current"}],
 "missions": {"M02": "907d8b01", "M03": "14e7fc66", "M04": "d0714b40", "M05": "d0714b40",
   "M06": "cfc8ea41", "M07": "477d3195", "M08": "67353077", "M09": "2ea6b0ff",
   "finalDeliverables": "ANALYSIS/MISSION_09/", "unknownRegister": "ANALYSIS/MISSION_09/FINAL_UNKNOWN_REGISTER.md"},
 "rejectedOutputs": [
   {"commit": "543a20ba", "verdict": "فاجعه", "reason": "phone mock shell, admin panels, layout-demo text used as lesson, hash-random questions", "bytes": 1603793},
   {"commit": "2042db0d", "verdict": "partially accepted (یکم بهتر شد)", "reason": "navigation fixed, lesson content still wrong", "bytes": 1495874}],
 "currentDeliverable": {
   "oneFile": "app/dist/Mimo.html", "bytes": 1863312,
   "sha256": "c6f8cbfbb3c7ee5628cd1f0e7763c9f95ff852d3ce22bc48fa30d691423b2435",
   "pwa": "app/dist/index.html", "zip": "app/dist/Mimo.zip", "zipBytes": 910509,
   "guide": "app/dist/START_HERE.txt", "readmeFa": "app/dist/README-fa.md",
   "manifest": "app/dist/BUILD_MANIFEST.json", "bundledModules": 15,
   "generator": "app/tools/build_output.py", "shell": "app/native/index.html", "controller": "app/src/native.js",
   "entryAction": "double-click Mimo.html; no server, no npm, no internet"},
 "content": {
   "package": "app/content/STRUCTURED_PACKAGE.json", "bytes": 175496,
   "contract": "app/content/MIMO_INFORMATION_FORM.json",
   "engine": "app/src/content-engine.js", "emitter": "app/tools/emit_structured_package.py",
   "bookProcessor": "app/tools/process_book.py",
   "shape": "track -> sections -> tutorialIds -> chapters -> micro-lessons -> typed blocks",
   "counts": {"tracks": 1, "sections": 4, "tutorials": 20, "chapters": 20,
     "microLessons": 120, "blocks": 160, "questions": 20, "knownAnswers": 20},
   "roles": ["hook", "check", "feedback", "explain", "practice", "recap"],
   "rendererFamilies": ["text", "strong", "MultipleChoice", "fillTheGap", "feedback"],
   "contentStatus": "structured", "reviewStatus": "unreviewed", "sourceKind": "placeholder",
   "bookDraft": "app/content/source/biology-12/PROCESSED_DRAFT.json (gitignored, noisy, NOT wired into app)",
   "ocr": {"pages": 848, "meanConfidence": 78.1, "words": 694860, "answerKeyEntries": 775,
     "fourOptionQuestions": 608, "joined": 600, "unjoined": 8, "matchedAnswerEntries": 392,
     "perOptionExplanations": 475, "proseDrafts": 300, "status": "complete-but-unreviewed"}},
 "honest": {
   "serverConfirmed": 0, "llm": False, "network": False, "generatedText": False,
   "externalProvider": "not-configured", "fetchOrXhrOrWebsocketOrEventSource": False,
   "apiKey": False, "reviewedTextbookContent": False, "physicalPwaInstallTested": False,
   "vocabulary": ["VERIFIED_STATIC", "VERIFIED_RUNTIME", "VERIFIED_ASSET", "VERIFIED_DATABASE",
     "VERIFIED_NETWORK_OBSERVATION", "INFERRED", "UNKNOWN", "SERVER_DEPENDENT"]},
 "verification": {
   "commands": ["npm test --prefix app", "npm run verify --prefix app",
     "python3 app/tools/validate_content.py app/content/STARTER_PACKAGE.json app/content/STRUCTURED_PACKAGE.json",
     "python3 docs/verify_docs.py"],
   "expected": {"npmTest": "45/45", "verifyApp": "54/54", "verifyOutput": "51/51", "contentValidator": "2/2"},
   "browser": {"fileUrl": True, "ports": [3000, 3001], "mimo": True, "microLessons": 120,
     "answerKeyRows": 4, "errors": []},
   "buildCommands": ["python3 app/tools/emit_structured_package.py", "python3 app/tools/build_output.py"]},
 "navigation": ["MainActivity/tabs", "PathMap", "ChapterActivity", "LessonRenderer", "QuitDialog",
   "Celebration", "SelectPath", "PathOverview", "SectionDetail", "PracticeGate", "ExamHub", "AI", "Tokens", "Output"],
 "designContract": {
   "version": "v12.5-fa", "tabs": ["Learn", "Practice", "AI", "Leaderboard", "Profile"],
   "tabsFa": ["یادگیری", "تمرین", "هوش مصنوعی", "امتیازها", "پروفایل"],
   "chips": ["coins", "keys∞", "streak"],
   "forbidden": ["MAX", "daily routine", "Habitica", "Dictate", "Pro", "payment"],
   "rtl": True, "nightMode": True, "examSections": 7, "defaultExamMinutes": 270,
   "answerSheetVsAnswerKey": "پاسخبرگ ≠ پاسخنامه",
   "tokens": {"bg": "#F6F7FB", "night": "#252746", "button": "#7E4BDE", "progress": "#8D60E2",
     "TextH1": "24sp", "TextP2": "16sp", "toolbar": "56dp", "cardRadius": "12dp"},
   "notesMustBeRespectedPercent": 100},
 "trees": {
   "root": {"strayUploads": ["Streets-of-Rage_Genesis_EN.zip", "pharmacy-inventory (3).html", "ttac-4.3.6.apk"],
     "canonical": ["README.md", "AGENTS.md", "REPO_INDEX.json", "docs/"]},
   "ANALYSIS": {"files": nfiles("ANALYSIS"), "tracked": tracked("ANALYSIS"),
     "subdirs": ["DECOMPILED", "GHIDRA", "RUNTIME", "_INPUT", "_TOOLCHAIN", "MISSION_05", "MISSION_06", "MISSION_07", "MISSION_08", "MISSION_09"]},
   "mimo-ui": {"files": nfiles("mimo-ui"), "tracked": tracked("mimo-ui"),
     "subdirs": ["ATLAS", "CATALOGS", "RECONSTRUCTION", "REFERENCE", "SCREENS", "SOURCE", "UPGRADE", "tools"]},
   "mimo-ui/UPGRADE": {"files": nfiles("mimo-ui/UPGRADE"), "markdownDocs": 25, "catalogs": 24,
     "status": "archived design rounds; conflicting superseded banners; NOT the current verdict"},
   "app": {"files": nfiles("app"), "tracked": tracked("app"),
     "subdirs": {"assets": "byte-identical approved v12.5-fa copies + native.css",
       "native": "native shell index.html", "src": "22 ESM modules",
       "content": "content contract + packages", "content/source": "1701 gitignored OCR JSON files",
       "dist": "12 generated output files", "docs": "7 implementation docs",
       "tools": "15 tracked python tools", "tests": "6 test files"}},
   "TOOLS": {"files": nfiles("TOOLS"), "tracked": tracked("TOOLS"),
     "submodules": {"TOOLS/ghidra": "NSA/ghidra master", "TOOLS/rea": "morluto/rea main"}},
   "google_drive": {"files": nfiles("google_drive"), "tracked": 0, "gitignored": True,
     "contents": ["Mimo_9.35 (1).zip", "Mimo_9.35 (1).z01", "Mimo_9.35 (1).z02",
       "Hadaf Plus_2.0.2.apk", "همدرس_7.4.4.apk", "@BankBookkonkor (26)_extract.pdf"]},
   ".github/workflows": ["mimo-re-toolchain.yml", "mimo-jadx-proxy.yml", "mimo-runtime-verification.yml"]},
 "ignoredByGit": ["/google_drive/", "/mimo-ui/.cache/", "__pycache__/", "/TOOLS/_*/",
   "/ANALYSIS/_TOOLCHAIN/_scratch/", "node_modules/", "/app/content/source/"],
 "staleDocuments": [
   {"path": "mimo-ui/UPGRADE/00_START_HERE.md", "issue": "says DESIGN v5 is حکم فعلی, plus v6..v12 superseded banners", "canonical": "README.md"},
   {"path": "mimo-ui/UPGRADE/README.md", "issue": "says plan-only / no product code written", "canonical": "README.md"},
   {"path": "app/OUTPUT_REPORT.md", "issue": "contains the rejected output report; newer report prepended", "canonical": "docs/04_CURRENT_STATE.md"},
   {"path": "app/README.md", "issue": "historical test counts", "canonical": "docs/04_CURRENT_STATE.md"},
   {"path": "app/content/README.md", "issue": "does not list STRUCTURED_PACKAGE.json", "canonical": "docs/04_CURRENT_STATE.md"}],
 "knownGaps": [
   "reviewStatus=unreviewed; textbook content NOT in app",
   "exam/QBANK and exam-template.js are placeholders",
   "chapterRefFor() is hash-based, not a real curriculum mapping",
   "only 5 of the measured renderer families are implemented",
   "app/assets/phone.html still statically contains the rejected layout-demo text",
   "U-WEB-001 native WebView bridge + payload remains UNKNOWN",
   "no server-side formulas, no runtime endpoint capture, SERVER CONFIRMED=0",
   "physical PWA install on a phone not tested",
   "no emulator/ADB/KVM available in this sandbox",
   "Practice/Leaderboard/Profile contents were not observed at runtime"],
 "roadmap": [
   {"id": "R1", "priority": "P0", "task": "human-reviewed textbook content -> approved STRUCTURED_PACKAGE"},
   {"id": "R2", "priority": "P0", "task": "deterministic chapterRefFor() mapping, no hash/random"},
   {"id": "R3", "priority": "P0", "task": "remove last layout-demo trace without destroying the approved hash"},
   {"id": "R4", "priority": "P1", "task": "validatedInput + solvedContent offline"},
   {"id": "R5", "priority": "P1", "task": "local InteractiveWebView bridge, zero network"},
   {"id": "R6", "priority": "P1", "task": "Reveal / noninteractiveSlide / executableFiles blocks"},
   {"id": "R7", "priority": "P1", "task": "hardMode + challengeLevel 0-2 cycle"},
   {"id": "R8", "priority": "P1", "task": "persistent cross-session mistake review queue"},
   {"id": "R9", "priority": "P2", "task": "real 7-section exam with answer sheet + answer key + timer"},
   {"id": "R10", "priority": "P2", "task": "replace learning-path.js synthetic KONKUR data"},
   {"id": "R11", "priority": "P2", "task": "Leaderboard/Profile: either approved UI or honest NOT MODELED"},
   {"id": "R12", "priority": "P2", "task": "keep ai-studio/harness local unless user explicitly requests an external provider"},
   {"id": "R13", "priority": "P3", "task": "physical Android PWA install test"},
   {"id": "R14", "priority": "P3", "task": "automated reference screenshots in CI"},
   {"id": "R15", "priority": "P3", "task": "fully byte-reproducible build (ZIP timestamp)"},
   {"id": "R16", "priority": "P3", "task": "root stray-upload cleanup, only with user permission"}],
 "rules": [
   "Only branch arena/aebb90b7-game; never switch/create/push another branch.",
   "Never claim server behaviour, correct OCR answers, or reviewed textbook content.",
   "No LLM, no network, no API key, no generated text.",
   "Never commit app/content/source/ or google_drive/ binaries.",
   "Never modify the byte-protected approved assets; verify_app.py checks their hashes.",
   "Never delete or rewrite historical evidence under mimo-ui/UPGRADE or ANALYSIS/MISSION_*.",
   "Never hand-edit app/dist/; it is generated.",
   "Answer the user in Persian; never ask for a clarification that the repo already answers."],
 "paths": []
}

paths = list(idx['readOrder']) + [d['path'] for d in idx['documents']] + [
 "ANALYSIS", "ANALYSIS/MISSION_09/FINAL_UNKNOWN_REGISTER.md", "ANALYSIS/HADAF_PLUS_AI_API_AUDIT.md",
 "mimo-ui", "mimo-ui/UPGRADE/DESIGN/index.html", "mimo-ui/UPGRADE/02_UI_FIDELITY_CONTRACT.md",
 "mimo-ui/UPGRADE/CATALOGS/UI_FIDELITY_RULES.csv",
 "app", "app/native/index.html", "app/assets/native.css", "app/assets/phone.html", "app/assets/proto.css",
 "app/assets/proto-data.js", "app/assets/proto-ui.js", "app/src/native.js", "app/src/content-engine.js",
 "app/src/content-package.js", "app/content/STRUCTURED_PACKAGE.json", "app/content/MIMO_INFORMATION_FORM.json",
 "app/content/STARTER_PACKAGE.json", "app/content/PEDAGOGY.md", "app/content/source",
 "app/dist/Mimo.html", "app/dist/index.html", "app/dist/Mimo.zip", "app/dist/BUILD_MANIFEST.json",
 "app/dist/START_HERE.txt", "app/dist/README-fa.md", "app/dist/sw.js", "app/dist/manifest.webmanifest",
 "app/tools/build_output.py", "app/tools/emit_structured_package.py", "app/tools/process_book.py",
 "app/tools/validate_content.py", "app/tools/verify_app.py", "app/tools/verify_output.py",
 "app/docs/MIMO_CONTENT_MODEL.md", "app/docs/MIMO_NATIVE_NAVIGATION.md", "app/docs/OUTPUT_GUIDE.md", "app/docs/TESTING.md",
 "app/README.md", "app/OUTPUT_REPORT.md", "app/package.json", "app/server.js",
 ".gitignore", ".gitmodules", ".github/workflows/mimo-runtime-verification.yml",
 "TOOLS/ghidra", "TOOLS/rea", "google_drive",
 "CLAUDE.md", "GEMINI.md", ".github/copilot-instructions.md"]
idx['paths'] = sorted(set(paths))
(ROOT / 'REPO_INDEX.json').write_text(json.dumps(idx, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('wrote REPO_INDEX.json: %d commits, %d verified paths' % (len(commits), len(idx['paths'])))
