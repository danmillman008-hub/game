# پروندهٔ لایه — `res/layout/code_view_action_button.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/code_view_action_button.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/code_view_action_button.xml`](../../SOURCE/res/layout/code_view_action_button.xml) |
| SHA-256 دیکد | `6618b0315b03246f16a4dd921913f3d1c252fb8f7124b5dc1f3cc31ec7b1e6bc` |
| ریشه | `merge` |
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
└─ merge
   ├─ ImageView  #@id/iv_code_view_action_button
   └─ TextView  #@id/tv_code_view_action_button
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `merge` | `android:layout_width` | `wrap_content` |
| 2 | `merge` | `android:layout_height` | `wrap_content` |
| 3 | `ImageView` | `android:id` | `@id/iv_code_view_action_button` |
| 4 | `ImageView` | `android:layout_width` | `wrap_content` |
| 5 | `ImageView` | `android:layout_height` | `wrap_content` |
| 6 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 7 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 8 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 9 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 10 | `TextView` | `android:textColor` | `@color/text_primary` |
| 11 | `TextView` | `android:gravity` | `0x00000011` |
| 12 | `TextView` | `android:id` | `@id/tv_code_view_action_button` |
| 13 | `TextView` | `android:layout_width` | `wrap_content` |
| 14 | `TextView` | `android:layout_height` | `wrap_content` |
| 15 | `TextView` | `android:text` | `@string/edit` |
| 16 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 17 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 18 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 19 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 20 | `TextView` | `style` | `@style/TextButton2` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@string/edit` | `Edit` / `Bearbeiten` (de) / `Editar` (es) / `Éditer` (fr) / `Edit` (in) / `Modifica` (it) / `Edytuj` (pl) / `Editar` (pt-rBR) / `Редактировать` (ru) / `Düzenle` (tr) |
| `@style/TextButton2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000dip', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_code_view_action_button
@id/tv_code_view_action_button
```

## ۵. ارجاع به لایه‌های دیگر

```text
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="wrap_content" android:layout_height="wrap_content">
  <ImageView android:id="@id/iv_code_view_action_button" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_code_view_action_button" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/edit" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextButton2"/>
</merge>
```
