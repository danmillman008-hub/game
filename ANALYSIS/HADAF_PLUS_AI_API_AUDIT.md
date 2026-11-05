# بررسی بخش «هوش مصنوعی» اپ هدف پلاس — کلید API و مقصد اتصال

**تاریخ:** ۲۰۲۶-۱۱-۰۵ · **شاخه:** `arena/aebb90b7-game`
**روش:** تحلیل استاتیک APK استخراجشده + جستجوی باینری کل ۱۵۱۶ entry خود APK +
اسناد ریپو. **هیچ ترافیک رانـتایمی از هدف پلاس ضبط نشده** و هیچ درخواست زندهای
به سرورهایش ارسال نشده است (دسترسی شبکهٔ این محیط محدود است).

---

## ۱) هویت نمونه

| مورد | مقدار |
|---|---|
| APK | `google_drive/Hadaf Plus_2.0.2.apk` (همچنین استخراجشده در `mimo-ui/UPGRADE/SOURCE_APPS/hadaf_plus/`) |
| SHA-256 | `b282f578b255fecc4b72ee74f2ce79eb5bbcde35f3515690342b7fa37a5bbf43` |
| بسته | `app.hadafplus.hadaf_plus` · Flutter (۳ معماری `libapp.so`) |
| مجوزها | شامل `INTERNET`, `ACCESS_NETWORK_STATE` |

---

## ۲) بخش هوش مصنوعی دقیقاً چیست (شواهد کد)

| ردپا | محل |
|---|---|
| `/ZistAI/conversations`، `/ZistAI/conversations/`، `/ZistAI/messages/` | `dart/ENDPOINTS.txt` و `libapp.so` |
| `/Chatbot/conversations`، `/Chatbot/conversations/`، `/Chatbot/messages/stream` | همان (stream = پاسخ جریانی SSE) |
| مسیرهای UI `/chatbot`، `/zistbot` | `dart/ROUTES.txt` |
| کلاسها/enumها: `ZistbotCategory`, `ZistbotFeedbackRating`, `ZistbotMediaType`, `ZistbotState`, `ChatbotState`, `zistbotBetaAccess` | `dart/STRINGS_ALL.txt` |
| داراییها: `assets/images/tools/zistbot.svg`, `assets/animations/chatbot.json`, `assets/images/icons/ai.svg` | `flutter_assets/` |
| رشتهٔ فارسی «در حال پردازش سوال» | `dart/PERSIAN_UTF16.txt` |
| `FEATURE_MAP.csv`: «AI Tutor (frozen look) … Hadaf /Chatbot» | `mimo-ui/UPGRADE/CATALOGS/FEATURE_MAP.csv` |

یعنی ربات «زیستبات / ZistAI» و «Chatbot» دو سرویس **First-party** روی بکاند خود اپاند،
نه یک SDK آمادهٔ مدل زبانی داخل کلاینت.

---

## ۳) کلید API چیست؟ → **هیچ کلید مدل زبانی وجود ندارد**

جستجوی باینری تمام entryهای APK:

| الگو | نتیجه |
|---|---|
| `openai`, `api.openai.com`, `anthropic`, `claude`, `chatgpt`, `gpt-4/3.5`, `gemini`, `generativelanguage` | **۰ مورد** |
| `sk-…` (کلید OpenAI)، `xoxb-…`، `x-api-key` | **۰ مورد** |
| `huggingface / cohere / groq / mistral / together.ai` | ۱ برخورد تصادفی در بایتهای یک PNG (false positive) |
| `AIza…` | **۳ مورد** — فقط در `lib/*/libapp.so` |
| `Bearer`, `Authorization` | موجود (۴ و ۲ entry) |

تنها رشتهٔ شبیه کلید، `AIzaSyBU…` (**redacted**) است: کلید استاندارد
**Firebase / Google Services** (FCM، Google Sign-In، Crash Reporting)؛ پروژهٔ
`hp-analytics-6a430.firebasestorage.app` و `FirebaseInitProvider` در مانیفست هم
همین را تأیید میکند. **این کلید ربطی به هوش مصنوعی/LLM ندارد** و نباید بهعنوان
«کلید API هوش مصنوعی» تعبیر شود.

احراز هویت درخواستها با **توکن کاربر (`Bearer`)** بعد از لاگین انجام میشود
(`/User/CheckPhoneNumber`, `/User/VerifyVerificationCode` و…)، نه با یک API key
سختکدشده. هیچ فایل `.env`، `google-services.json` حاوی کلید LLM، یا فایل
پیکربندی مدل در APK پیدا نشد.

> رشتهٔ `GPT - ` که در `STRINGS_ALL.txt` دیده میشود، عضوی از یک واژهنامه/لیست
> عمومی (GPT = جدول پارتیشن GUID) است، **نه** نام مدل GPT.

---

## ۴) وصل به کجاست؟ → **سرور خود هدف پلاس (ایرانی)**، نه مستقیم API خارجی

| دامنه | نقش | منبع |
|---|---|---|
| `https://gateway.hadafplus.app` | **API Gateway** (پایهٔ endpointها) | رشتهٔ باینری `lib/arm64-v8a/libapp.so` |
| `https://app.hadafplus.app` | وباپ / deep-link (مانیفست `<data android:host=…>`) | `manifest/AndroidManifest.xml` |
| `https://assets.hadafplus.app` | CDN تصاویر/صداها | `flutter_assets` |
| `https://hadafplus.ir` | سایت رسمی | `libapp.so` |
| `cafebazaar.ir/app/app.hadafplus.hadaf_plus`، `myket.ir/app/…`، `aparat.com/academyhadafplus`، `rubika.ir` | حضور ایرانی | `libapp.so` / رشتهها |

**هیچ دامنهای مثل `api.openai.com`، `generativelanguage.googleapis.com`،
`api.anthropic.com` و… در کل APK نیست.** پیشوند `/api/` یا نسخهٔ `/v1/` هم در
هدف پلاس دیده نشد (برخلاف میمو). بنابراین:

- از نگاه کلاینت، گفتگو به **زیرساخت خود شرکت هدف پلاس** میرود؛
- شرکت ایرانی است (دامنهٔ `.ir`، کافهبازار/مایکت، آپارات)؛
- **اما** اینکه سرور `gateway.hadafplus.app` در پشتصحنه خودش مدل دارد، یا به یک
  ارائهدهندهٔ خارجی/داخلی پراکسی میکند، از روی APK **قابل اثبات نیست**. برای
  اثباتش نیاز به ضبط ترافیک HTTPS رانـتایم، سیاست حریم خصوصی (`/about_us`) یا
  مستندات سرور است. هیچکدام در این ریپو موجود نیست. `SERVER CONFIRMED=0`.

> دربارهٔ واژهٔ «یارانی»: هیچ نام شرکتی با این املا در APK، رشتههای فارسی،
> کاتالوگها یا اسناد ریپو پیدا نشد. اگر منظور «شرکت **ایرانی**» بوده، پاسخ
> بالاست؛ اگر یک وندور خاص مدنظر است، نام دقیقش را بدهید تا همان را جستجو کنم.

---

## ۵) مقایسه با میمو (برای جلوگیری از قاطی شدن)

`ANALYSIS/MIMO_API_SURFACE.json` (از جدول رشتههای ۱۲DEX میمو ۹٫۳۵):

- endpoint هوش مصنوعی: `/v1/aiTutor/conversations`، `/v1/aiTutor/conversations/`،
  `/v1/aiTutor/conversations/messages/count` (فعل `GET` بهصورت استاتیک استنباط شده).
- base URLهای مشاهدهشده: `https://api.mimo.org`، `https://api-testing.mimo.org`،
  `https://api-production.8-lives-cat.io`، `https://engine.api.gist.build` و…؛
  سند صریحاً مینویسد: «runtime base-URL selection **NOT proven here**».
- وندورهای third-party دیدهشده همگی آنالیتیکس/پرداختاند (Mixpanel، Adjust،
  RevenueCat، Segment، Customer.io) — **هیچ ارائهدهندهٔ LLM و هیچ کلید LLMای** نیست.
- M08/M09 روی میمو: `retrofit2=0`، هیچ پاسخ سروری رؤیت نشد، `SERVER CONFIRMED=0`.

---

## ۶) اپی که خودمان ساختیم (`app/dist/Mimo.html`) — پاسخ قطعی

| پرسش | پاسخ |
|---|---|
| کلید API | **وجود ندارد.** جستجوی `AIza`/`sk-`/`apiKey=` در `app/src`, `app/assets`, `app/content` → خالی |
| ارائهدهنده | `local-content` داخل مرورگر؛ `generatesText:false`؛ `EXTERNAL_PROVIDER_CONTRACT.status = 'not-configured'` |
| شبکه | **۰ فراخوانی**: بدون `fetch` / `XMLHttpRequest` / `WebSocket` / `EventSource` (تأییدشده توسط `verify_output.py` ۴۵/۴۵) |
| Model / Cost | `local-content (بدون LLM)` و هزینهٔ `۰٫۰۰` — منابع محلی شمارش میشوند |

⚠️ **نکتهٔ مهم دربارهٔ ظاهر رابط:** در صفحهٔ AI پروتوتایپ تأییدشدهٔ `v12.5-fa`
یک چیپ «مدل سریع» با `data-code="gemini-flash-lite-latest · medium · TEACH / PRACTICE"`
و برچسب «۰٫۰۱ دلار» وجود دارد. اینها **فقط متن/ویژگی UI کپیشدهٔ بایتبهبایت از
طرح تأییدشده**اند — نه اتصال به Gemini، نه پرداخت واقعی، نه فراخوانی شبکهای.
در استودیوی جدید (`app/src/ai-studio.js`) مقدار Model صریحاً
`local-content (بدون LLM)` و Cost صفر نوشته شده است.

---

## ۷) آنچه نمیدانیم / گام بعد برای اثبات

1. آیا `gateway.hadafplus.app` پشتصحنه به OpenAI/Gemini/مدل داخلی پراکسی میکند؟ →
   نیاز به ضبط ترافیک رانـتایم (mitmproxy/Frida روی دستگاه)، یا متن سیاست حریم خصوصی اپ.
2. هدر دقیق، بدنهٔ درخواست/پاسخ و نام مدل → فقط از ترافیک یا مستندات سرور.
3. آیا `/ZistAI` همان `/Chatbot` است یا دو سرویس جدا (مثلاً زیستشناسی در برابر چت عمومی)؟
   استاتیک فقط وجود هر دو را ثابت میکند.
4. عبارت «یارانی» → هیچ ردپایی؛ نیاز به املای/نام دقیق وندور.

**خلاصهٔ یکخطی:** کلید API هوش مصنوعی در کار نیست؛ گفتگو از طریق توکن کاربر به
`gateway.hadafplus.app` (زیرساخت خود شرکت ایرانی هدف پلاس) میرود و هیچ دامنه/کلید
ارائهدهندهٔ خارجی در کلاینت دیده نمیشود — وصلشدن سرور به LLM خارجی نه رد و نه
تأیید شد. اپ آفلاین خودمان هم کاملاً بدون کلید و بدون شبکه است.
