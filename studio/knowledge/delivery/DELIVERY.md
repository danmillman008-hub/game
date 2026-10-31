# تحویل

## گردش کار بهینه (۲۰۲۶-۱۰-۳۰)

- `studio/shotplan.py` — پلنر صحنه: لنگر + یک جمله دوربین + یک جمله حرکت؛ زنجیره ≤۲
- `studio/mivi_shot.py --parallel 4 --dry-run --skip-existing` — تولید موازی
- بچ ۸ شاتی: ۲۴ دقیقه سریالی → **~۹ دقیقه**
- `studio/knowledge/workflow/WORKFLOW.md` — خط تولید · `CONSISTENCY_AND_SPEED.md` — پژوهش


## ⭐ صحنهٔ ۶۰ ثانیه‌ای، نسخهٔ ۲ — پرامپت‌های Wan 2

**https://drive.google.com/file/d/1bPl298n5rUc3xJdwCEFlFqJwu9Bpxtvp/view**

- `films/anime_ten/deliver/scene_min1_wan.mp4` — ۶۰.۴۶s · ۱۸MB
- ۱۵ شات، پرامپت‌های ۱۷–۳۲ کلمه‌ای، صفر توصیف ثابت، صفر ناقض قرارداد Wan
- لرزش فیلم ۲۱.۱ → ۱۵.۲ (همان حرکت، کمتر درهم‌برهم)
- قاعده‌ها و A/B: `studio/knowledge/prompting/WAN_PROMPTS.md` · گزارش: `MIN1_REPORT.md`


## ⭐ صحنهٔ ۶۰ ثانیه‌ای — «دروازه» (۱۵ شات، ۱۵ زاویه)

**https://drive.google.com/file/d/1SJVv6DBc0rYNbNZVIgt3sQUft28AuCsH/view**

- `films/anime_ten/deliver/scene_min1.mp4` — ۶۰.۴۶s · ۹۶۰×۱۲۸۰ · ۲۴fps · ۲۳MB
- ۱۵ شات، ۱۱ زاویهٔ متفاوت: های‌انگل ۹۰°، لوانگل از زمین، پروفایل، اکستریم کلوزآپ چشم، اینسرت دست، اور-ده-شولدر، دو-شات
- گزارش کامل با عدد: `MIN1_REPORT.md` · کانتکت‌شیت: `qc/min1_batchA.jpg` و `qc/min1_batchB.jpg`


## ⭐ نمونهٔ ۸ ثانیه‌ای (آخرین، ۲۰۲۶-۱۰-۳۰)

**https://drive.google.com/file/d/1XrcBijPqm_rf5ot_Q-mzEFN6fm_y56_e/view**

- `films/anime_ten/deliver/sample_8s.mp4` — ۸.۰۰ ثانیه، ۹۶۰×۱۲۸۰، ۲۴fps، ۲.۹MB
- روش: کانواس خالی → آرت مدل → زنجیره → یک حرکت دوربین پیوسته
- یک شات بدون کات: از مدیوم‌شات روی بانوی زره‌پوش، دوربین عقب می‌کشد تا نمای باز دروازه
- هیچ کامپوزیتی در کار نیست؛ هر فریم نقاشی خودِ مدل است
- استریپ بازبینی: `qc/sample8_strip.jpg`

# لینک‌های ویدیو

## نسخهٔ درست (این را ببین)

| فایل | توضیح | لینک |
|---|---|---|
| **scene1_v2.mp4** | سکانس ۱ بازسازی‌شده — شیت → ویدیو → زنجیره، بدون کامپوزیت | [Drive](https://drive.google.com/file/d/158qFzZMWpj_R-K0JizAEkazNZdZ22z5B/view) → `films/anime_ten/deliver/scene1_v2.mp4` |
| scene1_pilot.mp4 | خلبان اول — **روش غلط** (کامپوزیت PIL)، فقط برای مقایسه | [Drive](https://drive.google.com/file/d/14U5RtGh5iHGLQah1DJHv1Uga-mds3VpZ/view) → `films/anime_ten/deliver/scene1_pilot.mp4` |

مقایسهٔ چشمی چهار پنلی: `films/anime_ten/qc/method_comparison.jpg`

## کلیپ‌های خام نسخهٔ درست
`films/anime_ten/clips_v2/s01..s06` — و `films/anime_ten/keys/k1..k2`

## آزمون‌های قبلی
`films/short16/clips_gen/` — `a1_rain`, `a2_eye`, `a3_push`, `a4_chain`, `t1_seed`, `t2_cut`, `k3..k6`

# تحویل‌های ۲۰۲۶-۱۰-۳۱

| فیلم | مدت | لینک | فایل در ریپو |
|---|---|---|---|
| **نگهبانان در برف** — دو نگهبان زره‌پوش جلوی دروازهٔ قلعه در برف | ۱۲.۰۰s | [Drive](https://drive.google.com/file/d/19LEf4ANwgPRLiq19G_4c4yDaxjpKbLJo/view) | `films/anime_ten/deliver/winter_guards_12s.mp4` |
| **همان صحنه، یک کست** — هر چهار شات از یک master | ۱۲.۰۰s | [Drive](https://drive.google.com/file/d/1zehYy6d4fIa8Qkgweu1OjG_LX4EjC1Ps/view) | `films/anime_ten/deliver/cast_guards_12s.mp4` |
| **نگهبانان، سل‌انیمه** — master انیمه → پوش‌این → فریم آخر | ۱۱.۵۰s | [Drive](https://drive.google.com/file/d/1UUNNywblqd9madRLquSlWUCbEYmQ3DgZ/view) | `films/anime_ten/deliver/am_guard_11s.mp4` |
| **یک take، سل‌انیمه** — ۲.۹ ثانیه پوش × ۴.۱۴، بدون هیچ کات | ۱۲.۰۰s | [Drive](https://drive.google.com/file/d/1nzpOc5m_rD6yTv8sArN8NuLPQc1AF4ph/view) | `films/anime_ten/deliver/am_push_12s.mp4` |
| **زن سوار بر اسب** — ۳ زاویه، رو به سپاه دشمن | ۱۲.۰۰s | [Drive](https://drive.google.com/file/d/1v4SAygmVcWBOEWkdcKspZxnU9dy8NndT/view) | `films/anime_ten/deliver/horse_charge_12s.mp4` |
| **زن سوار بر اسب — پارت ۲** — شمشیر می‌کشد، خشمگین، به دل سپاه | ۱۲.۰۰s | [Drive](https://drive.google.com/file/d/156vRFxWM11ossWALM9fSLzUCFlSWaanj/view) | `films/anime_ten/deliver/horse_sword_12s.mp4` |
| **زن سوار بر اسب — کامل** — دو پارت، کات در ۱۲.۰ | ۲۴.۰۰s | [Drive](https://drive.google.com/file/d/1XUlfYuFMOCggYnfuk4gJiZpaoU3IPHoC/view) | `films/anime_ten/deliver/horse_battle_24s.mp4` |
| **زن سوار بر اسب — پارت ۳: جنگ** — از پشت خط، موج سواران، آخر حمله به دل سپاه | ۱۲.۰۰s | [Drive](https://drive.google.com/file/d/1y1q0M6-CiASVouKoKrg7cuWI1g3dHACQ/view) | `films/anime_ten/deliver/horse_war_12s.mp4` |
| **زن سوار بر اسب — کامل ۲۴s با وزن جنگ** — نزدیک‌شدن ۸ + شمشیر ۴ + جنگ ۱۲ | ۲۴.۰۰s | [Drive](https://drive.google.com/file/d/1isCvgNbZjCDT0pZYcHs8V9iUoDfsi_xO/view) | `films/anime_ten/deliver/horse_battle_24s_war.mp4` |
| دروازه در باران — پنج شات امضای خانه | ۲۰.۱۷s | — | `films/anime_ten/deliver/rain_gate_20s.mp4` |
| چهار شات تمیز (نسخهٔ کوتاه) | ۱۴.۳۳s | — | `films/anime_ten/deliver/silent_house_14s.mp4` |

**زن سوار بر اسب — پارت ۲:** از فریم آخر پارت ۱. او شمشیر می‌کشد (`hs_sword`)، با
چهرهٔ خشمگین اسب را جلو می‌برد (`hs_war`)، و کات به نمای باز که سواران به دل سپاه
می‌روند (`hs_impact`). ۷ کردیت خرج شد، ۳ تا به فیلم رسید: `hs_clash` (کانواس خالی) پوستر
دود شد، `hs_draw` نیزه به دستش داد، `hs_charge`/`hs_melee` سلاحشان با شات اول نمی‌خواند.
نسخهٔ ۲۴ ثانیه‌ای همان دو پارت است با کاتِ ۱۲.۰ که دیده نمی‌شود (پارت ۲ از همان فریم
شروع می‌شود). ساخت: `films/anime_ten/build_horse24.sh`.

**زن سوار بر اسب — ۳ زاویه:** نمای باز از زاویهٔ کم (ارتش در ردیف، سوار کوچک و بریده با
لبهٔ کادر) → سه‌چهارم روی او، ارتش پشت شانه‌اش → نزدیک از **فریم آخر** همان شات.
۳ کردیت، ۳/۳ موفق. هر take از ۰.۸s تا ۴.۰s (S21)، جمع ۹.۶s، کشش ۱.۲۵× → ۱۲.۰۰s.
روشنایی روی ۸۰ (روز، S23). ساخت: `films/anime_ten/build_horse12.sh`؛ طرح و محدودیت‌ها:
`films/anime_ten/story_horse.md`.

**یک take، سل‌انیمه — ۱۲ ثانیه، صفر کات:** پوش بی‌وقفه از دروازه تا دو چهره.
سه take (ثابت/آرام/تند) از همان master گرفته شد؛ نتیجه: مدل روی نقاشی تخت **همیشه**
پوش می‌کند و سرعت را پرامپت تعیین نمی‌کند، و چون هر take از یک فریم شروع می‌شود هر
کاتی مقیاس را به عقب می‌برد. پس یک take کش آمد: ۲.۹s × ۴.۱۴ با `minterpolate`.
نور ۵۷.۵–۶۰.۰ در کل ۱۲ ثانیه. ساختار: `films/anime_ten/build_am_push12.sh`.

**نگهبانان، سل‌انیمه — ۳ شات:** پوش‌این از دروازه تا سینه → دو چهره در برف →
کات به نمای باز و فید. ساخت: **یک** master روی کانواس `snow` (کردیت ۱) → پوش با
دوربین داخل همان کلیپ (کردیت ۳) → شات سوم از **فریم آخر همان پوش** (کردیت ۴).
کردیت ۲ (`compose` برای گرفتن کلوزآپ) جواب **نه** داد و ثبت شد. یک کست در هر سه شات،
سبک سل‌انیمه، `lumatch` روی ۵۸ (اختلاف میانگین سه شات: ۰.۴).
ساختار: `films/anime_ten/build_am_film.sh`.

**نگهبانان در برف — ۴ شات:** دروازه در برف (نمای باز) → دو-شات دو نگهبان → کلوزآپ
نگهبان چپ → کلوزآپ نگهبان راست. ساخت: چهار لنگر (`w_gate`, `w_two`, `c_left`, `c_right`)
روی کانواس `snow`، بعد چهار شات با دوربین قفل و بدون تغییر ژست، بعد `lumatch.py`
برای هم‌ترازی روشنایی (اختلاف میانگین چهار شات: ۹.۱ از ۲۵۵).

بازبینی: `studio/knowledge/method/HOUSE_STYLE.md` (take ۱۷–۲۹) · `winter_luma.json`

**پارت ۳ — جنگ (۲۰۲۶-۱۰-۳۱).** دلیل شکست take‌های قبلی پیدا شد: مدل همیشه روی
قوی‌ترین **چهرهٔ** کادر پوش می‌کند و «دوربین عقب می‌کشد» این پوش را لغو نمی‌کند
(اندازه‌گیری: `hw_pull` دقیقاً مثل بقیه روی صورتش نشست). پس هر شات جنگ با یکی از دو
شرط ساخته شد: کادری که چهرهٔ خوانا ندارد (همه از پشت / کلاه‌خود)، یا بریدن take قبل از
رسیدن پوش. پنجرهٔ هر take با روشنایی فریم‌به‌فریم اندازه‌گیری شد — `hw_backs` و
`hw_wall` از کانواس می‌آیند و ۱.۰/۱.۴ ثانیه اول محو از سیاه است، `hw_surge` و
`hw_pull` و `hs_impact` از تصویر می‌آیند و محو ندارند. حرکت جمعیت در `hw_surge`
اندازه‌گیری شد: اختلاف میانگین فریم‌ها ۲۷.۶ / ۳۱.۱ / ۴۷.۶ (شات‌های ایستادهٔ قبلی ۲–۶).
ساخت: `films/anime_ten/build_horse_war.sh` — شمارش فریم دقیق، ۲۸۸ و ۵۷۶ فریم.
