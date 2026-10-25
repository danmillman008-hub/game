package ir.darookhaneh.stock.feature.pharmacy.presentation.add

import androidx.compose.runtime.Immutable
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import ir.darookhaneh.stock.core.domain.pharmacy.DrugRules
import ir.darookhaneh.stock.core.domain.pharmacy.PharmacyError
import ir.darookhaneh.stock.core.domain.pharmacy.PharmacyException
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.CreateDrugWithStockUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.LookupDrugCodeUseCase
import ir.darookhaneh.stock.core.model.pharmacy.JalaliDate
import ir.darookhaneh.stock.core.model.pharmacy.LookupException
import ir.darookhaneh.stock.feature.pharmacy.presentation.lookup.LookupUiState
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

@Immutable
data class AddDrugUiState(
    val name: String = "",
    val genericName: String = "",
    val strength: String = "",
    val dosageForm: String = "",
    val gtin: String = "",
    val irc: String = "",
    /** تعداد واحد در بسته؛ برای تبدیل «کارتن × تعداد» و نمایش معادل بسته. */
    val packSize: String = "",
    val batchNumber: String = "",
    val expiryDate: Long? = null,
    val quantity: String = "",
    val location: String = "",
    val isSaving: Boolean = false,
    val errorMessage: String? = null,
    val savedDrugId: Long? = null,
    /** نتیجهٔ استعلام تیتک برای پیش‌پر کردن فرم؛ null یعنی استعلامی خواسته نشده. */
    val lookup: LookupUiState? = null,
    /** پیام موفقیت استعلام (مثلاً «فیلدها پر شد»). */
    val lookupNotice: String? = null,
) {
    val canSave: Boolean
        get() = !isSaving && DrugRules.validateName(name) == null

    /** اگر کاربر مقدار موجودی وارد کرده، باید بچ هم مشخص باشد. */
    val quantityValue: Int? get() = quantity.trim().toIntOrNull()
}

sealed interface AddDrugAction {
    data class OnNameChange(val value: String) : AddDrugAction
    data class OnGenericNameChange(val value: String) : AddDrugAction
    data class OnStrengthChange(val value: String) : AddDrugAction
    data class OnDosageFormChange(val value: String) : AddDrugAction
    data class OnGtinChange(val value: String) : AddDrugAction
    data class OnIrcChange(val value: String) : AddDrugAction
    data class OnPackSizeChange(val value: String) : AddDrugAction
    data class OnBatchNumberChange(val value: String) : AddDrugAction
    data class OnExpiryDateChange(val value: Long?) : AddDrugAction
    data class OnQuantityChange(val value: String) : AddDrugAction
    data class OnLocationChange(val value: String) : AddDrugAction
    data object Save : AddDrugAction
    data object DismissError : AddDrugAction

    /** استعلام کد واردشده (GTIN یا IRC) از تیتک — فقط با دکمهٔ کاربر. */
    data object StartLookup : AddDrugAction

    /** پر کردن فیلدهای نام/شرکت/GTIN/IRC از نتیجهٔ استعلام. */
    data object ApplyLookup : AddDrugAction
    data object DismissLookup : AddDrugAction
}

/**
 * ثبت دستی دارو + (اختیاری) بچ و ورود اولیهٔ موجودی.
 * هیچ وابستگی شبکه‌ای ندارد؛ اگر کد اسکن‌شده ناشناخته بود، همین مسیر جایگزین است.
 */
class AddDrugViewModel(
    private val createDrugWithStock: CreateDrugWithStockUseCase,
    private val lookupDrugCode: LookupDrugCodeUseCase,
) : ViewModel() {

    private val _uiState = MutableStateFlow(AddDrugUiState())
    val uiState: StateFlow<AddDrugUiState> = _uiState.asStateFlow()

    fun onAction(action: AddDrugAction) {
        when (action) {
            is AddDrugAction.OnNameChange -> _uiState.update { it.copy(name = action.value) }
            is AddDrugAction.OnGenericNameChange -> _uiState.update { it.copy(genericName = action.value) }
            is AddDrugAction.OnStrengthChange -> _uiState.update { it.copy(strength = action.value) }
            is AddDrugAction.OnDosageFormChange -> _uiState.update { it.copy(dosageForm = action.value) }
            is AddDrugAction.OnGtinChange -> _uiState.update { it.copy(gtin = action.value) }
            is AddDrugAction.OnIrcChange -> _uiState.update { it.copy(irc = action.value) }
            is AddDrugAction.OnPackSizeChange -> _uiState.update {
                it.copy(packSize = action.value.filter(Char::isDigit).take(5))
            }
            is AddDrugAction.OnBatchNumberChange -> _uiState.update { it.copy(batchNumber = action.value) }
            is AddDrugAction.OnExpiryDateChange -> _uiState.update { it.copy(expiryDate = action.value) }
            is AddDrugAction.OnQuantityChange -> _uiState.update {
                // فقط رقم؛ مقدار منفی حتی وارد هم نمی‌شود.
                it.copy(quantity = action.value.filter(Char::isDigit))
            }

            is AddDrugAction.OnLocationChange -> _uiState.update { it.copy(location = action.value) }
            AddDrugAction.DismissError -> _uiState.update { it.copy(errorMessage = null) }
            AddDrugAction.Save -> save()
            AddDrugAction.StartLookup -> startLookup()
            AddDrugAction.ApplyLookup -> applyLookup()
            AddDrugAction.DismissLookup -> _uiState.update { it.copy(lookup = null) }
        }
    }

    /** کدی که استعلام می‌شود: GTIN اگر پر باشد، وگرنه IRC. */
    private fun lookupCode(): String {
        val state = _uiState.value
        val raw = state.gtin.ifBlank { state.irc }
        return JalaliDate.latinDigits(raw).filter(Char::isDigit)
    }

    private fun startLookup() {
        val code = lookupCode()
        if (code.length < 8) {
            _uiState.update {
                it.copy(
                    lookup = LookupUiState(
                        code = code,
                        error = "برای استعلام، کد GTIN یا IRC (حداقل ۸ رقم) را وارد کنید.",
                    )
                )
            }
            return
        }

        _uiState.update { it.copy(lookup = LookupUiState(code = code, isLoading = true)) }
        viewModelScope.launch {
            try {
                val result = lookupDrugCode(code)
                _uiState.update { it.copy(lookup = LookupUiState(code = code, result = result)) }
            } catch (e: LookupException) {
                _uiState.update { it.copy(lookup = LookupUiState(code = code, error = e.message)) }
            } catch (e: Exception) {
                _uiState.update {
                    it.copy(
                        lookup = LookupUiState(
                            code = code,
                            error = "استعلام انجام نشد. بدون اینترنت هم ثبت دستی کار می‌کند.",
                        )
                    )
                }
            }
        }
    }

    /**
     * فیلدها را از نتیجهٔ استعلام پر می‌کند.
     * قاعده: فقط فیلدهای خالی را پر می‌کنیم تا نوشتهٔ دستی کاربر پاک نشود — جز GTIN/IRC
     * که منبع معتبرشان همان سامانه است.
     */
    private fun applyLookup() {
        val result = _uiState.value.lookup?.result ?: return
        _uiState.update {
            it.copy(
                name = it.name.ifBlank { result.name },
                genericName = it.genericName.ifBlank { result.englishName.orEmpty() },
                gtin = result.gtin ?: result.code,
                irc = result.irc.orEmpty(),
                lookup = null,
                lookupNotice = "اطلاعات دارو از سامانهٔ تیتک پر شد؛ بازبینی و ذخیره کنید.",
            )
        }
    }

    private fun save() {
        val state = _uiState.value
        if (!state.canSave) return

        val quantity = state.quantityValue ?: 0
        _uiState.update { it.copy(isSaving = true, errorMessage = null) }

        viewModelScope.launch {
            try {
                val drugId = createDrugWithStock(
                    name = state.name,
                    genericName = state.genericName,
                    strength = state.strength,
                    dosageForm = state.dosageForm,
                    gtin = state.gtin,
                    irc = state.irc,
                    packSize = state.packSize.toIntOrNull(),
                    batchNumber = state.batchNumber,
                    expiryDate = state.expiryDate,
                    initialQuantity = quantity,
                    location = state.location,
                )
                _uiState.update { it.copy(isSaving = false, savedDrugId = drugId) }
            } catch (e: PharmacyException) {
                _uiState.update { it.copy(isSaving = false, errorMessage = e.error.message) }
            } catch (e: Exception) {
                _uiState.update {
                    it.copy(isSaving = false, errorMessage = PharmacyError.StorageFailure.message)
                }
            }
        }
    }
}
