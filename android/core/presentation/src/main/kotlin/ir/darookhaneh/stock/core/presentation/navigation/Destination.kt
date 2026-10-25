package ir.darookhaneh.stock.core.presentation.navigation

import androidx.navigation3.runtime.NavKey
import kotlinx.serialization.Serializable

/**
 * نقشهٔ ناوبری نسخهٔ ۱:
 * داشبورد → فهرست داروها → جزئیات دارو/بچ، و مسیر اسکن/ثبت.
 */
@Serializable
sealed interface Destination : NavKey {

    /** داشبورد: هشدار انقضا، موجودی کم، اقدامات سریع. */
    @Serializable
    data object Dashboard : Destination

    /** فهرست داروها با جست‌وجو. */
    @Serializable
    data object Drugs : Destination

    /** ثبت سریع: دارو → عملیات → مقدار → ثبت، در یک صفحه. */
    @Serializable
    data object Record : Destination

    /**
     * استعلام کد از سامانهٔ تیتک (مقصد مستقل).
     *
     * چرا مقصد جدا: پیش‌تر استعلام یک دکمهٔ کوچک داخل کارت «پیدا نشد» بود و
     * کارفرما آن را «دکمه/روش مشخص» به حساب نیاورد. اکنون یک صفحهٔ کامل است.
     */
    @Serializable
    data class Lookup(val code: String? = null) : Destination

    /** تاریخچهٔ سراسری همهٔ عملیات. */
    @Serializable
    data object History : Destination

    /** جزئیات یک دارو و بچ‌های آن. */
    @Serializable
    data class DrugDetail(val drugId: Long) : Destination

    /** اسکن بارکد و جریان ثبت موجودی. */
    @Serializable
    data object Scanner : Destination

    /** ثبت دستی دارو؛ با کد اسکن‌شدهٔ ناشناخته هم پر می‌شود. */
    @Serializable
    data class AddDrug(val gtin: String? = null, val nameHint: String? = null) : Destination

    @Serializable
    data class Setting(
        val destination: SettingDestination = SettingDestination.Main
    ) : Destination
}

enum class SettingDestination {
    Main,
    Appearance,
    OtherSettings,
    YourData,
    AboutApp,
    OpenSource,
    Notification,
}
