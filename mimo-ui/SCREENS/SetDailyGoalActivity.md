# صفحه — `SetDailyGoalActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.profile.SetDailyGoalActivity` |
| نوع | `activity` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `@style/MaterialDarkModeTheme.NoAnim` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 4 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/onboarding_set_daily_goal_fragment.xml`](../SOURCE/res/layout/onboarding_set_daily_goal_fragment.xml) → [dossier](LAYOUTS/layout_onboarding_set_daily_goal_fragment.md)
- [`res/layout/set_daily_goal_activity.xml`](../SOURCE/res/layout/set_daily_goal_activity.xml) → [dossier](LAYOUTS/layout_set_daily_goal_activity.md)
- [`res/layout/set_daily_goal_card.xml`](../SOURCE/res/layout/set_daily_goal_card.xml) → [dossier](LAYOUTS/layout_set_daily_goal_card.md)
- [`res/layout/set_daily_goal_card_item.xml`](../SOURCE/res/layout/set_daily_goal_card_item.xml) → [dossier](LAYOUTS/layout_set_daily_goal_card_item.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/onboarding_set_daily_goal_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_set_daily_goal_title
   ├─ TextView  #@id/tv_goal_subtitle
   ├─ com.getmimo.ui.profile.view.SetDailyGoalCard  #@id/layout_daily_goal_card
   └─ androidx.compose.ui.platform.ComposeView  #@id/compose_content
```

### `res/layout/set_daily_goal_activity.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_daily_goal_settings
   │  └─ include  #@id/layout_toolbar
   ├─ com.getmimo.ui.streaks.DailySparksGoalProgressView  #@id/pb_set_daily_goal
   ├─ com.getmimo.ui.profile.view.SetDailyGoalCard  #@id/layout_daily_goal_card
   └─ androidx.compose.ui.platform.ComposeView  #@id/button_daily_goal_continue
```

### `res/layout/set_daily_goal_card.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.getmimo.ui.profile.view.SetDailyGoalCardItem  #@id/daily_goal_level_1
   ├─ View  #@id/line_daily_goal_level_1
   ├─ com.getmimo.ui.profile.view.SetDailyGoalCardItem  #@id/daily_goal_level_2
   ├─ View  #@id/line_daily_goal_level_2
   └─ com.getmimo.ui.profile.view.SetDailyGoalCardItem  #@id/daily_goal_level_3
```

### `res/layout/set_daily_goal_card_item.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.google.android.material.radiobutton.MaterialRadioButton  #@id/radio_daily_goal_level
   ├─ TextView  #@id/tv_daily_goal_level_name
   └─ TextView  #@id/tv_daily_goal_level
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
onboarding_set_daily_goal_title
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
