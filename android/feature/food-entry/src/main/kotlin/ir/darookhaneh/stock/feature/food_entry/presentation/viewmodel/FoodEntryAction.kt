package ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel

import android.net.Uri
import ir.darookhaneh.stock.core.model.food.StorageLocation
import ir.darookhaneh.stock.core.presentation.model.CategoryUiModel
import ir.darookhaneh.stock.core.presentation.viewmodel.UiAction

/**
 * Actions that can be performed within the food entry form.
 */
sealed interface FoodEntryAction : UiAction {
    data class OnNameChange(val name: String) : FoodEntryAction
    data class OnStorageLocationChange(val location: StorageLocation) : FoodEntryAction
    data class OnExpiryDateChange(val expiryDate: Long) : FoodEntryAction
    data class OnPurchaseDateChange(val purchaseDate: Long) : FoodEntryAction
    data class OnNoteChange(val note: String) : FoodEntryAction
    data class OnImagePick(val uri: Uri) : FoodEntryAction

    data object OnEditNameClick : FoodEntryAction
    data object OnNameConfirm : FoodEntryAction
    
    // Category related actions
    data class OnCategoryQueryChange(val query: String) : FoodEntryAction
    data class OnCategorySelect(val category: CategoryUiModel.ByCategory) : FoodEntryAction
    data class OnCategorySelectById(val id: String) : FoodEntryAction
    data object OnCategoryConfirm : FoodEntryAction

    // Overlay control
    data class OnShowOverlay(val overlay: FoodEntryOverlay) : FoodEntryAction
    data object OnDismissOverlay : FoodEntryAction
    data object OnSaveClick : FoodEntryAction
    data object OnBackClick : FoodEntryAction
    data class OnNotificationGranted(val granted: Boolean) : FoodEntryAction
}
