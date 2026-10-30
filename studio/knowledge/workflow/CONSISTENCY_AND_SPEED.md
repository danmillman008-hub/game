# تداوم هویت و سرعت — چه چیزی در دنیا جواب داده

> سه ایراد باقی‌مانده: **هویت در زنجیره می‌شکند**، **تولید کند شده**، **کلوزآپ‌ها
> قاب‌بندی دقیق نمی‌گیرند**. گشتم؛ هم ریپو، هم تجربهٔ آدم‌ها. هر ادعا منبع دارد.

## ۱) هویت در زنجیره — قاعده‌ای که همه به آن رسیده‌اند

از یک راهنمای عملی زنجیره‌سازی:

> «Quality drifts a little each pass... By the third or fourth pass the character can
> look a touch less like herself. **I keep chains to two or three links** for that
> reason.» — [samefacekit](https://samefacekit.tech/blog/longer-ai-videos-comfyui-chaining-clips/)

و همان‌جا، گزینه‌ای که اکثراً فراموش می‌شود:

> «There's also a cheaper option people forget: **don't chain at all.** Make each shot
> from a fresh still ... **a cut hides any mismatch, and every shot starts from full
> quality.**»

در r/comfyui هم دو نفر مستقل همین را می‌گویند:

> «I can only generate **1 next scene** to keep it similar in style to the initial
> image, and I try to create **every scene I want from the first initial image**.»
> — [r/comfyui](https://www.reddit.com/r/comfyui/comments/1oaxtfu/wan_22_long_videos_without_loosing_context_and/)

این با آنچه خودمان دیدیم یکی است: بچ دومی که ۸ شات زنجیره بود، مرد را موبلند و
شلوارجین کرد و مکان را به خیابان شهری برد.

### سه راه‌حل، به ترتیب هزینه

| راه | چه می‌کند | چه لازم دارد |
|---|---|---|
| **لنگر (adopted)** | هر شات از یک استیل تأییدشده شروع می‌شود؛ زنجیره فقط ۱–۲ حلقه | هیچ چیز اضافه، همین امروز |
| **فریم اول/آخر (FLF2V)** | مدل مقصد را می‌بیند، پس هویت را وسط راه عوض نمی‌کند | ❌ **تست شد، جواب نداد** — [`FLF_PROBE.md`](FLF_PROBE.md) |
| **مرجع/آنی‌میت (بعد)** | `Wan-Animate-2`, `VACE`, `SkyReels-A2`, `Phantom` سوژه را از تصویر مرجع نگه می‌دارند | اجرای مدل روی GPU خودمان یا سرویس‌دهنده‌ای که این مسیر را بدهد |

FLF در ComfyUI جواب اصلی است — ولی **API میوی آن را نمی‌فهمد** (آزمون: [`FLF_PROBE.md`](FLF_PROBE.md)). همان نقل‌قول‌ها برای اجرای محلی معتبرند:

> «I recommend doing a first to last frame workflow or even the first to middle to last
> frame... the character doesn't change as much since the AI knows how the character
> should look at the end.»
> — [r/comfyui: Wan 2.2 I2V Face Consistency](https://www.reddit.com/r/comfyui/comments/1q9ku7o/wan_22_i2v_face_consistency_help/)

و راه‌حل «بعد از تولید»: فیس‌سوآپ روی کلیپ نهایی (FaceFusion / ReActor).

## ۲) سرعت — چرا ۶۰ ثانیه شد ۱۸۰ ثانیه

عددی که از منابع درآمد:

| تنظیم | زمان هر کلیپ ۵ ثانیه‌ای | منبع |
|---|---|---|
| Wan 2.2 14B، ۲۰ استپ، 640×640 | ~۵۱۳ ثانیه | [runpod](https://www.runpod.io/articles/guides/comfyui-wan-2-2) |
| همان + **Lightning LoRA (۴ استپ)** | **~۷۱ ثانیه** (۵ تا ۷ برابر) | همان |
| ۴ استپ + کارت ۱۲GB با block swap | ۳ تا ۵ دقیقه | [earngenix](https://www.earngenix.com/workflows/wan-2-2-fast-comfyui) |
| فقط `cfg=1.0` روی سمپلر دوم | **۲۴٪ سریع‌تر** (۶۳۲→۴۷۷ ثانیه) | [jarvislabs](https://jarvislabs.ai/blog/wan-2-2-faster-one-setting) |

**مهم:** اینها برای اجرای محلی است. ما از API میوی استفاده می‌کنیم و به استپ/
کوانتیزه دسترسی نداریم. پس سرعت را جای دیگری باید برد:

### کاری که همین حالا شد (بدون تغییر مدل)

`studio/mivi_shot.py` قبلاً **یکی‌یکی** تسک می‌ساخت و منتظر می‌ماند؛ رانر در تمام
مدت فقط poll می‌کرد. تسک‌ها روی سرور مستقل‌اند، پس حالا:

- **`--parallel N`** — N تسک هم‌زمان در پرواز، poll مشترک
- **`--dry-run`** — گراف وابستگی، عمق زنجیره و تخمین زمان **قبل** از خرج
- **`--skip-existing`** — کلیپ موجود دوباره ساخته نمی‌شود
- پلنر لنگر: `studio/shotplan.py` — از یک فایل صحنه، جاب‌فایل موازی می‌سازد

عدد روی همان بچ ۸ شاتی: **۲۴ دقیقه سریالی → ~۹ دقیقه با parallel=4**.

### سرعتی که هنوز روی میز است

- **`ModelTC/LightX2V`** (۲٬۹۷۵★، Apache) — دیستیل ۴ استپ؛ فقط اگر خودمان مدل را
  اجرا کنیم معنی دارد.
- **`thu-ml/SageAttention`** (۳٬۹۸۴★) ۲–۵ برابر، **`TurboDiffusion`** (۳٬۸۵۹★)
  ۱۰۰–۲۰۰ برابر — همان شرط.
- **`ali-vilab/TeaCache`** (۱٬۳۸۷★) — کش تایم‌استپ، بدون آموزش.
- سمت API: کمتر کردن تعداد تلاش، و **کوتاه کردن زنجیره** (زنجیره = تولید سریالی).

## ۳) کلوزآپ — چرا قاب نمی‌گیرد

دو علت، هر دو قابل رفع:

1. **زنجیره از نمای باز** ⇒ مدل هنوز «آدم کوچک در قاب» را می‌بیند و همان را ادامه
   می‌دهد. راه‌حل: کلوزآپ از **لنگر کلوزآپ** شروع شود، نه از نمای باز. (همین الان
   در `shotplan.py` لنگر جدا برای `her_face` گذاشتم.)
2. **جملهٔ دوربین بدون سوژهٔ صریح** ⇒ در فریمی که دو نفر هستند، مدل صورت اشتباه را
   انتخاب می‌کند (در بچ دوم دقیقاً همین شد). قاعده: «The camera moves in on **the
   man in the red coat**.»

## ۴) چیزهایی که فقط با GPU خودمان ممکن است

| ریپو | ★ | چه می‌دهد |
|---|---|---|
| `Wan-Video/Wan-Animate-2` | ۳۶۰ | انیمیت کاراکتر با حفظ هویت + کنترل زاویهٔ دوربین با متن |
| `ali-vilab/VACE` | ۴٬۰۲۴ | reference-to-video، extend با overlap |
| `yihao-meng/HoloCine` | ۷۰۴ | چند-شات سینمایی با تداوم کاراکتر بین شات‌ها |
| `KlingAIResearch/MultiShotMaster` | ۱۸۴ | چند-شات قابل کنترل |
| `SkyworkAI/SkyReels-V2` | ۷٬۷۵۱ | ویدیوی بی‌نهایت با تداوم |

اینها مسیر «فیلم ۱۰ دقیقه‌ای» است، نه مسیر API فعلی. در `BANK.md` با گپ
`k-continuity` ثبت شدند.

## منابع

- Wan2.2 `wan/utils/system_prompt.py` (قرارداد پرامپت I2V) — [repo](https://github.com/Wan-Video/Wan2.2)
- [samefacekit — chaining clips](https://samefacekit.tech/blog/longer-ai-videos-comfyui-chaining-clips/)
- [r/comfyui — long videos without losing context](https://www.reddit.com/r/comfyui/comments/1oaxtfu/wan_22_long_videos_without_loosing_context_and/)
- [r/comfyui — I2V face consistency](https://www.reddit.com/r/comfyui/comments/1q9ku7o/wan_22_i2v_face_consistency_help/)
- [runpod — Wan 2.2 GPU guide (زمان‌ها)](https://www.runpod.io/articles/guides/comfyui-wan-2-2)
- [jarvislabs — cfg 1.0 = ۲۴٪ سریع‌تر](https://jarvislabs.ai/blog/wan-2-2-faster-one-setting)
- [earngenix — Lightning LoRA](https://www.earngenix.com/workflows/wan-2-2-fast-comfyui)
