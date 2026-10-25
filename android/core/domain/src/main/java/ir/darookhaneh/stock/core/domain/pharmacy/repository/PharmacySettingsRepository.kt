package ir.darookhaneh.stock.core.domain.pharmacy.repository

import kotlinx.coroutines.flow.Flow

/**
 * تنظیمات رفتاری داروخانه (نه ظاهر و نه زبان).
 *
 * چرا جدا: این تنظیم‌ها رفتار محصول را عوض می‌کنند — مثل «استعلام خودکار تیتک» که
 * در نسخهٔ HTML یک چک‌باکس مستقل بود — و باید بدون اینترنت خوانده شوند.
 */
interface PharmacySettingsRepository {

    /**
     * وقتی کد اسکن/جست‌وجوشده در انبار محلی نبود، خودکار از تیتک پرسیده شود؟
     * پیش‌فرض: بله (همان رفتار نسخهٔ HTML).
     */
    val autoLookup: Flow<Boolean>

    suspend fun setAutoLookup(enabled: Boolean)
}
