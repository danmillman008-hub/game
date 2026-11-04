#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_exam_v12_4.py — remove the extra exam buttons; ONE timer chip.

Starts from the accepted v12.3 / v12.1 exam structure (tools/design_v12_3_template.html)
and applies exactly what the user asked for, nothing structural:

  * remove the chips «توضیح با هوش مصنوعی» / «اتمام آزمون» / «خروج» from the tool row
    (the X in the chapter toolbar already exits; exam ends from پاسخبرگ ← ثبت پاسخها;
     the AI explanation moves into the پاسخنامه sheet where it belongs),
  * remove «رد کردن سؤال» — «ادامه» with nothing selected already skips,
  * remove «زمان تنظیم نشده» (duplicate of the timer chip label),
  * remove the flag button next to the timer (it made the timer hard to tap),
  * remove the option radio circle: each option just starts with «۱.», and the whole
    card changes colour when selected,
  * remove the separate «توقف» / «تنظیم مجدد» chips: while running, the SAME timer
    chip grows a compact play/pause + stop pair next to the countdown. Tapping the
    timer itself pauses/resumes.

Code-first from decoded APK vectors; screenshots VISUAL_CROSSCHECK_ONLY.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

UP = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
TOOLS, DESIGN = UP / "tools", UP / "DESIGN"
html = (TOOLS / "design_v12_3_template.html").read_text(encoding="utf-8")


def rep(old: str, new: str, label: str, count: int = 1):
    global html
    n = html.count(old)
    if n != count:
        raise SystemExit("%s matched %d times (expected %d)" % (label, n, count))
    html = html.replace(old, new, count)


# ---------------------------------------------------------------------------
# 1. CSS: no flag button, one timer chip with inline controls, no radio circles
# ---------------------------------------------------------------------------
rep('.exv12 .ln-x,.exv12 .ln-report{width:40px;height:40px;flex:0 0 40px;border:0;background:transparent;color:var(--weak-icon);display:inline-flex;align-items:center;justify-content:center;padding:0}',
    '.exv12 .ln-x{width:40px;height:40px;flex:0 0 40px;border:0;background:transparent;color:var(--weak-icon);display:inline-flex;align-items:center;justify-content:center;padding:0}',
    "ln-x CSS (flag removed)")
rep('.exv12 .ln-x:hover,.exv12 .ln-report:hover{color:var(--primary)}',
    '.exv12 .ln-x:hover{color:var(--primary)}', "ln-x hover CSS")

rep('.exv12 .ln-timer{flex:0 0 auto;font:700 10px/1 Tahoma,system-ui,sans-serif;padding:5px 8px;gap:4px}',
    r'''.exv12 .ln-timer{flex:0 0 auto;font:700 11px/1 Tahoma,system-ui,sans-serif;padding:3px 6px;gap:0}
.exv12 .tm-main{border:0;background:transparent;color:inherit;display:inline-flex;align-items:center;gap:5px;padding:2px 4px;font:inherit;white-space:nowrap}
.exv12 .tm-main:hover{color:var(--primary)}
.exv12 .tm-controls{display:inline-flex;align-items:center;gap:3px;border-inline-start:1px solid currentColor;padding-inline-start:6px;margin-inline-start:4px;opacity:.9}
.exv12 .tm-btn{width:22px;height:22px;flex:0 0 22px;border:0;border-radius:7px;background:rgba(37,39,70,.09);color:inherit;display:inline-flex;align-items:center;justify-content:center;padding:0}
.exv12 .tm-btn:hover{background:var(--primary);color:#fff}
.exv12 .tm-bars{display:block;width:3px;height:10px;background:currentColor;transform:translateX(-3px);box-shadow:6px 0 0 currentColor}
.exv12 .tm-play svg{display:block}
.exv12 .tm-square{display:block;width:9px;height:9px;border-radius:2px;background:currentColor}''',
    "one-chip timer CSS")

OLD_OPT_CSS = r'''.exv12 .opt-radio{width:20px;height:20px;flex:0 0 20px;border:2px solid var(--weak-icon);border-radius:999px;display:inline-flex;align-items:center;justify-content:center}
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
.exv12 .opt.wrong .opt-radio:after{content:"";width:8px;height:8px;border-radius:999px;background:#fff}'''
NEW_OPT_CSS = r'''.exv12 .opt-num{font:700 15px/1 Tahoma,system-ui,sans-serif;color:var(--text-weak);flex:0 0 auto;min-width:20px}
.exv12 .opt-txt{flex:1}
.exv12 .opt.on{border-color:var(--blue);background:var(--card-pressed)}
.exv12 .opt.on .opt-num{color:var(--primary)}
.exv12 .opt.correct{border-color:var(--success);background:var(--card)}
.exv12 .opt.correct .opt-num{color:var(--success)}
.exv12 .opt.wrong{border-color:var(--error);background:var(--card)}
.exv12 .opt.wrong .opt-num{color:var(--error)}'''
rep(OLD_OPT_CSS, NEW_OPT_CSS, "option CSS: no radio circle")
rep('.exv12 .lk-skip{align-self:center;border:0;background:transparent;color:var(--text-weak);font:400 11px/1 Tahoma,system-ui,sans-serif;text-decoration:underline;padding:2px 6px}\n',
    '', "lk-skip CSS removed")

# ---------------------------------------------------------------------------
# 2. chapter toolbar: ONE timer chip, NO flag
# ---------------------------------------------------------------------------
rep('''          <button class="timerchip ln-timer" id="timerChip" data-code="timer ONLY inside exam · comprehensive fixed at 270 min"><span data-icon="ic_clock_black_24dp" data-size="16" data-mono="1"></span><span id="timerLabel">تنظیم زمان</span></button>
          <button class="ln-report" data-sheet="paletteSheet" aria-label="پاسخبرگ"><span data-icon="ic_flag" data-size="22" data-mono="1"></span></button>''',
'''          <div class="timerchip ln-timer" id="timerWrap" data-code="timer ONLY inside exam · ONE chip: tap to set / pause / resume · comprehensive fixed 270 min">
            <button class="tm-main" id="timerChip" aria-label="تنظیم زمان"><span data-icon="ic_clock_black_24dp" data-size="16" data-mono="1"></span><span id="timerLabel">تنظیم زمان</span></button>
            <span class="tm-controls" id="timerControls" hidden>
              <button class="tm-btn" id="timerPause" aria-label="توقف تایمر"><span class="tm-bars"></span><span class="tm-play" data-icon="ic_play" data-size="12" data-mono="1" hidden></span></button>
              <button class="tm-btn" id="timerReset" aria-label="پاک کردن تایمر"><span class="tm-square"></span></button>
            </span>
          </div>''', "toolbar timer group")

# ---------------------------------------------------------------------------
# 3. one status line only
# ---------------------------------------------------------------------------
rep('<div class="lb-step"><span id="examStep">سؤال ۱ از ۲۰</span><span id="timerStateText">زمان تنظیم نشده</span></div>',
    '<div class="lb-step"><span id="examStep">سؤال ۱ از ۲۰</span></div>',
    "duplicate timer status removed")

# ---------------------------------------------------------------------------
# 4. options start with «۱.» — no radio circle
# ---------------------------------------------------------------------------
for i, word in enumerate(["اول", "دوم", "سوم", "چهارم"], 1):
    d = "۱۲۳۴"[i - 1]
    rep('<button class="opt" data-opt="%d"><span class="opt-radio"></span><span class="opt-txt">گزینهٔ %s</span><span class="opt-num">%s</span></button>'
        % (i, word, d),
        '<button class="opt" data-opt="%d"><span class="opt-num">%s.</span><span class="opt-txt">گزینهٔ %s</span></button>'
        % (i, d, word),
        "option %d" % i)

# ---------------------------------------------------------------------------
# 5. tool chips: only پاسخبرگ / پاسخنامه
# ---------------------------------------------------------------------------
OLD_TOOLS = r'''          <div class="lb-tools" data-code="lesson_skip / report_lesson / exam utilities (quiet chips, not a scrolling button bar)">
            <button class="lb-chip" id="answerSheetBtn" data-sheet="paletteSheet"><span data-icon="ic_list_bulleted" data-size="16" data-mono="1"></span>پاسخبرگ</button>
            <button class="lb-chip" id="answerKeyBtn" data-sheet="keySheet"><span data-icon="ic_file" data-size="16" data-mono="1"></span>پاسخنامه</button>
            <button class="lb-chip" id="askAiBtn"><span data-icon="ic_magic_wand" data-size="16" data-mono="1"></span>توضیح با هوش مصنوعی</button>
            <button class="lb-chip" id="endExam"><span data-icon="ic_task_completed" data-size="16" data-mono="1"></span>اتمام آزمون</button>
            <button class="lb-chip" id="timerPause" style="display:none"><span data-icon="ic_play" data-size="16" data-mono="1"></span><span id="timerPauseLabel">توقف</span></button>
            <button class="lb-chip" id="timerReset" style="display:none"><span data-icon="ic_settings" data-size="16" data-mono="1"></span>تنظیم مجدد</button>
            <button class="lb-chip" data-sheet="exitSheet"><span data-icon="ic_close" data-size="16" data-mono="1"></span>خروج</button>
          </div>'''
NEW_TOOLS = r'''          <div class="lb-tools" data-code="only پاسخبرگ / پاسخنامه chips remain · exit via chapter-toolbar X · end exam via پاسخبرگ · AI via پاسخنامه">
            <button class="lb-chip" id="answerSheetBtn" data-sheet="paletteSheet"><span data-icon="ic_list_bulleted" data-size="16" data-mono="1"></span>پاسخبرگ</button>
            <button class="lb-chip" id="answerKeyBtn" data-sheet="keySheet"><span data-icon="ic_file" data-size="16" data-mono="1"></span>پاسخنامه</button>
          </div>'''
rep(OLD_TOOLS, NEW_TOOLS, "tool chips")

# AI action lives in the answer-key sheet, where an explanation belongs
rep('<div class="krow" style="margin:12px 0 0"><button class="btn primary" data-close="keySheet">بستن</button></div>',
    '<div class="krow" style="margin:12px 0 0"><button class="btn primary" data-close="keySheet">بستن</button><button class="btn" id="askAiBtn"><span data-icon="ic_magic_wand" data-size="14" data-mono="1"></span>توضیح با هوش مصنوعی</button></div>',
    "AI button moved into پاسخنامه sheet")

# ---------------------------------------------------------------------------
# 6. footer: remove «رد کردن سؤال»
# ---------------------------------------------------------------------------
rep('''        <div class="lk" data-code="interaction_keyboard_view.xml · interaction_keyboard_height=68dp · run_button_view.xml">''',
    '''        <div class="lk" data-code="interaction_keyboard_view.xml · run_button_view.xml · lesson_skip=Skip is handled by «ادامه» with no selection">''',
    "lk data-code keeps lesson_skip evidence")
rep('''          <button class="lk-skip" id="skipQ" data-code="lesson_skip=Skip">رد کردن سؤال</button>
''', '', "skip link removed")

# ---------------------------------------------------------------------------
# 7. JS: timer state machine + remove handlers for deleted buttons
# ---------------------------------------------------------------------------
OLD_T = r'''  /* ---------- timer state machine ---------- */
  var T={state:"idle",remaining:0,total:0,timer:null,endAt:0};
  var chip=q("#timerChip"),label=q("#timerLabel"),stateText=q("#timerStateText");
  function fmt(s){var m=Math.floor(s/60),x=s%60;return fa(("0"+m).slice(-2))+":"+fa(("0"+x).slice(-2))}
  function render(){
    chip.classList.remove("running","finished");
    if(T.state==="idle"){label.textContent="تنظیم زمان";stateText.textContent="زمان تنظیم نشده";q("#timerPause").style.display="none";q("#timerReset").style.display="none"}
    else if(T.state==="setting"){label.textContent="تنظیم زمان";stateText.textContent="در حال تنظیم";q("#timerPause").style.display="none";q("#timerReset").style.display="none"}
    else if(T.state==="running"){label.textContent=fmt(T.remaining);chip.classList.add("running");stateText.textContent="زمان معکوس در حال اجرا";q("#timerPause").style.display="";q("#timerReset").style.display="";q("#timerPauseLabel").textContent="توقف"}
    else if(T.state==="paused"){label.textContent=fmt(T.remaining);stateText.textContent="متوقف شده";q("#timerPause").style.display="";q("#timerReset").style.display="";q("#timerPauseLabel").textContent="ادامه"}
    else if(T.state==="finished"){label.textContent=fmt(0);chip.classList.add("finished");stateText.textContent="زمان تمام شد";q("#timerPause").style.display="none";q("#timerReset").style.display=""}
  }'''
NEW_T = r'''  /* ---------- timer state machine · v12.4: ONE chip, no extra control chips ---------- */
  var T={state:"idle",remaining:0,total:0,timer:null,endAt:0};
  var wrap=q("#timerWrap"),chip=q("#timerChip"),label=q("#timerLabel"),ctl=q("#timerControls");
  function fmt(s){var m=Math.floor(s/60),x=s%60;return fa(("0"+m).slice(-2))+":"+fa(("0"+x).slice(-2))}
  function pauseOrResume(){
    if(T.state==="running"){T.remaining=Math.max(0,Math.ceil((T.endAt-Date.now())/1000));T.state="paused";clearInterval(T.timer);T.timer=null;toast("تایمر متوقف شد")}
    else if(T.state==="paused"){T.endAt=Date.now()+T.remaining*1000;T.state="running";T.timer=setInterval(tick,250);toast("ادامهٔ تایمر")}
    render();
  }
  function render(){
    wrap.classList.remove("running","finished");
    var pb=q("#timerPause"),bars=pb.querySelector(".tm-bars"),play=pb.querySelector(".tm-play");
    if(T.state==="idle"||T.state==="setting"){label.textContent="تنظیم زمان";ctl.hidden=true}
    else if(T.state==="running"){
      label.textContent=fmt(T.remaining);wrap.classList.add("running");ctl.hidden=false;
      pb.classList.remove("is-paused");pb.setAttribute("aria-label","توقف تایمر");bars.hidden=false;play.hidden=true;
    } else if(T.state==="paused"){
      label.textContent=fmt(T.remaining);wrap.classList.add("running");ctl.hidden=false;
      pb.classList.add("is-paused");pb.setAttribute("aria-label","ادامهٔ تایمر");bars.hidden=true;play.hidden=false;
    } else if(T.state==="finished"){label.textContent=fmt(0);wrap.classList.add("finished");ctl.hidden=true}
  }'''
rep(OLD_T, NEW_T, "timer render()")

rep('''  chip.addEventListener("click",function(){
    if(T.state==="running"||T.state==="paused"){toast("تایمر در حال اجراست؛ از «تنظیم مجدد» استفاده کنید");return}
    q("#timerSheet").classList.add("on");T.state="setting";''',
'''  chip.addEventListener("click",function(){
    if(T.state==="running"||T.state==="paused"){pauseOrResume();return}
    q("#timerSheet").classList.add("on");T.state="setting";''',
    "timer chip click = pause/resume when running")

rep('''  q("#timerPause").addEventListener("click",function(){
    if(T.state==="running"){T.remaining=Math.max(0,Math.ceil((T.endAt-Date.now())/1000));T.state="paused";clearInterval(T.timer);T.timer=null;toast("تایمر متوقف شد")}
    else if(T.state==="paused"){T.endAt=Date.now()+T.remaining*1000;T.state="running";T.timer=setInterval(tick,250);toast("ادامهٔ تایمر")}render();
  });
  q("#timerReset").addEventListener("click",function(){
    clearInterval(T.timer);T.timer=null;T.state="idle";T.remaining=0;T.total=0;
    q("#examFinished").innerHTML="";resetOptions();q("#timerSheet").classList.add("on");toast("زمان پاک شد — دوباره عدد بدهید");render();
  });''',
'''  q("#timerPause").addEventListener("click",function(e){e.stopPropagation();pauseOrResume()});
  q("#timerReset").addEventListener("click",function(e){
    e.stopPropagation();clearInterval(T.timer);T.timer=null;T.state="idle";T.remaining=0;T.total=0;
    q("#examFinished").innerHTML="";resetOptions();q("#timerSheet").classList.remove("on");
    toast("تایمر پاک شد");render();
  });''',
    "inline pause/stop handlers")

rep('''    T.state="idle";clearInterval(T.timer);T.timer=null;
    applyPolicy();go("exam-run");''',
'''    T.state="idle";clearInterval(T.timer);T.timer=null;render();
    applyPolicy();go("exam-run");''',
    "openExam resets the chip")

rep('''  q("#skipQ").addEventListener("click",function(){QI=Math.min(QTOTAL-1,QI+1);renderQuestion();toast("سؤال رد شد")});
''', '', "skipQ handler removed")
rep('''  q("#endExam").addEventListener("click",function(){finishExam("آزمون به پایان رسید")});
''', '', "endExam handler removed")

# ---------------------------------------------------------------------------
# 8. chrome text only (review document)
# ---------------------------------------------------------------------------
rep('<title>طرح رابط کاربری v12.3 — بازگشت به ساختار تأییدشدهٔ صفحهٔ آزمون + فلشهای RTL (Design Review)</title>',
    '<title>طرح رابط کاربری v12.4 — حذف دکمههای اضافی صفحهٔ آزمون + تایمر تکدکمهای (Design Review)</title>', "title")
rep('<h1>طرح رابط کاربری — دور دوازدهم <span class="ver">DESIGN v12.3 · REVIEW</span></h1>',
    '<h1>طرح رابط کاربری — دور دوازدهم <span class="ver">DESIGN v12.4 · REVIEW</span></h1>', "h1")
rep('⚠️ این <b>طرح دور دوازدهم v12.3</b> است، نه محصول.',
    '⚠️ این <b>طرح دور دوازدهم v12.4</b> است، نه محصول.', "footer lead")
rep('و فلشها در RTL اصلاح شدند (بعدی ←، قبلی/بازگشت →). نسخههای',
    'و فلشها در RTL اصلاح شدند (بعدی ←، قبلی/بازگشت →). <b>v12.4:</b> چیپهای «توضیح با هوش مصنوعی / اتمام آزمون / خروج / توقف / تنظیم مجدد»، پرچم کنار تایمر، «رد کردن سؤال»، متن تکراری «زمان تنظیم نشده» و دایرهٔ رادیویی گزینهها حذف شدند؛ تایمر حالا <b>یک دکمهٔ واحد</b> است که کنار زمانش علامت توقف/پلی و استاپ میگیرد. نسخههای',
    "footer v12.4 note")

# ---------------------------------------------------------------------------
# 9. sanity
# ---------------------------------------------------------------------------
for bad in ['id="timerStateText"', 'id="skipQ"', 'id="endExam"', 'class="ln-report"',
            'class="opt-radio"', 'id="timerPauseLabel"', 'class="lk-skip"']:
    assert bad not in html, bad
assert html.count('id="askAiBtn"') == 1
assert html.count('class="lb-chip"') == 2
erb = re.search(r'<section class="screen exv12" data-screen="exam-run".*?</section>', html, re.S).group(0)
assert 'data-icon="ic_flag"' not in erb and 'class="ln-report"' not in erb
assert html.count('class="tm-controls"') == 1
assert 'id="timerWrap"' in html and 'lesson_skip' in html
assert html.count('class="screen exv12"') == 3

(TOOLS / "design_v12_4_template.html").write_text(html, encoding="utf-8")
(DESIGN / "index.html").write_text(html, encoding="utf-8")
print(json.dumps({
    "output": str(DESIGN / "index.html"), "bytes": len(html.encode("utf-8")),
    "source": str(TOOLS / "design_v12_3_template.html"),
    "tool_chips": html.count('class="lb-chip"'),
    "one_timer_chip": 'id="timerWrap"' in html,
    "no_flag": 'data-icon="ic_flag"' not in erb,
    "no_radio": 'opt-radio' not in html,
    "no_skip_link": 'id="skipQ"' not in html,
    "no_duplicate_timer_status": 'id="timerStateText"' not in html,
    "ai_in_answer_key_sheet": html.count('id="askAiBtn"') == 1,
}, ensure_ascii=False, indent=2))
