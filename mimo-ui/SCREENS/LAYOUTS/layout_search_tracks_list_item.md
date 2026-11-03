# پروندهٔ لایه — `res/layout/search_tracks_list_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/search_tracks_list_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/search_tracks_list_item.xml`](../../SOURCE/res/layout/search_tracks_list_item.xml) |
| SHA-256 دیکد | `e079657872e6e1e6287fe72a40252e242e74b9d9ad365d1995303c83f7c3ebe6` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 15 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.google.android.material.card.MaterialCardView  #@id/cardview_banner
   │  ├─ ImageView  #@id/iv_item_icon_rectangle
   │  └─ ImageView  #@id/iv_item_icon_round
   ├─ TextView  #@id/tv_item_title
   └─ TextView  #@id/tv_item_description
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `?0x0101030E` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:padding` | `@dimen/spacing_s` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 5 | `com.google.android.material.card.MaterialCardView` | `android:id` | `@id/cardview_banner` |
| 6 | `com.google.android.material.card.MaterialCardView` | `android:layout_width` | `120.000000dip` |
| 7 | `com.google.android.material.card.MaterialCardView` | `android:layout_height` | `wrap_content` |
| 8 | `com.google.android.material.card.MaterialCardView` | `app:cardBackgroundColor` | `@color/transparent` |
| 9 | `com.google.android.material.card.MaterialCardView` | `app:cardCornerRadius` | `4.000000dip` |
| 10 | `com.google.android.material.card.MaterialCardView` | `app:cardElevation` | `0.000000dip` |
| 11 | `com.google.android.material.card.MaterialCardView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 12 | `com.google.android.material.card.MaterialCardView` | `app:layout_constraintStart_toStartOf` | `0` |
| 13 | `com.google.android.material.card.MaterialCardView` | `app:layout_constraintTop_toTopOf` | `0` |
| 14 | `ImageView` | `android:id` | `@id/iv_item_icon_rectangle` |
| 15 | `ImageView` | `android:visibility` | `gone` |
| 16 | `ImageView` | `android:layout_width` | `match_parent` |
| 17 | `ImageView` | `android:layout_height` | `80.000000dip` |
| 18 | `ImageView` | `android:scaleType` | `centerInside` |
| 19 | `ImageView` | `android:adjustViewBounds` | `true` |
| 20 | `ImageView` | `app:srcCompat` | `@drawable/ic_square_blue` |
| 21 | `ImageView` | `android:layout_gravity` | `0x00000011` |
| 22 | `ImageView` | `android:id` | `@id/iv_item_icon_round` |
| 23 | `ImageView` | `android:visibility` | `gone` |
| 24 | `ImageView` | `android:layout_width` | `81.000000dip` |
| 25 | `ImageView` | `android:layout_height` | `87.000000dip` |
| 26 | `ImageView` | `android:scaleType` | `centerInside` |
| 27 | `ImageView` | `android:adjustViewBounds` | `true` |
| 28 | `TextView` | `android:textColor` | `@color/text_primary` |
| 29 | `TextView` | `android:ellipsize` | `end` |
| 30 | `TextView` | `android:id` | `@id/tv_item_title` |
| 31 | `TextView` | `android:layout_width` | `0.000000dip` |
| 32 | `TextView` | `android:layout_height` | `wrap_content` |
| 33 | `TextView` | `android:maxLines` | `2` |
| 34 | `TextView` | `android:layout_marginStart` | `@dimen/general_margin_16dp` |
| 35 | `TextView` | `android:layout_marginEnd` | `2.000000dip` |
| 36 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 37 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/cardview_banner` |
| 38 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 39 | `TextView` | `style` | `@style/TextTitle1` |
| 40 | `TextView` | `android:textAppearance` | `@style/TextP3` |
| 41 | `TextView` | `android:textColor` | `@color/text_weak` |
| 42 | `TextView` | `android:gravity` | `0x00000030` |
| 43 | `TextView` | `android:id` | `@id/tv_item_description` |
| 44 | `TextView` | `android:layout_width` | `0.000000dip` |
| 45 | `TextView` | `android:layout_height` | `wrap_content` |
| 46 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xxs` |
| 47 | `TextView` | `android:layout_marginStart` | `@dimen/general_margin_16dp` |
| 48 | `TextView` | `android:layout_marginEnd` | `2.000000dip` |
| 49 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 50 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/cardview_banner` |
| 51 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_item_title` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@color/transparent` | `#00000000` |
| `@dimen/general_margin_16dp` | `16.000000dip` / `20.000000dip` (sw600dp) |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@style/TextP3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextTitle1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000dip', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/cardview_banner
@id/iv_item_icon_rectangle
@id/iv_item_icon_round
@id/tv_item_description
@id/tv_item_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.tracksearch.SearchTrackFragment$onViewCreated$4$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:background="?0x0101030E" android:padding="@dimen/spacing_s" android:layout_width="match_parent" android:layout_height="wrap_content">
  <com.google.android.material.card.MaterialCardView android:id="@id/cardview_banner" android:layout_width="120.000000dip" android:layout_height="wrap_content" app:cardBackgroundColor="@color/transparent" app:cardCornerRadius="4.000000dip" app:cardElevation="0.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <ImageView android:id="@id/iv_item_icon_rectangle" android:visibility="gone" android:layout_width="match_parent" android:layout_height="80.000000dip" android:scaleType="centerInside" android:adjustViewBounds="true" app:srcCompat="@drawable/ic_square_blue"/>
    <ImageView android:layout_gravity="0x00000011" android:id="@id/iv_item_icon_round" android:visibility="gone" android:layout_width="81.000000dip" android:layout_height="87.000000dip" android:scaleType="centerInside" android:adjustViewBounds="true"/>
  </com.google.android.material.card.MaterialCardView>
  <TextView android:textColor="@color/text_primary" android:ellipsize="end" android:id="@id/tv_item_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:maxLines="2" android:layout_marginStart="@dimen/general_margin_16dp" android:layout_marginEnd="2.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/cardview_banner" app:layout_constraintTop_toTopOf="0" style="@style/TextTitle1"/>
  <TextView android:textAppearance="@style/TextP3" android:textColor="@color/text_weak" android:gravity="0x00000030" android:id="@id/tv_item_description" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xxs" android:layout_marginStart="@dimen/general_margin_16dp" android:layout_marginEnd="2.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/cardview_banner" app:layout_constraintTop_toBottomOf="@id/tv_item_title"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
