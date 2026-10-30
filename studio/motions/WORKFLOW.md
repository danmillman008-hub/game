# گردش کار بهینه‌شده — از صحنه تا کلیپ، با عدد

> قبل: ۱۵ شات، 하나씩، ~۴۵ دقیقه، و ۸ شات آخر هویت را شکستند.
> بعد: لنگر + موازی، همان ۱۵ شات ~۱۲–۱۵ دقیقه، و زنجیره از ۲ حلقه بیشتر نمی‌شود.

## خط تولید

```
۱. لنگرها را بساز (آرت از کانواس)        →  art_k2, art_knight, art_plain2
۲. صحنه را بنویس (لنگر + یک جمله دوربین + یک جمله حرکت)
۳. shotplan.py  → جاب‌فایل + ممیزی پرامپت + عمق زنجیره + تخمین زمان
۴. mivi_shot.py --parallel 4  → کلیپ‌ها و gen_report.json
۵. filmkit assemble → فیلم
```

### ۲. فایل صحنه

`studio/motions/scenes/gate.json`:

```json
{
  "name": "gate",
  "anchors": {"gate_wide": "…/art_k2_last.png", "her_face": "…/art_knight_last.png"},
  "shots": [
    {"id": "g01", "anchor": "gate_wide", "camera": "The camera pushes in slowly toward the gate.",
     "action": "Rain falls through the lantern light."},
    {"id": "g02", "chain_from": "g01", "camera": "The camera keeps moving toward the arch.",
     "action": "She lowers her spear until it touches the wet stones."}
  ]
}
```

قاعده‌ها:
- **`anchor`** = استیل تأییدشده. هر شات مستقل ⇒ موازی‌سازی ممکن، هویت پایدار.
- **`chain_from`** فقط وقتی دوربین باید **پیوسته** حرکت کند. حداکثر ۲ حلقه.
- جملهٔ دوربین **سوژه را نام ببرد**: «the man in the red coat»، نه «him».
- کلوزآپ از **لنگر کلوزآپ** شروع شود، نه از نمای باز.

### ۳. پلنر

```bash
python3 studio/shotplan.py plan studio/motions/scenes/gate.json \
        --out films/short16/gen_jobs_gate.json --parallel 4
```

خروجی روی صحنهٔ نمونه:

```
scene gate: 5 shots, 3 anchored, 2 chained, longest chain 1
  waves: 0:3 | 1:2
  est. wall clock ~6 min at parallel=4 (serial ~15 min)
```

اگر پرامپتی ناقض قرارداد Wan باشد یا زنجیره از ۲ بگذرد، **کد ۱** برمی‌گرداند —
یعنی می‌شود در CI گذاشت.

### ۴. اجرا

```bash
python3 studio/mivi_shot.py films/short16/gen_jobs_gate.json \
        --out films/short16/clips_gen --parallel 4 --skip-existing
```

| فلگ | کار |
|---|---|
| `--parallel N` | N تسک هم‌زمان؛ poll مشترک |
| `--dry-run` | گراف، موج‌ها، عمق زنجیره، تخمین زمان — بدون خرج |
| `--skip-existing` | کلیپ موجود دوباره ساخته نشود |
| `--timeout` | سقف هر تلاش |

## عددها

| | قبل | بعد |
|---|---|---|
| ۱۵ شات، سریالی | ~۴۵ دقیقه | — |
| ۱۵ شات، `parallel=4` | — | **~۱۲–۱۵ دقیقه** |
| بچ ۸ شاتی (dry-run) | ۲۴ دقیقه | **۹ دقیقه** |
| عمق زنجیره | ۱۵ | **≤۲** |
| پرامپت ناقض Wan | ۸ از ۸ | **۰** |

## چه چیزی خودکار جلوی خرابی را می‌گیرد

1. `shotplan.py` — پرامپت ناقض و زنجیرهٔ عمیق را **قبل از تولید** رد می‌کند.
2. `mivi_shot.py` — `motionbank.lint` حالا همان قرارداد Wan را می‌سنجد (قبلاً
   پرامپت درست را ۶۴/۱۰۰ می‌داد چون «بلوک منفی» می‌خواست که API ما ندارد).
3. `--dry-run` — تخمین زمان و شکل گراف قبل از هر خرج.

## قدم بعدی (تصمیم لازم)

- **تست FLF:** `t_video` حالا فیلد `images` (آرایه) را می‌فرستد و `mivi_shot` فیلد
  `end_still` را به جاب می‌دهد. یک شات با دو عکس (اول و آخر) نشان می‌دهد آیا API
  فریم آخر را می‌فهمد. اگر بله، هویت تقریباً حل می‌شود.
- **فیس‌سوآپ پس از تولید** — اگر FLF جواب نداد، همان کاری که جامعه می‌کند.
- **GPU خودمان** (`LightX2V` ۴ استپ + `SageAttention`) فقط اگر بخواهیم ۱۰ دقیقه
  فیلم بسازیم؛ با API فعلی هر دقیقه فیلم ~۱۲ دقیقه راند می‌برد.
