# پروندهٔ لایه — `res/layout/choice_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/choice_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/choice_view.xml`](../../SOURCE/res/layout/choice_view.xml) |
| SHA-256 دیکد | `fb1376268fbbe8532d963fc36acda0b3b2508cdb8ef9ed726edba2f3e1219230` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ TextView  #@id/tv_multiplechoice_hint
   └─ androidx.recyclerview.widget.RecyclerView  #@id/rv_multiplechoice_options
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 3 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 4 | `TextView` | `android:id` | `@id/tv_multiplechoice_hint` |
| 5 | `TextView` | `android:layout_width` | `match_parent` |
| 6 | `TextView` | `android:layout_height` | `wrap_content` |
| 7 | `TextView` | `style` | `@style/TextInteractionHint` |
| 8 | `androidx.recyclerview.widget.RecyclerView` | `android:id` | `@id/rv_multiplechoice_options` |
| 9 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_width` | `match_parent` |
| 10 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_height` | `wrap_content` |
| 11 | `androidx.recyclerview.widget.RecyclerView` | `android:overScrollMode` | `2` |
| 12 | `androidx.recyclerview.widget.RecyclerView` | `android:nestedScrollingEnabled` | `false` |
| 13 | `androidx.recyclerview.widget.RecyclerView` | `android:paddingHorizontal` | `@dimen/spacing_s` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/spacing_s` | `12.000000dip` |
| `@style/TextInteractionHint` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_weak', 'value_type': 'reference'}, {'attr': 'android:gravity', 'attr_id': '0x010100AF', 'value': '0x00000010', 'value_type': 'int_hex'}, {'attr': 'android:layout_marginTop', 'attr_id': '0x010100F8', 'value': '@dimen/spacing_l', 'value_type': 'reference'}, {'attr': 'android:drawablePadding', 'attr_id': '0x01010171', 'value': '@dimen/spacing_xxs', 'value_type': 'reference'}, {'attr': 'android:layout_marginStart', 'attr_id': '0x010103B5', 'value': '@dimen/spacing_m', 'value_type': 'reference'}, {'attr': 'android:layout_marginEnd', 'attr_id': '0x010103B6', 'value': '@dimen/spacing_m', 'value_type': 'reference'}, {'attr': 'attr.drawableStartCompat', 'attr_id': '0x7F040217', 'value': '@drawable/ic_info_circle', 'value_type': 'reference'}, {'attr': 'attr.drawableTint', 'attr_id': '0x7F040218', 'value': '@color/text_weak', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/rv_multiplechoice_options
@id/tv_multiplechoice_hint
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
  <TextView android:id="@id/tv_multiplechoice_hint" android:layout_width="match_parent" android:layout_height="wrap_content" style="@style/TextInteractionHint"/>
  <androidx.recyclerview.widget.RecyclerView android:id="@id/rv_multiplechoice_options" android:layout_width="match_parent" android:layout_height="wrap_content" android:overScrollMode="2" android:nestedScrollingEnabled="false" android:paddingHorizontal="@dimen/spacing_s"/>
</LinearLayout>
```
