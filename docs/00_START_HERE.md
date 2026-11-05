# ۰ · شروع کنید (جهتیابی ۵ دقیقهای)

**تاریخ بهروزرسانی:** ۲۰۲۶-۱۱-۰۵ · **شاخه:** `arena/aebb90b7-game` · **HEAD:** `9179b8c4`

## این ریپو چیست؟

میخواستیم از روی **اپ واقعی Mimo 9.35** (`com.getmimo`) یک اپ یادگیری کنکور
تجربیِ فارسی و **کاملاً آفلاین** بسازیم: همان ناوبری، همان حس درسهای ریز،
همان مسیر پیشرفت — ولی با محتوای کنکور ایران (کتاب زیست دوازدهم) و بدون سرور.

سه لایهٔ جدا از هم داریم که **هرگز قاطی نکن**:

```
┌─────────────────────────────────────────────────────────────────┐
│ ۱. EVIDENCE  «میمو واقعاً چیست؟»                                 │
│    ANALYSIS/  ·  ANALYSIS/MISSION_05…09  ·  ANALYSIS/RUNTIME    │
│    mimo-ui/  (استخراج ۰–۱۰۰ UI)  ·  google_drive/*.apk         │
│    → ۱۳۷ کامیت، ۸ مأموریت، SERVER CONFIRMED=0                  │
├─────────────────────────────────────────────────────────────────┤
│ ۲. DESIGN  «کاربر چه طرحی را تأیید کرد؟»                        │
│    mimo-ui/UPGRADE/DESIGN/index.html  =  v12.5-fa              │
│    mimo-ui/UPGRADE/CATALOGS/*.csv  =  قواعد F10–F47 و …        │
│    → ۵ تب، ۳ چیپ، هاب ۷بخشی، RTL فارسی، توکنهای ARSC         │
├─────────────────────────────────────────────────────────────────┤
│ ۳. PRODUCT  «چی تحویل دادیم؟»                                   │
│    app/content/   قرارداد و بستهٔ محتوا                         │
│    app/src/       موتورها (۱۵ ماژول ESM)                        │
│    app/native/    پوستهٔ بومی ·  app/assets/  داراییهای مصوب    │
│    app/dist/      ★ Mimo.html ★ + PWA + ZIP (تولیدی)            │
└─────────────────────────────────────────────────────────────────┘
```

## خلاصهٔ یکخطی وضعیت امروز

> ناوبری و لایهٔ محتوا دو بار بازسازی شدند؛ خروجی `app/dist/Mimo.html`
> self-contained است و ۴۵ تست + ۱۰۵ بررسی استاتیک پاس میکند؛
> **اما درسنامهٔ نهایی کتاب هنوز بازبینی نشده و وارد اپ نشده است**،
> و هیچ رفتار سروری تأیید نشده (`SERVER CONFIRMED=0`).

## منبع حقیقت (اگر دو سند باهم جور درنیامدند)

| رتبه | منبع | توضیح |
|---|---|---|
| ۱ | `ANALYSIS/MISSION_09/*` و داراییهای دیکدشدهٔ APK | واقعیت اندازهگیریشدهٔ میمو |
| ۲ | `mimo-ui/UPGRADE/DESIGN/index.html` + `CATALOGS/` | حکم کاربر (v12.5-fa) |
| ۳ | `app/content/MIMO_INFORMATION_FORM.json` | قرارداد ورود محتوا |
| ۴ | `app/docs/MIMO_CONTENT_MODEL.md`, `MIMO_NATIVE_NAVIGATION.md` | تشریح پیادهسازی فعلی |
| ۵ | `app/dist/Mimo.html` | محصول ساختهشده |
| ۶ | `mimo-ui/UPGRADE/00…24_*.md`، `app/OUTPUT_REPORT.md` | **بایگانی**؛ بنرهای superseded دارند |

## پنج کار رایج → از کجا شروع کنم؟

| میخواهم… | برو به |
|---|---|
| کل ماجرا را بفهمم | `01_CHRONOLOGY.md` → `02_DECISIONS.md` → `03_ERRORS_AND_DEAD_ENDS.md` |
| بدونم الان چی کار میکند | `04_CURRENT_STATE.md`، بعد `app/docs/OUTPUT_GUIDE.md` |
| بدونم چی مانده | `05_ROADMAP.md` |
| یک ادعا را ثابت کنم | `06_EVIDENCE_INDEX.md` |
| کار را به ایجنت دیگری بدهم | `08_HANDOFF_PROMPT.md` + `AGENTS.md` |

## سه عددی که همیشه باید درست بمانند

- `SERVER CONFIRMED = 0`
- `externalProvider = 'not-configured'` (بدون LLM / شبکه / کلید / تولید متن)
- `reviewStatus = 'unreviewed'` برای هر محتوایی که از کتاب آمده

## بعد از این سند

همچنین: [`10_FILE_MAP.md`](10_FILE_MAP.md) (نقشهٔ فایلبهفایل) · بعدی: [`01_CHRONOLOGY.md`](01_CHRONOLOGY.md) · ایندکس ماشینخوان:
[`../REPO_INDEX.json`](../REPO_INDEX.json) · سلامت اسناد: `python3 docs/verify_docs.py`
