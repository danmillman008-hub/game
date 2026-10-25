package ir.darookhaneh.stock.feature.pharmacy.presentation.add

import androidx.compose.runtime.Immutable
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import ir.darookhaneh.stock.core.domain.pharmacy.DrugRules
import ir.darookhaneh.stock.core.domain.pharmacy.PharmacyError
import ir.darookhaneh.stock.core.domain.pharmacy.PharmacyException
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.CreateDrugWithStockUseCase
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
    val batchNumber: String = "",
    val expiryDate: Long? = null,
    val quantity: String = "",
    val location: String = "",
    val isSaving: Boolean = false,
    val errorMessage: String? = null,
    val savedDrugId: Long? = null,
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
    data class OnBatchNumberChange(val value: String) : AddDrugAction
    data class OnExpiryDateChange(val value: Long?) : AddDrugAction
    data class OnQuantityChange(val value: String) : AddDrugAction
    data class OnLocationChange(val value: String) : AddDrugAction
    data object Save : AddDrugAction
    data object DismissError : AddDrugAction
}

/**
 * ثبت دستی دارو + (اختیاری) بچ و ورود اولیهٔ موجودی.
 * هیچ وابستگی شبکه‌ای ندارد؛ اگر کد اسکن‌شده ناشناخته بود، همین مسیر جایگزین است.
 */
class AddDrugViewModel(
    private val createDrugWithStock: CreateDrugWithStockUseCase,
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
            is AddDrugAction.OnBatchNumberChange -> _uiState.update { it.copy(batchNumber = action.value) }
            is AddDrugAction.OnExpiryDateChange -> _uiState.update { it.copy(expiryDate = action.value) }
            is AddDrugAction.OnQuantityChange -> _uiState.update {
                // فقط رقم؛ مقدار منفی حتی وارد هم نمی‌شود.
                it.copy(quantity = action.value.filter(Char::isDigit))
            }

            is AddDrugAction.OnLocationChange -> _uiState.update { it.copy(location = action.value) }
            AddDrugAction.DismissError -> _uiState.update { it.copy(errorMessage = null) }
            AddDrugAction.Save -> save()
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
