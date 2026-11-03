# صفحه — `UpgradeModalActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.upgrade.UpgradeModalActivity` |
| نوع | `activity` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `@style/DialogModalTheme` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 3 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/upgrade_modal_activity.xml`](../SOURCE/res/layout/upgrade_modal_activity.xml) → [dossier](LAYOUTS/layout_upgrade_modal_activity.md)
- [`res/layout/upgrade_modal_bottom_view.xml`](../SOURCE/res/layout/upgrade_modal_bottom_view.xml) → [dossier](LAYOUTS/layout_upgrade_modal_bottom_view.md)
- [`res/layout/upgrade_modal_page.xml`](../SOURCE/res/layout/upgrade_modal_page.xml) → [dossier](LAYOUTS/layout_upgrade_modal_page.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/upgrade_modal_activity.xml`

```text
└─ FrameLayout  #@id/fl_main
   └─ com.google.android.material.card.MaterialCardView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ ImageButton  #@id/iv_upgrade_modal_close
         ├─ androidx.viewpager2.widget.ViewPager2  #@id/vp_in_app
         ├─ com.getmimo.ui.common.ViewPagerIndicator  #@id/vpi_in_app
         └─ com.getmimo.ui.upgrade.UpgradeModalBottomView  #@id/upgrade_modal_bottom_view
```

### `res/layout/upgrade_modal_bottom_view.xml`

```text
└─ merge
   ├─ View  #@id/view_bottom_part
   ├─ TextView  #@id/tv_countdown_timer
   ├─ TextView  #@id/tv_yearly_price
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_upgrade_modal_upgrade
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_upgrade_modal_other_plans
```

### `res/layout/upgrade_modal_page.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ FrameLayout  #@id/image_container_upgrade_modal
   │  ├─ ImageView  #@id/iv_upgrade_modal
   │  └─ app.rive.runtime.kotlin.RiveAnimationView  #@id/rive_upgrade_modal_animation
   ├─ TextView  #@id/tv_upgrade_modal_title
   └─ TextView  #@id/tv_upgrade_modal_description
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
upgrade_modal_ad_description
upgrade_modal_ad_title
upgrade_modal_cancel_anytime
upgrade_modal_certificate_ltc_description
upgrade_modal_certificate_other_description
upgrade_modal_certificate_title
upgrade_modal_codeplayground_description
upgrade_modal_codeplayground_title
upgrade_modal_local_theme_experiment_description
upgrade_modal_local_theme_experiment_title
upgrade_modal_other_plans
upgrade_modal_streak_freeze_description
upgrade_modal_unlimited_ai_tutor_description
upgrade_modal_unlimited_ai_tutor_title
upgrade_modal_unlimited_codeplayground_description
upgrade_modal_unlimited_codeplayground_title
upgrade_modal_upgrade_for_no_sales
upgrade_modal_upgrade_for_no_sales_with_free_trial
upgrade_modal_upgrade_for_sale_part1
upgrade_modal_upgrade_for_sale_part1_with_free_trial
upgrade_modal_upgrade_for_sale_part2
```

## ۴. رنگ‌های مرتبط (فهرست کامل)

(none)

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

```text
view_pager_dots_upgrade_modal_margin
```

## ۶. استایل‌های مرتبط (فهرست کامل)

(none)

## ۷. شواهد حالت‌ها (رشته‌های منبع)

```text
upgrade_modal_ad_description
upgrade_modal_ad_title
upgrade_modal_cancel_anytime
upgrade_modal_certificate_ltc_description
upgrade_modal_certificate_other_description
upgrade_modal_certificate_title
upgrade_modal_codeplayground_description
upgrade_modal_codeplayground_title
upgrade_modal_local_theme_experiment_description
upgrade_modal_local_theme_experiment_title
upgrade_modal_other_plans
upgrade_modal_streak_freeze_description
upgrade_modal_unlimited_ai_tutor_description
upgrade_modal_unlimited_ai_tutor_title
upgrade_modal_unlimited_codeplayground_description
upgrade_modal_unlimited_codeplayground_title
upgrade_modal_upgrade_for_no_sales
upgrade_modal_upgrade_for_no_sales_with_free_trial
upgrade_modal_upgrade_for_sale_part1
upgrade_modal_upgrade_for_sale_part1_with_free_trial
upgrade_modal_upgrade_for_sale_part2
```

## ۸. ناوبری / deep link

(هیچ intent-filter/data برای این سطح اعلان نشده)
