package ir.darookhaneh.stock.feature.scanner.domain.model

/**
 * Represent results of food date scanning.
 */
data class FoodDate(
    val productionDate: String? = null,
    val expiryDate: String? = null
)
