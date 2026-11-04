#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fix_design_v12_1.py — bug-fix pass over the v12 prototype (DESIGN ONLY, no product code).

Run AFTER build_design_v12.py. Source: tools/design_v12_template.html (the v12 output).
Fixes the code mistakes reported in review:

  B1  .exv12{overflow:hidden} clipped exam-hub AND exam-result (only exam-run has an
      internal .lb-body scroller + pinned .lk footer). Both were unscrollable, so 5 of the
      7 labelled exam sections and the lower result cards were unreachable.
  B2  after turning the 3-column node grid into Mimo list rows, the click handler was still
      bound to the 44dp .nodek icon only — clicking the row label did nothing although the
      whole row had cursor:pointer. Now delegated to the whole row (+ keyboard Enter/Space).
  B3  the 8 exam-hub filter chips were inert <span>s with no listener. Now real buttons
      that show/hide the 7 labelled sections.
  B4  AI context string hardcoded «سؤال ۳» regardless of the current question.
  B5  question counter said «از ۲۰» while QBANK only had 5 records (stems repeated
      silently); QI was also NOT reset when opening a new exam. Now 20 distinct records,
      one QTOTAL constant, QI=0 on every new exam.
  B6  RTL/LTR toggle only touched .mimo screens; after the skin change the 3 exam screens
      were skipped. Also render() did not reset the pause/reset chips in "setting" state.
  B7  the .mini meta badges were display:none (their info was lost); they are moved into
      the row label as a proper Mimo subtitle. Plus fragile subject split / pointless
      paintIcons call removed, and bookmarks now persist per question.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

UP = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
TOOLS = UP / "tools"
DESIGN = UP / "DESIGN"
html = (TOOLS / "design_v12_template.html").read_text(encoding="utf-8")


def rep(old: str, new: str, label: str, count: int = 1):
    global html
    n = html.count(old)
    if n != count:
        raise SystemExit("%s matched %d times (expected %d)" % (label, n, count))
    html = html.replace(old, new, count)


# ---------------------------------------------------------------- B1 / B7 CSS
rep(".exv12{direction:rtl;background:var(--bg);display:none;flex-direction:column;overflow:hidden}\n.exv12.on{display:flex}",
    ".exv12{direction:rtl;background:var(--bg);display:none;flex-direction:column;overflow:auto;padding:0}\n"
    ".exv12.on{display:flex}\n"
    "/* only exam-run owns an internal scroller (.lb-body) + pinned footer (.lk); the other two must scroll */\n"
    '.exv12[data-screen="exam-run"]{overflow:hidden}', "B1 scroll")
rep(".exv12 .lb-body{flex:1;overflow:auto;padding:8px 16px 16px}",
    ".exv12 .lb-body{flex:1;min-height:0;overflow:auto;padding:8px 16px 16px}", "B1 min-height")
rep(".exv12 .grid3>div{display:flex;align-items:center;gap:12px;background:var(--card);",
    ".exv12 .grid3>div{display:flex;align-items:center;gap:12px;position:relative;background:var(--card);", "B7 row position")
rep(".exv12 .nodek .mini{position:static;display:none}",
    ".exv12 .label .row-meta{display:block;font:400 10px/1.4 Tahoma,system-ui,sans-serif;color:var(--text-weak);margin-top:3px}",
    "B7 row subtitle")
rep(".exv12 .chips{padding:4px 16px 10px}",
    ".exv12 .chips{padding:4px 16px 10px}\n"
    ".exv12 .chips .chip{cursor:pointer;border:0;user-select:none}", "B3 chip cursor")
rep(".exv12 .qfoot{position:static;",
    ".exv12 #examFinished .banner{margin:14px 0 0}\n.exv12 .qfoot{position:static;", "banner margin")

# ---------------------------------------------------------------- B3 markup
rep('<div class="chips"><span class="chip on">همه</span><span class="chip">جامع</span><span class="chip">زماندار</span><span class="chip">تکدرسی</span><span class="chip">مبحثی</span><span class="chip">این ماه</span><span class="chip">تحلیلی</span><span class="chip">جمع بندی</span></div>',
    '<div class="chips" data-code="Mimo filter chips — functional section filters">\n'
    '          <button type="button" class="chip on" data-filter="all">همه</button>\n'
    '          <button type="button" class="chip" data-filter="0">جامع</button>\n'
    '          <button type="button" class="chip" data-filter="1">زماندار</button>\n'
    '          <button type="button" class="chip" data-filter="2">تکدرسی</button>\n'
    '          <button type="button" class="chip" data-filter="2">مبحثی</button>\n'
    '          <button type="button" class="chip" data-filter="3">این ماه</button>\n'
    '          <button type="button" class="chip" data-filter="4">تحلیلی</button>\n'
    '          <button type="button" class="chip" data-filter="5,6">جمع بندی</button>\n'
    '        </div>', "B3 chips markup")

# ---------------------------------------------------------------- B5 static text
rep('<span id="examStep">سؤال ۳ از ۲۰</span>', '<span id="examStep">سؤال ۱ از ۲۰</span>', "B5 step")
rep('<i id="examProgress" style="width:15%"></i>', '<i id="examProgress" style="width:5%"></i>', "B5 progress")

# ---------------------------------------------------------------- B2 / B3 / B7 JS: exam-open
rep('''  qa(".nodek[data-exam]").forEach(function(n){n.addEventListener("click",function(){
    EXAM_KIND=n.dataset.kind||"normal";q("#examTitle").textContent=n.dataset.exam;
    q("#examFinished").innerHTML="";resetOptions();renderQuestion();T.state="idle";clearInterval(T.timer);T.timer=null;
    applyPolicy();go("exam-run");toast("وارد «"+n.dataset.exam+"» شدید — "+(POLICY[EXAM_KIND]||POLICY.normal).label);
  })});''',
'''  /* v12.1 B2: the WHOLE Mimo list row is clickable, not just the 44dp icon */
  function openExam(n){
    EXAM_KIND=n.dataset.kind||"normal";q("#examTitle").textContent=n.dataset.exam;
    QI=0;MARKS={};q("#examFinished").innerHTML="";resetOptions();renderQuestion();
    T.state="idle";clearInterval(T.timer);T.timer=null;
    applyPolicy();go("exam-run");toast("وارد «"+n.dataset.exam+"» شدید — "+(POLICY[EXAM_KIND]||POLICY.normal).label);
  }
  var ehRows=qa('[data-screen="exam-hub"] .grid3 > div');
  ehRows.forEach(function(row){
    var n=row.querySelector(".nodek[data-exam]");if(!n)return;
    row.setAttribute("role","button");row.tabIndex=0;
    row.addEventListener("click",function(){openExam(n)});
    row.addEventListener("keydown",function(e){if(e.key==="Enter"||e.key===" "){e.preventDefault();openExam(n)}});
    /* B7: the previously hidden .mini badge becomes the row subtitle */
    var mini=row.querySelector(".mini"),lab=row.querySelector(".label");
    if(mini&&lab){mini.className="row-meta";lab.appendChild(mini)}
  });
  /* v12.1 B3: filter chips were decorative; wire them to the 7 labelled sections */
  var ehSec=q('[data-screen="exam-hub"]'),ehGroups=[],ehCur=null;
  Array.prototype.forEach.call(ehSec.children,function(c){
    if(c.classList.contains("sec")){ehCur=[c];ehGroups.push(ehCur)}
    else if(ehCur&&(c.classList.contains("cat-meta")||c.classList.contains("grid3")))ehCur.push(c);
  });
  qa('[data-screen="exam-hub"] .chips .chip').forEach(function(ch){
    ch.addEventListener("click",function(){
      qa('[data-screen="exam-hub"] .chips .chip').forEach(function(x){x.classList.remove("on")});
      ch.classList.add("on");
      var want=(ch.dataset.filter==="all")?null:ch.dataset.filter.split(",");
      ehGroups.forEach(function(g,i){
        var show=!want||want.indexOf(String(i))>=0;
        g.forEach(function(el){el.style.display=show?"":"none"});
      });
    });
  });''', "B2 exam-open + B3 filters + B7 meta")

# ---------------------------------------------------------------- B4 / B6
rep('    qa(".mimo",ph).forEach(function(s){s.style.direction=rtl?"rtl":"ltr"});',
    '    qa(".mimo,.exv12",ph).forEach(function(s){s.style.direction=rtl?"rtl":"ltr"});', "B6 rtl toggle")
rep('    else if(T.state==="setting"){label.textContent="تنظیم زمان";stateText.textContent="در حال تنظیم"}',
    '    else if(T.state==="setting"){label.textContent="تنظیم زمان";stateText.textContent="در حال تنظیم";q("#timerPause").style.display="none";q("#timerReset").style.display="none"}',
    "B6 render setting state")
rep('    setCtx("زمینه: "+q("#examTitle").textContent+" · سؤال ۳ · "+q("#qText").textContent+" · پاسخ شما: "+chosen.trim(),null);',
    '    setCtx("زمینه: "+q("#examTitle").textContent+" · سؤال "+fa(QI+1)+" · "+q("#qText").textContent+" · پاسخ شما: "+chosen.trim(),null);',
    "B4 AI context")

# ---------------------------------------------------------------- B5 question flow
start = "  function resetOptions(){"
end = "  renderQuestion();\n"
i = html.index(start)
j = html.index(end, i) + len(end)
QBLOCK = r'''  function resetOptions(){qa(".opt").forEach(function(o){o.style.pointerEvents="";o.style.opacity="";o.classList.remove("on","correct","wrong")})}
  /* ============ v12.1 · Mimo lesson_interactive question flow (corrected) ============
     ChoiceView -> btn_submit (بررسی پاسخ) -> feedback bottom sheet -> btn_continue_big
     (ادامه) -> next question.  btn_undo = سؤال قبل (48dp square).  No equal prev/next pair.
     B5: 20 distinct questions match the declared QTOTAL; QI resets for every new exam. */
  var QRAW=[
    ["زیست · سمها · دشواری متوسط","کدامیک از گزینههای زیر دربارهٔ «سمها» درست است؟",["سمها همواره تنها در کبد ساخته میشوند","سمها میتوانند با اتصال به آنزیمها، فعالیت آنها را مهار کنند","همهٔ سمها در بدن به گلوکز تبدیل میشوند","سمها فقط از راه پوست وارد بدن میشوند"],1,"سمها با اتصال به جایگاه فعال آنزیمها میتوانند آنها را مهار کنند؛ زیست یازدهم، فصل سمها و بیماریها."],
    ["شیمی · تعادل شیمیایی · دشواری متوسط","ثابت تعادل یک واکنش برگشتپذیر در دمای ثابت، با افزایش غلظت یکی از واکنشدهندهها…",["کاهش مییابد","افزایش مییابد","تغییر نمیکند","صفر میشود"],2,"Kc فقط تابع دماست؛ تغییر غلظت سامانه را جابهجا میکند ولی مقدار ثابت تعادل ثابت میماند (اصل لوشاتلیه)."],
    ["فیزیک · ترمودینامیک · دشواری سخت","کار انجامشده توسط گاز در یک فرایند همحجم برابر است با…",["PΔV","صفر","nRΔT","ΔU"],1,"در فرایند همحجم ΔV=۰ است، پس W=PΔV=۰ و تمام گرما صرف تغییر انرژی درونی میشود."],
    ["ریاضی · مشتق · دشواری متوسط","مشتق تابع f(x)=x³−3x در x=۱ کدام است؟",["۰","۱","۳","۶"],0,"f′(x)=3x²−3، پس f′(1)=0؛ نقطهٔ بحرانی و اکسترمم نسبی."],
    ["زیست · ژنتیک · دشواری آسان","در قانون دوم مندل (تفکیک)، نسبت ژنوتیپی نسل F₂ برای یک صفت تکژنی چیست؟",["۳:۱","۱:۲:۱","۹:۳:۳:۱","۱:۱"],1,"نسبت فنوتیپی ۳:۱ و نسبت ژنوتیپی ۱:۲:۱ است (AA:Aa:aa)."],
    ["شیمی · پیوند شیمیایی · دشواری آسان","کدام عنصر الکترونگاتیویتر است؟",["سدیم","منیزیم","کلر","پتاسیم"],2,"الکترونگاتیوی در یک دوره از چپ به راست افزایش و در یک گروه از بالا به پایین کاهش مییابد؛ کلر بیشینه است."],
    ["فیزیک · نور و پرتو · دشواری متوسط","هنگام گذر نور از هوا به شیشه، کدام کمیت ثابت میماند؟",["سرعت نور","طول موج","بسامد","جهت پرتو"],2,"بسامد نور هنگام تغییر محیط ثابت است؛ سرعت و طول موج تغییر میکنند و پرتو میشکند."],
    ["ریاضی · دنبالهها · دشواری متوسط","حد دنبالهٔ aₙ=(2n+1)/(3n−1) کدام است؟",["۰","۲/۳","۱","∞"],1,"با تقسیم صورت و مخرج بر n، حد برابر ۲/۳ میشود."],
    ["زیست · سلول · دشواری متوسط","کدام اندامک مسئول ساخت ATP در یاختهٔ یوکاریوتی است؟",["ریبوزوم","میتوکندری","دستگاه گلژی","شبکهٔ آندوپلاسمی"],1,"میتوکندری با تنفس یاخته‌ای ATP میسازد؛ ریبوزوم محل ساخت پروتئین است."],
    ["شیمی · استوکیومتری · دشواری متوسط","چند مولکول آب از واکنش کامل ۲ مول هیدروژن با اکسیژن کافی بهدست میآید؟",["۱ مول","۲ مول","۳ مول","۴ مول"],1,"2H₂+O₂→2H₂O؛ نسبت مولی H₂ به H₂O برابر ۱:۱ است، پس ۲ مول آب."],
    ["فیزیک · مکانیک · دشواری سخت","نیروی ۱۲ نیوتونی به جسمی به جرم ۳ کیلوگرم وارد میشود؛ شتاب چند متر بر مجذور ثانیه است؟",["۲","۳","۴","۱۲"],2,"قانون دوم نیوتون: a=F/m=۱۲/۳=۴ m/s²."],
    ["ریاضی · احتمال · دشواری متوسط","در پرتاب یک تاس سالم، احتمال آمدن عدد زوج چقدر است؟",["۱/۶","۱/۳","۱/۲","۲/۳"],2,"اعداد زوج ۲، ۴ و ۶اند؛ ۳ حالت مطلوب از ۶ حالت، یعنی ۱/۲."],
    ["زیست · فتوسنتز · دشواری متوسط","واکنشهای نوری فتوسنتز در کدام بخش کلروپلاست رخ میدهند؟",["استروما","تیلاکوئید","دیوارهٔ یاخته","واکوئول"],1,"واکنشهای نوری در غشای تیلاکوئید و چرخهٔ کالوین در استروما انجام میشود."],
    ["شیمی · محلولها · دشواری آسان","افزایش دما معمولاً انحلالپذیری نمکهای جامد در آب را…",["کاهش میدهد","افزایش میدهد","تغییر نمیدهد","صفر میکند"],1,"انحلال اغلب نمکهای جامد گرماگیر است؛ با افزایش دما انحلالپذیری بیشتر میشود."],
    ["فیزیک · الکتریسیته · دشواری متوسط","دو مقاومت ۶ و ۳ اهمی بهصورت موازی بسته شوند؛ مقاومت معادل چقدر است؟",["۹ اهم","۴٫۵ اهم","۲ اهم","۱ اهم"],2,"1/R=1/6+1/3=1/2، پس R=۲ اهم."],
    ["ریاضی · مثلثات · دشواری متوسط","مقدار sin²x+cos²x برای هر zاویهٔ x کدام است؟",["۰","۱/۲","۱","۲"],2,"اتحاد بنیادی مثلثات: sin²x+cos²x=۱."],
    ["زیست · گردش خون · دشواری آسان","خون سرشار از اکسیژن از ششها به کدام حفرهٔ قلب بازمیگردد؟",["دهلیز راست","بطن راست","دهلیز چپ","بطن چپ"],2,"سیاهرگهای ششی خون اکسیژندار را به دهلیز چپ میآورند."],
    ["شیمی · سینتیک · دشواری سخت","کاتالیزگر در یک واکنش شیمیایی چه میکند؟",["آنتروپی را تغییر میدهد","انرژی فعالسازی را کاهش میدهد","تعادل را جابهجا میکند","دمای واکنش را افزایش میدهد"],1,"کاتالیزگر مسیری با انرژی فعالسازی کمتر فراهم میکند؛ ثابت تعادل و ΔG را تغییر نمیدهد."],
    ["فیزیک · موج · دشواری متوسط","اگر بسامد موجی دو برابر شود و سرعت ثابت بماند، طول موج…",["دو برابر میشود","نصف میشود","ثابت میماند","چهار برابر میشود"],1,"v=fλ؛ با ثابت بودن v، دو برابر شدن f یعنی نصف شدن λ."],
    ["ریاضی · انتگرال · دشواری سخت","∫(2x+1)dx کدام است؟",["x²+x+C","2x²+x+C","x²+C","2+C"],0,"انتگرال جزءبهجزء: x²+x+C (C ثابت انتگرالگیری)."]
  ];
  var QBANK=QRAW.map(function(r){return {sub:r[0],stem:r[1],opts:r[2],ok:r[3],expl:r[4]}});
  var QTOTAL=QBANK.length,QI=0,QCHECKED=false,MARKS={};
  function renderQuestion(){
    var item=QBANK[QI%QBANK.length];
    q("#examStep").textContent="سؤال "+fa(QI+1)+" از "+fa(QTOTAL);
    /* B5: build the subject chip from DOM nodes (no innerHTML / no esc() dependency) */
    var subj=q("#examSubject");subj.innerHTML="";
    var dot=document.createElement("span");dot.className="lb-dot";subj.appendChild(dot);
    item.sub.split(" · ").forEach(function(part,i){
      if(i){var sep=document.createElement("span");sep.className="lb-sep";sep.textContent="·";subj.appendChild(sep)}
      var t=document.createElement("span");t.textContent=part;subj.appendChild(t);
    });
    q("#qText").textContent=item.stem;
    qa("#exChoices .opt").forEach(function(o,i){o.querySelector(".opt-txt").textContent=item.opts[i]});
    resetOptions();q("#exFeedback").hidden=true;QCHECKED=false;
    q("#nextQLabel").textContent="ادامه";
    q("#examProgress").style.width=Math.min(100,((QI+1)/QTOTAL)*100)+"%";
    q("#markQ").classList.toggle("marked",!!MARKS[QI]);
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
    QI=Math.min(QTOTAL-1,QI+1);renderQuestion();toast("سؤال بعدی · "+fa(QI+1)+" از "+fa(QTOTAL));
  });
  q("#prevQ").addEventListener("click",function(){QI=Math.max(0,QI-1);renderQuestion();toast("سؤال قبل · "+fa(QI+1)+" از "+fa(QTOTAL))});
  q("#skipQ").addEventListener("click",function(){QI=Math.min(QTOTAL-1,QI+1);renderQuestion();toast("سؤال رد شد")});
  q("#markQ").addEventListener("click",function(){
    if(MARKS[QI])delete MARKS[QI];else MARKS[QI]=true;
    q("#markQ").classList.toggle("marked",!!MARKS[QI]);
    toast(MARKS[QI]?"سؤال علامتگذاری شد":"علامت برداشته شد");
  });
  renderQuestion();
'''
html = html[:i] + QBLOCK + html[j:]

# ---------------------------------------------------------------- evidence + outputs
evp = DESIGN / "EXAM_UI_CODE_EVIDENCE.json"
ev = json.loads(evp.read_text(encoding="utf-8"))
ev["bugfixes_v12_1"] = [
    "B1: exam-hub / exam-result were clipped by overflow:hidden with no internal scroller -> whole-screen scroll, exam-run keeps its .lb-body scroller + pinned .lk footer",
    "B2: click handler bound only to the 44dp .nodek icon after the grid became list rows -> whole row + keyboard activation",
    "B3: 8 filter chips were inert spans -> real buttons filtering the 7 labelled sections",
    "B4: AI context hardcoded «سؤال ۳» -> dynamic fa(QI+1)",
    "B5: counter said 20 but QBANK had 5; QI not reset per exam -> 20 distinct questions, one QTOTAL, QI=0 on openExam",
    "B6: RTL/LTR toggle skipped exv12 screens; render() did not reset timer chips in setting state",
    "B7: hidden .mini badges lost their meta -> moved into each row label as a Mimo subtitle; DOM-built subject chip; per-question bookmarks",
]
evp.write_text(json.dumps(ev, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

(TOOLS / "design_v12_1_template.html").write_text(html, encoding="utf-8")
(DESIGN / "index.html").write_text(html, encoding="utf-8")
print(json.dumps({
    "output": str(DESIGN / "index.html"),
    "bytes": len(html.encode("utf-8")),
    "source": str(TOOLS / "design_v12_template.html"),
    "hub_and_result_scrollable": '.exv12[data-screen="exam-run"]{overflow:hidden}' in html and "overflow:auto;padding:0}" in html,
    "row_delegation": "function openExam(n)" in html and "ehRows.forEach" in html,
    "filter_chips": html.count('data-filter="') == 8,
    "question_bank": html.count('\n    ["') == 20,
    "qtotals": "QTOTAL=QBANK.length" in html and "var i=1;i<=20;i++" in html,
    "ai_dynamic": "سؤال \"+fa(QI+1)+\"" in html,
    "rtl_toggle": 'qa(".mimo,.exv12",ph)' in html,
    "row_meta": 'className="row-meta"' in html,
    "old_qnav_removed": 'class="qnav"' not in html,
    "curved_zigzag_kept": "M242 70 H280 Q312 70 312 102 V140" in html,
}, ensure_ascii=False, indent=2))
