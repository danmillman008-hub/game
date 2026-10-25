# چه چیزهایی را عمداً نصب نکردیم

هر مورد در تاریخ ۲۵ اکتبر ۲۰۲۶ با `git ls-remote` بررسی شد و **وجود دارد**؛ تصمیم
«نصب نکردن» آگاهانه است، نه به‌خاطر نبودِ ریپو.

| ریپو | چرا نه |
|---|---|
| `michaelbel/cuckcoder` | هارنس کامل (۳۵ rule + ۱۹ skill + ۲۲ subagent + MCP). ساختار و الگوی خودش را به پروژه تحمیل می‌کند؛ برای پروژه‌ای که معماری‌اش تثبیت شده مضر است، مخصوصاً چون MCP و subagent برای کار ما لازم نیست. |
| `ronjunevaldoz/kmp-agent-skills` | KMP-محور؛ ما Android-only هستیم و `expect/actual` نمی‌خواهیم. |
| `youndie/kotlin-skills` | KMP/Full-Stack؛ همان دلیل. |
| `Meet-Miyani/compose-skill` | پوشش وسیع اما تک‌فایلی و ناهم‌راستا (Navigation 3، Ktor، Paging 3)؛ با سه منبع هستهٔ ما هم‌پوشانی زیاد و تناقض احتمالی دارد. |
| `new-silvermoon/awesome-android-agent-skills` | سبک و خوب، ولی محتوایش زیرمجموعهٔ آن چیزی است که از `android-review` + `android-agent-skills` داریم؛ افزودنش فقط تکرار است. |
| `RidhwanAF/Android-AI-Agent-Skills` | نسخهٔ «Token-Efficient» جذاب است، ولی Hilt-محور است و ما Koin داریم؛ مرجعش با `krutikJain` هم‌پوشانی دارد. |
| `AlwaysLovePasta/claude-android-dev` | مخصوص Claude Code و Hilt-محور؛ ما ابزار-محور نیستیم و DI ما Koin است. |

## قانون بازگشت

اگر در فازی واقعاً کمبود داشتیم (مثلاً بازبینی امنیتی عمیق یا benchmark)، **یک مهارت
مشخص** از یکی از این مخازن را با همان روش `registry.json` اضافه می‌کنیم — نه کل مخزن.
