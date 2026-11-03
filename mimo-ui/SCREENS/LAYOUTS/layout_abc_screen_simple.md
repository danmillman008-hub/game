# پروندهٔ لایه — `res/layout/abc_screen_simple.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abc_screen_simple.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abc_screen_simple.xml`](../../SOURCE/res/layout/abc_screen_simple.xml) |
| SHA-256 دیکد | `56d1f5107fb8bf3e13e388e2947716370a849db3d65eda377b2357b08d7f44b5` |
| ریشه | `androidx.appcompat.widget.FitWindowsLinearLayout` |
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
└─ androidx.appcompat.widget.FitWindowsLinearLayout  #@id/action_bar_root
   ├─ androidx.appcompat.widget.ViewStubCompat  #@id/action_mode_bar_stub
   └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.appcompat.widget.FitWindowsLinearLayout` | `android:orientation` | `vertical` |
| 2 | `androidx.appcompat.widget.FitWindowsLinearLayout` | `android:id` | `@id/action_bar_root` |
| 3 | `androidx.appcompat.widget.FitWindowsLinearLayout` | `android:fitsSystemWindows` | `true` |
| 4 | `androidx.appcompat.widget.FitWindowsLinearLayout` | `android:layout_width` | `match_parent` |
| 5 | `androidx.appcompat.widget.FitWindowsLinearLayout` | `android:layout_height` | `match_parent` |
| 6 | `androidx.appcompat.widget.ViewStubCompat` | `android:id` | `@id/action_mode_bar_stub` |
| 7 | `androidx.appcompat.widget.ViewStubCompat` | `android:layout` | `@layout/abc_action_mode_bar` |
| 8 | `androidx.appcompat.widget.ViewStubCompat` | `android:inflatedId` | `@id/action_mode_bar` |
| 9 | `androidx.appcompat.widget.ViewStubCompat` | `android:layout_width` | `match_parent` |
| 10 | `androidx.appcompat.widget.ViewStubCompat` | `android:layout_height` | `wrap_content` |
| 11 | `include` | `layout` | `@layout/abc_screen_content_include` |

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
<androidx.appcompat.widget.FitWindowsLinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:id="@id/action_bar_root" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <androidx.appcompat.widget.ViewStubCompat android:id="@id/action_mode_bar_stub" android:layout="@layout/abc_action_mode_bar" android:inflatedId="@id/action_mode_bar" android:layout_width="match_parent" android:layout_height="wrap_content"/>
  <include layout="@layout/abc_screen_content_include"/>
</androidx.appcompat.widget.FitWindowsLinearLayout>
```
