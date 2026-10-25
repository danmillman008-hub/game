package ir.darookhaneh.stock.utils

import android.content.Context
import java.io.File
import java.io.PrintWriter
import java.io.StringWriter
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

/**
 * ثبت آخرین کرش در یک فایل داخل حافظهٔ خود اپ.
 *
 * چرا لازم شد: نسخهٔ ۲.۰.۰ روی گوشی کاربر «بعد از ثبت اولین دارو» بسته شد و هیچ
 * لاگی در دسترس نبود. از این پس هر کرش با نسخه، مدل دستگاه و stack trace کامل
 * ذخیره می‌شود؛ در شروع بعدی همان متن به کاربر نشان داده و با یک دکمه کپی می‌شود.
 *
 * این کار هیچ داده‌ای به اینترنت نمی‌فرستد (آفلاین اول): فقط روی دستگاه.
 */
class CrashReporter(private val context: Context) {

    private val file: File get() = File(context.filesDir, FILE_NAME)

    fun install() {
        val previous = Thread.getDefaultUncaughtExceptionHandler()
        Thread.setDefaultUncaughtExceptionHandler { thread, throwable ->
            runCatching { write(thread, throwable) }
            previous?.uncaughtException(thread, throwable)
        }
    }

    /** متن آخرین کرش، یا null اگر کرشی ثبت نشده باشد. */
    fun readLast(): String? = runCatching {
        file.takeIf { it.exists() && it.length() > 0 }?.readText()
    }.getOrNull()

    fun clear() {
        runCatching { if (file.exists()) file.delete() }
    }

    private fun write(thread: Thread, throwable: Throwable) {
        val buffer = StringWriter()
        throwable.printStackTrace(PrintWriter(buffer))
        val header = buildString {
            appendLine("=== گزارش خطای اپ انبار دارو ===")
            appendLine("زمان: " + SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.US).format(Date()))
            appendLine("اندروید: ${android.os.Build.VERSION.SDK_INT} (${android.os.Build.MODEL})")
            appendLine("نسخهٔ اپ: ${appVersion()}")
            appendLine("نخ: ${thread.name}")
            appendLine("--------------------------------")
        }
        file.writeText(header + buffer.toString())
    }

    private fun appVersion(): String = runCatching {
        val info = context.packageManager.getPackageInfo(context.packageName, 0)
        "${info.versionName} (${info.longVersionCode})"
    }.getOrDefault("?")

    companion object {
        const val FILE_NAME = "last-crash.txt"
    }
}
