# پروندهٔ لایه — `res/layout/item_bottom_sheet_picker.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/item_bottom_sheet_picker.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/item_bottom_sheet_picker.xml`](../../SOURCE/res/layout/item_bottom_sheet_picker.xml) |
| SHA-256 دیکد | `7afdb677072d4d9a7cd7afa6689999619aff143bb497537ebcded04745ac75ce` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 5 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   └─ TextView  #@id/tv_item_bottom_sheet_picker
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `56.000000dip` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:foreground` | `?attr/selectableItemBackground` |
| 4 | `TextView` | `android:textColor` | `@color/text_primary` |
| 5 | `TextView` | `android:id` | `@id/tv_item_bottom_sheet_picker` |
| 6 | `TextView` | `android:layout_width` | `wrap_content` |
| 7 | `TextView` | `android:layout_height` | `wrap_content` |
| 8 | `TextView` | `android:layout_marginStart` | `@dimen/rv_challenge_difficulty_inset` |
| 9 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 10 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 11 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 12 | `TextView` | `style` | `@style/TextSubtitle` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/rv_challenge_difficulty_inset` | `16.000000dip` |
| `@style/TextSubtitle` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/tv_item_bottom_sheet_picker
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="56.000000dip" android:foreground="?attr/selectableItemBackground">
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_item_bottom_sheet_picker" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginStart="@dimen/rv_challenge_difficulty_inset" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextSubtitle"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
