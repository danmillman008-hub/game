# ۰۵چ — قرارداد اجرای کد درس (Executable lessons)

**پایه:** ۴,۰۲۴ درس از نوع `executableFiles`؛ همهٔ محتوا در بسته؛ **بدون تست در کلاینت**.

## ۱. بار داده (VERIFIED_STATIC)

```json
{
  "instructions": "Add an `a` element that links to `/x.html` …",   // markdown سبک با backtick
  "preselectedFileIndex": 0,
  "hasVisualOutput": true,                  // پیش‌نمایش HTML لازم است
  "files": [ { "name": "index.html", "codeLanguage": "html",
               "content": "…", "solvedContent": "…" } ],
  "hints": [ { "title": "…", "content": "…" } ],
  "httpOptions": { … },                     // فقط ۸۵ درس (HTTP/API exercises)
  "sourceDatabaseTables":   [ … ],          // ۲۶۹ درس (SQL/Node)
  "solutionDatabaseTables": [ … ]
}
```

| سنجه | مقدار |
|---|---|
| درس کدی | ۴,۰۲۴ |
| فایل در درس کدی | ۶,۷۴۶ (همه با `codeLanguage`, `content`, `solvedContent`) |
| `solvedContent` غیر null | ۶,۷۰۴ (۴۲ فایل null ⇒ شکاف محتوا) |
| درس با `httpOptions` | ۸۵ |
| درس با جدول DB | ۲۶۹ |
| درس با راهنما | ۵۲۷ |

## ۲. آنچه در بسته **نیست** (مهم‌ترین شکاف)

| مورد | وضعیت | نتیجه |
|---|---|---|
| فایل تست | **NOT_ACCESSIBLE** | تست در کلاینت نیست |
| تعریف «درست» | فقط `solvedContent` | مقایسه با راه‌حل، یا اجرای سمت سرور |
| sandbox اجرا | در بسته نیست | `librive`/`libyrf` ارتباطی به اجرا ندارند |
| محدودیت CPU/زمان | نامعلوم | — |

## ۳. مسیرهای API مرتبط (VERIFIED_STATIC از annotationها)

| مسیر | فعل | نقش |
|---|---|---|
| `/v1/code/runfiles` | POST (MEDIUM) | اجرای فایل‌ها |
| `/v1/code` | POST (MEDIUM) | اجرای تک‌فایل/ذخیره |
| `/v1/code/{savedCodeId}/remixes` | POST | بازآفرینی کد ذخیره‌شده |
| `/v1/tutorials/{id}/chapters/{id}/lessons/{id}/savefiles` | POST | ذخیرهٔ فایل درس |

⇒ مدل عملی: کلاینت فایل‌ها را می‌فرستد، سرور اجرا و مقایسه می‌کند، نتیجه به شکل
درست/نادرست + خروجی برمی‌گردد. **این استنتاج است، نه مشاهدهٔ پاسخ** (`INFERRED`, MEDIUM).

## ۴. طرح پیشنهادی برای محصول مستقل (بخش الزامی «build-ready»)

سه گزینه با هزینه/کیفیت:

| گزینه | اجرا | تصحیح | هزینه | کیفیت بازخورد |
|---|---|---|---|---|
| A. محلی (WASM) | Pyodide/JS sandbox در WebView | diff ساختاری با `solvedContent` + تست نامرئی | کم | متوسط |
| B. سرویس اجرا | runner ایزوله (Firecracker/gVisor) | تست‌های واقعی (JUnit/pytest/stdout) | بالا | بالا |
| C. ترکیبی | JS/Python محلی، SQL محلی، بقیه سرویس | دو مرحله | متوسط | بالا |

**توصیه:** C. برای کنکور، اجرای کد لازم نیست؛ «آزمون شبیه‌سازی» است. اجرای کد فقط برای درس‌های
مهارتی (ریاضی/آمار با اجرای SQL یا Python) ارزش دارد.

**الزامات امنیتی اجرای محلی:** بدون شبکه، بدون دسترسی فایل، سقف ۲ ثانیه CPU، سقف حافظه ۶۴MB،
توقف روی حلقهٔ بی‌پایان، و لاگ خروجی در حافظه.

## ۵. شکاف‌های قابل ثبت

1. `httpOptions` ساختارش فقط ۸۵ نمونه دارد و بدون نمونهٔ کامل قابل بازسازی نیست — **UNKNOWN**.
2. تصحیح SQL: مقایسهٔ مجموعهٔ ردیف‌ها یا ترتیب‌دار؟ **UNKNOWN**.
3. `preselectedFileIndex` برای UX است، نه سنجش.
4. زبان `swift` (۶۴۳ فایل) اجرا در اندروید ندارد ⇒ در Mimo احتمالاً فقط نمایش/مقایسه است (INFERRED).
