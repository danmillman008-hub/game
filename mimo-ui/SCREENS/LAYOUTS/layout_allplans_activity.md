# پروندهٔ لایه — `res/layout/allplans_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/allplans_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/allplans_activity.xml`](../../SOURCE/res/layout/allplans_activity.xml) |
| SHA-256 دیکد | `285499de4ac024b72762fd647d0c3278c6343514990ba2fd781bd9b1c84e056c` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 14 |
| تعداد شناسه | 14 |
| تگ‌های استفاده‌شده | 10 |
| ویوهای سفارشی `com.getmimo` | 2 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 37 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_in_app_purchase
   ├─ androidx.viewpager2.widget.ViewPager2  #@id/vp_in_app
   ├─ com.getmimo.ui.common.ViewPagerIndicator  #@id/vpi_in_app
   ├─ com.getmimo.ui.iap.allplans.SubscriptionPodiumButton  #@id/in_app_button_podium_1
   ├─ com.getmimo.ui.iap.allplans.SubscriptionPodiumButton  #@id/in_app_button_podium_2
   ├─ TextView  #@id/tv_in_app_purchase_auto_renew
   ├─ ProgressBar  #@id/pb_in_app
   ├─ ImageView  #@id/iv_in_app_purchase_error
   ├─ TextView  #@id/tv_in_app_purchase_error_title
   ├─ TextView  #@id/tv_in_app_purchase_error_description
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_in_app_purchase_error
   ├─ ImageButton  #@id/btn_in_app_close
   ├─ androidx.constraintlayout.widget.Group  #@id/group_in_app_purchase_error
   └─ androidx.constraintlayout.widget.Group  #@id/group_in_app_purchase_screen
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_in_app_purchase` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 5 | `androidx.viewpager2.widget.ViewPager2` | `android:id` | `@id/vp_in_app` |
| 6 | `androidx.viewpager2.widget.ViewPager2` | `android:clipToPadding` | `false` |
| 7 | `androidx.viewpager2.widget.ViewPager2` | `android:layout_width` | `match_parent` |
| 8 | `androidx.viewpager2.widget.ViewPager2` | `android:layout_height` | `0.000000dip` |
| 9 | `androidx.viewpager2.widget.ViewPager2` | `app:layout_constraintBottom_toTopOf` | `@id/vpi_in_app` |
| 10 | `androidx.viewpager2.widget.ViewPager2` | `app:layout_constraintTop_toTopOf` | `0` |
| 11 | `com.getmimo.ui.common.ViewPagerIndicator` | `android:id` | `@id/vpi_in_app` |
| 12 | `com.getmimo.ui.common.ViewPagerIndicator` | `android:layout_width` | `wrap_content` |
| 13 | `com.getmimo.ui.common.ViewPagerIndicator` | `android:layout_height` | `wrap_content` |
| 14 | `com.getmimo.ui.common.ViewPagerIndicator` | `android:layout_marginBottom` | `@dimen/spacing_xxl` |
| 15 | `com.getmimo.ui.common.ViewPagerIndicator` | `app:layout_constraintBottom_toTopOf` | `@id/in_app_button_podium_2` |
| 16 | `com.getmimo.ui.common.ViewPagerIndicator` | `app:layout_constraintEnd_toEndOf` | `0` |
| 17 | `com.getmimo.ui.common.ViewPagerIndicator` | `app:layout_constraintStart_toStartOf` | `0` |
| 18 | `com.getmimo.ui.common.ViewPagerIndicator` | `app:layout_constraintTop_toBottomOf` | `@id/vp_in_app` |
| 19 | `com.getmimo.ui.common.ViewPagerIndicator` | `app:layout_constraintVertical_chainStyle` | `0` |
| 20 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `android:id` | `@id/in_app_button_podium_1` |
| 21 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `android:visibility` | `invisible` |
| 22 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `android:layout_width` | `@dimen/iap_podium_item_big_width` |
| 23 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `android:layout_height` | `wrap_content` |
| 24 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `android:layout_marginStart` | `@dimen/iap_podium_item_margin_start_end` |
| 25 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `android:layout_marginEnd` | `@dimen/iap_podium_item_margin_between_item` |
| 26 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `app:layout_constraintBottom_toBottomOf` | `@id/in_app_button_podium_2` |
| 27 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `app:layout_constraintEnd_toStartOf` | `@id/in_app_button_podium_2` |
| 28 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `app:layout_constraintHorizontal_chainStyle` | `2` |
| 29 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `app:layout_constraintStart_toStartOf` | `0` |
| 30 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `android:id` | `@id/in_app_button_podium_2` |
| 31 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `android:visibility` | `gone` |
| 32 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `android:layout_width` | `@dimen/iap_podium_item_big_width` |
| 33 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `android:layout_height` | `wrap_content` |
| 34 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `android:layout_marginStart` | `@dimen/iap_podium_item_margin_between_item` |
| 35 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `android:layout_marginEnd` | `@dimen/iap_podium_item_margin_start_end` |
| 36 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `app:layout_constraintBottom_toTopOf` | `@id/tv_in_app_purchase_auto_renew` |
| 37 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `app:layout_constraintEnd_toEndOf` | `0` |
| 38 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `app:layout_constraintStart_toEndOf` | `@id/in_app_button_podium_1` |
| 39 | `com.getmimo.ui.iap.allplans.SubscriptionPodiumButton` | `app:layout_constraintTop_toBottomOf` | `@id/vpi_in_app` |
| 40 | `TextView` | `android:gravity` | `0x00000011` |
| 41 | `TextView` | `android:id` | `@id/tv_in_app_purchase_auto_renew` |
| 42 | `TextView` | `android:layout_width` | `wrap_content` |
| 43 | `TextView` | `android:layout_height` | `wrap_content` |
| 44 | `TextView` | `android:text` | `@string/upgrade_modal_cancel_anytime` |
| 45 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 46 | `TextView` | `android:layout_marginVertical` | `@dimen/spacing_l` |
| 47 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 48 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 49 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 50 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/in_app_button_podium_2` |
| 51 | `TextView` | `style` | `@style/TextTitle3` |
| 52 | `ProgressBar` | `android:layout_gravity` | `0x00000011` |
| 53 | `ProgressBar` | `android:id` | `@id/pb_in_app` |
| 54 | `ProgressBar` | `android:visibility` | `gone` |
| 55 | `ProgressBar` | `android:layout_width` | `wrap_content` |
| 56 | `ProgressBar` | `android:layout_height` | `wrap_content` |
| 57 | `ProgressBar` | `android:indeterminateTint` | `@color/primary_default` |
| 58 | `ProgressBar` | `app:layout_constraintBottom_toBottomOf` | `@id/in_app_button_podium_2` |
| 59 | `ProgressBar` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 60 | `ProgressBar` | `app:layout_constraintRight_toRightOf` | `0` |
| 61 | `ProgressBar` | `app:layout_constraintTop_toTopOf` | `@id/in_app_button_podium_1` |
| 62 | `ImageView` | `android:id` | `@id/iv_in_app_purchase_error` |
| 63 | `ImageView` | `android:layout_width` | `wrap_content` |
| 64 | `ImageView` | `android:layout_height` | `wrap_content` |
| 65 | `ImageView` | `android:layout_marginBottom` | `@dimen/spacing_l` |
| 66 | `ImageView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_in_app_purchase_error_title` |
| 67 | `ImageView` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 68 | `ImageView` | `app:layout_constraintRight_toRightOf` | `0` |
| 69 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 70 | `ImageView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 71 | `ImageView` | `app:srcCompat` | `@drawable/ic_state_offline` |
| 72 | `TextView` | `android:textColor` | `@color/text_primary` |
| 73 | `TextView` | `android:gravity` | `0x00000011` |
| 74 | `TextView` | `android:id` | `@id/tv_in_app_purchase_error_title` |
| 75 | `TextView` | `android:layout_width` | `wrap_content` |
| 76 | `TextView` | `android:layout_height` | `wrap_content` |
| 77 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_xs` |
| 78 | `TextView` | `android:text` | `@string/in_app_purchase_error_title` |
| 79 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_in_app_purchase_error_description` |
| 80 | `TextView` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 81 | `TextView` | `app:layout_constraintRight_toRightOf` | `0` |
| 82 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_in_app_purchase_error` |
| 83 | `TextView` | `style` | `@style/TextH1` |
| 84 | `TextView` | `android:textColor` | `@color/text_weak` |
| 85 | `TextView` | `android:gravity` | `0x00000011` |
| 86 | `TextView` | `android:id` | `@id/tv_in_app_purchase_error_description` |
| 87 | `TextView` | `android:layout_width` | `wrap_content` |
| 88 | `TextView` | `android:layout_height` | `wrap_content` |
| 89 | `TextView` | `android:text` | `@string/in_app_purchase_error_description` |
| 90 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 91 | `TextView` | `app:layout_constrainedWidth` | `true` |
| 92 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 93 | `TextView` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 94 | `TextView` | `app:layout_constraintRight_toRightOf` | `0` |
| 95 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_in_app_purchase_error_title` |
| 96 | `TextView` | `app:layout_constraintWidth_max` | `360.000000dip` |
| 97 | `TextView` | `style` | `@style/TextP1` |
| 98 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_in_app_purchase_error` |
| 99 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 100 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 101 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 102 | `androidx.compose.ui.platform.ComposeView` | `android:text` | `@string/in_app_purchase_error_return` |
| 103 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_xs` |
| 104 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 105 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 106 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 107 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `360.000000dip` |
| 108 | `ImageButton` | `android:id` | `@id/btn_in_app_close` |
| 109 | `ImageButton` | `android:background` | `?attr/selectableItemBackgroundBorderless` |
| 110 | `ImageButton` | `android:padding` | `@dimen/modal_default_close_button_padding` |
| 111 | `ImageButton` | `android:layout_width` | `wrap_content` |
| 112 | `ImageButton` | `android:layout_height` | `wrap_content` |
| 113 | `ImageButton` | `app:layout_constraintEnd_toEndOf` | `0` |
| 114 | `ImageButton` | `app:layout_constraintTop_toTopOf` | `0` |
| 115 | `ImageButton` | `app:srcCompat` | `@drawable/ic_close` |
| 116 | `ImageButton` | `app:tint` | `@color/icon_weak` |
| 117 | `androidx.constraintlayout.widget.Group` | `android:id` | `@id/group_in_app_purchase_error` |
| 118 | `androidx.constraintlayout.widget.Group` | `android:visibility` | `gone` |
| 119 | `androidx.constraintlayout.widget.Group` | `android:layout_width` | `wrap_content` |
| 120 | `androidx.constraintlayout.widget.Group` | `android:layout_height` | `wrap_content` |
| 121 | `androidx.constraintlayout.widget.Group` | `app:constraint_referenced_ids` | `iv_in_app_purchase_error,tv_in_app_purchase_error_title,         tv_in_app_purchase_error_description, btn_in_app_purchase_error` |
| 122 | `androidx.constraintlayout.widget.Group` | `android:id` | `@id/group_in_app_purchase_screen` |
| 123 | `androidx.constraintlayout.widget.Group` | `android:visibility` | `gone` |
| 124 | `androidx.constraintlayout.widget.Group` | `android:layout_width` | `wrap_content` |
| 125 | `androidx.constraintlayout.widget.Group` | `android:layout_height` | `wrap_content` |
| 126 | `androidx.constraintlayout.widget.Group` | `app:constraint_referenced_ids` | `vp_in_app,vpi_in_app,tv_in_app_purchase_auto_renew, in_app_button_podium_1,in_app_button_podium_2` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@color/primary_default` | `#FF7E4BDE` / `#FF885BDE` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/iap_podium_item_big_width` | `165.000000dip` / `175.000000dip` (sw600dp) / `212.000000dip` (sw600dp-land) |
| `@dimen/iap_podium_item_margin_between_item` | `4.000000dip` / `16.000000dip` (sw600dp) |
| `@dimen/iap_podium_item_margin_start_end` | `8.000000dip` / `32.000000dip` (sw600dp) |
| `@dimen/modal_default_close_button_padding` | `12.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxl` | `40.000000dip` |
| `@string/in_app_purchase_error_description` | `There seems to be a glitch. If your internet is working fine, we recommend you try again a bit later.` / `Scheinbar gibt es ein kleines Problem. Wenn dein Internet gut funktioniert, empfehlen wir dir, es etwas später erneut zu versuchen.` (de) / `Parece que hay un error. Si tu conexión a internet es estable, te recomendamos que lo vuelvas a intentar más tarde.` (es) / `Il semble y avoir un problème. Si ton Internet fonctionne bien, nous te recommandons de réessayer un peu plus tard.` (fr) / `Sepertinya ada gangguan. Kalau internetmu lancar, kami sarankan coba lagi sebentar lagi.` (in) / `Sembra esserci un problema. Se la tua connessione funziona, ti consigliamo di riprovare tra poco.` (it) / `Coś się zacięło. Jeśli internet działa poprawnie, spróbuj ponownie za jakiś czas.` (pl) / `Parece haver uma falha. Se sua internet estiver funcionando bem, recomendamos que você tente novamente um pouco mais tarde.` (pt-rBR) / `Кажется, это глюк. Если твой интернет работает нормально, попробуй ещё раз чуть позже.` (ru) / `Bir aksilik var gibi görünüyor. İnternetin sorunsuz çalışıyorsa biraz sonra tekrar denemeni öneririz.` (tr) |
| `@string/in_app_purchase_error_return` | `Return` / `Zurück` (de) / `Volver` (es) / `Retourner` (fr) / `Kembali` (in) / `Indietro` (it) / `Wróć` (pl) / `Retornar` (pt-rBR) / `Назад` (ru) / `Geri dön` (tr) |
| `@string/in_app_purchase_error_title` | `Oops-a-daisy!` / `Hoppla!` (de) / `Ups!` (es) / `Oh là là !` (fr) / `Waduh` (in) / `Ops!` (it) / `Ups!` (pl) / `Opa!` (pt-rBR) / `Упс!` (ru) / `Hoppala!` (tr) |
| `@string/upgrade_modal_cancel_anytime` | `Secured by Google Play. Cancel anytime.` / `Gesichert durch Google Play. Jederzeit kündigen.` (de) / `Validado por Google Play. Cancela en cualquier momento.` (es) / `Sécurisé par Google Play. Annule à tout moment.` (fr) / `Diamankan oleh Google Play. Batalkan kapan saja.` (in) / `Pagamento sicuro con Google Play. Disdici quando vuoi.` (it) / `Zabezpieczone przez Google Play. Anuluj w każdej chwili.` (pl) / `Protegido pelo Google Play. Cancele a qualquer momento.` (pt-rBR) / `Защищено Google Play. Отмени в любое время.` (ru) / `Google Play güvencesiyle. İstediğin zaman iptal et.` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextTitle3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '12.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '15.599977sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_in_app_close
@id/btn_in_app_purchase_error
@id/group_in_app_purchase_error
@id/group_in_app_purchase_screen
@id/in_app_button_podium_1
@id/in_app_button_podium_2
@id/iv_in_app_purchase_error
@id/layout_in_app_purchase
@id/pb_in_app
@id/tv_in_app_purchase_auto_renew
@id/tv_in_app_purchase_error_description
@id/tv_in_app_purchase_error_title
@id/vp_in_app
@id/vpi_in_app
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.iap.allplans.AllPlansActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/layout_in_app_purchase" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent">
  <androidx.viewpager2.widget.ViewPager2 android:id="@id/vp_in_app" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="0.000000dip" app:layout_constraintBottom_toTopOf="@id/vpi_in_app" app:layout_constraintTop_toTopOf="0"/>
  <com.getmimo.ui.common.ViewPagerIndicator android:id="@id/vpi_in_app" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_xxl" app:layout_constraintBottom_toTopOf="@id/in_app_button_podium_2" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/vp_in_app" app:layout_constraintVertical_chainStyle="0"/>
  <com.getmimo.ui.iap.allplans.SubscriptionPodiumButton android:id="@id/in_app_button_podium_1" android:visibility="invisible" android:layout_width="@dimen/iap_podium_item_big_width" android:layout_height="wrap_content" android:layout_marginStart="@dimen/iap_podium_item_margin_start_end" android:layout_marginEnd="@dimen/iap_podium_item_margin_between_item" app:layout_constraintBottom_toBottomOf="@id/in_app_button_podium_2" app:layout_constraintEnd_toStartOf="@id/in_app_button_podium_2" app:layout_constraintHorizontal_chainStyle="2" app:layout_constraintStart_toStartOf="0"/>
  <com.getmimo.ui.iap.allplans.SubscriptionPodiumButton android:id="@id/in_app_button_podium_2" android:visibility="gone" android:layout_width="@dimen/iap_podium_item_big_width" android:layout_height="wrap_content" android:layout_marginStart="@dimen/iap_podium_item_margin_between_item" android:layout_marginEnd="@dimen/iap_podium_item_margin_start_end" app:layout_constraintBottom_toTopOf="@id/tv_in_app_purchase_auto_renew" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/in_app_button_podium_1" app:layout_constraintTop_toBottomOf="@id/vpi_in_app"/>
  <TextView android:gravity="0x00000011" android:id="@id/tv_in_app_purchase_auto_renew" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/upgrade_modal_cancel_anytime" android:layout_marginHorizontal="@dimen/spacing_m" android:layout_marginVertical="@dimen/spacing_l" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/in_app_button_podium_2" style="@style/TextTitle3"/>
  <ProgressBar android:layout_gravity="0x00000011" android:id="@id/pb_in_app" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:indeterminateTint="@color/primary_default" app:layout_constraintBottom_toBottomOf="@id/in_app_button_podium_2" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toTopOf="@id/in_app_button_podium_1"/>
  <ImageView android:id="@id/iv_in_app_purchase_error" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_l" app:layout_constraintBottom_toTopOf="@id/tv_in_app_purchase_error_title" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toTopOf="0" app:layout_constraintVertical_chainStyle="2" app:srcCompat="@drawable/ic_state_offline"/>
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_in_app_purchase_error_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_xs" android:text="@string/in_app_purchase_error_title" app:layout_constraintBottom_toTopOf="@id/tv_in_app_purchase_error_description" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toBottomOf="@id/iv_in_app_purchase_error" style="@style/TextH1"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_in_app_purchase_error_description" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/in_app_purchase_error_description" android:layout_marginHorizontal="@dimen/spacing_l" app:layout_constrainedWidth="true" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toBottomOf="@id/tv_in_app_purchase_error_title" app:layout_constraintWidth_max="360.000000dip" style="@style/TextP1"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_in_app_purchase_error" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m" android:text="@string/in_app_purchase_error_return" android:layout_marginHorizontal="@dimen/spacing_xs" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintWidth_max="360.000000dip"/>
  <ImageButton android:id="@id/btn_in_app_close" android:background="?attr/selectableItemBackgroundBorderless" android:padding="@dimen/modal_default_close_button_padding" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/ic_close" app:tint="@color/icon_weak"/>
  <androidx.constraintlayout.widget.Group android:id="@id/group_in_app_purchase_error" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" app:constraint_referenced_ids="iv_in_app_purchase_error,tv_in_app_purchase_error_title,         tv_in_app_purchase_error_description, btn_in_app_purchase_error"/>
  <androidx.constraintlayout.widget.Group android:id="@id/group_in_app_purchase_screen" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" app:constraint_referenced_ids="vp_in_app,vpi_in_app,tv_in_app_purchase_auto_renew, in_app_button_podium_1,in_app_button_podium_2"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
