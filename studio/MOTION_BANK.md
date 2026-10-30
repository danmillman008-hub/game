# بانک حرکات — `studio/motions/bank.json`

> قلب پروژهٔ فعلی. هر پرامپت تولید از اینجا ساخته می‌شود، و پرامپتی که قاعده‌ها را
> نشکند اجازهٔ تولید نمی‌گیرد.

> ⚠️ **به‌روزرسانی ۲۰۲۶-۱۰-۳۰ — قالب پرامپت عوض شد.** بلوک‌های `[shot]/[place]/[subject]`
> که پایین‌تر می‌بینی، **دیگر ساخته نمی‌شوند**. از این تاریخ `compose` نثر می‌نویسد
> (زیر ۱۰۰ کلمه، فقط حرکت، بدون بلوک منفی) چون قرارداد رسمی Wan همین است:
> [`knowledge/prompting/WAN_PROMPTS.md`](knowledge/prompting/WAN_PROMPTS.md).
> مثال قدیمی برای تاریخ نگه داشته شده، نه برای تقلید.
> دو بانک هم داریم: `bank.json` (لایو‌اکشن) و `anime_bank.json` (سل). با `--bank` انتخاب
> کن؛ id اشتباه حالا با کد ۱ رد می‌شود، نه اینکه بی‌صدا در پرامپت بنشیند.

## چه چیزی داخل بانک است

| دسته | تعداد | نمونه |
|---|---|---|
| `camera` | ۱۱ | `static_locked`, `micro_push`, `slow_dolly_in`, `track_left`, `orbit_small` |
| `shot_size` | ۸ | `ews`, `ws`, `ms`, `mcu`, `cu`, `ecu`, `ots`, `two_shot` |
| `subject` | ۱۵ | `rise_from_bench`, `walk_two_steps`, `embrace_and_hold`, `lift_umbrella`, `hand_umbrella` |
| `micro` | ۸ | `umbrella_settle`, `breath_visible`, `fingers_tighten`, `drip_edge` |
| `emotion` | ۷ | `calm`, `grief`, `hesitation`, `surrender`, `relief` — هر کدام با ترجمهٔ بدنی |
| `environment` | ۶ | `rain_lamp`, `bokeh_traffic`, `wet_asphalt`, `steam_vent` |
| `look` | ۳ | `cine_night`, `cu_night`, `wide_night` |
| `negative` | ۲ | `default`, `static` |

هر ورودی `en` (متن پرامپت)، `fa` (برچسب فارسی) و در صورت نیاز `default` برای
مقدار عددی دارد. منبع هر دسته در `sources` ثبت شده.

## قاعده‌ها — `lint` آن‌ها را اجرا می‌کند

| قاعده | چه چیزی را می‌گیرد |
|---|---|
| `one_move` | دو یا چند حرکت دوربین در یک شات |
| `state_static` | نبودِ جملهٔ صریح دربارهٔ دوربین |
| `micro_magnitude` | «subtle / slight / gentle» بدون عدد |
| `no_zoom_word` | استفادهٔ `zoom` برای حرکت فیزیکی |
| `one_beat` | چند «then» در یک کلیپ ۴ ثانیه‌ای |
| `end_state` | نبودِ «by the last frame …» |
| `negative` | نبودِ بلوک منفی |

نکتهٔ پیاده‌سازی: جمله‌های منفی («no zoom, no pan») قبل از شمارش حذف می‌شوند،
وگرنه خودِ همان محافظت به‌عنوان تخلف شمرده می‌شد.

## نمونهٔ واقعی

```
$ python3 studio/motionbank.py lint "…camera does not move. She steps forward and
  embraces him, arms wrapping, he holds the umbrella, subtle sway, no text"
score 76  [micro_magnitude] vague motion words with no number: ['subtle']
          [end_state] no end-state anchor
```

همان پرامپت قبلی خودمان بود که چتر در آن «برگشتی» شد. حالا از بانک:

```
$ python3 studio/motionbank.py compose films/short16/shots_hug.json
OK h1_rise  (static, 1 beat)  score=100
OK h2_hold  (static, 1 beat)  score=100
```

و پرامپت خروجی:

```
[shot] wide shot, locked-off static camera on a tripod, the camera never moves, no zoom, no pan, no handheld
[subject] her arms come up around his shoulders and stay there; his free arm settles across her back and stays;
          from this moment neither moves their feet
[place] same bus stop, same lamp, same framing as the previous clip
[motion] the umbrella tilts back no more than a few centimetres and settles; breath visible …
[environment] rain falling steadily through the cone of the streetlamp
[end] by the last frame: they are still, her cheek on his shoulder
[look] photorealistic wide, 28mm, deep focus, wet street reflections, film grain
[negative] no camera movement at all, no drift, no reframing, no text, no subtitle
```

## اتصال به پایپ‌لاین

```
shots.json ──► motionbank jobs ──► gen_jobs.json ──► (GitHub runner) mivi_shot
                     │                                        │
                     └── lint (بدون عبور، هشدار) ◄─────────────┘
```

سه نقطهٔ اتصال که واقعاً وصل شده‌اند:

1. **`motionbank.py jobs <spec> --out gen_jobs.json`** — خروجی همان فرمتی است که
   `studio/mivi_shot.py` می‌خورد.
2. **`.github/workflows/mivi.yml`** — ورودی `spec` دارد؛ اگر بدهی، قبل از تولید
   `motionbank jobs` اجرا می‌شود و خروجی‌اش جای فایل پیش‌فرض می‌نشیند.
3. **`studio/mivi_shot.py`** — قبل از هر تولید، پرامپت را با `motionbank.lint`
   می‌سنجد و در لاگ هشدار می‌دهد. یعنی هیچ تولیدی روی پرامپت بد خرج نمی‌شود.
4. **`studio/chainkit.py bridge --motion-spec shot.json`** — پرامپت لینک از بانک
   ساخته می‌شود و `prompt.lint.json` کنار پکیج لینک ذخیره می‌ماند.

## افزودن حرکت تازه

```json
{"id": "shoulder_check", "en": "he glances over his shoulder once, then back to her",
 "fa": "نگاه از روی شانه", "beats": 1}
```

قاعدهٔ نانوشته: هر ورودی `subject` باید **یک بیت** باشد. اگر دو کار در یک جمله
داری، دو ورودی بساز؛ ترکیبشان در یک پرامپت همان اشتباه قدیمی است.
