# صفحه — `CertificateUpgradeActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.certificateupgrade.CertificateUpgradeActivity` |
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

- [`res/layout/certificate_upgrade_activity.xml`](../SOURCE/res/layout/certificate_upgrade_activity.xml) → [dossier](LAYOUTS/layout_certificate_upgrade_activity.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/certificate_upgrade_activity.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ LinearLayout  #@id/ll_certificate_upgrade
   │  ├─ ImageView  #@id/iv_badge
   │  ├─ TextView
   │  └─ TextView  #@id/tv_user_name
   ├─ TextView  #@id/tv_title
   ├─ LinearLayout  #@id/ll_advantages_upgrade
   │  ├─ TextView
   │  ├─ TextView
   │  └─ TextView
   ├─ TextView  #@id/tv_secured_by
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_upgrade
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_no_thanks
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
