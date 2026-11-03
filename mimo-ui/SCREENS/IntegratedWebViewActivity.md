# صفحه — `IntegratedWebViewActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.integratedwebview.IntegratedWebViewActivity` |
| نوع | `activity` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 1 |
| ComposeView | خیر |
| WebView | بله |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/integrated_webview_activity.xml`](../SOURCE/res/layout/integrated_webview_activity.xml) → [dossier](LAYOUTS/layout_integrated_webview_activity.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/integrated_webview_activity.xml`

```text
└─ LinearLayout
   ├─ com.google.android.material.appbar.AppBarLayout
   │  └─ include  #@id/layout_toolbar
   └─ FrameLayout
      ├─ com.getmimo.ui.components.common.MimoWebView  #@id/integrated_webview
      ├─ com.getmimo.ui.components.common.OfflineView  #@id/offline_view_integrated_webview
      └─ com.getmimo.ui.components.common.LoadingView  #@id/loading_view_integrated_webview
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
