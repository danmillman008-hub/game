# ۱۷ب — مدل دادهٔ هدف (قابل پیاده‌سازی)

تفاوت بنیادی با Mimo: **سؤال مستقل از درس** + **نسخه‌داری در سطح سؤال** + **تشخیص خطا**.

```sql
-- مفاهیم و پیش‌نیازها (Mimo ندارد)
CREATE TABLE concept (id TEXT PRIMARY KEY, title TEXT, subject TEXT, grade INT);
CREATE TABLE concept_edge (src TEXT, dst TEXT, kind TEXT, PRIMARY KEY (src,dst,kind));

-- بانک سؤال (هستهٔ کنکور؛ در Mimo مفهومی معادل ندارد)
CREATE TABLE question (
  id TEXT PRIMARY KEY,
  concept_id TEXT REFERENCES concept(id),
  stem_md TEXT NOT NULL,
  type TEXT NOT NULL,            -- mcq | multi | numeric | fill | order
  difficulty SMALLINT NOT NULL,  -- 1..5
  source TEXT, exam_year INT, exam_field TEXT,
  answer_key JSONB NOT NULL,
  answer_key_version INT NOT NULL,
  explanation_md TEXT,
  media JSONB
);
CREATE TABLE option (
  id TEXT PRIMARY KEY, question_id TEXT REFERENCES question(id),
  idx SMALLINT, body_md TEXT,
  is_correct BOOLEAN NOT NULL,
  error_code TEXT                  --  تشخیص خطای رایج (کلید ارزش)
);

-- محتوای آموزشی (الهام از Mimo، ساده‌شده)
CREATE TABLE lesson (id TEXT PRIMARY KEY, concept_id TEXT, body_dsl TEXT, version INT);
CREATE TABLE chapter (id TEXT PRIMARY KEY, title TEXT, item_ids JSONB);

-- تعامل و پیشرفت
CREATE TABLE attempt (
  id TEXT PRIMARY KEY, question_id TEXT, user_id TEXT, session_id TEXT,
  started_at TIMESTAMPTZ, answered_at TIMESTAMPTZ, duration_ms INT,
  response JSONB, is_correct BOOLEAN, error_code TEXT, hint_level SMALLINT
);
CREATE TABLE mastery (
  user_id TEXT, concept_id TEXT, score REAL, stability REAL, difficulty REAL,
  last_review TIMESTAMPTZ, next_review TIMESTAMPTZ, updated_at TIMESTAMPTZ,
  PRIMARY KEY (user_id, concept_id)
);

-- آزمون
CREATE TABLE exam (id TEXT PRIMARY KEY, title TEXT, bluePrint JSONB,
                   duration_min INT, started_at TIMESTAMPTZ, finished_at TIMESTAMPTZ);
CREATE TABLE exam_answer (exam_id TEXT, question_id TEXT, response JSONB,
  is_correct BOOLEAN, duration_ms INT, position INT, PRIMARY KEY (exam_id, question_id));
CREATE TABLE exam_score (exam_id TEXT PRIMARY KEY, raw INT, percent REAL,
  scaled REAL, national_rank_est INT, computed_at TIMESTAMPTZ);

-- صف همگام (الگوی outbox از Mimo، با idempotency)
CREATE TABLE outbox (id TEXT PRIMARY KEY, kind TEXT, payload JSONB, attempts INT DEFAULT 0);
```

## قواعد الزامی

| قاعده | دلیل |
|---|---|
| `answer_key_version` | کلید تصحیح ممکن است اصلاح شود ⇒ آمار باید تفکیک شود |
| `error_code` روی گزینه | تشخیص خطا؛ Mimo ندارد |
| نرمال‌سازی متن سؤال | جستجو + جستجوی FTS5 |
| `attempt` فقط append | تحلیل و بازپخش |
| `mastery` جدا از `attempt` | قابل بازسازی از attempt |
| چندسکویی | SQLite محلی + Postgres سرور با اسکیمای مشترک |
