# پروندهٔ لایه — `res/layout/partially_editable_edittext.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/partially_editable_edittext.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/partially_editable_edittext.xml`](../../SOURCE/res/layout/partially_editable_edittext.xml) |
| SHA-256 دیکد | `a8daa79aac0714c68b8b5981ddcd0951b02f1b92df02c01ef7cb0d117d7b3705` |
| ریشه | `com.getmimo.ui.lesson.interactive.PartiallyEditableEditText` |
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
└─ com.getmimo.ui.lesson.interactive.PartiallyEditableEditText  #@id/et_lesson_code
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `com.getmimo.ui.lesson.interactive.PartiallyEditableEditText` | `android:gravity` | `0x00800033` |
| 2 | `com.getmimo.ui.lesson.interactive.PartiallyEditableEditText` | `android:id` | `@id/et_lesson_code` |
| 3 | `com.getmimo.ui.lesson.interactive.PartiallyEditableEditText` | `android:background` | `@null` |
| 4 | `com.getmimo.ui.lesson.interactive.PartiallyEditableEditText` | `android:paddingTop` | `@dimen/lesson_codeview_padding_top` |
| 5 | `com.getmimo.ui.lesson.interactive.PartiallyEditableEditText` | `android:paddingBottom` | `@dimen/lesson_codeview_padding_bottom` |
| 6 | `com.getmimo.ui.lesson.interactive.PartiallyEditableEditText` | `android:focusable` | `true` |
| 7 | `com.getmimo.ui.lesson.interactive.PartiallyEditableEditText` | `android:clickable` | `true` |
| 8 | `com.getmimo.ui.lesson.interactive.PartiallyEditableEditText` | `android:layout_width` | `match_parent` |
| 9 | `com.getmimo.ui.lesson.interactive.PartiallyEditableEditText` | `android:layout_height` | `wrap_content` |
| 10 | `com.getmimo.ui.lesson.interactive.PartiallyEditableEditText` | `android:textCursorDrawable` | `@drawable/codeeditor_cursor_background` |
| 11 | `com.getmimo.ui.lesson.interactive.PartiallyEditableEditText` | `style` | `@style/TextCodeEditor` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/lesson_codeview_padding_bottom` | `@dimen/spacing_s_expandable` |
| `@dimen/lesson_codeview_padding_top` | `@dimen/spacing_xs_expandable` |
| `@style/TextCodeEditor` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/code_primary', 'value_type': 'reference'}, {'attr': 'android:textCursorDrawable', 'attr_id': '0x01010362', 'value': '@drawable/codeeditor_cursor_background', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/et_lesson_code
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
<com.getmimo.ui.lesson.interactive.PartiallyEditableEditText xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00800033" android:id="@id/et_lesson_code" android:background="@null" android:paddingTop="@dimen/lesson_codeview_padding_top" android:paddingBottom="@dimen/lesson_codeview_padding_bottom" android:focusable="true" android:clickable="true" android:layout_width="match_parent" android:layout_height="wrap_content" android:textCursorDrawable="@drawable/codeeditor_cursor_background" style="@style/TextCodeEditor"/>
```
