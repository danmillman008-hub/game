# پروندهٔ لایه — `res/layout/invitations_overview_bottomsheet.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/invitations_overview_bottomsheet.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/invitations_overview_bottomsheet.xml`](../../SOURCE/res/layout/invitations_overview_bottomsheet.xml) |
| SHA-256 دیکد | `9769592de990a2b54ce999a8aef97977c5565bc2f8fb81abd93a4ee0c8aaaa27` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 15 |
| تعداد شناسه | 12 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 8 |
| ارجاع به منابع | 31 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ ImageView  #@id/iv_invitation_overview
   ├─ TextView  #@id/tv_invitation_overview_title
   ├─ TextView  #@id/tv_invitation_overview_description
   ├─ include  #@id/card_share_link
   └─ androidx.cardview.widget.CardView  #@id/card_share_info
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ TextView  #@id/tv_invites_card_title
         ├─ ImageView  #@id/iv_accepted_invitations_icon
         ├─ TextView
         ├─ TextView  #@id/tv_accepted_invitations_nb
         ├─ ImageView  #@id/iv_free_days_icon
         ├─ TextView  #@id/tv_free_days_title
         ├─ TextView  #@id/tv_free_days_nb
         └─ androidx.constraintlayout.widget.Group  #@id/group_free_days
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 3 | `ImageView` | `android:id` | `@id/iv_invitation_overview` |
| 4 | `ImageView` | `android:layout_width` | `wrap_content` |
| 5 | `ImageView` | `android:layout_height` | `wrap_content` |
| 6 | `ImageView` | `android:layout_marginTop` | `39.000000dip` |
| 7 | `ImageView` | `android:maxWidth` | `@dimen/general_max_width` |
| 8 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 9 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 10 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 11 | `TextView` | `android:textColor` | `@color/text_primary` |
| 12 | `TextView` | `android:gravity` | `0x00000011` |
| 13 | `TextView` | `android:id` | `@id/tv_invitation_overview_title` |
| 14 | `TextView` | `android:layout_width` | `0.000000dip` |
| 15 | `TextView` | `android:layout_height` | `wrap_content` |
| 16 | `TextView` | `android:layout_marginTop` | `20.000000dip` |
| 17 | `TextView` | `android:layout_marginStart` | `28.000000dip` |
| 18 | `TextView` | `android:layout_marginEnd` | `28.000000dip` |
| 19 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 20 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 21 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_invitation_overview` |
| 22 | `TextView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 23 | `TextView` | `style` | `@style/TextH1` |
| 24 | `TextView` | `android:textColor` | `@color/text_weak` |
| 25 | `TextView` | `android:gravity` | `0x00000011` |
| 26 | `TextView` | `android:id` | `@id/tv_invitation_overview_description` |
| 27 | `TextView` | `android:layout_width` | `0.000000dip` |
| 28 | `TextView` | `android:layout_height` | `wrap_content` |
| 29 | `TextView` | `android:layout_marginTop` | `16.000000dip` |
| 30 | `TextView` | `android:layout_marginStart` | `28.000000dip` |
| 31 | `TextView` | `android:layout_marginEnd` | `28.000000dip` |
| 32 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 33 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 34 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_invitation_overview_title` |
| 35 | `TextView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 36 | `TextView` | `style` | `@style/TextP1` |
| 37 | `include` | `android:id` | `@id/card_share_link` |
| 38 | `include` | `android:background` | `@color/card_enabled` |
| 39 | `include` | `android:layout_width` | `0.000000dip` |
| 40 | `include` | `android:layout_height` | `wrap_content` |
| 41 | `include` | `android:layout_marginTop` | `40.000000dip` |
| 42 | `include` | `android:layout_marginStart` | `12.000000dip` |
| 43 | `include` | `android:layout_marginEnd` | `12.000000dip` |
| 44 | `include` | `app:layout_constraintEnd_toEndOf` | `0` |
| 45 | `include` | `app:layout_constraintStart_toStartOf` | `0` |
| 46 | `include` | `app:layout_constraintTop_toBottomOf` | `@id/tv_invitation_overview_description` |
| 47 | `include` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 48 | `include` | `layout` | `@layout/invitations_overview_bottomsheet_invite_card` |
| 49 | `androidx.cardview.widget.CardView` | `android:id` | `@id/card_share_info` |
| 50 | `androidx.cardview.widget.CardView` | `android:layout_width` | `0.000000dip` |
| 51 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 52 | `androidx.cardview.widget.CardView` | `android:layout_marginTop` | `12.000000dip` |
| 53 | `androidx.cardview.widget.CardView` | `android:layout_marginBottom` | `12.000000dip` |
| 54 | `androidx.cardview.widget.CardView` | `android:layout_marginStart` | `12.000000dip` |
| 55 | `androidx.cardview.widget.CardView` | `android:layout_marginEnd` | `12.000000dip` |
| 56 | `androidx.cardview.widget.CardView` | `app:cardBackgroundColor` | `@color/card_enabled` |
| 57 | `androidx.cardview.widget.CardView` | `app:cardCornerRadius` | `@dimen/cardview_corner_radius_large` |
| 58 | `androidx.cardview.widget.CardView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 59 | `androidx.cardview.widget.CardView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 60 | `androidx.cardview.widget.CardView` | `app:layout_constraintStart_toStartOf` | `0` |
| 61 | `androidx.cardview.widget.CardView` | `app:layout_constraintTop_toBottomOf` | `@id/card_share_link` |
| 62 | `androidx.cardview.widget.CardView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 63 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingTop` | `@dimen/spacing_m` |
| 64 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingBottom` | `@dimen/spacing_l` |
| 65 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 66 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 67 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingHorizontal` | `@dimen/spacing_m` |
| 68 | `TextView` | `android:textColor` | `@color/text_primary` |
| 69 | `TextView` | `android:id` | `@id/tv_invites_card_title` |
| 70 | `TextView` | `android:layout_width` | `wrap_content` |
| 71 | `TextView` | `android:layout_height` | `wrap_content` |
| 72 | `TextView` | `android:text` | `@string/friends_your_invites` |
| 73 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 74 | `TextView` | `app:layout_constraintHorizontal_bias` | `0.000000` |
| 75 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 76 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 77 | `TextView` | `style` | `@style/TextTitle2` |
| 78 | `ImageView` | `android:id` | `@id/iv_accepted_invitations_icon` |
| 79 | `ImageView` | `android:layout_width` | `24.000000dip` |
| 80 | `ImageView` | `android:layout_height` | `24.000000dip` |
| 81 | `ImageView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 82 | `ImageView` | `android:src` | `@drawable/ic_user_circle` |
| 83 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 84 | `ImageView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_invites_card_title` |
| 85 | `ImageView` | `app:tint` | `@color/icon_weak` |
| 86 | `TextView` | `android:textColor` | `@color/text_primary` |
| 87 | `TextView` | `android:layout_width` | `wrap_content` |
| 88 | `TextView` | `android:layout_height` | `wrap_content` |
| 89 | `TextView` | `android:text` | `@string/friends_invite_accepted_invitations` |
| 90 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_xs` |
| 91 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_accepted_invitations_icon` |
| 92 | `TextView` | `app:layout_constraintEnd_toStartOf` | `@id/tv_accepted_invitations_nb` |
| 93 | `TextView` | `app:layout_constraintHorizontal_bias` | `0.000000` |
| 94 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_accepted_invitations_icon` |
| 95 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/iv_accepted_invitations_icon` |
| 96 | `TextView` | `style` | `@style/TextP1` |
| 97 | `TextView` | `android:textColor` | `@color/text_primary` |
| 98 | `TextView` | `android:id` | `@id/tv_accepted_invitations_nb` |
| 99 | `TextView` | `android:layout_width` | `wrap_content` |
| 100 | `TextView` | `android:layout_height` | `wrap_content` |
| 101 | `TextView` | `android:layout_marginEnd` | `9.000000dip` |
| 102 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_accepted_invitations_icon` |
| 103 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 104 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/iv_accepted_invitations_icon` |
| 105 | `TextView` | `style` | `@style/TextH2` |
| 106 | `ImageView` | `android:id` | `@id/iv_free_days_icon` |
| 107 | `ImageView` | `android:layout_width` | `24.000000dip` |
| 108 | `ImageView` | `android:layout_height` | `24.000000dip` |
| 109 | `ImageView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 110 | `ImageView` | `android:src` | `@drawable/ic_trophy` |
| 111 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 112 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 113 | `ImageView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_accepted_invitations_icon` |
| 114 | `ImageView` | `app:tint` | `@color/icon_weak` |
| 115 | `TextView` | `android:textColor` | `@color/text_primary` |
| 116 | `TextView` | `android:id` | `@id/tv_free_days_title` |
| 117 | `TextView` | `android:layout_width` | `wrap_content` |
| 118 | `TextView` | `android:layout_height` | `wrap_content` |
| 119 | `TextView` | `android:text` | `@string/friends_invite_free_days_mimo_pro` |
| 120 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_xs` |
| 121 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_free_days_icon` |
| 122 | `TextView` | `app:layout_constraintEnd_toStartOf` | `@id/tv_free_days_nb` |
| 123 | `TextView` | `app:layout_constraintHorizontal_bias` | `0.000000` |
| 124 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_free_days_icon` |
| 125 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/iv_free_days_icon` |
| 126 | `TextView` | `style` | `@style/TextP1` |
| 127 | `TextView` | `android:textColor` | `@color/text_primary` |
| 128 | `TextView` | `android:id` | `@id/tv_free_days_nb` |
| 129 | `TextView` | `android:layout_width` | `wrap_content` |
| 130 | `TextView` | `android:layout_height` | `wrap_content` |
| 131 | `TextView` | `android:layout_marginEnd` | `9.000000dip` |
| 132 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_free_days_icon` |
| 133 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 134 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/iv_free_days_icon` |
| 135 | `TextView` | `style` | `@style/TextH2` |
| 136 | `androidx.constraintlayout.widget.Group` | `android:id` | `@id/group_free_days` |
| 137 | `androidx.constraintlayout.widget.Group` | `android:visibility` | `gone` |
| 138 | `androidx.constraintlayout.widget.Group` | `android:layout_width` | `match_parent` |
| 139 | `androidx.constraintlayout.widget.Group` | `android:layout_height` | `match_parent` |
| 140 | `androidx.constraintlayout.widget.Group` | `app:constraint_referenced_ids` | `tv_free_days_nb, tv_free_days_title, iv_free_days_icon` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/card_enabled` | `#FFFFFFFF` / `#FF3F4273` (night) |
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/cardview_corner_radius_large` | `12.000000dip` |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@string/friends_invite_accepted_invitations` | `Accepted invitations` / `Angenommene Einladungen` (de) / `Invitaciones aceptadas` (es) / `Invitations acceptées` (fr) / `Undangan diterima` (in) / `Inviti accettati` (it) / `Przyjęte zaproszenia` (pl) / `Convites aceitos` (pt-rBR) / `Принятые приглашения` (ru) / `Kabul edilen davetler` (tr) |
| `@string/friends_invite_free_days_mimo_pro` | `Free days of Mimo Pro` / `Kostenlose Tage Mimo Pro` (de) / `Días gratis de Mimo Pro` (es) / `Jours gratuits de Mimo Pro` (fr) / `Hari gratis Mimo Pro` (in) / `Giorni gratis di Mimo Pro` (it) / `Darmowe dni Mimo Pro` (pl) / `Dias grátis de Mimo Pro` (pt-rBR) / `Бесплатные дни Mimo Pro` (ru) / `Ücretsiz Mimo Pro günleri` (tr) |
| `@string/friends_your_invites` | `Your invites` / `Deine Einladungen` (de) / `Tus invitaciones` (es) / `Tes invités` (fr) / `Undanganmu` (in) / `I tuoi inviti` (it) / `Twoje zaproszenia` (pl) / `Seus convites` (pt-rBR) / `Приглашённые друзья` (ru) / `Davetlerin` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextH2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '26.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextTitle2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/card_share_info
@id/card_share_link
@id/group_free_days
@id/iv_accepted_invitations_icon
@id/iv_free_days_icon
@id/iv_invitation_overview
@id/tv_accepted_invitations_nb
@id/tv_free_days_nb
@id/tv_free_days_title
@id/tv_invitation_overview_description
@id/tv_invitation_overview_title
@id/tv_invites_card_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
0
0.000000dip
12.000000dip
40.000000dip
@dimen/general_max_width
@id/tv_invitation_overview_description
@layout/invitations_overview_bottomsheet_invite_card
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/invite_overview_bottomsheet_dialog.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="wrap_content">
  <ImageView android:id="@id/iv_invitation_overview" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="39.000000dip" android:maxWidth="@dimen/general_max_width" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_invitation_overview_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="20.000000dip" android:layout_marginStart="28.000000dip" android:layout_marginEnd="28.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_invitation_overview" app:layout_constraintWidth_max="@dimen/general_max_width" style="@style/TextH1"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_invitation_overview_description" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip" android:layout_marginStart="28.000000dip" android:layout_marginEnd="28.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_invitation_overview_title" app:layout_constraintWidth_max="@dimen/general_max_width" style="@style/TextP1"/>
  <include android:id="@id/card_share_link" android:background="@color/card_enabled" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="40.000000dip" android:layout_marginStart="12.000000dip" android:layout_marginEnd="12.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_invitation_overview_description" app:layout_constraintWidth_max="@dimen/general_max_width" layout="@layout/invitations_overview_bottomsheet_invite_card"/>
  <androidx.cardview.widget.CardView android:id="@id/card_share_info" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="12.000000dip" android:layout_marginBottom="12.000000dip" android:layout_marginStart="12.000000dip" android:layout_marginEnd="12.000000dip" app:cardBackgroundColor="@color/card_enabled" app:cardCornerRadius="@dimen/cardview_corner_radius_large" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/card_share_link" app:layout_constraintWidth_max="@dimen/general_max_width">
    <androidx.constraintlayout.widget.ConstraintLayout android:paddingTop="@dimen/spacing_m" android:paddingBottom="@dimen/spacing_l" android:layout_width="match_parent" android:layout_height="match_parent" android:paddingHorizontal="@dimen/spacing_m">
      <TextView android:textColor="@color/text_primary" android:id="@id/tv_invites_card_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/friends_your_invites" app:layout_constraintEnd_toEndOf="0" app:layout_constraintHorizontal_bias="0.000000" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextTitle2"/>
      <ImageView android:id="@id/iv_accepted_invitations_icon" android:layout_width="24.000000dip" android:layout_height="24.000000dip" android:layout_marginTop="@dimen/spacing_m" android:src="@drawable/ic_user_circle" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_invites_card_title" app:tint="@color/icon_weak"/>
      <TextView android:textColor="@color/text_primary" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/friends_invite_accepted_invitations" android:layout_marginHorizontal="@dimen/spacing_xs" app:layout_constraintBottom_toBottomOf="@id/iv_accepted_invitations_icon" app:layout_constraintEnd_toStartOf="@id/tv_accepted_invitations_nb" app:layout_constraintHorizontal_bias="0.000000" app:layout_constraintStart_toEndOf="@id/iv_accepted_invitations_icon" app:layout_constraintTop_toTopOf="@id/iv_accepted_invitations_icon" style="@style/TextP1"/>
      <TextView android:textColor="@color/text_primary" android:id="@id/tv_accepted_invitations_nb" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginEnd="9.000000dip" app:layout_constraintBottom_toBottomOf="@id/iv_accepted_invitations_icon" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="@id/iv_accepted_invitations_icon" style="@style/TextH2"/>
      <ImageView android:id="@id/iv_free_days_icon" android:layout_width="24.000000dip" android:layout_height="24.000000dip" android:layout_marginTop="@dimen/spacing_m" android:src="@drawable/ic_trophy" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_accepted_invitations_icon" app:tint="@color/icon_weak"/>
      <TextView android:textColor="@color/text_primary" android:id="@id/tv_free_days_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/friends_invite_free_days_mimo_pro" android:layout_marginHorizontal="@dimen/spacing_xs" app:layout_constraintBottom_toBottomOf="@id/iv_free_days_icon" app:layout_constraintEnd_toStartOf="@id/tv_free_days_nb" app:layout_constraintHorizontal_bias="0.000000" app:layout_constraintStart_toEndOf="@id/iv_free_days_icon" app:layout_constraintTop_toTopOf="@id/iv_free_days_icon" style="@style/TextP1"/>
      <TextView android:textColor="@color/text_primary" android:id="@id/tv_free_days_nb" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginEnd="9.000000dip" app:layout_constraintBottom_toBottomOf="@id/iv_free_days_icon" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="@id/iv_free_days_icon" style="@style/TextH2"/>
      <androidx.constraintlayout.widget.Group android:id="@id/group_free_days" android:visibility="gone" android:layout_width="match_parent" android:layout_height="match_parent" app:constraint_referenced_ids="tv_free_days_nb, tv_free_days_title, iv_free_days_icon"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </androidx.cardview.widget.CardView>
</androidx.constraintlayout.widget.ConstraintLayout>
```
