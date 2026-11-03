# پروندهٔ لایه — `res/layout/profile_header_unlocked.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/profile_header_unlocked.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/profile_header_unlocked.xml`](../../SOURCE/res/layout/profile_header_unlocked.xml) |
| SHA-256 دیکد | `20f1a55e5627df1c56be8f27ee43c95fd5c3de6632a00078b3f974536abc1620` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 8 |
| تعداد شناسه | 7 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 14 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.getmimo.ui.components.placeholder.TextPlaceholderView  #@id/tv_settings_user_name
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_profile_header_add_bio
   ├─ com.getmimo.ui.components.placeholder.TextPlaceholderView  #@id/tv_profile_header_bio
   ├─ androidx.constraintlayout.widget.Barrier  #@id/barrier_bio_bottom
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_profile_header_upgrade
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_follow
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_unfollow
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 3 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `android:id` | `@id/tv_settings_user_name` |
| 4 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `android:layout_width` | `0.000000dip` |
| 5 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `android:layout_height` | `wrap_content` |
| 6 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `android:layout_marginHorizontal` | `@dimen/spacing_s_expandable` |
| 7 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `app:content_centered` | `true` |
| 8 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `app:content_line_spacing_extra` | `0.000000dip` |
| 9 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `app:content_max_lines` | `2` |
| 10 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `app:content_text_color` | `@color/text_primary` |
| 11 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `app:content_text_style` | `@style/TextH2` |
| 12 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 13 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `app:layout_constraintStart_toStartOf` | `0` |
| 14 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `app:layout_constraintTop_toTopOf` | `0` |
| 15 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `app:placeholder_corner_radius` | `4.000000dip` |
| 16 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_profile_header_add_bio` |
| 17 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 18 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 19 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 20 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_xs_expandable` |
| 21 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 22 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 23 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_settings_user_name` |
| 24 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `android:id` | `@id/tv_profile_header_bio` |
| 25 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `android:layout_width` | `0.000000dip` |
| 26 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `android:layout_height` | `wrap_content` |
| 27 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `android:layout_marginTop` | `@dimen/spacing_s_expandable` |
| 28 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `android:layout_marginHorizontal` | `@dimen/spacing_s_expandable` |
| 29 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `app:content_centered` | `true` |
| 30 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `app:content_text_color` | `@color/text_weak` |
| 31 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `app:content_text_style` | `@style/TextP2` |
| 32 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 33 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `app:layout_constraintStart_toStartOf` | `0` |
| 34 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_settings_user_name` |
| 35 | `com.getmimo.ui.components.placeholder.TextPlaceholderView` | `app:placeholder_corner_radius` | `4.000000dip` |
| 36 | `androidx.constraintlayout.widget.Barrier` | `android:id` | `@id/barrier_bio_bottom` |
| 37 | `androidx.constraintlayout.widget.Barrier` | `android:layout_width` | `wrap_content` |
| 38 | `androidx.constraintlayout.widget.Barrier` | `android:layout_height` | `wrap_content` |
| 39 | `androidx.constraintlayout.widget.Barrier` | `app:barrierDirection` | `3` |
| 40 | `androidx.constraintlayout.widget.Barrier` | `app:constraint_referenced_ids` | `btn_profile_header_add_bio, tv_profile_header_bio` |
| 41 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_profile_header_upgrade` |
| 42 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 43 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 44 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 45 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_m_expandable` |
| 46 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 47 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 48 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/barrier_bio_bottom` |
| 49 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_follow` |
| 50 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `invisible` |
| 51 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 52 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 53 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_m_expandable` |
| 54 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 55 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 56 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 57 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/barrier_bio_bottom` |
| 58 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `140.000000dip` |
| 59 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_unfollow` |
| 60 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 61 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 62 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 63 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_m_expandable` |
| 64 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 65 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 66 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 67 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/barrier_bio_bottom` |
| 68 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `140.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_s_expandable` | `12.000000dip` / `16.000000dip` (sw600dp) |
| `@dimen/spacing_xs_expandable` | `8.000000dip` / `12.000000dip` (sw600dp) |
| `@style/TextH2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '26.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/barrier_bio_bottom
@id/btn_follow
@id/btn_profile_header_add_bio
@id/btn_profile_header_upgrade
@id/btn_unfollow
@id/tv_profile_header_bio
@id/tv_settings_user_name
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.profile.main.ProfileFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/profile_header_view.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_width="match_parent" android:layout_height="wrap_content">
  <com.getmimo.ui.components.placeholder.TextPlaceholderView android:id="@id/tv_settings_user_name" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginHorizontal="@dimen/spacing_s_expandable" app:content_centered="true" app:content_line_spacing_extra="0.000000dip" app:content_max_lines="2" app:content_text_color="@color/text_primary" app:content_text_style="@style/TextH2" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:placeholder_corner_radius="4.000000dip"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_profile_header_add_bio" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs_expandable" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_settings_user_name"/>
  <com.getmimo.ui.components.placeholder.TextPlaceholderView android:id="@id/tv_profile_header_bio" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s_expandable" android:layout_marginHorizontal="@dimen/spacing_s_expandable" app:content_centered="true" app:content_text_color="@color/text_weak" app:content_text_style="@style/TextP2" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_settings_user_name" app:placeholder_corner_radius="4.000000dip"/>
  <androidx.constraintlayout.widget.Barrier android:id="@id/barrier_bio_bottom" android:layout_width="wrap_content" android:layout_height="wrap_content" app:barrierDirection="3" app:constraint_referenced_ids="btn_profile_header_add_bio, tv_profile_header_bio"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_profile_header_upgrade" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m_expandable" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/barrier_bio_bottom"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_follow" android:visibility="invisible" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m_expandable" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/barrier_bio_bottom" app:layout_constraintWidth_max="140.000000dip"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_unfollow" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m_expandable" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/barrier_bio_bottom" app:layout_constraintWidth_max="140.000000dip"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
