# پروندهٔ لایه — `res/layout/design_layout_snackbar.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/design_layout_snackbar.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/design_layout_snackbar.xml`](../../SOURCE/res/layout/design_layout_snackbar.xml) |
| SHA-256 دیکد | `d3662a32cc4bbb036f8d1950eb2d66c864bd829ef2dfeeca10b36ff48ddc2209` |
| ریشه | `view` |
| تعداد گره | 1 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 2 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `view` | `android:theme` | `@style/ThemeOverlay.AppCompat.Dark` |
| 2 | `view` | `android:layout_gravity` | `0x00000050` |
| 3 | `view` | `android:layout_width` | `match_parent` |
| 4 | `view` | `android:layout_height` | `wrap_content` |
| 5 | `view` | `class` | `com.google.android.material.snackbar.Snackbar$SnackbarLayout` |
| 6 | `view` | `style` | `@style/Widget.Design.Snackbar` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/ThemeOverlay.AppCompat.Dark` | `[]` |
| `@style/Widget.Design.Snackbar` | `[{'attr': 'android:background', 'attr_id': '0x010100D4', 'value': '@drawable/design_snackbar_background', 'value_type': 'reference'}, {'attr': 'android:paddingLeft', 'attr_id': '0x010100D6', 'value': '@dimen/design_snackbar_padding_horizontal', 'value_type': 'reference'}, {'attr': 'android:paddingRight', 'attr_id': '0x010100D8', 'value': '@dimen/design_snackbar_padding_horizontal', 'value_type': 'reference'}, {'attr': 'android:maxWidth', 'attr_id': '0x0101011F', 'value': '@dimen/design_snackbar_max_width', 'value_type': 'reference'}, {'attr': 'android:minWidth', 'attr_id': '0x0101013F', 'value': '@dimen/design_snackbar_min_width', 'value_type': 'reference'}, {'attr': 'attr.actionTextColorAlpha', 'attr_id': '0x7F040025', 'value': '@dimen/design_snackbar_action_text_color_alpha', 'value_type': 'reference'}, {'attr': 'attr.animationMode', 'attr_id': '0x7F04003E', 'value': '0', 'value_type': 'int_dec'}, {'attr': 'attr.elevation', 'attr_id': '0x7F040227', 'value': '@dimen/design_snackbar_elevation', 'value_type': 'reference'}, {'attr': 'attr.maxActionInlineWidth', 'attr_id': '0x7F040419', 'value': '@dimen/design_snackbar_action_inline_max_width', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
(none)
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
<view xmlns:android="http://schemas.android.com/apk/res/android" android:theme="@style/ThemeOverlay.AppCompat.Dark" android:layout_gravity="0x00000050" android:layout_width="match_parent" android:layout_height="wrap_content" class="com.google.android.material.snackbar.Snackbar$SnackbarLayout" style="@style/Widget.Design.Snackbar"/>
```
