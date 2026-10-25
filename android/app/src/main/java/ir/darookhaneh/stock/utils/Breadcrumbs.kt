package ir.darookhaneh.stock.utils

import android.content.Context
import java.io.File
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

/**
 * «ردپای مسیر» — آخرین کارهایی که کاربر در اپ انجام داده، تا اگر کرش کرد بدانیم کجا بود.
 *
 * چرا لازم شد: کاربر گفت «بعد از ثبت اولین دارو کرش می‌کند» و هیچ لاگی در دست نبود.
 * stack trace می‌گوید کجا افتاد، ولی نه «قبلش چه کاری انجام شد». این فایل آن شکاف را
 * پر می‌کند: هر تغییر صفحه و هر عملیات مهم یک خط با زمان ثبت می‌شود و در گزارش خطا
 * ضمیمه می‌گردد. نوشتن سبک و همگام است (چند خط در ثانیه) و هیچ اثری روی UI ندارد.
 */
object Breadcrumbs {

    private const val FILE_NAME = "breadcrumbs.log"
    private const val MAX_BYTES = 64 * 1024
    private val timeFormat = SimpleDateFormat("HH:mm:ss.SSS", Locale.US)

    @Volatile
    private var file: File? = null

    fun init(context: Context) {
        file = File(context.filesDir, FILE_NAME)
        mark("اپ باز شد")
    }

    /** یک رویداد را ثبت می‌کند. هرگز استثنا نمی‌دهد. */
    fun mark(tag: String) {
        val target = file ?: return
        runCatching {
            val line = "${timeFormat.format(Date())}  $tag\n"
            target.appendText(line)
            if (target.length() > MAX_BYTES) {
                val tail = target.readLines().takeLast(400)
                target.writeText(tail.joinToString("\n", postfix = "\n"))
            }
        }
    }

    /** محتوای ردپا برای ضمیمه کردن به گزارش خطا. */
    fun tail(lines: Int = 40): String = runCatching {
        file?.takeIf { it.exists() }?.readLines()?.takeLast(lines)?.joinToString("\n").orEmpty()
    }.getOrDefault("")
}
