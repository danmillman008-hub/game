# Kotlinx Serialization
-keepattributes *Annotation*

# Retrofit
-keep interface ir.darookhaneh.stock.core.network.api.** { *; }
-keep class ir.darookhaneh.stock.core.network.model.** { *; }

# Biometric (nếu cần)
-keep class androidx.biometric.** { *; }

# Dontwarn
-dontwarn javax.annotation.**
-dontwarn org.conscrypt.**