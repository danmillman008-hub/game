package ir.darookhaneh.stock.feature.pharmacy.presentation.scan

import androidx.compose.runtime.Immutable
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import ir.darookhaneh.stock.core.domain.pharmacy.repository.DrugRepository
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.ResolveScannedCodeUseCase
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

@Immutable
data class ScannerUiState(
    val isResolving: Boolean = false,
    val lastCode: String? = null,
    /** کد خوانده شد اما در دیتابیس محلی نبود → باید به فرم ثبت دستی برود. */
    val unknownCode: String? = null,
    /** کد پیدا شد → رفتن به جزئیات دارو. */
    val foundDrugId: Long? = null,
)

/**
 * تحلیل کد اسکن‌شده کاملاً محلی است (ResolveScannedCodeUseCase → Room).
 * برای کد ناشناخته هیچ درخواست شبکه‌ای زده نمی‌شود؛ فقط مسیر ثبت دستی باز می‌شود.
 */
class ScannerViewModel(
    private val resolveScannedCode: ResolveScannedCodeUseCase,
    drugRepository: DrugRepository,
) : ViewModel() {

    private val _uiState = MutableStateFlow(ScannerUiState())
    val uiState: StateFlow<ScannerUiState> = _uiState.asStateFlow()

    private val drugRepository = drugRepository

    fun onCodeScanned(rawValue: String) {
        val code = rawValue.trim()
        if (code.isEmpty() || _uiState.value.isResolving) return
        if (code == _uiState.value.lastCode && _uiState.value.isResolving) return

        _uiState.update { it.copy(isResolving = true, lastCode = code) }

        viewModelScope.launch {
            val drug = runCatching { resolveScannedCode(code) }.getOrNull()
            _uiState.update { state ->
                if (drug != null) {
                    state.copy(isResolving = false, foundDrugId = drug.id)
                } else {
                    state.copy(isResolving = false, unknownCode = code)
                }
            }
        }
    }

    /** بعد از باز شدن فرم ثبت دستی، وضعیت پاک می‌شود تا اسکن دوباره کار کند. */
    fun onUnknownHandled() {
        _uiState.update { it.copy(unknownCode = null) }
    }

    fun onFoundHandled() {
        _uiState.update { it.copy(foundDrugId = null, lastCode = null) }
    }

    fun onResume() {
        _uiState.update { it.copy(lastCode = null, unknownCode = null, foundDrugId = null) }
    }

    fun drugNameHint(drugId: Long, onResult: (String?) -> Unit) {
        viewModelScope.launch {
            onResult(runCatching { drugRepository.getById(drugId)?.name }.getOrNull())
        }
    }
}
