package ir.darookhaneh.stock.widget.total_food

import android.content.Context
import androidx.compose.runtime.Composable
import androidx.glance.GlanceId
import androidx.glance.GlanceModifier
import androidx.glance.GlanceTheme
import androidx.glance.action.actionStartActivity
import androidx.glance.action.clickable
import androidx.glance.appwidget.GlanceAppWidget
import androidx.glance.appwidget.components.Scaffold
import androidx.glance.appwidget.provideContent
import androidx.glance.background
import androidx.glance.layout.fillMaxSize
import androidx.glance.preview.ExperimentalGlancePreviewApi
import androidx.glance.preview.Preview
import ir.darookhaneh.stock.MainActivity
import ir.darookhaneh.stock.feature.settings.data.WidgetExceptionLogger
import ir.darookhaneh.stock.widget.model.FreshnessStatisticModel
import ir.darookhaneh.stock.widget.model.fakeFreshnessStats
import ir.darookhaneh.stock.widget.model.toFreshnessStats
import ir.darookhaneh.stock.widget.total_food.component.TotalFoodContent
import ir.darookhaneh.stock.widget.total_food.component.TotalFoodTopBar
import ir.darookhaneh.stock.widget.usecase.GetFoodsUseCase
import ir.darookhaneh.stock.widget.utils.ErrorStateWidget
import ir.darookhaneh.stock.widget.utils.WidgetColorScheme
import ir.darookhaneh.stock.widget.utils.WidgetColors
import ir.darookhaneh.stock.widget.utils.toColorProvider
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import org.koin.core.component.KoinComponent
import org.koin.core.component.inject

class TotalFoodWidget : GlanceAppWidget(), KoinComponent {
    private val getAllFoodsUseCase: GetFoodsUseCase by inject()
    private val widgetExceptionLogger: WidgetExceptionLogger by inject()
    override suspend fun provideGlance(
        context: Context,
        id: GlanceId
    ) {
        try {
            val freshnessStats = getAllFoodsUseCase().toFreshnessStats()
            provideContent {
                GlanceTheme(WidgetColorScheme.colors) {
                    TotalFoodWidget(freshnessStatisticModel = freshnessStats)
                }
            }
        } catch (e: Exception) {
            widgetExceptionLogger.log(e, "$id")
            provideContent {
                ErrorStateWidget()
            }
        }
    }

    override suspend fun providePreview(context: Context, widgetCategory: Int) {
        val fakeStats = fakeFreshnessStats
        provideContent {
            TotalFoodWidget(freshnessStatisticModel = fakeStats)
        }
    }

    override fun onCompositionError(
        context: Context,
        glanceId: GlanceId,
        appWidgetId: Int,
        throwable: Throwable
    ) {
        CoroutineScope(Dispatchers.IO).launch {
            widgetExceptionLogger.log(throwable, "$glanceId")
        }
        super.onCompositionError(
            context,
            glanceId,
            appWidgetId,
            throwable
        )
    }
}

@Composable
private fun TotalFoodWidget(
    freshnessStatisticModel: FreshnessStatisticModel,
) {
    Scaffold(
        modifier = GlanceModifier.clickable(
            onClick = actionStartActivity<MainActivity>()
        ),
        backgroundColor = WidgetColors.BACKGROUND.toColorProvider(),
        titleBar = { TotalFoodTopBar() }
    ) {
        TotalFoodContent(
            modifier = GlanceModifier.fillMaxSize(),
            freshnessStatisticModel = freshnessStatisticModel
        )
    }
}

@OptIn(ExperimentalGlancePreviewApi::class)
@Composable
@Preview(widthDp = 360, heightDp = 240)
fun PreviewTotalFoodWidget() {
    GlanceTheme(WidgetColorScheme.colors) {
        androidx.glance.layout.Box(
            modifier = GlanceModifier.fillMaxSize()
                .background(WidgetColorScheme.colors.secondary),
            contentAlignment = androidx.glance.layout.Alignment.Center
        ) {
            TotalFoodWidget(freshnessStatisticModel = fakeFreshnessStats)
        }
    }
}