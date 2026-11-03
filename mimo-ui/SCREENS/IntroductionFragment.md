# صفحه — `IntroductionFragment`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.onboarding.step1.IntroductionFragment` |
| نوع | `fragment` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view binding` |
| تعداد لایه‌های متصل | 4 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/feature_introduction_modal_fragment.xml`](../SOURCE/res/layout/feature_introduction_modal_fragment.xml) → [dossier](LAYOUTS/layout_feature_introduction_modal_fragment.md)
- [`res/layout/leaderboard_introduction_fragment.xml`](../SOURCE/res/layout/leaderboard_introduction_fragment.xml) → [dossier](LAYOUTS/layout_leaderboard_introduction_fragment.md)
- [`res/layout/onboarding_step_1_introduction_fragment.xml`](../SOURCE/res/layout/onboarding_step_1_introduction_fragment.xml) → [dossier](LAYOUTS/layout_onboarding_step_1_introduction_fragment.md)
- [`res/layout/quiz_introduction_fragment.xml`](../SOURCE/res/layout/quiz_introduction_fragment.xml) → [dossier](LAYOUTS/layout_quiz_introduction_fragment.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/feature_introduction_modal_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_feature_introduction_modal
   ├─ include  #@id/base_modal_card
   └─ com.getmimo.ui.common.CutoutBackgroundView  #@id/cutout_view_feature_intro
```

### `res/layout/leaderboard_introduction_fragment.xml`

```text
└─ FrameLayout
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ ImageView  #@id/iv_leaderboard_intro_image
      ├─ TextView  #@id/iv_leaderboard_intro_title
      ├─ TextView  #@id/iv_leaderboard_intro_subtitle
      ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/cl_leaderboard_intro_details_container
      │  ├─ ImageView  #@id/iv_leaderboard_into_league_image
      │  ├─ TextView  #@id/tv_leaderboard_into_league_title
      │  ├─ TextView  #@id/tv_leaderboard_into_league_subtitle
      │  ├─ ImageView  #@id/iv_leaderboard_into_time_image
      │  ├─ TextView  #@id/tv_leaderboard_into_time_title
      │  └─ TextView
      └─ androidx.compose.ui.platform.ComposeView  #@id/mb_leaderboard_into_got_it
```

### `res/layout/onboarding_step_1_introduction_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_set_experience_introduction_title
   ├─ TextView  #@id/tv_set_experience_introduction_description
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/lv_set_experience_introduction
   └─ androidx.compose.ui.platform.ComposeView  #@id/compose_content
```

### `res/layout/quiz_introduction_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ ImageView  #@id/iv_quiz_introduction
   ├─ TextView  #@id/tv_quiz_introduction_title
   ├─ TextView  #@id/tv_quiz_introduction_description
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_start_quiz
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_not_now
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
input_console_introduction_description
input_console_introduction_title
quiz_introduction_description
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
