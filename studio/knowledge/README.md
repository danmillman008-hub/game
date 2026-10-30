# knowledge — the bank

یک جای واحد برای هر چیزی که از بیرون یاد گرفته‌ایم. هدفش این است که دانش
**قابل بازبینی** بماند، نه اینکه در چت گم شود.

```
knowledge/
├── repos.json        ⇐ منبع حقیقت: هر ریپویی که بررسی کردیم، با اعداد زنده
├── BANK.md           ⇐ از repos.json ساخته می‌شود (دستی ویرایش نکن)
├── learnings.md      ⇐ درس‌ها: اعداد سینمایی، تله‌های لایسنس، تله‌های محیط
├── measurements.json ⇐ اعداد اندازه‌گیری‌شدهٔ TTS روی رانر (RTF، بایت، sha256)
├── bank.py           ⇐ check / verify / export / stats / list
└── measure.py        ⇐ رندر را به عدد تبدیل می‌کند
```

## چرا JSON و نه فقط markdown

جدول دست‌نویس فردا غلط است: `piper` ارگ عوض کرد، `Wav2Lip` هنوز لایسنس ندارد،
`video-shotcraft` نام owner عوض شد. فایل JSON را می‌شود در ۵۵ ثانیه با API گیت‌هاب
دوباره چک کرد و **دقیقاً** فهمید چه چیزی تغییر کرده. `BANK.md` هم از همان JSON
تولید می‌شود تا خواندنی و داده هرگز از هم جدا نشوند.

## فیلدهای هر ریپو

| فیلد | معنی |
|---|---|
| `repo` | `owner/name` — کلید یکتا |
| `gap` | کدام گپ از `studio/GAPS.md` را پر می‌کند |
| `verdict` | `take` (استفاده می‌کنیم) · `study` (الگوریتم را می‌خوانیم، کد را نه) · `avoid` |
| `note` | چرا — با عدد، نه صفت |
| `stars` `license` `pushed_at` `archived` | **تولیدشده توسط `verify`**، هرگز دستی |

`verdict = study` معمولاً یعنی GPL یا رهاشده: ایده را برمی‌داریم، کد را نه.

## اجرا

```bash
python3 studio/knowledge/bank.py check     # ساختار درست است؟
python3 studio/knowledge/bank.py stats     # چند تا، به تفکیک گپ و حکم
python3 studio/knowledge/bank.py list --verdict take
python3 studio/knowledge/bank.py verify    # گیت‌هاب را می‌خواند و drift را می‌گوید
python3 studio/knowledge/bank.py export    # BANK.md را بازمی‌سازد
```

## اندازه‌گیری، نه ادعا

`measurements.json` را هیچ‌کس دستی ننوشته. این زنجیره آن را ساخته:

```
.github/workflows/voice.yml
  → مدل‌ها را روی رانر دانلود می‌کند (۱۴۲MB انگلیسی + ۶۴MB فارسی)
  → voice.py render روی films/voice_probe
  → measure.py  (مدت، بایت، RTF، sha256 هر خط + مشخصات ماشین)
  → git commit  ⇐ اعداد به برنچ برمی‌گردند
```

چون سندباکسی که کد را می‌نویسد به CDN و HuggingFace دسترسی ندارد، **رانر
ابزار اندازه‌گیری است**. هر عددی که در `learnings.md` می‌بینی از همان‌جا آمده.

## تست

```bash
python3 studio/knowledge/banktest.py     # آفلاین، بدون شبکه
```

## افزودن ریپو

```python
{"repo": "owner/name", "url": "https://github.com/owner/name",
 "gap": "lipsync", "verdict": "study", "note": "چرا — با عدد",
 "stars": null, "license": null, "pushed_at": null}
```
بعد: `bank.py verify --update && bank.py export`. ستاره‌ها را دستی ننویس.
