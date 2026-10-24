plugins {
    id("stock.android.feature")
}

android {
    namespace = "ir.darookhaneh.stock.feature.inventory"
}

dependencies {
    implementation(project(":core:datastore"))
    implementation(project(":feature:food-entry"))
}
