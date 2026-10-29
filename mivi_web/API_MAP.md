# نقشهٔ کامل API و موتورهای Mivi AI 2.37.407

استخراج‌شده در ۲۰۲۶-۱۰-۲۹ از بایت‌کد خودِ APK (۸ دکس، ۴٫۵۳۳ ورودی، ۱۵۴ کتابخانهٔ `.so`).
هدف: بستن همهٔ «نقاط تاریک» باقی‌مانده — یعنی معلوم شود اپ چند موتور دارد، هر کدام چه
بدنه‌ای می‌فرستد، و کدام‌شان روی سرور زنده است.

## ۰) بازسازی APK در سندباکس

سه بخش آپلودشده در گوگل‌درایو (`.z01` + `.z02` + `.zip`) در همین ترتیب به هم چسبانده
می‌شوند و یک زیپ معتبر می‌سازند:

```bash
cat "Mivi AI_2.37.407.z01" "Mivi AI_2.37.407.z02" "Mivi AI_2.37.407.zip" > mivi_full.zip
unzip -o mivi_full.zip -d /tmp/apk        # → Mivi AI_2.37.407.apk  (۱۹۶٫۶ MB)
```

ابزار تحلیل: `python -m venv /tmp/venv && /tmp/venv/bin/pip install androguard`
(بدون venv نصب رد می‌شود: PEP 668). ابزارهای محلی در `mivi_web/re/`.

## ۱) ۱۳ موتور ویدیو در یک enum

```java
public enum P2Type {
  GX_AiVideoP2V, AiVideoLtx, AiVideoPixVerse, AiVideoUnify,
  AiVideoGoogleVeo, AiVideoHD, AiVideoHDVidu, AiVideoT2V,
  AiText2VideoUnify, AiSequenceVideo, AiHug, AiHugP2V, AiDance
}
```

یعنی Mivi فقط «Wan-LoRA» نیست: **LTX، PixVerse، Unified، Google Veo و Vidu-HD** هم
مسیر جداگانه دارند. مسیری که تا امروز استفاده می‌کردیم `GX_AiVideoP2V` است
(endpoint `beatImage2Video/createNormalTask`، فایل خروجی `img2video_wanlora-*.mp4`).

## ۲) نقشهٔ لایهٔ سرویس ← قابلیت ← متد Retrofit

`Image2VideoServer` یک متد Kotlin برای هر قابلیت دارد که یک کلاس کوروتین
`...$createXxxTask$1` می‌سازد و در نهایت متد Retrofit در `com.ufotosoft.ai.base.g`
را صدا می‌زند. این نگاشت با اسکن `const-class` به‌دست آمده (قطعی، نه حدس):

| متد سرور | قابلیت | متد Retrofit | اندپوینت |
|---|---|---|---|
| `y` | `createGXAiVideoTask` — **مسیر فعلی ما** | `g.P` | `POST /algo/v1/faceFusion/aigc/beatImage2Video/createNormalTask` |
| `v` | `createAiVideoLtxTask` | `g.C` | `POST /algo/v1/faceFusion/aigc/image2video/createTask` |
| `w` | `createAiVideoUnifiedTask` | `g.l` | `POST /algo/v1/faceFusion/aigc/image2video/unifiedTaskCreate` |
| `z` | `createGoogleVeoVideoTask` | `g.g0` | `POST /algo/v1/faceFusion/aigc/image2video/image2VideoCreateV5` |
| `F` | `createVideoHdTaskVidu` | `g.R` | `POST /algo/v1/faceFusion/aigc/createVideoHdTaskVidu` |
| `t` | `createAiSequenceVideoTask` (نسخهٔ جدید) | — | `…/integrated/image2VideoCreateV4` |
| `u` | `createText2VideoTaskVidu` | `g.e0` | مسیر T2V |
| — | کوئری | `g.b` | `POST /algo/v1/faceFusion/aigc/image2VideoQuery` |
| — | کوئری beat | `g.M` | `POST /algo/v1/faceFusion/aigc/beatImage2Video/queryTask` |

> ⚠️ نگاشت «مسیر ← متد» برای ردیف‌های `g.C/g.l/g.g0/g.R` از **ترتیب و نام قابلیت**
> به‌دست آمده، نه از Annotation؛ پارسر annotation ما روی این دکس کامل نشد
> (بخش ۷). بدنه‌ها اما صد‌درصد از بایت‌کد است.

`startGoogleVeoVideo` و `startVideoHDVidu` در `Image2VideoTask` (متدهای `c3` و `l3`)
همان دو مسیر را از لایهٔ UI صدا می‌زنند.

## ۳) بدنهٔ دقیق هر مسیر (از `invokeSuspend`)

ترتیب کلیدها همان ترتیبی است که در بایت‌کد `JSONObject.put` می‌شود.

### GX / beat — مسیر فعلی
```
imageUrls[], level, effectType, imageEffectType(اگر ≠۰), prompt(اگر خالی نباشد), quality(اگر ≠۰)
```
`quality`: ۱ = 360P، ۲ = 720P. `effectType` = ۶۲۰۹ برای «AI Video» و شناسهٔ قالب برای بقیه.

### LTX
```
imageUrls[], level, effectType
```
بدون prompt و بدون quality.

### Unified
```
imageUrls[], level, deviceToken, prompt, ratio, movementAmplitude, example, ifTest
```
`example` همان فیلدی است که همهٔ تست‌های ما را با
`c=1013 example is empty or illegal` رد کرد؛ از کاتالوگ پر می‌شود، نه از APK.

### Google Veo (V5)
```
imageUrls[], level, deviceToken, googleId, audio(bool), prompt, duration(int), ifTest(bool)
```
+ هر کلید اضافهٔ `HashMap` ورودی. `audio` یعنی **Veo 3 با صدا**؛ `duration` تنها
جایی است که مدت واقعاً به سرور می‌رود (در مسیر beat نادیده گرفته می‌شد).

### Vidu HD
```
taskId, level, deviceToken, ifTest
```
ورودی‌اش **taskId یک تسک تمام‌شده** است، نه عکس ⇒ این یک **ارتقادهندهٔ پس از تولید**
است. تنها مسیری که می‌تواند «ایهنسر» باشد که کاربر حسش کرده بود.

### Sequence (دو نسخه)
```
imageUrls[], level, deviceToken, effectType, poseSequenceId, pixVerseId, ifTest
```

### Text2Video Vidu
```
level, deviceToken, duration, prompt, enhance, style, ratio, ifTest
```
`enhance` فقط اینجا هست — یک پرچم تقویت، مستقل از `quality`.

## ۴) فهرست کامل اندپوینت‌های زندهٔ AIGC (۶۱ مورد در کلاس `g`)

```
/algo/v1/aiGenerate-aigc/multipleUpload
/algo/v1/faceFusion/aigc/beatImage2Video/{createNormalTask,queryTask,cancelTask}
/algo/v1/faceFusion/aigc/image2video/{createTask,queryTask,unifiedTaskCreate,integratedTaskCreate,image2VideoCreateV5}
/algo/v1/faceFusion/aigc/integrated/image2VideoCreateV4
/algo/v1/faceFusion/aigc/image2Video{Create,CreateV2,CreateV3,Query,Detect,Cancel}
/algo/v1/faceFusion/aigc/createVideoHdTaskVidu
/algo/v1/faceFusion/aigc/getAllPoseSequenceId
/algo/v1/faceFusion/aigc/image2VideoCustomer/{createTemplate,queryTemplate,cancelTemplate,upload}
/algo/v1/faceFusion/aigc/{createAiPhotoTask,createAiPhotoTaskV2,queryAiPhotoTask,queryAiPhotoModels,createAiPhotoModel,createAiPhotoModelV2}
/algo/v1/faceFusion/aigc/{createPictureDetectTask,queryPictureDetectTask}
/algo/v1/faceFusion/aigc/{emoVideoCreate,emoVideoQuery,emoVideoCancel,emoImageDetect,createSwapFace}
/algo/v1/faceFusion/aigc/{livePortraitCreate,livePortraitQuery}
/algo/v1/faceFusion/aigc/{createInpaintAnything,createInpaintCleaner}
/algo/v1/faceFusion/aigc/image2image/{createImageTask,createAiStyleTask}
/algo/v1/faceFusion/aigc/{createFaceKeyTask,createFaceKeyTaskV2,queryFaceKeyTask,queryFaceKeyTaskV2}
/algo/v1/faceFusion/aigc/{createAiCustomizeTask,queryAiCustomizeTask,cancelAiCustomizeTask}
/algo/v1/faceFusion/aigc/babyPredict{Create,CreateV2,Query,QueryV2}
/algo/v1/faceFusion/aigc/{stitchImage/createTask,stitchImage/queryTask}
/algo/v1/faceFusion/aigc/{createSuperResolutionNew,querySuperResolutionNew}
/algo/v1/faceFusion/aigc/getFaceInfo
/algo/v1/faceAnimation/{createFaceAnimationTask,queryFaceAnimationTask,cancelFaceAnimationTask,redoFaceAnimationTask,multipleUpload}
/algo/v1/faceFusion/{createAiStyleTask,queryAiStyleTask,cancelAiStyleTask}
/style/v1/{videoFaceFusion,queryVideoFaceFusion,redoVideoFaceFusion,cancelFaceFusion,videoFaceDriven,queryVideoFaceDriven,cancelFaceDriven,face/faceSwap}
/file/style/{upload,multipleUpload}
/common/vibe/resourceNew            (کاتالوگ ۳۱۰ قالب + toolGroups)
/storyart/ncrnau/beat/getResourceList
/common/category/{appName}/resource
/common/country/getCountryCode
/v1/config · /api/env · /api/v1_2/{adconf,crosspro,ev,open} · /api/v2/ev
/billing/property/{issuePrivilegeV2,getUpgradeInfo,restore,userReport,purchaseFailReport}
```

## ۵) سه ابزار صفحهٔ اول در کاتالوگ

`toolGroups` فقط سه ورودی دارد و **دقیقاً همان سه کاشی اسکرین‌شات کاربر** است:

| groupId | groupName | یعنی |
|---|---|---|
| 5074 | `Custom_Ai_Video` | کاشی **AI Video** ⇒ مسیر beat با effectType ۶۲۰۹ |
| 5075 | `AI_Expand` | کاشی **Expand** |
| 5076 | `AI_Enhance` | کاشی **Enhance** |

نتیجهٔ مهم: **«Enhance» یک ابزار مستقل در صفحهٔ اول است، نه بخشی از حالت Pro.**
متن «Pro: 720p & Enhanced Visuals» در اسکرین‌شات فقط برچسب بازاریابی است؛ پرچم
قابل‌اندازه‌گیری‌اش همان `quality` است و ابزار واقعی تقویت
`createSuperResolutionNew` / `createVideoHdTaskVidu` است.

## ۶) جمع‌بندی: چه چیزهایی بسته شد

- ✅ تعداد و نام همهٔ موتورها (۱۳ مورد) و پنج مسیر ورودی-عکس
- ✅ بدنهٔ دقیق هر مسیر، شامل `audio`/`duration` برای Veo و `taskId` برای Vidu-HD
- ✅ منبع «Enhance»: ابزار مستقل + اندپوینت‌های super-resolution/HD
- ✅ فهرست کامل ۶۱ اندپوینت AIGC (چیزی پشت «۴۰۴» پنهان نیست — مسیر در APK هست)
- ✅ تأیید دوبارهٔ فرمول امضا: `wa.a.g(signKey + ts)` = `MD5("m3snil"+ts)`
- ❌ هنوز باز: مقدار مجاز `example` (از کاتالوگ سرور می‌آید، در APK ثابتی ندارد)
- ❌ هنوز باز: نگاشت قطعی مسیر↔متد برای ۴ اندپوینت (بخش ۲، هشدار)

## ۷) چرا پارسر annotation کامل نشد

نوشتن `mivi_web/re/dexann.py` تا سطح `annotations_directory_item` و
`annotation_set_item` کار می‌کند، ولی آفست‌های `annotation_set` برای متدهای کلاس
`Lcom/ufotosoft/ai/base/g;` به annotationهای کلاس‌های دیگر (IronSource/AdMob)
اشاره می‌کنند ⇒ خواندن آفست‌ها یک لایه جابه‌جا است. چون همهٔ اطلاعات عملی
(بدنه‌ها، هدرها، مسیرها) از راه دیگری به‌دست آمد، این کار متوقف شد.

---

# پیوست: بدنهٔ واقعی هر مسیر، خوانده‌شده از دستورالعمل‌های dex

منبع: `Lcom/ufotosoft/ai/image2video/Image2VideoServer$create*Task$1` — هر کلاس
درونی یک مسیر است و `invokeSuspend` آن با `org.json.JSONObject.put` بدنه را
می‌سازد. نام کلاس‌ها **خودشان** مسیر را نام‌گذاری می‌کنند:

`createAiPhotoTask` (V1) · `createAiPhotoTaskV2` · `createAiPhotoTaskV3` ·
`createAiVideoLtxTask` · `createAiVideoUnifiedTask` · `createGXAiVideoTask` ·
`createGoogleVeoVideoTask` · `createAiSequenceVideoTask` ·
`createText2VideoTaskVidu` · `createText2VideoUnifiedTask` ·
`createVideoHdTask` · `createVideoHdTaskVidu` · `getAllPoseSequenceId`

## بدنه‌ها (به ترتیب قرار گرفتن در کد)

| مسیر | فیلدهایی که واقعاً گذاشته می‌شود |
|---|---|
| `createAiVideoLtxTask` | `imageUrls[]`, `level`, `effectType` — **نه prompt، نه duration، نه ratio** |
| `createGoogleVeoVideoTask` | `imageUrls[]`, `level`, `deviceToken`, `googleId`, `audio`, `prompt`, `duration`, `ifTest` |
| `createAiVideoUnifiedTask` | `imageUrls[]`, `level`, `deviceToken`, `prompt`, `ratio`, `movementAmplitude`, `example`, `ifTest` |
| `createAiSequenceVideoTask` | `imageUrls[]`, `level`, `deviceToken`, سپس **یا** `effectType`+`poseSequenceId`+`pixVerseId` **یا** `example`+`extParams`، سپس `ifTest` |
| `createAiPhotoTaskV3` | `imageUrls[]`, `level`, `deviceToken`, …, `pixVerseId` |

## سه نتیجهٔ قطعی

**۱) Veo هیچ‌وقت `effectType` نمی‌فرستد.** بدنهٔ بالا کامل است. سرور روی
`image2VideoCreateV5` می‌گوید `param error: effectType illegal` ⇒ **V5 اندپوینت
Veo نیست**؛ با بدنهٔ دقیق اپ هم همان خطا را می‌دهد. پس آن مسیر به موتور دیگری
تعلق دارد و `googleId` هم کلید Veo نیست.

**۲) `createAiVideoLtxTask` ⇒ PixVerse است، نه LTX.** بدنه فقط
`imageUrls`+`level`+`effectType` است، و `image2VideoCreateV3` پاسخ داد
`pixVerseId不能为空` ⇒ همان مسیر V3 و همان `pixVerseId` کلاس V3. مسیر LTX واقعی
هنوز پیدا نشده.

**۳) Sequence دو نسخه دارد و کلیدش `extParams["example"]` است.**
`Image2VideoTask.g()` این را می‌خواند:

```java
String ex = extParams.get("example");
boolean isNewVersion = (ex != null && ex.length() > 0);
Log.d("Image2VideoServer", "createAiSequenceVideoTask isNewVersion: " + isNewVersion);
if (!isNewVersion) { body.put("effectType", …); body.put("poseSequenceId", …); body.put("pixVerseId", …); }
for (Map.Entry e : extParams.entrySet()) body.put(e.getKey(), e.getValue());
```

یعنی وقتی `example` پر باشد، `effectType` و بقیه **کامل حذف** می‌شوند و فقط
`example` + هر چه در `extParams` باشد فرستاده می‌شود. پس رد شدن
`effectType=4991/5041/4877/5202` طبیعی است: آن اعداد افکت ویدیوی پیش‌ساخته‌اند
و مسیر Sequence آن‌ها را نمی‌پذیرد. **آزمون درست، فرستادن `example` بدون
`effectType` است** — چیپ‌های Animate/Walk/Wave در اسکرین‌شات هم دقیقاً
`samples` همین `example` هستند.

## ابزار تازه: `re/annpaths.py`

پارسر خام annotation روی خودِ فایل dex (بدون androguard). `encoded_value`
های ثابت‌عرض را با `value_arg+1` بایت می‌خواند، نه uleb — این یک اشتباه رایج
است که کل پارس را یک بایت جابه‌جا می‌کند. روی هشت dex اجرا شد:
**۷۴٬۵۸۲ متد annotate‌شده با ۱۲۹ نوع annotation** خوانده شد.

ولی **هیچ annotation از `retrofit2` پیدا نشد** ⇒ لایهٔ HTTP این اپ Retrofit
نیست (برخلاف حدس قبلی) و مسیرها از جای دیگری می‌آیند. بنابراین نگاشت
مسیر↔متد با annotation **قابل حل نیست** و باید تجربی (همان جدول واریانت‌ها)
بسته شود.

## تنها راه قانونی برای `poseSequenceId` / `pixVerseId`

اندپوینت `getAllPoseSequenceId` در APK هست
(`Image2VideoServer$getAllPoseSequenceId$1`، متد کلاینت `g.V(...)`). این
همان API‌ای است که اپ برای پر کردن `poseSequenceId` و `pixVerseId` صدا می‌زند؛
یعنی **این دو مقدار دادهٔ سرورند و در APK ثابت نیستند**. تا مسیر این اندپوینت
پیدا نشود، مسیرهای V3/Sequence-قدیم عملاً بسته‌اند.

---

# پیوست ۲: آپدیت ۲.۳۷.۴۰۸ — چه چیزی عوض شد و چه چیزی نه

منبع: `new apk` در درایو (سه بخش: `.z01` ۵۰MB + `.z02` ۵۰MB + `.zip` ۱۹.۲MB).
یک نکتهٔ فنی: این یک zip چندبخشی (spanned) است؛ چسباندن سرهم کافی نیست، چون
EOCD عدد دیسک را ۲ می‌گذارد و `zipfile` ارور `Bad magic number` می‌دهد. با
صفر کردن `disk`/`cddisk` و افزودن آفست بخش آخر به `cdoff` درست می‌شود.
APK نهایی: ۱۹۸٬۹۷۷٬۴۶۷ بایت، ۴٬۵۷۷ فایل، ۸ dex.

## ۱) چه چیزی عوض نشده (مهم‌ترین نتیجه)

| بررسی | نتیجه |
|---|---|
| فهرست مسیرهای `/algo/v1/...` | **۶۴ مسیر در هر دو نسخه، صفر تفاوت** |
| کلاس `Image2VideoServer` (۱۴۸ متد) | **رشته‌های بدنه بی‌ته‌تفاوت‌اند** |
| کل بستهٔ `com/ufotosoft/ai/image2video/` (۷۹۳ خط رشته) | فقط حروف ابفاسکیت عوض شده (`xa`→`ya`, `hi`→`ii`) |
| تعداد کلاس‌ها | ۷۰٬۶۱۹ → ۷۴٬۰۵۱ (+۴٬۸۲۷ / −۱٬۳۹۵) |

پس **آپدیت هیچ پاسخی برای مسیرهای ویدیو نداشت**. تغییرات واقعی:
فیچر تازهٔ «Ref to Image» (`RefToImageEditActivity`, `RefToImageStylesManager`,
`RefToImageStyleItem`, `TemplateScene`)، بازنویسی کامل کراپ
(`edit/crop/CropImageView`, `HeadTailCropActivity`, `HugProcessInfo`) و
۴٬۸۲۷ کلاس تبلیغاتی Facebook.

تنها رشته‌های تازهٔ مرتبط: `aigc_params`، `getPoseSequenceId` (یک getter)،
` , poseSequenceId=` (لاگ).

## ۲) ولی در بازخوانی، سه چیز پیدا شد که در نسخهٔ قبل هم بود

### الف) `getAllPoseSequenceId` مسیرش را دارد

```
POST /algo/v1/faceFusion/aigc/getAllPoseSequenceId
body = {}            ← در کد: new JSONObject() خالی، بدون هیچ فیلدی
```

این **همان API‌ای** است که `poseSequenceId` و `pixVerseId` قانونی را می‌دهد.
تا امروز فکر می‌کردیم مسیرش را نداریم؛ در فهرست ۶۴ مسیر بود و از چشم افتاده بود.

### ب) بدنهٔ کامل هر مسیر (نسخهٔ ۴۰۸، با فیلدهای تازه)

| متد | بدنه |
|---|---|
| `createAiPhotoTask` (V1) | `poseSequenceId, imageKey, level, deviceToken, videoRatio, specialPic, audioKey, ifTest` |
| `createAiPhotoTaskV2` | `imageUrls, level, deviceToken, effectType, poseSequenceId, duration, prompt, **enhance**, ifTest` |
| `createAiPhotoTaskV3` | `imageUrls, level, deviceToken, pixVerseId, duration, prompt, **enhance**, ifTest` |
| `createGXAiVideoTask` | `imageUrls, level, effectType, **imageEffectType**, prompt, quality` |
| `createAiVideoLtxTask` | `imageUrls, level, effectType` |
| `createAiVideoUnifiedTask` | `imageUrls, level, deviceToken, prompt, ratio, movementAmplitude, example, ifTest` |
| `createGoogleVeoVideoTask` | `imageUrls, level, deviceToken, googleId, audio, prompt, duration, ifTest` |
| `createAiSequenceVideoTask` | `imageUrls, level, deviceToken` + (**`example`** یا `effectType`+`poseSequenceId`+`pixVerseId`) + `ifTest` |
| `createText2VideoTaskVidu` | `level, deviceToken, duration, prompt, **enhance**, style, ratio, ifTest` |
| `createText2VideoUnifiedTask` | `level, deviceToken, duration, prompt, ratio, ifTest` |
| `createVideoHdTaskVidu` | `taskId, level, deviceToken, ifTest` |
| `createVideoHdTask` | `videoUrl, fileMd5, fileSize, fileTime, width, height, level, deviceToken, ifTest` |

دو فیلد تازه نسبت به نقشهٔ قبلی:

- **`enhance`** — یک بولین در V2/V3/Text2Video-Vidu. این همان چیزی است که در
  اسکرین‌شات «Pro: 720p & **Enhanced Visuals**» نامیده شده. مسیر GX آن را ندارد.
- **`imageEffectType`** — فقط در مسیر GX/beat. در کاتالوگ ۳۱۰ افکت، **یک**
  منبع این فیلد را دارد: `resId` با `imageEffectType = 7186`. یعنی مسیر beat
  علاوه بر افکت ویدیو، می‌تواند یک افکت «تصویری» هم بگیرد.

### ج) `createVideoHdTask` روی ویدیوی خودمان کار می‌کند

بدنه‌اش `videoUrl` + متادیتای فایل است، نه `taskId`. یعنی برخلاف
`createVideoHdTaskVidu` (که تسک GX را رد کرد) این یکی قرار است یک ویدیوی موجود
را ارتقا بدهد. مسیرش در فهرست رشته‌ها نیست؛ به همین دلیل صفحهٔ آزمون آن را
با نام متد صدا می‌زند تا یا کار کند یا خطای واقعی بدهد.

---

# پیوست ۳: نتیجهٔ آزمون زندهٔ بیلد `2026-10-30a` (۱۵:۰۱)

چهار واقعیت تازه که هر کدام یک قدم جلو برد:

## ۱) `imageEffectType` موتور را عوض می‌کند

| درخواست | taskId برگشتی |
|---|---|
| GX (بدون `imageEffectType`) | `60014-1793282490-…` |
| GXi (`imageEffectType=7186`) | `INTEGRATED_60019-1793282490-…` |

پیشوند تسک از **۶۰۰۱۴** به **INTEGRATED_60019** تغییر کرد ⇒ این فیلد یک
پارامتر استایل نیست، **مسیریاب موتور** است. یعنی با همان بدنهٔ beat می‌شود
موتور ۶۰۰۱۹ را صدا زد. ولی کوئری‌اش معلوم نیست: روی
`beatImage2Video/queryTask` و `imageVideo/queryTask` و `image2VideoQuery`
همه‌جا `c=3035` برگشت (نه وضعیت، نه خطای پارامتر) ⇒ تسک ساخته شد ولی
جدول کوئری دیگری دارد. مسیر مشکوک بعدی: `queryAiPhotoTask`، یا شناسهٔ
بدون پیشوند `INTEGRATED_`.

## ۲) چهار اثر کاتالوگ، برای V5 قانونی‌اند

| بدنه | پاسخ |
|---|---|
| `effectType=6209` + Veo کامل | `c=1013 effectType illegal` |
| `effectType=4899/4991/6093/7849` | `c=400 **googleId 不能为空**` |

یعنی اعتبارسنجی از `effectType` **رد شد و به فیلد بعدی رسید** ⇒ این چهار عدد
پذیرفته می‌شوند. V5 = `effectType` قانونی + `googleId`. تنها مجهول باقی‌مانده
مقدار `googleId` است. (با `googleId="1"` و `effectType=6209` فقط خطای
effectType را می‌داد، پس مقدار googleId هنوز آزمون نشده.)

## ۳) `getAllPoseSequenceId` روی این هاست باز نیست

`POST /algo/v1/faceFusion/aigc/getAllPoseSequenceId` با بدنهٔ خالی →
`HTTP 404`. مسیر در dex هست ولی روی `cpi.ufotosoft.com` منتشر نشده؛
هاست دوم (`cpi.wiseoel.com`) هم باید آزمون شود.

## ۴) `createVideoHdTask` زنده است و متادیتا می‌خواهد

```
{"videoUrl":…,"fileSize":3212288,"width":960,"height":1280,"fileTime":0}
→ c=1013 "param error: video metadata incomplete"
```

یعنی اندپوینت وجود دارد و قراردادش همان `videoUrl + fileMd5 + fileSize +
fileTime + width + height` است. `fileTime=0` به‌عنوان «خالی» شمرده می‌شود و
`fileMd5` هم نبود. بیلد بعدی هر دو را می‌فرستد (md5 خام بایت‌های فایل).

همچنین `createSuperResolutionNew` زنده است ولی `imageUrls` می‌خواهد ⇒
**ارتقای عکس** است، نه ویدیو.

---

# پیوست ۴: نقشهٔ کامل «متد ← مسیر» — چیزی که تا حالا باز بود

این بار جواب در کد بود، نه در تست. آن ۶۴ مسیر در dex **هیچ ارجاع
`const-string`ی ندارند** (با شاهد: `imageUrls` ۳۷ ارجاع دارد،
`createNormalTask` صفر). علتش پیدا شد: مسیرها **مقدارِ annotation** هستند،
نه رشتهٔ داخل کد — و androguard آن‌ها را برای متدها برنمی‌گرداند. با خواندن
خام بخش `ANNOTATION_ITEM` درآمدند.

نقشهٔ کلاینت `Lcom/ufotosoft/ai/base/g;` (همان که `Image2VideoServer` صدا
می‌زند) کامل است:

| متد کلاینت | نوع annotation | مسیر |
|---|---|---|
| `a` | `Lak/o;` | `/algo/v1/aiGenerate-aigc/multipleUpload` |
| `m` | `Lak/o;` | `/algo/v1/faceFusion/aigc/babyPredictCreate` |
| `w` | `Lak/o;` | `/algo/v1/faceFusion/aigc/babyPredictCreateV2` |
| `f` | `Lak/o;` | `/algo/v1/faceFusion/aigc/babyPredictQuery` |
| `h0` | `Lak/o;` | `/algo/v1/faceFusion/aigc/babyPredictQueryV2` |
| `r` | `Lak/o;` | `/algo/v1/faceFusion/aigc/beatImage2Video/cancelTask` |
| `P` | `Lak/o;` | `/algo/v1/faceFusion/aigc/beatImage2Video/createNormalTask` |
| `M` | `Lak/o;` | `/algo/v1/faceFusion/aigc/beatImage2Video/queryTask` |
| `o` | `Lak/o;` | `/algo/v1/faceFusion/aigc/cancelAiCustomizeTask` |
| `W` | `Lak/o;` | `/algo/v1/faceFusion/aigc/createAiCustomizeTask` |
| `i0` | `Lak/o;` | `/algo/v1/faceFusion/aigc/createAiPhotoModel` |
| `z` | `Lak/o;` | `/algo/v1/faceFusion/aigc/createAiPhotoModelV2` |
| `g` | `Lak/o;` | `/algo/v1/faceFusion/aigc/createAiPhotoTask` |
| `y` | `Lak/o;` | `/algo/v1/faceFusion/aigc/createAiPhotoTaskV2` |
| `F` | `Lak/o;` | `/algo/v1/faceFusion/aigc/createFaceKeyTask` |
| `j0` | `Lak/o;` | `/algo/v1/faceFusion/aigc/createFaceKeyTaskV2` |
| `B` | `Lak/o;` | `/algo/v1/faceFusion/aigc/createInpaintAnything` |
| `d` | `Lak/o;` | `/algo/v1/faceFusion/aigc/createInpaintCleaner` |
| `i` | `Lak/o;` | `/algo/v1/faceFusion/aigc/createPictureDetectTask` |
| `x` | `Lak/o;` | `/algo/v1/faceFusion/aigc/createSwapFace` |
| `R` | `Lak/o;` | `/algo/v1/faceFusion/aigc/createVideoHdTaskVidu` |
| `Q` | `Lak/o;` | `/algo/v1/faceFusion/aigc/emoImageDetect` |
| `q` | `Lak/o;` | `/algo/v1/faceFusion/aigc/emoVideoCancel` |
| `f0` | `Lak/o;` | `/algo/v1/faceFusion/aigc/emoVideoCreate` |
| `d0` | `Lak/o;` | `/algo/v1/faceFusion/aigc/emoVideoQuery` |
| `V` | `Lak/f;` | `/algo/v1/faceFusion/aigc/getAllPoseSequenceId` |
| `t` | `Lak/o;` | `/algo/v1/faceFusion/aigc/getFaceInfo` |
| `u` | `Lak/o;` | `/algo/v1/faceFusion/aigc/image2VideoCancel` |
| `J` | `Lak/o;` | `/algo/v1/faceFusion/aigc/image2VideoCreate` |
| `a0` | `Lak/o;` | `/algo/v1/faceFusion/aigc/image2VideoCreateV2` |
| `U` | `Lak/o;` | `/algo/v1/faceFusion/aigc/image2VideoCreateV3` |
| `E` | `Lak/o;` | `/algo/v1/faceFusion/aigc/image2VideoCustomer/cancelTemplate` |
| `l0` | `Lak/o;` | `/algo/v1/faceFusion/aigc/image2VideoCustomer/createTemplate` |
| `s` | `Lak/o;` | `/algo/v1/faceFusion/aigc/image2VideoCustomer/queryTemplate` |
| `j` | `Lak/o;` | `/algo/v1/faceFusion/aigc/image2VideoDetect` |
| `b` | `Lak/o;` | `/algo/v1/faceFusion/aigc/image2VideoQuery` |
| `D` | `Lak/o;` | `/algo/v1/faceFusion/aigc/image2image/createAiStyleTask` |
| `I` | `Lak/o;` | `/algo/v1/faceFusion/aigc/image2image/createImageTask` |
| `C` | `Lak/o;` | `/algo/v1/faceFusion/aigc/image2video/createTask` |
| `g0` | `Lak/o;` | `/algo/v1/faceFusion/aigc/image2video/image2VideoCreateV5` |
| `c0` | `Lak/o;` | `/algo/v1/faceFusion/aigc/image2video/integratedTaskCreate` |
| `k` | `Lak/o;` | `/algo/v1/faceFusion/aigc/image2video/queryTask` |
| `l` | `Lak/o;` | `/algo/v1/faceFusion/aigc/image2video/unifiedTaskCreate` |
| `X` | `Lak/o;` | `/algo/v1/faceFusion/aigc/integrated/image2VideoCreateV4` |
| `b0` | `Lak/o;` | `/algo/v1/faceFusion/aigc/livePortraitCreate` |
| `h` | `Lak/o;` | `/algo/v1/faceFusion/aigc/livePortraitQuery` |
| `O` | `Lak/o;` | `/algo/v1/faceFusion/aigc/queryAiCustomizeTask` |
| `A` | `Lak/o;` | `/algo/v1/faceFusion/aigc/queryAiPhotoModels` |
| `p` | `Lak/o;` | `/algo/v1/faceFusion/aigc/queryAiPhotoTask` |
| `Y` | `Lak/o;` | `/algo/v1/faceFusion/aigc/queryFaceKeyTask` |
| `K` | `Lak/o;` | `/algo/v1/faceFusion/aigc/queryFaceKeyTaskV2` |
| `H` | `Lak/o;` | `/algo/v1/faceFusion/aigc/queryPictureDetectTask` |
| `c` | `Lak/o;` | `/algo/v1/faceFusion/cancelAiStyleTask` |
| `T` | `Lak/o;` | `/algo/v1/faceFusion/createAiStyleTask` |
| `L` | `Lak/o;` | `/algo/v1/faceFusion/queryAiStyleTask` |

## و اتصال هر مسیر به سازندهٔ بدنه

هر کلاس `Image2VideoServer$create*Task$1` در کد یکی از این متدها را صدا
می‌زند؛ یعنی نقشه دیگر حدس نیست:

| سازندهٔ بدنه | متد کلاینت | مسیر واقعی | وضعیت |
|---|---|---|---|
| `createGXAiVideoTask` | `g.P` | `/algo/v1/faceFusion/aigc/beatImage2Video/createNormalTask` | ✅ کار می‌کند |
| `createAiVideoLtxTask` | `g.C` | `/algo/v1/faceFusion/aigc/image2video/**createTask**` | قبلاً با `image2VideoCreateV3` اشتباه گرفته شده بود |
| `createAiPhotoTaskV3` (PixVerse) | `g.U` | `/algo/v1/faceFusion/aigc/image2VideoCreateV3` | `pixVerseId` لازم دارد |
| `createAiVideoUnifiedTask` | `g.l` | `/algo/v1/faceFusion/aigc/image2video/unifiedTaskCreate` | `example` لازم دارد |
| `createGoogleVeoVideoTask` | `g.g0` | `/algo/v1/faceFusion/aigc/image2video/image2VideoCreateV5` | **پس V5 واقعاً Veo است** |
| `createAiSequenceVideoTask` | `g.X` / `g.c0` | `integrated/image2VideoCreateV4` / `image2video/**integratedTaskCreate**` | نسخهٔ قدیم/نو |
| `createText2VideoTaskVidu` | — | `createText2VideoTask` | — |
| `createVideoHdTaskVidu` | `g.R` | `/algo/v1/faceFusion/aigc/createVideoHdTaskVidu` | تسک GX را رد می‌کند |

### سه نتیجهٔ فوری از این نقشه

1. **LTX هرگز آزموده نشد.** مسیرش `image2video/createTask` است، نه
   `image2VideoCreateV3`. آن یک بار که ۴۰۴ گرفتیم روی **هاست دوم** بود
   (`cpi.wiseoel.com`)، نه هاست اصلی.
2. **`integratedTaskCreate` هرگز آزموده نشد** — فقط `integrated/image2VideoCreateV4`
   آزموده شد که `effectType` را رد کرد. این توضیح می‌دهد چرا تسک‌های
   `INTEGRATED_60019-…` هیچ کوئری‌ای نداشتند: **هرگز از درِ درست وارد نشدند.**
3. **`getAllPoseSequenceId` با annotation نوع `Lak/f;` علامت خورده، نه `Lak/o;`**
   مثل بقیه. یعنی متد دیگری (احتمالاً GET) است؛ POST دادن ۴۰۴ منطقی است.
