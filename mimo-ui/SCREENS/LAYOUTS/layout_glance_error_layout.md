# پروندهٔ لایه — `res/layout/glance_error_layout.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/glance_error_layout.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/glance_error_layout.xml`](../../SOURCE/res/layout/glance_error_layout.xml) |
| SHA-256 دیکد | `8fc53132b01bc4b1105582948389b0a9068017335a8ef634f215303482926313` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   └─ FrameLayout
      └─ TextView  #@id/error_text_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 3 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 4 | `LinearLayout` | `style` | `@style/Glance.AppWidget.Background.Error` |
| 5 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 6 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 7 | `TextView` | `android:textColor` | `@color/glance_colorOnSurface` |
| 8 | `TextView` | `android:layout_gravity` | `0x00000011` |
| 9 | `TextView` | `android:id` | `@id/error_text_view` |
| 10 | `TextView` | `android:layout_width` | `wrap_content` |
| 11 | `TextView` | `android:layout_height` | `wrap_content` |
| 12 | `TextView` | `android:text` | `@string/glance_error_layout_text_v2` |
| 13 | `TextView` | `android:layout_weight` | `1.000000` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/glance_colorOnSurface` | `#FF1C1B1F` / `#FFE6E1E5` (night) / `@android:01060020` (night-v31) / `@android:01060028` (v31) |
| `@string/glance_error_layout_text_v2` | `Can't show content` / `Kan nie inhoud wys nie` (af) / `ይዘትን ማሳየት አልተቻለም` (am) / `يتعذّر عرض المحتوى.` (ar) / `সমল দেখুৱাব নোৱাৰি` (as) / `Kontenti göstərmək olmur` (az) / `Не ўдалося загрузіць змесціва` (be) / `Съдържанието не може да се покаже` (bg) / `কন্টেন্ট দেখানো যাচ্ছে না` (bn) / `Nije moguće prikazati sadržaj` (bs) / `No es pot mostrar el contingut` (ca) / `Obsah nelze zobrazit` (cs) / `Indholdet kan ikke vises` (da) / `Inhalt kann nicht angezeigt werden` (de) / `Δεν είναι δυνατή η εμφάνιση περιεχομένου` (el) / `Can't show content` (en-rAU) / `Can't show content` (en-rCA) / `Can't show content` (en-rGB) / `Can't show content` (en-rIN) / `‎‏‎‎‎‎‎‏‎‏‏‏‎‎‎‎‎‎‏‎‎‏‎‎‎‎‏‏‏‏‏‏‏‏‎‎‏‎‎‎‎‎‎‎‏‎‏‎‏‎‏‏‏‏‎‎‎‎‎‏‏‏‏‏‏‏‎‎‏‏‏‏‎‏‎‎‏‎‎‏‏‎‎‏‏‏‏‏‎‏‎‎‎‎‎‏‎Can't show content‎‏‎‎‏‎` (en-rXC) / `No se puede mostrar el contenido` (es) / `No se puede mostrar el contenido` (es-rUS) / `Sisu ei saa kuvada` (et) / `Ezin da erakutsi edukia` (eu) / `محتوا نشان داده نشد` (fa) / `Sisältöä ei voi näyttää` (fi) / `Impossible d'afficher le contenu` (fr) / `Impossible d'afficher le contenu` (fr-rCA) / `Non se puido mostrar o contido` (gl) / `કન્ટેન્ટ બતાવી શકતા નથી` (gu) / `कॉन्टेंट नहीं दिखाया जा सकता` (hi) / `Sadržaj se ne može prikazati` (hr) / `A tartalom nem jeleníthető meg` (hu) / `Հնարավոր չէ ցույց տալ բովանդակությունը` (hy) / `Tidak dapat menampilkan konten` (in) / `Ekki er hægt að sýna efnið` (is) / `Impossibile mostrare i contenuti` (it) / `לא ניתן להציג את התוכן` (iw) / `コンテンツを表示できません` (ja) / `კონტენტის ჩვენება ვერ ხერხდება` (ka) / `Контентті көрсету мүмкін емес.` (kk) / `មិនអាចបង្ហាញ​ខ្លឹមសារបានទេ` (km) / `ಕಂಟೆಂಟ್ ಅನ್ನು ತೋರಿಸಲು ಸಾಧ್ಯವಿಲ್ಲ` (kn) / `콘텐츠를 표시할 수 없음` (ko) / `Контент көрсөтүлбөй жатат` (ky) / `ບໍ່ສາມາດສະແດງເນື້ອຫາໄດ້` (lo) / `Nepavyko parodyti turinio` (lt) / `Nevar parādīt saturu.` (lv) / `Не може да се прикажат содржините` (mk) / `ഉള്ളടക്കം കാണിക്കാനാകില്ല` (ml) / `Контентыг харуулах боломжгүй` (mn) / `आशय दाखवू शकत नाही` (mr) / `Tidak dapat memaparkan kandungan` (ms) / `အကြောင်းအရာကို ပြ၍မရပါ` (my) / `Kan ikke vise innhold` (nb) / `सामग्री देखाउन सकिएन` (ne) / `Kan content niet tonen` (nl) / `ବିଷୟବସ୍ତୁ ଦେଖାଯାଇପାରିବ ନାହିଁ` (or) / `ਸਮੱਗਰੀ ਨਹੀਂ ਦਿਖਾਈ ਜਾ ਸਕਦੀ` (pa) / `Nie można wyświetlić zawartości` (pl) / `Não é possível mostrar conteúdo` (pt) / `Não é possível mostrar conteúdo` (pt-rBR) / `Não é possível mostrar o conteúdo` (pt-rPT) / `Nu se poate afișa conținutul` (ro) / `Невозможно показать контент.` (ru) / `අන්තර්ගතය පෙන්විය නොහැක` (si) / `Obsah nie je možné zobraziť` (sk) / `Ni mogoče prikazati vsebine` (sl) / `Përmbajtja nuk mund të shfaqet` (sq) / `Садржај не може да се прикаже` (sr) / `Det gick inte att visa innehållet` (sv) / `Imeshindwa kuonyesha maudhui` (sw) / `உள்ளடக்கத்தைக் காட்ட முடியவில்லை` (ta) / `కంటెంట్‌ను చూపడం సాధ్యం కాదు` (te) / `แสดงเนื้อหาไม่ได้` (th) / `Hindi makapagpakita ng content` (tl) / `İçerik gösterilemiyor` (tr) / `Не вдається відобразити контент` (uk) / `مواد نہیں دکھایا جاسکتا` (ur) / `Kontent chiqmaydi` (uz) / `Không hiện được nội dung` (vi) / `无法显示内容` (zh-rCN) / `無法顯示內容` (zh-rHK) / `無法顯示內容` (zh-rTW) / `Ayikwazi ukubonisa okuqukethwe` (zu) |
| `@style/Glance.AppWidget.Background.Error` | `[{'attr': 'android:background', 'attr_id': '0x010100D4', 'value': '@drawable/glance_error_layout_background', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/error_text_view
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="match_parent" style="@style/Glance.AppWidget.Background.Error">
  <FrameLayout android:layout_width="match_parent" android:layout_height="match_parent">
    <TextView android:textColor="@color/glance_colorOnSurface" android:layout_gravity="0x00000011" android:id="@id/error_text_view" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/glance_error_layout_text_v2" android:layout_weight="1.000000"/>
  </FrameLayout>
</LinearLayout>
```
