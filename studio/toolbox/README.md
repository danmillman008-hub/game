# toolbox — ابزار تخصصی که کم داشتیم

> سؤال: «کیفیت خروجی خوب نیست، جعبه‌ابزار مناسب لازم است». جواب: گردن‌گیر اصلی
> **ورودی** بود، نه پرامپت. شیت‌ها ۳۰۰×۴۹۹ بودند و از مدل می‌خواستیم از ۳۰۰ پیکسل فیلم بسازد.

## آنچه جست‌وجو شد و آنچه انتخاب شد

`studio/knowledge/BANK.md` (گپ `j-frame`) — ۷ ریپوی تازه، همه با ستاره/لایسنس از API:

| ریپو | ★ | لایسنس | چرا |
|---|---|---|---|
| **`xinntao/Real-ESRGAN`** | 37,280 | BSD-3 | مدل `x4plus_anime_6B` مخصوص آرت سل |
| **`TianZerL/pyanime4k`** | 122 | MIT | Anime4K روی CPU، **بدون GPU** |
| `TianZerL/Anime4KCPP` | 2,044 | GPL | هستهٔ C++ همان |
| `bloc97/Anime4K` | 21,581 | MIT | شیدرهای GLSL، مرجع الگوریتم |
| `Doubiiu/ToonCrafter` | 6,044 | Apache | درون‌یابی انیمه — GPU لازم، مرحلهٔ بعد |
| `Mukosame/Anime2Sketch` | 2,138 | MIT | استخراج لاین‌آرت از شیت |
| `tencent-ailab/IP-Adapter` | 6,705 | Apache | قفل هویت کاراکتر |

## اندازه‌گیری — روی رانر، CPU، بدون GPU

هر عدد روی **یک اندازهٔ خروجی** (۱۰۰۰px) گرفته شده تا مقایسه معتبر باشد.
خطای اول من این بود که تصویر بزرگ‌تر را «تارتر» گزارش کردم؛ gradient به ازای
هر پیکسل با بزرگ‌شدن کم می‌شود، پس باید بعد از نرمال‌سازی اندازه سنجید.

| موتور | c1 (شیت) | c6 (شیت) | زمان | حکم |
|---|---|---|---|---|
| **bicubic (کنترل)** | ۱۱.۳۲ | ۱۶.۳۱ | ۰s | مبنا |
| **Anime4K (pyanime4k)** | **۲۴.۶۳** | **۳۱.۸۹** | **۱s** | ۲.۲× و ۲.۰× کنترل |
| **Real-ESRGAN anime-6B** | **۳۱.۵۸** | **۳۷.۴۱** | ۱۱s | ۲.۸۰× و ۲.۳۰× کنترل |

میانگین شش شیت: Anime4K **۱.۷۹×**، Real-ESRGAN **۲.۰۶×** نسبت به bicubic.
یعنی این ابزار «تزئینی» نیست — لاین‌آرت را واقعاً بازمی‌سازد.

## نصب (روی رانر، نه سندباکس)

```bash
pip install pyanime4k                      # Anime4K، CPU، ۱ ثانیه
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install basicsr==1.4.2 realesrgan      # Real-ESRGAN
# basicsr به ماژولی import می‌کند که torchvision ≥0.17 حذف کرده:
python3 -c "import torchvision,os;open(os.path.join(os.path.dirname(torchvision.__file__),'transforms','functional_tensor.py'),'w').write('from torchvision.transforms.functional import *\n')"
```

⚠️ دو دام واقعی: (۱) `torch` و `torchvision` باید از **یک ایندکس** نصب شوند وگرنه
`operator torchvision::nms does not exist`؛ (۲) شیم `functional_tensor` باید **فایل**
باشد نه `sys.modules`، چون در پروسهٔ بعدی وجود ندارد.

## استفاده

```bash
python3 studio/toolbox/upscale.py compare --src films/anime_ten/refs/c1.png   # A/B با کنترل
python3 studio/toolbox/upscale.py refs --engine realesrgan --scale 4          # ۶ شیت
python3 studio/toolbox/upscale.py clean                                       # پاک‌سازی آرتیفکت
```

## A/B واقعی — شیت خام در برابر شیت ۴×

دو کلیپ از یک پرامپت، یکی از شیت ۳۰۰px و یکی از شیت ۴× پاک‌شده:
`films/anime_ten/qc/upscale_ab.jpg`

| | شیت خام | شیت ۴× |
|---|---|---|
| خط دور کاراکتر | ضخیم، لرزان | نازک و یکدست |
| جزئیات لباس | تکه‌تکه | بندها و سگک‌ها جدا |
| کلوزآپ | محو | چشم و ابرو تمیز |
| **اما** | | یک **نوار سفید** روی افق ظاهر شد |

آن نوار سفید، همان آرتیفکت شیت است که مدل دوباره کشیده. پاک‌سازی مستطیلی من
کافی نبود — هنوز یک ردیف روشن در شیت باقی است. **درس: تا وقتی کی‌فریم تمیز نشود،
هیچ آپ‌اسکیلری کیفیت نهایی را درست نمی‌کند.**

## چه چیزی هنوز کم است

1. **آرت واقعی بزرگ** — آپ‌اسکیل، جزئیاتِ نبوده را نمی‌سازد؛ فقط لبه‌ها را تمیز می‌کند.
   برای کیفیت استودیویی، شیت باید از اول ۲K+ باشد یا با تصویرساز بازسازی شود.
2. **تصویرساز** در سندباکس ۴۰۳ می‌دهد و endpoint عکس Mivi روی رانر `token` می‌خواهد
   که در کد اپ نیست. این تنها درِ بستهٔ باقی‌مانده است.
3. **ToonCrafter** برای درون‌یابی بین دو کی‌فریم — GPU لازم دارد، مرحلهٔ بعد.
