package ir.darookhaneh.stock.feature.scanner.domain.usecase

import android.net.Uri
import ir.darookhaneh.stock.core.domain.repository.FoodRepository
import ir.darookhaneh.stock.core.domain.repository.LocalMediaStorage
import ir.darookhaneh.stock.core.model.error_handling.Resource
import ir.darookhaneh.stock.core.model.food.FoodItem
import ir.darookhaneh.stock.feature.scanner.domain.BarcodeScanner

class ScanBarcodeUseCase(
    private val repository: FoodRepository,
    private val barcodeScanner: BarcodeScanner,
    private val localMediaStorage: LocalMediaStorage
) {
    suspend fun fromBarcode(barcode: String): Resource<FoodItem> {
        return repository.scanFoodBarcode(barcode)
    }

    suspend fun fromUri(uri: Uri): Resource<FoodItem> {
        val barcode = barcodeScanner.scanFromImage(uri)
        val result = if (barcode != null) {
            repository.scanFoodBarcode(barcode)
        } else {
            Resource.Failure(Exception("No barcode found in image"))
        }
        localMediaStorage.deleteImageFromInternalStorage(uri.toString())
        return result
    }
}
