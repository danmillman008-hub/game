# پروندهٔ لایه — `res/layout/integrated_webview_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/integrated_webview_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/integrated_webview_activity.xml`](../../SOURCE/res/layout/integrated_webview_activity.xml) |
| SHA-256 دیکد | `163545c7ee35d7a6384a7ab60e20f28bc3a8dad9f057f6b6c8bb7798f6625c19` |
| ریشه | `LinearLayout` |
| تعداد گره | 7 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 7 |
| ویوهای سفارشی `com.getmimo` | 3 |
| `ComposeView` | 0 |
| `WebView` | 1 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 9 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ com.google.android.material.appbar.AppBarLayout
   │  └─ include  #@id/layout_toolbar
   └─ FrameLayout
      ├─ com.getmimo.ui.components.common.MimoWebView  #@id/integrated_webview
      ├─ com.getmimo.ui.components.common.OfflineView  #@id/offline_view_integrated_webview
      └─ com.getmimo.ui.components.common.LoadingView  #@id/loading_view_integrated_webview
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 3 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 4 | `com.google.android.material.appbar.AppBarLayout` | `android:background` | `@color/navbar_background` |
| 5 | `com.google.android.material.appbar.AppBarLayout` | `android:fitsSystemWindows` | `true` |
| 6 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_width` | `match_parent` |
| 7 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_height` | `wrap_content` |
| 8 | `com.google.android.material.appbar.AppBarLayout` | `app:elevation` | `0.000000dip` |
| 9 | `include` | `android:id` | `@id/layout_toolbar` |
| 10 | `include` | `android:layout_width` | `match_parent` |
| 11 | `include` | `android:layout_height` | `@dimen/toolbar_height` |
| 12 | `include` | `layout` | `@layout/toolbar` |
| 13 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 14 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 15 | `com.getmimo.ui.components.common.MimoWebView` | `android:id` | `@id/integrated_webview` |
| 16 | `com.getmimo.ui.components.common.MimoWebView` | `android:layout_width` | `match_parent` |
| 17 | `com.getmimo.ui.components.common.MimoWebView` | `android:layout_height` | `match_parent` |
| 18 | `com.getmimo.ui.components.common.OfflineView` | `android:id` | `@id/offline_view_integrated_webview` |
| 19 | `com.getmimo.ui.components.common.OfflineView` | `android:background` | `@color/background_primary` |
| 20 | `com.getmimo.ui.components.common.OfflineView` | `android:visibility` | `gone` |
| 21 | `com.getmimo.ui.components.common.OfflineView` | `android:layout_width` | `match_parent` |
| 22 | `com.getmimo.ui.components.common.OfflineView` | `android:layout_height` | `match_parent` |
| 23 | `com.getmimo.ui.components.common.OfflineView` | `app:offline_description` | `@string/integrated_webview_offline_view` |
| 24 | `com.getmimo.ui.components.common.LoadingView` | `android:layout_gravity` | `0x00000011` |
| 25 | `com.getmimo.ui.components.common.LoadingView` | `android:id` | `@id/loading_view_integrated_webview` |
| 26 | `com.getmimo.ui.components.common.LoadingView` | `android:background` | `@color/background_primary` |
| 27 | `com.getmimo.ui.components.common.LoadingView` | `android:visibility` | `gone` |
| 28 | `com.getmimo.ui.components.common.LoadingView` | `android:layout_width` | `match_parent` |
| 29 | `com.getmimo.ui.components.common.LoadingView` | `android:layout_height` | `match_parent` |
| 30 | `com.getmimo.ui.components.common.LoadingView` | `android:elevation` | `2.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/navbar_background` | `#FFFFFFFF` / `#FF333661` (night) |
| `@dimen/toolbar_height` | `56.000000dip` |
| `@string/integrated_webview_offline_view` | `Connect to the internet to continue using Mimo` / `Verbinde dich mit dem Internet, um Mimo weiterhin zu nutzen` (de) / `Conéctate a internet para continuar usando Mimo` (es) / `Connecte-toi à Internet pour continuer à utiliser Mimo` (fr) / `Hubungkan ke internet untuk lanjut pakai Mimo` (in) / `Connettiti a internet per continuare a usare Mimo` (it) / `Połącz się z internetem, aby dalej korzystać z Mimo` (pl) / `Conecte-se à internet para continuar usando o Mimo` (pt-rBR) / `Подключись к Интернету, чтобы продолжить использовать Mimo` (ru) / `Mimo'yu kullanmaya devam etmek için internete bağlan` (tr) |

## ۴. شناسه‌های `@id`

```text
@id/integrated_webview
@id/layout_toolbar
@id/loading_view_integrated_webview
@id/offline_view_integrated_webview
```

## ۵. ارجاع به لایه‌های دیگر

```text
@dimen/toolbar_height
@layout/toolbar
match_parent
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.integratedwebview.IntegratedWebViewActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.google.android.material.appbar.AppBarLayout android:background="@color/navbar_background" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="wrap_content" app:elevation="0.000000dip">
    <include android:id="@id/layout_toolbar" android:layout_width="match_parent" android:layout_height="@dimen/toolbar_height" layout="@layout/toolbar"/>
  </com.google.android.material.appbar.AppBarLayout>
  <FrameLayout android:layout_width="match_parent" android:layout_height="match_parent">
    <com.getmimo.ui.components.common.MimoWebView android:id="@id/integrated_webview" android:layout_width="match_parent" android:layout_height="match_parent"/>
    <com.getmimo.ui.components.common.OfflineView android:id="@id/offline_view_integrated_webview" android:background="@color/background_primary" android:visibility="gone" android:layout_width="match_parent" android:layout_height="match_parent" app:offline_description="@string/integrated_webview_offline_view"/>
    <com.getmimo.ui.components.common.LoadingView android:layout_gravity="0x00000011" android:id="@id/loading_view_integrated_webview" android:background="@color/background_primary" android:visibility="gone" android:layout_width="match_parent" android:layout_height="match_parent" android:elevation="2.000000dip"/>
  </FrameLayout>
</LinearLayout>
```
