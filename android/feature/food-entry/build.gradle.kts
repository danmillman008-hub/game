plugins {
    id("stock.android.feature")
    alias(libs.plugins.jetbrains.kotlin.serialization)
}

android {
    namespace = "ir.darookhaneh.stock.feature.food_entry"
}

dependencies {
    implementation(libs.kotlinx.serialization.json)
    implementation(project(":core:datastore"))
}
