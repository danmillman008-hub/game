package ir.darookhaneh.stock.feature.pharmacy.presentation.detail

import androidx.compose.runtime.Immutable
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import ir.darookhaneh.stock.core.domain.pharmacy.PharmacyError
import ir.darookhaneh.stock.core.domain.pharmacy.PharmacyException
import ir.darookhaneh.stock.core.domain.pharmacy.repository.BatchRepository
import ir.darookhaneh.stock.core.domain.pharmacy.repository.DrugRepository
import ir.darookhaneh.stock.core.domain.pharmacy.repository.InventoryRepository
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.AddBatchUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.RecordInventoryEventUseCase
import ir.darookhaneh.stock.core.model.pharmacy.Batch
import ir.darookhaneh.stock.core.model.pharmacy.Drug
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEvent
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEventType
import kotlinx.coroutines.Job
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

@Immutable
data class DrugDetailUiState(
    val drug: Drug? = null,
    val batches: List<Batch> = emptyList(),
    val selectedBatchId: Long? = null,
    val events: List<InventoryEvent> = emptyList(),
    val amount: String = "",
    val isSaving: Boolean = false,
    val message: String? = null,
    val showAddBatch: Boolean = false,
    val newBatchNumber: String = "",
    val newBatchExpiry: Long? = null,
    val newBatchLocation: String = "",
) {
    val selectedBatch: Batch? get() = batches.firstOrNull { it.id == selectedBatchId }
    val totalQuantity: Int get() = batches.sumOf { it.quantity }
    val amountValue: Int? get() = amount.trim().toIntOrNull()
    val canSubmitAmount: Boolean get() = !isSaving && amountValue != null && selectedBatch != null
    val canSaveBatch: Boolean
        get() = !isSaving && (newBatchNumber.isNotBlank() || newBatchExpiry != null)
}

sealed interface DrugDetailAction {
    data class SelectBatch(val batchId: Long) : DrugDetailAction
    data class OnAmountChange(val value: String) : DrugDetailAction
    data class Record(val type: InventoryEventType) : DrugDetailAction
    data object DismissMessage : DrugDetailAction
    data object OpenAddBatch : DrugDetailAction
    data object DismissAddBatch : DrugDetailAction
    data class OnNewBatchNumberChange(val value: String) : DrugDetailAction
    data class OnNewBatchExpiryChange(val value: Long?) : DrugDetailAction
    data class OnNewBatchLocationChange(val value: String) : DrugDetailAction
    data object SaveBatch : DrugDetailAction
}

/**
 * جزئیات دارو: بچ‌ها، رخدادهای موجودی و عملیات ورود/خروج/اصلاح/شمارش.
 * همهٔ تغییرات موجودی از یک مسیر اتمیک می‌گذرند (RecordInventoryEventUseCase).
 */
class DrugDetailViewModel(
    private val drugId: Long,
    drugRepository: DrugRepository,
    batchRepository: BatchRepository,
    private val inventoryRepository: InventoryRepository,
    private val addBatch: AddBatchUseCase,
    private val recordInventoryEvent: RecordInventoryEventUseCase,
) : ViewModel() {

    private val _uiState = MutableStateFlow(DrugDetailUiState())
    val uiState: StateFlow<DrugDetailUiState> = _uiState.asStateFlow()

    private var eventsJob: Job? = null

    init {
        viewModelScope.launch {
            drugRepository.observeById(drugId).collect { drug ->
                _uiState.update { it.copy(drug = drug) }
            }
        }
        viewModelScope.launch {
            batchRepository.observeByDrug(drugId).collect { batches ->
                _uiState.update { state ->
                    val selected = state.selectedBatchId
                        ?.takeIf { id -> batches.any { it.id == id } }
                        ?: batches.firstOrNull()?.id
                    state.copy(batches = batches, selectedBatchId = selected)
                }
                observeEvents(_uiState.value.selectedBatchId)
            }
        }
    }

    private fun observeEvents(batchId: Long?) {
        eventsJob?.cancel()
        if (batchId == null) {
            _uiState.update { it.copy(events = emptyList()) }
            return
        }
        eventsJob = viewModelScope.launch {
            inventoryRepository.observeEvents(batchId).collect { events ->
                _uiState.update { it.copy(events = events) }
            }
        }
    }

    fun onAction(action: DrugDetailAction) {
        when (action) {
            is DrugDetailAction.SelectBatch -> {
                _uiState.update { it.copy(selectedBatchId = action.batchId, amount = "") }
                observeEvents(action.batchId)
            }

            is DrugDetailAction.OnAmountChange -> _uiState.update {
                it.copy(amount = action.value.filter(Char::isDigit), message = null)
            }

            is DrugDetailAction.Record -> record(action.type)
            DrugDetailAction.DismissMessage -> _uiState.update { it.copy(message = null) }
            DrugDetailAction.OpenAddBatch -> _uiState.update { it.copy(showAddBatch = true) }
            DrugDetailAction.DismissAddBatch -> _uiState.update { it.copy(showAddBatch = false) }
            is DrugDetailAction.OnNewBatchNumberChange -> _uiState.update {
                it.copy(newBatchNumber = action.value)
            }

            is DrugDetailAction.OnNewBatchExpiryChange -> _uiState.update {
                it.copy(newBatchExpiry = action.value)
            }

            is DrugDetailAction.OnNewBatchLocationChange -> _uiState.update {
                it.copy(newBatchLocation = action.value)
            }

            DrugDetailAction.SaveBatch -> saveBatch()
        }
    }

    private fun record(type: InventoryEventType) {
        val state = _uiState.value
        val batchId = state.selectedBatchId ?: return
        val amount = state.amountValue ?: return
        _uiState.update { it.copy(isSaving = true, message = null) }

        viewModelScope.launch {
            try {
                recordInventoryEvent(batchId = batchId, type = type, amount = amount)
                _uiState.update { it.copy(isSaving = false, amount = "", message = "ثبت شد.") }
            } catch (e: PharmacyException) {
                _uiState.update { it.copy(isSaving = false, message = e.error.message) }
            } catch (e: Exception) {
                _uiState.update {
                    it.copy(isSaving = false, message = PharmacyError.StorageFailure.message)
                }
            }
        }
    }

    private fun saveBatch() {
        val state = _uiState.value
        _uiState.update { it.copy(isSaving = true, message = null) }

        viewModelScope.launch {
            try {
                addBatch(
                    drugId = drugId,
                    batchNumber = state.newBatchNumber,
                    expiryDate = state.newBatchExpiry,
                    location = state.newBatchLocation,
                )
                _uiState.update {
                    it.copy(
                        isSaving = false,
                        showAddBatch = false,
                        newBatchNumber = "",
                        newBatchExpiry = null,
                        newBatchLocation = "",
                        message = "بچ اضافه شد.",
                    )
                }
            } catch (e: PharmacyException) {
                _uiState.update { it.copy(isSaving = false, message = e.error.message) }
            } catch (e: Exception) {
                _uiState.update {
                    it.copy(isSaving = false, message = PharmacyError.StorageFailure.message)
                }
            }
        }
    }
}
