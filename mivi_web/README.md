# 🎬 Mivi AI — اپ وب تولید ویدیو (تصویر + متن → ویدیو)

بازسازی مستقل و تک‌صفحه‌ای خط لوله ابری **Mivi AI** (`instagram.story.art.collage`
نسخه ۲.۳۷.۴۰۷) به‌صورت یک فایل HTML به‌علاوه یک سرور پروکسی کوچک پایتونی —
بدون نیاز به اپلیکیشن و بدون محدودیت‌های داخل اپ.

## فایل‌ها

| فایل | نقش |
|---|---|
| `mivi_app.html` | کل اپ در یک فایل: رابط فارسی، پیاده‌سازی MD5 خالص JS، آپلود عکس، ساخت تسک، polling و دانلود ویدیو |
| `serve.py` | سرور محلی فقط با کتابخانه استاندارد پایتون (بدون pip): سرو HTML + پروکسی درخواست‌ها برای رفع محدودیت CORS |
| `test_serve.py` | تست end-to-end با سرور mock (اجرا: `python3 test_serve.py`) |

## اجرا (روی کامپیوتر خودتان)

```bash
cd mivi_web
python3 serve.py
# مرورگر: http://localhost:8770
```

سپس: عکس انتخاب کنید → پرامپت بنویسید → «تولید ویدیو» بزنید. مراحل
(آپلود → ساخت تسک → پردازش → دانلود) در همان صفحه نمایش داده می‌شود و ویدیو
قابل پخش و دانلود است.

> باز کردن مستقیم `mivi_app.html` با مرورگر (file://) هم ممکن است کار کند،
> اما چون سرور ufotosoft هدر CORS ندارد، روش مطمئن همین `serve.py` است.

## پروتکل (استخراج‌شده از APK)

- هاست: `https://face-api.ufotosoft.com`
- signKey ثابت: **`m3snil`** (رمزگشایی DES/CBC از رشته هاردکد `hCzXemhkIkY=`)
- امضای APIهای الگوریتمی: `MD5(userId + زمان‌یونیکس)`
- امضای آپلود: `MD5("m3snil" + زمان‌یونیکس)`
- هدرها: `userid/userId, timeStamp, cp=instagram.story.art.collage, version=407, platform=1, sign, ifWise/ifHttps`
- اندپوینت‌ها:
  - `POST /algo/v1/aiGenerate-aigc/multipleUpload` (multipart، فیلد `files`)
  - `POST /algo/v1/faceFusion/aigc/image2video/unifiedTaskCreate`
  - `POST /algo/v1/faceFusion/aigc/image2video/queryTask`
- `userId` به‌صورت محلی ساخته و در `localStorage` ذخیره می‌شود (معادل
  ANDROID_ID در اپ)؛ ثبت‌نام/لاگینی وجود ندارد.

## امنیت پروکسی

`serve.py` فقط مقصدهای `ufotosoft.com` و `videomate.cc` را فوروارد می‌کند
(پروکسی عمومی باز نیست) و هدر `Access-Control-Allow-Origin: *` می‌دهد.
