# ۰۵ت — مشخصات سنجش و تصحیح پاسخ

**وضعیت:** الگوریتم‌ها **VERIFIED_STATIC** (داده + قرارداد) با اجرای مرجع در `tools/lesson_dsl.py`؛
ترتیب دقیق رخدادها در UI **INFERRED** (بدون اجرا).

## ۱. قرارداد داده

```python
Block   = { name, codelang, source, gaps: Gap[], distractors: str[], inputs: ValidatedInput[] }
Gap     = { start, end }          # آفست کاراکتر روی source
Input   = { start, end }
Selection = { items: [{value, correct, html}], multiple: bool }
```

## ۲. الگوریتم تصحیح (مرجع، اجراشده)

```python
def grade_block(block, chips: dict[int, str], typed: dict[int, str]) -> Result:
    for g in block.gaps:                       # هر جای خالی مستقل
        expected = block.source[g.start:g.end]
        got      = chips.get(g.index)          # چیپ کشیده‌شده
        if got is None:            → UNANSWERED
        elif got == expected:      → CORRECT    (تساوی دقیق، بدون normalize)
        else:                      → WRONG
    for v in block.inputs:
        expected = block.source[v.start:v.end]
        got      = typed.get(v.index, "")
        CORRECT iff got == expected
    block_ok = all gaps/inputs CORRECT and no UNANSWERED
```

**تصمیم‌های مهم (با شاهد):**

| تصمیم | انتخاب Mimo | شاهد | توصیهٔ ما |
|---|---|---|---|
| تطبیق رشته | **تساوی دقیق** (بدون trim/case-fold) | عرض میانهٔ بازه ۴ کاراکتر، ۸۳۷ بازهٔ «فضای خالی» | برای درس کد: exact + trim فاصله‌های لبه؛ برای متنی: normalize |
| ترتیب بررسی | مستقل برای هر جای خالی | ۲۹,۰۹۳ بازهٔ مستقل | همان |
| بازخورد جزئی | **ندارد** (یک `wrong` برای کل بلوک) | ۱۹,۱۰۱ `p visible-if="wrong"` در کل بسته، بدون `visible-if="wrong:gap1"` | در محصول هدف: بازخورد per-gap لازم است |
| تلاش مجدد | آزاد تا درست شدن | رشته‌های `try_again`, «درست نشد» | نگه دارید |
| راه‌حل | پس از تأیید (`see_solution_confirm_dialog_*`) | ۷ رشته | نگه دارید؛ اما فقط برای درس کد |

## ۳. `selection`

```python
def grade_selection(sel, chosen: set[int]) -> bool:
    return chosen == {v for v, c, _ in sel.items if c}
```
* همهٔ ۷,۳۵۶ بلوک `multiple="multiple"` هستند ⇒ «همهٔ درست‌ها» الزامی است، نه «هر درست».
* دقیقاً یک `correct=true` در هر بلوک (۷,۳۵۶/۷,۳۵۶).
* ۱۲۵ بلوک `value` تکراری دارند ⇒ اگر `value` کلید باشد، تصحیح مبهم است. **ریسک ثبت‌شده.**

## ۴. `database`

```
1) اجرای bootstrapScript روی SQLite در حافظه (seed)
2) اجرای کد/دستور کاربر
3) مقایسهٔ ساختاری: مجموعهٔ جدول‌ها، نام ستون‌ها، مجموعهٔ ردیف‌ها (بدون ترتیب)
4) اگر <output> موجود: مقایسهٔ متن خروجی
```
کلاس: **INFERRED** — شاهد: `sourceDatabaseTables`/`solutionDatabaseTables` در درس‌های کدی،
`<output>` در ۵,۷۸۴ بلوک، و نبود منطق تصحیح SQL در محتوای ماندگار. محل اجرا (کلاینت یا سرور) **UNKNOWN**.

## ۵. درس کدی (executable) — بزرگ‌ترین شکاف

یافتهٔ مهم: **هیچ فایل تست در محتوای درس کدی وجود ندارد.**
کلیدهای `executableContent` فقط: `instructions`, `preselectedFileIndex`, `hasVisualOutput`,
`files[{name, codeLanguage, content, solvedContent}]`, `hints[{title, content}]`،
و در برخی درس‌ها `httpOptions`, `sourceDatabaseTables`, `solutionDatabaseTables`.

⇒ نتیجه‌گیری (INFERRED، اطمینان MEDIUM): تصحیح درس کدی **سمت سرور** انجام می‌شود؛
کلاینت کد را به `/v1/code/runfiles` می‌فرستد و پاسخ درست/نادرست برمی‌گردد
(پشتوانه: endpoint `/v1/code/runfiles`, `/v1/code`, و نبود تست در کلاینت).
اگر بخواهیم محصول مستقل باشد، **باید** تصحیح را یا در کلاینت (اجرای محلی + diff رفتاری) یا در
سرویس اجرای خودمان انجام دهیم — این بخش از Mimo قابل کپی نیست.

## ۶. اختلاف نسخهٔ سخت (`hardModeContent`)

* ۶,۰۵۸ درس نسخهٔ دوم دارند؛ ۳,۲۵۵ مورد `hardModeSelected=true` و ۲,۸۰۳ مورد `null`.
* `hardModeSelected` یعنی **کدام نسخه در عمل منتشر شده** (شاهد: نام + تفاوت تعداد).
* برای محصول هدف: نگه داشتن دو نسخه برای هر سؤال، هزینهٔ تألیف را دوبرابر می‌کند؛
  توصیه: نسخهٔ «دشوار» فقط برای سؤالات کلیدی کنکور.

## ۷. بردارهای آزمون

`fixtures/` + `TEST_VECTORS.md` + `../16_TESTS/test_lesson_dsl.py` (pytest؛ همه سبز).
