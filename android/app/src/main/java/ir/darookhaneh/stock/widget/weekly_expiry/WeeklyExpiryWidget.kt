package ir.darookhaneh.stock.widget.weekly_expiry

import android.content.Context
import androidx.compose.runtime.Composable
import androidx.glance.GlanceId
import androidx.glance.GlanceModifier
import androidx.glance.GlanceTheme
import androidx.glance.LocalSize
import androidx.glance.action.ActionParameters
import androidx.glance.action.actionParametersOf
import androidx.glance.appwidget.GlanceAppWidget
import androidx.glance.appwidget.PreviewSizeMode
import androidx.glance.appwidget.SizeMode
import androidx.glance.appwidget.action.actionRunCallback
import androidx.glance.appwidget.components.Scaffold
import androidx.glance.appwidget.provideContent
import androidx.glance.layout.fillMaxSize
import androidx.glance.layout.fillMaxWidth
import ir.darookhaneh.stock.feature.settings.data.WidgetExceptionLogger
import ir.darookhaneh.stock.widget.model.ExpiryFoodModel
import ir.darookhaneh.stock.widget.model.fakeExpiryFoodList
import ir.darookhaneh.stock.widget.model.toFoodWidgetModelList
import ir.darookhaneh.stock.widget.usecase.GetFoodsUseCase
import ir.darookhaneh.stock.widget.utils.WidgetColorScheme
import ir.darookhaneh.stock.widget.utils.WidgetColors
import ir.darookhaneh.stock.widget.utils.WidgetLayoutConfig
import ir.darookhaneh.stock.widget.utils.toColorProvider
import ir.darookhaneh.stock.widget.weekly_expiry.component.WeeklyExpiryLargeTopBar
import ir.darookhaneh.stock.widget.weekly_expiry.component.WeeklyExpiryMediumTopBar
import ir.darookhaneh.stock.widget.weekly_expiry.component.WeeklyExpirySmallTopBar
import ir.darookhaneh.stock.widget.weekly_expiry.component.WeeklyLargeExpiryContent
import ir.darookhaneh.stock.widget.weekly_expiry.component.WeeklyMediumExpiryContent
import ir.darookhaneh.stock.widget.weekly_expiry.component.WeeklySmallExpiryContent
import ir.darookhaneh.stock.widget.worker.CallbackScheduler
import kotlinx.collections.immutable.ImmutableList
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import org.koin.core.component.KoinComponent
import org.koin.core.component.inject
import timber.log.Timber

val foodIdKey = ActionParameters.Key<String>(CallbackScheduler.FOOD_ID)

class WeeklyExpiryWidget : GlanceAppWidget(), KoinComponent {
    private val getThisWeekFoods: GetFoodsUseCase by inject()
    private val widgetExceptionLogger: WidgetExceptionLogger by inject()

    override val sizeMode: SizeMode
        get() = SizeMode.Exact

    override val previewSizeMode: PreviewSizeMode
        get() = WidgetLayoutConfig.defaultSizeMode

    override suspend fun provideGlance(
        context: Context,
        id: GlanceId
    ) {
        val expiryFoodModels = getThisWeekFoods.getThisWeek().toFoodWidgetModelList()
        provideContent {
            val size = LocalSize.current
            Timber.tag("StockWidget").d("size=${size.width} x ${size.height}")

            GlanceTheme(WidgetColorScheme.colors) {
                when (WidgetLayoutConfig.getModeForSize(size)) {
                    WidgetLayoutConfig.WidgetMode.COMPACT -> WeekExpirySmallWidget(expiryFoodModels)
                    WidgetLayoutConfig.WidgetMode.MEDIUM -> WeekExpiryMediumWidget(
                        expiryFoodModels = expiryFoodModels,
                        onConsume = { id ->
                            val actionParameters = actionParametersOf(foodIdKey to id)
                            actionRunCallback<ConsumeFoodCallBack>(parameters = actionParameters)
                        }
                    )

                    WidgetLayoutConfig.WidgetMode.EXPANDED -> WeekExpiryLargeWidget(
                        expiryFoodModels = expiryFoodModels,
                        onConsume = { id ->
                            val actionParameters = actionParametersOf(foodIdKey to id)
                            actionRunCallback<ConsumeFoodCallBack>(parameters = actionParameters)
                        }
                    )
                }
            }
        }
    }

    override suspend fun providePreview(context: Context, widgetCategory: Int) {
        val expiryFoodModels = fakeExpiryFoodList
        provideContent {
            val size = LocalSize.current
            GlanceTheme(WidgetColorScheme.colors) {
                when (WidgetLayoutConfig.getModeForSize(size)) {
                    WidgetLayoutConfig.WidgetMode.COMPACT -> WeekExpirySmallWidget(expiryFoodModels)
                    WidgetLayoutConfig.WidgetMode.MEDIUM -> WeekExpiryMediumWidget(
                        expiryFoodModels = expiryFoodModels,
                        onConsume = {}
                    )

                    WidgetLayoutConfig.WidgetMode.EXPANDED -> WeekExpiryLargeWidget(
                        expiryFoodModels = expiryFoodModels,
                        onConsume = {}
                    )
                }
            }
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
fun WeekExpirySmallWidget(
    expiryFoodModels: ImmutableList<ExpiryFoodModel>,
) {
    Timber.tag("ExpiryWidget").d("Small")
    Scaffold(
        modifier = GlanceModifier.fillMaxSize(),
        titleBar = {
            WeeklyExpirySmallTopBar(
                modifier = GlanceModifier
            )
        },
        backgroundColor = WidgetColors.BACKGROUND.toColorProvider()
    ) {
        WeeklySmallExpiryContent(
            expiryFoodModels = expiryFoodModels,
            modifier = GlanceModifier.fillMaxWidth()
        )
    }
}

@Composable
fun WeekExpiryMediumWidget(
    expiryFoodModels: ImmutableList<ExpiryFoodModel>,
    onConsume: (id: String) -> Unit
) {
    Timber.tag("ExpiryWidget").d("Medium")
    Scaffold(
        modifier = GlanceModifier.fillMaxSize(),
        titleBar = {
            WeeklyExpiryMediumTopBar(
                modifier = GlanceModifier
            )
        },
        backgroundColor = WidgetColors.BACKGROUND.toColorProvider()
    ) {
        WeeklyMediumExpiryContent(
            expiryFoodModels = expiryFoodModels,
            modifier = GlanceModifier.fillMaxWidth(),
            onConsume = onConsume
        )
    }
}

@Composable
fun WeekExpiryLargeWidget(
    expiryFoodModels: ImmutableList<ExpiryFoodModel>,
    onConsume: (id: String) -> Unit
) {
    Timber.tag("ExpiryWidget").d("Large")
    Scaffold(
        modifier = GlanceModifier.fillMaxSize(),
        titleBar = {
            WeeklyExpiryLargeTopBar(
                modifier = GlanceModifier
            )
        },
        backgroundColor = WidgetColors.BACKGROUND.toColorProvider()
    ) {
        WeeklyLargeExpiryContent(
            expiryFoodModels = expiryFoodModels,
            modifier = GlanceModifier.fillMaxWidth(),
            onConsume = onConsume
        )
    }
}