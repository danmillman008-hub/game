package ir.darookhaneh.stock.feature.scanner.domain.usecase

import android.net.Uri
import androidx.camera.core.ImageProxy
import ir.darookhaneh.stock.core.model.error_handling.Resource
import ir.darookhaneh.stock.feature.scanner.domain.FoodDateScanner
import ir.darookhaneh.stock.feature.scanner.domain.model.FoodDate

class ScanFoodDateUseCase(
    private val scanner: FoodDateScanner
) {
    suspend fun fromImage(imageProxy: ImageProxy): Resource<FoodDate?> {
        return scanner.scanImage(imageProxy)
    }

    suspend fun fromUri(uri: Uri): Resource<FoodDate?> {
        return scanner.scanFromUri(uri)
    }
}
