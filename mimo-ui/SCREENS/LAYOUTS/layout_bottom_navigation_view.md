# پروندهٔ لایه — `res/layout/bottom_navigation_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/bottom_navigation_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/bottom_navigation_view.xml`](../../SOURCE/res/layout/bottom_navigation_view.xml) |
| SHA-256 دیکد | `1944760a32153bfc94a1fad376cabe265356d6444d5550c3ac109a5516493aeb` |
| ریشه | `com.google.android.material.bottomnavigation.BottomNavigationView` |
| تعداد گره | 1 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ com.google.android.material.bottomnavigation.BottomNavigationView  #@id/bottom_navigation_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `com.google.android.material.bottomnavigation.BottomNavigationView` | `android:id` | `@id/bottom_navigation_view` |
| 2 | `com.google.android.material.bottomnavigation.BottomNavigationView` | `android:background` | `@color/background_secondary` |
| 3 | `com.google.android.material.bottomnavigation.BottomNavigationView` | `android:layout_width` | `match_parent` |
| 4 | `com.google.android.material.bottomnavigation.BottomNavigationView` | `android:layout_height` | `wrap_content` |
| 5 | `com.google.android.material.bottomnavigation.BottomNavigationView` | `app:itemIconTint` | `@drawable/bottom_navigation_colors` |
| 6 | `com.google.android.material.bottomnavigation.BottomNavigationView` | `app:itemRippleColor` | `@color/selection_selected` |
| 7 | `com.google.android.material.bottomnavigation.BottomNavigationView` | `app:itemTextAppearanceActive` | `@style/BottomNavigationViewTextStyle` |
| 8 | `com.google.android.material.bottomnavigation.BottomNavigationView` | `app:itemTextAppearanceInactive` | `@style/BottomNavigationViewTextStyle` |
| 9 | `com.google.android.material.bottomnavigation.BottomNavigationView` | `app:itemTextColor` | `@drawable/bottom_navigation_colors` |
| 10 | `com.google.android.material.bottomnavigation.BottomNavigationView` | `app:labelVisibilityMode` | `1` |
| 11 | `com.google.android.material.bottomnavigation.BottomNavigationView` | `app:menu` | `@menu/bottom_navigation_menu` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/selection_selected` | `#FFEDEEF6` / `#FF4A4D85` (night) |
| `@style/BottomNavigationViewTextStyle` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '10.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/bottom_navigation_view
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<com.google.android.material.bottomnavigation.BottomNavigationView xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/bottom_navigation_view" android:background="@color/background_secondary" android:layout_width="match_parent" android:layout_height="wrap_content" app:itemIconTint="@drawable/bottom_navigation_colors" app:itemRippleColor="@color/selection_selected" app:itemTextAppearanceActive="@style/BottomNavigationViewTextStyle" app:itemTextAppearanceInactive="@style/BottomNavigationViewTextStyle" app:itemTextColor="@drawable/bottom_navigation_colors" app:labelVisibilityMode="1" app:menu="@menu/bottom_navigation_menu"/>
```
