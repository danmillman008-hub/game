#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_design_v12.py — round 12: rebuild the EXAM surfaces on real Mimo lesson UI.

CODE-FIRST evidence (decoded com.getmimo 9.35 APK, screenshots VISUAL_CROSSCHECK_ONLY):
  chapter_toolbar.xml ............ 52dp nav: X | pb_chapter (6dp) | flag, 1dp line_primary
  lesson_interactive_multiplechoice_fragment.xml .. ScrollView + LessonDescriptionView + ChoiceView
  choice_view.xml / choice_list_item.xml / layout_choice_card_item.xml .. radio + TextP1 + 48dp cards
  multiplechoice_background_{unselected,selected,correct,wrong}.xml .. 12dp radius, 2dp strokes
  interaction_keyboard_view.xml / run_button_view.xml .. 68dp footer, 48dp squares + btn_continue_big
  lesson_interactive_feedback_bottom_sheet_dialog.xml .. inline correct/wrong feedback
  lesson_awesome_fragment.xml / chapter_finished_*.xml .. result celebration + full-width CTA
  strings: lesson_continue / lesson_submit / lesson_skip / interaction_hint_single_choice

The user explicitly allowed a structural break: the two equal-weight «سؤال قبل / سؤال بعد»
pill buttons are GONE.  prevQ is now a 48dp square icon button (btn_undo slot) and nextQ is
the single full-width purple CONTINUE/SUBMIT CTA (btn_continue_big / btn_submit slot).
Everything else (5 tabs, 7 labelled exam sections, fixed 270 min, timer only inside exam,
پاسخبرگ≠پاسخنامه, exactly one pre-existing exam-hub lock, one AI button, isolated
section-practice, curved zigzag) is UNCHANGED. Design/prototype only — no product code.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

UP = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
TOOLS = UP / "tools"
DESIGN = UP / "DESIGN"
SRC = TOOLS / "design_v11_full.html"
html = SRC.read_text(encoding="utf-8")


def rep(old: str, new: str, label: str, count: int = 1):
    global html
    n = html.count(old)
    if n != count:
        raise SystemExit("%s matched %d times (expected %d)" % (label, n, count))
    html = html.replace(old, new, count)


def rx1(pattern: str, new: str, label: str):
    global html
    out, n = re.subn(pattern, lambda m: new, html, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("regex %s matched %d times" % (label, n))
    html = out


# ---------------------------------------------------------------------------
# 1. machine-readable code evidence
# ---------------------------------------------------------------------------
EVIDENCE = {
    "round": "v12",
    "method": "CODE_FIRST / decoded APK resources; screenshots VISUAL_CROSSCHECK_ONLY",
    "apk": "com.getmimo 9.35 / versionCode 1792759685",
    "principle": "The exam screens must look like the SAME app as the Learn screens. "
                 "No separate 'konkur' skin, no bespoke button pairs.",
    "layouts": {
        "chapter_toolbar.xml": "52dp nav: btn_lesson_close(ic_close) | pb_chapter(6dp ProgressBarChapter) "
                               "| btn_lesson_report(ic_flag) | v_line 1dp line_primary",
        "lesson_interactive_fragment.xml": "FrameLayout container_lesson_interactive, paddingTop=lesson_progress_navbar_height",
        "lesson_interactive_multiplechoice_fragment.xml": "LinearLayout vertical, background_primary; "
            "ScrollView nsv_multiplechoice_lesson_content (weight 1) with LessonDescriptionView + "
            "LessonOutputView + ChoiceView; InteractionKeyboardContainerView pinned at bottom",
        "choice_view.xml": "tv_multiplechoice_hint (TextInteractionHint) + rv_multiplechoice_options RecyclerView",
        "choice_list_item.xml": "TextView TextP1 18sp, minHeight 48dp, margin 4dp/12dp, "
            "padding 16dp/12dp, elevation 1dp, background multiplechoice_background_unselected",
        "layout_choice_card_item.xml": "MaterialRadioButton + tv_choice_card_item_name (TextP2 16sp), padding 12dp",
        "interaction_keyboard_view.xml": "68dp; border_top 1dp line_primary; btn_reset/btn_undo 48dp squares on left; "
            "RunButton with btn_play / btn_continue_big / btn_submit full-width on right",
        "run_button_view.xml": "btn_play 48dp, btn_continue_big (0dp full width, min 140dp), btn_submit (same)",
        "lesson_interactive_feedback_bottom_sheet_dialog.xml": "drawer_bottom_sheet_background, maxWidth 496dp; "
            "compose feedback content = correct / wrong explanation",
        "quiz_introduction_fragment.xml": "ic_survey illustration + TextH1 title + TextP1 description "
            "+ btn_start_quiz / btn_not_now full-width buttons",
        "lesson_awesome_fragment.xml / chapter_finished_leaderboard_fragment.xml":
            "celebration hero + stats + one full-width bottom CTA",
    },
    "dimens_dp": {
        "lesson_progress_navbar_height": 52, "lesson_progressbar_height": 6,
        "lesson_content_margin_top": 8, "lesson_content_margin_bottom": 16,
        "interaction_keyboard_height": 68, "interaction_keyboard_button_margin_bottom": 12,
        "interaction_keyboard_button_width": 140, "multiplechoice_elevation": 1,
        "cardview_corner_radius_large": 12, "spacing_xxs": 4, "spacing_xs": 8, "spacing_s": 12,
        "spacing_m": 16, "spacing_l": 24, "spacing_xl": 32, "toolbar_height": 56,
    },
    "colors": {
        "background_primary": "#FFF6F7FB", "navbar_background": "#FFFFFFFF",
        "text_primary": "#FF252746", "text_weak": "#FF4A4D85", "navbar_icon": "#FF626596",
        "line_primary": "#FFEDEEF6", "button_primary": "#FF7E4BDE",
        "button_primary_highlight": "#FF6E3EC8",
        "selection_enabled": "#FFFFFFFF", "selection_selected": "#FFEDEEF6",
        "support_green": "#FF66BC5A", "support_blue": "#FF3890FA", "support_coral": "#FFF05A6E",
        "progress_chapter_primary": "#FF8D60E2", "progress_chapter_background": "#FFE4E6F1",
    },
    "styles": {"TextH1": 24, "TextH2": 20, "TextP1": 18, "TextP2": 16,
               "TextLabel1": 14, "TextButton1": 18, "TextButton2": 16,
               "TextInteractionHint": "text_weak + ic_info_circle drawableStartCompat + spacing_l top"},
    "strings": {"lesson_continue": "Continue", "lesson_submit": "Submit", "lesson_skip": "Skip",
                "continue_next": "Continue next", "start_quiz": "Start quiz",
                "interaction_hint_single_choice": "Tap the correct answer",
                "interaction_hint_multiple_choice": "Tap the correct answers"},
    "drawables": ["multiplechoice_background_unselected.xml", "multiplechoice_background_selected.xml",
                  "multiplechoice_background_correct.xml", "multiplechoice_background_wrong.xml",
                  "progress_bar_chapter.xml", "drawer_bottom_sheet_background.xml", "ic_close.xml",
                  "ic_flag.xml", "ic_info_circle.xml"],
    "ui_mapping": [
        {"apk": "btn_lesson_close (ic_close)", "prototype": ".ln-x → exitSheet"},
        {"apk": "pb_chapter (SpringAnimatingProgressBar 6dp)", "prototype": ".ln-prog > i #examProgress"},
        {"apk": "btn_lesson_report (ic_flag)", "prototype": ".ln-report → paletteSheet"},
        {"apk": "LessonDescriptionView / TextH1-H2", "prototype": ".qtext #qText"},
        {"apk": "tv_multiplechoice_hint (TextInteractionHint)", "prototype": ".lb-hint"},
        {"apk": "rv_multiplechoice_options / choice_list_item", "prototype": ".lb-choices > .opt"},
        {"apk": "multiplechoice_background_selected/correct/wrong", "prototype": ".opt.on / .correct / .wrong"},
        {"apk": "lesson_interactive_feedback_bottom_sheet_dialog", "prototype": "#exFeedback"},
        {"apk": "btn_undo 48dp square", "prototype": "#prevQ .lk-square (سؤال قبل)"},
        {"apk": "btn_reset 48dp square", "prototype": "#markQ .lk-square (علامتگذاری)"},
        {"apk": "btn_continue_big / btn_submit FULL-WIDTH primary", "prototype": "#nextQ .lk-cta"},
        {"apk": "lesson_skip", "prototype": "#skipQ .lk-skip"},
        {"apk": "lesson_awesome_fragment celebration", "prototype": ".rf-hero (exam-result)"},
    ],
    "button_correction": {
        "before_v11": "two equal-weight pill buttons .qnav: «سؤال قبل» (left) + «سؤال بعد» (right), "
                      "plus a 7-button horizontally-scrolling .qfoot toolbar",
        "after_v12": "ONE full-width purple CONTINUE/SUBMIT CTA + one 48dp icon-only back square "
                     "+ one 48dp bookmark square, all inside a 68dp Mimo interaction keyboard; "
                     "secondary tools collapse into a quiet chip row above the footer",
        "reason": "decoded interaction_keyboard_view.xml / run_button_view.xml + mimo-04 screenshot",
    },
    "screenshots_visual_crosscheck_only": ["DESIGN/REFERENCE/mimo-04-lesson-continue.jpg"],
    "unchanged_contract": ["5 tabs / no MAX", "7 labelled exam sections + templates + descriptive answer",
        "fixed 270 min for comprehensive", "timer only inside exam", "پاسخبرگ≠پاسخنامه",
        "exactly one exam-hub lock", "one AI button (two places)", "isolated section-practice",
        "original curved zigzag path map", "no UI annotation notes"],
}
(DESIGN / "EXAM_UI_CODE_EVIDENCE.json").write_text(
    json.dumps(EVIDENCE, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# ---------------------------------------------------------------------------
# 2. CSS — all exam screens now use Mimo tokens, no separate 'konkur' skin
# ---------------------------------------------------------------------------
CSS12 = r'''
/* ---- v12 · EXAM surfaces rebuilt from decoded Mimo lesson layouts ---- */
.exv12{direction:rtl;background:var(--bg);display:none;flex-direction:column;overflow:hidden}
.exv12.on{display:flex}
.exv12 *{scrollbar-width:thin}
/* chapter_toolbar.xml : 52dp */
.exv12 .ln{height:52px;min-height:52px;display:flex;align-items:center;gap:6px;padding:0 10px;background:var(--card);border-bottom:1px solid var(--line);position:relative;z-index:3;flex:0 0 52px}
.exv12 .ln-x,.exv12 .ln-report{width:40px;height:40px;flex:0 0 40px;border:0;background:transparent;color:var(--weak-icon);display:inline-flex;align-items:center;justify-content:center;padding:0}
.exv12 .ln-x:hover,.exv12 .ln-report:hover{color:var(--primary)}
.exv12 .ln-mid{flex:1;min-width:0;display:flex;flex-direction:column;gap:5px;align-items:center}
.exv12 .ln-mid b{font:700 11px/1.2 Tahoma,system-ui,sans-serif;color:var(--text-weak);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:100%}
.exv12 .ln-prog{width:100%;height:6px;border-radius:999px;background:var(--progress-bg);overflow:hidden}
.exv12 .ln-prog i{display:block;height:100%;border-radius:999px;background:var(--progress);transition:width .22s ease}
.exv12 .ln-timer{flex:0 0 auto;font:700 10px/1 Tahoma,system-ui,sans-serif;padding:5px 8px;gap:4px}
.exv12 .tag{font:700 10px/1 Tahoma,system-ui,sans-serif;padding:4px 9px}
/* lesson body / ScrollView */
.exv12 .lb-body{flex:1;overflow:auto;padding:8px 16px 16px}
.exv12 .lb-step{display:flex;justify-content:space-between;align-items:center;gap:10px;font:400 11px/1.5 Tahoma,system-ui,sans-serif;color:var(--text-weak);margin:8px 0 14px}
.exv12 .lb-subject{display:inline-flex;align-items:center;gap:6px;font:700 11px/1.3 Tahoma,system-ui,sans-serif;color:var(--primary);background:var(--card);border:1px solid var(--line);border-radius:999px;padding:4px 10px;margin:0 0 14px}
.exv12 .lb-dot{width:6px;height:6px;border-radius:999px;background:var(--progress)}
.exv12 .lb-sep{color:var(--weak-icon)}
.exv12 .qtext{font:400 18px/1.8 Tahoma,system-ui,sans-serif;color:var(--text);margin:0 0 16px;letter-spacing:0}
/* TextInteractionHint */
.exv12 .lb-hint{display:flex;align-items:center;gap:6px;font:400 12px/1.5 Tahoma,system-ui,sans-serif;color:var(--text-weak);margin:0 0 10px}
/* choice_list_item.xml : 48dp min, 12dp radius, 16dp/12dp padding */
.exv12 .lb-choices{display:flex;flex-direction:column;gap:8px}
.exv12 .opt{width:100%;min-height:52px;margin:0;padding:12px 14px;border:2px solid transparent;border-radius:12px;background:var(--card);box-shadow:0 1px 2px rgba(37,39,70,.10);display:flex;align-items:center;gap:10px;text-align:right;font:400 15px/1.5 Tahoma,system-ui,sans-serif;color:var(--text)}
.exv12 .opt:hover{background:var(--card-pressed)}
.exv12 .opt-radio{width:20px;height:20px;flex:0 0 20px;border:2px solid var(--weak-icon);border-radius:999px;display:inline-flex;align-items:center;justify-content:center}
.exv12 .opt-txt{flex:1}
.exv12 .opt-num{font:700 12px/1 Tahoma,system-ui,sans-serif;color:var(--text-weak);background:var(--card-pressed);border-radius:999px;padding:4px 7px;flex:0 0 auto}
.exv12 .opt.on{border-color:var(--blue);background:var(--card-pressed)}
.exv12 .opt.on .opt-radio{border-color:var(--blue);background:var(--blue)}
.exv12 .opt.on .opt-radio:after{content:"";width:8px;height:8px;border-radius:999px;background:#fff}
.exv12 .opt.correct{border-color:var(--success);background:var(--card)}
.exv12 .opt.correct .opt-radio{border-color:var(--success);background:var(--success)}
.exv12 .opt.correct .opt-radio:after{content:"";width:8px;height:8px;border-radius:999px;background:#fff}
.exv12 .opt.wrong{border-color:var(--error);background:var(--card)}
.exv12 .opt.wrong .opt-radio{border-color:var(--error);background:var(--error)}
.exv12 .opt.wrong .opt-radio:after{content:"";width:8px;height:8px;border-radius:999px;background:#fff}
/* lesson_interactive_feedback_bottom_sheet_dialog.xml */
.exv12 .lb-feedback{display:flex;gap:10px;align-items:flex-start;background:var(--card);border:1px solid var(--line);border-right:4px solid var(--success);border-radius:12px;padding:12px;margin:14px 0 0;box-shadow:0 2px 0 var(--card-pressed)}
.exv12 .lb-feedback.bad{border-right-color:var(--error)}
.exv12 .lb-feedback .fb-ic{width:30px;height:30px;flex:0 0 30px;border-radius:999px;background:var(--success);color:#fff;display:inline-flex;align-items:center;justify-content:center}
.exv12 .lb-feedback.bad .fb-ic{background:var(--error)}
.exv12 .lb-feedback b{font:700 13px/1.4 Tahoma,system-ui,sans-serif;color:var(--text)}
.exv12 .lb-feedback p{margin:4px 0 0;font:400 12px/1.8 Tahoma,system-ui,sans-serif;color:var(--text-weak)}
/* quiet utility chip row (secondary exam actions, NOT a scrolling button bar) */
.exv12 .lb-tools{display:flex;flex-wrap:wrap;gap:6px;margin:18px 0 4px;padding-top:14px;border-top:1px solid var(--line)}
.exv12 .lb-chip{display:inline-flex;align-items:center;gap:5px;border:1px solid var(--line);background:var(--card);color:var(--text-weak);border-radius:999px;padding:5px 10px;font:400 11px/1.3 Tahoma,system-ui,sans-serif}
.exv12 .lb-chip:hover{border-color:var(--primary);color:var(--primary)}
/* interaction_keyboard_view.xml : 1dp border + 48dp squares + FULL-WIDTH primary CTA */
.exv12 .lk{flex:0 0 auto;background:var(--card);border-top:1px solid var(--line);padding:10px 16px 8px;display:flex;flex-direction:column;gap:6px}
.exv12 .lk-row{display:flex;align-items:center;gap:10px}
.exv12 .lk-square{width:48px;height:48px;flex:0 0 48px;border:1px solid var(--line);background:var(--card);border-radius:16px;color:var(--text-weak);display:inline-flex;align-items:center;justify-content:center;padding:0}
.exv12 .lk-square:hover{border-color:var(--primary);color:var(--primary)}
.exv12 .lk-square.marked{border-color:var(--yellow);color:var(--primary);background:var(--card-pressed)}
.exv12 .lk-cta{flex:1;min-width:140px;height:52px;border:0;border-radius:12px;background:var(--primary);color:#fff;display:inline-flex;align-items:center;justify-content:center;gap:8px;box-shadow:0 3px 0 var(--primary-hi);font:700 16px/1 Tahoma,system-ui,sans-serif}
.exv12 .lk-cta:active{transform:translateY(2px);box-shadow:0 1px 0 var(--primary-hi)}
.exv12 .lk-cta b{font-weight:700;letter-spacing:.5px}
.exv12 .lk-skip{align-self:center;border:0;background:transparent;color:var(--text-weak);font:400 11px/1 Tahoma,system-ui,sans-serif;text-decoration:underline;padding:2px 6px}
/* ---- exam hub: Mimo list rows instead of a detached 3-column node grid ---- */
.exv12 .appbar{background:var(--card);border-bottom:1px solid var(--line);padding:0 16px;height:56px;min-height:56px;margin:0;display:flex;align-items:center;justify-content:space-between}
.exv12 .appbar b{font:700 18px/1.2 Tahoma,system-ui,sans-serif;color:var(--text)}
.exv12 .iconbtn{background:var(--card-pressed);border:1px solid var(--line);color:var(--primary);border-radius:999px;width:32px;height:32px;display:inline-flex;align-items:center;justify-content:center}
.exv12 .eh-hero{display:flex;align-items:center;gap:14px;margin:14px 16px 6px;padding:14px;background:var(--card);border:1px solid var(--line);border-radius:16px;box-shadow:0 2px 0 var(--card-pressed)}
.exv12 .eh-art{width:64px;height:64px;flex:0 0 64px;border-radius:999px;background:var(--card-pressed);display:flex;align-items:center;justify-content:center;color:var(--primary)}
.exv12 .eh-hero b{font:700 18px/1.3 Tahoma,system-ui,sans-serif;color:var(--text)}
.exv12 .eh-hero p{margin:4px 0 0;font:400 12px/1.6 Tahoma,system-ui,sans-serif;color:var(--text-weak)}
.exv12 .chips{padding:4px 16px 10px}
.exv12 .chip{font:700 11px/1 Tahoma,system-ui,sans-serif}
.exv12 .sec{font:700 13px/1.3 Tahoma,system-ui,sans-serif;color:var(--text);margin:18px 16px 2px}
.exv12 .cat-meta{background:transparent;border:0;border-radius:0;padding:0;font:400 11px/1.75 Tahoma,system-ui,sans-serif;color:var(--text-weak);margin:0 16px 10px}
.exv12 .cat-meta b{color:var(--primary)}
.exv12 .grid3{display:flex;flex-direction:column;gap:8px;padding:0 16px}
.exv12 .grid3>div{display:flex;align-items:center;gap:12px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 12px;box-shadow:0 2px 0 var(--card-pressed);cursor:pointer}
.exv12 .grid3>div:hover{border-color:var(--primary)}
.exv12 .nodek{width:44px;height:44px;flex:0 0 44px;border-radius:12px;background:var(--card-pressed);border:0;box-shadow:none;display:flex;align-items:center;justify-content:center;color:var(--primary);position:static;padding:0}
.exv12 .nodek .mini{position:static;display:none}
.exv12 .label{text-align:right;font:700 12px/1.4 Tahoma,system-ui,sans-serif;color:var(--text);margin:0;min-height:0;flex:1}
.exv12 .progress{margin:14px 16px}
/* ---- exam result: Mimo celebration ---- */
.exv12 .rf-hero{text-align:center;padding:20px 16px 6px}
.exv12 .rf-art{width:104px;height:104px;margin:0 auto 10px;border-radius:999px;background:var(--card-pressed);display:flex;align-items:center;justify-content:center;color:var(--primary)}
.exv12 .rf-hero h2{margin:0;font:700 24px/1.4 Tahoma,system-ui,sans-serif;color:var(--text)}
.exv12 .rf-hero p{margin:6px 0 0;font:400 13px/1.7 Tahoma,system-ui,sans-serif;color:var(--text-weak)}
.exv12 .card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin:10px 16px;box-shadow:0 2px 0 var(--card-pressed)}
.exv12 .card b{font:700 14px/1.4 Tahoma,system-ui,sans-serif;color:var(--text)}
.exv12 .kv{font:400 12px/1.5 Tahoma,system-ui,sans-serif}
.exv12 .wrong{background:var(--card-pressed);border:1px solid var(--line);border-radius:12px;padding:9px 11px;font:400 11.5px/1.9 Tahoma,system-ui,sans-serif}
.exv12 .qfoot{position:static;display:flex;flex-wrap:wrap;gap:8px;overflow:visible;margin:14px 16px;padding:0;background:transparent;border:0}
.exv12 .qfoot .btn{font:700 12px/1 Tahoma,system-ui,sans-serif;padding:10px 14px;border-radius:12px;color:var(--text);background:var(--card);border:1px solid var(--line);white-space:nowrap;display:inline-flex;align-items:center;gap:6px}
.exv12 .qfoot .btn:hover{border-color:var(--primary);color:var(--primary)}
'''
rep("</style>", CSS12 + "\n</style>", "inject v12 CSS")

# remove the obsolete v8/v10 "konkur exam skin" + dead .qnav rules (structural break)
rx1(r'/\* ---- v10 · exam surfaces \(unchanged\): MORE Mimo, skin only ---- \*/.*?/\* ---- v8 · no visible code/design annotations',
    '''/* ---- v12 · the separate "konkur exam skin" is GONE; AI screen keeps only these tokens ---- */
.konkur .appbar{background:var(--card);border-bottom:1px solid var(--line);padding:0 16px;height:var(--toolbar);min-height:56px}
.konkur .appbar b{font:700 18px/1.2 system-ui,sans-serif;color:var(--text)}
.konkur .iconbtn{background:var(--card-pressed);border:1px solid var(--line);color:var(--primary)}
.konkur .tag{background:var(--card-pressed);border:1px solid var(--primary);color:var(--primary);border-radius:999px}
/* ---- v8 · no visible code/design annotations''', "clean dead exam CSS")
rx1(r'\.qnav\{[^\n]*\}\n\.qnav \.btn\{[^\n]*\}\n\.qnav \.btn:hover\{[^\n]*\}\n\.qnav \.ic\{[^\n]*\}\n',
    '', "remove dead .qnav CSS")

# ---------------------------------------------------------------------------
# 3. exam-hub: class + Mimo quiz-introduction hero
# ---------------------------------------------------------------------------
rep('<section class="screen konkur" data-screen="exam-hub">',
    '<section class="screen exv12" data-screen="exam-hub" data-code="quiz_introduction_fragment.xml">',
    "exam-hub class")
rep('        <div class="chips">',
    '''        <div class="eh-hero" data-code="quiz_introduction_fragment.xml · iv_quiz_introduction / TextH1 / TextP1">
          <div class="eh-art"><span data-icon="ic_mimo_mascot" data-size="48"></span></div>
          <div><b>آزمونها</b><p>هر آزمون، یک قدم نزدیکتر به هدف کنکور</p></div>
        </div>
        <div class="chips">''', "exam-hub hero")

# ---------------------------------------------------------------------------
# 4. EXAM RUN — full structural rebuild
# ---------------------------------------------------------------------------
NEW_RUN = r'''      <!-- ============ 9. EXAM RUN · Mimo lesson_interactive_multiplechoice (v12) ============ -->
      <section class="screen exv12" data-screen="exam-run" data-code="lesson_interactive_multiplechoice_fragment.xml">
        <!-- chapter_toolbar.xml : 52dp · btn_lesson_close / pb_chapter / btn_lesson_report -->
        <div class="ln" data-code="chapter_toolbar.xml · lesson_progress_navbar_height=52dp · pb_chapter=6dp">
          <button class="ln-x" data-sheet="exitSheet" aria-label="خروج"><span data-icon="ic_close" data-size="24" data-mono="1"></span></button>
          <div class="ln-mid"><b id="examTitle">آزمون جامع کنکور</b><div class="ln-prog" data-code="ProgressBarChapter / progress_bar_chapter.xml"><i id="examProgress" style="width:15%"></i></div></div>
          <button class="timerchip ln-timer" id="timerChip" data-code="timer ONLY inside exam · comprehensive fixed at 270 min"><span data-icon="ic_clock_black_24dp" data-size="16" data-mono="1"></span><span id="timerLabel">تنظیم زمان</span></button>
          <button class="ln-report" data-sheet="paletteSheet" aria-label="پاسخبرگ"><span data-icon="ic_flag" data-size="22" data-mono="1"></span></button>
        </div>

        <!-- ScrollView nsv_multiplechoice_lesson_content / LessonDescriptionView / ChoiceView -->
        <div class="lb-body" data-code="nsv_multiplechoice_lesson_content · layout_lesson_description · lesson_multiplechoice_view">
          <div class="lb-step"><span id="examStep">سؤال ۳ از ۲۰</span><span id="timerStateText">زمان تنظیم نشده</span></div>
          <div class="lb-subject" id="examSubject"><span class="lb-dot"></span>زیست<span class="lb-sep">·</span>سمها<span class="lb-sep">·</span>دشواری متوسط</div>
          <h2 class="qtext" id="qText" data-code="LessonDescriptionView · TextH2 20sp / TextP1 18sp">کدامیک از گزینههای زیر دربارهٔ «سمها» درست است؟ اگر پاسخ را نمیدانید میتوانید علامت بزنید و بعداً برگردید.</h2>
          <div class="lb-hint" data-code="tv_multiplechoice_hint · interaction_hint_single_choice = Tap the correct answer"><span data-icon="ic_help" data-size="14" data-mono="1"></span>گزینهٔ درست را انتخاب کنید</div>
          <div class="lb-choices" id="exChoices" data-code="rv_multiplechoice_options · choice_list_item.xml · layout_choice_card_item.xml">
            <button class="opt" data-opt="1"><span class="opt-radio"></span><span class="opt-txt">گزینهٔ اول</span><span class="opt-num">۱</span></button>
            <button class="opt" data-opt="2"><span class="opt-radio"></span><span class="opt-txt">گزینهٔ دوم</span><span class="opt-num">۲</span></button>
            <button class="opt" data-opt="3"><span class="opt-radio"></span><span class="opt-txt">گزینهٔ سوم</span><span class="opt-num">۳</span></button>
            <button class="opt" data-opt="4"><span class="opt-radio"></span><span class="opt-txt">گزینهٔ چهارم</span><span class="opt-num">۴</span></button>
          </div>
          <div class="lb-feedback" id="exFeedback" hidden data-code="lesson_interactive_feedback_bottom_sheet_dialog.xml">
            <span class="fb-ic" data-icon="ic_check_white" data-size="18" data-mono="1"></span>
            <div><b id="exFeedbackTitle">پاسخ درست است</b><p id="exFeedbackText">توضیح مبحث و ارجاع به کتاب درسی.</p></div>
          </div>
          <div id="examFinished"></div>
          <div class="hint" id="policyHint" hidden></div>
          <div class="lb-tools" data-code="lesson_skip / report_lesson / exam utilities (quiet chips, not a scrolling button bar)">
            <button class="lb-chip" id="answerSheetBtn" data-sheet="paletteSheet"><span data-icon="ic_list_bulleted" data-size="16" data-mono="1"></span>پاسخبرگ</button>
            <button class="lb-chip" id="answerKeyBtn" data-sheet="keySheet"><span data-icon="ic_file" data-size="16" data-mono="1"></span>پاسخنامه</button>
            <button class="lb-chip" id="askAiBtn"><span data-icon="ic_magic_wand" data-size="16" data-mono="1"></span>توضیح با هوش مصنوعی</button>
            <button class="lb-chip" id="endExam"><span data-icon="ic_task_completed" data-size="16" data-mono="1"></span>اتمام آزمون</button>
            <button class="lb-chip" id="timerPause" style="display:none"><span data-icon="ic_play" data-size="16" data-mono="1"></span><span id="timerPauseLabel">توقف</span></button>
            <button class="lb-chip" id="timerReset" style="display:none"><span data-icon="ic_settings" data-size="16" data-mono="1"></span>تنظیم مجدد</button>
            <button class="lb-chip" data-sheet="exitSheet"><span data-icon="ic_close" data-size="16" data-mono="1"></span>خروج</button>
          </div>
        </div>

        <!-- interaction_keyboard_view.xml / run_button_view.xml : NO prev/next pill pair -->
        <div class="lk" data-code="interaction_keyboard_view.xml · interaction_keyboard_height=68dp · run_button_view.xml">
          <div class="lk-row">
            <button class="lk-square" id="prevQ" aria-label="سؤال قبل" data-code="btn_undo · 48dp square"><span data-icon="ic_arrow_back_24" data-size="22" data-mono="1"></span></button>
            <button class="lk-square" id="markQ" aria-label="علامتگذاری" data-code="btn_reset · 48dp square"><span data-icon="bookmark" data-size="20" data-mono="1"></span></button>
            <button class="lk-cta" id="nextQ" data-code="btn_continue_big / btn_submit · lesson_continue=Continue · lesson_submit=Submit"><b id="nextQLabel">ادامه</b><span data-icon="ic_arrow_right" data-size="18" data-mono="1"></span></button>
          </div>
          <button class="lk-skip" id="skipQ" data-code="lesson_skip=Skip">رد کردن سؤال</button>
        </div>
      </section>
'''
rx1(r'      <!-- ============ 9\. EXAM RUN ============ -->.*?      </section>\n\n      <!-- ============ 10\. EXAM RESULT',
    NEW_RUN + '\n      <!-- ============ 10. EXAM RESULT', "exam-run rebuild")

# ---------------------------------------------------------------------------
# 5. EXAM RESULT — Mimo celebration screen
# ---------------------------------------------------------------------------
NEW_RESULT = r'''      <!-- ============ 10. EXAM RESULT · Mimo chapter-finished (v12) ============ -->
      <section class="screen exv12" data-screen="exam-result" data-code="lesson_awesome_fragment.xml / chapter_finished_leaderboard_fragment.xml">
        <div class="ln">
          <button class="ln-x" data-nav="exam-hub" aria-label="بازگشت"><span data-icon="ic_arrow_back_24" data-size="22" data-mono="1"></span></button>
          <div class="ln-mid"><b>نتیجهٔ آزمون</b><div class="ln-prog"><i style="width:100%"></i></div></div>
          <span class="tag" id="resultKind">جامع</span>
        </div>
        <div class="rf-hero" data-code="chapter finished celebration · full-width CTA at bottom">
          <div class="rf-art"><span data-icon="ic_mimo_mascot" data-size="72"></span></div>
          <h2>آزمون تمام شد!</h2>
          <p>۳ سؤال نیاز به مرور دارد. پاسخنامهٔ تشریحی آماده است.</p>
        </div>
        <div class="card">
          <b>نتیجه و تحلیل</b>
          <div class="kv"><span>درصد با نمرهٔ منفی</span><span>۶۸٪</span></div>
          <div class="kv"><span>اگر غلطها نزده میذاشتی</span><span>۷۴٪</span></div>
          <div class="kv"><span>غلط / نزده</span><span>۴ / ۵</span></div>
          <div class="kv"><span>رتبه / تراز</span><span>۱۲۴۰ / ۶۲۰۰</span></div>
        </div>
        <div class="card">
          <b>صورت اشتباهات (منتقلشونده به AI)</b>
          <div class="wrong">سؤال ۲ · زیست / سمها — صورت سؤال: «کدام گزینه دربارهٔ سمها درست است؟» · پاسخ شما: گزینهٔ ۴ · پاسخ صحیح: گزینهٔ ۱</div>
          <div class="wrong">سؤال ۴ · شیمی / تعادل — صورت سؤال: «ثابت تعادل در دمای ثابت…» · پاسخ شما: نزده · پاسخ صحیح: گزینهٔ ۴</div>
          <div class="wrong">سؤال ۹ · فیزیک / ترمودینامیک — صورت سؤال: «کار انجامشده در فرایند همحجم…» · پاسخ شما: گزینهٔ ۲ · پاسخ صحیح: گزینهٔ ۳</div>
        </div>
        <div class="qfoot result-foot">
          <button class="btn" id="resultBargBtn" data-sheet="paletteSheet"><span data-icon="ic_list_bulleted" data-size="15" data-mono="1"></span>پاسخبرگ</button>
          <button class="btn" id="resultKeyBtn" data-sheet="keySheet"><span data-icon="ic_file" data-size="15" data-mono="1"></span>پاسخنامه</button>
          <button class="btn" id="askAiResultBtn"><span data-icon="ic_magic_wand" data-size="15" data-mono="1"></span>توضیح با هوش مصنوعی</button>
        </div>
      </section>
'''
rx1(r'      <!-- ============ 10\. EXAM RESULT ============ -->.*?      </section>\n\n      <!-- ============ 11\. AI CHAT',
    NEW_RESULT + '\n      <!-- ============ 11. AI CHAT', "exam-result rebuild")

# ---------------------------------------------------------------------------
# 6. JS — real Mimo question flow (submit → feedback → continue), keep all IDs
# ---------------------------------------------------------------------------
rep('    q("#examFinished").innerHTML="";resetOptions();T.state="idle";clearInterval(T.timer);T.timer=null;\n    applyPolicy();go("exam-run");',
    '    q("#examFinished").innerHTML="";resetOptions();renderQuestion();T.state="idle";clearInterval(T.timer);T.timer=null;\n    applyPolicy();go("exam-run");',
    "nodek handler")

rep('q("#timerPause").textContent="توقف"', 'q("#timerPauseLabel").textContent="توقف"', "pause label 1")
rep('q("#timerPause").textContent="ادامه"', 'q("#timerPauseLabel").textContent="ادامه"', "pause label 2")

OLD_HANDLERS = '''  function resetOptions(){qa(".opt").forEach(function(o){o.style.pointerEvents="";o.style.opacity="";o.classList.remove("on")})}
  qa(".opt").forEach(function(o){o.addEventListener("click",function(){if(T.state==="finished")return;qa(".opt").forEach(function(x){x.classList.remove("on")});o.classList.add("on")})});
  q("#nextQ").addEventListener("click",function(){toast("سؤال بعدی (همان چیدمان lesson_interactive میمو)")});
  q("#prevQ").addEventListener("click",function(){toast("سؤال قبل (همان چیدمان lesson_interactive میمو)")});
'''
NEW_HANDLERS = r'''  function resetOptions(){qa(".opt").forEach(function(o){o.style.pointerEvents="";o.style.opacity="";o.classList.remove("on","correct","wrong")})}
  /* ============ v12 · Mimo lesson_interactive question flow ============
     ChoiceView selection -> btn_submit (بررسی پاسخ) -> feedback bottom sheet
     -> btn_continue_big (ادامه) -> next question.  btn_undo = سؤال قبل (48dp square).
     No equal-weight prev/next pill pair any more (interaction_keyboard_view.xml). */
  var QBANK=[
    {sub:"زیست · سمها · دشواری متوسط",stem:"کدامیک از گزینههای زیر دربارهٔ «سمها» درست است؟",
     opts:["سمها همواره تنها در کبد ساخته میشوند","سمها میتوانند با اتصال به آنزیمها، فعالیت آنها را مهار کنند","همهٔ سمها در بدن به گلوکز تبدیل میشوند","سمها فقط از راه پوست وارد بدن میشوند"],ok:1,
     expl:"سمها با اتصال به جایگاه فعال آنزیمها میتوانند آنها را مهار کنند؛ زیست یازدهم، فصل سمها و بیماریها."},
    {sub:"شیمی · تعادل شیمیایی · دشواری متوسط",stem:"ثابت تعادل یک واکنش برگشتپذیر در دمای ثابت، با افزایش غلظت یکی از واکنشدهندهها…",
     opts:["کاهش مییابد","افزایش مییابد","تغییر نمیکند","صفر میشود"],ok:2,
     expl:"Kc فقط تابع دماست؛ تغییر غلظت، سامانه را جابهجا میکند ولی مقدار ثابت تعادل ثابت میماند (اصل لوشاتلیه)."},
    {sub:"فیزیک · ترمودینامیک · دشواری سخت",stem:"کار انجامشده توسط گاز در یک فرایند همحجم برابر است با…",
     opts:["PΔV","صفر","nRΔT","ΔU"],ok:1,
     expl:"در فرایند همحجم ΔV=۰ است، پس W=PΔV=۰ و تمام گرما صرف تغییر انرژی درونی میشود."},
    {sub:"ریاضی · مشتق · دشواری متوسط",stem:"مشتق تابع f(x)=x³-3x در x=۱ کدام است؟",
     opts:["۰","۱","۳","۶"],ok:0,
     expl:"f′(x)=3x²-3، پس f′(1)=0؛ نقطهٔ بحرانی و اکسترمم نسبی."},
    {sub:"زیست · ژنتیک · دشواری آسان",stem:"در قانون دوم مندل (تفکیک)، نسبت ژنوتیپی نسل F₂ برای یک صفت تکژنی چیست؟",
     opts:["۳:۱","۱:۲:۱","۹:۳:۳:۱","۱:۱"],ok:1,
     expl:"نسبت فنوتیپی ۳:۱ و نسبت ژنوتیپی ۱:۲:۱ است (AA:Aa:aa)."}
  ];
  var QI=2,QCHECKED=false;
  function renderQuestion(){
    var item=QBANK[QI%QBANK.length];
    q("#examStep").textContent="سؤال "+fa(QI+1)+" از ۲۰";
    q("#examSubject").innerHTML='<span class="lb-dot"></span>'+esc(item.sub.split(" · ")[0])+'<span class="lb-sep">·</span>'+esc(item.sub.split(" · ")[1])+'<span class="lb-sep">·</span>'+esc(item.sub.split(" · ")[2]);
    q("#qText").textContent=item.stem;
    qa("#exChoices .opt").forEach(function(o,i){o.querySelector(".opt-txt").textContent=item.opts[i]});
    resetOptions();q("#exFeedback").hidden=true;QCHECKED=false;
    q("#nextQLabel").textContent="ادامه";
    q("#examProgress").style.width=Math.min(100,((QI+1)/20)*100)+"%";
    q("#markQ").classList.remove("marked");
    paintIcons(q("#examSubject"));
  }
  function setCtaLabel(){q("#nextQLabel").textContent=(q(".opt.on")&&!QCHECKED)?"بررسی پاسخ":"ادامه"}
  qa(".opt").forEach(function(o){o.addEventListener("click",function(){
    if(T.state==="finished")return;
    qa(".opt").forEach(function(x){x.classList.remove("on","correct","wrong")});
    o.classList.add("on");QCHECKED=false;q("#exFeedback").hidden=true;setCtaLabel();
  })});
  q("#nextQ").addEventListener("click",function(){
    var chosen=q(".opt.on");
    if(chosen&&!QCHECKED){
      var item=QBANK[QI%QBANK.length];
      var ok=+chosen.dataset.opt-1===item.ok;
      QCHECKED=true;
      chosen.classList.remove("on");chosen.classList.add(ok?"correct":"wrong");
      var fb=q("#exFeedback");fb.classList.toggle("bad",!ok);fb.hidden=false;
      q("#exFeedbackTitle").textContent=ok?"پاسخ درست است":"پاسخ نادرست است";
      q("#exFeedbackText").textContent=item.expl;
      q("#nextQLabel").textContent="ادامه";toast(ok?"درست ✔ پاسخنامهٔ تشریحی نشان داده شد":"نادرست ✕ توضیح مبحث نشان داده شد");
      return;
    }
    QI=Math.min(19,QI+1);renderQuestion();toast("سؤال بعدی · "+fa(QI+1)+" از ۲۰");
  });
  q("#prevQ").addEventListener("click",function(){QI=Math.max(0,QI-1);renderQuestion();toast("سؤال قبل · "+fa(QI+1)+" از ۲۰")});
  q("#skipQ").addEventListener("click",function(){QI=Math.min(19,QI+1);renderQuestion();toast("سؤال رد شد")});
  q("#markQ").addEventListener("click",function(){q("#markQ").classList.toggle("marked");toast(q("#markQ").classList.contains("marked")?"سؤال علامتگذاری شد":"علامت برداشته شد")});
  renderQuestion();
'''
rep(OLD_HANDLERS, NEW_HANDLERS, "question flow")

# ---------------------------------------------------------------------------
# 7. chrome / docs text -> round 12
# ---------------------------------------------------------------------------
rep("<title>طرح رابط کاربری v10 — معماری اورجینال قوسدار مسیر یادگیری (Design Review)</title>",
    "<title>طرح رابط کاربری v12 — سطوح آزمون بر اساس lesson_interactive میمو (Design Review)</title>", "title")
rep("<h1>طرح رابط کاربری — دور یازدهم <span class=\"ver\">DESIGN v11 · REVIEW</span></h1>",
    "<h1>طرح رابط کاربری — دور دوازدهم <span class=\"ver\">DESIGN v12 · REVIEW</span></h1>", "h1")
old_p = html[html.index("<p>بازآفرینی ۱۰۰٪"):html.index("</p>", html.index("<p>بازآفرینی ۱۰۰٪")) + 4]
rep(old_p,
    "<p>بازآفرینی ۱۰۰٪ بخشهای اصلی میمو <b>از روی کد/مهندسی معکوس</b> · <b>دور دوازدهم:</b> "
    "سطوح آزمون از روی لایههای واقعی میمو بازسازی شدند: <code>chapter_toolbar.xml</code> (X + نوار پیشرفت ۶dp + پرچم)، "
    "<code>lesson_interactive_multiplechoice_fragment.xml</code>، <code>choice_list_item.xml</code> و "
    "<code>interaction_keyboard_view.xml</code> (<b>یک دکمهٔ بنفش تمامعرض CONTINUE</b> + دکمههای مربعی ۴۸dp). "
    "دو دکمهٔ هموزن «سؤال قبل / سؤال بعد» و نوار ۷ دکمهای حذف شدند؛ پاسخبرگ، پاسخنامه، AI و تایمر در ردیف چیپهای آرام و پاسخنامهٔ تشریحی بهصورت پنل feedback میمو نمایش داده میشوند. "
    "معماری اورجینال قوسدار، ۵ تب، ۷ بخش آزمون، ۲۷۰ دقیقهٔ ثابت و قفلها دستنخوردهاند. اسکرینشاتها فقط چک بصری.</p>",
    "header paragraph")
rep("⚠️ این <b>طرح دور یازدهم v11</b> است، نه محصول.",
    "⚠️ این <b>طرح دور دوازدهم v12</b> است، نه محصول.", "footer lead")
rep("در دور یازدهم محتوای لیدربورد/مسیرها/کورسها کنکوری و بدون نشانهای برنامهنویسی شد.",
    "در دور یازدهم محتوای لیدربورد/مسیرها/کورسها کنکوری و بدون نشانهای برنامهنویسی شد. "
    "در دور دوازدهم سطوح آزمون با معماری واقعی صفحهٔ درس/کوییز میمو هماهنگ شدند.", "footer paragraph")

rep('<aside class="spec">\n    <h3>دور یازدهم', '''<aside class="spec">
    <h3>دور دوازدهم · آزمونها روی معماری واقعی صفحهٔ درس میمو</h3>
    <ul>
      <li><b>کد مبنا:</b> <code>chapter_toolbar.xml</code> (۵۲dp: <code>btn_lesson_close</code> / <code>pb_chapter</code> ۶dp / <code>btn_lesson_report</code>)، <code>lesson_interactive_multiplechoice_fragment.xml</code>، <code>choice_view.xml</code>، <code>choice_list_item.xml</code>، <code>layout_choice_card_item.xml</code>، <code>interaction_keyboard_view.xml</code>، <code>run_button_view.xml</code>، <code>lesson_interactive_feedback_bottom_sheet_dialog.xml</code>، <code>quiz_introduction_fragment.xml</code>. شواهد کامل: <code>DESIGN/EXAM_UI_CODE_EVIDENCE.json</code>.</li>
      <li><b>اصلاح دکمهها:</b> دو دکمهٔ هموزن <code>.qnav</code> («سؤال قبل» + «سؤال بعد») و نوار ۷ دکمهای <code>.qfoot</code> بطور کامل حذف شدند. حالا <b>یک دکمهٔ بنفش تمامعرض</b> (<code>btn_continue_big</code> / <code>btn_submit</code>) + یک دکمهٔ مربعی ۴۸dp برای «سؤال قبل» (<code>btn_undo</code>) + یک مربع ۴۸dp علامتگذاری (<code>btn_reset</code>) داخل فوتر ۶۸dp قرار دارند؛ «رد کردن سؤال» هم از <code>lesson_skip</code> آمده.</li>
      <li><b>چرخهٔ واقعی:</b> انتخاب گزینه ← «بررسی پاسخ» (<code>lesson_submit</code>) ← پنل feedback سبز/قرمز با توضیح مبحث ← «ادامه» (<code>lesson_continue</code>) ← سؤال بعد. گزینهها همان <code>multiplechoice_background_selected/correct/wrong</code> با شعاع ۱۲dp و حاشیهٔ ۲dpاند.</li>
      <li><b>هماهنگی پوسته:</b> کلاس جداگانهٔ <code>konkur</code> از سه صفحهٔ آزمون برداشته شد؛ همان توکنهای ARSC، همان وکتورها، همان تایپوگرافی. هاب آزمونها به ردیفهای لیستی میمو + کارت معرفی <code>quiz_introduction</code> تبدیل شد و نتیجه به صفحهٔ celebration میمو.</li>
      <li><b>بدون تغییر:</b> ۵ تب و <code>MAX</code> ممنوع · ۷ بخش لیبلدار + قالبها + پاسخنامهٔ تشریحی · تنها قفل «آزمون نهایی / دو هفتگی» · ۲۷۰ دقیقهٔ ثابت · تایمر فقط داخل آزمون · «پاسخبرگ»≠«پاسخنامه» · تکدکمهٔ AI · <code>section-practice</code> جدا · معماری قوسدار اورجینال.</li>
      <li>اسکرینشات <code>mimo-04-lesson-continue.jpg</code> فقط <b>چک بصری</b>؛ حکم نهایی از XML/DEX/ARSC است. در صورت نپسندیدن، <code>tools/design_v11_full.html</code> مسیر برگشت است.</li>
    </ul>
    <h3>دور یازدهم''', "aside v12")

# ---------------------------------------------------------------------------
# 8. outputs
# ---------------------------------------------------------------------------
(TOOLS / "design_v12_template.html").write_text(html, encoding="utf-8")
(DESIGN / "index.html").write_text(html, encoding="utf-8")
print(json.dumps({
    "output": str(DESIGN / "index.html"),
    "bytes": len(html.encode("utf-8")),
    "source": str(SRC),
    "exam_run_rebuilt": 'class="ln"' in html and 'id="nextQ"' in html and 'id="prevQ"' in html,
    "old_qnav_removed": 'class="qnav"' not in html and 'id="prevQ"' in html,
    "old_equal_pills_removed": "سؤال قبل</button>" not in html,
    "full_width_cta": "lk-cta" in html and "btn_continue_big" in html,
    "mimo_choice_cards": "lb-choices" in html and "opt-radio" in html,
    "feedback_panel": "exFeedback" in html,
    "hub_rows": "eh-hero" in html and html.count('class="cat-meta"') == 7,
    "code_evidence": str(DESIGN / "EXAM_UI_CODE_EVIDENCE.json"),
    "curved_zigzag_kept": "M242 70 H280 Q312 70 312 102 V140" in html,
    "method": "CODE_FIRST / decoded APK layouts; screenshots VISUAL_CROSSCHECK_ONLY",
}, ensure_ascii=False, indent=2))
