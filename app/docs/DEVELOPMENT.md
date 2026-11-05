# روند توسعه

## قوانین غیرقابل تغییر

1. **هیچ فایلی در `mimo-ui/UPGRADE/` ویرایش نمیشود.** پروتوتایپ `DESIGN/index.html`
   (SHA `c356068daa5ccafbee46599897ad18bdf1e4f91f1ca23f36b1b8bd153dbfdb78`)
   مرجع نهایی و محافظتشده است. همینطور مدارک `ANALYSIS/MISSION_05…09`.
2. طراحی فقط در صورتی تغییر میکند که طرح تأییدشدهٔ تازهای از سوی کاربر برسد.
   در آن صورت: `tools/extract_from_prototype.py` ← `tools/build_index.py` ← تستها.
3. کد محصول فقط در `app/src/` نوشته میشود. داراییهای `app/assets/` خروجی
   ساختهشدهاند و نباید دستی ویرایش شوند.
4. دادهٔ نهایی (سرفصل/سؤال/توضیح) وارد `fixtures.js` نمیشود؛ آن فایل مخصوص
   placeholder است و `placeholder:true` / `contentReady:false` دارد.
5. هیچ رفتار سرورمالک جعل نمیشود. هر قاعدهای که از M09 تأیید نشده، در کد با
   `DESIGN_CHOICE` برچسب میخورد و در مستندات بهعنوان «مستقل محلی» گفته میشود.

## چرخهٔ کار

```bash
cd /home/user/game/app

# ۱) بازسازی داراییها از روی پروتوتایپ + تولید index.html (idempotent)
npm run build

# ۲) راستیآزمایی استاتیک یکپارچگی طرح
npm run verify
python3 ../mimo-ui/UPGRADE/tools/verify_upgrade.py ../mimo-ui/UPGRADE

# ۳) تستها
npm install      # فقط jsdom، در devDependencies
npm test

# ۴) اجرای واقعی / پیشنمایش زنده
npm start        # 0.0.0.0:3000
```

`npm run build` دو اسکریپت پایتونی را اجرا میکند:
- `tools/extract_from_prototype.py`: هش مبدأ را چک میکند، سپس CSS، مارکاپ گوشی،
  چهار بلاک داده و کپی کاری UI را میسازد و `assets/PROVENANCE.json` را مینویسد.
- `tools/build_index.py`: مارکاپ گوشی را عیناً در `index.html` درج میکند تا صفحه
  محصول خودکفا و بدون وابستگی زمان ساخت باشد.

اگر وصلهٔ تازهای به `proto-ui.js` لازم شد، **فقط** لیست `patches` در
`extract_from_prototype.py` را تغییر بده و دوباره `npm run build` بزن؛ وصلهها
با anchor متنی اعمال میشوند و در صورت تغییر مبدأ، اسکریپت با خطا متوقف میشود
(بیهما فایل خراب تولید نمیکند).

## اضافه کردن یک صفحه

- صفحهای که در پروتوتایپ هست: فقط `PROTO.go(name)` صدا بزن و در صورت نیاز
  `PROTO.tabMap[name]` را در `app.js` نگاشت بده.
- صفحهٔ تازه: در `src/views.js` با کلاسهای موجود بساز، با `insert()` قبل از
  `#tabs` اضافه کن، `data-screen` بده، `PROTO.tabMap` را در `app.js` به یکی از
  پنج تب مجاز نگاشت کن، و در `onNavigate()` رندر/ریفرش آن را اضافه کن.
- هر عنصر `data-icon` تازه حتماً `PROTO.paintIcons(root)` میخواهد.

## اضافه کردن وضعیت تازه

1. کلید را به `defaultState()` در `src/store.js` اضافه کن (با مقدار امن پیشفرض).
2. `migrate()` بهطور خودکار شاخهٔ `object` را ادغام میکند؛ برای آرایهها و
   invariance خاص، قانون صریح اضافه کن.
3. فقط از `store.set/patch/push` استفاده کن؛ نوشتن مستقیم روی `store.state`
   ذخیره نمیشود (جز `grant/enqueue` که عمداً روی همان آبجکت کار میکنند و بلافاصله
   با `store.set` همراهاند).
4. یک تست «تغییر → بستن → باز کردن مجدد → بازیابی» در `tests/acceptance.test.mjs`
   اضافه کن.

## افزودن انیمیشن

فقط در `assets/motion.css`، فقط `transition` / `@keyframes` / حالت `:active` /
`hover`. رنگ hard-coded، فونت، شعاع، ابعاد و چینش عناصر تأییدشده تغییر نمیکند.
قاعدهٔ `body.reduce-motion` و `prefers-reduced-motion` باید پابرجا بماند.

## قراردادهای نامگذاری

- شناسههای DOM پروتوتایپ دستنخوردهاند (`#examTitle`, `#timerChip`, …).
- عناصر اضافهشدهٔ محصول `data-role` دارند یا پیشوند `app-` / شناسهٔ توصیفی
  (`#planAction`, `#bankStart`, `#settingsModal`) تا با رندرر تداخل نکنند.
- اعداد فارسی در UI با `PROTO.fa()` / `faNum()` تولید میشوند.

## وابستگیها

| نوع | مورد | دلیل |
|---|---|---|
| زمان اجرا | **هیچ** | HTML/CSS/JS خالص + Node استاتیکسرور |
| dev | `jsdom` | تست DOM واقعی و چرخهٔ بستن/باز کردن |
| ابزار | Python 3 (کتابخانهٔ استاندارد) | استخراج و راستیآزمایی، بدون pip |
