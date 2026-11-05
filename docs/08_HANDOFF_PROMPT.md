# ۸ · متن آمادهٔ تحویل به ایجنت بعدی

> کپی کن و به همراه لینک ریپو بده. (همچنین `../AGENTS.md` را ضمیمه کن.)

---

```
تو یک ایجنت کدنویسی هستی روی ریپوی `danmillman008-hub/game`،
شاخهٔ `arena/aebb90b7-game` (فقط همین شاخه؛ شاخهٔ دیگری نساز و به جای
دیگری push نکن). زبان کاربر فارسی است؛ جواب نهایی را فارسی بده.

قبل از هر تغییری، به ترتیب بخوان:
  README.md
  AGENTS.md                ← قوانین سخت
  docs/00_START_HERE.md    ← جهتیابی
  docs/01_CHRONOLOGY.md    ← ۱۳۷ کامیت، M02–M09، دو خروجی ردشده
  docs/02_DECISIONS.md     ← تصمیمات لازمالاجرا و لغوشده
  docs/03_ERRORS_AND_DEAD_ENDS.md  ← بنبستها را دوباره نرو
  docs/04_CURRENT_STATE.md ← فایلها، اعداد، دستورات
  docs/05_ROADMAP.md       ← کاری که قرار است بسازیم (R1…R16)
  docs/06_EVIDENCE_INDEX.md ← محل شواهد
  REPO_INDEX.json          ← ایندکس ماشینخوان

قوانینی که هرگز نقض نکن:
• SERVER CONFIRMED=0. هیچ رفتار سرور/URL زنده/هدر/بدنه/فرمول پاداشی را
  تأییدشده اعلام نکن. استاتیک APK ≠ رانتایم.
• بدون LLM، بدون شبکه، بدون کلید API، بدون fetch/XHR/WebSocket/EventSource،
  بدون متن تولیدشده. externalProvider باید 'not-configured' بماند.
• محتوای درسنامه را نساز/حدس نزن. اپ فعلی STRUCTURED_PACKAGE.json دارد
  (structured ولی unreviewed). پیشنویس OCR کتاب در app/content/source/
  gitignored است و نباید وارد اپ یا گیت شود.
• داراییهای مصوب (mimo-ui/UPGRADE/DESIGN/index.html با SHA c356068…،
  app/assets/phone.html و proto.css/proto-data.js/proto-ui.js) بایتبهبایت
  دستنخورده بمانند؛ verify_app.py هشها را چک میکند.
• یادداشتهای v12.5-fa صددرصد رعایت شود: ۵ تب فارسی، ۳ چیپ، بدون مکس/
  روتین/Pro/پرداخت، RTL، توکنهای ARSC، هاب ۷بخشی آزمون، «پاسخبرگ» ≠
  «پاسخنامه»، تایمر فقط داخل آزمون.
• خروجی app/dist/ تولیدی است؛ منبع آن app/native/index.html و
  app/src/native.js و app/tools/build_output.py است.
• اسناد تاریخی (mimo-ui/UPGRADE/*, ANALYSIS/MISSION_*) را پاک/بازنویسی نکن.

وضعیت فعلی: HEAD 9179b8c4، خروجی app/dist/Mimo.html (یک فایل خودکفا،
بدون سرور/اینترنت)، ۴۵ تست + ۵۴ و ۵۱ بررسی استاتیک + ۲ ولیدیتور محتوا سبز.
ناوبری M09 و لایهٔ ۱۲۰ ریزدرس پیاده شده؛ ولی محتوای کتاب بازبینی نشده،
exam/QBANK و chapterRefFor() همچنان placeholder/هشپایهاند، و تنها ۵ خانواده
رندرر پیاده شده است.

کار بعدی را از docs/05_ROADMAP.md بگیر (پیشنهاد: R1 → R2 → R9).
قبل از اتمام حتماً اجرا کن:
  npm test --prefix app
  npm run verify --prefix app
  python3 app/tools/validate_content.py app/content/STARTER_PACKAGE.json app/content/STRUCTURED_PACKAGE.json
  python3 docs/verify_docs.py
و اگر فایل/عددی تغییر کرد، docs/04_CURRENT_STATE.md و REPO_INDEX.json را
هم بهروز کن. هیچ چیزی را «کاملاً شبیه شد» یا «تأییدشده» اعلام نکن مگر
با شاهد مشخص؛ ناتمامها را صریح بگو. سؤال توضیحی از کاربر نپرس؛ با کار نشان بده.
```

---

## چکلیست تحویل انسان ↔ ایجنت

- [ ] `README.md` + `AGENTS.md` خوانده شد
- [ ] `REPO_INDEX.json` با وضعیت روز همخوان است
- [ ] شاخهٔ کار `arena/aebb90b7-game` است
- [ ] چهار دستور بررسی اجرا و نتیجه گزارش شد
- [ ] `SERVER CONFIRMED=0` و `reviewStatus` در پاسخ نهایی ذکر شد
- [ ] هیچ سند تاریخی حذف/بازنویسی نشد

فهرست کامیتها: [`09_COMMIT_LOG.md`](09_COMMIT_LOG.md) · ایندکس:
[`../REPO_INDEX.json`](../REPO_INDEX.json)
