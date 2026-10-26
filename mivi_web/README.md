# 🎬 Mivi AI — اپ وب تک‌فایل (تصویر + متن → ویدیو)

بازسازی مستقل خط لوله ابری **Mivi AI** (`instagram.story.art.collage`
نسخه ۲.۳۷.۴۰۷) در **یک فایل HTML واحد** — بدون نیاز به نصب، سرور جانبی یا pip.

## فایل

| فایل | نقش |
|---|---|
| `mivi_all_in_one.html` | کل اپ در یک فایل: رابط فارسی RTL، MD5 خالص JS، امضای درخواست‌ها، آپلود عکس، ساخت تسک، polling و دانلود ویدیو |

## نحوه استفاده

۱. فایل `mivi_all_in_one.html` را با مرورگر باز کنید (دابل‌کلیک، همان file://).
۲. عکس انتخاب کنید، پرامپت بنویسید و «تولید ویدیو» بزنید.
۳. ویدیوی ~۶ ثانیه‌ای در همان صفحه پخش و قابل دانلود است.

### اگر خطای CORS / Failed to fetch گرفتید

مرورگرها در حالت file:// ممکن است تماس مستقیم با `face-api.ufotosoft.com` را
بلاک کنند. در همان فایل، بخش **«⚙️ تنظیمات اتصال و احراز هویت»** را باز کنید:

- حالت «پروکسی عمومی corsproxy.io / allorigins» را انتخاب کنید، یا
- آدرس پروکسی CORS شخصی خودتان را وارد کنید (با جایگره `{url}` یا چسباندن
  URL هدف به انتها).

پخش ویدیو با تگ `<video>` حتی بدون CORS هم کار می‌کند؛ فقط فراخوانی API و
دانلود خودکار به مجوز سرور نیاز دارد.

## پروتکل (استخراج‌شده از APK)

- هاست: `https://face-api.ufotosoft.com`
- signKey ثابت: **`m3snil`** (رمزگشایی DES/CBC از رشته هاردکد `hCzXemhkIkY=`)
- امضای API الگوریتمی: `MD5(userId + زمان‌یونیکس)`
- امضای آپلود: `MD5("m3snil" + زمان‌یونیکس)`
- هدرها: `userid/userId, timeStamp, cp=instagram.story.art.collage,
  version=407, platform=1, sign, ifWise/ifHttps`
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
