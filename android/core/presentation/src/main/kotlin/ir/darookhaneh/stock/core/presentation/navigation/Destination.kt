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

    /** جزئیات یک دارو و بچ‌های آن. */
    @Serializable
    data class DrugDetail(val drugId: Long) : Destination

    /** اسکن بارکد و جریان ثبت موجودی. */
    @Serializable
    data object Scanner : Destination

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
