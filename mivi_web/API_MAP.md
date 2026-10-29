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
