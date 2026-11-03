# پروندهٔ لایه — `res/layout/ime_secondary_split_test_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/ime_secondary_split_test_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/ime_secondary_split_test_activity.xml`](../../SOURCE/res/layout/ime_secondary_split_test_activity.xml) |
| SHA-256 دیکد | `ac25982a5026f180127f8c00f263f534fdc22b112c350839eb23383a34f66d51` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 2 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ EditText  #@id/edit_text_id
   └─ Button  #@id/hide_ime_id
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 3 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 4 | `EditText` | `android:gravity` | `0x00000011` |
| 5 | `EditText` | `android:id` | `@id/edit_text_id` |
| 6 | `EditText` | `android:layout_width` | `wrap_content` |
| 7 | `EditText` | `android:layout_height` | `wrap_content` |
| 8 | `EditText` | `android:minHeight` | `200.000000px` |
| 9 | `EditText` | `android:text` | `EditText` |
| 10 | `EditText` | `android:inputType` | `0x00000001` |
| 11 | `Button` | `android:id` | `@id/hide_ime_id` |
| 12 | `Button` | `android:layout_width` | `match_parent` |
| 13 | `Button` | `android:layout_height` | `wrap_content` |
| 14 | `Button` | `android:text` | `Hide Ime` |
| 15 | `Button` | `android:textAllCaps` | `false` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/edit_text_id
@id/hide_ime_id
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="match_parent">
  <EditText android:gravity="0x00000011" android:id="@id/edit_text_id" android:layout_width="wrap_content" android:layout_height="wrap_content" android:minHeight="200.000000px" android:text="EditText" android:inputType="0x00000001"/>
  <Button android:id="@id/hide_ime_id" android:layout_width="match_parent" android:layout_height="wrap_content" android:text="Hide Ime" android:textAllCaps="false"/>
</LinearLayout>
```
