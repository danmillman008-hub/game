# پروندهٔ لایه — `res/layout/md_dialog_stub_scrollview.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/md_dialog_stub_scrollview.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/md_dialog_stub_scrollview.xml`](../../SOURCE/res/layout/md_dialog_stub_scrollview.xml) |
| SHA-256 دیکد | `c4bd89089961b7ef469cd3546866af20a97716e35344a921e1bfbcb6e1650dc9` |
| ریشه | `com.afollestad.materialdialogs.internal.main.DialogScrollView` |
| تعداد گره | 2 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ com.afollestad.materialdialogs.internal.main.DialogScrollView  #@id/md_scrollview_content
   └─ LinearLayout  #@id/md_scrollview_frame_content
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `com.afollestad.materialdialogs.internal.main.DialogScrollView` | `android:id` | `@id/md_scrollview_content` |
| 2 | `com.afollestad.materialdialogs.internal.main.DialogScrollView` | `android:clipToPadding` | `false` |
| 3 | `com.afollestad.materialdialogs.internal.main.DialogScrollView` | `android:layout_width` | `match_parent` |
| 4 | `com.afollestad.materialdialogs.internal.main.DialogScrollView` | `android:layout_height` | `wrap_content` |
| 5 | `LinearLayout` | `android:id` | `@id/md_scrollview_frame_content` |
| 6 | `LinearLayout` | `style` | `@style/MD_Dialog_ScrollView_FrameContent` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/MD_Dialog_ScrollView_FrameContent` | `[{'attr': 'android:gravity', 'attr_id': '0x010100AF', 'value': '0x00000011', 'value_type': 'int_hex'}, {'attr': 'android:orientation', 'attr_id': '0x010100C4', 'value': '1', 'value_type': 'int_dec'}, {'attr': 'android:layout_width', 'attr_id': '0x010100F4', 'value': '-1', 'value_type': 'int_dec'}, {'attr': 'android:layout_height', 'attr_id': '0x010100F5', 'value': '-2', 'value_type': 'int_dec'}]` |

## ۴. شناسه‌های `@id`

```text
@id/md_scrollview_content
@id/md_scrollview_frame_content
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
<com.afollestad.materialdialogs.internal.main.DialogScrollView xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/md_scrollview_content" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="wrap_content">
  <LinearLayout android:id="@id/md_scrollview_frame_content" style="@style/MD_Dialog_ScrollView_FrameContent"/>
</com.afollestad.materialdialogs.internal.main.DialogScrollView>
```
