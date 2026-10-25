package ir.darookhaneh.stock.core.model.setting

/**
 * زبان‌های پشتیبانی‌شده.
 * محصول داروخانه فارسی است؛ `PERSIAN` زبان پیش‌فرض و مقصد fallback است.
 */
enum class AppLanguage(val isoCode: String) {
    PERSIAN("fa"),
    ENGLISH("en"),
    VIETNAMESE("vi"),
    ;

    companion object {
        val DEFAULT = PERSIAN

        fun fromIsoCode(code: String?): AppLanguage =
            entries.firstOrNull { it.isoCode == code } ?: DEFAULT
    }
}

fun String?.toAppLanguage(): AppLanguage = AppLanguage.fromIsoCode(this)
