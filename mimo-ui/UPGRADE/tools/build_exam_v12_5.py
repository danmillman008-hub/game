#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_exam_v12_5.py — user corrections over v12.4 (REVIEW / prototype only).

1. «توضیح با هوش مصنوعی» goes back into the exam body as the THIRD .lb-chip,
   exactly the v12.1 / v12.3 position + style (ic_magic_wand, 16dp, mono),
   beside پاسخبرگ / پاسخنامه.  The v12.4 duplicate inside #keySheet is removed.
2. #timerMinutes is editable in EVERY exam kind (no readOnly / no «غیرقابل تغییر»).
   270 stays only as the comprehensive default/preset; the 6 quick presets stay.
3. #exitSheet gets a third option «پایان آزمون و دیدن کارنامه» (خروج و دیدن درصد):
   a partial کارنامه computed from the answers given so far.
   «خروج و ذخیره» now really saves QI / answers / marks / timer and can be
   resumed later; finishing after a resume yields the full کارنامه.

Everything else from v12.4 (accepted v12.1 structure, v12.3 RTL arrows, the
removed extra chips, one timer chip, number-only options) is untouched.

Reads tools/design_v12_4_template.html, writes tools/design_v12_5_template.html
and DESIGN/index.html.  Idempotent: always starts from the v12.4 template.
"""
from __future__ import annotations
import sys
from pathlib import Path

UP = Path(__file__).resolve().parents[1]
TOOLS = UP / "tools"
SRC = TOOLS / "design_v12_4_template.html"

s = SRC.read_text(encoding="utf-8")
n = 0


def rep(old: str, new: str, count: int = 1) -> None:
    """Exact, asserted replacement — fail loudly if the source drifts."""
    global s, n
    got = s.count(old)
    assert got == count, f"expected {count} match(es), got {got}: {old[:110]!r}"
    s = s.replace(old, new, count)
    n += 1


# ---------------------------------------------------------------- 1. chrome / labels
rep(
    '<title>طرح رابط کاربری v12.4 — حذف دکمههای اضافی صفحهٔ آزمون + تایمر تکدکمهای (Design Review)</title>',
    '<title>طرح رابط کاربری v12.5 — بازگشت چیپ AI + مدت دستی در همهٔ آزمونها + گزینهٔ سوم خروج و کارنامه (Design Review)</title>',
)
rep('<span class="ver">DESIGN v12.4 · REVIEW</span>',
    '<span class="ver">DESIGN v12.5 · REVIEW</span>')
rep(
    'پاسخبرگ، پاسخنامه، AI و تایمر در ردیف چیپهای آرام و پاسخنامهٔ تشریحی بهصورت پنل feedback میمو نمایش داده میشوند. معماری اورجینال قوسدار، ۵ تب، ۷ بخش آزمون، ۲۷۰ دقیقهٔ ثابت و قفلها دستنخوردهاند.',
    'چیپهای «پاسخبرگ»، «پاسخنامه» و «توضیح با هوش مصنوعی» دقیقاً کنار هم در بدنهٔ آزموناند و پاسخنامهٔ تشریحی بهصورت پنل feedback میمو نمایش داده میشود. معماری اورجینال قوسدار، ۵ تب، ۷ بخش آزمون، ۲۷۰ دقیقه بهعنوان پیشفرضِ قابل تغییر و قفلها دستنخوردهاند.',
)
rep(
    '<div class="cat-meta">قالب ثابت: <b>زمان ثابت ۲۷۰ دقیقه</b> · ۲۰۰–۴۰۰ سؤال · نمرهٔ منفی ⅓ · «زمان خالص آزمون» · پاسخنامه در پایان آزمون باز میشود</div>',
    '<div class="cat-meta">قالب: <b>زمان ثابت ۲۷۰ دقیقه</b> بهعنوان پیشفرض (مدت در تنظیم زمان، برای همهٔ آزمونها قابل تغییر است) · ۲۰۰–۴۰۰ سؤال · نمرهٔ منفی ⅓ · «زمان خالص آزمون» · پاسخنامه در پایان آزمون باز میشود</div>',
)
rep('<span class="mini">زمان ثابت</span>', '<span class="mini">قابل تغییر</span>', 2)
rep(
    'data-code="timer ONLY inside exam · ONE chip: tap to set / pause / resume · comprehensive fixed 270 min"',
    'data-code="timer ONLY inside exam · ONE chip: tap to set / pause / resume · manual minutes for EVERY exam kind · 270 = comprehensive preset only"',
)

# ------------------------------------------------- 2. three chips in .lb-tools (v12.1 style)
rep(
    '''<div class="lb-tools" data-code="only پاسخبرگ / پاسخنامه chips remain · exit via chapter-toolbar X · end exam via پاسخبرگ · AI via پاسخنامه">
            <button class="lb-chip" id="answerSheetBtn" data-sheet="paletteSheet"><span data-icon="ic_list_bulleted" data-size="16" data-mono="1"></span>پاسخبرگ</button>
            <button class="lb-chip" id="answerKeyBtn" data-sheet="keySheet"><span data-icon="ic_file" data-size="16" data-mono="1"></span>پاسخنامه</button>
          </div>''',
    '''<div class="lb-tools" data-code="v12.5 · THREE quiet chips exactly as v12.1: پاسخبرگ / پاسخنامه / توضیح با هوش مصنوعی · exit via chapter-toolbar X · end exam via پاسخبرگ or exitSheet">
            <button class="lb-chip" id="answerSheetBtn" data-sheet="paletteSheet"><span data-icon="ic_list_bulleted" data-size="16" data-mono="1"></span>پاسخبرگ</button>
            <button class="lb-chip" id="answerKeyBtn" data-sheet="keySheet"><span data-icon="ic_file" data-size="16" data-mono="1"></span>پاسخنامه</button>
            <button class="lb-chip" id="askAiBtn"><span data-icon="ic_magic_wand" data-size="16" data-mono="1"></span>توضیح با هوش مصنوعی</button>
          </div>''',
)

# ------------------------------------------------------------- 3. timer sheet: always editable
rep(
    '<div class="field"><label>مدت (دقیقه)</label><input type="number" id="timerMinutes" min="1" max="300" value="30"></div>\n        <p class="note" id="timerFixedHint">عدد دلخواه بین ۱ تا ۳۰۰ دقیقه.</p>',
    '<div class="field"><label>مدت (دقیقه)</label><input type="number" id="timerMinutes" min="1" step="1" value="270" inputmode="numeric" data-code="v12.5 · editable in EVERY exam kind · 270 = comprehensive preset only"></div>\n        <p class="note" id="timerHint">مدت دلخواه به دقیقه — در همهٔ آزمونها، حتی جامع، قابل تغییر است.</p>',
)

# ----------------------------------------------- 4. keySheet: drop the v12.4 duplicate AI button
rep(
    '<div class="krow" style="margin:12px 0 0"><button class="btn primary" data-close="keySheet">بستن</button><button class="btn" id="askAiBtn"><span data-icon="ic_magic_wand" data-size="14" data-mono="1"></span>توضیح با هوش مصنوعی</button></div>',
    '<div class="krow" style="margin:12px 0 0"><button class="btn primary" data-close="keySheet">بستن</button></div>',
)

# ------------------------------------------------------------- 5. exitSheet: third option
rep(
    '<div class="sheet" id="exitSheet"><div class="handle"></div><h4>خروج از آزمون؟</h4><p class="note">پاسخهای تا این لحظه ذخیره میشوند.</p><div class="krow" style="margin:0"><button class="btn primary" data-close="exitSheet" data-nav="exam-hub">خروج و ذخیره</button><button class="btn" data-close="exitSheet">ادامهٔ آزمون</button></div></div>',
    '''<div class="sheet" id="exitSheet"><div class="handle"></div><h4>خروج از آزمون؟</h4><p class="note">پاسخها تا این لحظه ذخیره میشوند. «خروج و ذخیره» بعداً از همان سؤال قابل ادامه است و در انتها کارنامه میدهد؛ گزینهٔ سوم همانجا درصد پاسخهای زدهشده را نشان میدهد.</p><div class="krow exit-actions" style="margin:0"><button class="btn primary" id="exitSaveBtn" data-close="exitSheet" data-nav="exam-hub">خروج و ذخیره</button><button class="btn" data-close="exitSheet">ادامهٔ آزمون</button><button class="btn" id="exitFinishBtn">پایان آزمون و دیدن کارنامه<small>خروج و دیدن درصد تا همینجا</small></button></div></div>''',
)

# ------------------------------------------------- 6. result screen: ids for the partial report
rep(
    '''          <h2>آزمون تمام شد!</h2>
          <p>۳ سؤال نیاز به مرور دارد. پاسخنامهٔ تشریحی آماده است.</p>''',
    '''          <h2 id="resTitle">آزمون تمام شد!</h2>
          <p id="resSub">۳ سؤال نیاز به مرور دارد. پاسخنامهٔ تشریحی آماده است.</p>''',
)
rep(
    '''          <div class="kv"><span>درصد با نمرهٔ منفی</span><span>۶۸٪</span></div>
          <div class="kv"><span>اگر غلطها نزده میذاشتی</span><span>۷۴٪</span></div>
          <div class="kv"><span>غلط / نزده</span><span>۴ / ۵</span></div>
          <div class="kv"><span>رتبه / تراز</span><span>۱۲۴۰ / ۶۲۰۰</span></div>
        </div>''',
    '''          <div class="kv"><span id="resPctLabel">درصد با نمرهٔ منفی</span><span id="resPct">۶۸٪</span></div>
          <div class="kv"><span>اگر غلطها نزده میذاشتی</span><span id="resPctNoNeg">۷۴٪</span></div>
          <div class="kv"><span>غلط / نزده</span><span id="resWrongBlank">۴ / ۵</span></div>
          <div class="kv"><span>رتبه / تراز</span><span id="resRank">۱۲۴۰ / ۶۲۰۰</span></div>
        </div>
        <div class="banner warn" id="resPartial" hidden data-code="v12.5 · خروج و دیدن درصد: computed only from answered-so-far"></div>''',
)

# ------------------------------------------- 7. hidden resume bar in exam hub (only after save)
rep(
    '''        <div class="sec">۱ · آزمونهای جامع</div>''',
    '''        <div class="resume-bar" id="resumeBar" hidden data-code="v12.5 · خروج و ذخیره → resume the same exam from the saved question"><span id="resumeText">آزمون ذخیرهشده</span><button class="btn primary" id="resumeBtn">ادامهٔ آزمون ذخیرهشده</button></div>
        <div class="sec">۱ · آزمونهای جامع</div>''',
)

# --------------------------------------------------------------------------- 8. CSS additions
rep(
    '.exv12 .lb-chip:hover{border-color:var(--primary);color:var(--primary)}',
    '''.exv12 .lb-chip:hover{border-color:var(--primary);color:var(--primary)}
/* v12.5 · three stacked exit choices + the hidden "resume saved exam" bar */
#exitSheet .exit-actions{flex-direction:column;align-items:stretch;gap:8px}
#exitSheet .exit-actions .btn{width:100%;text-align:center;padding:9px 13px}
#exitSheet .exit-actions small{display:block;font:400 10px/1.4 Tahoma,system-ui,sans-serif;color:var(--text-weak);margin-top:2px}
.exv12 .resume-bar{display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;margin:0 14px 10px;padding:10px 12px;border:1px solid var(--line2);border-radius:12px;background:var(--card);font:400 11px/1.5 Tahoma,system-ui,sans-serif}
.exv12 .resume-bar .btn{white-space:nowrap}
.exv12 .screen [hidden],.exv12 [hidden]{display:none!important}''',
)

# ------------------------------------------------------------ 9. footer / version note
rep(
    '⚠️ این <b>طرح دور دوازدهم v12.4</b> است، نه محصول.',
    '⚠️ این <b>طرح دور دوازدهم v12.5</b> است، نه محصول.',
)
rep(
    'تایمر حالا <b>یک دکمهٔ واحد</b> است که کنار زمانش علامت توقف/پلی و استاپ میگیرد. نسخههای',
    'تایمر حالا <b>یک دکمهٔ واحد</b> است که کنار زمانش علامت توقف/پلی و استاپ میگیرد. <b>v12.5:</b> چیپ «توضیح با هوش مصنوعی» دقیقاً به همان جایگاه و استایل قبل، کنار «پاسخبرگ / پاسخنامه» برگشت و کپی اضافهٔ داخل پاسخنامه حذف شد؛ مدت آزمون در <b>همهٔ</b> آزمونها (حتی جامع ۲۷۰ دقیقه) دستی و قابل تغییر است؛ کشوی خروج گزینهٔ سوم «پایان آزمون و دیدن کارنامه / خروج و دیدن درصد» گرفت که درصد پاسخهای زدهشده تا همان لحظه را نشان میدهد، و «خروج و ذخیره» پیشرفت را نگه میدارد تا بعداً ادامه شود و در پایان کارنامه بدهد. نسخههای',
)

# =========================================================== JS ===========================================================
rep(
    '  /* ---------- timer state machine · v12.4: ONE chip, no extra control chips ---------- */',
    '  /* ---------- timer state machine · v12.5: ONE chip, manual minutes for EVERY exam kind ---------- */',
)
# fmt(): 270 minutes must render as ۲۷۰:۰۰, not ۷۰:۰۰
rep(
    '  function fmt(s){var m=Math.floor(s/60),x=s%60;return fa(("0"+m).slice(-2))+":"+fa(("0"+x).slice(-2))}',
    '  function fmt(s){var m=Math.floor(s/60),x=s%60;return fa(m>=100?String(m):("0"+m).slice(-2))+":"+fa(("0"+x).slice(-2))}',
)

# finishExam(reason, partial): the FULL finish (submit / timer end / resumed finish) yields
# the کارنامه; the THIRD exit option yields the partial کارنامه.
rep(
    '''  function finishExam(reason){
    T.state="finished";clearInterval(T.timer);T.timer=null;
    q("#examFinished").innerHTML='<div class="banner warn">'+reason+' — گزینهها قفل و پاسخها ثبت شدند.</div>';
    qa(".opt").forEach(function(o){o.style.pointerEvents="none";o.style.opacity=".55"});
    go("exam-result");render();
    var p=POLICY[EXAM_KIND]||POLICY.normal;
    if(!p.during){q("#keySheet").classList.add("on");toast("پایان آزمون: صفحهٔ پاسخنامه باز شد")}
    else toast("آزمون به پایان رسید — پاسخبرگ و پاسخنامه آمادهاند");
  }''',
    '''  function finishExam(reason,partial){
    T.state="finished";clearInterval(T.timer);T.timer=null;
    q("#examFinished").innerHTML='<div class="banner warn">'+reason+' — گزینهها قفل و پاسخها ثبت شدند.</div>';
    qa(".opt").forEach(function(o){o.style.pointerEvents="none";o.style.opacity=".55"});
    /* the exam is over: no saved run is left behind, the کارنامه is the result screen */
    SAVED=null;q("#resumeBar").hidden=true;
    go("exam-result");render();renderReport(!!partial);
    var p=POLICY[EXAM_KIND]||POLICY.normal;
    if(partial){toast("کارنامهٔ تا این لحظه — درصد پاسخهای زدهشده")}
    else if(!p.during){q("#keySheet").classList.add("on");toast("پایان آزمون: صفحهٔ پاسخنامه باز شد")}
    else toast("آزمون به پایان رسید — پاسخبرگ و پاسخنامه آمادهاند");
  }''',
)

# chip click: never lock the field; 270 is only a preset (set per exam in openExam)
rep(
    '''    q("#timerSheet").classList.add("on");T.state="setting";
    if(EXAM_KIND==="comprehensive"){q("#timerMinutes").value=270;q("#timerMinutes").readOnly=true;q("#timerFixedHint").textContent="زمان ثابت ۲۷۰ دقیقه (آزمون جامع) — غیرقابل تغییر"}
    else{q("#timerMinutes").readOnly=false;q("#timerFixedHint").textContent="عدد دلخواه بین ۱ تا ۳۰۰ دقیقه"}
    render();''',
    '''    q("#timerSheet").classList.add("on");T.state="setting";
    /* v12.5: manual minutes in EVERY exam kind — the field is never locked.
       270 is only the comprehensive preset, assigned once in openExam(). */
    var fld=q("#timerMinutes");fld.readOnly=false;fld.removeAttribute("readonly");
    q("#timerHint").textContent="مدت دلخواه به دقیقه — در همهٔ آزمونها قابل تغییر است"+(EXAM_KIND==="comprehensive"?" (پیشفرض جامع: ۲۷۰ دقیقه)":"");
    render();''',
)
rep(
    '    var m=parseInt(q("#timerMinutes").value,10);if(!m||m<1||m>300){toast("عددی بین ۱ تا ۳۰۰ دقیقه وارد کنید");return}',
    '    var m=parseInt(q("#timerMinutes").value,10);if(!m||m<1){toast("مدت آزمون را به دقیقه وارد کنید");return}',
)
# timer start / reset must not visually erase a recorded answer
rep(
    'q("#timerSheet").classList.remove("on");q("#examFinished").innerHTML="";resetOptions();',
    'q("#timerSheet").classList.remove("on");q("#examFinished").innerHTML="";resetOptions();restoreAnswer();',
)
rep(
    'q("#examFinished").innerHTML="";resetOptions();q("#timerSheet").classList.remove("on");',
    'q("#examFinished").innerHTML="";resetOptions();restoreAnswer();q("#timerSheet").classList.remove("on");',
)

# openExam: reset the real answer state, set the 270 preset (still editable), resume a saved run
rep(
    '''  function openExam(n){
    EXAM_KIND=n.dataset.kind||"normal";q("#examTitle").textContent=n.dataset.exam;
    QI=0;MARKS={};q("#examFinished").innerHTML="";resetOptions();renderQuestion();
    T.state="idle";clearInterval(T.timer);T.timer=null;render();
    applyPolicy();go("exam-run");toast("وارد «"+n.dataset.exam+"» شدید — "+(POLICY[EXAM_KIND]||POLICY.normal).label);
  }''',
    '''  function openExam(n){
    if(SAVED&&SAVED.exam===n.dataset.exam){resumeExam();return}
    EXAM_KIND=n.dataset.kind||"normal";q("#examTitle").textContent=n.dataset.exam;
    QI=0;MARKS={};ANSWERS={};CHECKED={};q("#examFinished").innerHTML="";resetOptions();renderQuestion();
    T.state="idle";clearInterval(T.timer);T.timer=null;render();
    /* 270 is a preset, NOT a lock: the same field stays editable for every kind */
    q("#timerMinutes").value=EXAM_KIND==="comprehensive"?270:30;
    q("#timerMinutes").readOnly=false;
    applyPolicy();go("exam-run");toast("وارد «"+n.dataset.exam+"» شدید — "+(POLICY[EXAM_KIND]||POLICY.normal).label);
  }''',
)

# real in-memory answer / resume state
rep(
    '  var QTOTAL=QBANK.length,QI=0,QCHECKED=false,MARKS={};',
    '''  var QTOTAL=QBANK.length,QI=0,QCHECKED=false,MARKS={};
  /* v12.5 · prototype-only in-memory state: chosen option per question, whether its
     feedback was shown, and the snapshot taken by «خروج و ذخیره». */
  var ANSWERS={},CHECKED={},SAVED=null;''',
)

# restore the recorded answer when a question is rendered again (resume / back navigation)
rep(
    '''    resetOptions();q("#exFeedback").hidden=true;QCHECKED=false;
    q("#nextQLabel").textContent="ادامه";
    q("#examProgress").style.width=Math.min(100,((QI+1)/QTOTAL)*100)+"%";
    q("#markQ").classList.toggle("marked",!!MARKS[QI]);
  }''',
    '''    resetOptions();q("#exFeedback").hidden=true;QCHECKED=false;
    restoreAnswer();paintPalette();
    q("#nextQLabel").textContent=(q(".opt.on")&&!QCHECKED)?"بررسی پاسخ":"ادامه";
    q("#examProgress").style.width=Math.min(100,((QI+1)/QTOTAL)*100)+"%";
    q("#markQ").classList.toggle("marked",!!MARKS[QI]);
  }''',
)

# record the choice
rep(
    '''    o.classList.add("on");QCHECKED=false;q("#exFeedback").hidden=true;setCtaLabel();''',
    '''    o.classList.add("on");ANSWERS[QI]=+o.dataset.opt;CHECKED[QI]=false;QCHECKED=false;q("#exFeedback").hidden=true;setCtaLabel();''',
)
rep(
    '''      var ok=+chosen.dataset.opt-1===item.ok;
      QCHECKED=true;''',
    '''      var ok=+chosen.dataset.opt-1===item.ok;
      ANSWERS[QI]=+chosen.dataset.opt;CHECKED[QI]=true;QCHECKED=true;''',
)

# palette now reflects the real answers / current question
rep(
    '''    if(i<15)d.className="done";if(i===3)d.className="cur";pal.appendChild(d);
  }''',
    '''    if(i<15)d.className="done";if(i===3)d.className="cur";pal.appendChild(d);
  }
  paintPalette();''',
)

# ------------------------------------------------- 10. v12.5 state helpers + exit wiring
rep(
    '''  /* ---------- ONE AI button: exam questions page + exam final page ---------- */''',
    '''  /* ---------- v12.5 · answer state, save/resume, partial & full کارنامه ---------- */
  function restoreAnswer(){
    var a=ANSWERS[QI];if(!a)return;
    var pick=null;qa("#exChoices .opt").forEach(function(o){if(+o.dataset.opt===a)pick=o});
    if(!pick)return;
    var item=QBANK[QI%QBANK.length];
    if(CHECKED[QI]){
      var ok=a-1===item.ok;
      pick.classList.add(ok?"correct":"wrong");QCHECKED=true;
      var fb=q("#exFeedback");fb.classList.toggle("bad",!ok);fb.hidden=false;
      q("#exFeedbackTitle").textContent=ok?"پاسخ درست است":"پاسخ نادرست است";
      q("#exFeedbackText").textContent=item.expl;
    }else pick.classList.add("on");
  }
  function paintPalette(){
    /* keep the v12.1 static 20-cell demo sheet until a real answer is recorded */
    if(!Object.keys(ANSWERS).length)return;
    var cells=qa("#palette > div");if(cells.length!==20)return;
    cells.forEach(function(c,i){var a=ANSWERS[i];c.className=i===QI?"cur":(a?"done":"");
      var sm=c.querySelector("small");if(sm)sm.textContent=a?fa(a):"—"});
  }
  function score(){
    var correct=0,wrong=0,answered=0;
    Object.keys(ANSWERS).forEach(function(k){
      var i=+k,a=ANSWERS[k];if(!a)return;
      answered++;if(a-1===QBANK[i%QBANK.length].ok)correct++;else wrong++;
    });
    return {correct:correct,wrong:wrong,blank:QTOTAL-answered,answered:answered,
            pct:answered?Math.max(0,Math.round((correct-wrong/3)/answered*100)):0,
            pctNoNeg:answered?Math.round(correct/answered*100):0};
  }
  /* partial = «پایان آزمون و دیدن کارنامه / خروج و دیدن درصد»;
     full    = «ثبت پاسخها و پایان» / اتمام تایمر، حتی بعد از ادامهٔ آزمون ذخیرهشده */
  function renderReport(partial){
    var s=score();
    if(partial){
      q("#resTitle").textContent="کارنامهٔ تا این لحظه";
      q("#resSub").textContent="پایان زودهنگام · "+fa(s.answered)+" پاسخ زدهشده محاسبه شد"+(s.answered?"":" (هنوز پاسخی ثبت نشده است)");
      q("#resPctLabel").textContent="درصد تا این لحظه (با نمرهٔ منفی)";
      q("#resPct").textContent=fa(s.pct)+"٪";
      q("#resPctNoNeg").textContent=fa(s.pctNoNeg)+"٪";
      q("#resWrongBlank").textContent=fa(s.wrong)+" / "+fa(s.blank);
      q("#resRank").textContent="—";
      q("#resultKind").textContent="تا این لحظه";
      var b=q("#resPartial");b.hidden=false;
      b.textContent="خروج و دیدن درصد: این عدد فقط از "+fa(s.answered)+" پاسخی که تا همینجا زدهاید بهدست آمد ("+fa(s.correct)+" درست · "+fa(s.wrong)+" غلط)؛ "+fa(s.blank)+" سؤال نزده ماندهاند.";
    }else{
      q("#resTitle").textContent="آزمون تمام شد!";
      q("#resSub").textContent="۳ سؤال نیاز به مرور دارد. پاسخنامهٔ تشریحی آماده است.";
      q("#resPctLabel").textContent="درصد با نمرهٔ منفی";
      q("#resPct").textContent="۶۸٪";
      q("#resPctNoNeg").textContent="۷۴٪";
      q("#resWrongBlank").textContent="۴ / ۵";
      q("#resRank").textContent="۱۲۴۰ / ۶۲۰۰";
      q("#resultKind").textContent=EXAM_KIND==="comprehensive"?"جامع":(POLICY[EXAM_KIND]||POLICY.normal).label.split(" · ")[0];
      q("#resPartial").hidden=true;
    }
  }
  function saveExam(){
    if(T.state==="running"){
      T.remaining=Math.max(0,Math.ceil((T.endAt-Date.now())/1000));
      clearInterval(T.timer);T.timer=null;T.state="paused";render();
    }
    SAVED={exam:q("#examTitle").textContent,kind:EXAM_KIND,qi:QI,
      answers:Object.assign({},ANSWERS),checked:Object.assign({},CHECKED),marks:Object.assign({},MARKS),
      minutes:q("#timerMinutes").value,
      timer:{state:T.state,remaining:T.remaining,total:T.total}};
    q("#resumeBar").hidden=false;
    q("#resumeText").textContent="«"+SAVED.exam+"» · سؤال "+fa(QI+1)+" از "+fa(QTOTAL)+" ذخیره شد";
    toast("پیشرفت ذخیره شد — بعداً از همان سؤال ادامه میدهید");
  }
  function resumeExam(){
    if(!SAVED)return;
    var sv=SAVED;
    EXAM_KIND=sv.kind;q("#examTitle").textContent=sv.exam;
    QI=sv.qi;ANSWERS=Object.assign({},sv.answers);CHECKED=Object.assign({},sv.checked);MARKS=Object.assign({},sv.marks);
    q("#timerMinutes").value=sv.minutes;q("#timerMinutes").readOnly=false;
    T.state=sv.timer.state;T.remaining=sv.timer.remaining;T.total=sv.timer.total;
    T.endAt=Date.now()+T.remaining*1000;clearInterval(T.timer);T.timer=null;
    if(T.state==="running")T.state="paused"; /* ادامه با همان پلی داخل چیپ تایمر */
    q("#examFinished").innerHTML="";renderQuestion();render();applyPolicy();go("exam-run");
    q("#resumeBar").hidden=true;SAVED=null;
    toast("ادامهٔ آزمون ذخیرهشده · سؤال "+fa(QI+1));
  }
  q("#exitSaveBtn").addEventListener("click",saveExam);
  q("#exitFinishBtn").addEventListener("click",function(){
    q("#exitSheet").classList.remove("on");finishExam("پایان آزمون و دیدن کارنامه",true);
  });
  q("#resumeBtn").addEventListener("click",resumeExam);

  /* ---------- ONE AI button: exam questions page + exam final page ---------- */''',
)

# sanity: the old locks must be completely gone
assert 'readOnly=true' not in s
assert 'غیرقابل تغییر' not in s
assert 'timerFixedHint' not in s
assert s.count('class="lb-chip"') == 3
assert s.count('id="askAiBtn"') == 1
assert s.count('<p class="note"') == 3

(TOOLS / "design_v12_5_template.html").write_text(s, encoding="utf-8")
# DESIGN/index.html is produced by tools/localize_v12_5_fa.py (pass فارسیسازی)،
# not here — otherwise a re-run of this builder would silently undo the
# default-Persian labels and bring the glossary affordance back.
print(f"v12.5 built: {n} replacements, {len(s.encode('utf-8'))} bytes")
print("next: python3 tools/localize_v12_5_fa.py  ->  DESIGN/index.html")
