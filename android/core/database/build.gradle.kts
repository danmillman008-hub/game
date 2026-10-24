plugins {
    id("stock.android.library")
    id("com.google.devtools.ksp")
    id("androidx.room")
}

android {
    namespace = "ir.darookhaneh.stock.core.database"
}

room {
    schemaDirectory("$projectDir/schemas")
}

dependencies {
    implementation(project(":core:model"))
    api(libs.room.runtime)
    api(libs.room.ktx)
    ksp(libs.room.compiler)
    api(libs.androidx.sqlite.ktx)
}
