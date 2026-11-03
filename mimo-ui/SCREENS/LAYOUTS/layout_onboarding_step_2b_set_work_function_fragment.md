# پروندهٔ لایه — `res/layout/onboarding_step_2b_set_work_function_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/onboarding_step_2b_set_work_function_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/onboarding_step_2b_set_work_function_fragment.xml`](../../SOURCE/res/layout/onboarding_step_2b_set_work_function_fragment.xml) |
| SHA-256 دیکد | `bf3fcb5b40d2a80544931d19ca6bdac7c3ef72d462a7ec56a1609efa40a7c818` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 12 |
| تعداد شناسه | 9 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 31 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   └─ ScrollView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ TextView  #@id/tv_set_work_function_title
         └─ LinearLayout  #@id/layout_work_functions
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_marketing
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_sales
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_customer_support
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_software_it_data
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_product_management
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_admin_finance
            └─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_other
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000031` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:maxWidth` | `@dimen/general_max_width` |
| 5 | `ScrollView` | `android:layout_width` | `0.000000dip` |
| 6 | `ScrollView` | `android:layout_height` | `0.000000dip` |
| 7 | `ScrollView` | `android:fillViewport` | `true` |
| 8 | `ScrollView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 9 | `ScrollView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 10 | `ScrollView` | `app:layout_constraintStart_toStartOf` | `0` |
| 11 | `ScrollView` | `app:layout_constraintTop_toTopOf` | `0` |
| 12 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 13 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 14 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 15 | `TextView` | `android:textColor` | `@color/text_primary` |
| 16 | `TextView` | `android:gravity` | `0x00000011` |
| 17 | `TextView` | `android:id` | `@id/tv_set_work_function_title` |
| 18 | `TextView` | `android:layout_width` | `0.000000dip` |
| 19 | `TextView` | `android:layout_height` | `wrap_content` |
| 20 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 21 | `TextView` | `android:text` | `@string/onboarding_set_work_function_title` |
| 22 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 23 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 24 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 25 | `TextView` | `style` | `@style/TextH1` |
| 26 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 27 | `LinearLayout` | `android:orientation` | `vertical` |
| 28 | `LinearLayout` | `android:id` | `@id/layout_work_functions` |
| 29 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 30 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 31 | `LinearLayout` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 32 | `LinearLayout` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 33 | `LinearLayout` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 34 | `LinearLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 35 | `LinearLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 36 | `LinearLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_set_work_function_title` |
| 37 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:id` | `@id/btn_work_function_marketing` |
| 38 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_width` | `match_parent` |
| 39 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_height` | `wrap_content` |
| 40 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_marginVertical` | `@dimen/spacing_xs` |
| 41 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_image` | `@drawable/img_marketing` |
| 42 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_title` | `@string/onboarding_set_work_function_marketing` |
| 43 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:id` | `@id/btn_work_function_sales` |
| 44 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_width` | `match_parent` |
| 45 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_height` | `wrap_content` |
| 46 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_marginVertical` | `@dimen/spacing_xs` |
| 47 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_image` | `@drawable/img_sales` |
| 48 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_title` | `@string/onboarding_set_work_function_sales` |
| 49 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:id` | `@id/btn_work_function_customer_support` |
| 50 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_width` | `match_parent` |
| 51 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_height` | `wrap_content` |
| 52 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_marginVertical` | `@dimen/spacing_xs` |
| 53 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_image` | `@drawable/img_customer_support` |
| 54 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_title` | `@string/onboarding_set_work_function_customer_support` |
| 55 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:id` | `@id/btn_work_function_software_it_data` |
| 56 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_width` | `match_parent` |
| 57 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_height` | `wrap_content` |
| 58 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_marginVertical` | `@dimen/spacing_xs` |
| 59 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_image` | `@drawable/img_software_it_data` |
| 60 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_title` | `@string/onboarding_set_work_function_software_it_data` |
| 61 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:id` | `@id/btn_work_function_product_management` |
| 62 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_width` | `match_parent` |
| 63 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_height` | `wrap_content` |
| 64 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_marginVertical` | `@dimen/spacing_xs` |
| 65 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_image` | `@drawable/img_product_management` |
| 66 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_title` | `@string/onboarding_set_work_function_product_management` |
| 67 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:id` | `@id/btn_work_function_admin_finance` |
| 68 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_width` | `match_parent` |
| 69 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_height` | `wrap_content` |
| 70 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_marginVertical` | `@dimen/spacing_xs` |
| 71 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_image` | `@drawable/img_administration_finance` |
| 72 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_title` | `@string/onboarding_set_work_function_admin_finance` |
| 73 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:id` | `@id/btn_work_function_other` |
| 74 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_width` | `match_parent` |
| 75 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_height` | `wrap_content` |
| 76 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_marginVertical` | `@dimen/spacing_xs` |
| 77 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_image` | `@drawable/img_something_else` |
| 78 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_title` | `@string/onboarding_set_work_function_other` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@string/onboarding_set_work_function_admin_finance` | `Administration & finance` / `Verwaltung und Finanzen` (de) / `Administración y finanzas` (es) / `Administration et finances` (fr) / `Administrasi & keuangan` (in) / `Amministrazione e finanza` (it) / `Administracja i finanse` (pl) / `Administração e finanças` (pt-rBR) / `Администрирование и финансы` (ru) / `İdari işler ve finans` (tr) |
| `@string/onboarding_set_work_function_customer_support` | `Customer support` / `Kundenservice` (de) / `Atención al cliente` (es) / `Service client` (fr) / `Dukungan pelanggan` (in) / `Assistenza clienti` (it) / `Obsługa klienta` (pl) / `Atendimento ao cliente` (pt-rBR) / `Поддержка клиентов` (ru) / `Müşteri desteği` (tr) |
| `@string/onboarding_set_work_function_marketing` | `Marketing` / `Marketing` (de) / `Marketing` (es) / `Marketing` (fr) / `Pemasaran` (in) / `Marketing` (it) / `Marketing` (pl) / `Marketing` (pt-rBR) / `Маркетинг` (ru) / `Pazarlama` (tr) |
| `@string/onboarding_set_work_function_other` | `Something else` / `Etwas anderes` (de) / `Otra área` (es) / `Autre chose` (fr) / `Lainnya` (in) / `Altro` (it) / `Coś innego` (pl) / `Outra área` (pt-rBR) / `Другое` (ru) / `Başka bir şey` (tr) |
| `@string/onboarding_set_work_function_product_management` | `Product management` / `Produktmanagement` (de) / `Gestión de productos` (es) / `Gestion de produit` (fr) / `Manajemen produk` (in) / `Gestione del prodotto` (it) / `Zarządzanie produktem` (pl) / `Gestão de produtos` (pt-rBR) / `Управление продуктом` (ru) / `Ürün yönetimi` (tr) |
| `@string/onboarding_set_work_function_sales` | `Sales` / `Vertrieb` (de) / `Ventas` (es) / `Ventes` (fr) / `Penjualan` (in) / `Vendite` (it) / `Sprzedaż` (pl) / `Vendas` (pt-rBR) / `Продажи` (ru) / `Satış` (tr) |
| `@string/onboarding_set_work_function_software_it_data` | `Software, IT & data` / `Software, IT & Daten` (de) / `Software, TI y datos` (es) / `Logiciels, informatique et données` (fr) / `Perangkat lunak, TI & data` (in) / `Software, IT e dati` (it) / `Oprogramowanie, IT i dane` (pl) / `Software, TI e dados` (pt-rBR) / `Разработка, ИТ и данные` (ru) / `Yazılım, BT ve veri` (tr) |
| `@string/onboarding_set_work_function_title` | `What kind of work do you do?` / `Was für eine Arbeit machst du?` (de) / `¿A qué tipo de trabajo te dedicas?` (es) / `Quel type de travail fais-tu ?` (fr) / `Apa jenis pekerjaanmu?` (in) / `Che tipo di lavoro fai?` (it) / `Jaką pracę wykonujesz?` (pl) / `Que tipo de trabalho você faz?` (pt-rBR) / `Чем ты занимаешься на работе?` (ru) / `Ne tür bir iş yapıyorsun?` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_work_function_admin_finance
@id/btn_work_function_customer_support
@id/btn_work_function_marketing
@id/btn_work_function_other
@id/btn_work_function_product_management
@id/btn_work_function_sales
@id/btn_work_function_software_it_data
@id/layout_work_functions
@id/tv_set_work_function_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.onboarding.OnboardingActivity
com.getmimo.ui.onboarding.workfunction.SetWorkFunctionFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000031" android:layout_width="match_parent" android:layout_height="match_parent" android:maxWidth="@dimen/general_max_width">
  <ScrollView android:layout_width="0.000000dip" android:layout_height="0.000000dip" android:fillViewport="true" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginHorizontal="@dimen/spacing_l">
      <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_set_work_function_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/onboarding_set_work_function_title" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextH1"/>
      <LinearLayout android:gravity="0x00000011" android:orientation="vertical" android:id="@id/layout_work_functions" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:layout_marginBottom="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_set_work_function_title">
        <com.getmimo.ui.onboarding.motive.OnboardingMotiveButton android:id="@id/btn_work_function_marketing" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginVertical="@dimen/spacing_xs" app:motive_image="@drawable/img_marketing" app:motive_title="@string/onboarding_set_work_function_marketing"/>
        <com.getmimo.ui.onboarding.motive.OnboardingMotiveButton android:id="@id/btn_work_function_sales" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginVertical="@dimen/spacing_xs" app:motive_image="@drawable/img_sales" app:motive_title="@string/onboarding_set_work_function_sales"/>
        <com.getmimo.ui.onboarding.motive.OnboardingMotiveButton android:id="@id/btn_work_function_customer_support" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginVertical="@dimen/spacing_xs" app:motive_image="@drawable/img_customer_support" app:motive_title="@string/onboarding_set_work_function_customer_support"/>
        <com.getmimo.ui.onboarding.motive.OnboardingMotiveButton android:id="@id/btn_work_function_software_it_data" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginVertical="@dimen/spacing_xs" app:motive_image="@drawable/img_software_it_data" app:motive_title="@string/onboarding_set_work_function_software_it_data"/>
        <com.getmimo.ui.onboarding.motive.OnboardingMotiveButton android:id="@id/btn_work_function_product_management" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginVertical="@dimen/spacing_xs" app:motive_image="@drawable/img_product_management" app:motive_title="@string/onboarding_set_work_function_product_management"/>
        <com.getmimo.ui.onboarding.motive.OnboardingMotiveButton android:id="@id/btn_work_function_admin_finance" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginVertical="@dimen/spacing_xs" app:motive_image="@drawable/img_administration_finance" app:motive_title="@string/onboarding_set_work_function_admin_finance"/>
        <com.getmimo.ui.onboarding.motive.OnboardingMotiveButton android:id="@id/btn_work_function_other" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginVertical="@dimen/spacing_xs" app:motive_image="@drawable/img_something_else" app:motive_title="@string/onboarding_set_work_function_other"/>
      </LinearLayout>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </ScrollView>
</androidx.constraintlayout.widget.ConstraintLayout>
```
