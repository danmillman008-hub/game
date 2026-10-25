package ir.darookhaneh.stock.core.data.pharmacy

import android.content.Context
import ir.darookhaneh.stock.core.domain.pharmacy.repository.PharmacySettingsRepository
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow

/**
 * ذخیرهٔ تنظیمات داروخانه در SharedPreferences.
 *
 * چرا SharedPreferences و نه Room/DataStore: دو مقدار بولی است، باید همگام و بی‌درنگ
 * در دسترس باشد (صفحهٔ ثبت بلافاصله بعد از تغییر رفتار عوض شود) و هیچ مهاجرت اسکیمایی
 * لازم نداشته باشد. فایل جدا از دیتابیس موجودی است تا پشتیبان‌گیری/پاک‌کردن داده‌ها
 * تنظیمات را از بین نبرد.
 */
class PharmacySettingsRepositoryImpl(context: Context) : PharmacySettingsRepository {

    private val prefs = context.applicationContext
        .getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)

    private val autoLookupState = MutableStateFlow(prefs.getBoolean(KEY_AUTO_LOOKUP, true))

    override val autoLookup: Flow<Boolean> = autoLookupState.asStateFlow()

    override suspend fun setAutoLookup(enabled: Boolean) {
        prefs.edit().putBoolean(KEY_AUTO_LOOKUP, enabled).apply()
        autoLookupState.value = enabled
    }

    private companion object {
        const val PREFS_NAME = "pharmacy-settings"
        const val KEY_AUTO_LOOKUP = "auto_lookup"
    }
}
