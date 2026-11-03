# پروندهٔ لایه — `res/layout/settings_user_settings.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/settings_user_settings.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/settings_user_settings.xml`](../../SOURCE/res/layout/settings_user_settings.xml) |
| SHA-256 دیکد | `ed23b5c8f0b591650cc4ebdb37605f0f9d534f668a345042372661da00388a20` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 13 |
| تعداد شناسه | 12 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 34 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.google.android.material.imageview.ShapeableImageView  #@id/iv_settings_profile
   ├─ com.google.android.material.imageview.ShapeableImageView  #@id/iv_settings_profile_edit_avatar
   ├─ TextView  #@id/tv_settings_profile_name_header
   ├─ com.google.android.material.textfield.TextInputLayout  #@id/til_settings_profile_name
   │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_settings_profile_name
   ├─ TextView  #@id/tv_settings_profile_bio_header
   ├─ com.google.android.material.textfield.TextInputLayout  #@id/til_settings_profile_bio
   │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_settings_profile_bio
   ├─ TextView  #@id/tv_settings_profile_email_header
   ├─ com.google.android.material.textfield.TextInputLayout  #@id/til_settings_profile_email
   │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_settings_profile_email
   └─ androidx.constraintlayout.widget.Group  #@id/group_anonymous
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:orientation` | `vertical` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 4 | `com.google.android.material.imageview.ShapeableImageView` | `android:layout_gravity` | `0x00000001` |
| 5 | `com.google.android.material.imageview.ShapeableImageView` | `android:id` | `@id/iv_settings_profile` |
| 6 | `com.google.android.material.imageview.ShapeableImageView` | `android:layout_width` | `@dimen/profile_header_avatar_size` |
| 7 | `com.google.android.material.imageview.ShapeableImageView` | `android:layout_height` | `@dimen/profile_header_avatar_size` |
| 8 | `com.google.android.material.imageview.ShapeableImageView` | `android:scaleType` | `centerCrop` |
| 9 | `com.google.android.material.imageview.ShapeableImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 10 | `com.google.android.material.imageview.ShapeableImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 11 | `com.google.android.material.imageview.ShapeableImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 12 | `com.google.android.material.imageview.ShapeableImageView` | `app:shapeAppearanceOverlay` | `@style/CircularImageView` |
| 13 | `com.google.android.material.imageview.ShapeableImageView` | `android:layout_gravity` | `0x00000001` |
| 14 | `com.google.android.material.imageview.ShapeableImageView` | `android:id` | `@id/iv_settings_profile_edit_avatar` |
| 15 | `com.google.android.material.imageview.ShapeableImageView` | `android:background` | `@color/primary_default` |
| 16 | `com.google.android.material.imageview.ShapeableImageView` | `android:padding` | `1.000000dip` |
| 17 | `com.google.android.material.imageview.ShapeableImageView` | `android:layout_width` | `34.000000dip` |
| 18 | `com.google.android.material.imageview.ShapeableImageView` | `android:layout_height` | `34.000000dip` |
| 19 | `com.google.android.material.imageview.ShapeableImageView` | `android:foreground` | `?attr/selectableItemBackgroundBorderless` |
| 20 | `com.google.android.material.imageview.ShapeableImageView` | `android:scaleType` | `centerInside` |
| 21 | `com.google.android.material.imageview.ShapeableImageView` | `app:contentPadding` | `8.000000dip` |
| 22 | `com.google.android.material.imageview.ShapeableImageView` | `app:layout_constraintCircle` | `@id/iv_settings_profile` |
| 23 | `com.google.android.material.imageview.ShapeableImageView` | `app:layout_constraintCircleAngle` | `135.000000` |
| 24 | `com.google.android.material.imageview.ShapeableImageView` | `app:layout_constraintCircleRadius` | `45.000000dip` |
| 25 | `com.google.android.material.imageview.ShapeableImageView` | `app:shapeAppearanceOverlay` | `@style/CircularImageView` |
| 26 | `com.google.android.material.imageview.ShapeableImageView` | `app:srcCompat` | `@drawable/ic_edit` |
| 27 | `com.google.android.material.imageview.ShapeableImageView` | `app:strokeColor` | `@color/background_primary` |
| 28 | `com.google.android.material.imageview.ShapeableImageView` | `app:strokeWidth` | `2.000000dip` |
| 29 | `com.google.android.material.imageview.ShapeableImageView` | `app:tint` | `@color/white` |
| 30 | `TextView` | `android:textColor` | `@color/text_weak` |
| 31 | `TextView` | `android:id` | `@id/tv_settings_profile_name_header` |
| 32 | `TextView` | `android:layout_width` | `wrap_content` |
| 33 | `TextView` | `android:layout_height` | `wrap_content` |
| 34 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 35 | `TextView` | `android:text` | `@string/settings_user_display_name` |
| 36 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 37 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 38 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_settings_profile` |
| 39 | `TextView` | `style` | `@style/TextTitle3` |
| 40 | `com.google.android.material.textfield.TextInputLayout` | `android:id` | `@id/til_settings_profile_name` |
| 41 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `0.000000dip` |
| 42 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 43 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 44 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 45 | `com.google.android.material.textfield.TextInputLayout` | `app:counterEnabled` | `true` |
| 46 | `com.google.android.material.textfield.TextInputLayout` | `app:counterMaxLength` | `30` |
| 47 | `com.google.android.material.textfield.TextInputLayout` | `app:counterTextAppearance` | `@style/TextTitle4` |
| 48 | `com.google.android.material.textfield.TextInputLayout` | `app:counterTextColor` | `@color/text_weak` |
| 49 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constrainedWidth` | `true` |
| 50 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 51 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 52 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_settings_profile_name_header` |
| 53 | `com.google.android.material.textfield.TextInputLayout` | `style` | `@style/MaterialEditTextLayout` |
| 54 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/et_settings_profile_name` |
| 55 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 56 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `wrap_content` |
| 57 | `com.google.android.material.textfield.TextInputEditText` | `android:hint` | `Victoria Smith` |
| 58 | `com.google.android.material.textfield.TextInputEditText` | `android:ems` | `10` |
| 59 | `com.google.android.material.textfield.TextInputEditText` | `android:inputType` | `0x00000061` |
| 60 | `com.google.android.material.textfield.TextInputEditText` | `android:imeOptions` | `0x00000005` |
| 61 | `com.google.android.material.textfield.TextInputEditText` | `style` | `@style/MaterialEditText` |
| 62 | `TextView` | `android:textColor` | `@color/text_weak` |
| 63 | `TextView` | `android:id` | `@id/tv_settings_profile_bio_header` |
| 64 | `TextView` | `android:layout_width` | `wrap_content` |
| 65 | `TextView` | `android:layout_height` | `wrap_content` |
| 66 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 67 | `TextView` | `android:text` | `@string/settings_user_about_you` |
| 68 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 69 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 70 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/til_settings_profile_name` |
| 71 | `TextView` | `style` | `@style/TextTitle3` |
| 72 | `com.google.android.material.textfield.TextInputLayout` | `android:id` | `@id/til_settings_profile_bio` |
| 73 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `0.000000dip` |
| 74 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 75 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 76 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 77 | `com.google.android.material.textfield.TextInputLayout` | `app:counterEnabled` | `true` |
| 78 | `com.google.android.material.textfield.TextInputLayout` | `app:counterMaxLength` | `90` |
| 79 | `com.google.android.material.textfield.TextInputLayout` | `app:counterTextAppearance` | `@style/TextTitle4` |
| 80 | `com.google.android.material.textfield.TextInputLayout` | `app:counterTextColor` | `@color/text_weak` |
| 81 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constrainedWidth` | `true` |
| 82 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 83 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 84 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_settings_profile_bio_header` |
| 85 | `com.google.android.material.textfield.TextInputLayout` | `style` | `@style/MaterialEditTextLayout` |
| 86 | `com.google.android.material.textfield.TextInputEditText` | `android:gravity` | `0x00000030` |
| 87 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/et_settings_profile_bio` |
| 88 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 89 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `wrap_content` |
| 90 | `com.google.android.material.textfield.TextInputEditText` | `android:hint` | `@string/settings_user_about_you_hint` |
| 91 | `com.google.android.material.textfield.TextInputEditText` | `android:ems` | `10` |
| 92 | `com.google.android.material.textfield.TextInputEditText` | `android:inputType` | `0x00020001` |
| 93 | `com.google.android.material.textfield.TextInputEditText` | `style` | `@style/MaterialEditText` |
| 94 | `TextView` | `android:textColor` | `@color/text_weak` |
| 95 | `TextView` | `android:id` | `@id/tv_settings_profile_email_header` |
| 96 | `TextView` | `android:layout_width` | `wrap_content` |
| 97 | `TextView` | `android:layout_height` | `wrap_content` |
| 98 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 99 | `TextView` | `android:text` | `@string/settings_user_email` |
| 100 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 101 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 102 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/til_settings_profile_bio` |
| 103 | `TextView` | `style` | `@style/TextTitle3` |
| 104 | `com.google.android.material.textfield.TextInputLayout` | `android:id` | `@id/til_settings_profile_email` |
| 105 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `0.000000dip` |
| 106 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `48.000000dip` |
| 107 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 108 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 109 | `com.google.android.material.textfield.TextInputLayout` | `android:paddingVertical` | `2.000000dip` |
| 110 | `com.google.android.material.textfield.TextInputLayout` | `app:endIconDrawable` | `@drawable/ic_lock_alt_02` |
| 111 | `com.google.android.material.textfield.TextInputLayout` | `app:endIconMode` | `-1` |
| 112 | `com.google.android.material.textfield.TextInputLayout` | `app:endIconTint` | `@color/icon_weak` |
| 113 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constrainedWidth` | `true` |
| 114 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 115 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 116 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_settings_profile_email_header` |
| 117 | `com.google.android.material.textfield.TextInputLayout` | `style` | `@style/MaterialEditTextLayout` |
| 118 | `com.google.android.material.textfield.TextInputEditText` | `android:enabled` | `false` |
| 119 | `com.google.android.material.textfield.TextInputEditText` | `android:textColor` | `@color/text_primary` |
| 120 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/et_settings_profile_email` |
| 121 | `com.google.android.material.textfield.TextInputEditText` | `android:focusable` | `false` |
| 122 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 123 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `wrap_content` |
| 124 | `com.google.android.material.textfield.TextInputEditText` | `android:ems` | `10` |
| 125 | `com.google.android.material.textfield.TextInputEditText` | `android:inputType` | `0x00000021` |
| 126 | `com.google.android.material.textfield.TextInputEditText` | `style` | `@style/MaterialEditText` |
| 127 | `androidx.constraintlayout.widget.Group` | `android:id` | `@id/group_anonymous` |
| 128 | `androidx.constraintlayout.widget.Group` | `android:layout_width` | `0.000000dip` |
| 129 | `androidx.constraintlayout.widget.Group` | `android:layout_height` | `0.000000dip` |
| 130 | `androidx.constraintlayout.widget.Group` | `app:constraint_referenced_ids` | `til_settings_profile_bio,til_settings_profile_email,til_settings_profile_name,tv_settings_profile_bio_header,tv_settings_profile_email_header,tv_settings_profile_name_header,iv_settings_profile_edit_avatar` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@color/primary_default` | `#FF7E4BDE` / `#FF885BDE` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@color/white` | `#FFFFFFFF` |
| `@dimen/profile_header_avatar_size` | `88.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@string/settings_user_about_you` | `About you` / `Über dich` (de) / `Sobre ti` (es) / `À propos de toi` (fr) / `Tentang kamu` (in) / `Su di te` (it) / `O tobie` (pl) / `Sobre você` (pt-rBR) / `О тебе` (ru) / `Hakkında` (tr) |
| `@string/settings_user_about_you_hint` | `Say something about you for the world to see` / `Erzähle der Welt etwas über dich` (de) / `Cuenta algo sobre ti para que el mundo lo vea` (es) / `Dis quelque chose à propos de toi que le monde pourra voir` (fr) / `Ceritakan sesuatu tentang dirimu untuk dilihat dunia` (in) / `Racconta qualcosa di te al mondo` (it) / `Napisz coś o sobie, żeby świat cię poznał` (pl) / `Diga algo sobre você para o mundo ver` (pt-rBR) / `Расскажи немного о себе` (ru) / `Dünyanın görmesi için kendinden bahset` (tr) |
| `@string/settings_user_display_name` | `Your name` / `Dein Name` (de) / `Tu nombre` (es) / `Ton nom` (fr) / `Namamu` (in) / `Il tuo nome` (it) / `Twoje imię` (pl) / `Seu nome` (pt-rBR) / `Твоё имя` (ru) / `Adın` (tr) |
| `@string/settings_user_email` | `Email` / `E-Mail` (de) / `Email` (es) / `Email` (fr) / `Email` (in) / `Email` (it) / `E-mail` (pl) / `E-mail` (pt-rBR) / `Email` (ru) / `E-posta` (tr) |
| `@style/CircularImageView` | `[{'attr': 'attr.cornerFamily', 'attr_id': '0x7F0401A1', 'value': '0', 'value_type': 'int_dec'}, {'attr': 'attr.cornerSize', 'attr_id': '0x7F0401A8', 'value': '50.000001%', 'value_type': 'fraction'}]` |
| `@style/MaterialEditText` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}, {'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_weak', 'value_type': 'reference'}, {'attr': 'android:padding', 'attr_id': '0x010100D5', 'value': '@dimen/spacing_s', 'value_type': 'reference'}]` |
| `@style/MaterialEditTextLayout` | `[{'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_disabled', 'value_type': 'reference'}, {'attr': 'android:imeOptions', 'attr_id': '0x01010264', 'value': '0x00000006', 'value_type': 'int_hex'}, {'attr': 'attr.boxBackgroundColor', 'attr_id': '0x7F040099', 'value': '@color/background_secondary', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomEnd', 'attr_id': '0x7F04009C', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomStart', 'attr_id': '0x7F04009D', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopEnd', 'attr_id': '0x7F04009E', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopStart', 'attr_id': '0x7F04009F', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxStrokeColor', 'attr_id': '0x7F0400A0', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.endIconTint', 'attr_id': '0x7F040236', 'value': '@color/icon_weak', 'value_type': 'reference'}, {'attr': 'attr.hintEnabled', 'attr_id': '0x7F0402E7', 'value': 'false', 'value_type': 'int_boolean'}, {'attr': 'attr.strokeColor', 'attr_id': '0x7F040586', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.strokeWidth', 'attr_id': '0x7F040587', 'value': '1.000000dip', 'value_type': 'dimension'}]` |
| `@style/TextTitle3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '12.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '15.599977sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextTitle4` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '10.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '2.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/et_settings_profile_bio
@id/et_settings_profile_email
@id/et_settings_profile_name
@id/group_anonymous
@id/iv_settings_profile
@id/iv_settings_profile_edit_avatar
@id/til_settings_profile_bio
@id/til_settings_profile_email
@id/til_settings_profile_name
@id/tv_settings_profile_bio_header
@id/tv_settings_profile_email_header
@id/tv_settings_profile_name_header
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.settings.SettingsActivity
com.getmimo.ui.settings.SettingsFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/settings_fragment.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="wrap_content">
  <com.google.android.material.imageview.ShapeableImageView android:layout_gravity="0x00000001" android:id="@id/iv_settings_profile" android:layout_width="@dimen/profile_header_avatar_size" android:layout_height="@dimen/profile_header_avatar_size" android:scaleType="centerCrop" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:shapeAppearanceOverlay="@style/CircularImageView"/>
  <com.google.android.material.imageview.ShapeableImageView android:layout_gravity="0x00000001" android:id="@id/iv_settings_profile_edit_avatar" android:background="@color/primary_default" android:padding="1.000000dip" android:layout_width="34.000000dip" android:layout_height="34.000000dip" android:foreground="?attr/selectableItemBackgroundBorderless" android:scaleType="centerInside" app:contentPadding="8.000000dip" app:layout_constraintCircle="@id/iv_settings_profile" app:layout_constraintCircleAngle="135.000000" app:layout_constraintCircleRadius="45.000000dip" app:shapeAppearanceOverlay="@style/CircularImageView" app:srcCompat="@drawable/ic_edit" app:strokeColor="@color/background_primary" app:strokeWidth="2.000000dip" app:tint="@color/white"/>
  <TextView android:textColor="@color/text_weak" android:id="@id/tv_settings_profile_name_header" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/settings_user_display_name" android:layout_marginStart="@dimen/spacing_m" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_settings_profile" style="@style/TextTitle3"/>
  <com.google.android.material.textfield.TextInputLayout android:id="@id/til_settings_profile_name" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:layout_marginHorizontal="@dimen/spacing_m" app:counterEnabled="true" app:counterMaxLength="30" app:counterTextAppearance="@style/TextTitle4" app:counterTextColor="@color/text_weak" app:layout_constrainedWidth="true" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_settings_profile_name_header" style="@style/MaterialEditTextLayout">
    <com.google.android.material.textfield.TextInputEditText android:id="@id/et_settings_profile_name" android:layout_width="match_parent" android:layout_height="wrap_content" android:hint="Victoria Smith" android:ems="10" android:inputType="0x00000061" android:imeOptions="0x00000005" style="@style/MaterialEditText"/>
  </com.google.android.material.textfield.TextInputLayout>
  <TextView android:textColor="@color/text_weak" android:id="@id/tv_settings_profile_bio_header" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:text="@string/settings_user_about_you" android:layout_marginStart="@dimen/spacing_m" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/til_settings_profile_name" style="@style/TextTitle3"/>
  <com.google.android.material.textfield.TextInputLayout android:id="@id/til_settings_profile_bio" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:layout_marginHorizontal="@dimen/spacing_m" app:counterEnabled="true" app:counterMaxLength="90" app:counterTextAppearance="@style/TextTitle4" app:counterTextColor="@color/text_weak" app:layout_constrainedWidth="true" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_settings_profile_bio_header" style="@style/MaterialEditTextLayout">
    <com.google.android.material.textfield.TextInputEditText android:gravity="0x00000030" android:id="@id/et_settings_profile_bio" android:layout_width="match_parent" android:layout_height="wrap_content" android:hint="@string/settings_user_about_you_hint" android:ems="10" android:inputType="0x00020001" style="@style/MaterialEditText"/>
  </com.google.android.material.textfield.TextInputLayout>
  <TextView android:textColor="@color/text_weak" android:id="@id/tv_settings_profile_email_header" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:text="@string/settings_user_email" android:layout_marginStart="@dimen/spacing_m" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/til_settings_profile_bio" style="@style/TextTitle3"/>
  <com.google.android.material.textfield.TextInputLayout android:id="@id/til_settings_profile_email" android:layout_width="0.000000dip" android:layout_height="48.000000dip" android:layout_marginTop="@dimen/spacing_xs" android:layout_marginHorizontal="@dimen/spacing_m" android:paddingVertical="2.000000dip" app:endIconDrawable="@drawable/ic_lock_alt_02" app:endIconMode="-1" app:endIconTint="@color/icon_weak" app:layout_constrainedWidth="true" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_settings_profile_email_header" style="@style/MaterialEditTextLayout">
    <com.google.android.material.textfield.TextInputEditText android:enabled="false" android:textColor="@color/text_primary" android:id="@id/et_settings_profile_email" android:focusable="false" android:layout_width="match_parent" android:layout_height="wrap_content" android:ems="10" android:inputType="0x00000021" style="@style/MaterialEditText"/>
  </com.google.android.material.textfield.TextInputLayout>
  <androidx.constraintlayout.widget.Group android:id="@id/group_anonymous" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:constraint_referenced_ids="til_settings_profile_bio,til_settings_profile_email,til_settings_profile_name,tv_settings_profile_bio_header,tv_settings_profile_email_header,tv_settings_profile_name_header,iv_settings_profile_edit_avatar"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
