package ir.darookhaneh.stock.feature.pharmacy.presentation.record

import androidx.compose.runtime.Immutable
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import ir.darookhaneh.stock.core.domain.pharmacy.PharmacyError
import ir.darookhaneh.stock.core.domain.pharmacy.PharmacyException
import ir.darookhaneh.stock.core.domain.pharmacy.repository.BatchRepository
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.AddBatchUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.ObserveDrugSummariesUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.RecordInventoryEventUseCase
import ir.darookhaneh.stock.core.model.pharmacy.Batch
import ir.darookhaneh.stock.core.model.pharmacy.CountingMode
import ir.darookhaneh.stock.core.model.pharmacy.DrugSummary
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEventType
import ir.darookhaneh.stock.core.model.pharmacy.JalaliDate
import ir.darookhaneh.stock.core.model.pharmacy.QuantityInput
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.flatMapLatest
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

/**
 * «ثبت سریع» — یک صفحه برای کل چرخهٔ روزانهٔ داروخانه:
 * انتخاب دارو (جست‌وجو/اسکن) → نوع عملیات → مقدار (تکی/کارتن/باز) → بچ و انقضا → ثبت.
 *
 * چرا این صفحه ساخته شد: فرم قبلی ۱۱ فیلد داشت و برای ثبت یک خروج روزمره غیرقابل‌استفاده
 * بود؛ نسخهٔ HTML همین چرخه را در یک صفحه با سه روش شمارش انجام می‌داد.
 */
@Immutable
data class RecordUiState(
    val query: String = "",
    val results: List<DrugSummary> = emptyList(),
    val selectedDrug: DrugSummary? = null,
    val batches: List<Batch> = emptyList(),
    val selectedBatchId: Long? = null,
    /** حالت «بچ جدید»: شماره و تاریخ انقضا دستی وارد می‌شود. */
    val creatingBatch: Boolean = false,
    val operation: InventoryEventType = InventoryEventType.RECEIVE,
    val mode: CountingMode = CountingMode.SINGLE,
    val packs: String = "",
    val cartons: String = "",
    val unitsPerCarton: String = "",
    val loosePacks: String = "",
    val openUnits: String = "",
    val batchNumber: String = "",
    val expiryText: String = "",
    val note: String = "",
    val isSaving: Boolean = false,
    val message: String? = null,
    val isError: Boolean = false,
) {
    val packSize: Int? get() = selectedDrug?.packSize

    val quantityInput: QuantityInput
        get() = QuantityInput(
            mode = mode,
            packs = packs.toIntOrNull() ?: 0,
            cartons = cartons.toIntOrNull() ?: 0,
            unitsPerCarton = unitsPerCarton.toIntOrNull() ?: 0,
            loosePacks = loosePacks.toIntOrNull() ?: 0,
            openUnits = openUnits.toIntOrNull() ?: 0,
        )

    /** مقدار نهایی به **واحد** — همان عددی که در دیتابیس می‌نشیند. */
    val units: Int get() = quantityInput.toUnits(packSize)

    /** متن پیش‌نمایش: «= ۴۰ عدد (۲ بسته)». */
    val preview: String
        get() {
            if (units == 0) return "مقدار را وارد کنید"
            val per = packSize
            return if (per != null && per > 0) {
                "${JalaliDate.toPersianDigits(units)} عدد · ${JalaliDate.toPersianDigits(units / per)} بسته و ${JalaliDate.toPersianDigits(units % per)} واحد"
            } else {
                "${JalaliDate.toPersianDigits(units)} عدد"
            }
        }

    val expiryMillis: Long? get() = JalaliDate.parse(expiryText)?.toEpochMillis()

    val needsBatchIdentity: Boolean
        get() = selectedBatchId == null || creatingBatch

    val canSave: Boolean
        get() = !isSaving && selectedDrug != null && units > 0 &&
            (!needsBatchIdentity || batchNumber.isNotBlank() || expiryMillis != null)
}

sealed interface RecordAction {
    data class OnQueryChange(val value: String) : RecordAction
    data class SelectDrug(val drug: DrugSummary) : RecordAction
    data object ClearDrug : RecordAction
    data class SelectBatch(val batchId: Long?) : RecordAction
    data object StartNewBatch : RecordAction
    data class OnOperation(val type: InventoryEventType) : RecordAction
    data class OnMode(val mode: CountingMode) : RecordAction
    data class OnPacksChange(val value: String) : RecordAction
    data class OnCartonsChange(val value: String) : RecordAction
    data class OnUnitsPerCartonChange(val value: String) : RecordAction
    data class OnLoosePacksChange(val value: String) : RecordAction
    data class OnOpenUnitsChange(val value: String) : RecordAction
    data class OnBatchNumberChange(val value: String) : RecordAction
    data class OnExpiryTextChange(val value: String) : RecordAction
    data class OnExpiryPicked(val millis: Long?) : RecordAction
    data class OnNoteChange(val value: String) : RecordAction
    data object Save : RecordAction
    data object DismissMessage : RecordAction
}

@OptIn(ExperimentalCoroutinesApi::class)
class RecordViewModel(
    observeDrugSummaries: ObserveDrugSummariesUseCase,
    private val batchRepository: BatchRepository,
    private val addBatch: AddBatchUseCase,
    private val recordInventoryEvent: RecordInventoryEventUseCase,
) : ViewModel() {

    private val _uiState = MutableStateFlow(RecordUiState())
    val uiState: StateFlow<RecordUiState> = _uiState.asStateFlow()

    init {
        viewModelScope.launch {
            _uiState
                .flatMapLatest { state ->
                    observeDrugSummaries(state.query.takeIf { it.isNotBlank() })
                }
                .collect { drugs ->
                    _uiState.update { state ->
                        // وقتی دارویی انتخاب شده، فهرست نتایج پنهان می‌شود.
                        state.copy(results = drugs.take(30))
                    }
                }
        }
        viewModelScope.launch {
            _uiState
                .flatMapLatest { state ->
                    val drugId = state.selectedDrug?.id
                    if (drugId == null) {
                        kotlinx.coroutines.flow.flowOf(emptyList<Batch>())
                    } else {
                        batchRepository.observeByDrug(drugId)
                    }
                }
                .collect { batches ->
                    _uiState.update { state ->
                        val selected = state.selectedBatchId
                            ?.takeIf { id -> batches.any { it.id == id } }
                            ?: if (state.creatingBatch) null else batches.firstOrNull()?.id
                        state.copy(batches = batches, selectedBatchId = selected)
                    }
                }
        }
    }

    fun onAction(action: RecordAction) {
        when (action) {
            is RecordAction.OnQueryChange -> _uiState.update { it.copy(query = action.value) }
            is RecordAction.SelectDrug -> selectDrug(action.drug)
            RecordAction.ClearDrug -> _uiState.update {
                it.copy(selectedDrug = null, batches = emptyList(), selectedBatchId = null, query = "")
            }

            is RecordAction.SelectBatch -> _uiState.update {
                it.copy(selectedBatchId = action.batchId, creatingBatch = false)
            }

            RecordAction.StartNewBatch -> _uiState.update {
                it.copy(creatingBatch = true, selectedBatchId = null)
            }

            is RecordAction.OnOperation -> _uiState.update {
                it.copy(operation = action.type, message = null)
            }

            is RecordAction.OnMode -> _uiState.update { it.copy(mode = action.mode) }
            is RecordAction.OnPacksChange -> _uiState.update { it.copy(packs = digits(action.value)) }
            is RecordAction.OnCartonsChange -> _uiState.update { it.copy(cartons = digits(action.value)) }
            is RecordAction.OnUnitsPerCartonChange -> _uiState.update {
                it.copy(unitsPerCarton = digits(action.value))
            }

            is RecordAction.OnLoosePacksChange -> _uiState.update { it.copy(loosePacks = digits(action.value)) }
            is RecordAction.OnOpenUnitsChange -> _uiState.update { it.copy(openUnits = digits(action.value)) }
            is RecordAction.OnBatchNumberChange -> _uiState.update { it.copy(batchNumber = action.value) }
            is RecordAction.OnExpiryTextChange -> _uiState.update { it.copy(expiryText = action.value) }
            is RecordAction.OnExpiryPicked -> _uiState.update {
                val jalali = action.millis?.let { millis -> JalaliDate.fromEpochMillis(millis) }
                it.copy(expiryText = jalali?.format() ?: "")
            }

            is RecordAction.OnNoteChange -> _uiState.update { it.copy(note = action.value) }
            RecordAction.Save -> save()
            RecordAction.DismissMessage -> _uiState.update { it.copy(message = null) }
        }
    }

    private fun selectDrug(drug: DrugSummary) {
        _uiState.update {
            it.copy(
                selectedDrug = drug,
                query = "",
                selectedBatchId = null,
                creatingBatch = false,
                batchNumber = "",
                expiryText = "",
                message = null,
            )
        }
    }

    private fun save() {
        val state = _uiState.value
        val drug = state.selectedDrug ?: return
        val units = state.units
        if (units <= 0) {
            _uiState.update { it.copy(message = "مقدار باید بیشتر از صفر باشد.", isError = true) }
            return
        }
        if (state.needsBatchIdentity && state.batchNumber.isBlank() && state.expiryMillis == null) {
            _uiState.update {
                it.copy(message = "برای بچ جدید، شمارهٔ بچ یا تاریخ انقضا لازم است.", isError = true)
            }
            return
        }

        _uiState.update { it.copy(isSaving = true, message = null) }

        viewModelScope.launch {
            try {
                val batchId = if (state.needsBatchIdentity) {
                    addBatch(
                        drugId = drug.id,
                        batchNumber = state.batchNumber.ifBlank { null },
                        expiryDate = state.expiryMillis,
                    )
                } else {
                    state.selectedBatchId!!
                }

                recordInventoryEvent(
                    batchId = batchId,
                    type = state.operation,
                    amount = units,
                    note = state.note.ifBlank { null },
                )

                _uiState.update {
                    it.copy(
                        isSaving = false,
                        // دارو انتخاب‌شده می‌ماند تا ثبت بعدی سریع باشد (رفتار نسخهٔ HTML).
                        packs = "",
                        cartons = "",
                        loosePacks = "",
                        openUnits = "",
                        note = "",
                        batchNumber = "",
                        expiryText = "",
                        creatingBatch = false,
                        selectedBatchId = batchId,
                        message = "ثبت شد ✔",
                        isError = false,
                    )
                }
            } catch (e: PharmacyException) {
                _uiState.update { it.copy(isSaving = false, message = e.error.message, isError = true) }
            } catch (e: Exception) {
                _uiState.update {
                    it.copy(isSaving = false, message = PharmacyError.StorageFailure.message, isError = true)
                }
            }
        }
    }

    private fun digits(value: String): String =
        JalaliDate.latinDigits(value).filter(Char::isDigit).take(9)
}
