# صفحه — `SetExperienceFragment`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.onboarding.step2.SetExperienceFragment` |
| نوع | `fragment` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view binding` |
| تعداد لایه‌های متصل | 1 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/onboarding_step_3_set_experience_fragment.xml`](../SOURCE/res/layout/onboarding_step_3_set_experience_fragment.xml) → [dossier](LAYOUTS/layout_onboarding_step_3_set_experience_fragment.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/onboarding_step_3_set_experience_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_set_experience_slider_title
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/iv_set_experience_animation
   ├─ LinearLayout  #@id/layout_set_experience_slider_and_text
   │  ├─ com.getmimo.ui.common.SeekBarWithIntervals  #@id/seekbar_set_experience
   │  └─ TextView  #@id/tv_set_experience_slider_description
   └─ androidx.compose.ui.platform.ComposeView  #@id/compose_content
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
onboarding_set_experience_little_description
onboarding_set_experience_little_title
onboarding_set_experience_lot_description
onboarding_set_experience_lot_title
onboarding_set_experience_none_description
onboarding_set_experience_none_title
onboarding_set_experience_title
```

## ۴. رنگ‌های مرتبط (فهرست کامل)

(none)

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

(none)

## ۶. استایل‌های مرتبط (فهرست کامل)

(none)

## ۷. شواهد حالت‌ها (رشته‌های منبع)

(none)

## ۸. ناوبری / deep link

(هیچ intent-filter/data برای این سطح اعلان نشده)
