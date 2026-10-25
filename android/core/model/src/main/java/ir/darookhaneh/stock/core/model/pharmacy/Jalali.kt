package ir.darookhaneh.stock.core.model.pharmacy

import java.time.Instant
import java.time.LocalDate
import java.time.ZoneId

/**
 * تاریخ شمسی — بدون هیچ وابستگی خارجی.
 *
 * چرا خودمان نوشتیم: همهٔ تاریخ‌های دارو (انقضا) در داروخانه شمسی خوانده می‌شوند و
 * نسخهٔ HTML هم شمسی بود؛ افزودن یک کتابخانهٔ تقویم فقط برای تبدیل، حجم APK را
 * بی‌دلیل بالا می‌برد.
 *
 * الگوریتم: تبدیل متعارف جلالی↔میلادی (همان روشی که در `jalaali-js` استفاده شده)،
 * با تست‌های شناخته‌شده: ۱۴۰۳/۰۱/۰۱ = ۲۰۲۴-۰۳-۲۰ و ۱۴۰۳/۱۲/۳۰ = ۲۰۲۵-۰۳-۲۰.
 */
data class JalaliDate(val year: Int, val month: Int, val day: Int) {

    val isValid: Boolean
        get() = year in 1200..1600 && month in 1..12 && day in 1..monthLength(year, month)

    /** ۱۴۰۳/۰۷/۰۳ */
    fun format(separator: Char = '/'): String =
        "%04d%c%02d%c%02d".format(year, separator, month, separator, day)

    /** ۳ مهر ۱۴۰۳ */
    fun formatLong(): String = "$day ${monthName(month)} $year"

    /** همان تاریخ در تقویم میلادی. */
    fun toGregorian(): LocalDate = jalaliToGregorian(year, month, day)

    fun toEpochMillis(zone: ZoneId = ZoneId.systemDefault()): Long =
        toGregorian().atStartOfDay(zone).toInstant().toEpochMilli()

    companion object {

        val MONTH_NAMES = listOf(
            "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
            "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند",
        )

        fun monthName(month: Int): String = MONTH_NAMES.getOrElse(month - 1) { "" }

        /** طول ماه شمسی؛ ۶ ماه اول ۳۱ روز، ۶ ماه دوم ۳۰ روز و اسفند ۲۹/۳۰. */
        fun monthLength(year: Int, month: Int): Int {
            if (month in 1..6) return 31
            if (month in 7..11) return 30
            if (month == 12) return if (isLeapYear(year)) 30 else 29
            return 0
        }

        /** سال کبیسهٔ شمسی (الگوریتم ۳۳ ساله). */
        fun isLeapYear(year: Int): Boolean {
            val mod = ((year + 2346) % 2820 + 2820) % 2820
            return ((mod + 38) * 682) % 2816 < 682
        }

        fun of(year: Int, month: Int, day: Int): JalaliDate? =
            JalaliDate(year, month, day).takeIf { it.isValid }

        /** از تاریخ میلادی. */
        fun from(gregorian: LocalDate): JalaliDate =
            gregorianToJalali(gregorian.year, gregorian.monthValue, gregorian.dayOfMonth)

        /** از میلی‌ثانیهٔ یونیکس (نیمه‌شب محلی). */
        fun fromEpochMillis(millis: Long, zone: ZoneId = ZoneId.systemDefault()): JalaliDate =
            from(Instant.ofEpochMilli(millis).atZone(zone).toLocalDate())

        /**
         * پارس ورودی کاربر: `1403/7/3`، `1403-07-03`، `14030703` یا `1403/7`
         * (روزِ خالی = آخرین روز ماه، مثل نسخهٔ HTML).
         * سال دو رقمی با +1400 اصلاح می‌شود.
         */
        fun parse(text: String?): JalaliDate? {
            val digits = text?.let(::latinDigits)?.filter { it.isDigit() || it == '/' || it == '-' }
                ?: return null
            val parts = digits.split('/', '-').filter { it.isNotEmpty() }
            if (parts.isEmpty()) return null
            if (parts.size == 1 && parts[0].length == 8) {
                val raw = parts[0]
                return of(raw.substring(0, 4).toInt(), raw.substring(4, 6).toInt(), raw.substring(6, 8).toInt())
            }
            var year = parts.getOrNull(0)?.toIntOrNull() ?: return null
            if (year < 100) year += 1400
            val month = parts.getOrNull(1)?.toIntOrNull() ?: return null
            if (month !in 1..12) return null
            val day = parts.getOrNull(2)?.toIntOrNull() ?: monthLength(year, month)
            return of(year, month, day)
        }

        /** اعداد فارسی/عربی را به لاتین تبدیل می‌کند (ورودی صفحه‌کلید فارسی). */
        fun latinDigits(text: String): String = buildString(text.length) {
            for (ch in text) {
                append(
                    when (ch) {
                        in '۰'..'۹' -> '0' + (ch - '۰')
                        in '٠'..'٩' -> '0' + (ch - '٠')
                        else -> ch
                    }
                )
            }
        }

        /** عدد را با ارقام فارسی برمی‌گرداند؛ برای نمایش. */
        fun toPersianDigits(value: Any?): String =
            value.toString().map { ch ->
                if (ch in '0'..'9') '۰' + (ch - '0') else ch
            }.joinToString("")

        private fun gregorianToJalali(gy: Int, gm: Int, gd: Int): JalaliDate {
            val leap = if ((gy % 4 == 0 && gy % 100 != 0) || gy % 400 == 0) 1 else 0
            val monthDays = intArrayOf(0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
            var days = 355666 + (365 * gy) + ((gy + 3 + (if (gm > 2) 1 else 0)) / 4) -
                ((gy + 99) / 100) + ((gy + 399) / 400) + gd +
                monthDays[gm - 1] + (if (gm > 2) leap else 0)

            var jy = -1595 + (33 * (days / 12053))
            days %= 12053
            jy += 4 * (days / 1461)
            days %= 1461
            if (days > 365) {
                jy += (days - 1) / 365
                days = (days - 1) % 365
            }
            val jm: Int
            val jd: Int
            if (days < 186) {
                jm = 1 + (days / 31)
                jd = 1 + (days % 31)
            } else {
                jm = 7 + ((days - 186) / 30)
                jd = 1 + ((days - 186) % 30)
            }
            return JalaliDate(jy, jm, jd)
        }

        private fun jalaliToGregorian(jy0: Int, jm: Int, jd: Int): LocalDate {
            val jy = jy0 + 1595
            var days = -355668 + (365 * jy) + ((jy / 33) * 8) + (((jy % 33) + 3) / 4) + jd +
                (if (jm < 7) (jm - 1) * 31 else ((jm - 7) * 30 + 186))

            var gy = 400 * (days / 146097)
            days %= 146097
            if (days > 36524) {
                gy += 100 * ((days - 1) / 36524)
                days = (days - 1) % 36524
                if (days >= 365) days++
            }
            gy += 4 * (days / 1461)
            days %= 1461
            if (days > 365) {
                gy += (days - 1) / 365
                days = (days - 1) % 365
            }
            var gd = days + 1
            val isLeap = (gy % 4 == 0 && gy % 100 != 0) || gy % 400 == 0
            val monthDays = intArrayOf(
                0, 31, if (isLeap) 29 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,
            )
            var gm = 1
            while (gm <= 12 && gd > monthDays[gm]) {
                gd -= monthDays[gm]
                gm++
            }
            return LocalDate.of(gy, gm.coerceAtMost(12), gd.coerceIn(1, 31))
        }
    }
}

/** نمایش استاندارد تاریخ برای UI: `۱۴۰۳/۰۷/۰۳` یا `—`. */
fun formatJalali(millis: Long?, zone: ZoneId = ZoneId.systemDefault()): String =
    millis?.let { JalaliDate.toPersianDigits(JalaliDate.fromEpochMillis(it, zone).format()) } ?: "—"

/** نمایش تاریخ انقضا با وضعیت: «۳ روز پیش» / «۱۲ روز مانده» / «بدون تاریخ». */
fun daysUntil(millis: Long, now: Long, millisPerDay: Long = 86_400_000L): Long =
    Math.floorDiv(millis - now, millisPerDay)
