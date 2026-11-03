# پروندهٔ لایه — `res/layout/code_edit_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/code_edit_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/code_edit_view.xml`](../../SOURCE/res/layout/code_edit_view.xml) |
| SHA-256 دیکد | `ab7a59c266202be508f3ba3c1f86e8693165599384d6a2dbcc011986f824120c` |
| ریشه | `com.getmimo.ui.codeeditor.view.CodeEditView` |
| تعداد گره | 1 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ com.getmimo.ui.codeeditor.view.CodeEditView  #@id/codeeditor_editable
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `com.getmimo.ui.codeeditor.view.CodeEditView` | `android:gravity` | `0x00000030` |
| 2 | `com.getmimo.ui.codeeditor.view.CodeEditView` | `android:id` | `@id/codeeditor_editable` |
| 3 | `com.getmimo.ui.codeeditor.view.CodeEditView` | `android:background` | `@null` |
| 4 | `com.getmimo.ui.codeeditor.view.CodeEditView` | `android:paddingTop` | `@dimen/lesson_codeview_padding_top` |
| 5 | `com.getmimo.ui.codeeditor.view.CodeEditView` | `android:paddingBottom` | `@dimen/lesson_codeview_padding_bottom` |
| 6 | `com.getmimo.ui.codeeditor.view.CodeEditView` | `android:layout_width` | `match_parent` |
| 7 | `com.getmimo.ui.codeeditor.view.CodeEditView` | `android:layout_height` | `wrap_content` |
| 8 | `com.getmimo.ui.codeeditor.view.CodeEditView` | `android:minHeight` | `@dimen/codeview_min_height` |
| 9 | `com.getmimo.ui.codeeditor.view.CodeEditView` | `style` | `@style/TextCodeEditor` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/codeview_min_height` | `100.000000dip` |
| `@dimen/lesson_codeview_padding_bottom` | `@dimen/spacing_s_expandable` |
| `@dimen/lesson_codeview_padding_top` | `@dimen/spacing_xs_expandable` |
| `@style/TextCodeEditor` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/code_primary', 'value_type': 'reference'}, {'attr': 'android:textCursorDrawable', 'attr_id': '0x01010362', 'value': '@drawable/codeeditor_cursor_background', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/codeeditor_editable
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
<com.getmimo.ui.codeeditor.view.CodeEditView xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000030" android:id="@id/codeeditor_editable" android:background="@null" android:paddingTop="@dimen/lesson_codeview_padding_top" android:paddingBottom="@dimen/lesson_codeview_padding_bottom" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="@dimen/codeview_min_height" style="@style/TextCodeEditor"/>
```
