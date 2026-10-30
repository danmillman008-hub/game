# نگارش پرامپت حرکت — قواعد استخراج‌شده + لیست ریپوها

> هدف: حرکتِ طبیعی. ایراد ما «اسمبلی» نبود، «جمله‌بندی» بود.

---

## ۱) شش قاعده‌ای که از منابع درآمد

### قاعدهٔ ۱ — یک حرکت، نه چند
در هر شات فقط **یک** حرکت دوربین. ترکیب «dolly + pan + tilt» شایع‌ترین دلیل لرزش و
چرخش ناخواسته است (higgsfield-camera، بخش The One-Move Rule).

### قاعدهٔ ۲ — «ثابت» را صریح بنویس
اگر دوربین نباید حرکت کند، **همین را بنویس**: `locked-off static camera, no movement`.
اگر ننویسی، مدل خودش drift اختراع می‌کند. «no zoom, no pan» تنها کافی نیست —
بهترین شکل: `the camera is locked off on a tripod and never moves`.

### قاعدهٔ ۳ — حرکت کوچک را با **فاصله و زمان** بنویس
برای حرکت‌های ریز، مقدار و مدت لازم است وگرنه مدل اغراق می‌کند:
`over the full 4 seconds the camera pushes in only 10–15 centimeters — slow enough to barely register`.
و هرگز برای حرکت فیزیکی کلمهٔ `zoom` ننویس؛ `dolly` / `push in` / `track` بنویس.

### قاعدهٔ ۴ — احساس را به **بدن** ترجمه کن
مدل «غمگین» و «آرام» را نمی‌فهمد؛ «شانه‌ها پایین، نفس آرام، سر کمی خم» را می‌فهمد.
این جدول از `04-情绪外化表` گرفته شده و مهم‌ترین ابزار برای ما است:

| حالت | ترجمهٔ بدنی |
|---|---|
| آرامش / خستگی | شانه‌ها پایین می‌آید، سر کمی خم می‌شود، یک بازدم بلند |
| غم | نگاه پایین، پلک سنگین، دست‌ها بی‌هدف جمع می‌شوند |
| تردید | دهان باز می‌شود و بسته، نگاه می‌لغزد، وزن روی یک پا |
| تسلیم / آغوش | شانه‌ها رها، وزن به سمت دیگری می‌رود، دست‌ها بالا می‌آید و می‌ماند |
| تنش | فک قفل، نفس کوتاه، انگشتان باز و بسته |

### قاعدهٔ ۵ — یک بیت در هر کلیپ
هر کلیپ ۴ ثانیه‌ای فقط **یک** رویداد. «بلند می‌شود، راه می‌رود، در آغوش می‌گیرد»
سه بیت است و مدل هر سه را نصفه انجام می‌دهد.

### قاعدهٔ ۶ — دنبالهٔ زمانی و حرکت محیطی
با `first … then … by the end` ترتیب را تحمیل کن، و یک حرکت پس‌زمینهٔ مستقل بده
(باران، بخار، برگ) تا فریم زنده بماند.

---

## ۲) قالب پیشنهادی برای کلیپ ۴ ثانیه‌ای Mivi

```
[Shot]        locked-off static wide shot, tripod, the camera never moves, no zoom, no pan
[Subject]     Raha (woman, long dark hair, grey coat, dark scarf) and Arad (man, grey coat, black umbrella)
[Place]       rainy bus stop at night, warm streetlamp behind them, wet asphalt reflections
[One beat]    she rises from the bench — weight shifts forward, hands push off the slat, coat falls straight
[Physics]     the umbrella above him sways slightly with his breathing, water drips from its edge
[End state]   by the last frame she is standing, still holding his gaze
[Look]        photorealistic, 35mm, shallow depth of field, film grain
[Negative]    no text, no subtitle, no camera shake, no morphing, no warping, no extra fingers
```

---

## ۳) بازنویسی پرامپت‌های واقعی خودمان

### بد (پرامپت قبلی لینک ۲)
```
SAME STATIC LOCKED-OFF TRIPOD WIDE SHOT ... She steps forward and embraces him,
arms wrapping around his shoulders, he holds the umbrella above them and closes
his arm around her back, rain falling, subtle sway ...
```
ایراد: چهار حرکت در یک جمله (قدم، آغوش، چتر، تکان) + «subtle sway» بدون مقدار.
نتیجه: چتر یک حرکت رفت‌وبرگشتی می‌زند که شبیه عقب‌برگرداندن فریم دیده می‌شود.

### خوب
```
locked-off static tripod wide shot, camera never moves, no zoom, no pan.
She takes one step into him and stops; her arms come up around his shoulders and
stay there. His free arm settles across her back. From this moment neither of them
moves their feet. The only movement is breathing: shoulders rise and fall slowly,
the umbrella tilts back no more than a few centimetres and settles, rain keeps
falling past the lamp. By the last frame they are still, her cheek on his shoulder.
photorealistic, film grain, no text, no subtitle, no camera movement, no warping.
```

تفاوت‌ها: یک حرکت اصلی · چتر با **مقدار** («چند سانتی‌متر») · «بعد از این هیچ‌کدام
قدم برنمی‌دارند» به‌جای منفی‌های پشت‌سرهم · پایان مشخص.

---

## ۴) ریپوها — چه چیزی برای برداشتن دارند

| ریپو | ★ | لایسنس | چه دارد | برای ما |
|---|---|---|---|---|
| `OSideMedia/higgsfield-ai-prompt-skill` | 823 | MIT | ۳۲ زیرمهارت؛ `skills/higgsfield-camera/SKILL.md` با **One-Move Rule**، **Reliable Phrasing Library**، «حرکت ریز = فاصلهٔ دقیق» | ⭐ بیشترین ارزش برای «حرکت طبیعی دوربین» |
| `cclank/lanshu-awesome-ai-video-kit` | 437 | MIT | `methodology/` ۲۱ سند: `05-运镜词典` (واژه‌نامهٔ کامل نما و حرکت)، `04-情绪外化表` (احساس→بدن)، `06-约束词清单`، `03-分镜时序` | ⭐ بهترین برای ترجمهٔ احساس به حرکت |
| `ai-boost/awesome-image-video-prompts` | 3409 | GPL-3.0 | **۹۴۰ پرامپت YAML با خروجی واقعی**؛ ساختار `Main Subject / Location / Visual Style / Camera Style / Timeline / Audio` | ⭐ الگوی ساختاری + بانک مثال |
| `ddia56/wan22_prompt_selector` | 204 | — | انتخاب‌گر پرامپت بر اساس **سند رسمی Wan 2.2** | نزدیک‌ترین به موتور خودمان |
| `Zambav/ComfyUI-Agent-Toolkit` | 20 | MIT | `prompting-guides/wan-2.2-prompting-guide.md`: ترتیب `Subject → setting → action → camera → mood → temporal` | کم‌ستاره ولی دقیقاً Wan |
| `LearnPrompt/awesome-seedance` | 2354 | — | ۸۴۰+ کیس با ریشه‌یابی به منبع اصلی | بانک مرجع |
| `YouMind-OpenLab/awesome-seedance-2-prompts` | 2188 | — | ۲۰۰۰+ پرامپت سینمایی | بانک مرجع |
| `ZeroLu/awesome-seedance` | 2802 | — | مجموعهٔ پرامپت با کیفیت بالا | بانک مرجع |
| `Blizaine/Maestro` | 879 | — | حالت Director که شات‌ها را برنامه‌ریزی می‌کند | ایدهٔ ساختار |

**نتیجهٔ عملی:** سه مورد اول کافی است. `higgsfield-camera` برای جمله‌بندی حرکت
دوربین، `lanshu/04` برای ترجمهٔ احساس به بدن، `ai-boost` برای الگوی ساختاری.

---

## ۵) چک‌لیست قبل از هر تولید

- [ ] دوربین: صریح نوشته شده (ثابت یا یک حرکت با مقدار و زمان)؟
- [ ] فقط یک بیت در این ۴ ثانیه؟
- [ ] هر حرکت ریز مقدار دارد (سانتی‌متر / ثانیه)؟
- [ ] احساس به بدن ترجمه شده، نه صفت؟
- [ ] حالت پایان مشخص است؟
- [ ] یک حرکت محیطی مستقل (باران/بخار) هست؟
- [ ] نگتیو: `no text, no subtitle, no camera movement, no warping, no morphing`؟
