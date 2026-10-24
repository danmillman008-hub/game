package ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel

import androidx.lifecycle.viewModelScope
import ir.darookhaneh.stock.core.data.util.product
import ir.darookhaneh.stock.core.model.food.FoodCategory
import ir.darookhaneh.stock.core.presentation.model.CategoryUiModel
import ir.darookhaneh.stock.core.presentation.model.toUiModel
import ir.darookhaneh.stock.core.presentation.viewmodel.BaseViewModel
import ir.darookhaneh.stock.feature.food_entry.domain.model.FoodEntryPreferences
import ir.darookhaneh.stock.feature.food_entry.domain.usecase.AddCategoryUseCase
import ir.darookhaneh.stock.feature.food_entry.domain.usecase.FoodEntryPreferencesUseCase
import ir.darookhaneh.stock.feature.food_entry.domain.usecase.ObserveCategoriesUseCase
import ir.darookhaneh.stock.feature.food_entry.domain.usecase.SaveFoodItemUseCase
import ir.darookhaneh.stock.feature.food_entry.presentation.model.EntryUiModel
import ir.darookhaneh.stock.feature.food_entry.presentation.model.toFoodItem
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.WhileSubscribed
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.launchIn
import kotlinx.coroutines.flow.onEach
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch
import kotlin.time.Duration.Companion.seconds

class FoodEntryViewModel(
    entryUiModel: EntryUiModel?,
    private val observeCategoriesUseCase: ObserveCategoriesUseCase,
    private val foodEntryPreferencesUseCase: FoodEntryPreferencesUseCase,
    private val saveFoodItemUseCase: SaveFoodItemUseCase,
    private val addCategoryUseCase: AddCategoryUseCase,
) : BaseViewModel<FoodEntryUiState, FoodEntryEvent, FoodEntryAction>() {
    private val _uiState = MutableStateFlow(FoodEntryUiState())
    override val uiState: StateFlow<FoodEntryUiState> = _uiState.asStateFlow()

    val foodEntryPreferences = foodEntryPreferencesUseCase.observe()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5.seconds), FoodEntryPreferences())
    private val currentPreferences get() = foodEntryPreferences.value

    init {
        viewModelScope.launch {
            val currentEntry = entryUiModel ?: EntryUiModel()

            _uiState.product {
                copy(
                    entry = currentEntry,
                    currentCategory = currentEntry.categoryUiModel,
                )
            }

        }
        observeCategories()
    }

    override fun onAction(action: FoodEntryAction) {
        when (action) {
            is FoodEntryAction.OnNameChange -> {
                _uiState.product {
                    copy(entry = entry.copy(name = action.name))
                }
            }

            is FoodEntryAction.OnStorageLocationChange -> {
                _uiState.product {
                    copy(entry = entry.copy(location = action.location))
                }
            }

            is FoodEntryAction.OnPurchaseDateChange -> {
                _uiState.product {
                    copy(
                        entry = entry.copy(purchaseDate = action.purchaseDate),
                        overlay = FoodEntryOverlay.NONE
                    )
                }
            }

            is FoodEntryAction.OnExpiryDateChange -> {
                _uiState.product {
                    copy(
                        entry = entry.copy(expiryDate = action.expiryDate),
                        overlay = FoodEntryOverlay.NONE
                    )
                }
            }

            is FoodEntryAction.OnNoteChange -> {
                _uiState.product {
                    copy(
                        entry = entry.copy(notes = action.note)
                    )
                }
            }

            is FoodEntryAction.OnImagePick -> {
                _uiState.product {
                    copy(
                        entry = entry.copy(imageUri = action.uri.toString())
                    )
                }
            }

            is FoodEntryAction.OnCategoryQueryChange -> _uiState.product { copy(categoryQuery = action.query) }
            is FoodEntryAction.OnCategorySelect -> {
                _uiState.product {
                    copy(
                        currentCategory = action.category,
                        entry = entry.copy(categoryUiModel = action.category)
                    )
                }
            }

            is FoodEntryAction.OnCategorySelectById -> {


            }

            FoodEntryAction.OnCategoryConfirm -> viewModelScope.launch {
                addCategoryUseCase(category = FoodCategory(name = currentState.categoryQuery))
                _uiState.product { copy(overlay = FoodEntryOverlay.NONE) }
            }

            is FoodEntryAction.OnShowOverlay -> _uiState.product { copy(overlay = action.overlay) }
            FoodEntryAction.OnDismissOverlay -> _uiState.product { copy(overlay = FoodEntryOverlay.NONE) }
            FoodEntryAction.OnSaveClick -> saveFood()
            FoodEntryAction.OnBackClick -> {

            }
            is FoodEntryAction.OnNotificationGranted -> viewModelScope.launch {
                if (!currentPreferences.hasAskNotificationPermission) {
                    foodEntryPreferencesUseCase.askNotificationPermission(true)
                }
            }

            FoodEntryAction.OnEditNameClick -> {
                _uiState.product { copy(overlay = FoodEntryOverlay.FOOD_NAME_ADD) }
            }

            FoodEntryAction.OnNameConfirm -> {
                _uiState.product { copy(overlay = FoodEntryOverlay.NONE) }
            }
        }
    }

    private fun saveFood() {
        if (currentPreferences.addItemFirst && !currentPreferences.hasAskNotificationPermission) {
            emitEvent(FoodEntryEvent.AskNotificationPermission)
            return
        }
        performSave()
    }

    private fun performSave() {
        viewModelScope.launch {
            val foodItem = currentState.entry.toFoodItem()
            saveFoodItemUseCase(foodItem)
            _uiState.product { copy(overlay = FoodEntryOverlay.NONE, entry = EntryUiModel()) }
            if (!currentPreferences.addItemFirst) {
                foodEntryPreferencesUseCase.addItemFirst(true)
            }
            emitEvent(FoodEntryEvent.OnNavigateBack)
        }
    }

    private fun observeCategories() {
        observeCategoriesUseCase()
            .onEach { categories ->
                val uiModel = categories.map { it.toUiModel() }
                    .filterIsInstance<CategoryUiModel.ByCategory>()
                _uiState.product {
                    copy(categories = uiModel)
                }
            }
            .launchIn(viewModelScope)
    }
}

