# فاز ۱ — مدل داده و دامنه

> **خروجی این فاز:** موجودیت‌ها، روابط، قواعد اعتبارسنجی، اسکیمای SQL، استراتژی مهاجرت.
> **وضعیت: منتظر تأیید.** هیچ کد اپلیکیشنی نوشته نشده؛ فقط طرح داده نهایی شده است.

---

## ۱) اصل حاکم: دفترِ تراکنش، نه «عددِ موجودی»

موجودی **ذخیره نمی‌شود**؛ **محاسبه می‌شود** از مجموع تراکنش‌ها.
دلیل: اگر فقط عدد ذخیره شود، هیچ‌وقت نمی‌فهمیم چرا این عدد است. با دفتر تراکنش:

- هر تغییر قابل حسابرسی است (چه کسی، چه وقت، چرا).
- اشتباه کاربر با یک تراکنش معکوس اصلاح می‌شود، نه با ویرایش تاریخ.
- خرابی/قطع برق، داده را نیمه‌کاره نمی‌گذارد (تراکنش اتمیک).
- برای گزارش «موجودی الان» از یک جدول خلاصه (materialized) استفاده می‌کنیم که همیشه از دفتر بازسازی‌شدنی است.

---

## ۲) موجودیت‌ها

```
┌──────────────┐         ┌──────────────┐
│    drug      │1       n│    batch     │
│ (فرآورده)    ├─────────┤ (بچ/سری ساخت)│
└──────┬───────┘         └──────┬───────┘
       │1                       │1
       │                        │
       │n                       │n
┌──────┴────────────────────────┴───────┐
│            movement                   │  ← دفتر کل (append-only)
│ (شمارش/ورود/خروج/ضایعات/مرجوعی)      │
└──────┬───────────────────┬────────────┘
       │                   │
       │n                  │n
┌──────┴───────┐    ┌──────┴────────┐      ┌───────────────┐
│ stock_balance│    │   user        │      │   inquiry     │
│ (خلاصهٔ زنده) │    │ (شمارنده)     │      │ (کش استعلام)  │
└──────────────┘    └───────────────┘      └───────────────┘

┌──────────────┐   ┌───────────────┐   ┌──────────────┐
│   license    │   │   settings    │   │  audit_log   │
└──────────────┘   └───────────────┘   └──────────────┘
```

---

## ۳) قواعد دامنه (invariant) — این‌ها در DB و در لایهٔ دامنه هر دو اعمال می‌شوند

| # | قاعده | چرا |
|---|---|---|
| I1 | **هیچ فرآورده‌ای بدون نام ذخیره نمی‌شود** (`name_fa` غیرخالی) | قاعدهٔ سخت کارفرما؛ رکورد بی‌نام یعنی داده‌ی بی‌مصرف |
| I2 | مقدارها **عدد صحیح** هستند (واحد پایه)، نه اعشاری | حذف خطای گردکردن |
| I3 | هر جابه‌جایی مقدار باید `client_uuid` یکتا داشته باشد | ضد دوباره‌ثبت‌شدن (دوبار لمس، تلاش مجدد، کپی) |
| I4 | `batch` بدون `batch_code` و `expiry` ساخته نمی‌شود (یا هر دو، یا هیچ) | جلوگیری از بچِ بی‌هویت |
| I5 | موجودی هیچ بچی منفی نمی‌شود؛ برای اصلاح، تراکنش معکوس ثبت می‌شود | حسابرسی |
| I6 | تاریخ‌ها در DB همیشه **ISO (YYYY-MM-DD)**؛ شمسی فقط در لایهٔ نمایش | تبدیل در یک نقطه، نه همه‌جا |
| I7 | حذف فیزیکی ممنوع؛ `archived_at` | تاریخچه نباید بشکند |
| I8 | کلید خارجی و `ON DELETE RESTRICT` | دادهٔ یتیم نداشته باشیم |
| I9 | هر نوشتن در یک تراکنش DB انجام می‌شود که `stock_balance` را هم به‌روز کند | اتمیک بودن |
| I10 | `gtin` و `irc` در صورت وجود، یکتا (بدون تکرار) | جلوگیری از دو رکورد برای یک دارو |

---

## ۴) واحد اندازه‌گیری — تصمیم مهم

مسئله: گاهی «۳ کارتن ۲۰تایی» می‌شماریم، گاهی «۷ قلم باز». حل ساده و بدون خطا:

- `drug.pack_size` = تعداد واحد پایه در یک بسته (مثلاً ۲۰). اگر نامعلوم باشد `NULL`.
- همهٔ مقدارها در `movement.qty_units` به **واحد پایه** ذخیره می‌شوند (قرص/آمپول/mL).
- «۳ کارتن×۲۰» = `60`؛ «۷ قلم باز» = `7`؛ «۲ بسته + ۳ قلم» = `43`.
- اگر `pack_size` نامعلوم بود و کاربر با «بسته» کار می‌کند، واحد پایه = بسته و `pack_size=1`.
- نمایش «چند بسته و چند قلم» فقط در لایهٔ UI محاسبه می‌شود.

مبلغ (`price_rial`) همیشه `INTEGER` (ریال) — هیچ `Double` در مسیر داده.

---

## ۵) اسکیمای SQL (SQLite / Room)

```sql
-- ───────────────────────────────────────────────────────────────
-- فرآورده (کاتالوگ)
-- ───────────────────────────────────────────────────────────────
CREATE TABLE drug (
  id           INTEGER PRIMARY KEY AUTOINCREMENT,
  gtin         TEXT,                       -- ۱۴ رقمی، ممکن است NULL
  irc          TEXT,                       -- کد فرآورده، ممکن است NULL
  name_fa      TEXT NOT NULL CHECK (length(trim(name_fa)) > 0),
  name_en      TEXT,
  company      TEXT,                       -- صاحب پروانه/سازنده
  pack_size    INTEGER CHECK (pack_size IS NULL OR pack_size > 0),
  form         TEXT,                       -- شکل دارویی
  source       TEXT NOT NULL DEFAULT 'manual'
               CHECK (source IN ('import','manual','inquiry')),
  archived_at  TEXT,
  created_at   TEXT NOT NULL,
  updated_at   TEXT NOT NULL,
  CHECK (gtin IS NULL OR length(gtin) BETWEEN 8 AND 14),
  CHECK (irc  IS NULL OR length(irc)  BETWEEN 6 AND 16)
);
CREATE UNIQUE INDEX ux_drug_gtin ON drug(gtin) WHERE gtin IS NOT NULL;
CREATE UNIQUE INDEX ux_drug_irc  ON drug(irc)  WHERE irc  IS NOT NULL;
CREATE INDEX ix_drug_name ON drug(name_fa COLLATE NOCASE);

-- جست‌وجوی متنی سریع (به‌جای LIKE '%…%' که اسکن کامل جدول است)
CREATE VIRTUAL TABLE drug_fts USING fts4(
  name_fa, name_en, company, content='drug', content_rowid='id'
);

-- ───────────────────────────────────────────────────────────────
-- بچ / سری ساخت
-- ───────────────────────────────────────────────────────────────
CREATE TABLE batch (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  drug_id     INTEGER NOT NULL REFERENCES drug(id) ON DELETE RESTRICT,
  batch_code  TEXT    NOT NULL CHECK (length(trim(batch_code)) > 0),
  expiry_date TEXT    NOT NULL CHECK (expiry_date GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
  created_at  TEXT    NOT NULL
);
CREATE UNIQUE INDEX ux_batch ON batch(drug_id, batch_code, expiry_date);
CREATE INDEX ix_batch_expiry ON batch(expiry_date);          -- هشدار انقضا
CREATE INDEX ix_batch_drug   ON batch(drug_id, expiry_date); -- موجودی هر دارو به ترتیب انقضا

-- ───────────────────────────────────────────────────────────────
-- دفتر تراکنش (append-only)
-- ───────────────────────────────────────────────────────────────
CREATE TABLE movement (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  client_uuid TEXT    NOT NULL UNIQUE,        -- I3: ضد دوباره‌ثبت
  occurred_at TEXT    NOT NULL,               -- ISO-8601 با ثانیه (UTC)
  local_date  TEXT    NOT NULL,               -- YYYY-MM-DD محلی (برای گزارش روزانه)
  op          TEXT    NOT NULL CHECK (op IN ('COUNT','IN','OUT','WASTE','RETURN','ADJUST')),
  mode        TEXT    NOT NULL CHECK (mode IN ('single','carton','open')),
  drug_id     INTEGER NOT NULL REFERENCES drug(id) ON DELETE RESTRICT,
  batch_id    INTEGER          REFERENCES batch(id) ON DELETE RESTRICT,
  qty_units   INTEGER NOT NULL,               -- تغییر خالص (می‌تواند منفی باشد)
  before_units INTEGER NOT NULL DEFAULT 0,
  after_units  INTEGER NOT NULL DEFAULT 0,
  user_id     INTEGER          REFERENCES user(id) ON DELETE SET NULL,
  note        TEXT,
  device_id   TEXT    NOT NULL,
  synced_at   TEXT                            -- برای نسخهٔ چنددستگاهی آینده
);
CREATE INDEX ix_mv_drug_time ON movement(drug_id, occurred_at DESC);
CREATE INDEX ix_mv_time      ON movement(occurred_at DESC);
CREATE INDEX ix_mv_batch     ON movement(batch_id, occurred_at DESC);
CREATE INDEX ix_mv_pending   ON movement(occurred_at) WHERE synced_at IS NULL; -- ایندکس جزئی

-- ───────────────────────────────────────────────────────────────
-- خلاصهٔ موجودی (از دفتر بازسازی‌شدنی)
-- ───────────────────────────────────────────────────────────────
CREATE TABLE stock_balance (
  batch_id    INTEGER PRIMARY KEY REFERENCES batch(id) ON DELETE RESTRICT,
  drug_id     INTEGER NOT NULL REFERENCES drug(id) ON DELETE RESTRICT,
  qty_units   INTEGER NOT NULL DEFAULT 0 CHECK (qty_units >= 0),   -- I5
  updated_at  TEXT    NOT NULL
);
CREATE INDEX ix_sb_drug ON stock_balance(drug_id);

-- ───────────────────────────────────────────────────────────────
-- کاربر (شمارنده) — بدون رمز، فقط برای انتساب
-- ───────────────────────────────────────────────────────────────
CREATE TABLE user (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  name       TEXT NOT NULL CHECK (length(trim(name)) > 0),
  active     INTEGER NOT NULL DEFAULT 1,
  created_at TEXT NOT NULL
);
CREATE UNIQUE INDEX ux_user_name ON user(name COLLATE NOCASE);

-- ───────────────────────────────────────────────────────────────
-- کش استعلام آنلاین
-- ───────────────────────────────────────────────────────────────
CREATE TABLE inquiry (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  code          TEXT NOT NULL,
  kind          TEXT NOT NULL CHECK (kind IN ('gs1','uid','auth16','gtin','name')),
  status_code   INTEGER,
  error_code    INTEGER,
  raw_json      TEXT,
  name_fa       TEXT,
  name_en       TEXT,
  irc           TEXT,
  gtin          TEXT,
  company       TEXT,
  pack_size     INTEGER,
  uid           TEXT,
  checked_at    TEXT NOT NULL,
  expires_at    TEXT NOT NULL,      -- TTL: کد اصالت کوتاه، کاتالوگ بلند
  CHECK (expires_at > checked_at)
);
CREATE UNIQUE INDEX ux_inquiry_code ON inquiry(kind, code);
CREATE INDEX ix_inquiry_exp ON inquiry(expires_at);   -- پاکسازی دوره‌ای

-- ───────────────────────────────────────────────────────────────
-- لایسنس و تنظیمات و لاگ
-- ───────────────────────────────────────────────────────────────
CREATE TABLE license (
  id            INTEGER PRIMARY KEY CHECK (id = 1),   -- تک‌ردیفی
  payload_b64   TEXT NOT NULL,
  signature_b64 TEXT NOT NULL,
  device_hash   TEXT NOT NULL,
  issued_at     TEXT NOT NULL,
  expires_at    TEXT NOT NULL,
  last_seen_ts  TEXT NOT NULL          -- ضد عقب‌بردن ساعت
);

CREATE TABLE settings (
  key   TEXT PRIMARY KEY,
  value TEXT NOT NULL
);

CREATE TABLE audit_log (
  id     INTEGER PRIMARY KEY AUTOINCREMENT,
  ts     TEXT NOT NULL,
  event  TEXT NOT NULL,      -- license_check, import, export, migration, integrity
  detail TEXT
);
```

---

## ۶) چرا این ایندکس‌ها (شاهد، نه سلیقه)

- **`LIKE '%x%'` روی جدول بزرگ، اسکن کامل است** و با رشد داده خطی بدتر می‌شود؛ ایندکس B-Tree هم کمکی نمی‌کند چون پیشوند آزاد است. راه درست FTS است. (بنچمارک منتشرشده: در ۵٬۰۰۰ رکورد، FTS حدود **۹٫۴ برابر** سریع‌تر از LIKE: ‏۶٫۸ms در برابر ۶۴ms)
- برای لیست‌های صفحه‌بندی‌شده روی جدول بزرگ، **ایندکس جزئی/پوشا** تفاوت را از ~۱۵۸ms به ~۳ms می‌رساند (بنچمارک روی ۵۰۰ هزار ردیف).
- `Room` از `@Fts4` پشتیبانی می‌کند (FTS5 نیاز به SQL خام دارد). برای دامنهٔ ما (کاتالوگ دارو، حدود ۲۰۰ هزار ردیف) FTS4 کافی است و سازگاری بیشتری دارد.
- همهٔ ایندکس‌ها با `EXPLAIN QUERY PLAN` در تست تأیید می‌شوند تا «ایندکس تزئینی» نداشته باشیم.

---

## ۷) استراتژی مهاجرت (Migration)

1. اسکیمای Room با `exportSchema = true` و فایل‌های JSON نسخه‌ها در ریپو نگه داشته می‌شود.
2. هر تغییر = یک `Migration(n → n+1)` + یک تست مهاجرت با `MigrationTestHelper` روی دادهٔ نمونه.
3. قانون: مهاجرت‌ها **فقط افزودنی** (additive) باشند؛ تغییر نام/حذف ستون = ساخت جدول جدید + کپی + سواپ.
4. هیچ مهاجرتی نباید داده از دست بدهد؛ اگر لازم شد، ابتدا **پشتیبان خودکار** گرفته می‌شود.
5. `PRAGMA user_version` فقط از طریق Room مدیریت می‌شود؛ دستکاری دستی ممنوع.

---

## ۸) استراتژی پشتیبان (این بخش ریسک R5 را می‌بندد)

- پشتیبان زمان‌بندی‌شده: هر ۲۴ ساعت و هر ۵۰ ثبت، **فایل فشرده شده** در پوشهٔ خصوصی اپ + امکان «اشتراک‌گذاری» به فضای ابری کاربر.
- نگهداری ۵ نسخهٔ چرخشی (نه بیشتر، برای کنترل حجم).
- خروجی اکسل همچنان در دسترس است (برای مدیر)، ولی پشتیبان JSON کاملاً بازگردانی‌پذیر است.
- در نوار بالا همیشه نمایش داده می‌شود: «آخرین پشتیبان: ۳ ساعت پیش» — اگر بیشتر از ۳ روز شد، هشدار.

---

## ۹) سؤال‌های باز این فاز

1. آیا `pack_size` را از دیتابیس اکسل داروخانه می‌گیریم یا فقط از استعلام؟ (پیشنهاد: هر جا بود، اولویت Excel، بعد استعلام، بعد دستی)
2. آیا برای هر بچ، «تاریخ تولید» هم لازم است؟ (پیشنهاد: اختیاری، برای v1 کافی نیست)
3. نگهداری چند «انبار/قفسه» لازم است؟ (پیشنهاد v1: تک‌انبار؛ چند انبار در فاز بعد)

---

## ۱۰) تعریف «تمام‌شده» برای این فاز

- [x] همهٔ موجودیت‌ها با کلید، قید و ایندکس تعریف شده‌اند.
- [x] هر عدد اعشاری از مسیر داده حذف شده است.
- [x] مسیر حسابرسی (دفتر تراکنش) و بازسازی موجودی مشخص است.
- [x] قاعدهٔ «رکورد بی‌نام ممنوع» در سطح DB اعمال شده (`CHECK`).
- [x] مهاجرت و پشتیبان برنامه دارند.
- [x] ایندکس‌ها با شاهد فنی توجیه شده‌اند.

**قدم بعد (فاز ۲):** معماری فنی، ماژول‌ها، پروتکل لایسنس، بودجهٔ عملکرد و ساختار تست.
