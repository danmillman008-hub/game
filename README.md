# میمو ۹٫۳۵ → اپ یادگیری کنکور (آفلاین)

> **اگر یک ایجنت / هوش مصنوعی هستی: اول [`AGENTS.md`](AGENTS.md) را بخوان.**
> اگر انسان هستی و ۵ دقیقه داری: [`docs/00_START_HERE.md`](docs/00_START_HERE.md).

این ریپو حاصل **۱۳۷ کامیت محصول** (تا `9179b8c4`) از ۲۰۲۶-۱۰-۲۴ تا
۲۰۲۶-۱۱-۰۵ روی شاخهٔ
`arena/aebb90b7-game` است: مهندسی معکوس کامل APK میمو ۹٫۳۵، ۱۲ دور طراحی
پروتوتایپ، ۸ مأموریت رانتایم، ساخت اپ آفلاین، OCR کامل کتاب ۸۴۸ صفحهای،
خروجی یککلیکه، حسابرسی API، و دو بار بازسازی بعد از ایراد کاربر.
(کامیتهای بعدی فقط نگهداری همین اسناد تحویلاند؛ فهرست ← `docs/09_COMMIT_LOG.md`.)

**تحویل فعلی (روی گیت، قابل اجرا):** [`app/dist/Mimo.html`](app/dist/Mimo.html) —
یک فایل خودکفا؛ دوبار کلیک کن، نه سرور نه اینترنت نه `npm`.
همچنین `app/dist/index.html` (PWA نصبشدنی)، `Mimo.zip`، `launcher.html`.

| | |
|---|---|
| شاخه | `arena/aebb90b7-game` (فعال؛ فقط همین شاخه) |
| HEAD محصول | `9179b8c4` (اسناد تحویل بعد از آن اضافه شدند) |
| وضعیت سرور | **`SERVER CONFIRMED=0`** — هیچ رفتار زندهای از سرور میمو تأیید نشده |
| LLM / شبکه / کلید API / تولید متن | **همگی خیر**؛ `externalProvider: not-configured` |
| محتوای درسنامه | ساختاریافته ولی `unreviewed`؛ کتاب نهایی همچنان بازبینی نشده |

---

## نقشهٔ اسناد (برای «همهچیز تمیز دستت باشه»)

| سند | سؤالی که جواب میدهد |
|---|---|
| [`AGENTS.md`](AGENTS.md) | یک ایجنت باید چه قوانینی را رعایت کند، از کجا شروع کند، چه چیزی را هرگز ادعا نکند؟ |
| [`docs/00_START_HERE.md`](docs/00_START_HERE.md) | این ریپو چیست، سه لایهاش کداماند، منبع حقیقت کجاست؟ |
| [`docs/01_CHRONOLOGY.md`](docs/01_CHRONOLOGY.md) | از کجا شروع کردیم، دقیقاً چه کردیم، ترتیب ۱۳۷ کامیت و مأموریتها؟ |
| [`docs/02_DECISIONS.md`](docs/02_DECISIONS.md) | کدام تصمیمها الزامیاند، کدام لغو شدهاند، کدام تعارضها چطور حل شدند؟ |
| [`docs/03_ERRORS_AND_DEAD_ENDS.md`](docs/03_ERRORS_AND_DEAD_ENDS.md) | چه شکستها، باگها، بنبستها و خروجیهای ردشده داشتیم؟ |
| [`docs/04_CURRENT_STATE.md`](docs/04_CURRENT_STATE.md) | الان دقیقاً چه فایلهایی هست، چطور بسازیم/تست کنیم، اعداد بررسی چقدر است؟ |
| [`docs/05_ROADMAP.md`](docs/05_ROADMAP.md) | چه چیزی قرار است بسازیم، اولویت و تعریف «تمام شد» چیست؟ |
| [`docs/06_EVIDENCE_INDEX.md`](docs/06_EVIDENCE_INDEX.md) | هر ادعا از کدام فایل شواهد میآید و اعتبارش چیست؟ |
| [`docs/07_GLOSSARY.md`](docs/07_GLOSSARY.md) | درسنامه / پاسخبرگ / ریزدرس / KONKUR / v12.5-fa یعنی چه؟ |
| [`docs/08_HANDOFF_PROMPT.md`](docs/08_HANDOFF_PROMPT.md) | متن آمادهٔ Paste برای تحویل به ایجنت بعدی |
| [`docs/09_COMMIT_LOG.md`](docs/09_COMMIT_LOG.md) | فهرست کامل ۱۳۷ کامیت |
| [`docs/10_FILE_MAP.md`](docs/10_FILE_MAP.md) | نقشهٔ فایلبهفایل: هر ماژول/ابزار/سند دقیقاً چیست |
| [`REPO_INDEX.json`](REPO_INDEX.json) | همان نقشه، بهصورت ماشینخوان |

**فایلهای همخوان ایجنتها:** `AGENTS.md` (استاندارد)،
[`CLAUDE.md`](CLAUDE.md)، [`GEMINI.md`](GEMINI.md) و
[`.github/copilot-instructions.md`](.github/copilot-instructions.md) —
هر چهار فقط به همان `AGENTS.md` ارجاع میدهند تا منبع حقیقت یکی بماند.

**ایندکس ماشینخوان:** `REPO_INDEX.json` · **بررسی سلامت اسناد:**
`python3 docs/verify_docs.py`

---

## دستورات طلایی

```bash
# تست و بررسی (اعداد مورد انتظار در docs/04_CURRENT_STATE.md)
npm test --prefix app                 # ۴۵/۴۵
npm run verify --prefix app           # ۵۴/۵۴ + ۵۱/۵۱
python3 app/tools/validate_content.py app/content/STARTER_PACKAGE.json app/content/STRUCTURED_PACKAGE.json
python3 docs/verify_docs.py           # لینکها و ایندکس

# ساخت خروجی (dist/ را دستی ویرایش نکن)
python3 app/tools/emit_structured_package.py   # بستهٔ محتوا
python3 app/tools/build_output.py               # Mimo.html + PWA + ZIP
python3 app/tools/process_book.py               # پیشنویس کتاب (خارج از گیت)

# اجرا
cd app && npm start                  # http://localhost:3000
```

---

## نگهداری این تحویل (برای ایجنتهای بعدی)

بعد از هر کامیت تازه: (۱) `docs/04_CURRENT_STATE.md` و `REPO_INDEX.json` را
بهروز کن (`python3 docs/build_repo_index.py`)؛ (۲) فهرست کامیتها را با
`git log --date=short --pretty=format:"%h %ad %s"` بازتولید کن؛
(۳) `python3 docs/verify_docs.py` را اجرا کن. اسناد تاریخی (`ANALYSIS/`،
`mimo-ui/UPGRADE/`) دستنخورده بمانند.

---

## سلسلهمراتب منبع حقیقت (بالا → پایین)

1. داراییهای دیکدشدهٔ APK و اسناد `ANALYSIS/MISSION_0*` = **واقعیت میمو**
2. `mimo-ui/UPGRADE/DESIGN/index.html` (v12.5-fa) + `CATALOGS/*.csv` = **طرح تأییدشدهٔ کاربر**
3. `app/content/MIMO_INFORMATION_FORM.json` = **قرارداد محتوا**
4. `app/src/*`, `app/assets/*` = **پیادهسازی**
5. `app/dist/*` = **خروجی ساختهشده** (تولیدی، دستکاری نشود)
6. `mimo-ui/UPGRADE/00…24_*.md` = **بایگانی دورهای طراحی** (حاوی بنرهای superseded؛ حکم فعلی نیستند)

> ⚠️ `app/README.md` و `app/content/README.md` جزئیات فنی فاز خودشان را دارند؛
> حکم کلی همیشه این `README.md` و `AGENTS.md` است.
