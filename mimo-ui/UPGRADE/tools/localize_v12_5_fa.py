#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""localize_v12_5_fa.py — pass فارسیسازی روی v12.5 (فقط ویرایش لیبل/تمیزکاری).

منبع همیشه tools/design_v12_5_template.html (خروجی build_exam_v12_5.py) است،
پس این اسکریپت idempotent است: هر بار همان خروجی فارسی را میسازد.

قواعد:
  * فقط متن دیدنی عوض میشود؛ data-tab / data-mode / data-code / data-lh و
    payload های GEO / LEARN / NODE / KONKUR دستنخورده میمانند.
  * واژههای انگلیسی قدیمی فقط در صفتهای نامرئی (data-code / data-lh)
    بهعنوان شاهد باقی میمانند تا assertionهای کدفirst نشکنند.
  * آیکون «واژهنامهٔ مبحث» (gloss-fab) بهطور کامل از DOM/CSS/هندلر حذف میشود.
  * ناوبری پایین بهصورت پیشفرض فارسی است؛ دکمهٔ RTL فقط جهت را آینه میکند و
    دیگر متن انگلیسی برنمیگرداند.
"""
from __future__ import annotations
from pathlib import Path

UP = Path(__file__).resolve().parents[1]
SRC = UP / "tools" / "design_v12_5_template.html"
OUT = UP / "DESIGN" / "index.html"
TPL_FA = UP / "tools" / "design_v12_5_fa_template.html"


def rep(s: str, old: str, new: str, n: int = 1) -> str:
    c = s.count(old)
    if c != n:
        raise SystemExit(f"REPLACEMENT MISS: expected {n}, found {c} :: {old[:120]!r}")
    return s.replace(old, new)


R = []  # (old, new, expected_count)


def add(old, new, n=1):
    R.append((old, new, n))


# ---------------------------------------------------------------- ۱) سربرگ / عنوان سند
add(r'''<title>طرح رابط کاربری v12.5 — بازگشت چیپ AI + مدت دستی در همهٔ آزمونها + گزینهٔ سوم خروج و کارنامه (Design Review)</title>''',
    r'''<title>طرح رابط کاربری v12.5 — بازگشت چیپ هوش مصنوعی + مدت دستی در همهٔ آزمونها + گزینهٔ سوم خروج و کارنامه (بازبینی طراحی)</title>''')
add(r'''    <h1>طرح رابط کاربری — دور دوازدهم <span class="ver">DESIGN v12.5 · REVIEW</span></h1>''',
    r'''    <h1>طرح رابط کاربری — دور دوازدهم <span class="ver" data-code="DESIGN v12.5 · REVIEW">طرح v12.5 · بازبینی</span></h1>''')
add(r'''<b>یک دکمهٔ بنفش تمامعرض CONTINUE</b>''',
    r'''<b data-code="CONTINUE">یک دکمهٔ بنفش تمامعرض «ادامه»</b>''')
add(r'''    <button class="btn" id="dirBtn">↔ فارسی / RTL</button>''',
    r'''    <button class="btn" id="dirBtn" data-code="RTL mirror toggle">↔ راستبهچپ</button>''')
add(r'''      <button data-go="ai">۱۴ · چت AI</button>''',
    r'''      <button data-go="ai">۱۴ · چت هوش مصنوعی</button>''')

# ---------------------------------------------------------------- ۲) حذف آیکون واژهنامهٔ مبحث
add(r'''.gloss-fab{position:absolute;z-index:4;right:16px;bottom:12px;width:56px;height:56px;border-radius:50%;background:var(--card);border:1px solid var(--line2);display:flex;align-items:center;justify-content:center;color:var(--text);cursor:pointer;box-shadow:0 3px 8px rgba(37,39,70,.12)}
.gloss-fab .ga{position:absolute;font:700 13px/1 system-ui,sans-serif;color:var(--primary)}''',
    r'''/* v12.5-fa: دایرهٔ .gloss-fab / «واژهنامهٔ مبحث» حذف شد؛ شواهد فقط در data-code و NODE payload */''')
add(r'''.gloss-fab{position:absolute;z-index:4;right:12px;bottom:8px;width:56px;height:56px;border-radius:50%;background:var(--card);border:1px solid var(--line2);display:flex;align-items:center;justify-content:center;color:var(--text);cursor:pointer;box-shadow:0 3px 8px rgba(37,39,70,.12)}
.gloss-fab .book{width:27px;height:31px;border:2px solid var(--text);border-radius:5px;position:relative;display:flex;align-items:center;justify-content:center}
.gloss-fab .book:before{content:"";position:absolute;left:4px;top:0;bottom:0;width:2px;background:var(--text);opacity:.55}
.gloss-fab .book b{font:700 13px/1 system-ui,sans-serif;margin-left:4px;color:var(--text)}''',
    r'''/* v12.5-fa: CSS دایرهٔ .gloss-fab / .book حذف شد (شاهد قدیمی: NODE payload) */''')
add(r'''          <div class="gloss-fab" data-glossary="1" data-code="floating book / dictionary affordance"><span class="book"><b>A</b></span></div>
''', r'''''')
add(r'''    var gl=e.target.closest("[data-glossary]");
    if(gl){toast("واژهنامهٔ مبحث");return}
''', r'''''')
add(r'''      <li><b>شناور:</b> دایرهٔ کتاب/واژهنامه با A (<code>ic_file.xml</code> + <code>bookmark_no_fill.xml</code>) · سربرگ ۳ چیپ''',
    r'''      <li><b>شناور:</b> دایرهٔ کتاب/واژهنامه <b>حذف شد</b> (شواهد قدیمی: <code>ic_file.xml</code> + <code>bookmark_no_fill.xml</code>، فقط در <code>data-code</code>) · سربرگ ۳ چیپ''')

# ---------------------------------------------------------------- ۳) عرض تبها (جلوگیری از شکستن «هوش مصنوعی»)
add(r'''.tabs .tab{font-size:10px;letter-spacing:0}''',
    r'''.tabs .tab{font-size:10px;letter-spacing:0}
.tabs .tab>span:last-child{white-space:nowrap}''')

# ---------------------------------------------------------------- ۴) انتخاب مسیر / نمای مسیر / جزئیات مبحث / درس
add(r'''<b data-fa="انتخاب مسیر">Select Path</b>''', r'''<b data-fa="انتخاب مسیر">انتخاب مسیر</b>''')
add(r'''        <button class="sd-cta" id="sdContinue" data-nav="chapter" data-fa="ادامه">Continue</button>''',
    r'''        <button class="sd-cta" id="sdContinue" data-nav="chapter" data-fa="ادامه">ادامه</button>''')
add(r'''        <button class="sd-link" id="sdOverview" data-nav="path-overview" data-fa="نمای دوره">See course overview</button>''',
    r'''        <button class="sd-link" id="sdOverview" data-nav="path-overview" data-fa="نمای دوره">نمای دوره</button>''')
add(r'''            <p data-fa="گاهی لازم است متنها را با شکستن خطوط، خواناتر کنیم.">Sometimes we want to format paragraphs with line breaks.</p>''',
    r'''            <p data-fa="گاهی لازم است متنها را با شکستن خطوط، خواناتر کنیم.">گاهی لازم است متنها را با شکستن خطوط، خواناتر کنیم.</p>''')
add(r'''            <p data-fa="مثلاً این جمله خیلی بهتر میشد اگر &lt;span class=&quot;codechip&quot;&gt;غضروف&lt;/span&gt; در یک خط و &lt;span class=&quot;codechip&quot;&gt;استخوان&lt;/span&gt; در خط بعدی قرار میگرفت.">For example, this song would look much better if <span class="codechip">Raindrops on roses</span> appeared on one line, <span class="codechip">Whiskers on kittens</span> on the next, and so on.</p>''',
    r'''            <p data-fa="مثلاً این جمله خیلی بهتر میشد اگر &lt;span class=&quot;codechip&quot;&gt;غضروف&lt;/span&gt; در یک خط و &lt;span class=&quot;codechip&quot;&gt;استخوان&lt;/span&gt; در خط بعدی قرار میگرفت.">مثلاً این جمله خیلی بهتر میشد اگر <span class="codechip">غضروف</span> در یک خط و <span class="codechip">استخوان</span> در خط بعدی قرار میگرفت.</p>''')
add(r'''                <h3 data-fa="بافتها">My favorite things</h3>''',
    r'''                <h3 data-fa="بافتها">بافتها</h3>''')
add(r'''                <p data-fa="بافت پوششی، بافت پیوندی، بافت ماهیچهای و بافت عصبی">Raindrops on roses Whiskers on kittens Bright copper kettles Warm woolen mittens</p>''',
    r'''                <p data-fa="بافت پوششی، بافت پیوندی، بافت ماهیچهای و بافت عصبی">بافت پوششی، بافت پیوندی، بافت ماهیچهای و بافت عصبی</p>''')
add(r'''          <button class="continue-btn" data-nav="learn" data-fa="ادامه">Continue</button>''',
    r'''          <button class="continue-btn" data-nav="learn" data-fa="ادامه">ادامه</button>''')

# ---------------------------------------------------------------- ۵) لیدربورد
add(r'''        <div class="sec-h" data-fa="وضعیت من" data-code="profile_info_card_view.xml">My status</div>''',
    r'''        <div class="sec-h" data-fa="وضعیت من" data-code="profile_info_card_view.xml · My status (archived EN label)">وضعیت من</div>''')
add(r'''<small data-fa="روز متوالی">Day streak</small>''', r'''<small data-fa="روز متوالی">روز متوالی</small>''')
add(r'''<small data-fa="امتیاز کل">XP total</small>''', r'''<small data-fa="امتیاز کل">امتیاز کل</small>''')
add(r'''          <h4 data-fa="آزمونها و امتیازات من">My exams &amp; scores</h4>''',
    r'''          <h4 data-fa="آزمونها و امتیازات من">آزمونها و امتیازات من</h4>''')
add(r'''<span data-fa="آزمون جامع تجربی">Comprehensive exam</span>''', r'''<span data-fa="آزمون جامع تجربی">آزمون جامع تجربی</span>''')
add(r'''<span data-fa="آزمون تکدرسی زیست">Biology single-subject</span>''', r'''<span data-fa="آزمون تکدرسی زیست">آزمون تکدرسی زیست</span>''')
add(r'''<span data-fa="آزمون زماندار شیمی">Timed chemistry</span>''', r'''<span data-fa="آزمون زماندار شیمی">آزمون زماندار شیمی</span>''')
add(r'''<span data-fa="آزمون تحلیلی غلطها">Analytical / wrong answers</span>''', r'''<span data-fa="آزمون تحلیلی غلطها">آزمون تحلیلی غلطها</span>''')
add(r'''<span data-fa="امتیاز این هفته">Weekly XP</span><b>330 ⚡</b>''', r'''<span data-fa="امتیاز این هفته">امتیاز این هفته</span><b>۳۳۰ ⚡</b>''')

# ---------------------------------------------------------------- ۶) پروفایل کاربر
add(r'''        <div class="up-head"><span class="bk" data-nav="leaderboard">‹ Back</span><b data-fa="پروفایل کاربر">User Profile</b>''',
    r'''        <div class="up-head"><span class="bk" data-nav="leaderboard">‹ بازگشت</span><b data-fa="پروفایل کاربر">پروفایل کاربر</b>''')
add(r'''          <h3 data-fa="سارا">malibu</h3>''', r'''          <h3 data-fa="سارا">سارا</h3>''')
add(r'''          <p data-fa="هنوز اطلاعاتی از سارا ثبت نشده است">We don't know anything about malibu</p>''',
    r'''          <p data-fa="هنوز اطلاعاتی از سارا ثبت نشده است">هنوز اطلاعاتی از سارا ثبت نشده است</p>''')
add(r'''          <button class="follow" data-fa="دنبال کردن">Follow</button>''',
    r'''          <button class="follow" data-fa="دنبال کردن">دنبال کردن</button>''')
add(r'''          <div class="statcard"><span class="ic" data-icon="ic_streak_active" data-size="32"></span><b>1</b><small>Day streak</small></div>
          <div class="statcard"><span class="ic" data-icon="ic_flash_filled" data-size="32" data-mono="1" style="color:var(--yellow)"></span><b>480</b><small>XP total</small></div>
          <div class="statcard"><span class="ic" data-icon="img_brain" data-size="32"></span><b>Wooden</b><small>League</small></div>''',
    r'''          <div class="statcard"><span class="ic" data-icon="ic_streak_active" data-size="32"></span><b>1</b><small data-fa="روز متوالی">روز متوالی</small></div>
          <div class="statcard"><span class="ic" data-icon="ic_flash_filled" data-size="32" data-mono="1" style="color:var(--yellow)"></span><b>480</b><small data-fa="امتیاز کل">امتیاز کل</small></div>
          <div class="statcard"><span class="ic" data-icon="img_brain" data-size="32"></span><b data-fa="چوبی">چوبی</b><small data-fa="لیگ">لیگ</small></div>''')
add(r'''        <div class="sec-h">Playgrounds</div>''', r'''        <div class="sec-h" data-fa="آزمونهای من">آزمونهای من</div>''')
add(r'''<b data-fa="هیچ آزمونی نیست">No playgrounds</b><p data-fa="برای ساختن آزمون تازه، روی «ساخت آزمون» بزن">There are no Playgrounds on malibu's profile</p>''',
    r'''<b data-fa="هیچ آزمونی نیست">هیچ آزمونی نیست</b><p data-fa="برای ساختن آزمون تازه، روی «ساخت آزمون» بزن">برای ساختن آزمون تازه، روی «ساخت آزمون» بزن</p>''')

# ---------------------------------------------------------------- ۷) پروفایل (HTML -> نام درس کنکور)
add(r'''        <div class="prof-head"><b data-fa="پروفایل">Profile</b>''',
    r'''        <div class="prof-head"><b data-fa="پروفایل">پروفایل</b>''')
add(r'''          <b data-fa="زیستشناسی">HTML</b><span class="pct">0%</span>''',
    r'''          <b data-fa="زیست دهم" data-code="HTML (archived EN course label)">زیست دهم</b><span class="pct">0%</span>''')
add(r'''        <div class="sec-h" data-fa="جامهای لیگ">Leaderboard Trophies</div>''',
    r'''        <div class="sec-h" data-fa="جامهای امتیازها">جامهای امتیازها</div>''')
add(r'''          <b data-fa="هنوز جامی ندارید">No trophies yet</b>''',
    r'''          <b data-fa="هنوز جامی ندارید">هنوز جامی ندارید</b>''')
add(r'''          <p data-fa="به بالای لیدربورد برسید تا جام بگیرید">Get to the top of your Leaderboard and win a trophy</p>''',
    r'''          <p data-fa="به بالای لیدربورد برسید تا جام بگیرید">به بالای لیدربورد برسید تا جام بگیرید</p>''')
add(r'''        <div class="plink"><span data-fa="آزمونهای من">Playgrounds</span><span data-sheet="playgroundSheet" data-fa="＋ ساخت آزمون">＋ PLAYGROUNDS</span></div>''',
    r'''        <div class="plink"><span data-fa="آزمونهای من">آزمونهای من</span><span data-sheet="playgroundSheet" data-fa="＋ ساخت آزمون">＋ ساخت آزمون</span></div>''')
add(r'''          <b data-fa="ایدههایتان را کاوش کنید">Explore Your Ideas</b>''',
    r'''          <b data-fa="ایدههایتان را کاوش کنید">ایدههایتان را کاوش کنید</b>''')
add(r'''          <p data-fa="آزمون بسازید، تست بزنید و نتیجه را از گوشی دنبال کنید">Code, test, and share projects seamlessly from your phone</p>''',
    r'''          <p data-fa="آزمون بسازید، تست بزنید و نتیجه را از گوشی دنبال کنید">آزمون بسازید، تست بزنید و نتیجه را از گوشی دنبال کنید</p>''')

# ---------------------------------------------------------------- ۸) نتیجهٔ آزمون / چت هوشمند
add(r'''          <b>صورت اشتباهات (منتقلشونده به AI)</b>''',
    r'''          <b>صورت اشتباهات (منتقلشونده به هوش مصنوعی)</b>''')
add(r'''</div><span class="cost" data-lh="Cost $0.01">$0.01</span>''',
    r'''</div><span class="cost" data-lh="Cost $0.01">۰٫۰۱ دلار</span>''')
add(r'''          <div class="in"><input id="aiInput" placeholder="What do you want to learn? · ai_tutor_input_placeholder">''',
    r'''          <div class="in"><input id="aiInput" placeholder="دربارهٔ کدام مبحث میخواهی یاد بگیری؟" data-code="ai_tutor_input_placeholder · What do you want to learn?">''')
add(r'''          <div class="foot ai-foot">''',
    r'''          <div class="foot ai-foot" data-code="gemini-flash-lite-latest · medium · TEACH / PRACTICE">''')
add(r'''data-fa="آموزش">TEACH </button><button data-mode="PRACTICE" data-lh="PRACTICE mode" data-fa="تمرین">PRACTICE </button>''',
    r'''data-fa="آموزش">آموزش</button><button data-mode="PRACTICE" data-lh="PRACTICE mode" data-fa="تمرین">تمرین</button>''')
add(r'''            <button class="fchip ai-foot-chip" data-lh="Model picker">gemini-flash-lite-latest <span''',
    r'''            <button class="fchip ai-foot-chip" data-lh="Model picker">مدل سریع <span''')
add(r'''            <button class="fchip ai-foot-chip" data-lh="Effort">medium <span''',
    r'''            <button class="fchip ai-foot-chip" data-lh="Effort">تلاش متوسط <span''')
add(r'''    toast("ارسال به LearnHarness (/max)");''', r'''    toast("ارسال به چارچوب یادگیری");''')
add(r'''toast("حالت "+b.dataset.mode+" انتخاب شد")''', r'''toast("حالت "+b.dataset.fa+" انتخاب شد")''')
add(r'''  go("ai");toast("اشتباهات، پاسخها و صورت سؤالها به AI منتقل شد");''',
    r'''  go("ai");toast("اشتباهات، پاسخها و صورت سؤالها به هوش مصنوعی منتقل شد");''')

# ---------------------------------------------------------------- ۹) تمرین مبحث (HTML Basics -> مبحث کنکور)
add(r'''<b data-fa="تمرین مبحث">Section practice</b>''', r'''<b data-fa="تمرین مبحث">تمرین مبحث</b>''')
add(r'''          <span class="kick">SECTION · PRACTICE</span>''', r'''          <span class="kick">مبحث · تمرین</span>''')
add(r'''          <h2 id="spTitle">HTML Basics</h2>''',
    r'''          <h2 id="spTitle" data-code="HTML Basics (archived EN section)">ساختار سلول و بافت</h2>''')
add(r'''          <p>Sharpen your skills with hands-on practice exercises and projects</p>''',
    r'''          <p>تمرینهای کوتاه و طبقهبندیشدهٔ مباحث تا فصل ۴</p>''')
add(r'''        <button class="sd-cta" id="practiceStart">Start lesson</button>''',
    r'''        <button class="sd-cta" id="practiceStart">شروع تمرین</button>''')
add(r'''        <button class="sd-link" data-modal="practiceModal">Fully charged!</button>''',
    r'''        <button class="sd-link" data-modal="practiceModal">شارژ کامل!</button>''')

# ---------------------------------------------------------------- ۱۰) کشوی قالبها -> نام آزمونهای کنکور
add(r'''<b style="font:700 18px/1 system-ui,sans-serif">Create Playground</b></div>''',
    r'''<b style="font:700 18px/1 system-ui,sans-serif">ساخت آزمون</b></div>''')
add(r'''        <div class="lbl" style="color:var(--text-weak);font:700 14px/1 system-ui,sans-serif;margin-bottom:12px">Select a Template</div>''',
    r'''        <div class="lbl" style="color:var(--text-weak);font:700 14px/1 system-ui,sans-serif;margin-bottom:12px">انتخاب قالب آزمون</div>''')
add(r'''        <div class="tpl-row"><div class="tpl-thumb"><span data-icon="ic_file" data-size="40"></span></div><div><b>Python</b><p>Python environment for experimentation and prototyping</p></div></div>''',
    r'''        <div class="tpl-row" data-code="Python (archived EN template)"><div class="tpl-thumb"><span data-icon="ic_file" data-size="40"></span></div><div><b>آزمون جامع</b><p>همهٔ درسها، با زمانبندی و کارنامهٔ کامل</p></div></div>''')
add(r'''        <div class="tpl-row"><div class="tpl-thumb"><span data-icon="ic_square_rounded" data-size="40"></span></div><div><b>JavaScript</b><p>JavaScript environment for experimentation and prototyping</p></div></div>''',
    r'''        <div class="tpl-row" data-code="JavaScript (archived EN template)"><div class="tpl-thumb"><span data-icon="ic_square_rounded" data-size="40"></span></div><div><b>آزمون تکدرس</b><p>یک مبحث مشخص، مثلاً «زیست دهم»</p></div></div>''')
add(r'''        <div class="tpl-row"><div class="tpl-thumb"><span data-icon="ic_task_completed" data-size="40"></span></div><div><b>Static website</b><p>Basic HTML, CSS, and JS starter for static sites</p></div></div>''',
    r'''        <div class="tpl-row" data-code="Static website (archived EN template)"><div class="tpl-thumb"><span data-icon="ic_task_completed" data-size="40"></span></div><div><b>آزمون زماندار</b><p>زمان محدود و تمرین سرعت پاسخگویی</p></div></div>''')
add(r'''        <div class="tpl-row"><div class="tpl-thumb"><span data-icon="ic_sparks" data-size="40"></span></div><div><b>React app</b><p>React starter for dynamic single-page applications</p></div></div>''',
    r'''        <div class="tpl-row" data-code="React app (archived EN template)"><div class="tpl-thumb"><span data-icon="ic_sparks" data-size="40"></span></div><div><b>آزمون تحلیلی</b><p>بررسی غلطها و سؤالهای نزده</p></div></div>''')

# ---------------------------------------------------------------- ۱۱) مودالها
add(r'''        <h2 data-fa="مسیر ناتمام">Unfinished track</h2>''',
    r'''        <h2 data-fa="مسیر ناتمام">مسیر ناتمام</h2>''')
add(r'''        <p data-fa="مسیر را تمام کنید تا گواهی شخصیشدهاقتان را بگیرید">Finish the track and receive your personalised certificate</p>''',
    r'''        <p data-fa="مسیر را تمام کنید تا گواهی شخصیشدهاقتان را بگیرید">مسیر را تمام کنید تا گواهی شخصیشدهاقتان را بگیرید</p>''')
add(r'''        <button class="utok" data-modal-close="unfinishedModal" data-fa="باشه">Ok</button>''',
    r'''        <button class="utok" data-modal-close="unfinishedModal" data-fa="باشه">باشه</button>''')
add(r'''        <h2 id="practiceModalTitle">Fully charged!</h2>''',
    r'''        <h2 id="practiceModalTitle">شارژ کامل!</h2>''')
add(r'''        <p id="practiceModalText">Practicing little every day is proved to be the most effective.</p>''',
    r'''        <p id="practiceModalText">هر روز کمی تمرین کردن، مؤثرترین راه یادگیری است.</p>''')
add(r'''        <button class="utok" data-modal-close="practiceModal">Practice anyway</button>''',
    r'''        <button class="utok" data-modal-close="practiceModal">بااینحال تمرین میکنم</button>''')
add(r'''        <div class="mtop"><span class="lbl" data-fa="یادگیری">Learn</span>''',
    r'''        <div class="mtop"><span class="lbl" data-fa="یادگیری">یادگیری</span>''')
add(r'''        <h2 data-fa="ساختار سلول و بافت">Structuring Text with Tags</h2>''',
    r'''        <h2 data-fa="ساختار سلول و بافت">ساختار سلول و بافت</h2>''')
add(r'''        <div class="chapter-row"><span data-fa="فصل">Chapter</span><span>0/2</span></div>''',
    r'''        <div class="chapter-row"><span data-fa="فصل">فصل</span><span>0/2</span></div>''')
add(r'''        <button class="startbtn" id="startLearning"><span data-fa="شروع یادگیری">Start learning</span>''',
    r'''        <button class="startbtn" id="startLearning"><span data-fa="شروع یادگیری">شروع یادگیری</span>''')

# ---------------------------------------------------------------- ۱۲) ناوبری پایین: فارسی بهصورت پیشفرض
add(r'''<span data-fa="یادگیری">Learn</span></div>''', r'''<span data-fa="یادگیری">یادگیری</span></div>''')
add(r'''<span data-fa="تمرین">Practice</span></div>''', r'''<span data-fa="تمرین">تمرین</span></div>''')
add(r'''<span>AI</span></div>''',
    r'''<span data-fa="هوش مصنوعی" data-code="AI (archived EN tab label)">هوش مصنوعی</span></div>''')
add(r'''<span data-fa="لیدربورد">Leaderboard</span></div>''',
    r'''<span data-fa="امتیازها">امتیازها</span></div>''')
add(r'''<span data-fa="پروفایل">Profile</span></div>''', r'''<span data-fa="پروفایل">پروفایل</span></div>''')

# ---------------------------------------------------------------- ۱۳) JS: toast تبها / RTL / شواهد کد
add(r'''    var lh=e.target.closest("[data-lh]");if(lh){toast("LearnHarness ← "+lh.dataset.lh);return}''',
    r'''    var lh=e.target.closest("[data-lh]");if(lh){toast("چارچوب یادگیری ← "+(lh.dataset.fa||"شاهد کد"));return}''')
add(r'''  qa("#tabs .tab").forEach(function(t){t.addEventListener("click",function(){go(tabScreen[t.dataset.tab]);toast("تب "+t.dataset.tab+" · ناوبری ۵ تب میمو")})});''',
    r'''  var tabFa={Learn:"یادگیری",Practice:"تمرین",AI:"هوش مصنوعی",Leaderboard:"امتیازها",Profile:"پروفایل"};
  qa("#tabs .tab").forEach(function(t){t.addEventListener("click",function(){go(tabScreen[t.dataset.tab]);toast("تب "+tabFa[t.dataset.tab]+" · ناوبری ۵ تب میمو")})});''')
add(r'''  var rtl=false;
  q("#dirBtn").addEventListener("click",function(){
    rtl=!rtl;var ph=q("#phone");ph.style.direction=rtl?"rtl":"ltr";
    qa(".mimo,.exv12",ph).forEach(function(s){s.style.direction=rtl?"rtl":"ltr"});
    qa("[data-fa]",ph).forEach(function(el){
      if(el.dataset.enhtml===undefined)el.dataset.enhtml=el.innerHTML;
      el.innerHTML=rtl?el.dataset.fa:el.dataset.enhtml;
    });
    this.textContent=rtl?"↔ English / LTR":"↔ فارسی / RTL";
    toast(rtl?"آینهٔ RTL + لیبلهای فارسی":"نمای ۱۰۰٪ میمو (LTR)");
  });''',
    r'''  var rtl=false;
  /* v12.5-fa: لیبلها پیشفرض فارسیاند؛ دکمه فقط جهت را آینه میکند و متن انگلیسی برنمیگرداند */
  q("#dirBtn").addEventListener("click",function(){
    rtl=!rtl;var ph=q("#phone");ph.style.direction=rtl?"rtl":"ltr";
    qa(".mimo,.exv12",ph).forEach(function(s){s.style.direction=rtl?"rtl":"ltr"});
    this.textContent=rtl?"↔ چپبراست":"↔ راستبهچپ";
    toast(rtl?"آینهٔ راستبهچپ · لیبلها فارسی":"نمای چپبراست · لیبلها فارسی");
  });''')

# ---------------------------------------------------------------- ۱۴) JS تمرین: نام فصلهای کنکوری + متن فارسی
add(r'''  var NS=NODE.strings, NCM=NODE.contentModel, PRACTICE_SECTION=3;''',
    r'''  var NS=NODE.strings, NCM=NODE.contentModel, PRACTICE_SECTION=3;
  /* v12.5-fa: نام فصلهای کنکوری جایگزین عنوانهای HTML/برنامهنویسی شد */
  var P_FA=["ساختار سلول و بافت","آنزیمها","اتم و ساختار الکترونی","حرکتشناسی","تابع و مشتق","ژنتیک و وراثت","تعادل شیمیایی","ترمودینامیک","گسلش و فشار","دستهبندی گیاهان"];''')
add(r'''    q("#spTitle").textContent=sec.name;''', r'''    q("#spTitle").textContent=P_FA[Math.min(n,P_FA.length)-1];''')
add(r'''      var sname=sc.sections[i%sc.sections.length].name;''', r'''      var sname=P_FA[i%P_FA.length];''')
add(r''' · tutorialId '+fa(tid)+''', r''' · شناسهٔ درس '+fa(tid)+''')
add(r'''    q("#practiceModalTitle").textContent=NS.practice.section_details_smart_practice_charged_dialog_title;''',
    r'''    q("#practiceModalTitle").textContent="شارژ کامل!";''')
add(r'''    q("#practiceModalText").textContent=NS.practice.section_details_smart_practice_charged_dialog_description;''',
    r'''    q("#practiceModalText").textContent="هر روز کمی تمرین کردن، مؤثرترین راه یادگیری است.";''')
add(r'''+esc(NS.chapter_start.lesson_feedback_keep_going||"Let's keep it going.")''', r'''+esc("ادامه بده، خوب پیش میروی")''')
add(r'''      q("#practiceModalTitle").textContent=NS.practice.section_details_smart_practice_mastered_dialog_title;''',
    r'''      q("#practiceModalTitle").textContent="همهٔ تمرینها تمام شد!";''')
add(r'''      q("#practiceModalText").textContent=NS.practice.section_details_smart_practice_mastered_dialog_description;''',
    r'''      q("#practiceModalText").textContent="این مبحث را بهطور کامل تمرین کردهاید.";''')
add(r'''      toast(NS.practice.you_finished_all_practice_sessions);''',
    r'''      toast("همهٔ تمرینهای این مبحث انجام شد");''')

# ---------------------------------------------------------------- ۱۵) پنل مشخصات / پاورقی
add(r''' فقط <b>My status / وضعیت من</b> و''', r''' فقط <b data-code="My status">«وضعیت من»</b> و''')
add(r'''    <ul><li><b>DESIGN v8 · REVIEW</b> — منتظر تأیید نهایی</li>''',
    r'''    <ul><li><b data-code="DESIGN v8 · REVIEW">طرح v12.5 · بازبینی</b> — منتظر تأیید نهایی</li>''')
add(r''' «وارد کردن کلید API» فقط یک یادداشت است''',
    r''' <b>بستهٔ فارسیسازی:</b> لیبلهای دیدنی لیدربورد/پروفایل/ناوبری/تمرین فارسی شدند، عنوانهای HTML و قالبهای برنامهنویسی به نام درسها و آزمونهای کنکور تغییر کردند، آیکون «واژهنامهٔ مبحث» حذف شد و ناوبری پایین بدون نیاز به دکمهٔ RTL فارسی است؛ رشتههای انگلیسی قدیمی فقط بهعنوان شاهد نامرئی (<code>data-code</code> / <code>data-lh</code>) و در payloadهای کد باقیاند. «وارد کردن کلید API» فقط یک یادداشت است''')


def main():
    s = SRC.read_text(encoding="utf-8")
    for old, new, n in R:
        s = rep(s, old, new, n)
    # sanity: هیچکدام از شناسهها / شواهد دست نخوردهاند
    assert s.count('data-tab="') == 5, "data-tab identifiers changed"
    assert s.count('class="note"') == 3, "p.note count changed"
    assert s.count("data-code=") >= 15 and s.count("data-lh=") >= 7, "hidden evidence lost"
    assert 'data-glossary="1"' not in s, "glossary affordance still in DOM"
    assert 'class="gloss-fab"' not in s, "gloss-fab element still in DOM"
    assert "var GEO=" in s and "var LEARN=" in s and "var NODE=" in s and "var KONKUR=" in s, "payload damaged"
    OUT.write_text(s, encoding="utf-8")
    TPL_FA.write_text(s, encoding="utf-8")
    print(f"localize_v12_5_fa: {len(R)} replacements -> {len(s):,} chars")
    print(f"  wrote {OUT.relative_to(UP)} and {TPL_FA.relative_to(UP)}")


if __name__ == "__main__":
    main()
