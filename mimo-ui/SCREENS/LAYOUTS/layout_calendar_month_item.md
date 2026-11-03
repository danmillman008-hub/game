# پروندهٔ لایه — `res/layout/calendar_month_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/calendar_month_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/calendar_month_item.xml`](../../SOURCE/res/layout/calendar_month_item.xml) |
| SHA-256 دیکد | `e83523ed7978917f359f6c4530a4a16d678ee860bbc09efe36d3f2c76a27fcd9` |
| ریشه | `FrameLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 13 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout  #@id/test222
   ├─ androidx.recyclerview.widget.RecyclerView  #@id/rv_month
   ├─ com.google.android.material.progressindicator.CircularProgressIndicator  #@id/progress_indicator
   └─ TextView  #@id/tv_error_message
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:id` | `@id/test222` |
| 2 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 3 | `FrameLayout` | `android:layout_height` | `@dimen/streak_calendar_height` |
| 4 | `androidx.recyclerview.widget.RecyclerView` | `android:id` | `@id/rv_month` |
| 5 | `androidx.recyclerview.widget.RecyclerView` | `android:background` | `@color/background_secondary` |
| 6 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_width` | `match_parent` |
| 7 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_height` | `@dimen/streak_calendar_height` |
| 8 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:layout_gravity` | `0x00000011` |
| 9 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:id` | `@id/progress_indicator` |
| 10 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:visibility` | `invisible` |
| 11 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:layout_width` | `wrap_content` |
| 12 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:layout_height` | `wrap_content` |
| 13 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:layout_marginBottom` | `@dimen/spacing_l` |
| 14 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:indeterminate` | `true` |
| 15 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:indicatorColor` | `@color/progress_weak` |
| 16 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:showDelay` | `0` |
| 17 | `TextView` | `android:textColor` | `@color/text_primary` |
| 18 | `TextView` | `android:gravity` | `0x00000001` |
| 19 | `TextView` | `android:layout_gravity` | `0x00000011` |
| 20 | `TextView` | `android:id` | `@id/tv_error_message` |
| 21 | `TextView` | `android:visibility` | `invisible` |
| 22 | `TextView` | `android:layout_width` | `match_parent` |
| 23 | `TextView` | `android:layout_height` | `wrap_content` |
| 24 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_l` |
| 25 | `TextView` | `android:text` | `@string/streak_drawer_error_text` |
| 26 | `TextView` | `android:drawablePadding` | `@dimen/spacing_xs` |
| 27 | `TextView` | `app:drawableTint` | `@color/text_primary` |
| 28 | `TextView` | `app:drawableTopCompat` | `@drawable/ic_alert_circle` |
| 29 | `TextView` | `style` | `@style/TextP2` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/progress_weak` | `#FFD8C9F5` / `#FF6954B2` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/streak_calendar_height` | `264.000000dip` / `324.000000dip` (sw600dp) |
| `@string/streak_drawer_error_text` | `Oh no! Something went wrong here..` / `Oh nein! Hier ist etwas schiefgegangen ...` (de) / `¡Oh, no! Algo ha ido mal...` (es) / `Oh non ! Quelque chose a mal tourné ici..` (fr) / `Oh tidak, ada yang salah di sini..` (in) / `Qualcosa è andato storto..` (it) / `O nie! Coś tu poszło nie tak..` (pl) / `Ah não! Algo deu errado aqui...` (pt-rBR) / `О, нет! Что-то пошло не так…` (ru) / `Olamaz! Burada bir şeyler ters gitti..` (tr) |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/progress_indicator
@id/rv_month
@id/test222
@id/tv_error_message
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
<FrameLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/test222" android:layout_width="match_parent" android:layout_height="@dimen/streak_calendar_height">
  <androidx.recyclerview.widget.RecyclerView android:id="@id/rv_month" android:background="@color/background_secondary" android:layout_width="match_parent" android:layout_height="@dimen/streak_calendar_height"/>
  <com.google.android.material.progressindicator.CircularProgressIndicator android:layout_gravity="0x00000011" android:id="@id/progress_indicator" android:visibility="invisible" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_l" android:indeterminate="true" app:indicatorColor="@color/progress_weak" app:showDelay="0"/>
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000001" android:layout_gravity="0x00000011" android:id="@id/tv_error_message" android:visibility="invisible" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_l" android:text="@string/streak_drawer_error_text" android:drawablePadding="@dimen/spacing_xs" app:drawableTint="@color/text_primary" app:drawableTopCompat="@drawable/ic_alert_circle" style="@style/TextP2"/>
</FrameLayout>
```
