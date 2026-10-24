package ir.darookhaneh.stock.feature.food_entry.domain.model

data class FoodEntryPreferences(
    val hasAskNotificationPermission: Boolean = false,
    val addItemFirst: Boolean = false
)