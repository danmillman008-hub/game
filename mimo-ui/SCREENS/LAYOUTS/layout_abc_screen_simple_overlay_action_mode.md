# پروندهٔ لایه — `res/layout/abc_screen_simple_overlay_action_mode.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abc_screen_simple_overlay_action_mode.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abc_screen_simple_overlay_action_mode.xml`](../../SOURCE/res/layout/abc_screen_simple_overlay_action_mode.xml) |
| SHA-256 دیکد | `cde20e0a9ca08859068af659f38d43c7a26cdb03f86fac9b9d29b41b8fb54825` |
| ریشه | `androidx.appcompat.widget.FitWindowsFrameLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 1 |
| ارجاع به منابع | 5 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.appcompat.widget.FitWindowsFrameLayout  #@id/action_bar_root
   ├─ include
   └─ androidx.appcompat.widget.ViewStubCompat  #@id/action_mode_bar_stub
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.appcompat.widget.FitWindowsFrameLayout` | `android:id` | `@id/action_bar_root` |
| 2 | `androidx.appcompat.widget.FitWindowsFrameLayout` | `android:fitsSystemWindows` | `true` |
| 3 | `androidx.appcompat.widget.FitWindowsFrameLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.appcompat.widget.FitWindowsFrameLayout` | `android:layout_height` | `match_parent` |
| 5 | `include` | `layout` | `@layout/abc_screen_content_include` |
| 6 | `androidx.appcompat.widget.ViewStubCompat` | `android:id` | `@id/action_mode_bar_stub` |
| 7 | `androidx.appcompat.widget.ViewStubCompat` | `android:layout` | `@layout/abc_action_mode_bar` |
| 8 | `androidx.appcompat.widget.ViewStubCompat` | `android:inflatedId` | `@id/action_mode_bar` |
| 9 | `androidx.appcompat.widget.ViewStubCompat` | `android:layout_width` | `match_parent` |
| 10 | `androidx.appcompat.widget.ViewStubCompat` | `android:layout_height` | `wrap_content` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/action_bar_root
@id/action_mode_bar_stub
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/abc_screen_content_include
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.appcompat.widget.FitWindowsFrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/action_bar_root" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <include layout="@layout/abc_screen_content_include"/>
  <androidx.appcompat.widget.ViewStubCompat android:id="@id/action_mode_bar_stub" android:layout="@layout/abc_action_mode_bar" android:inflatedId="@id/action_mode_bar" android:layout_width="match_parent" android:layout_height="wrap_content"/>
</androidx.appcompat.widget.FitWindowsFrameLayout>
```
