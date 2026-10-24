package ir.darookhaneh.stock.core.network.model

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class GithubApiResponse(
    @SerialName("tag_name")
    val tagName: String? = null
)

