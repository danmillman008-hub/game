# پروندهٔ لایه — `res/layout/fingerprint_dialog_layout.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/fingerprint_dialog_layout.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/fingerprint_dialog_layout.xml`](../../SOURCE/res/layout/fingerprint_dialog_layout.xml) |
| SHA-256 دیکد | `4183d47343a9febcd9e6e6adbfb3de04aa16fceaf8cb555d0bc6b3520708dca2` |
| ریشه | `ScrollView` |
| تعداد گره | 6 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ ScrollView
   └─ LinearLayout
      ├─ TextView  #@id/fingerprint_subtitle
      ├─ TextView  #@id/fingerprint_description
      ├─ ImageView  #@id/fingerprint_icon
      └─ TextView  #@id/fingerprint_error
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ScrollView` | `android:orientation` | `vertical` |
| 2 | `ScrollView` | `android:layout_width` | `match_parent` |
| 3 | `ScrollView` | `android:layout_height` | `match_parent` |
| 4 | `LinearLayout` | `android:orientation` | `vertical` |
| 5 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 6 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 7 | `TextView` | `android:textSize` | `16.000000sp` |
| 8 | `TextView` | `android:textColor` | `?0x01010038` |
| 9 | `TextView` | `android:ellipsize` | `marquee` |
| 10 | `TextView` | `android:id` | `@id/fingerprint_subtitle` |
| 11 | `TextView` | `android:layout_width` | `match_parent` |
| 12 | `TextView` | `android:layout_height` | `wrap_content` |
| 13 | `TextView` | `android:layout_marginTop` | `8.000000dip` |
| 14 | `TextView` | `android:singleLine` | `true` |
| 15 | `TextView` | `android:marqueeRepeatLimit` | `-1` |
| 16 | `TextView` | `android:layout_marginStart` | `24.000000dip` |
| 17 | `TextView` | `android:layout_marginEnd` | `24.000000dip` |
| 18 | `TextView` | `android:textSize` | `16.000000sp` |
| 19 | `TextView` | `android:textColor` | `?0x01010038` |
| 20 | `TextView` | `android:id` | `@id/fingerprint_description` |
| 21 | `TextView` | `android:paddingTop` | `0.000000dip` |
| 22 | `TextView` | `android:layout_width` | `match_parent` |
| 23 | `TextView` | `android:layout_height` | `wrap_content` |
| 24 | `TextView` | `android:maxLines` | `4` |
| 25 | `TextView` | `android:layout_marginStart` | `24.000000dip` |
| 26 | `TextView` | `android:layout_marginEnd` | `24.000000dip` |
| 27 | `ImageView` | `android:layout_gravity` | `0x00000001` |
| 28 | `ImageView` | `android:id` | `@id/fingerprint_icon` |
| 29 | `ImageView` | `android:layout_width` | `@dimen/fingerprint_icon_size` |
| 30 | `ImageView` | `android:layout_height` | `@dimen/fingerprint_icon_size` |
| 31 | `ImageView` | `android:layout_marginTop` | `32.000000dip` |
| 32 | `ImageView` | `android:scaleType` | `fitXY` |
| 33 | `TextView` | `android:textSize` | `14.000000sp` |
| 34 | `TextView` | `android:textColor` | `?0x01010038` |
| 35 | `TextView` | `android:gravity` | `0x00000001` |
| 36 | `TextView` | `android:id` | `@id/fingerprint_error` |
| 37 | `TextView` | `android:paddingTop` | `16.000000dip` |
| 38 | `TextView` | `android:paddingBottom` | `24.000000dip` |
| 39 | `TextView` | `android:layout_width` | `match_parent` |
| 40 | `TextView` | `android:layout_height` | `wrap_content` |
| 41 | `TextView` | `android:text` | `@string/fingerprint_dialog_touch_sensor` |
| 42 | `TextView` | `android:layout_marginStart` | `24.000000dip` |
| 43 | `TextView` | `android:layout_marginEnd` | `24.000000dip` |
| 44 | `TextView` | `android:accessibilityLiveRegion` | `1` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/fingerprint_icon_size` | `64.000000dip` |
| `@string/fingerprint_dialog_touch_sensor` | `Touch the fingerprint sensor` / `Raak die vingerafdruksensor` (af) / `የጣት አሻራ ዳሳሹን ይንኩ` (am) / `المس زر استشعار بصمة الإصبع` (ar) / `ফিংগাৰপ্ৰিণ্ট ছেন্সৰটো স্পৰ্শ কৰক` (as) / `Barmaq izi sensoruna klikləyin` (az) / `Дакраніцеся да сканера адбіткаў пальцаў` (be) / `Докоснете сензора за отпечатъци` (bg) / `আঙ্গুলের ছাপের সেন্সর টাচ করুন` (bn) / `Dodirnite senzor za otisak prsta` (bs) / `Toca sensor d'empremtes` (ca) / `Dotkněte se snímače otisků prstů` (cs) / `Sæt finger på fingeraftrykslæser` (da) / `Fingerabdrucksensor berühren` (de) / `Αγγίξτε τον αισθ. δακτ. αποτ.` (el) / `Touch the fingerprint sensor` (en-rAU) / `Touch the fingerprint sensor` (en-rCA) / `Touch the fingerprint sensor` (en-rGB) / `Touch the fingerprint sensor` (en-rIN) / `‎‏‎‎‎‎‎‏‎‏‏‏‎‎‎‎‎‎‏‎‎‏‎‎‎‎‏‏‏‏‏‎‎‏‏‏‎‏‏‏‎‎‎‎‏‏‎‎‏‏‎‏‎‎‏‏‏‏‏‎‎‎‎‏‎‎‎‎‏‎‎‎‏‏‏‏‏‎‎‎‎‏‏‏‎‎‎‎‎‎‎‏‏‎Touch the fingerprint sensor‎‏‎‎‏‎` (en-rXC) / `Toca sensor huellas digitales` (es) / `Toca el sensor de huellas dig.` (es-rUS) / `Puudutage sõrmejäljeandurit` (et) / `Sakatu hatz-marken sentsorea` (eu) / `حسگر اثر انگشت را لمس کنید` (fa) / `Kosketa sormenjälkitunnistinta` (fi) / `Appuyez sur lecteur d'empreinte` (fr) / `Touch. capteur empr. digitales` (fr-rCA) / `Toca o sensor de impresión dixital` (gl) / `ફિંગરપ્રિન્ટના સેન્સરને સ્પર્શ કરો` (gu) / `फ़िंगरप्रिंट सेंसर को छुएं` (hi) / `Dodirnite senzor otiska prsta` (hr) / `Érintse meg az ujjlenyomat-érzékelőt` (hu) / `Հպեք մատնահետքի սկաներին` (hy) / `Sentuh sensor sidik jari` (in) / `Snertu fingrafaralesarann` (is) / `Tocca sensore impronte` (it) / `יש לגעת בחיישן טביעות האצבע` (iw) / `指紋認証センサーをタップ` (ja) / `შეეხეთ თითის ანაბეჭდის სენსორს` (ka) / `Саусақ ізін оқу сканерін түртіңіз` (kk) / `ប៉ះ​ឧបករណ៍​ចាប់ស្នាម​ម្រាមដៃ` (km) / `ಫಿಂಗರ್‌ಪ್ರಿಂಟ್ ಸೆನ್ಸರ್‌‌ ಅನ್ನು ಸ್ಪರ್ಶಿಸಿ` (kn) / `지문 센서를 터치하세요.` (ko) / `Манжа изинин сенсорун басыңыз` (ky) / `ແຕະເຊັນເຊີລາຍນິ້ວມື` (lo) / `Palieskite piršto antspaudo jutiklį` (lt) / `Pieskarieties pirksta nospieduma sensoram` (lv) / `Допрете го сенз. за отпечатоци` (mk) / `ഫിംഗർപ്രിന്റ് സെൻസർ സ്‌പർശിക്കുക` (ml) / `Хурууны хээ мэдрэгчид хүрнэ үү` (mn) / `फिंगरप्रिंट सेन्सरला स्पर्श करा` (mr) / `Sentuh penderia cap jari` (ms) / `လက်ဗွေအာရုံခံကိရိယာကို တို့ပါ` (my) / `Trykk på fingeravtrykkssensoren` (nb) / `फिंगरप्रिन्ट सेन्सरमा छुनुहोस्‌` (ne) / `Raak de vingerafdruksensor aan` (nl) / `ଟିପଚିହ୍ନ ସେନସର୍‌କୁ ଛୁଅଁନ୍ତୁ` (or) / `ਫਿੰਗਰਪ੍ਰਿੰਟ ਸੈਂਸਰ ਨੂੰ ਸਪਰਸ਼ ਕਰੋ` (pa) / `Dotknij czytnika linii papilarnych` (pl) / `Toque no sensor de digital` (pt) / `Toque no sensor de digital` (pt-rBR) / `Toque no sensor de impressões digitais` (pt-rPT) / `Atingeți senzorul de amprentă` (ro) / `Коснитесь сканера отпечатков.` (ru) / `ඇඟිලි සලකුණු සංවේදකය ස්පර්ශ කරන්න` (si) / `Dotknite sa senzora odtlačkov prstov` (sk) / `Dotaknite se tipala prst. odt.` (sl) / `Prek sensorin e gjurmës së gishtit` (sq) / `Додирн. сензор за отисак прста` (sr) / `Tryck på fingeravtryckssensorn` (sv) / `Gusa kitambua alama ya kidole` (sw) / `கைரேகை சென்சாரைத் தொடுக` (ta) / `వేలిముద్ర సెన్సార్‌ను తాకండి` (te) / `แตะเซ็นเซอร์ลายนิ้วมือ` (th) / `Pindutin ang fingerprint sensor` (tl) / `Parmak izi sensörüne dokunun` (tr) / `Торкніться сканера відбитків пальців` (uk) / `فنگر پرنٹ سینسر کو ٹچ کریں` (ur) / `Barmoq izi skaneriga tegining` (uz) / `Chạm vào cảm biến vân tay` (vi) / `请轻触指纹传感器` (zh-rCN) / `請輕觸指紋感應器` (zh-rHK) / `請輕觸指紋感應器` (zh-rTW) / `Thinta inzwa yezigxivizo zeminwe` (zu) |

## ۴. شناسه‌های `@id`

```text
@id/fingerprint_description
@id/fingerprint_error
@id/fingerprint_icon
@id/fingerprint_subtitle
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
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="match_parent">
  <LinearLayout android:orientation="vertical" android:layout_width="match_parent" android:layout_height="wrap_content">
    <TextView android:textSize="16.000000sp" android:textColor="?0x01010038" android:ellipsize="marquee" android:id="@id/fingerprint_subtitle" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="8.000000dip" android:singleLine="true" android:marqueeRepeatLimit="-1" android:layout_marginStart="24.000000dip" android:layout_marginEnd="24.000000dip"/>
    <TextView android:textSize="16.000000sp" android:textColor="?0x01010038" android:id="@id/fingerprint_description" android:paddingTop="0.000000dip" android:layout_width="match_parent" android:layout_height="wrap_content" android:maxLines="4" android:layout_marginStart="24.000000dip" android:layout_marginEnd="24.000000dip"/>
    <ImageView android:layout_gravity="0x00000001" android:id="@id/fingerprint_icon" android:layout_width="@dimen/fingerprint_icon_size" android:layout_height="@dimen/fingerprint_icon_size" android:layout_marginTop="32.000000dip" android:scaleType="fitXY"/>
    <TextView android:textSize="14.000000sp" android:textColor="?0x01010038" android:gravity="0x00000001" android:id="@id/fingerprint_error" android:paddingTop="16.000000dip" android:paddingBottom="24.000000dip" android:layout_width="match_parent" android:layout_height="wrap_content" android:text="@string/fingerprint_dialog_touch_sensor" android:layout_marginStart="24.000000dip" android:layout_marginEnd="24.000000dip" android:accessibilityLiveRegion="1"/>
  </LinearLayout>
</ScrollView>
```
