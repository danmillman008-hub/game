package ir.darookhaneh.stock.feature.settings.domain.model

data class Capability(
    val dynamicColorSupported: Boolean = false,
    val notificationGranted: Boolean = false,
    val biometricSupported: Boolean = false
)
