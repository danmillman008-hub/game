# صفحه — `AllPlansActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.iap.allplans.AllPlansActivity` |
| نوع | `activity` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `@style/AllPlansUpgradeScreen` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 1 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/allplans_activity.xml`](../SOURCE/res/layout/allplans_activity.xml) → [dossier](LAYOUTS/layout_allplans_activity.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/allplans_activity.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_in_app_purchase
   ├─ androidx.viewpager2.widget.ViewPager2  #@id/vp_in_app
   ├─ com.getmimo.ui.common.ViewPagerIndicator  #@id/vpi_in_app
   ├─ com.getmimo.ui.iap.allplans.SubscriptionPodiumButton  #@id/in_app_button_podium_1
   ├─ com.getmimo.ui.iap.allplans.SubscriptionPodiumButton  #@id/in_app_button_podium_2
   ├─ TextView  #@id/tv_in_app_purchase_auto_renew
   ├─ ProgressBar  #@id/pb_in_app
   ├─ ImageView  #@id/iv_in_app_purchase_error
   ├─ TextView  #@id/tv_in_app_purchase_error_title
   ├─ TextView  #@id/tv_in_app_purchase_error_description
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_in_app_purchase_error
   ├─ ImageButton  #@id/btn_in_app_close
   ├─ androidx.constraintlayout.widget.Group  #@id/group_in_app_purchase_error
   └─ androidx.constraintlayout.widget.Group  #@id/group_in_app_purchase_screen
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
all_plans
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
