plugins {
    id("stock.android.application")
    id("org.jetbrains.kotlin.plugin.compose")
    alias(libs.plugins.jetbrains.kotlin.serialization)
    alias(libs.plugins.aboutlibraries)
}

android {
    namespace = "ir.darookhaneh.stock"
    defaultConfig {
        applicationId = "ir.darookhaneh.stock"
        targetSdk = 36
        versionCode = 9
        versionName = "2.1.1"
    }

    buildFeatures {
        buildConfig = true
    }

    // Robolectric برای تست ترکیب صفحه‌ها به منابع اندروید نیاز دارد.
    testOptions {
        unitTests {
            isIncludeAndroidResources = true
        }
    }

    // سه ABI جدا + یک universal؛ برای تست روی گوشی، نسخهٔ arm64-v8a کافی است و حجم کمتری دارد.
    splits {
        abi {
            isEnable = true
            reset()
            include("arm64-v8a", "armeabi-v7a", "x86_64")
            isUniversalApk = true
        }
    }


    /*
    applicationVariants.all {
        val variant = this
        variant.outputs.all {
            val output = this as com.android.build.gradle.internal.api.BaseVariantOutputImpl
            val fileName = "Stock_${variant.name}_v${variant.versionName}.apk"
            output.outputFileName = fileName
        }
    }
    */
}

dependencies {
    implementation(project(":core:presentation"))
    implementation(project(":core:data"))
    implementation(project(":core:database"))
    implementation(project(":core:network"))
    implementation(project(":core:notifications"))
    implementation(project(":core:datastore"))
    implementation(project(":core:domain"))

    implementation(project(":feature:settings"))
    implementation(project(":feature:pharmacy"))

    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.appcompat)
    implementation(libs.androidx.core.splashscreen)
    implementation(libs.androidx.lifecycle.runtime.ktx)
    implementation(libs.androidx.activity.compose)
    implementation(platform(libs.androidx.compose.bom))
    implementation(libs.androidx.ui)
    implementation(libs.androidx.ui.graphics)
    implementation(libs.androidx.ui.tooling.preview)
    implementation(libs.androidx.material3)

    // Koin & Navigation
    implementation(libs.koin.android)
    implementation(libs.koin.compose)
    implementation(libs.koin.androidx.workmanager)
    implementation(libs.androidx.navigation.compose)

    //Biometric Authenticator
    implementation(libs.androidx.biometric)

    //Glance

    //Serialization
    implementation(libs.kotlinx.serialization.core)

    // Testing
    testImplementation(libs.junit)
    testImplementation(libs.androidx.junit)
    testImplementation(libs.koin.test)
    testImplementation(libs.robolectric)
    testImplementation(libs.mockk)
    testImplementation(libs.kotlinx.coroutines.test)
    testImplementation(libs.turbine)
    // تست ترکیب صفحه‌ها روی Robolectric (بدون امولاتور)
    testImplementation(libs.androidx.ui.test.junit4)
    testImplementation(libs.androidx.ui.test.manifest)
    // Room واقعی (in-memory) برای تست مسیر ثبت دارو/موجودی
    testImplementation(libs.room.runtime)
    testImplementation(libs.room.ktx)

    androidTestImplementation(libs.androidx.junit)
    androidTestImplementation(libs.androidx.espresso.core)
    androidTestImplementation(platform(libs.androidx.compose.bom))
    androidTestImplementation(libs.androidx.ui.test.junit4)
    androidTestImplementation(libs.mockk.android)

    debugImplementation(libs.androidx.ui.tooling)
    debugImplementation(libs.androidx.ui.test.manifest)
}
