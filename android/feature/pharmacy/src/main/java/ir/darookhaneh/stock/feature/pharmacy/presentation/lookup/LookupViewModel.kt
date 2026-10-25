package ir.darookhaneh.stock.feature.pharmacy.presentation.lookup

import androidx.compose.runtime.Immutable
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import ir.darookhaneh.stock.core.domain.pharmacy.PharmacyException
import ir.darookhaneh.stock.core.domain.pharmacy.repository.DrugRepository
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.CreateDrugWithStockUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.LookupDrugCodeUseCase
import ir.darookhaneh.stock.core.model.pharmacy.Drug
import ir.darookhaneh.stock.core.model.pharmacy.DrugLookupResult
import ir.darookhaneh.stock.core.model.pharmacy.JalaliDate
import ir.darookhaneh.stock.core.model.pharmacy.LookupException
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

/**
 * صفحهٔ مستقل «استعلام از سامانهٔ تیتک».
 *
 * چرا صفحهٔ جدا و نه یک دکمهٔ گوشهٔ صفحهٔ ثبت: در نسخهٔ ۲.۱.۰ استعلام فقط یک
 * TextButton کوچک داخل کارت «دارویی پیدا نشد» بود؛ کارفرما حق داشت بگوید
 * «نه دکمهٔ مشخصی گذاشتی نه روش مشخصی». اکنون یک مقصد مستقل در ناوبری است با
 * ورودی کد، دکمهٔ اصلی بزرگ، توضیح روش، و نتیجهٔ کامل.
 */
@Immutable
data class LookupScreenState(
    /** کد واردشده توسط کاربر (هر شکلی: بارکد، IRC، رهگیری، یا با فاصله/خط‌تیره). */
    val input: String = "",
    val isLoading: Boolean = false,
    val result: DrugLookupResult? = null,
    val error: String? = null,
    /** اگر دارو از نتیجه ساخته/پیدا شد، شناسهٔ آن برای رفتن به جزئیات. */
    val openDrugId: Long? = null,
    val notice: String? = null,
) {
    /** کد نرمال‌شده (فقط رقم، ارقام فارسی → لاتین). */
    val code: String get() = JalaliDate.latinDigits(input).filter(Char::isDigit)

    val kind: LookupCodeKind get() = LookupCodeKind.of(code)

    /** دکمهٔ استعلام فقط با کد معتبر فعال است. */
    val canLookup: Boolean get() = !isLoading && kind != LookupCodeKind.UNKNOWN

    val canApply: Boolean get() = !isLoading && result != null
}

/** نوع کد از روی طول آن — همان قاعدهٔ اپ رسمی تیتک و نسخهٔ HTML. */
enum class LookupCodeKind(val label: String) {
    GTIN("بارکد کالا (GTIN/EAN) → CheckBarcode"),
    AUTH_16("کد اصالت ۱۶ رقمی → CheckSixteenCode"),
    UID("شناسهٔ رهگیری ۲۰ رقمی → CheckUid"),
    GS1("بارکد GS1 طولانی (حاوی بچ/انقضا) → CheckBarcode"),
    UNKNOWN("کد نامعتبر — حداقل ۸ رقم لازم است");

    companion object {
        fun of(digits: String): LookupCodeKind = when {
            digits.length >= 21 -> GS1
            digits.length == 20 -> UID
            digits.length == 16 -> AUTH_16
            digits.length in 8..15 -> GTIN
            else -> UNKNOWN
        }
    }
}

sealed interface LookupScreenAction {
    data class OnInputChange(val value: String) : LookupScreenAction
    data object Start : LookupScreenAction
    /** ثبت دارو از نتیجه (یا انتخاب داروی موجود با همان GTIN/IRC). */
    data object Apply : LookupScreenAction
    data object DismissResult : LookupScreenAction
    /** بعد از رفتن به صفحهٔ جزئیات، تا رویداد تکرار نشود. */
    data object ConsumeOpenDrug : LookupScreenAction
}

class LookupViewModel(
    private val lookupDrugCode: LookupDrugCodeUseCase,
    private val createDrugWithStock: CreateDrugWithStockUseCase,
    private val drugRepository: DrugRepository,
) : ViewModel() {

    private val _uiState = MutableStateFlow(LookupScreenState())
    val uiState: StateFlow<LookupScreenState> = _uiState.asStateFlow()

    fun onAction(action: LookupScreenAction) {
        when (action) {
            is LookupScreenAction.OnInputChange -> _uiState.update {
                it.copy(
                    input = action.value,
                    // تغییر کد، نتیجهٔ قبلی را بی‌اعتبار می‌کند تا کاربر اشتباهی
                    // داروی کد قبلی را ثبت نکند.
                    result = null,
                    error = null,
                    notice = null,
                )
            }

            LookupScreenAction.Start -> start()
            LookupScreenAction.Apply -> apply()
            LookupScreenAction.DismissResult -> _uiState.update {
                it.copy(result = null, error = null, notice = null)
            }

            LookupScreenAction.ConsumeOpenDrug -> _uiState.update { it.copy(openDrugId = null) }
        }
    }

    private fun start() {
        val state = _uiState.value
        val code = state.code
        if (!state.canLookup) {
            _uiState.update {
                it.copy(error = "کد معتبر نیست؛ حداقل ۸ رقم لازم است.")
            }
            return
        }

        _uiState.update { it.copy(isLoading = true, error = null, notice = null, result = null) }
        viewModelScope.launch {
            try {
                val result = lookupDrugCode(code)
                _uiState.update { it.copy(isLoading = false, result = result) }
            } catch (e: LookupException) {
                _uiState.update { it.copy(isLoading = false, error = e.message) }
            } catch (e: Exception) {
                _uiState.update {
                    it.copy(
                        isLoading = false,
                        error = "استعلام انجام نشد. ثبت دستی دارو همیشه کار می‌کند.",
                    )
                }
            }
        }
    }

    /**
     * دارو را از نتیجه می‌سازد — ولی اگر همان GTIN/IRC از قبل در انبار باشد،
     * داروی تکراری نمی‌سازد و همان را باز می‌کند.
     */
    private fun apply() {
        val result = _uiState.value.result ?: return
        _uiState.update { it.copy(isLoading = true, error = null) }

        viewModelScope.launch {
            try {
                val existing: Drug? = result.gtin?.let { drugRepository.findByGtin(it) }
                    ?: result.irc?.let { drugRepository.findByIrc(it) }

                val drugId = existing?.id ?: createDrugWithStock(
                    name = result.name,
                    gtin = result.gtin ?: result.code,
                    irc = result.irc,
                    packSize = null,
                )

                _uiState.update {
                    it.copy(
                        isLoading = false,
                        openDrugId = drugId,
                        notice = if (existing != null) {
                            "این دارو از قبل در انبار بود؛ همان باز شد."
                        } else {
                            "دارو با اطلاعات تیتک ثبت شد."
                        },
                    )
                }
            } catch (e: PharmacyException) {
                _uiState.update { it.copy(isLoading = false, error = e.error.message) }
            } catch (e: Exception) {
                _uiState.update {
                    it.copy(isLoading = false, error = "ثبت دارو از نتیجهٔ استعلام انجام نشد.")
                }
            }
        }
    }
}
