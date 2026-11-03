# پروندهٔ لایه — `res/layout/offline_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/offline_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/offline_view.xml`](../../SOURCE/res/layout/offline_view.xml) |
| SHA-256 دیکد | `577cc19e175fd7dcfce9278a82b1cab546c564d8ecb35dbabd80cbb067d18992` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 14 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ ImageView  #@id/iv_offline_illustration
   ├─ TextView  #@id/tv_offline_header
   ├─ TextView  #@id/tv_offline_description
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_offline_refresh
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000011` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `ImageView` | `android:id` | `@id/iv_offline_illustration` |
| 5 | `ImageView` | `android:layout_width` | `wrap_content` |
| 6 | `ImageView` | `android:layout_height` | `wrap_content` |
| 7 | `ImageView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_offline_header` |
| 8 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 9 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 10 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 11 | `ImageView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 12 | `ImageView` | `app:srcCompat` | `@drawable/ic_state_offline` |
| 13 | `TextView` | `android:textColor` | `@color/text_primary` |
| 14 | `TextView` | `android:id` | `@id/tv_offline_header` |
| 15 | `TextView` | `android:layout_width` | `wrap_content` |
| 16 | `TextView` | `android:layout_height` | `wrap_content` |
| 17 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 18 | `TextView` | `android:text` | `@string/offline_message` |
| 19 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_offline_description` |
| 20 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 21 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 22 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_offline_illustration` |
| 23 | `TextView` | `style` | `@style/TextH3` |
| 24 | `TextView` | `android:textColor` | `@color/text_weak` |
| 25 | `TextView` | `android:gravity` | `0x00000011` |
| 26 | `TextView` | `android:id` | `@id/tv_offline_description` |
| 27 | `TextView` | `android:layout_width` | `0.000000dip` |
| 28 | `TextView` | `android:layout_height` | `wrap_content` |
| 29 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 30 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_xxl` |
| 31 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/btn_offline_refresh` |
| 32 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 33 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 34 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_offline_header` |
| 35 | `TextView` | `style` | `@style/TextP2` |
| 36 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_offline_refresh` |
| 37 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 38 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 39 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 40 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 41 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 42 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 43 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 44 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_offline_description` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xxl` | `40.000000dip` |
| `@string/offline_message` | `Looks like you're offline` / `Sieht so aus, als wärst du offline` (de) / `Parece que estás offline` (es) / `Il semble que tu sois hors ligne` (fr) / `Sepertinya kamu sedang offline` (in) / `Sembra che tu sia offline` (it) / `Wygląda na to, że jesteś offline` (pl) / `Parece que você está off-line` (pt-rBR) / `Кажется, ты оффлайн` (ru) / `Görünüşe göre çevrimdışısın` (tr) |
| `@style/TextH3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_offline_refresh
@id/iv_offline_illustration
@id/tv_offline_description
@id/tv_offline_header
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000011" android:layout_width="match_parent" android:layout_height="match_parent">
  <ImageView android:id="@id/iv_offline_illustration" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintBottom_toTopOf="@id/tv_offline_header" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:layout_constraintVertical_chainStyle="2" app:srcCompat="@drawable/ic_state_offline"/>
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_offline_header" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/offline_message" app:layout_constraintBottom_toTopOf="@id/tv_offline_description" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_offline_illustration" style="@style/TextH3"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_offline_description" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:layout_marginHorizontal="@dimen/spacing_xxl" app:layout_constraintBottom_toTopOf="@id/btn_offline_refresh" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_offline_header" style="@style/TextP2"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_offline_refresh" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_offline_description"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
