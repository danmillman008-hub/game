# صفحه — `DevMenuRemoteConfigActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.developermenu.remoteconfig.DevMenuRemoteConfigActivity` |
| نوع | `activity` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `@style/MaterialDarkModeTheme` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 1 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/developer_menu_remote_config_activity.xml`](../SOURCE/res/layout/developer_menu_remote_config_activity.xml) → [dossier](LAYOUTS/layout_developer_menu_remote_config_activity.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/developer_menu_remote_config_activity.xml`

```text
└─ androidx.coordinatorlayout.widget.CoordinatorLayout
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_developermenu
   │  └─ include  #@id/layout_toolbar
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ EditText  #@id/et_remote_config_id
      ├─ EditText  #@id/et_remote_config_value
      ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_remote_config_add
      └─ androidx.recyclerview.widget.RecyclerView  #@id/rv_remote_config
```

## ۳. رشته‌های مرتبط (فهرست کامل)

(none)

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
