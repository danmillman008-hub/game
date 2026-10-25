package ir.darookhaneh.stock.navigation

import androidx.compose.runtime.Composable
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
import ir.darookhaneh.stock.feature.settings.navigation.SettingRoute
import ir.darookhaneh.stock.transition.AppTransitions
import ir.darookhaneh.stock.transition.toContentTransform
import ir.darookhaneh.stock.ui.PlaceholderScreen
import org.koin.compose.koinInject

@Composable
fun AppGraph(
    backStack: NavBackStack<NavKey>,
    modifier: Modifier = Modifier,
) {
    val navigator = koinInject<Navigator>()

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
                PlaceholderScreen(
                    title = "داشبورد",
                    description = "هشدار انقضا، موجودی کم و اقدامات سریع",
                )
            }

            entry<Destination.Drugs> {
                PlaceholderScreen(
                    title = "فهرست داروها",
                    description = "جست‌وجو و مشاهدهٔ موجودی",
                )
            }

            entry<Destination.DrugDetail> { key ->
                PlaceholderScreen(
                    title = "جزئیات دارو",
                    description = "شناسه: ${key.drugId}",
                )
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
                PlaceholderScreen(
                    title = "اسکن و ثبت",
                    description = "اسکن بارکد، سپس ثبت موجودی",
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
