package ir.darookhaneh.stock.core.network.data_source

import ir.darookhaneh.stock.core.network.api.FoodApi
import ir.darookhaneh.stock.core.network.model.FoodApiResponse

interface FoodRemoteDataSource {
    //GET
    suspend fun fetchFoodApiResponse(barcodeString: String) : FoodApiResponse
}

class FoodRemoteDataSourceImpl(
    private val foodApi: FoodApi
) : FoodRemoteDataSource {
    override suspend fun fetchFoodApiResponse(barcodeString: String): FoodApiResponse {
        return foodApi.fetchFoodDetail(barcodeString)
    }
}
