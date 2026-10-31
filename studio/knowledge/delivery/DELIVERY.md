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
| **نگهبانان، سل‌انیمه** — master انیمه → پوش‌این → فریم آخر | ۱۱.۵۰s | — | `films/anime_ten/deliver/am_guard_11s.mp4` |
| دروازه در باران — پنج شات امضای خانه | ۲۰.۱۷s | — | `films/anime_ten/deliver/rain_gate_20s.mp4` |
| چهار شات تمیز (نسخهٔ کوتاه) | ۱۴.۳۳s | — | `films/anime_ten/deliver/silent_house_14s.mp4` |

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
