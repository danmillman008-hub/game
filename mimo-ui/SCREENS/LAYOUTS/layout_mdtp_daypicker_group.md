# پروندهٔ لایه — `res/layout/mdtp_daypicker_group.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mdtp_daypicker_group.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mdtp_daypicker_group.xml`](../../SOURCE/res/layout/mdtp_daypicker_group.xml) |
| SHA-256 دیکد | `5f0d78808d25ba651aa0da4f8a50896029a26cd447d698dc67927d07090164fa` |
| ریشه | `FrameLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout
   ├─ ImageButton  #@id/mdtp_previous_month_arrow
   └─ ImageButton  #@id/mdtp_next_month_arrow
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 2 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 3 | `ImageButton` | `android:id` | `@id/mdtp_previous_month_arrow` |
| 4 | `ImageButton` | `android:background` | `@drawable/mdtp_month_arrow_background` |
| 5 | `ImageButton` | `android:visibility` | `invisible` |
| 6 | `ImageButton` | `android:layout_width` | `wrap_content` |
| 7 | `ImageButton` | `android:layout_height` | `wrap_content` |
| 8 | `ImageButton` | `android:src` | `@drawable/mdtp_ic_chevron_left_black_24dp` |
| 9 | `ImageButton` | `android:minWidth` | `48.000000dip` |
| 10 | `ImageButton` | `android:minHeight` | `48.000000dip` |
| 11 | `ImageButton` | `android:contentDescription` | `@string/mdtp_previous_month_arrow_description` |
| 12 | `ImageButton` | `android:nextFocusForward` | `@id/mdtp_next_month_arrow` |
| 13 | `ImageButton` | `android:id` | `@id/mdtp_next_month_arrow` |
| 14 | `ImageButton` | `android:background` | `@drawable/mdtp_month_arrow_background` |
| 15 | `ImageButton` | `android:visibility` | `invisible` |
| 16 | `ImageButton` | `android:layout_width` | `wrap_content` |
| 17 | `ImageButton` | `android:layout_height` | `wrap_content` |
| 18 | `ImageButton` | `android:src` | `@drawable/mdtp_ic_chevron_right_black_24dp` |
| 19 | `ImageButton` | `android:minWidth` | `48.000000dip` |
| 20 | `ImageButton` | `android:minHeight` | `48.000000dip` |
| 21 | `ImageButton` | `android:contentDescription` | `@string/mdtp_next_month_arrow_description` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@string/mdtp_next_month_arrow_description` | `Next Month` / `Næste måned` (da) / `Nächsten Monat` (de) / `Next Month` (en-rGB) / `Next Month` (en-rIN) / `Pŕoximo Mes` (es) / `Pŕoximo Mes` (es-rUS) / `Seuraava kuukausi` (fi) / `Mois Suivant` (fr) / `Mois Suivant` (fr-rCA) / `Prossimo mese` (it) / `Neste måned` (nb) / `Volgende Maand` (nl) / `Próximo Mês` (pt) / `Próximo Mês` (pt-rPT) / `Nästä månad` (sv) |
| `@string/mdtp_previous_month_arrow_description` | `Previous Month` / `Foregående måned` (da) / `Vorheriger Monat` (de) / `Previous Month` (en-rGB) / `Previous Month` (en-rIN) / `Mes Previo` (es) / `Mes Previo` (es-rUS) / `Edellinen kuukausi` (fi) / `Mois Précédent` (fr) / `Mois Précédent` (fr-rCA) / `Mese precedente` (it) / `Forrige måned` (nb) / `Vorige Maand` (nl) / `Mês Anterior` (pt) / `Mês Anterior` (pt-rPT) / `Föregående månad` (sv) |

## ۴. شناسه‌های `@id`

```text
@id/mdtp_next_month_arrow
@id/mdtp_previous_month_arrow
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
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="match_parent">
  <ImageButton android:id="@id/mdtp_previous_month_arrow" android:background="@drawable/mdtp_month_arrow_background" android:visibility="invisible" android:layout_width="wrap_content" android:layout_height="wrap_content" android:src="@drawable/mdtp_ic_chevron_left_black_24dp" android:minWidth="48.000000dip" android:minHeight="48.000000dip" android:contentDescription="@string/mdtp_previous_month_arrow_description" android:nextFocusForward="@id/mdtp_next_month_arrow"/>
  <ImageButton android:id="@id/mdtp_next_month_arrow" android:background="@drawable/mdtp_month_arrow_background" android:visibility="invisible" android:layout_width="wrap_content" android:layout_height="wrap_content" android:src="@drawable/mdtp_ic_chevron_right_black_24dp" android:minWidth="48.000000dip" android:minHeight="48.000000dip" android:contentDescription="@string/mdtp_next_month_arrow_description"/>
</FrameLayout>
```
