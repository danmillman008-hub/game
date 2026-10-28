# 🎬 Mivi AI — اپ وب تک‌فایل (تصویر + متن → ویدیو)

بازسازی مستقل خط لوله ابری **Mivi AI** (`instagram.story.art.collage`
نسخه ۲.۳۷.۴۰۷) در **یک فایل HTML واحد** — بدون نیاز به نصب، سرور جانبی یا pip.

## فایل

| فایل | نقش |
|---|---|
| `mivi_all_in_one.html` | کل اپ در یک فایل: رابط فارسی RTL، MD5 خالص JS، امضای درخواست‌ها، آپلود عکس، ساخت تسک، polling و دانلود ویدیو + دکمه دانلود پروکسی ویندوزی و پایتونی |
| `mivi_diagnostics.html` | ابزار تشخیص اتصال: تست شبکه، CORS واقعی سرور، پروکسی محلی و باتری پروکسی‌های عمومی + گزارش قابل کپی |
| `mivi_veo_probe.html` | آزمایشگاه زندهٔ موتور Veo/V5: باتری ۱۶ پروبی سیستماتیک روی `image2VideoCreateV5` و اندپوینت‌های هم‌خانواده برای کشف شرط بازشدن Veo + بخش ارسال دستی با بدنهٔ JSON آزاد |
| `mivi-proxy-windows.bat` | پروکسی محلی تک‌فایل ویندوز با PowerShell داخلی (بدون نصب هیچ چیزی، دابل‌کلیک) |
| `catalog_effects.json` | خلاصهٔ ۳۱۰ افکت کاتالوگ زندهٔ سرور (گروه، نام، effectsType، نسبت، تک/چندنفره) — نسخهٔ فشرده‌اش داخل HTML جاسازی شده |
| `RUN_PROXY_FA.md` | راهنمای کامل اجرای پروکسی به فارسی |

## نحوه استفاده

۱. فایل `mivi_all_in_one.html` را با مرورگر باز کنید (دابل‌کلیک، همان file://).
۲. حالت تولید را انتخاب کنید:
   - **✍️ پرامپت اختصاصی (Make AI Video):** عکس + متن دلخواه خودتان + کلید
     کیفیت 360P (`quality=1`) / 720P (`quality=2`). این معادل دقیق همان بخش
     «Make AI Video» اپ است (نه افکت‌های آماده).
   - **🎞️ افکت آمادهٔ کاتالوگ:** یک افکت از ۳۱۰ قالب (پیش‌فرض Catwalk/4991 که
     تست زندهٔ موفق با آن انجام شد) + پرامپت اختیاری.
۳. «تولید ویدیو» بزنید؛ ویدیوی ~۶ ثانیه‌ای (معمولاً ظرف ۱۵–۳۰ ثانیه) در همان
   صفحه پخش و قابل دانلود است.

## 🔬 زنجیره کامل «Make AI Video» (استخراج کامل از APK، classes5–7)

مسیر دقیق دکمهٔ 720P/360P با تصویر و پرامپت شخصی، از UI تا سرور:

1. `AiToolsFragment` (گروه `Custom_Ai_Video`، category=1402، از
   `ToolsResponseKt.transform`/`AiToolsDataKt.transform`) →
   `AiToolVideoHugActivity` (روت `/edit/aiphoto_ai_tool_hug`)، آبجکت
   `TemplateItem` با extra `key_mv_entry_info`.
2. متد `Z3()`: مدل آنالیتیکس `model = "720p"` اگر سوئیچ `binding.k0` تیک خورده
   باشد وگرنه `"360p"`؛ تک‌تصویر = type `aivideo`/phototype 1.
3. `K3()` → `processSingle$1` (کراپ/فشرده‌سازی) → `o3()` → `K2()`:
   `TemplateItem.setPrompt(متن کاربر)` و `setQuality(2 برای 720P / 1 برای 360P)`،
   سپس روت `/gallery/facecombinetask` با `face_fusion_from=custom_aivideo`.
4. `CombineTaskActivity` چون `groupName == "Custom_Ai_Video"` (متد `a1()`)
   پیش‌بارگذار `com.gallery.preload.f0` و ابزرور
   `com.gallery.facefusion.observer.g` را انتخاب می‌کند.
5. `observer.g.k0()`:
   - userId = شناسهٔ دستگاه (`com.ufotosoft.base.d.c.a().b()`)،
   - signKey = رمزگشایی DES/CBC/PKCS5 از `hCzXemhkIkY=` با کلید `IM41OUCa` و
     IV `12345678 90ABCDEF` → **`m3snil`** (به‌صورت مستقل در پایتون تأیید شد)،
   - `P2Type.GX_AiVideoP2V` (ثابت؛ نوع وئو با کیفیت عوض نمی‌شود)،
   - اگر گروه Custom_Ai_Video باشد: `f.R(prompt)` و `f.S(quality)`.
6. `Image2VideoTask.e2()` → جدول `$b` case 9 → `b3()` → `j3()` → `g3()` →
   کوروتین `startSequenceVideo$2` → فشرده‌سازی JPEG →
   `Image2VideoServer.y()` → کوروتین **`createGXAiVideoTask$1`**.
7. **درخواست نهایی HTTP (همان اندپوینت اثبات‌شدهٔ beat، نه مسیر جداگانهٔ Veo):**
   - `POST /algo/v1/faceFusion/aigc/beatImage2Video/createNormalTask`
     (متد Retrofit `g.P`)
   - هدرها (از annotation پارامترها): `userid, timeStamp(ثانیه), cp, version,
     platform, sign=MD5("m3snil"+ts), ifWise=true` + `Content-Type: application/json`
   - بدنه:
     ```json
     {"imageUrls":["<url آپلودشده>"], "level":1, "effectType":6209,
      "imageEffectType":<فقط اگر ناصفر — در حالت سفارشی وجود ندارد>,
      "prompt":"<متن کاربر>", "quality":2}
     ```
     (`imageEffectType` در حالت سفارشی صفر و حذف می‌شود؛ `prompt` فقط اگر
     خالی نباشد؛ `quality` همیشه 1 یا 2).
   - کوئری: `POST .../beatImage2Video/queryTask` با `{"taskId":"..."}`
     (متد `g.M`)، لغو: `.../cancelTask` (متد `g.r`).

**نکته کلیدی — بازبینی کامل موتور (۲۰۲۶-۱۰-۲۸، هر ۸ دکس + همهٔ کتابخانه‌های
`.so`):** کلاس‌های `AiVideoGoogleVeo` / `startGoogleVeoVideo$2` /
`createGoogleVeoVideoTask$1` به مسیر **جداگانهٔ**
`/algo/v1/faceFusion/aigc/image2video/image2VideoCreateV5` (متد `g.g0`، با
فیلدهای `googleId/deviceToken/audio/duration/ifTest`) تعلق دارند و P2Type آن‌ها
`AiVideoGoogleVeo=10` است. ادلهٔ قطعی خفته‌بودن این مسیر در نسخهٔ ۲.۳۷.۴۰۷:

1. در کل APK تنها سه جا P2Type روی پارامتر ست می‌شود (`f.P`/`e.A`):
   `observer.g.k0 → GX_AiVideoP2V`، `observer.b.k0 → AiVideoLtx` و
   `AiVideoLtxEditInterface → LTX`. **هیچ‌کدام Veo را ست نمی‌کند.**
2. تنها `sget` مقدار `AiVideoGoogleVeo` خارج از جدول‌های switch در متد سنتتیک
   `Image2VideoTask.d3` است که فقط از `e2` case 3 صدا زده می‌شود؛ ورودی آن
   (`f.l()` به‌عنوان `veoId`) هیچ ست‌کننده‌ای در کل اپ ندارد و
   رشته‌های `googleVeoId/googleVeoEnableAudio` هیچ ارجاع کدی ندارند.
3. کلمهٔ «gemini» هیچ‌جای APK نیست؛ رشتهٔ «Veo» فقط در همین کد خفته است و
   هیچ کتابخانهٔ nativeای حاوی اندپوینت/موتور شبکه نیست (همهٔ `.so`ها
   اف‌اف‌مپگ، فیس‌ترکینگ، تبلیغات و آنالیتیکس‌اند).

بنابراین زنجیرهٔ «Make AI Video» خود اپ — در هر دو کیفیت 360P و 720P — فقط
همان سرویس beat را صدا می‌زند و تفاوت کیفیت تنها فیلد `quality` است. انتخاب
موتور واقعی تولید (Wan-LoRA/Veo/…) سمت **سرور** انجام می‌شود و کلاینت هیچ
پارامتر انتخاب موتوری ندارد؛ تنها نشانهٔ قابل مشاهده، نام فایل داخل `videoUrl`
است (مثلاً `img2video_wanlora-….mp4`). اپ وب این موتور را از روی لینک خروجی
در گزارش مراحل اعلام می‌کند و بخش
**«🧪 آزمایشگاه موتور Google Veo / Gemini (مسیر V5)»** امکان تست زندهٔ مستقیم
اندپوینت V5 را فراهم می‌کند تا پاسخ دقیق سرور (شرط بازشدن Veo، احتمالاً
`googleId` معتبر) ثبت شود. (لوگوی Gemini روی خروجی، در صورت وجود، سمت سرور
روی همین بک‌اند اعمال می‌شود، نه از طریق یک اندپوینت کلاینت دیگر.)

شمارندهٔ محدودیت روزانهٔ اپ (`_custom_aivideo_<تاریخ>` در SharedPreferences،
کلاس `com.ufotosoft.base.c`) کاملاً سمت کلاینت است؛ فراخوانی مستقیم API این
مرز را ندارد. گیت پریمیوم (`com.ufotosoft.common.utils.q.b`) هم فقط در UI
بررسی می‌شود و در بدنهٔ درخواست چیزی جز `quality` وجود ندارد.

### تست زندهٔ اندپوینت V5 (۲۰۲۶-۱۰-۲۸)

فراخوانی مستقیم `image2video/image2VideoCreateV5` با بدنهٔ وفادار به بایت‌کد
(googleId/deviceToken خالی) پاسخ زندهٔ زیر را داد:

```json
{"c":500,"m":"Internal Server Error [NumberFormatException: For input string: \"\"]","d":null}
```

نکات استنتاجی و تکامل تست‌های زنده:

- اندپوینت **زنده و معتبر** است (404 نیست) و هدرهای امضای ما پذیرفته می‌شود.
- مرحله ۱ — فیلد خالی: سرور یکی از دو فیلد (`googleId` یا `deviceToken`) را
  عددی پارس می‌کند و با `NumberFormatException: For input string: ""` رد می‌کند.
- مرحله ۲ — با `googleId/deviceToken="0"`: خطای پارس عددی کامل برطرف و پاسخ به
  `c=1013 param error: effectType illegal` تغییر کرد. یعنی V5 همان اعتبارسنجی
  پارامتری مسیر beat را دارد و یک `effectType` معتبر (۶۲۰۹) می‌خواهد. کارت Veo
  در فایل اصلی و باتری پروب از این مرحله به بعد `effectType=6209` و `quality`
  را خودکار در بدنه می‌گذارند.
- در بایت‌کد تأیید شد که فیلدهای `h.J` (deviceToken) و `h.I` در کل اپ
  هیچ‌وقت نوشته نمی‌شوند (مقدار پیش‌فرض null/0) — پس هیچ مقدار کلاینتی برای
  کپی‌کردن وجود ندارد و هر مقدار معنادار برای این فیلدها باید از سمت
  سرور/کانفیگ ابری تخصیص داده شود.
- `mivi_veo_probe.html` با ۱۶ پروب این فرضیه را می‌آزماید: دو لنگر خطاهای
  شناخته‌شده، سپس ترکیب‌های ۶۲۰۹ با صفر/عدد تصادفی/حذف فیلد/حذف ifTest/
  audio/duration/quality، اندپوینت‌های هم‌خانواده
  (unifiedTaskCreate/createTask/integratedTaskCreate/V4) و یک کنترل beat با
  تشخیص موتور از روی نام فایل خروجی. هر پاسخ خام به‌همراه traceId ثبت می‌شود.
- در فایل اصلی هم کارت آزمایشگاه Veo با «حالت پر کردن فیلد خالی» (دقیق/حذف/صفر/تصادفی)
  به‌روزرسانی شد.

مرحله ۳ — باتری ۱۶ پروبی زنده (همان جلسه):

- V5 با `effectType=6209` (و کیفیت/پرامپت/صوت/مدت متنوع) همیشه
  `c=1013 effectType illegal` داد؛ یعنی V5 رجیستری effectType **جدا از beat**
  دارد و ۶۲۰۹ در آن معتبر نیست.
- حذف googleId از بدنه V5 → `c=400 googleId不能为空`: googleId فیلد اجباری
  حضور‌ی است و `"0"` فقط چک خالی‌نبودن را رد می‌کند.
- `image2video/unifiedTaskCreate` → `c=400 example不能为空` و
  `image2video/integratedTaskCreate` → `c=1013 "example" is empty or illegal`.
  از بایت‌کد `createAiVideoUnifiedTask$1`: بدنهٔ این مسیر
  `imageUrls, level, deviceToken, prompt, ratio, movementAmplitude, example,
  ifTest` است و اصلاً effectType ندارد.
- `image2video/createTask` روی سرور استقرار ندارد (HTTP 404 واقعی)؛
  `integrated/image2VideoCreateV4` هم ۶۲۰۹ را با `c=1001 effectType illegal` رد کرد.
- کنترل `beatImage2Video/createNormalTask` با همان بدنهٔ ۶۲۰۹/quality=2 پاسخ
  `c=200` و taskId گرفت — اثبات دوبارهٔ اینکه تنها مسیر کاریِ این کلاینت beat است.
- باتری نسخهٔ c (۱۸ پروب): جاروب ۱۰ کد effectType روی V5 (۰،۱،۲،۵،۱۰ و کدهای
  کاتالوگ ۴۹۹۱/۴۸۹۹/۵۲۹۱/۶۰۹۳/۷۹۶۹) برای کشف رجیستری V5، و سه حالت ارسال
  `example` (رشته خالی / URL تصویر / حداقلی) روی unified و integrated.
  نتیجهٔ زنده: **همهٔ ۱۰ کد effectType روی V5 همان `1013 effectType illegal`
  را دادند** — یا رجیستری V5 کاملاً جداست یا اعتبارسنجی به googleId گره خورده
  و با شناسهٔ `"0"` هیچ کدی معتبر نیست. `example` با URL تصویر هم با
  `"example" is empty or illegal` رد شد (example تصویر نیست). assets اپ
  (AdConfig/SceneConfig/aigc/lock) فقط تبلیغات/انیمیشن Lottie‌اند و هیچ کانفیگ
  V5/example ندارند؛ رشتهٔ `example` فقط در classes6 و فقط به‌صورت خواندن از
  HashMap وجود دارد.
- باتری نسخهٔ d (۱۶ پروب): فرضیهٔ `example = videoPreviewUrl` (ویدیوی نمونهٔ
  قالب‌های کاتالوگ، مثل `res.wiseoel.com/common/video/UF…_press.mp4`) روی
  unified/integrated با بدنهٔ دقیق بایت‌کد (بدون effectType، با
  ratio/movementAmplitude)، حالت‌های مختلف ifTest، و چند واریانت V5 برای
  کشف ترتیب اعتبارسنجی googleId. نتیجهٔ زنده: روی unified/integrated همان
  `"example" is empty or illegal` و روی V5 با حضور فیلد example خطا به
  **`c=1001 example illegal`** تغییر کرد (به‌جای 1013 effectType) — یعنی سرور
  example را می‌بیند ولی URL ویدیوی کاتالوگ برایش قانونی نیست؛ googleId=1 هم
  رفتار را عوض نکرد. اندپوینت‌های `image2VideoCustomer/*` در کل APK بدون هیچ
  ارجاع کدی‌اند (فقط رشتهٔ Retrofit یتیم) — مسیر ساخت قالب مشتری هم در دسترس نیست.
- باتری نسخهٔ e (۱۶ پروب): سه پروب اول کوئری تسک‌های beat موفق همین جلسه از هر
  دو اندپوینت queryTask برای کشف `videoUrl` و موتور واقعی خروجی (نام فایل، مثل
  wanlora/veo)؛ سپس `example` به‌صورت رشته/عدد ۴۹۹۱، ۶۲۰۹، taskId و videoUrl
  همان تسک روی unified/integrated/V5 تست می‌شود. نتیجهٔ زنده:
  - `image2video/queryTask` استقرار ندارد (HTTP 404)؛ فقط
    `beatImage2Video/queryTask` جواب می‌دهد.
  - خروجی‌های موفق beat با **نام‌گذاری هشی بدون برند** برمی‌گردند
    (`algo-v1.wiseoel.com/temp/60014/261029/<32hex>.mp4`) — برخلاف تست‌های
    اولیه که `img2video_wanlora-…mp4` بود؛ یعنی موتور از روی URL قابل تشخیص نیست.
  - همهٔ فرمت‌های example (رشته/عدد ۴۹۹۱ و ۶۲۰۹، taskId، videoUrl خود تسک،
    URL ویدیوی کاتالوگ، URL عکس) رد شدند: unified/integrated همیشه
    `1013 "example" is empty or illegal` و V5 همیشه `1001 example illegal`.
    هیچ مقدار example در داده‌های کلاینت (دکس/کاتالوگ/assets) وجود ندارد.
- نسخهٔ f — کارت فارنزیک MP4 درون‌مرورگری: چون برند موتور در URL نیست، خود فایل
  ویدیو دانلود و اتم‌های MP4 پارس می‌شوند (ftyp/برندها، رزولوشن واقعی avc1/hvc1
  برای اثبات 720P در برابر 360P، مدت از mvhd، هندلرهای hdlr، و اسکن رشته‌های
  ASCII برای نشانه‌های موتور مثل wan/veo/kling/vidu/encoder). دکمهٔ
  «تست مقایسه‌ای» دو تسک beat با quality=1 و quality=2 می‌سازد و هر دو ویدیو را
  کنار هم تحلیل می‌کند تا تفاوت واقعی کیفیت سمت سرور اثبات شود.

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
  - مسیر کوئری قدیمی `image2video/queryTask` منسوخ شده (۴۰۴).
  - **مسیر ساخت تسک اثبات‌شده با تست زندهٔ کامل (۲۰۲۶-۱۰-۲۶):**
    `POST /algo/v1/faceFusion/aigc/beatImage2Video/createNormalTask` (متد
    Retrofit `g.P`، از بایت‌کد `Image2VideoServer$createGXAiVideoTask$1`).
    بدنه: `{"imageUrls":["..."],"level":1,"effectType":4991,"prompt":"..."}`
    (حالت افکت کاتالوگ) — **فیلد `example` ندارد**؛ `effectType` شناسهٔ افکت
    از کاتالوگ زندهٔ سرور است. در حالت Make AI Video همان اندپوینت با
    `effectType=6209` (کد هاردکدشدهٔ `ToolsResponseKt.transform` برای گروه
    `Custom_Ai_Video`؛ در فیلد `TemplateExtra.effectsType` قرار می‌گیرد و
    `observer.g` آن را به `f.M` → فیلد `effectType` بدنه می‌دهد) و فیلد اضافهٔ
    `quality` (1=360P، 2=720P) صدا زده می‌شود. **تست زنده ۲۰۲۶-۱۰-۲۸ نشان داد
    سرور `effectType=0` را با `c=1013 "param error: effectType illegal"` رد
    می‌کند**؛ کد صحیح همان 6209 است (جزئیات کامل در بخش «زنجیره کامل Make AI
    Video» بالاتر). کوئری همتای آن:
    `POST /algo/v1/faceFusion/aigc/beatImage2Video/queryTask` با
    `{"taskId":"..."}` (متد `g.M`)، هدر `userid` کوچک + `ifWise=true`.
  - تست زندهٔ موفق: آپلود `c=200` → ساخت با `effectType=4991` (Catwalk)
    `c=200` و `taskId=60004-1793049728-...`، وضعیت `doing` و سپس در سومین
    کوئری (~۱۸ ثانیه) `taskStatus=success` با
    `videoUrl=https://algo-v1.wiseoel.com/temp/.../img2video_wanlora-....mp4`.
  - مسیر قدیمی‌تر `image2video/unifiedTaskCreate` فیلد **`example`** اجباری
    دارد که فقط از کاتالوگ قالب‌های دانلودی سرور پر می‌شود و هیچ مقدار ثابتی
    در APK ندارد (همهٔ مقادیر آزمایشی با `c=1013 example is empty or illegal`
    رد شدند)؛ به همین دلیل خط لوله روی مسیر beat متمرکز شد.
  - **کاتالوگ افکت‌ها (بدون امضا، GET):**
    `GET /common/vibe/resourceNew?version=407&cp=<package>&platform=1&ifHttps=true&day=0&language=en&packageLevel=1`
    روی `cpi.ufotosoft.com`/`cpi.wiseoel.com` (appName ثابت `vibe`، از
    `ServerRequestManager.D()`). پاسخ ۲۴ گروه و ۳۱۰ قالب با فیلد
    `extraObject.effectsType` است؛ خلاصهٔ استخراج‌شده در
    `catalog_effects.json` و نسخهٔ فشرده داخل خود HTML جاسازی شده.
  - پاسخ: پاکت `{c,m,d}` و `d` با فیلدهای
    `taskId, taskStatus ("success"/"fail"/"doing"), taskReason, videoUrl`.
  - صفحه دایگنستیک پروب‌های A–G را دارد؛ پروب G کل زنجیره را با
    effectTypeهای واقعی کاتالوگ به‌صورت زنده اجرا و تا گرفتن videoUrl پول می‌کند.
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
  - `POST /algo/v1/faceFusion/aigc/beatImage2Video/createNormalTask`
  - `POST /algo/v1/faceFusion/aigc/beatImage2Video/queryTask`
  - `GET  /common/vibe/resourceNew` (کاتالوگ ۳۱۰ قالب؛ در HTML جاسازی شده)
- `userId` به‌صورت محلی ساخته و در `localStorage` ذخیره می‌شود؛ هیچ
  ثبت‌نام/لاگینی در پروتکل اپ وجود ندارد.

## تست‌ها

- MD5 جاوااسکریپت با Node `crypto` روی بردارهای معروف، متن فارسی (UTF-8) و
  فرمول‌های امضا تطبیق کامل دارد.
- سینتکس کل اسکریپت داخل فایل با Node بررسی شده است.
