# صفحه — `IntroSlidesActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.onboarding.intro.IntroSlidesActivity` |
| نوع | `activity` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `@style/MaterialDarkModeTheme.NoAnim` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 2 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/intro_slides_activity.xml`](../SOURCE/res/layout/intro_slides_activity.xml) → [dossier](LAYOUTS/layout_intro_slides_activity.md)
- [`res/layout/onboarding_intro_slides_page.xml`](../SOURCE/res/layout/onboarding_intro_slides_page.xml) → [dossier](LAYOUTS/layout_onboarding_intro_slides_page.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/intro_slides_activity.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ androidx.viewpager.widget.ViewPager  #@id/vp_intro_slides
   ├─ com.getmimo.ui.common.ViewPagerIndicator  #@id/vp_indicator
   └─ androidx.compose.ui.platform.ComposeView  #@id/compose_content
```

### `res/layout/onboarding_intro_slides_page.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/iv_rive_animation
   └─ LinearLayout  #@id/layout_slide_text_views
      ├─ TextView  #@id/tv_onboarding_page_title
      └─ TextView  #@id/tv_onboarding_page_description
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
onboarding_intro_slides_already_have_an_account
```

## ۴. رنگ‌های مرتبط (فهرست کامل)

(none)

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

```text
onboarding_container_intro_slides_dots_margin_vertical
```

## ۶. استایل‌های مرتبط (فهرست کامل)

(none)

## ۷. شواهد حالت‌ها (رشته‌های منبع)

(none)

## ۸. ناوبری / deep link

(هیچ intent-filter/data برای این سطح اعلان نشده)
