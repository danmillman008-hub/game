# ریپو به‌ازای هر شکاف — نتیجهٔ جست‌وجو

> مکمل `GAPS.md`. برای هر شکاف (A تا K) ریپوهای واقعی جست‌وجو و بازبینی شدند:
> ستاره، لایسنس، آخرین پوش، و «چرا/چرا نه». تاریخ: ۲۰۲۶-۱۰-۳۰.

---

## ۱) شکاف A — گرامر برش (J-cut / L-cut / برش روی مرز کلمه)

| ریپو | ★ | لایسنس | آخرین پوش | حکم |
|---|---|---|---|---|
| `FireRedTeam/FireRed-OpenStoryline` | 3,595 | Apache-2.0 | 2026-07-31 | ⭐ **مهم‌ترین.** ایجنت تدوین با زبان طبیعی. سه قابلیت مستقیماً مال ما: **rough cut با ASR** (حذف پرکننده/تکرار با تایم‌استمپ کلمه)، **AI Transition Generation** (شات گذار از *آخرین فریم کلیپ A* + *اولین فریم کلیپ B* می‌سازد)، و **بایگانی Skill** (کل جریان تدوین را ذخیره می‌کند) |
| `open-ribbi/velocut` | 453 | MIT | 2026-10-13 | ایجنت‌محور و مرورگری (Rust/WASM، WebGPU)؛ انسان و LLM روی یک تایم‌لاین کار می‌کنند |
| `fxl1209739475-fxl/ai-xunjian` | 41 | MIT | 2026-08-07 | «برش خشن» قاعده‌محور: رونویسی، برش سکوت، پرش؛ نزدیک به نیاز ما |
| `mitch7w/ai-video-editor` | 54 | — | 2025-04-09 | LLM چند کلیپ را می‌چسباند؛ قدیمی، بدون لایسنس |
| `andriidrok1/autobroll` | 24 | MIT | — | مرتب‌سازی برداشت‌ها و برش سکوت، مرورگری |
| `kwakseongjae/dawn-cut` | 12 | MIT | — | تدوین متن‌محور، کاملاً محلی |

**قابل برداشت:** الگوی artifact «edit_decisions» با فیلدهای
`cuts[] / overlays[] / subtitles / music / transitions` (از OpenMontage) + منطق
«برش روی مرز کلمه» از OpenStoryline. J/L-cut خودش ~۸۰ خط است و ریپو لازم ندارد.

---

## ۲) شکاف B — ریتم و پیسینگ

| ریپو | ★ | لایسنس | حکم |
|---|---|---|---|
| `Vincentwei1021/video-shotcraft` | **14,955** | Apache-2.0 | ⭐ **گنجینهٔ این دور.** اسکیل Claude Code/Codex با **۱۲۴ کارت / ۱۵۰ شات** در `references/shots/{camera,transition,rhythm,opening,outro,effects,typography,interaction,ui-entrance,data}` + `references/music-beat-sync.md` |
| `Alpha-Park/moras-...-pacing-composer-skill` | 7 | — | کامپوزر ریتم صحنه؛ کوچک ولی دقیقاً همین موضوع |

**قابل برداشت از `music-beat-sync.md`** (روش کمّی، نه سلیقه‌ای):
- «**موسیقی اول**»: تا شبکهٔ ضرب تأیید نشود، فهرست شات طراحی نمی‌شود.
- شبکهٔ ضرب با **کمترین مربعات** روی دنبالهٔ بیت فیت می‌شود؛ به اسکالر tempo
  اعتماد نکن (اندازه‌گیری: ۱۲۹.۲ در برابر ۱۳۱.۹۷ واقعی، خطای ۲٪+).
- همهٔ زمان‌ها **ثانیهٔ اعشاری** می‌مانند؛ تبدیل به فریم **فقط در آخرین مرحله**.
- معیار قبولی: خطای هر برش **≤ ۳ فریم** (اندازه‌گیری‌شده ۲.۲f روی یک ۷۰ ثانیه/۱۸ شات/۱۳۱.۹۷BPM).

---

## ۳) شکاف C — قاعدهٔ مِرچ و انتخاب نقطهٔ برش

| ریپو | ★ | لایسنس | حکم |
|---|---|---|---|
| `FireRedTeam/FireRed-OpenStoryline` | 3,595 | Apache | «intention-driven directing» — از دستور زبانی به تصمیم برش |
| `koosoli/OpenShotDesigner` | 35 | — | سوئیت پیش‌تولید: **lined script، پلان کف، shot list، استوری‌بورد، فهرست تجهیزات** (2026-10-26، فعال) |

سلسله‌مراتب مِرچ (احساس > داستان > ریتم > مسیر نگاه > قانون ۱۸۰ > فضای سه‌بعدی)
از `OpenMontage/skills/creative/cinematic.md` — کد لازم ندارد، ترتیب تصمیم است.

---

## ۴) شکاف D — داستان و ساختار

| ریپو | ★ | لایسنس | حکم |
|---|---|---|---|
| `dungnotnull/plot-screenplay-structure-analyzer-agent-skill` | 5 | MIT | اسکیل تحلیل ساختار روایت: **تشخیص پیسینگ و قوس شخصیت** |
| `CCrowRun/save-the-cat-beats` | 1 | — | تفکیک بصری **۱۵ بیت Save the Cat** |
| `kirklasalle/CineMatrix` | 6 | MIT | پیش‌تولید و استودیوی کارگردانی از فیلمنامه |
| `66530/BeatSheet-AI` | 0 | — | بازسازی رمان به بیت‌شیت |

ارزش واقعی همچنان در متن `OpenMontage/skills/creative/storytelling.md` است
(قوس با تایم‌کد، قاعدهٔ ۳۰ ثانیه، «but/therefore»، برچسب گذارِ سوژه) — ریپوهای
بالا فقط ابزار هستند.

---

## ۵) شکاف E — قاعدهٔ ضدذهنی

هیچ ریپوی اختصاصی پیدا نشد. منبعش همان `OpenMontage` است (Anti-Subjective Rule) و
جدول «احساس ← بدن» از `cclank/lanshu-awesome-ai-video-kit` که قبلاً برداشتیم.
**این شکاف با نوشتن حل می‌شود، نه با کد.**

---

## ۶) شکاف F — تطبیق رنگ

| ریپو | ★ | لایسنس | حکم |
|---|---|---|---|
| `hahnec/color-matcher` | 678 | **GPL-3.0** | جامع‌ترین: Reinhard / MKL / IDT / MVGD / **Wasserstein**، هم‌راستاسازی چند‌مرجعی. ⚠️ GPL — اگر کدش را وارد کنیم کل پروژه GPL می‌شود؛ فقط **الگوریتم** را بخوان |
| `fayadanthony/color-transfer-optimal-transport` | 0 | MIT | مقایسهٔ هیستوگرام در برابر انتقال بهینهٔ transporte — مرجع ریاضی |
| OpenCV (خودِ کتابخانه) | — | Apache | `cv2.createCLAHE`, تطبیق هیستوگرام Lab — برای ما کافی است |

**تصمیم:** خودمان با OpenCV می‌نویسیم (تطبیق میانگین+انحراف در Lab با شدت ۰.۷)،
چون `color-matcher` GPL است.

---

## ۷) شکاف G — صدا و داکینگ

| ریپو | ★ | لایسنس | آخرین پوش | حکم |
|---|---|---|---|---|
| `librosa/librosa` | 8,724 | ISC | 2026-10-06 | ⭐ لازم برای تحلیل بیت و پوش انرژی (همان روش shotcraft) |
| `guigulaoshi/music-video-director-skill` | 62 | MIT | 2026-09-25 | اسکیل کارگردانی موزیک‌ویدئو؛ الگوی «موسیقی → برش» |
| `mfahsold/montage-ai` | 60 | NOASSERTION | 2026-03-09 | تدوین محلی بر پایهٔ رونویسی + **beat sync** |
| `R0mb0/Auto_podcast_mixer` | 0 | MIT | — | میکس خودکار گفتار (داکینگ) — الگوی ffmpeg |

اعداد داکینگ و EQ از `OpenMontage/skills/creative/sound-design.md` (موسیقی ۱۸–۲۰dB
زیر دیالوگ، کات ۲–۴kHz، SFX با شروع ۱۰–۲۰ms قبل از تصویر).

---

## ۸) شکاف H — پرامپت موتور (طول ۲۰۰–۴۰۰ کلمه برای Wan)

| ریپو | ★ | لایسنس | حکم |
|---|---|---|---|
| `ddia56/wan22_prompt_selector` | 204 | — | بر پایهٔ سند رسمی Wan 2.2 |
| `Zambav/ComfyUI-Agent-Toolkit` | 20 | MIT | راهنمای Wan 2.2 با ترتیب Subject→Action→Camera |
| `ai-boost/awesome-image-video-prompts` | 3,409 | GPL-3.0 | ۹۴۰ نمونهٔ YAML با خروجی واقعی (فقط مطالعه) |
| `cclank/lanshu-awesome-ai-video-kit` | 437 | MIT | ۲۱ سند روش؛ جدول احساس→بدن |

---

## ۹) شکاف I — کیفیت خودکار

| ریپو | ★ | لایسنس | حکم |
|---|---|---|---|
| `VQAssessment/DOVER` | 535 | NOASSERTION | ICCV 2023، ارزیابی **زیبایی‌شناختی + فنی** ویدیو، وزن منتشرشده. نیاز به GPU؛ ولی مدل ذهنی‌اش (دو محور جدا) را می‌شود با `scorer.py` تقلید کرد |
| `jyfu-vcl/CodecArena_public` | 6 | — | داور VLM برای کیفیت |
| `breno-sh/vlm-vqa-judge-artifact` | 0 | — | داورهای zero-shot VLM |

**وضعیت ما:** `scorer.py` (۸ متریک) + `motionlint.py` (تشخیص برگشت حرکت) داریم؛
کاری که مانده: اجرای خودکار در ران و رد‌کردن کلیپ بدبین.

---

## ۱۰) شکاف J — تصویر (letterbox، fps، upscale، interpolation)

| ریپو | ★ | لایسنس | حکم |
|---|---|---|---|
| `k4yt3x/video2x` | **22,481** | AGPL-3.0 | ⭐ چتری برای upscale + interpolation (Real-ESRGAN + RIFE) — فقط CLI، کدش را وارد نکن |
| `hzwer/ECCV2022-RIFE` | 5,630 | MIT | ⭐ درون‌یابی فریم؛ ۳۲→۶۴fps یا نرم‌کردن حرکت کند |
| `nihui/rife-ncnn-vulkan` | 1,122 | MIT | همان RIFE با Vulkan، بدون نیاز به CUDA کامل |
| `Kiteretsu77/FAST_Anime_VSR` | 74 | MIT | Real-CUGAN + Real-ESRGAN سبک |

letterbox و ۲۴fps را خودمان با ffmpeg می‌زنیم (بدون ریپو).

---

## ۱۱) شکاف K — تداوم به‌عنوان داده

| ریپو | ★ | لایسنس | آخرین پوش | حکم |
|---|---|---|---|---|
| **`raccordhq/raccord`** | 1 | — | 2026-08-03 | ⭐⭐ **مهم‌ترین کشف این جست‌وجو.** «اسکریپت سوپروایزر برای ویدیوی مولد»: جهان به‌صورت داده (کاراکتر/پراپ/مکان + رخدادهای تغییر حالت)، **کامپایلر قطعی** (همان ورودی ⇒ همان خروجی بایت‌به‌بایت)، **۷ بررسی** (هویت، ظاهر، پراپ، رنگ، هندسه، پایداری، داور معنایی)، **نردبان تعمیر** (re-roll → re-seed → flag)، خروجی EDL/OTIO |
| `koosoli/OpenShotDesigner` | 35 | — | 2026-10-26 | lined script + shot list + پلان کف |
| `raccordhq`، `Zachiran42/continuity-ai`، `mohithhh/Continuity-Room` | 0–1 | MIT | — | نمونه‌های کوچک «اسکریپت سوپروایزر AI» |

`raccord` فقط ۱ ستاره دارد ولی معماری‌اش **دقیقاً** همان چیزی است که ما تکه‌تکه
ساخته‌ایم (CHAR_LOCK، داور، نردبان تلاش). باید کامل خوانده شود.

---

## ۱۲) زیرساخت مشترک (توصیهٔ قطعی)

| ریپو | ★ | لایسنس | چرا |
|---|---|---|---|
| `AcademySoftwareFoundation/OpenTimelineIO` | 2,046 | Apache-2.0 | ⭐ فرمت استاندارد تایم‌لاین. اگر خروجی ما OTIO باشد، هر NLE (Resolve/Premiere) آن را باز می‌کند — پایان قفل‌شدن در ffmpeg |
| `iluvcapra/pycmx` | 31 | MIT | پارس/تولید **EDL (CMX 3600)** برای تحویل به تدوین‌گر انسانی |
| `librosa/librosa` | 8,724 | ISC | بیت، پوش انرژی، تحلیل صدا |

---

## ۱۳) جدول نهایی — چه بگیریم، چه نه

| اولویت | ریپو | چه چیزی | نوع استفاده |
|---|---|---|---|
| **P0** | `Vincentwei1021/video-shotcraft` | کارت‌های شات + روش beat-sync با خطای ≤۳ فریم | خواندن و اقتباس (Apache) |
| **P0** | `raccordhq/raccord` | معماری «جهان به‌عنوان داده + کامپایلر قطعی + ۷ بررسی» | خواندن معماری |
| **P0** | `AcademySoftwareFoundation/OpenTimelineIO` | فرمت تایم‌لاین | وابستگی مستقیم |
| **P1** | `FireRedTeam/FireRed-OpenStoryline` | rough cut با ASR، شات گذار از فریم آخر/اول | خواندن + ایده |
| **P1** | `hzwer/ECCV2022-RIFE` | درون‌یابی فریم | ابزار CLI |
| **P1** | `librosa/librosa` | تحلیل ریتم | وابستگی |
| **P2** | `hahnec/color-matcher` | الگوریتم‌های انتقال رنگ | فقط مطالعه (GPL) |
| **P2** | `VQAssessment/DOVER` | چهارچوب ارزیابی دو‌محوری | مطالعه (GPU) |
| **P2** | `iluvcapra/pycmx` | EDL | اختیاری |
| ✕ | `mitch7w/ai-video-editor`, `66530/BeatSheet-AI`, `Alpha-Park/…` | بدون لایسنس / رها‌شده | رد |

---

## ۱۴) یک جملهٔ جمع‌بندی

از ۱۷ ریپوی این دور، **سه‌تا واقعاً مسیر را عوض می‌کنند**:
`video-shotcraft` (کارت شات + روش عددی beat-sync)، `raccord` (جهان به‌عنوان داده)،
و `OpenTimelineIO` (فرمت تایم‌لاین). بقیه یا خیلی کوچک‌اند یا فقط تأیید می‌کنند
که راه ما درست است.
