# game — Mivi film studio

ساخت فیلم انیمه با مدل ویدیویی Mivi، از شیت کاراکتر تا فیلم تدوین‌شده. همه‌چیز
روی گیت‌هاب اجرا می‌شود؛ سندباکس فقط کد می‌نویسد.

**دانش پروژه، همه در یک جا: [`studio/knowledge/`](studio/knowledge/README.md)**
(روش، پرامپت، خط تولید، بانک ۵۴ ریپو، اعداد اندازه‌گیری‌شده، تحویل‌ها)

## نقشه

```
studio/                 ابزار تولید
├── mivi_shot.py        تولید روی رانر: --parallel --dry-run --skip-existing
├── shotplan.py         فایل صحنه → جاب‌فایل موازی (لنگر، زنجیره ≤۲)
├── artgen.py           کانواس خالی → تصویر (بدون تصویرساز)
├── wanprompt.py        ممیزی پرامپت طبق قرارداد رسمی Wan I2V
├── motionbank.py       بانک حرکت + lint
├── filmkit.py          تدوین: assemble / subtitle / …
├── toolbox/upscale.py  آپ‌اسکیل انیمه (Anime4K / Real-ESRGAN، CPU)
└── knowledge/          ← همهٔ دانش این‌جاست

films/<name>/           یک پروژه: project.json منبع حقیقت
films/anime_ten/        فیلم انیمه (refs، canvas، art، clips، deliver، qc)
bridge/                 پل Mivi ↔ ابزارها (mivi_mcp.py، mivi_bridge.py)
mivi_web/               مهندسی معکوس اپ: API_MAP.md (نقشهٔ ۶۱ اندپوینت)
_inbox/                 فایل‌هایی که ربطی به خط تولید ندارند
```

## سه دستور که ۹۰٪ کار را می‌کنند

```bash
# ۱. صحنه را پلن کن — پرامپت ناقض و زنجیرهٔ عمیق را رد می‌کند
python3 studio/shotplan.py plan studio/motions/scenes/gate.json \
        --out films/short16/gen_jobs_gate.json --parallel 4

# ۲. ببین چه چیزی خرج می‌شود (بدون تولید)
python3 studio/mivi_shot.py films/short16/gen_jobs_gate.json --out out --dry-run

# ۳. روی رانر تولید کن
printf 'films/short16/gen_jobs_gate.json\n' > .mivi-trigger   # و push کن
```

تریگرها: `.mivi-trigger` (تولید) · `.toolbox-trigger` (آپ‌اسکیل) · `.photo-trigger`
(پروب اندپوینت عکس) · `.render-trigger` (رندر). هر کدام نام فایل جاب را در خط اول
می‌گیرند؛ ورک‌فلو همان را می‌خواند.

## قواعد سختِ این ریپو

1. **عدد، نه صفت.** هر ادعای کیفیت باید اندازه‌گیری شده باشد و مسیرش در
   `studio/knowledge/` باشد.
2. **کامپوزیت PIL ممنوع** برای ساخت کی‌فریم ویدیو. (دلیل: `knowledge/method/ANIME_METHOD.md`)
3. **پرامپت Wan**: زیر ۱۰۰ کلمه، فقط حرکت، بدون توصیف چیزهایی که در فریم است.
4. **زنجیره حداکثر ۲ حلقه**؛ بعد از آن لنگر جدید.
5. **هیچ تولیدی بدون `--dry-run`**.

## آیا ریپو سالم است؟

```bash
python3 studio/verify.py          # یا: make verify
```

یک پاس آفلاین، نُه گروه:

| گروه | چه چیزی را ثابت می‌کند |
|---|---|
| `inventory` | هر `.py`/`.yml` در `studio/inventory.json` ثبت است و هر ردیف به فایل موجود اشاره می‌کند |
| `data` | هر ۶۲ فایل JSON و هر ۸ workflow بپارس |
| `triggers` | هر `.*-trigger` به چیزی اشاره می‌کند که وجود دارد |
| `deps` | وابستگی‌های اعلام‌شده با importهای واقعی هر فایل می‌خواند |
| `links` | هیچ مسیر مرده‌ای در md/py/yml نیست؛ فایل غول (>۲۰MB) دیده می‌شود |
| `make` | هر target در `.PHONY` واقعاً resolve می‌شود (`make -n`) |
| `selftest` | خودِ چک با نقص‌های تزریق‌شده سنجیده می‌شود |
| `compile` | هر ۴۰ فایل `.py` کامپایل می‌شود |
| `smoke` | `--help` هر CLI و اجرای واقعی تست‌ها |

`REPO_STATUS.md` از همین نتیجه‌ها ساخته می‌شود، نه دستی.

`REPO_STATUS.md` را همین دستور می‌نویسد؛ هر کس اجرا کند نسخهٔ خودش را می‌گیرد
(تاریخ و نام محیط بالای فایل است). رانر آن را در خلاصهٔ همان اجرا (job summary) و
به‌عنوان artifact منتشر می‌کند و در گیت commit نمی‌کند — وگرنه هر push با نسخهٔ
تولیدشدهٔ محلی تضاد پیدا می‌کند.

گروه `selftest` خودِ چک را می‌آزماید: در هر اجرا چند نقص عمداً تزریق می‌شود و اگر
چک آن‌ها را نگیرد، build قرمز می‌شود. روی گیت‌هاب `verify.yml` با `--ci` اجرا می‌شود:
آنجا تنها فایلی که مجاز است اجرا نشود `studio/toolbox/upscale.py` است (استک torch،
~۲.۵ گیگ) و دلیلش در همان ردیف نوشته می‌شود؛ بقیه باید واقعاً اجرا شوند.

## وضعیت

| فیلم | وضعیت |
|---|---|
| `films/anime_ten` | صحنهٔ ۶۰ ثانیه‌ای، ۱۵ شات، نسخهٔ ۲ با پرامپت Wan — [لینک](studio/knowledge/delivery/DELIVERY.md) |
| `films/short16` | کارگاه: آرت، زنجیره، بچ‌های آزمایشی |
| `films/before_leaving` | پروژهٔ کامل قبلی (صدا + لب‌سینک) |
