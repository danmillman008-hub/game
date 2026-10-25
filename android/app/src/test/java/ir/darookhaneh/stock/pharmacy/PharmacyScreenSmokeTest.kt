package ir.darookhaneh.stock.pharmacy

import androidx.compose.material3.MaterialTheme
import androidx.compose.ui.test.junit4.createComposeRule
import ir.darookhaneh.stock.core.model.pharmacy.Batch
import ir.darookhaneh.stock.core.model.pharmacy.BatchAlert
import ir.darookhaneh.stock.core.model.pharmacy.DashboardSnapshot
import ir.darookhaneh.stock.core.model.pharmacy.Drug
import ir.darookhaneh.stock.core.model.pharmacy.DrugSummary
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEvent
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEventType
import ir.darookhaneh.stock.feature.pharmacy.presentation.add.AddDrugScreen
import ir.darookhaneh.stock.feature.pharmacy.presentation.add.AddDrugUiState
import ir.darookhaneh.stock.feature.pharmacy.presentation.dashboard.DashboardScreen
import ir.darookhaneh.stock.feature.pharmacy.presentation.detail.DrugDetailScreen
import ir.darookhaneh.stock.feature.pharmacy.presentation.detail.DrugDetailUiState
import ir.darookhaneh.stock.feature.pharmacy.presentation.home.MedicationHomeScreen
import ir.darookhaneh.stock.feature.pharmacy.presentation.home.MedicationHomeUiState
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config

/**
 * اسموک تست ترکیب (composition) همهٔ صفحه‌های محصول.
 *
 * دلیل وجود: کاربر بعد از ثبت اولین دارو کرش گرفت. تست‌های واحد لایهٔ داده این را
 * نمی‌گیرند، چون کرش در **رندر** صفحه اتفاق می‌افتد. اینجا هر صفحه با دادهٔ واقعی‌شکل
 * (لیست پر، هشدار، بچ، رخداد) رندر می‌شود؛ هر استثنای Compose تست را قرمز می‌کند.
 */
@RunWith(RobolectricTestRunner::class)
@Config(sdk = [34], application = android.app.Application::class)
class PharmacyScreenSmokeTest {

    @get:Rule
    val compose = createComposeRule()

    private val now = 1_772_000_000_000L
    private val day = 86_400_000L

    private val drug = Drug(
        id = 1,
        name = "استامینوفن ۵۰۰",
        genericName = "Paracetamol",
        strength = "500mg",
        dosageForm = "قرص",
        gtin = "6260000000001",
        irc = "1234567890123456",
        packSize = 20,
        createdAt = now,
        updatedAt = now,
    )

    private val batch = Batch(
        id = 10,
        drugId = 1,
        batchNumber = "A-12",
        expiryDate = now + 30 * day,
        quantity = 4,
        createdAt = now,
        updatedAt = now,
    )

    @Test
    fun dashboard_renders_with_alerts() {
        compose.setContent {
            MaterialTheme {
                DashboardScreen(
                    snapshot = DashboardSnapshot(
                        drugCount = 3,
                        unitCount = 120,
                        lowStockDrugs = listOf(
                            DrugSummary(id = 1, name = "استامینوفن", totalQuantity = 4, batchCount = 1)
                        ),
                        expiringSoon = listOf(
                            BatchAlert(
                                batchId = 10, drugId = 1, drugName = "استامینوفن",
                                batchNumber = "A-12", expiryDate = now + 30 * day,
                                quantity = 4, daysToExpiry = 30,
                            )
                        ),
                        expired = listOf(
                            BatchAlert(
                                batchId = 11, drugId = 2, drugName = "آموکسی‌سیلین",
                                batchNumber = "B-3", expiryDate = now - 5 * day,
                                quantity = 9, daysToExpiry = -5,
                            )
                        ),
                    ),
                    onAddDrug = {},
                    onScan = {},
                    onOpenDrug = {},
                    onOpenDrugs = {},
                )
            }
        }
        compose.waitForIdle()
    }

    @Test
    fun drug_list_renders_with_rows() {
        compose.setContent {
            MaterialTheme {
                MedicationHomeScreen(
                    uiState = MedicationHomeUiState(
                        query = "",
                        drugs = listOf(
                            DrugSummary(
                                id = 1, name = "استامینوفن ۵۰۰", totalQuantity = 4,
                                batchCount = 1, nearestExpiry = now + day, isLowStock = true,
                            ),
                            DrugSummary(id = 2, name = "شربت دیفن‌هیدرامین", totalQuantity = 40, batchCount = 2),
                        ),
                        isLoading = false,
                    ),
                    onAction = {},
                    onAddDrug = {},
                    onScan = {},
                    onOpenDrug = {},
                )
            }
        }
        compose.waitForIdle()
    }

    @Test
    fun drug_detail_renders_with_batch_and_events() {
        compose.setContent {
            MaterialTheme {
                DrugDetailScreen(
                    uiState = DrugDetailUiState(
                        drug = drug,
                        batches = listOf(batch),
                        selectedBatchId = batch.id,
                        events = listOf(
                            InventoryEvent(id = 1, batchId = 10, type = InventoryEventType.RECEIVE, quantityDelta = 20, createdAt = now),
                            InventoryEvent(id = 2, batchId = 10, type = InventoryEventType.DISPENSE, quantityDelta = -16, createdAt = now),
                            InventoryEvent(id = 3, batchId = 10, type = InventoryEventType.DAMAGE, quantityDelta = -1, createdAt = now),
                            InventoryEvent(id = 4, batchId = 10, type = InventoryEventType.RETURN, quantityDelta = 1, createdAt = now),
                            InventoryEvent(id = 5, batchId = 10, type = InventoryEventType.COUNT, quantityDelta = 0, createdAt = now),
                        ),
                    ),
                    onAction = {},
                )
            }
        }
        compose.waitForIdle()
    }

    @Test
    fun add_drug_renders_with_error_state() {
        compose.setContent {
            MaterialTheme {
                AddDrugScreen(
                    uiState = AddDrugUiState(
                        name = "ا",
                        quantity = "5",
                        errorMessage = "این بچ قبلاً ثبت شده است.",
                        isSaving = false,
                    ),
                    onAction = {},
                    onCancel = {},
                )
            }
        }
        compose.waitForIdle()
    }
}
