# پروندهٔ لایه — `res/layout/invitations_overview_bottomsheet_invite_card.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/invitations_overview_bottomsheet_invite_card.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/invitations_overview_bottomsheet_invite_card.xml`](../../SOURCE/res/layout/invitations_overview_bottomsheet_invite_card.xml) |
| SHA-256 دیکد | `1b49d1444f899c5d97bff8f9ff2a7081a0a45e6b7736476f2caec1372aed71cf` |
| ریشه | `androidx.cardview.widget.CardView` |
| تعداد گره | 7 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 26 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.cardview.widget.CardView
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ TextView  #@id/tv_share_link_card_title
      ├─ com.google.android.material.textfield.TextInputLayout  #@id/layout_share_link_text_variant
      │  └─ com.google.android.material.textfield.TextInputEditText  #@id/tv_invite_link_variant
      ├─ com.google.android.material.button.MaterialButton  #@id/btn_invite_friends_whatsapp
      └─ com.google.android.material.button.MaterialButton  #@id/btn_invite_friends_message
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.cardview.widget.CardView` | `android:layout_width` | `match_parent` |
| 2 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 3 | `androidx.cardview.widget.CardView` | `app:cardBackgroundColor` | `@color/card_enabled` |
| 4 | `androidx.cardview.widget.CardView` | `app:cardCornerRadius` | `@dimen/cardview_corner_radius_large` |
| 5 | `androidx.cardview.widget.CardView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 6 | `androidx.cardview.widget.CardView` | `app:layout_constraintStart_toStartOf` | `0` |
| 7 | `androidx.cardview.widget.CardView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_invitation_overview_description` |
| 8 | `androidx.cardview.widget.CardView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 9 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:padding` | `@dimen/spacing_m` |
| 10 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 11 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 12 | `TextView` | `android:textColor` | `@color/text_primary` |
| 13 | `TextView` | `android:id` | `@id/tv_share_link_card_title` |
| 14 | `TextView` | `android:layout_width` | `wrap_content` |
| 15 | `TextView` | `android:layout_height` | `wrap_content` |
| 16 | `TextView` | `android:text` | `@string/friends_share_link` |
| 17 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 18 | `TextView` | `app:layout_constraintHorizontal_bias` | `0.000000` |
| 19 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 20 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 21 | `TextView` | `style` | `@style/TextTitle2` |
| 22 | `com.google.android.material.textfield.TextInputLayout` | `android:id` | `@id/layout_share_link_text_variant` |
| 23 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `0.000000dip` |
| 24 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 25 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 26 | `com.google.android.material.textfield.TextInputLayout` | `app:endIconDrawable` | `@drawable/ic_copy` |
| 27 | `com.google.android.material.textfield.TextInputLayout` | `app:endIconMode` | `-1` |
| 28 | `com.google.android.material.textfield.TextInputLayout` | `app:endIconTint` | `@color/icon_weak` |
| 29 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constrainedWidth` | `true` |
| 30 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 31 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 32 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_share_link_card_title` |
| 33 | `com.google.android.material.textfield.TextInputLayout` | `style` | `@style/MaterialEditTextLayout` |
| 34 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/tv_invite_link_variant` |
| 35 | `com.google.android.material.textfield.TextInputEditText` | `android:focusable` | `false` |
| 36 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 37 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `wrap_content` |
| 38 | `com.google.android.material.textfield.TextInputEditText` | `android:inputType` | `0x00000000` |
| 39 | `com.google.android.material.textfield.TextInputEditText` | `style` | `@style/MaterialEditText` |
| 40 | `com.google.android.material.button.MaterialButton` | `android:gravity` | `0x00000011` |
| 41 | `com.google.android.material.button.MaterialButton` | `android:id` | `@id/btn_invite_friends_whatsapp` |
| 42 | `com.google.android.material.button.MaterialButton` | `android:layout_width` | `0.000000dip` |
| 43 | `com.google.android.material.button.MaterialButton` | `android:layout_height` | `wrap_content` |
| 44 | `com.google.android.material.button.MaterialButton` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 45 | `com.google.android.material.button.MaterialButton` | `android:text` | `@string/friends_share_link_invite_friends_whatsapp` |
| 46 | `com.google.android.material.button.MaterialButton` | `android:layout_marginEnd` | `@dimen/spacing_xxs` |
| 47 | `com.google.android.material.button.MaterialButton` | `android:backgroundTint` | `@color/support_green` |
| 48 | `com.google.android.material.button.MaterialButton` | `app:icon` | `@drawable/ic_whatsapp` |
| 49 | `com.google.android.material.button.MaterialButton` | `app:layout_constraintEnd_toStartOf` | `@id/btn_invite_friends_message` |
| 50 | `com.google.android.material.button.MaterialButton` | `app:layout_constraintStart_toStartOf` | `0` |
| 51 | `com.google.android.material.button.MaterialButton` | `app:layout_constraintTop_toBottomOf` | `@id/layout_share_link_text_variant` |
| 52 | `com.google.android.material.button.MaterialButton` | `app:layout_constraintWidth_max` | `360.000000dip` |
| 53 | `com.google.android.material.button.MaterialButton` | `style` | `@style/MaterialButton.Secondary` |
| 54 | `com.google.android.material.button.MaterialButton` | `android:id` | `@id/btn_invite_friends_message` |
| 55 | `com.google.android.material.button.MaterialButton` | `android:layout_width` | `0.000000dip` |
| 56 | `com.google.android.material.button.MaterialButton` | `android:layout_height` | `wrap_content` |
| 57 | `com.google.android.material.button.MaterialButton` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 58 | `com.google.android.material.button.MaterialButton` | `android:text` | `@string/friends_share_link_invite_friends_message` |
| 59 | `com.google.android.material.button.MaterialButton` | `android:layout_marginStart` | `@dimen/spacing_xxs` |
| 60 | `com.google.android.material.button.MaterialButton` | `android:backgroundTint` | `@color/support_blue` |
| 61 | `com.google.android.material.button.MaterialButton` | `app:icon` | `@drawable/ic_chat_bubble` |
| 62 | `com.google.android.material.button.MaterialButton` | `app:layout_constraintEnd_toEndOf` | `0` |
| 63 | `com.google.android.material.button.MaterialButton` | `app:layout_constraintStart_toEndOf` | `@id/btn_invite_friends_whatsapp` |
| 64 | `com.google.android.material.button.MaterialButton` | `app:layout_constraintTop_toBottomOf` | `@id/layout_share_link_text_variant` |
| 65 | `com.google.android.material.button.MaterialButton` | `app:layout_constraintWidth_max` | `360.000000dip` |
| 66 | `com.google.android.material.button.MaterialButton` | `style` | `@style/MaterialButton.Secondary` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/card_enabled` | `#FFFFFFFF` / `#FF3F4273` (night) |
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@color/support_blue` | `#FF3890FA` / `#FF00C5FF` (night) |
| `@color/support_green` | `#FF66BC5A` / `#FF78D86B` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/cardview_corner_radius_large` | `12.000000dip` |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@string/friends_share_link` | `Share your link` / `Teile deinen Link` (de) / `Comparte tu enlace` (es) / `Partager ton lien` (fr) / `Bagikan linkmu` (in) / `Condividi il tuo link` (it) / `Udostępnij swój link` (pl) / `Compartilhe seu link` (pt-rBR) / `Поделиться ссылкой` (ru) / `Bağlantını paylaş` (tr) |
| `@string/friends_share_link_invite_friends_message` | `Message` / `Nachricht` (de) / `Mensaje` (es) / `Message` (fr) / `Pesan` (in) / `Messaggi` (it) / `Wiadomość` (pl) / `Mensagem` (pt-rBR) / `Message` (ru) / `Mesaj` (tr) |
| `@string/friends_share_link_invite_friends_whatsapp` | `Whatsapp` / `WhatsApp` (de) / `Whatsapp` (es) / `WhatsApp` (fr) / `Whatsapp` (in) / `Whatsapp` (it) / `WhatsApp` (pl) / `Whatsapp` (pt-rBR) / `Whatsapp` (ru) / `Whatsapp` (tr) |
| `@style/MaterialButton.Secondary` | `[{'attr': 'android:textAppearance', 'attr_id': '0x01010034', 'value': '@style/TextButton2', 'value_type': 'reference'}, {'attr': 'android:minWidth', 'attr_id': '0x0101013F', 'value': '120.000000dip', 'value_type': 'dimension'}, {'attr': 'android:minHeight', 'attr_id': '0x01010140', 'value': '40.000000dip', 'value_type': 'dimension'}, {'attr': 'attr.iconSize', 'attr_id': '0x7F0402F8', 'value': '@dimen/icon_size_small', 'value_type': 'reference'}]` |
| `@style/MaterialEditText` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}, {'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_weak', 'value_type': 'reference'}, {'attr': 'android:padding', 'attr_id': '0x010100D5', 'value': '@dimen/spacing_s', 'value_type': 'reference'}]` |
| `@style/MaterialEditTextLayout` | `[{'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_disabled', 'value_type': 'reference'}, {'attr': 'android:imeOptions', 'attr_id': '0x01010264', 'value': '0x00000006', 'value_type': 'int_hex'}, {'attr': 'attr.boxBackgroundColor', 'attr_id': '0x7F040099', 'value': '@color/background_secondary', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomEnd', 'attr_id': '0x7F04009C', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomStart', 'attr_id': '0x7F04009D', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopEnd', 'attr_id': '0x7F04009E', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopStart', 'attr_id': '0x7F04009F', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxStrokeColor', 'attr_id': '0x7F0400A0', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.endIconTint', 'attr_id': '0x7F040236', 'value': '@color/icon_weak', 'value_type': 'reference'}, {'attr': 'attr.hintEnabled', 'attr_id': '0x7F0402E7', 'value': 'false', 'value_type': 'int_boolean'}, {'attr': 'attr.strokeColor', 'attr_id': '0x7F040586', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.strokeWidth', 'attr_id': '0x7F040587', 'value': '1.000000dip', 'value_type': 'dimension'}]` |
| `@style/TextTitle2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_invite_friends_message
@id/btn_invite_friends_whatsapp
@id/layout_share_link_text_variant
@id/tv_invite_link_variant
@id/tv_share_link_card_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/invitations_overview_bottomsheet.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.cardview.widget.CardView xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_width="match_parent" android:layout_height="wrap_content" app:cardBackgroundColor="@color/card_enabled" app:cardCornerRadius="@dimen/cardview_corner_radius_large" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_invitation_overview_description" app:layout_constraintWidth_max="@dimen/general_max_width">
  <androidx.constraintlayout.widget.ConstraintLayout android:padding="@dimen/spacing_m" android:layout_width="match_parent" android:layout_height="match_parent">
    <TextView android:textColor="@color/text_primary" android:id="@id/tv_share_link_card_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/friends_share_link" app:layout_constraintEnd_toEndOf="0" app:layout_constraintHorizontal_bias="0.000000" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextTitle2"/>
    <com.google.android.material.textfield.TextInputLayout android:id="@id/layout_share_link_text_variant" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" app:endIconDrawable="@drawable/ic_copy" app:endIconMode="-1" app:endIconTint="@color/icon_weak" app:layout_constrainedWidth="true" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_share_link_card_title" style="@style/MaterialEditTextLayout">
      <com.google.android.material.textfield.TextInputEditText android:id="@id/tv_invite_link_variant" android:focusable="false" android:layout_width="match_parent" android:layout_height="wrap_content" android:inputType="0x00000000" style="@style/MaterialEditText"/>
    </com.google.android.material.textfield.TextInputLayout>
    <com.google.android.material.button.MaterialButton android:gravity="0x00000011" android:id="@id/btn_invite_friends_whatsapp" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:text="@string/friends_share_link_invite_friends_whatsapp" android:layout_marginEnd="@dimen/spacing_xxs" android:backgroundTint="@color/support_green" app:icon="@drawable/ic_whatsapp" app:layout_constraintEnd_toStartOf="@id/btn_invite_friends_message" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/layout_share_link_text_variant" app:layout_constraintWidth_max="360.000000dip" style="@style/MaterialButton.Secondary"/>
    <com.google.android.material.button.MaterialButton android:id="@id/btn_invite_friends_message" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:text="@string/friends_share_link_invite_friends_message" android:layout_marginStart="@dimen/spacing_xxs" android:backgroundTint="@color/support_blue" app:icon="@drawable/ic_chat_bubble" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/btn_invite_friends_whatsapp" app:layout_constraintTop_toBottomOf="@id/layout_share_link_text_variant" app:layout_constraintWidth_max="360.000000dip" style="@style/MaterialButton.Secondary"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
</androidx.cardview.widget.CardView>
```
