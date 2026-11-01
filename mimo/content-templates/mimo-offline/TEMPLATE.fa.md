# برگهٔ الگو و راهنمای فیلدها

این فایل دو کار می‌کند: (۱) توضیح می‌دهد هر فیلد چه معنایی دارد، (۲) برگهٔ تقلب DSL برای نوشتن `body` است.

## ۱. فیلدهای بسته

| فیلد | الزامی | معنا |
|---|---|---|
| `publishSetVersion` | ✔ | شمارهٔ نسخهٔ محتوا؛ هر بار محتوا را تغییر دادید یک عدد بالا ببرید |
| `title` / `description` | – | نام و توضیح بسته (در صفحهٔ یادگیری دیده می‌شود) |
| `tracks[].id` | ✔ | شناسهٔ عددی یکتای مسیر |
| `tracks[].title` | ✔ | نام مسیر، مثل «ریاضی پایهٔ دهم» |
| `tracks[].description` | – | یک جمله دربارهٔ مسیر |
| `tracks[].sections[].index` | – | ترتیب نمایش بخش (یکتا در هر مسیر) |
| `tracks[].sections[].name` | ✔ | نام بخش/فصل |
| `tracks[].sections[].tutorials[].id` | ✔ | شناسهٔ توتوریال؛ فایل `tutorial-<id>.json` باید باشد |

## ۲. فیلدهای توتوریال

| فیلد | الزامی | معنا |
|---|---|---|
| `id` | ✔ | همان شناسهٔ فایل |
| `version` | – | نسخهٔ توتوریال (در پیشرفت ذخیره می‌شود) |
| `type` | – | `course` یا `practice` |
| `title` / `summary` | ✔ / – | نام و توضیح کوتاه |
| `chapters[].id` | ✔ | شناسهٔ عددی یکتا در توتوریال |
| `chapters[].title` | ✔ | نام فصل |
| `chapters[].lessons[].id` | ✔ | شناسهٔ عددی یکتای درس |
| `chapters[].lessons[].title` | ✔ | عنوان درس |
| `chapters[].lessons[].contentType` | ✔ | `interactive` (این موتور) یا `executableFiles` (نیازمند سندباکس اجرا — پشتیبانی نمی‌شود) |
| `chapters[].lessons[].objectives` | – | فهرست هدف‌های یادگیری (در بالای درس نمایش داده می‌شود) |
| `chapters[].lessons[].body` | ✔ | سند درس در DSL |
| `chapters[].lessons[].feedback` | – | نکته‌های بازخورد که در پنل نتیجه نشان داده می‌شود |

## ۳. برگهٔ تقلب DSL (بدنهٔ درس)

```html
<p>متن معمولی. <strong>پررنگ</strong>، <em>مورب</em>، <br/> شکست خط.</p>
<h2>عنوان بخش</h2>
<ul><li>فهرست</li></ul>
<blockquote>نقل‌قول یا نکتهٔ مهم</blockquote>

<!-- جای خالی درون متن (EXT-01، افزودهٔ این موتور) -->
<p>پایتخت ایران <interaction type="fillTheGap" answer="تهران" label="پایتخت" width="8"/> است.</p>

<!-- پاسخ متنی دقیق درون متن -->
<p>حاصل ۲+۲ برابر <interaction type="validatedInput" answer="4" label="حاصل" width="4"/> است.</p>

<!-- پرسش چندگزینه‌ای (تکی) -->
<selection question="کدام عدد زوج است؟">
  <item value="1" correct="true">۴</item>
  <item value="2" correct="false">۳</item>
  <item value="3" correct="false">۷</item>
</selection>

<!-- چندگزینه‌ای چندپاسخی: همهٔ درست‌ها باید انتخاب شوند -->
<selection multiple="multiple" question="کدام‌ها عدد اول‌اند؟">
  <item value="1" correct="true">۲</item>
  <item value="2" correct="true">۳</item>
  <item value="3" correct="false">۴</item>
</selection>

<!-- بلوک کد با تعامل روی بخشی از کد؛ startIndex/endIndex نسبت به متن داخل <content> -->
<code codelang="js" version="2" name="مثال">
  <content><text class="keyword">let</text> x = 1;</content>
  <interactions>
    <interaction type="validatedInput" startIndex="4" endIndex="9" isDefault="true"/>
  </interactions>
</code>

<!-- بازخورد شرطی -->
<p visible-if="wrong">این متن فقط پس از پاسخ نادرست دیده می‌شود.</p>
<p visible-if="correct">این متن فقط پس از پاسخ درست دیده می‌شود.</p>

<!-- جدول، تصویر، لینک -->
<table name="t1"><header content="نام"/><row><data content="مقدار"/></row></table>
<img src="assets/diagram.png" alt="نمودار"/>
```

### نکته‌های عملی

- `startIndex`/`endIndex` را با شمارش **نویسه‌های متن داخل `<content>`** بگذارید (تگ‌ها حساب نمی‌شوند). اعتبارسنج این بازه را بررسی می‌کند.
- برای پاسخ‌های فارسی، `validatedInput` سخت‌گیر است: فقط وقتی «درست» می‌شود که متن کاربر **دقیقاً** برابر پاسخ باشد. تفاوت فاصله‌گذاری نتیجهٔ «نزدیک بود» (PARTIAL) می‌دهد.
- `fillTheGap` در متن آزاد برای پاسخ‌های کوتاه مناسب است.
- یک درس می‌تواند چند تعامل داشته باشد؛ نتیجهٔ درس از ترکیب آن‌ها ساخته می‌شود (هر نادرست ⇒ نادرست).
