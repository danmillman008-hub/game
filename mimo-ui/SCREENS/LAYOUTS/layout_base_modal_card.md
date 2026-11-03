# پروندهٔ لایه — `res/layout/base_modal_card.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/base_modal_card.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/base_modal_card.xml`](../../SOURCE/res/layout/base_modal_card.xml) |
| SHA-256 دیکد | `0204db9b8fbbb672442f911981c0bf4c4fa94370518e120aff1e01a2e9a1148e` |
| ریشه | `androidx.cardview.widget.CardView` |
| تعداد گره | 12 |
| تعداد شناسه | 10 |
| تگ‌های استفاده‌شده | 10 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 30 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.cardview.widget.CardView
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ ImageButton  #@id/iv_modal_close
      ├─ FrameLayout  #@id/image_container_base_modal
      │  ├─ ImageView  #@id/iv_base_modal
      │  ├─ com.airbnb.lottie.LottieAnimationView  #@id/lav_base_modal_animation
      │  └─ app.rive.runtime.kotlin.RiveAnimationView  #@id/rive_base_modal_animation
      ├─ TextView  #@id/tv_base_modal_title
      ├─ ScrollView  #@id/sv_base_modal_description
      │  └─ TextView  #@id/tv_base_modal_description
      ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_primary_action
      └─ TextView  #@id/tv_secondary_action
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.cardview.widget.CardView` | `android:layout_gravity` | `0x00000011` |
| 2 | `androidx.cardview.widget.CardView` | `android:focusable` | `true` |
| 3 | `androidx.cardview.widget.CardView` | `android:clickable` | `true` |
| 4 | `androidx.cardview.widget.CardView` | `android:layout_width` | `@dimen/modal_default_width` |
| 5 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 6 | `androidx.cardview.widget.CardView` | `android:layout_margin` | `@dimen/spacing_m` |
| 7 | `androidx.cardview.widget.CardView` | `android:paddingHorizontal` | `@dimen/spacing_l` |
| 8 | `androidx.cardview.widget.CardView` | `app:cardBackgroundColor` | `@color/background_secondary` |
| 9 | `androidx.cardview.widget.CardView` | `app:cardCornerRadius` | `@dimen/modal_corner_radius` |
| 10 | `androidx.cardview.widget.CardView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 11 | `androidx.cardview.widget.CardView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 12 | `androidx.cardview.widget.CardView` | `app:layout_constraintStart_toStartOf` | `0` |
| 13 | `androidx.cardview.widget.CardView` | `app:layout_constraintTop_toTopOf` | `0` |
| 14 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 15 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 16 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 17 | `ImageButton` | `android:id` | `@id/iv_modal_close` |
| 18 | `ImageButton` | `android:background` | `?attr/selectableItemBackgroundBorderless` |
| 19 | `ImageButton` | `android:padding` | `@dimen/modal_default_close_button_padding` |
| 20 | `ImageButton` | `android:layout_width` | `wrap_content` |
| 21 | `ImageButton` | `android:layout_height` | `wrap_content` |
| 22 | `ImageButton` | `app:layout_constraintEnd_toEndOf` | `0` |
| 23 | `ImageButton` | `app:layout_constraintTop_toTopOf` | `0` |
| 24 | `ImageButton` | `app:srcCompat` | `@drawable/ic_close` |
| 25 | `ImageButton` | `app:tint` | `@color/icon_weak` |
| 26 | `FrameLayout` | `android:id` | `@id/image_container_base_modal` |
| 27 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 28 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 29 | `FrameLayout` | `android:layout_marginTop` | `@dimen/spacing_xxl` |
| 30 | `FrameLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 31 | `FrameLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 32 | `FrameLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 33 | `FrameLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 34 | `ImageView` | `android:id` | `@id/iv_base_modal` |
| 35 | `ImageView` | `android:visibility` | `gone` |
| 36 | `ImageView` | `android:layout_width` | `wrap_content` |
| 37 | `ImageView` | `android:layout_height` | `@dimen/modal_default_image_height` |
| 38 | `ImageView` | `android:scaleType` | `centerInside` |
| 39 | `ImageView` | `android:adjustViewBounds` | `true` |
| 40 | `com.airbnb.lottie.LottieAnimationView` | `android:id` | `@id/lav_base_modal_animation` |
| 41 | `com.airbnb.lottie.LottieAnimationView` | `android:visibility` | `gone` |
| 42 | `com.airbnb.lottie.LottieAnimationView` | `android:layout_width` | `wrap_content` |
| 43 | `com.airbnb.lottie.LottieAnimationView` | `android:layout_height` | `@dimen/modal_default_image_height` |
| 44 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_gravity` | `0x00000001` |
| 45 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:id` | `@id/rive_base_modal_animation` |
| 46 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:visibility` | `gone` |
| 47 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_width` | `120.000000dip` |
| 48 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_height` | `100.000000dip` |
| 49 | `TextView` | `android:textColor` | `@color/text_primary` |
| 50 | `TextView` | `android:gravity` | `0x00000011` |
| 51 | `TextView` | `android:id` | `@id/tv_base_modal_title` |
| 52 | `TextView` | `android:layout_width` | `0.000000dip` |
| 53 | `TextView` | `android:layout_height` | `wrap_content` |
| 54 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 55 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 56 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 57 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 58 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/image_container_base_modal` |
| 59 | `TextView` | `style` | `@style/TextH2` |
| 60 | `ScrollView` | `android:id` | `@id/sv_base_modal_description` |
| 61 | `ScrollView` | `android:layout_width` | `0.000000dip` |
| 62 | `ScrollView` | `android:layout_height` | `0.000000dip` |
| 63 | `ScrollView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 64 | `ScrollView` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 65 | `ScrollView` | `app:layout_constraintBottom_toTopOf` | `@id/btn_primary_action` |
| 66 | `ScrollView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 67 | `ScrollView` | `app:layout_constraintHeight_default` | `1` |
| 68 | `ScrollView` | `app:layout_constraintHeight_max` | `@dimen/modal_default_description_max_height` |
| 69 | `ScrollView` | `app:layout_constraintHeight_min` | `16.000000dip` |
| 70 | `ScrollView` | `app:layout_constraintStart_toStartOf` | `0` |
| 71 | `ScrollView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_base_modal_title` |
| 72 | `TextView` | `android:textColor` | `@color/text_weak` |
| 73 | `TextView` | `android:gravity` | `0x00000011` |
| 74 | `TextView` | `android:id` | `@id/tv_base_modal_description` |
| 75 | `TextView` | `android:layout_width` | `match_parent` |
| 76 | `TextView` | `android:layout_height` | `wrap_content` |
| 77 | `TextView` | `style` | `@style/TextP2` |
| 78 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_primary_action` |
| 79 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 80 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 81 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 82 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 83 | `androidx.compose.ui.platform.ComposeView` | `android:minWidth` | `@dimen/modal_upgrade_continue_button_width` |
| 84 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 85 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_secondary_action` |
| 86 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 87 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 88 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/sv_base_modal_description` |
| 89 | `TextView` | `android:id` | `@id/tv_secondary_action` |
| 90 | `TextView` | `android:visibility` | `gone` |
| 91 | `TextView` | `android:layout_width` | `0.000000dip` |
| 92 | `TextView` | `android:layout_height` | `wrap_content` |
| 93 | `TextView` | `android:text` | `@string/not_now` |
| 94 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 95 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 96 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 97 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/btn_primary_action` |
| 98 | `TextView` | `style` | `@style/MaterialButton.TextButton.Enabled` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/modal_corner_radius` | `12.000000dip` |
| `@dimen/modal_default_close_button_padding` | `12.000000dip` |
| `@dimen/modal_default_description_max_height` | `200.000000dip` / `300.000000dip` (sw600dp) / `150.000000dip` (sw600dp-land) |
| `@dimen/modal_default_image_height` | `80.000000dip` |
| `@dimen/modal_default_width` | `296.000000dip` / `360.000000dip` (sw600dp) |
| `@dimen/modal_upgrade_continue_button_width` | `200.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxl` | `40.000000dip` |
| `@string/not_now` | `Not now` / `Jetzt nicht` (de) / `Ahora no` (es) / `Pas maintenant` (fr) / `Nanti saja` (in) / `Non ora` (it) / `Nie teraz` (pl) / `Agora não` (pt-rBR) / `Не сейчас` (ru) / `Şimdi değil` (tr) |
| `@style/MaterialButton.TextButton.Enabled` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/button_text_enabled', 'value_type': 'reference'}]` |
| `@style/TextH2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '26.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_primary_action
@id/image_container_base_modal
@id/iv_base_modal
@id/iv_modal_close
@id/lav_base_modal_animation
@id/rive_base_modal_animation
@id/sv_base_modal_description
@id/tv_base_modal_description
@id/tv_base_modal_title
@id/tv_secondary_action
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/base_modal_fragment.xml
res/layout/feature_introduction_modal_fragment.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.cardview.widget.CardView xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_gravity="0x00000011" android:focusable="true" android:clickable="true" android:layout_width="@dimen/modal_default_width" android:layout_height="wrap_content" android:layout_margin="@dimen/spacing_m" android:paddingHorizontal="@dimen/spacing_l" app:cardBackgroundColor="@color/background_secondary" app:cardCornerRadius="@dimen/modal_corner_radius" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
  <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m">
    <ImageButton android:id="@id/iv_modal_close" android:background="?attr/selectableItemBackgroundBorderless" android:padding="@dimen/modal_default_close_button_padding" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/ic_close" app:tint="@color/icon_weak"/>
    <FrameLayout android:id="@id/image_container_base_modal" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xxl" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
      <ImageView android:id="@id/iv_base_modal" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="@dimen/modal_default_image_height" android:scaleType="centerInside" android:adjustViewBounds="true"/>
      <com.airbnb.lottie.LottieAnimationView android:id="@id/lav_base_modal_animation" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="@dimen/modal_default_image_height"/>
      <app.rive.runtime.kotlin.RiveAnimationView android:layout_gravity="0x00000001" android:id="@id/rive_base_modal_animation" android:visibility="gone" android:layout_width="120.000000dip" android:layout_height="100.000000dip"/>
    </FrameLayout>
    <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_base_modal_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/image_container_base_modal" style="@style/TextH2"/>
    <ScrollView android:id="@id/sv_base_modal_description" android:layout_width="0.000000dip" android:layout_height="0.000000dip" android:layout_marginTop="@dimen/spacing_xs" android:layout_marginHorizontal="@dimen/spacing_l" app:layout_constraintBottom_toTopOf="@id/btn_primary_action" app:layout_constraintEnd_toEndOf="0" app:layout_constraintHeight_default="1" app:layout_constraintHeight_max="@dimen/modal_default_description_max_height" app:layout_constraintHeight_min="16.000000dip" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_base_modal_title">
      <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_base_modal_description" android:layout_width="match_parent" android:layout_height="wrap_content" style="@style/TextP2"/>
    </ScrollView>
    <androidx.compose.ui.platform.ComposeView android:id="@id/btn_primary_action" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:layout_marginBottom="@dimen/spacing_m" android:minWidth="@dimen/modal_upgrade_continue_button_width" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toTopOf="@id/tv_secondary_action" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/sv_base_modal_description"/>
    <TextView android:id="@id/tv_secondary_action" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:text="@string/not_now" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/btn_primary_action" style="@style/MaterialButton.TextButton.Enabled"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
</androidx.cardview.widget.CardView>
```
