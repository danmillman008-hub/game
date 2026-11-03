# پروندهٔ لایه — `res/layout/abc_screen_content_include.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abc_screen_content_include.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abc_screen_content_include.xml`](../../SOURCE/res/layout/abc_screen_content_include.xml) |
| SHA-256 دیکد | `ed690a3a034daa29e86d95bdfcf38dcfdf7473fa3939972d54ccb65980a8f74c` |
| ریشه | `merge` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 2 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   └─ androidx.appcompat.widget.ContentFrameLayout  #@id/action_bar_activity_content
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.appcompat.widget.ContentFrameLayout` | `android:id` | `@id/action_bar_activity_content` |
| 2 | `androidx.appcompat.widget.ContentFrameLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.appcompat.widget.ContentFrameLayout` | `android:layout_height` | `match_parent` |
| 4 | `androidx.appcompat.widget.ContentFrameLayout` | `android:foreground` | `?0x01010059` |
| 5 | `androidx.appcompat.widget.ContentFrameLayout` | `android:foregroundGravity` | `0x00000037` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/action_bar_activity_content
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout-v26/abc_screen_toolbar.xml
res/layout/abc_dialog_title_material.xml
res/layout/abc_screen_simple.xml
res/layout/abc_screen_simple_overlay_action_mode.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:android="http://schemas.android.com/apk/res/android">
  <androidx.appcompat.widget.ContentFrameLayout android:id="@id/action_bar_activity_content" android:layout_width="match_parent" android:layout_height="match_parent" android:foreground="?0x01010059" android:foregroundGravity="0x00000037"/>
</merge>
```
