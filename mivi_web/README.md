# 🎬 Mivi AI — اپ وب تک‌فایل (تصویر + متن → ویدیو)

بازسازی مستقل خط لوله ابری **Mivi AI** (`instagram.story.art.collage`
نسخه ۲.۳۷.۴۰۷) در **یک فایل HTML واحد** — بدون نیاز به نصب، سرور جانبی یا pip.

## فایل

| فایل | نقش |
|---|---|
| `mivi_all_in_one.html` | کل اپ در یک فایل: رابط فارسی RTL، MD5 خالص JS، امضای درخواست‌ها، آپلود عکس، ساخت تسک، polling و دانلود ویدیو + دکمه دانلود پروکسی ویندوزی و پایتونی |
| `mivi_diagnostics.html` | ابزار تشخیص اتصال: تست شبکه، CORS واقعی سرور، پروکسی محلی و باتری پروکسی‌های عمومی + گزارش قابل کپی |
| `mivi-proxy-windows.bat` | پروکسی محلی تک‌فایل ویندوز با PowerShell داخلی (بدون نصب هیچ چیزی، دابل‌کلیک) |
| `RUN_PROXY_FA.md` | راهنمای کامل اجرای پروکسی به فارسی |

## نحوه استفاده

۱. فایل `mivi_all_in_one.html` را با مرورگر باز کنید (دابل‌کلیک، همان file://).
۲. عکس انتخاب کنید، پرامپت بنویسید و «تولید ویدیو» بزنید.
۳. ویدیوی ~۶ ثانیه‌ای در همان صفحه پخش و قابل دانلود است.

### اگر خطای CORS / Failed to fetch گرفتید

در همان فایل، بخش **«⚙️ تنظیمات اتصال و احراز هویت»** را باز کنید:

1. اول دکمه **«🔍 تست اتصال»** را بزنید. این تست با حالت `no-cors` تشخیص
   می‌دهد که سرور از شبکه شما اصلاً reachable هست یا مشکل فیلترینگ/DNS است،
   و separately مسیر CORS فعلی را آزمایش می‌کند.
2. راه‌حل مطمئن: دکمه **«⬇️ ساخت و دانلود فایل پروکسی محلی (proxy.py)»** را
   بزنید — فایل پایتونی (فقط کتابخانه استاندارد، بدون pip) دانلود و حالت
   اتصال خودکار روی «پروکسی محلی» می‌رود. سپس:
   ```bash
   python3 proxy.py
   ```
   و دوباره تولید ویدیو را بزنید. پروکسی فقط دامنه‌های `ufotosoft.com` و
   `videomate.cc` را فوروارد می‌کند.
3. اگر تست اتصال حتی با پروکسی محلی هم خطای شبکه داد، یعنی ISP شما دامنه را
   مسدود کرده و باید VPN روشن کنید.

امکانات دیگر: انتخاب هاست جایگزین `face-api.ufotosoft.com` یا
`face-api.videomate.cc`، پروکسی سفارشی با جایگره `{url}`، و گزارش URL کامل هر
درخواست در «گزارش مراحل».

> محدودیت پروکسی‌های عمومی: allorigins فقط GET است (آپلود POST کار نمی‌کند) و
> corsproxy.io ممکن است کلید/ثبت Origin بخواهد؛ بنابراین پروکسی محلی گزینه
> پیشنهادی است.

## پروتکل (استخراج‌شده از APK)

- هاست AIGC (اثبات‌شده از روی بایت‌کد classes7.dex): `https://cpi.ufotosoft.com`
  - مسیر زنجیره: `net.b.a()` ← `DebugAssemblyUtils$a.d()/c()` ← کلید
    `base_url_test/defaultUtl` با مقدار پیش‌فرض `https://cpi.ufotosoft.com`
  - `face-api.ufotosoft.com` و `face-api.videomate.cc` فقط مسیر درایور Tencent
    هستند و روی اندپوینت‌های AIGC پاسخ ۴۰۴ می‌دهند (با درخواست واقعی تأیید شد).
- **وضعیت زنده (تأییدشده با درخواست واقعی امضاشده):**
  - آپلود `POST /algo/v1/aiGenerate-aigc/multipleUpload` روی `cpi.ufotosoft.com`
    پاسخ `{"c":200,"m":"成功","d":["http://algo.ufotosoft.com/...jpg"]}` می‌دهد —
    یعنی کلید امضا `m3snil`، هدرها و فرمول MD5 کاملاً درست کار می‌کنند.
  - هاست زنده سرویس `https://cpi.ufotosoft.com` است (هاست دوم
    `cpi.wiseoel.com` همان بک‌اند را سرو می‌کند). `face-api.*` فقط درایور Tencent
    است و روی این مسیرها ۴۰۴ می‌دهد؛ `algo.ufotosoft.com` فقط CDN منابع است.
  - مسیر کوئری قدیمی `image2video/queryTask` منسوخ شده (۴۰۴). مسیر زنده نسخه ۴۰۷
    `POST /algo/v1/faceFusion/aigc/image2VideoQuery` با بدنه `{"taskId":"..."}`
    است (روی تسک ناموجود `c=3036 IMAGE2VIDEO_TASK_OVERTIME` برمی‌گرداند).
  - مسیر ساخت تسک: `POST /algo/v1/faceFusion/aigc/image2video/unifiedTaskCreate`.
    بدنه (استخراج از `Image2VideoServer$createAiVideoUnifiedTask$1`):
    `imageUrls` (آرایه URLهای آپلودشده)، `level` (int)، `deviceToken` (رشته)،
    `prompt`/`ratio`/`movementAmplitude` (اختیاری)، و **`example` (اجباری، غیرخالی؛
    سرور روی حالت خالی `c=400 Parameter error [example不能为空]` می‌دهد)**؛ اپ
    مقدار example را از همان URL تصویر می‌فرستد.
  - پاسخ: پاکت `{c,m,d}` و `d` از نوع `CreateVideoResponse` با فیلدهای
    `taskId, taskStatus ("success"/"fail"/در حال پردازش), taskReason, videoUrl`.
  - صفحه دایگنستیک «پروب C» ماتریس هاست × مسیر را اسکن می‌کند و «پروب D» یک
    آپلود تازه + چهار ترکیب مختلف `example/level` برای unifiedTaskCreate را
    با امضای صحیح `MD5(signKey+ts)` و هدر `userId` بزرگ (بدون ifWise) تست
    می‌کند و در صورت ساخت تسک، سه بار با image2VideoQuery وضعیتش را پول می‌کند.
  - دامنه `wiseoel.com` به allow-list هر دو پروکسی (bat و python) اضافه شده؛
    اگر نسخه قدیمی بات در حال اجراست، فایل جدید را دانلود و جایگزین کنید.
- signKey ثابت: **`m3snil`** (رمزگشایی DES/CBC از رشته هاردکد `hCzXemhkIkY=`)
- **فرمول امضا (تصحیح‌شده با اثبات زنده + بایت‌کد): همه فراخوانی‌های سرویس
  الگوریتمی `g` و آپلود، `sign = MD5(signKey + زمان‌یونیکس)` یعنی
  `MD5("m3snil" + ts)` هستند.** فرمول قبلی `MD5(userId+ts)` غلط بود و سرور با
  `c=1009 "Auth fail [sign illegal]"` ردش می‌کرد (اثبات زنده ۲۰۲۶-۱۰-۲۶).
  محل بایت‌کد: `Image2VideoServer$createAiVideoUnifiedTask$1` و
  `$queryAiPhotoTask$1` که آرگومان اول سازنده‌شان `signKey` است و
  `wa.a.g(signKey + ts)` را به‌عنوان sign می‌فرستند.
- هدرها مطابق Annotation پارامترهای Retrofit:
  - ساخت تسک `g.l` (unifiedTaskCreate): `userId` (بزرگ)، `timeStamp, cp,
    version, platform, sign` — **بدون ifWise**
  - `g.c0` (integratedTaskCreate): همان‌ها با `userId` بزرگ + `ifWise=true`
  - کوئری `g.b` (image2VideoQuery): `userid` (کوچک)، `timeStamp, cp, version,
    platform, sign, ifWise=true`
  - آپلود: `cp, version, platform, sign, timeStamp, userId, ifHttps=true`
- اندپوینت‌های استفاده‌شده در فایل:
  - `POST /algo/v1/aiGenerate-aigc/multipleUpload` (multipart، فیلد `files`)
  - `POST /algo/v1/faceFusion/aigc/image2video/unifiedTaskCreate`
  - `POST /algo/v1/faceFusion/aigc/image2video/queryTask`
- `userId` به‌صورت محلی ساخته و در `localStorage` ذخیره می‌شود؛ هیچ
  ثبت‌نام/لاگینی در پروتکل اپ وجود ندارد.

## تست‌ها

- MD5 جاوااسکریپت با Node `crypto` روی بردارهای معروف، متن فارسی (UTF-8) و
  فرمول‌های امضا تطبیق کامل دارد.
- سینتکس کل اسکریپت داخل فایل با Node بررسی شده است.
