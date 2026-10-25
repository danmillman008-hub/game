package ir.darookhaneh.stock.navigation

import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.ui.Modifier
import androidx.lifecycle.viewmodel.navigation3.rememberViewModelStoreNavEntryDecorator
import androidx.navigation3.runtime.NavBackStack
import androidx.navigation3.runtime.NavKey
import androidx.navigation3.runtime.entryProvider
import androidx.navigation3.runtime.rememberSaveableStateHolderNavEntryDecorator
import androidx.navigation3.ui.NavDisplay
import ir.darookhaneh.stock.core.presentation.ObserveEffect
import ir.darookhaneh.stock.core.presentation.navigation.Destination
import ir.darookhaneh.stock.core.presentation.navigation.NavigateEvent
import ir.darookhaneh.stock.core.presentation.navigation.Navigator
import ir.darookhaneh.stock.feature.pharmacy.presentation.add.AddDrugRoute
import ir.darookhaneh.stock.feature.pharmacy.presentation.dashboard.DashboardRoute
import ir.darookhaneh.stock.feature.pharmacy.presentation.detail.DrugDetailRoute
import ir.darookhaneh.stock.feature.pharmacy.presentation.history.HistoryRoute
import ir.darookhaneh.stock.feature.pharmacy.presentation.home.MedicationHomeRoute
import ir.darookhaneh.stock.feature.pharmacy.presentation.lookup.LookupRoute
import ir.darookhaneh.stock.feature.pharmacy.presentation.record.RecordRoute
import ir.darookhaneh.stock.feature.pharmacy.presentation.scan.ScannerRoute
import ir.darookhaneh.stock.feature.settings.navigation.SettingRoute
import ir.darookhaneh.stock.transition.AppTransitions
import ir.darookhaneh.stock.utils.Breadcrumbs
import ir.darookhaneh.stock.transition.toContentTransform
import org.koin.compose.koinInject

@Composable
fun AppGraph(
    backStack: NavBackStack<NavKey>,
    modifier: Modifier = Modifier,
) {
    val navigator = koinInject<Navigator>()

    // ردپای مسیر: با هر تغییر صفحه یک خط ثبت می‌شود (برای گزارش خطا).
    val currentEntry = backStack.lastOrNull()
    LaunchedEffect(currentEntry) {
        Breadcrumbs.mark("صفحه: " + (currentEntry?.let { it::class.simpleName } ?: "?"))
    }

    ObserveEffect(navigator.event) { event ->
        when (event) {
            NavigateEvent.NavigateBack -> if (backStack.isNotEmpty()) backStack.removeLastOrNull()
            is NavigateEvent.NavigateTo -> backStack.add(event.destination)
        }
    }

    NavDisplay(
        modifier = modifier,
        backStack = backStack,
        entryDecorators = listOf(
            rememberSaveableStateHolderNavEntryDecorator(),
            rememberViewModelStoreNavEntryDecorator(),
        ),
        transitionSpec = {
            AppTransitions.bottomBarExpressive.toContentTransform()
        },
        popTransitionSpec = {
            AppTransitions.bottomBarExpressive.toContentTransform()
        },
        predictivePopTransitionSpec = {
            AppTransitions.bottomBarExpressive.toContentTransform()
        },
        onBack = { if (backStack.isNotEmpty()) backStack.removeLastOrNull() },
        entryProvider = entryProvider {
            entry<Destination.Dashboard> {
                DashboardRoute(
                    onRecord = { backStack.add(Destination.Record) },
                    onAddDrug = { backStack.add(Destination.AddDrug()) },
                    onScan = { backStack.add(Destination.Scanner) },
                    onOpenDrug = { drugId -> backStack.add(Destination.DrugDetail(drugId)) },
                    onOpenDrugs = { backStack.add(Destination.Drugs) },
                    onLookup = { backStack.add(Destination.Lookup()) },
                )
            }

            entry<Destination.AddDrug>(
                metadata = NavDisplay.transitionSpec {
                    AppTransitions.enterFromBottom.toContentTransform()
                } + NavDisplay.popTransitionSpec {
                    AppTransitions.enterFromTop.toContentTransform()
                } + NavDisplay.predictivePopTransitionSpec {
                    AppTransitions.enterFromTop.toContentTransform()
                }
            ) { key ->
                AddDrugRoute(
                    initialGtin = key.gtin,
                    initialName = key.nameHint,
                    onSaved = { drugId ->
                        backStack.removeLastOrNull()
                        backStack.add(Destination.DrugDetail(drugId))
                    },
                    onCancel = { backStack.removeLastOrNull() },
                )
            }

            entry<Destination.Drugs> {
                MedicationHomeRoute(
                    onRecord = { backStack.add(Destination.Record) },
                    onAddDrug = { backStack.add(Destination.AddDrug()) },
                    onScan = { backStack.add(Destination.Scanner) },
                    onOpenDrug = { drugId -> backStack.add(Destination.DrugDetail(drugId)) },
                )
            }

            entry<Destination.Record> {
                RecordRoute(
                    onCreatedDrugNeeded = { name ->
                        backStack.add(Destination.AddDrug(nameHint = name))
                    },
                    onOpenScan = { backStack.add(Destination.Scanner) },
                )
            }

            entry<Destination.History> {
                HistoryRoute()
            }

            entry<Destination.Lookup> { key ->
                LookupRoute(
                    initialCode = key.code,
                    onOpenDrug = { drugId ->
                        backStack.removeLastOrNull()
                        backStack.add(Destination.DrugDetail(drugId))
                    },
                    onManualAdd = {
                        backStack.removeLastOrNull()
                        backStack.add(Destination.AddDrug())
                    },
                )
            }

            entry<Destination.DrugDetail> { key ->
                DrugDetailRoute(drugId = key.drugId)
            }

            entry<Destination.Scanner>(
                metadata = NavDisplay.transitionSpec {
                    AppTransitions.enterFromBottom.toContentTransform()
                } + NavDisplay.popTransitionSpec {
                    AppTransitions.enterFromTop.toContentTransform()
                } + NavDisplay.predictivePopTransitionSpec {
                    AppTransitions.enterFromTop.toContentTransform()
                }
            ) {
                ScannerRoute(
                    onUnknownCode = { code ->
                        backStack.removeLastOrNull()
                        backStack.add(Destination.AddDrug(gtin = code))
                    },
                    onDrugFound = { drugId ->
                        backStack.removeLastOrNull()
                        backStack.add(Destination.DrugDetail(drugId))
                    },
                    onNavigateBack = { backStack.removeLastOrNull() },
                )
            }

            entry<Destination.Setting> { setting ->
                SettingRoute(
                    destination = setting.destination,
                    onNavigateToSettingRoute = { destination -> backStack.add(destination) },
                    onNavigateBack = backStack::removeLastOrNull,
                )
            }
        }
    )
}
