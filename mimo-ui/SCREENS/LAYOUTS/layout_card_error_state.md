# پروندهٔ لایه — `res/layout/card_error_state.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/card_error_state.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/card_error_state.xml`](../../SOURCE/res/layout/card_error_state.xml) |
| SHA-256 دیکد | `2096771e8c2142e6a7b460fe7adf0b179d1a87248a8fa611fb00723b47a4d6f6` |
| ریشه | `LinearLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   └─ TextView  #@id/layout_saved_code_empty_view_description
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:background` | `@drawable/border_dashed` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 5 | `LinearLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_s` |
| 6 | `TextView` | `android:textColor` | `@color/text_weak` |
| 7 | `TextView` | `android:gravity` | `0x00000001` |
| 8 | `TextView` | `android:layout_gravity` | `0x00000001` |
| 9 | `TextView` | `android:id` | `@id/layout_saved_code_empty_view_description` |
| 10 | `TextView` | `android:layout_width` | `wrap_content` |
| 11 | `TextView` | `android:layout_height` | `wrap_content` |
| 12 | `TextView` | `android:layout_margin` | `@dimen/spacing_l` |
| 13 | `TextView` | `android:text` | `@string/profile_error` |
| 14 | `TextView` | `style` | `@style/TextP2` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@string/profile_error` | `Oh no! Something went wrong here.` / `Oh nein! Hier ist etwas schiefgegangen.` (de) / `¡Oh, no! Algo ha salido mal.` (es) / `Oh non! Quelque chose a mal tourné ici.` (fr) / `Oh tidak, ada yang salah di sini.` (in) / `Qualcosa è andato storto.` (it) / `O nie! Coś tu poszło nie tak.` (pl) / `Ah não! Algo deu errado aqui.` (pt-rBR) / `Упс! Что-то пошло не так.` (ru) / `Olamaz! Burada bir şeyler ters gitti.` (tr) |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/layout_saved_code_empty_view_description
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:background="@drawable/border_dashed" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginHorizontal="@dimen/spacing_s">
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000001" android:layout_gravity="0x00000001" android:id="@id/layout_saved_code_empty_view_description" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_margin="@dimen/spacing_l" android:text="@string/profile_error" style="@style/TextP2"/>
</LinearLayout>
```
