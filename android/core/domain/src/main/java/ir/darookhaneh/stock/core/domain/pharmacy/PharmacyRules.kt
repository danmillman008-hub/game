package ir.darookhaneh.stock.core.domain.pharmacy

import ir.darookhaneh.stock.core.model.pharmacy.InventoryEventType

/**
 * قواعد خالص دامنه — بدون Android، بدون Room، بدون شبکه.
 * همهٔ تصمیم‌های «اجازه دارد / ندارد» در همین فایل است تا تست پذیر باشد
 * و UI و لایهٔ داده مجبور نباشند قاعده را دوباره پیاده کنند.
 */

/** دلیل رد عملیات. */
sealed interface PharmacyError {
    val message: String

    data object BlankDrugName : PharmacyError {
        override val message = "نام دارو نباید خالی باشد."
    }

    data object MissingBatchIdentity : PharmacyError {
        override val message = "حداقل یکی از شمارهٔ بچ یا تاریخ انقضا لازم است."
    }

    data object DuplicateBatch : PharmacyError {
        override val message = "این بچ با همین شماره و تاریخ انقضا قبلاً ثبت شده است."
    }

    data object InvalidAmount : PharmacyError {
        override val message = "مقدار وارد‌شده معتبر نیست."
    }

    data object NegativeQuantity : PharmacyError {
        override val message = "موجودی نمی‌تواند منفی باشد."
    }

    data object InsufficientStock : PharmacyError {
        override val message = "موجودی کافی نیست."
    }

    data object DrugNotFound : PharmacyError {
        override val message = "دارو یافت نشد."
    }

    data object BatchNotFound : PharmacyError {
        override val message = "بچ یافت نشد."
    }

    data object StorageFailure : PharmacyError {
        override val message = "ذخیره‌سازی انجام نشد."
    }
}

class PharmacyException(val error: PharmacyError) : IllegalStateException(error.message)

/** قواعد ساخت دارو. */
object DrugRules {

    const val MIN_NAME_LENGTH = 2

    /** نام اجباری است؛ IRC و GTIN هیچ‌کدام اجباری نیستند. */
    fun validateName(name: String): PharmacyError? {
        val trimmed = name.trim()
        return when {
            trimmed.isEmpty() -> PharmacyError.BlankDrugName
            trimmed.length < MIN_NAME_LENGTH -> PharmacyError.BlankDrugName
            else -> null
        }
    }

    fun normalizeGtin(gtin: String?): String? = gtin?.trim()?.takeIf { it.isNotEmpty() }

    /**
     * IRC اختیاری است: مقدار خالی به null تبدیل می‌شود تا ستون معنای «ثبت‌نشده» داشته باشد
     * و چند دارو بتوانند IRC نداشته باشند (بدون UNIQUE).
     */
    fun normalizeIrc(irc: String?): String? = irc?.trim()?.takeIf { it.isNotEmpty() }
}

/** قواعد بچ. */
object BatchRules {

    /**
     * در SQLite مقدار NULL در قید یکتایی تکرارپذیر است؛ پس بچِ «بی‌نام و بی‌تاریخ»
     * می‌توانست چندبار ثبت شود. این قاعده جلوی آن را می‌گیرد:
     * حداقل یکی از شمارهٔ بچ یا تاریخ انقضا باید وجود داشته باشد.
     */
    fun validateIdentity(batchNumber: String?, expiryDate: Long?): PharmacyError? {
        val hasNumber = !batchNumber.isNullOrBlank()
        return if (hasNumber || expiryDate != null) null else PharmacyError.MissingBatchIdentity
    }

    /** کلید منطقی یکتایی بچ. */
    fun identityKey(batchNumber: String?, expiryDate: Long?): String =
        "${batchNumber?.trim().orEmpty()}|${expiryDate ?: -1L}"
}

/** قواعد موجودی — تنها مرجع مجاز تغییر `quantity`. */
object InventoryRules {

    /**
     * موجودی جدید را محاسبه می‌کند یا دلیل رد را برمی‌گرداند.
     * هیچ‌وقت مقدار منفی برنمی‌گرداند.
     *
     * @param current موجودی فعلی بچ
     * @param type نوع رخداد
     * @param amount برای RECEIVE/DISPENSE مقدار مثبت (تعداد)،
     *               برای ADJUSTMENT تغییر با علامت، برای COUNT مقدار شمارش‌شده
     */
    fun quantityAfter(
        current: Int,
        type: InventoryEventType,
        amount: Int,
    ): Result<Int> {
        if (current < 0) return Result.failure(PharmacyException(PharmacyError.NegativeQuantity))

        val next = when (type) {
            InventoryEventType.RECEIVE -> {
                if (amount <= 0) return invalidAmount()
                current + amount
            }

            InventoryEventType.DISPENSE -> {
                if (amount <= 0) return invalidAmount()
                if (amount > current) {
                    return Result.failure(PharmacyException(PharmacyError.InsufficientStock))
                }
                current - amount
            }

            InventoryEventType.ADJUSTMENT -> {
                if (amount == 0) return invalidAmount()
                val candidate = current + amount
                if (candidate < 0) {
                    return Result.failure(PharmacyException(PharmacyError.NegativeQuantity))
                }
                candidate
            }

            InventoryEventType.COUNT -> {
                if (amount < 0) {
                    return Result.failure(PharmacyException(PharmacyError.NegativeQuantity))
                }
                amount
            }
        }

        return Result.success(next)
    }

    /** تغییر خالصی که باید در `inventory_event.quantityDelta` ثبت شود. */
    fun delta(current: Int, next: Int): Int = next - current

    private fun <T> invalidAmount(): Result<T> =
        Result.failure(PharmacyException(PharmacyError.InvalidAmount))
}

/** آستانه‌های نمایشی (قابل تغییر در تنظیمات؛ فعلاً مقدار پیش‌فرض). */
object PharmacyThresholds {
    /** موجودی کم برای مجموع بچ‌های فعال یک دارو، نه برای هر بچ. */
    const val DEFAULT_LOW_STOCK_THRESHOLD = 10

    /** «بچ نزدیک انقضا» بر حسب روز. */
    const val DEFAULT_EXPIRING_SOON_DAYS = 90L

    const val MILLIS_PER_DAY = 24L * 60 * 60 * 1000
}
