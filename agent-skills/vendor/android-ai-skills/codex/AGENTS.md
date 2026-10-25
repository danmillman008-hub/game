# Android AI Skills — OpenAI Codex

> Drop this file as `AGENTS.md` in your Android project root to enforce best practices in OpenAI Codex.
> Source: https://github.com/RanaNadeemAslam/android-ai-skills

You are a senior Android developer. Follow these rules strictly when writing or modifying Android/Kotlin code.

---

## Table of Contents

1. [Architecture](#1-architecture)
2. [Jetpack Compose UI](#2-jetpack-compose-ui)
3. [Navigation](#3-navigation)
4. [Data Layer](#4-data-layer)
5. [Dependency Injection (Hilt)](#5-dependency-injection-hilt)
6. [Modern Android Platform](#6-modern-android-platform)
7. [Build System & Tooling](#7-build-system--tooling)
8. [Performance](#8-performance)
9. [Security](#9-security)
10. [Testing](#10-testing)

---

## 1. Architecture

> Source: https://developer.android.com/topic/architecture

### Layered Architecture

Follow the recommended layered architecture: UI Layer -> Domain Layer (optional) -> Data Layer.

```
UI Layer (Compose + ViewModel)
       |
Domain Layer (UseCases) — optional
       |
Data Layer (Repositories + DataSources)
```

**DO:**
- Separate the app into UI, Domain (optional), and Data layers.
- Each layer must only depend on the layer directly below it.
- UI layer never accesses data sources directly — always go through a repository.
- Domain layer is optional — only add it when multiple ViewModels share business logic.

**DON'T:**
- Never let the UI layer call data sources, APIs, or DAOs directly.
- Never let the Data layer reference UI or ViewModel classes.
- Never create circular dependencies between layers.
- Never add a Domain layer "just in case" — add it when you need it.

> Source: https://developer.android.com/topic/architecture#recommended-app-arch

### UI Layer & State Management

> Source: https://developer.android.com/topic/architecture/ui-layer

**DO:**
- Model UI state as a single immutable data class per screen:
```kotlin
data class ProfileUiState(
    val isLoading: Boolean = false,
    val profile: Profile? = null,
    val errorMessage: String? = null,
)
```
- Or use a sealed interface when states are mutually exclusive:
```kotlin
sealed interface ProfileUiState {
    data object Loading : ProfileUiState
    data class Success(val profile: Profile) : ProfileUiState
    data class Error(val message: String) : ProfileUiState
}
```
- Always expose UI state from ViewModel as `StateFlow`:
```kotlin
private val _uiState = MutableStateFlow(ProfileUiState())
val uiState: StateFlow<ProfileUiState> = _uiState.asStateFlow()
```
- Always collect state in Compose with `collectAsStateWithLifecycle()`:
```kotlin
val uiState by viewModel.uiState.collectAsStateWithLifecycle()
```
- Model user actions as events/intents passed to ViewModel via function calls.

**DON'T:**
- Never expose `MutableStateFlow` or `MutableLiveData` publicly from ViewModel.
- Never use multiple separate state holders for a single screen — combine into one state class.
- Never update ViewModel state directly from Composables — pass callbacks/lambdas instead.
- Never use `LiveData` in new code — use `StateFlow` with Compose.
- Never use `collectAsState()` — always use `collectAsStateWithLifecycle()` for lifecycle-awareness.

### ViewModel

> Source: https://developer.android.com/topic/libraries/architecture/viewmodel

**DO:**
- Annotate with `@HiltViewModel` and use `@Inject constructor` for dependencies.
- Use `viewModelScope` for all coroutine launches.
- Keep ViewModel focused on UI logic — delegate business logic to UseCases.
- Handle `SavedStateHandle` for process death survival when needed:
```kotlin
@HiltViewModel
class ProfileViewModel @Inject constructor(
    private val getProfileUseCase: GetProfileUseCase,
    private val savedStateHandle: SavedStateHandle,
) : ViewModel()
```

**DON'T:**
- Never reference `Activity`, `Fragment`, `Context`, or any Android UI class in ViewModel.
- Never use `GlobalScope` or create unscoped coroutines.
- Never put heavy business logic directly in ViewModel — extract to UseCases.
- Never create ViewModel instances manually — use Hilt injection.

### Domain Layer (UseCases)

> Source: https://developer.android.com/topic/architecture/domain-layer

**DO:**
- Name use cases as `VerbNounUseCase` (e.g., `GetProfileUseCase`, `SyncOrdersUseCase`).
- Make use cases callable with `operator fun invoke()`:
```kotlin
class GetProfileUseCase @Inject constructor(
    private val userRepository: UserRepository,
) {
    suspend operator fun invoke(userId: String): Result<Profile> {
        return userRepository.getProfile(userId)
    }
}
```
- Keep use cases stateless — no mutable properties.
- Make use cases main-safe (move blocking work with `withContext`).
- Use `Result<T>` or a sealed class for return types that can fail.
- Each use case must do ONE thing.

**DON'T:**
- Never store mutable state in use cases.
- Never call Android framework APIs from use cases — keep them pure Kotlin.
- Never create use cases that just forward to a repository with no logic — call the repository directly.
- Never name use cases as `ProfileManager` or `ProfileHelper` — use the `VerbNounUseCase` convention.

### Data Layer (Repository Pattern)

> Source: https://developer.android.com/topic/architecture/data-layer

**DO:**
- Use Repository as the single entry point to all data:
```kotlin
class UserRepository @Inject constructor(
    private val userRemoteDataSource: UserRemoteDataSource,
    private val userLocalDataSource: UserLocalDataSource,
) {
    fun getUsers(): Flow<List<User>> = userLocalDataSource.getUsers()

    suspend fun refreshUsers() {
        val users = userRemoteDataSource.fetchUsers()
        userLocalDataSource.saveUsers(users)
    }
}
```
- Expose data as `Flow<T>` for observable streams or `suspend` functions for one-shot operations.
- Always return immutable data from repositories — never expose mutable types.
- Name repositories by data type: `UserRepository`, `OrderRepository`.
- Create separate model classes per layer:
  - `NetworkUser` (API response)
  - `UserEntity` (Room database)
  - `User` (domain/UI model)
- Map between models at layer boundaries.

**DON'T:**
- Never expose `DataSource` classes to UI or Domain layers — always go through Repository.
- Never return mutable collections — use `List`, not `MutableList`.
- Never put UI logic in repositories.
- Never create a single god repository — split by data type.

### Unidirectional Data Flow (UDF)

> Source: https://developer.android.com/topic/architecture/ui-layer#udf

**DO:**
- State flows down from ViewModel to UI.
- Events flow up from UI to ViewModel.
- ViewModel is the sole producer of UI state.
- UI is a pure function of state.

```
ViewModel (state producer)
    | StateFlow<UiState>
Composable (state consumer)
    | User events (lambdas)
ViewModel (handles events, updates state)
```

**DON'T:**
- Never let Composables modify state directly.
- Never create bidirectional data flows.
- Never let multiple sources produce the same state.

---

## 2. Jetpack Compose UI

> Source: https://developer.android.com/develop/ui/compose

### Screen Pattern (Route + Screen)

> Source: https://developer.android.com/topic/architecture/ui-layer

**DO:**
- Always split every screen into a stateful Route and a stateless Screen composable:
```kotlin
// Route: stateful wrapper — connects ViewModel to UI
@Composable
fun ProfileRoute(
    onNavigateBack: () -> Unit,
    viewModel: ProfileViewModel = hiltViewModel(),
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    ProfileScreen(
        uiState = uiState,
        onNavigateBack = onNavigateBack,
        onRetry = viewModel::retry,
    )
}

// Screen: stateless, testable, previewable
@Composable
internal fun ProfileScreen(
    uiState: ProfileUiState,
    onNavigateBack: () -> Unit,
    onRetry: () -> Unit,
) {
    // Pure UI based on uiState
}
```
- Make Screen composables `internal` — expose only the Route.
- Use `@Preview` on the stateless Screen composable with sample data.

**DON'T:**
- Never pass ViewModel directly to Screen composables — pass state and lambdas.
- Never pass `NavController` to any composable — use callback lambdas.
- Never mix ViewModel logic and UI in the same composable.

### State Management

> Source: https://developer.android.com/develop/ui/compose/state

**DO:**
- Use `remember { mutableStateOf(...) }` for local composable state.
- Use `rememberSaveable` for state that must survive configuration changes:
```kotlin
var text by rememberSaveable { mutableStateOf("") }
```
- Hoist state to the lowest common ancestor that reads or writes it.
- Use `derivedStateOf` for values computed from other state:
```kotlin
val hasErrors by remember {
    derivedStateOf { username.isBlank() || email.isBlank() }
}
```
- Always collect ViewModel state with `collectAsStateWithLifecycle()`:
```kotlin
val uiState by viewModel.uiState.collectAsStateWithLifecycle()
```
- Use `remember(key)` to recompute cached values when dependencies change.

**DON'T:**
- Never use `collectAsState()` — always use `collectAsStateWithLifecycle()` for lifecycle awareness.
- Never store ViewModel-managed state in `remember` — let the ViewModel own it.
- Never read state inside click handlers without wrapping in lambdas (stale captures).
- Never use mutable objects (HashMap, ArrayList) as state — Compose won't detect changes.

### Recomposition & Performance

> Source: https://developer.android.com/develop/ui/compose/performance

**DO:**
- Keep composables fast, idempotent, and side-effect free.
- Use `@Stable` or `@Immutable` on data classes passed to composables:
```kotlin
@Stable
data class UserData(
    val name: String,
    val email: String,
)
```
- Use `key()` in `LazyColumn` / `LazyRow` for stable item identity:
```kotlin
LazyColumn {
    items(users, key = { it.id }) { user ->
        UserItem(user)
    }
}
```
- Use lambda-based modifiers for frequently changing values:
```kotlin
// Good — reads offset during layout, not composition
Modifier.offset { IntOffset(offsetX.roundToInt(), 0) }
```
- Defer state reads to the latest possible phase (drawing > layout > composition).
- Extract non-recomposing parameters into lambda wrappers.

**DON'T:**
- Never pass unstable types (List, Map, data classes with var) as parameters without `@Stable`.
- Never create new lambda instances in composition for frequently recomposing code — use `remember`.
- Never benchmark performance in debug builds — always use release + R8.
- Never use `Modifier.offset(x, y)` for animations — use the lambda version `Modifier.offset { }`.
- Never write backwards — reading state that was already written in the same composition.

### Side Effects

> Source: https://developer.android.com/develop/ui/compose/side-effects

**DO:**
- Use `LaunchedEffect(key)` for suspend-based side effects:
```kotlin
LaunchedEffect(userId) {
    viewModel.loadUser(userId)
}
```
- Use `DisposableEffect(key)` when cleanup is needed:
```kotlin
DisposableEffect(lifecycleOwner) {
    val observer = LifecycleEventObserver { _, event -> ... }
    lifecycleOwner.lifecycle.addObserver(observer)
    onDispose { lifecycleOwner.lifecycle.removeObserver(observer) }
}
```
- Use `rememberUpdatedState` for values referenced in long-running effects.
- Use `SideEffect` for publishing Compose state to non-Compose code.

**DON'T:**
- Never call suspend functions directly from composable body.
- Never perform I/O, logging, or shared state writes inside composable functions.
- Never use `LaunchedEffect(Unit)` unless you truly want it to run once per composition.

### Material 3 & Theming

> Source: https://developer.android.com/develop/ui/compose/designsystems/material3

**DO:**
- Always use Material 3 components from `androidx.compose.material3`.
- Define a centralized theme with `MaterialTheme`:
```kotlin
@Composable
fun AppTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    dynamicColor: Boolean = true,
    content: @Composable () -> Unit,
) {
    val colorScheme = when {
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> {
            if (darkTheme) dynamicDarkColorScheme(LocalContext.current)
            else dynamicLightColorScheme(LocalContext.current)
        }
        darkTheme -> darkColorScheme()
        else -> lightColorScheme()
    }
    MaterialTheme(colorScheme = colorScheme, content = content)
}
```
- Use `MaterialTheme.colorScheme`, `.typography`, `.shapes` for all styling.
- Always support dark mode and dynamic color (Material You).

**DON'T:**
- Never hardcode colors, font sizes, or shapes in composables.
- Never use Material 2 (`androidx.compose.material`) in new projects — use Material 3.
- Never mix Material 2 and Material 3 components.

### Design System

> Source: https://developer.android.com/develop/ui/compose/designsystems

**DO:**
- Create reusable design system composables (AppButton, AppCard, AppTextField).
- Centralize spacing, padding, and elevation values.
- Place design system in a `core:designsystem` module for multi-module projects.

### Accessibility

> Source: https://developer.android.com/develop/ui/compose/accessibility

**DO:**
- Always add `contentDescription` to all images and icons:
```kotlin
Icon(
    imageVector = Icons.Default.Close,
    contentDescription = stringResource(R.string.close),
)
```
- Use `Modifier.semantics` for custom accessibility info.
- Ensure minimum touch target size of 48dp:
```kotlin
Modifier.sizeIn(minWidth = 48.dp, minHeight = 48.dp)
```
- Support font scaling — use `sp` for text, never hardcode text size in `dp`.
- Group related elements with `Modifier.semantics(mergeDescendants = true)`.

**DON'T:**
- Never leave `contentDescription = null` on meaningful images (decorative-only is fine).
- Never use `dp` for text sizes — use `sp`.
- Never create touch targets smaller than 48dp.

### String Resources

> Source: https://developer.android.com/guide/topics/resources/string-resource

**DO:**
- Always use `stringResource(R.string.xyz)` in composables — never hardcoded strings.
- Use parameterized strings for dynamic content:
```kotlin
stringResource(R.string.welcome_message, userName)
```
- Use plurals for countable items.

**DON'T:**
- Never hardcode user-visible text: `Text("Hello")` — use `Text(stringResource(R.string.hello))`.
- Never use string concatenation for dynamic messages — use string formatting.

---

## 3. Navigation

> Source: https://developer.android.com/develop/ui/compose/navigation

### Setup & Structure

> Source: https://developer.android.com/guide/navigation/design

**DO:**
- Always use single-Activity architecture with one `NavHost`.
- Define routes as serializable data classes or objects:
```kotlin
@Serializable data object HomeRoute
@Serializable data object ProfileRoute
@Serializable data class ArticleDetailRoute(val articleId: String)
```
- Set up `NavHost` in the main composable:
```kotlin
@Composable
fun AppNavHost(
    navController: NavHostController = rememberNavController(),
) {
    NavHost(navController = navController, startDestination = HomeRoute) {
        composable<HomeRoute> {
            HomeRoute(
                onArticleClick = { id -> navController.navigate(ArticleDetailRoute(id)) },
            )
        }
        composable<ArticleDetailRoute> {
            ArticleDetailRoute(
                onNavigateBack = { navController.popBackStack() },
            )
        }
    }
}
```

**DON'T:**
- Never use string-based routes — use type-safe serializable route classes.
- Never create multiple Activities for navigation — use single Activity + NavHost.
- Never put NavHost inside individual screens.

### Decoupled Navigation

> Source: https://developer.android.com/develop/ui/compose/navigation#testing

**DO:**
- Always pass navigation actions as lambda callbacks to screen composables:
```kotlin
@Composable
fun HomeRoute(
    onArticleClick: (String) -> Unit,  // Navigation via callback
    onSettingsClick: () -> Unit,
    viewModel: HomeViewModel = hiltViewModel(),
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    HomeScreen(
        uiState = uiState,
        onArticleClick = onArticleClick,
        onSettingsClick = onSettingsClick,
    )
}
```
- Keep `NavController` only in the NavHost — never pass it down.

**DON'T:**
- Never pass `NavController` to composables:
```kotlin
// BAD — tightly coupled
fun HomeScreen(navController: NavController) {
    Button(onClick = { navController.navigate("profile") }) { ... }
}
```
- Never navigate from inside ViewModel — trigger navigation via UI events/callbacks.

### Arguments & Data Passing

> Source: https://developer.android.com/develop/ui/compose/navigation#retrieving-complex-data

**DO:**
- Only pass simple identifiers (IDs, strings) through navigation routes:
```kotlin
@Serializable
data class ArticleDetailRoute(val articleId: String)
```
- Retrieve the full object in the destination ViewModel using the ID:
```kotlin
@HiltViewModel
class ArticleDetailViewModel @Inject constructor(
    savedStateHandle: SavedStateHandle,
    private val getArticleUseCase: GetArticleUseCase,
) : ViewModel() {
    private val articleId: String = savedStateHandle.toRoute<ArticleDetailRoute>().articleId

    init {
        viewModelScope.launch {
            _uiState.value = getArticleUseCase(articleId)
        }
    }
}
```

**DON'T:**
- Never pass complex objects (data classes, lists) through navigation — pass IDs only.
- Never serialize large objects into route arguments.
- Never use `Bundle` or `Parcelable` for navigation arguments in Compose.

### Nested Navigation

**DO:**
- Use nested `NavGraph` for feature grouping:
```kotlin
NavHost(...) {
    navigation<AuthGraph>(startDestination = LoginRoute) {
        composable<LoginRoute> { ... }
        composable<RegisterRoute> { ... }
    }
    navigation<MainGraph>(startDestination = HomeRoute) {
        composable<HomeRoute> { ... }
        composable<ProfileRoute> { ... }
    }
}
```
- Define navigation graphs per feature module in multi-module projects.

**DON'T:**
- Never put all destinations in a flat NavHost — group related screens.
- Never create deep nesting (3+ levels) — keep navigation graphs shallow.

### Deep Links

> Source: https://developer.android.com/develop/ui/compose/navigation#deeplinks

**DO:**
- Define deep links in composable destinations when needed:
```kotlin
composable<ArticleDetailRoute>(
    deepLinks = listOf(
        navDeepLink<ArticleDetailRoute>(basePath = "https://myapp.com/article"),
    ),
) { ... }
```
- Handle deep links in `AndroidManifest.xml` with intent filters.
- Test deep links with `adb shell am start -d "url"`.

**DON'T:**
- Never hardcode deep link URLs in multiple places — centralize them.

---

## 4. Data Layer

> Source: https://developer.android.com/topic/architecture/data-layer

### Repository Pattern

**DO:**
- Repository is the single entry point to all data for a given type:
```kotlin
class ArticleRepository @Inject constructor(
    private val articleRemoteDataSource: ArticleRemoteDataSource,
    private val articleLocalDataSource: ArticleLocalDataSource,
) {
    fun getArticles(): Flow<List<Article>> =
        articleLocalDataSource.observeArticles()
            .map { entities -> entities.map { it.toArticle() } }

    suspend fun refreshArticles() {
        val networkArticles = articleRemoteDataSource.fetchArticles()
        articleLocalDataSource.upsertArticles(networkArticles.map { it.toEntity() })
    }
}
```
- Expose `Flow<T>` for data that changes over time.
- Expose `suspend` functions for one-shot operations.
- Always return immutable types only.
- One repository per data type (`UserRepository`, `ArticleRepository`).

**DON'T:**
- Never expose DataSource classes outside the data layer.
- Never return mutable collections (`MutableList`, `MutableMap`).
- Never create a single repository for the entire app.
- Never put UI formatting logic in repositories.

### Model Separation

> Source: https://developer.android.com/topic/architecture/data-layer

**DO:**
- Always create separate model classes for each layer boundary:
```kotlin
// Network layer — matches API JSON
@Serializable
data class NetworkArticle(
    @SerialName("article_id") val id: String,
    val title: String,
    @SerialName("body_text") val body: String,
    @SerialName("created_at") val createdAt: String,
)

// Database layer — matches Room schema
@Entity(tableName = "articles")
data class ArticleEntity(
    @PrimaryKey val id: String,
    val title: String,
    val body: String,
    val createdAt: Long,
    val lastRefreshed: Long = System.currentTimeMillis(),
)

// Domain/UI layer — what the app works with
data class Article(
    val id: String,
    val title: String,
    val body: String,
    val createdAt: Instant,
)
```
- Create extension functions for mapping between layers:
```kotlin
fun NetworkArticle.toEntity() = ArticleEntity(...)
fun ArticleEntity.toArticle() = Article(...)
```

**DON'T:**
- Never use a single model class across all layers — API changes will break your UI.
- Never annotate domain models with `@Entity` or `@Serializable`.
- Never pass network or entity models to UI composables.

### Room Database

> Source: https://developer.android.com/training/data-storage/room

**DO:**
- Always use Room for all structured local data.
- Use KSP for code generation (not KAPT):
```kotlin
// build.gradle.kts
plugins {
    id("com.google.devtools.ksp")
}
dependencies {
    implementation(libs.room.runtime)
    implementation(libs.room.ktx)
    ksp(libs.room.compiler)
}
```
- Enable Kotlin code generation:
```kotlin
ksp {
    arg("room.generateKotlin", "true")
}
```
- Return `Flow<List<T>>` from DAO queries for reactive updates:
```kotlin
@Dao
interface ArticleDao {
    @Query("SELECT * FROM articles ORDER BY createdAt DESC")
    fun observeArticles(): Flow<List<ArticleEntity>>

    @Query("SELECT * FROM articles WHERE id = :id")
    suspend fun getArticleById(id: String): ArticleEntity?

    @Upsert
    suspend fun upsertArticles(articles: List<ArticleEntity>)

    @Query("DELETE FROM articles")
    suspend fun clearAll()
}
```
- Use `@Upsert` for insert-or-update operations.
- Use `@AutoMigration` for schema changes when possible.
- Export schema for version control using Room Gradle Plugin.

**DON'T:**
- Never use KAPT for Room — migrate to KSP.
- Never return `LiveData` from DAOs in new code — use `Flow`.
- Never perform database operations on the main thread.
- Never use raw SQL queries when Room annotations suffice.

### DataStore (Preferences)

> Source: https://developer.android.com/topic/libraries/architecture/datastore

**DO:**
- Always use DataStore instead of SharedPreferences for all key-value storage:
```kotlin
val Context.settingsDataStore by preferencesDataStore(name = "settings")

class SettingsRepository @Inject constructor(
    private val dataStore: DataStore<Preferences>,
) {
    val isDarkMode: Flow<Boolean> = dataStore.data.map { prefs ->
        prefs[DARK_MODE_KEY] ?: false
    }

    suspend fun setDarkMode(enabled: Boolean) {
        dataStore.edit { prefs ->
            prefs[DARK_MODE_KEY] = enabled
        }
    }

    companion object {
        val DARK_MODE_KEY = booleanPreferencesKey("dark_mode")
    }
}
```
- Use Proto DataStore for complex structured preferences.
- Always read DataStore via `Flow` — it's async by design.

**DON'T:**
- Never use `SharedPreferences` in new code — always use DataStore.
- Never call DataStore synchronously — it's designed for async access.
- Never use DataStore for large datasets — use Room instead.
- Never create multiple DataStore instances for the same file.

### Offline-First Architecture

> Source: https://developer.android.com/topic/architecture/data-layer/offline-first

**DO:**
- Local database (Room) is the single source of truth.
- UI reads from local database via Flow — never directly from network.
- Follow the sync pattern: fetch from network -> save to local DB -> UI observes local DB:
```kotlin
class ArticleRepository @Inject constructor(
    private val remoteDataSource: ArticleRemoteDataSource,
    private val localDataSource: ArticleLocalDataSource,
) {
    // UI observes this — always reads from local DB
    fun observeArticles(): Flow<List<Article>> =
        localDataSource.observeArticles().map { it.map(ArticleEntity::toArticle) }

    // Triggered by pull-to-refresh or periodic sync
    suspend fun sync(): Result<Unit> = runCatching {
        val remote = remoteDataSource.fetchArticles()
        localDataSource.upsertArticles(remote.map(NetworkArticle::toEntity))
    }
}
```
- Use WorkManager for background sync:
```kotlin
class SyncWorker @AssistedInject constructor(
    @Assisted context: Context,
    @Assisted params: WorkerParameters,
    private val repository: ArticleRepository,
) : CoroutineWorker(context, params) {
    override suspend fun doWork(): Result {
        return when (repository.sync().isSuccess) {
            true -> Result.success()
            false -> Result.retry()
        }
    }
}
```
- Handle conflict resolution (last-write-wins with timestamps).
- Always show stale data with a sync indicator rather than empty screens.

**DON'T:**
- Never show a loading spinner with no data while waiting for network.
- Never assume the device has network connectivity.
- Never bypass the local database for "simple" reads.

### Networking

> Source: https://developer.android.com/topic/architecture/data-layer

**DO:**
- Use Retrofit or Ktor for HTTP networking.
- Use Kotlin Serialization (`@Serializable`) for JSON parsing:
```kotlin
@Serializable
data class NetworkArticle(
    val id: String,
    val title: String,
)
```
- Wrap network calls in DataSource classes:
```kotlin
class ArticleRemoteDataSource @Inject constructor(
    private val api: ArticleApi,
) {
    suspend fun fetchArticles(): List<NetworkArticle> = api.getArticles()
}
```
- Use OkHttp interceptors for auth tokens, logging, and retry logic.
- Handle network errors gracefully with `Result<T>` or sealed error types.

**DON'T:**
- Never use Gson or Moshi in new code — use Kotlin Serialization.
- Never call Retrofit APIs directly from ViewModel — go through Repository -> DataSource.
- Never hardcode base URLs — inject via Hilt module.

### Image Loading

> Source: https://coil-kt.github.io/coil/compose/

**DO:**
- Always use Coil for image loading in Compose (built for Compose, coroutine-native):
```kotlin
AsyncImage(
    model = imageUrl,
    contentDescription = stringResource(R.string.profile_photo),
    modifier = Modifier.size(64.dp),
    contentScale = ContentScale.Crop,
)
```
- Configure caching and placeholder images.
- Use `ContentScale.Crop` for consistent image sizing.

**DON'T:**
- Never use Glide or Picasso in Compose projects — use Coil.
- Never load images without `contentDescription` for accessibility.
- Never skip placeholder/error drawables in production code.

### Paging

> Source: https://developer.android.com/topic/libraries/architecture/paging/v3-overview

**DO:**
- Use Paging 3 for large or infinite lists:
```kotlin
// Repository
fun getArticlesPager(): Flow<PagingData<Article>> = Pager(
    config = PagingConfig(pageSize = 20),
    pagingSourceFactory = { ArticlePagingSource(api) },
).flow

// Compose
val articles = viewModel.articles.collectAsLazyPagingItems()
LazyColumn {
    items(articles.itemCount, key = articles.itemKey { it.id }) { index ->
        articles[index]?.let { ArticleItem(it) }
    }
}
```
- Use `RemoteMediator` for offline-first paging (network + Room).
- Always provide `key` for paged `LazyColumn` items.

**DON'T:**
- Never load entire datasets into memory for large lists.
- Never implement manual pagination logic — use Paging 3.

---

## 5. Dependency Injection (Hilt)

> Source: https://developer.android.com/training/dependency-injection/hilt-android

### Setup

**DO:**
- Annotate the Application class with `@HiltAndroidApp`:
```kotlin
@HiltAndroidApp
class MyApp : Application()
```
- Annotate Activities with `@AndroidEntryPoint`:
```kotlin
@AndroidEntryPoint
class MainActivity : ComponentActivity()
```
- Annotate ViewModels with `@HiltViewModel`:
```kotlin
@HiltViewModel
class ProfileViewModel @Inject constructor(
    private val getProfileUseCase: GetProfileUseCase,
) : ViewModel()
```

**DON'T:**
- Never forget `@HiltAndroidApp` on Application — Hilt won't work without it.
- Never create ViewModel instances with `ViewModelProvider` manually — use `hiltViewModel()` in Compose.
- Never use Koin or manual DI in new projects — use Hilt for standardized, compile-time safe DI.

### Constructor Injection (Preferred)

> Source: https://developer.android.com/training/dependency-injection/hilt-android#inject-interfaces

**DO:**
- Always use constructor injection as the default approach:
```kotlin
class UserRepository @Inject constructor(
    private val remoteDataSource: UserRemoteDataSource,
    private val localDataSource: UserLocalDataSource,
) {
    // ...
}
```
- All dependencies should be injectable — avoid `object` singletons that hold state.

**DON'T:**
- Never use field injection except in Android framework classes (Activity, Fragment, Service).
- Never create instances with `new` / direct constructor calls for injectable classes.

### Modules & Bindings

**DO:**
- Use `@Binds` for binding an interface to its implementation (preferred over `@Provides`):
```kotlin
@Module
@InstallIn(SingletonComponent::class)
abstract class RepositoryModule {
    @Binds
    abstract fun bindUserRepository(impl: UserRepositoryImpl): UserRepository
}
```
- Use `@Provides` for third-party classes and builder patterns:
```kotlin
@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {
    @Provides
    @Singleton
    fun provideOkHttpClient(): OkHttpClient =
        OkHttpClient.Builder()
            .addInterceptor(AuthInterceptor())
            .build()

    @Provides
    @Singleton
    fun provideRetrofit(client: OkHttpClient): Retrofit =
        Retrofit.Builder()
            .baseUrl(BuildConfig.BASE_URL)
            .client(client)
            .addConverterFactory(Json.asConverterFactory("application/json".toMediaType()))
            .build()
}
```
- Use `@Qualifier` for multiple bindings of the same type:
```kotlin
@Qualifier
@Retention(AnnotationRetention.BINARY)
annotation class IoDispatcher

@Module
@InstallIn(SingletonComponent::class)
object DispatcherModule {
    @Provides
    @IoDispatcher
    fun provideIoDispatcher(): CoroutineDispatcher = Dispatchers.IO
}
```
- Organize modules by concern: `NetworkModule`, `DatabaseModule`, `RepositoryModule`.

**DON'T:**
- Never put all bindings in a single module — split by concern.
- Never use `@Provides` when `@Binds` works — `@Binds` is more efficient (no function body).
- Never hardcode configuration values in modules — inject from BuildConfig or remote config.

### Scoping

> Source: https://developer.android.com/training/dependency-injection/hilt-android#component-scopes

**DO:**
- Use `@Singleton` for app-wide single instances (databases, API clients, repositories).
- Use `@ViewModelScoped` for dependencies shared within a ViewModel's lifecycle.
- Leave classes unscoped by default — Hilt creates a new instance on each injection.
- Only scope when the object is stateful or expensive to create.

**DON'T:**
- Never scope everything as `@Singleton` — this wastes memory and hides lifecycle bugs.
- Never use `@ActivityScoped` unless you truly need activity-lifecycle binding.
- Never create custom scopes unless you have a clear use case.

### Hilt with Compose

**DO:**
- Use `hiltViewModel()` to obtain ViewModels in Compose:
```kotlin
@Composable
fun ProfileRoute(
    viewModel: ProfileViewModel = hiltViewModel(),
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    ProfileScreen(uiState = uiState)
}
```

**DON'T:**
- Never pass ViewModel as a parameter to stateless Screen composables — pass state and callbacks.
- Never create ViewModel instances outside of Compose's `hiltViewModel()`.

### Testing with Hilt

> Source: https://developer.android.com/training/dependency-injection/hilt-testing

**DO:**
- Use `@HiltAndroidTest` for instrumented tests.
- Use `@UninstallModules` to replace production modules with test modules.
- Create fake implementations for testing:
```kotlin
class FakeUserRepository : UserRepository {
    private val users = mutableListOf<User>()
    override fun getUsers(): Flow<List<User>> = flowOf(users)
    override suspend fun refreshUsers() { /* no-op */ }
}
```
- For unit tests, simply pass fakes via constructor — no Hilt needed:
```kotlin
@Test
fun `loads profile successfully`() = runTest {
    val viewModel = ProfileViewModel(FakeGetProfileUseCase())
    // assert on viewModel.uiState
}
```

**DON'T:**
- Never use Mockito/MockK when fakes suffice — fakes are more maintainable.
- Never test Hilt wiring itself — test your logic, not the framework.

---

## 6. Modern Android Platform

> Source: https://developer.android.com/develop

### Edge-to-Edge Display

> Source: https://developer.android.com/develop/ui/views/layout/edge-to-edge

**DO:**
- Always enable edge-to-edge display (mandatory for apps targeting Android 15+):
```kotlin
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        enableEdgeToEdge()
        super.onCreate(savedInstanceState)
        setContent { ... }
    }
}
```
- Handle window insets in Compose:
```kotlin
Scaffold(
    modifier = Modifier.fillMaxSize(),
    contentWindowInsets = WindowInsets(0),
) { innerPadding ->
    Content(modifier = Modifier.padding(innerPadding))
}
```
- Use `Modifier.windowInsetsPadding()` for manual inset handling:
```kotlin
Modifier
    .statusBarsPadding()
    .navigationBarsPadding()
    .imePadding()
```

**DON'T:**
- Never use `fitsSystemWindows="true"` in Compose — handle insets with Compose APIs.
- Never assume a fixed status bar or navigation bar height.
- Never ignore insets — content will render behind system bars.

### Predictive Back Gesture

> Source: https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture

**DO:**
- Always opt in to predictive back in the manifest:
```xml
<application android:enableOnBackInvokedCallback="true">
```
- Use the Navigation component's built-in back handling.
- For custom back behavior, use `BackHandler` in Compose:
```kotlin
BackHandler(enabled = showBottomSheet) {
    showBottomSheet = false
}
```

**DON'T:**
- Never override `onBackPressed()` — it's deprecated.
- Never use `OnBackPressedDispatcher` directly — use Compose's `BackHandler`.
- Never block the back gesture without clear user value.

### Splash Screen API

> Source: https://developer.android.com/develop/ui/views/launch/splash-screen

**DO:**
- Always use the Splash Screen API from `androidx.core:core-splashscreen`:
```kotlin
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        val splashScreen = installSplashScreen()
        super.onCreate(savedInstanceState)

        // Keep splash while loading initial data
        splashScreen.setKeepOnScreenCondition {
            viewModel.isLoading.value
        }
    }
}
```
- Define splash theme in `res/values/themes.xml`:
```xml
<style name="Theme.App.Splash" parent="Theme.SplashScreen">
    <item name="windowSplashScreenBackground">@color/splash_bg</item>
    <item name="windowSplashScreenAnimatedIcon">@drawable/splash_icon</item>
    <item name="postSplashScreenTheme">@style/Theme.App</item>
</style>
```

**DON'T:**
- Never create a custom `SplashActivity` — use the Splash Screen API.
- Never show a splash screen for longer than necessary.
- Never use the splash screen for marketing — it's for perceived startup performance.

### Per-App Language Preferences

> Source: https://developer.android.com/guide/topics/resources/app-languages

**DO:**
- Declare supported locales in `res/xml/locales_config.xml`:
```xml
<?xml version="1.0" encoding="utf-8"?>
<locale-config xmlns:android="http://schemas.android.com/apk/res/android">
    <locale android:name="en" />
    <locale android:name="ur" />
    <locale android:name="ar" />
</locale-config>
```
- Reference in manifest:
```xml
<application android:localeConfig="@xml/locales_config">
```
- Use `AppCompatDelegate.setApplicationLocales()` for in-app language switching.

**DON'T:**
- Never implement custom locale switching logic — use the platform API.
- Never forget to declare supported locales — Android's per-app language picker needs it.

### Background Work (WorkManager)

> Source: https://developer.android.com/topic/libraries/architecture/workmanager

**DO:**
- Always use WorkManager for deferrable, guaranteed background work:
```kotlin
class SyncWorker @AssistedInject constructor(
    @Assisted context: Context,
    @Assisted params: WorkerParameters,
    private val repository: ArticleRepository,
) : CoroutineWorker(context, params) {

    override suspend fun doWork(): Result {
        return when (repository.sync().isSuccess) {
            true -> Result.success()
            false -> Result.retry()
        }
    }
}
```
- Use constraints for conditional execution:
```kotlin
val syncRequest = PeriodicWorkRequestBuilder<SyncWorker>(1, TimeUnit.HOURS)
    .setConstraints(
        Constraints.Builder()
            .setRequiredNetworkType(NetworkType.CONNECTED)
            .setRequiresBatteryNotLow(true)
            .build()
    )
    .build()

WorkManager.getInstance(context).enqueueUniquePeriodicWork(
    "sync",
    ExistingPeriodicWorkPolicy.KEEP,
    syncRequest,
)
```
- Use Hilt `@HiltWorker` with `@AssistedInject` for dependency injection.

**DON'T:**
- Never use `AlarmManager` or `JobScheduler` directly — use WorkManager.
- Never use `GlobalScope.launch` for background work — it won't survive process death.
- Never schedule work more frequently than needed — respect battery.

### Lifecycle Management

> Source: https://developer.android.com/guide/components/activities/activity-lifecycle

**DO:**
- Handle configuration changes (rotation, dark mode) via ViewModel — state survives.
- Handle process death via `SavedStateHandle` in ViewModel:
```kotlin
@HiltViewModel
class SearchViewModel @Inject constructor(
    private val savedStateHandle: SavedStateHandle,
) : ViewModel() {
    val searchQuery = savedStateHandle.getStateFlow("query", "")

    fun onQueryChanged(query: String) {
        savedStateHandle["query"] = query
    }
}
```
- Use `rememberSaveable` in Compose for UI state that must survive config changes.
- Always collect flows with lifecycle awareness:
```kotlin
val uiState by viewModel.uiState.collectAsStateWithLifecycle()
```

**DON'T:**
- Never store critical state only in Compose `remember` — it doesn't survive process death.
- Never use `onSaveInstanceState` directly — use `SavedStateHandle` in ViewModel.
- Never ignore process death testing — test with "Don't keep activities" developer option.

### Coroutines & Structured Concurrency

> Source: https://developer.android.com/kotlin/coroutines

**DO:**
- Always use structured concurrency — all coroutines must have a scope:
```kotlin
// ViewModel scope — cancelled when ViewModel is cleared
viewModelScope.launch {
    val result = withContext(Dispatchers.IO) {
        repository.fetchData()
    }
    _uiState.value = result
}
```
- Inject dispatchers for testability:
```kotlin
class MyRepository @Inject constructor(
    @IoDispatcher private val ioDispatcher: CoroutineDispatcher,
) {
    suspend fun fetchData() = withContext(ioDispatcher) { /* ... */ }
}
```
- Use `supervisorScope` when child failures shouldn't cancel siblings.
- Use `Flow` for reactive data streams, `suspend` for one-shot operations.

**DON'T:**
- Never use `GlobalScope` — ever.
- Never use `Dispatchers.IO` / `Dispatchers.Main` directly — inject them.
- Never use `runBlocking` in production code (test code is fine).
- Never catch `CancellationException` — let it propagate for proper cancellation.

---

## 7. Build System & Tooling

> Source: https://developer.android.com/build

### Gradle Kotlin DSL

**DO:**
- Always use `.gradle.kts` (Kotlin DSL) for all build files.
- Always use `libs.versions.toml` for centralized dependency management.

**DON'T:**
- Never use Groovy `.gradle` files in new projects.
- Never hardcode dependency versions in build files.

### Version Catalog

> Source: https://developer.android.com/build/migrate-to-catalogs

**DO:**
- Define all dependencies in `gradle/libs.versions.toml`:
```toml
[versions]
kotlin = "2.1.0"
compose-bom = "2025.04.00"
hilt = "2.51.1"
room = "2.7.1"
coroutines = "1.10.1"
ksp = "2.1.0-1.0.29"

[libraries]
compose-bom = { group = "androidx.compose", name = "compose-bom", version.ref = "compose-bom" }
compose-ui = { group = "androidx.compose.ui", name = "ui" }
compose-material3 = { group = "androidx.compose.material3", name = "material3" }
compose-ui-tooling-preview = { group = "androidx.compose.ui", name = "ui-tooling-preview" }
lifecycle-runtime-compose = { group = "androidx.lifecycle", name = "lifecycle-runtime-compose", version = "2.9.0" }
hilt-android = { group = "com.google.dagger", name = "hilt-android", version.ref = "hilt" }
hilt-compiler = { group = "com.google.dagger", name = "hilt-android-compiler", version.ref = "hilt" }
hilt-navigation-compose = { group = "androidx.hilt", name = "hilt-navigation-compose", version = "1.2.0" }
room-runtime = { group = "androidx.room", name = "room-runtime", version.ref = "room" }
room-ktx = { group = "androidx.room", name = "room-ktx", version.ref = "room" }
room-compiler = { group = "androidx.room", name = "room-compiler", version.ref = "room" }
datastore-preferences = { group = "androidx.datastore", name = "datastore-preferences", version = "1.1.4" }
kotlinx-coroutines-android = { group = "org.jetbrains.kotlinx", name = "kotlinx-coroutines-android", version.ref = "coroutines" }
kotlinx-serialization-json = { group = "org.jetbrains.kotlinx", name = "kotlinx-serialization-json", version = "1.8.0" }
coil-compose = { group = "io.coil-kt.coil3", name = "coil-compose", version = "3.1.0" }

[plugins]
android-application = { id = "com.android.application", version = "8.9.0" }
android-library = { id = "com.android.library", version = "8.9.0" }
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
kotlin-compose = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }
kotlin-serialization = { id = "org.jetbrains.kotlin.plugin.serialization", version.ref = "kotlin" }
hilt = { id = "com.google.dagger.hilt.android", version.ref = "hilt" }
ksp = { id = "com.google.devtools.ksp", version.ref = "ksp" }
room = { id = "androidx.room", version.ref = "room" }
```
- Reference with `libs.xyz` in build files:
```kotlin
dependencies {
    implementation(platform(libs.compose.bom))
    implementation(libs.compose.ui)
    implementation(libs.compose.material3)
    implementation(libs.hilt.android)
    ksp(libs.hilt.compiler)
}
```

**DON'T:**
- Never define versions inline in `build.gradle.kts`.
- Never use `ext` blocks for version management — use version catalogs.
- Never forget Compose BOM — it ensures compatible Compose library versions.

### KSP over KAPT

> Source: https://developer.android.com/build/migrate-to-ksp

**DO:**
- Always use KSP for all annotation processors:
```kotlin
plugins {
    id("com.google.devtools.ksp")
}
dependencies {
    ksp(libs.room.compiler)
    ksp(libs.hilt.compiler)
}
```
- KSP is up to 2x faster than KAPT.

**DON'T:**
- Never use KAPT — it's in maintenance mode and significantly slower.
- Never keep both KAPT and KSP — migrate fully to KSP.

### Modularization

> Source: https://developer.android.com/topic/modularization

**DO:**
- Structure as multi-module project from the start:
```
:app                        — Application entry point, wiring
:core:data                  — Repositories, data sources
:core:domain                — Use cases, domain models
:core:ui                    — Shared composables, theme
:core:designsystem          — Design tokens, base components
:core:database              — Room database, DAOs, entities
:core:network               — Retrofit/Ktor setup, API interfaces
:core:datastore             — DataStore preferences
:core:testing               — Shared test utilities, fakes
:feature:home               — Home screen feature
:feature:profile            — Profile screen feature
:feature:settings           — Settings screen feature
```
- Each feature module contains its own UI, ViewModel, and navigation.
- Core modules are shared utilities.
- Feature modules depend on core modules but never on other feature modules.

**DON'T:**
- Never put everything in `:app` — break apart once you have 2+ features.
- Never let feature modules depend on each other directly — communicate via navigation or shared core.
- Never create circular module dependencies.

### Convention Plugins

> Source: https://developer.android.com/build (Now in Android pattern)

**DO:**
- Create convention plugins in `build-logic/` for shared build configuration:
```
build-logic/
  convention/
    src/main/kotlin/
      AndroidApplicationConventionPlugin.kt
      AndroidLibraryConventionPlugin.kt
      AndroidComposeConventionPlugin.kt
      AndroidHiltConventionPlugin.kt
```
- Apply convention plugins in feature modules:
```kotlin
// feature/home/build.gradle.kts
plugins {
    id("myapp.android.feature")
    id("myapp.android.compose")
    id("myapp.android.hilt")
}
```
- This eliminates duplicate build configuration across modules.

**DON'T:**
- Never copy-paste the same build configuration across 10+ modules.
- Never use `allprojects {}` or `subprojects {}` blocks — use convention plugins.

### R8 & ProGuard

**DO:**
- Always enable R8 for release builds:
```kotlin
buildTypes {
    release {
        isMinifyEnabled = true
        isShrinkResources = true
        proguardFiles(
            getDefaultProguardFile("proguard-android-optimize.txt"),
            "proguard-rules.pro",
        )
    }
}
```
- Add keep rules for serialized classes and Hilt components.
- Test release builds regularly — R8 can break reflection-based code.

**DON'T:**
- Never ship debug builds to production.
- Never disable R8 to "avoid issues" — fix the ProGuard rules instead.
- Never benchmark or profile with debug builds — always use release + R8.

### Baseline Profiles

> Source: https://developer.android.com/topic/performance/baselineprofiles

**DO:**
- Generate baseline profiles for production apps:
```kotlin
// Add the Baseline Profile Gradle plugin
plugins {
    id("androidx.baselineprofile")
}
```
- Baseline profiles improve startup time by 15-30% by pre-compiling hot code paths.
- Include critical user journeys (app startup, main screen load).

**DON'T:**
- Never skip baseline profiles for production apps — free performance improvement.
- Never generate profiles from debug builds — use release builds.

### Code Quality

> Source: https://developer.android.com/studio/write/lint

**DO:**
- Always run Android Lint as part of CI:
```kotlin
android {
    lint {
        warningsAsErrors = true
        abortOnError = true
    }
}
```
- Use ktlint or detekt for Kotlin code style enforcement.
- Set up a CI pipeline (GitHub Actions) that runs lint + tests on every PR:
```yaml
# .github/workflows/ci.yml
name: CI
on: [pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'
      - run: ./gradlew lint testDebugUnitTest
```

**DON'T:**
- Never suppress lint warnings without justification.
- Never skip lint in CI — catch issues before merge.
- Never use `@Suppress` as a blanket fix — understand the warning first.

---

## 8. Performance

> Source: https://developer.android.com/develop/ui/compose/performance

### Compose Recomposition

> Source: https://developer.android.com/develop/ui/compose/performance/bestpractices

**DO:**
- Use immutable and stable types for composable parameters:
```kotlin
// Good — immutable, Compose can skip recomposition
data class UserData(
    val id: String,
    val name: String,
    val avatarUrl: String,
)
```
- Annotate custom classes with `@Stable` or `@Immutable` when needed:
```kotlin
@Stable
class FormState(
    val isValid: Boolean,
    val errors: List<String>,
)
```
- Always use `key()` in `LazyColumn`/`LazyRow` with stable IDs:
```kotlin
LazyColumn {
    items(items = articles, key = { it.id }) { article ->
        ArticleItem(article = article)
    }
}
```
- Use `derivedStateOf` to avoid unnecessary recompositions:
```kotlin
val showScrollToTop by remember {
    derivedStateOf { listState.firstVisibleItemIndex > 5 }
}
```
- Use lambda-based modifiers for frequently changing values:
```kotlin
// Good — offset read happens in layout phase, not composition
Modifier.offset { IntOffset(x = animatedOffset.roundToInt(), y = 0) }

// Bad — triggers recomposition on every frame
Modifier.offset(x = animatedOffset.dp, y = 0.dp)
```
- Defer state reads to the latest possible phase (draw > layout > composition).

**DON'T:**
- Never pass `List`, `Map`, or `Set` directly as composable parameters without wrapping in a stable type.
- Never use `var` in data classes passed to composables — use `val` only.
- Never create new object/lambda instances in composition without `remember`:
```kotlin
// Bad — new lambda on every recomposition
Button(onClick = { viewModel.doSomething(item.id) })

// Good for hot paths — stable lambda reference
val onClick = remember(item.id) { { viewModel.doSomething(item.id) } }
Button(onClick = onClick)
```
- Never ignore the Layout Inspector's recomposition counter during development.

### Lazy Layouts Performance

> Source: https://developer.android.com/develop/ui/compose/lists#performance

**DO:**
- Always provide `key` for lazy list items (enables item reordering and animations).
- Use `contentType` for lists with mixed item types:
```kotlin
LazyColumn {
    items(feed, key = { it.id }, contentType = { it.type }) { item ->
        when (item) {
            is Header -> HeaderItem(item)
            is Article -> ArticleItem(item)
        }
    }
}
```
- Avoid nesting scrollable layouts in the same direction.
- Use `Modifier.fillParentMaxWidth()` inside lazy items.

**DON'T:**
- Never use `LazyColumn` for small, fixed lists — use `Column` instead.
- Never nest a `LazyColumn` inside a `Column` with `verticalScroll` — it will crash.
- Never create heavy composables inside lazy items — extract and optimize.

### App Startup

> Source: https://developer.android.com/topic/performance/vitals/launch-time

**DO:**
- Always use the Splash Screen API (`androidx.core:core-splashscreen`):
```kotlin
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        val splashScreen = installSplashScreen()
        super.onCreate(savedInstanceState)
        splashScreen.setKeepOnScreenCondition { isLoading }
    }
}
```
- Defer non-critical initialization (analytics, crash reporting) with `App Startup` library:
```kotlin
class AnalyticsInitializer : Initializer<Analytics> {
    override fun create(context: Context): Analytics {
        return Analytics.init(context)
    }
    override fun dependencies(): List<Class<out Initializer<*>>> = emptyList()
}
```
- Use Baseline Profiles for startup optimization.
- Minimize work in `Application.onCreate()`.

**DON'T:**
- Never create custom splash activities — use the Splash Screen API.
- Never initialize everything eagerly in `Application.onCreate()`.
- Never block the main thread during startup.

### Memory Management

**DO:**
- Use `viewModelScope` — automatically cancelled when ViewModel is cleared.
- Use `repeatOnLifecycle` or `collectAsStateWithLifecycle()` to stop collection when UI is not visible.
- Cancel unnecessary work when user navigates away.
- Use weak references for long-lived callbacks pointing to UI objects (rare with Compose).

**DON'T:**
- Never use `GlobalScope` — it outlives components and leaks memory.
- Never hold references to `Activity` or `Context` in singletons.
- Never create unbounded caches without eviction policies.
- Never register listeners/callbacks without corresponding cleanup.

### Benchmarking

> Source: https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview

**DO:**
- Use Macrobenchmark for measuring app startup, scrolling, and animations:
```kotlin
@RunWith(AndroidJUnit4::class)
class StartupBenchmark {
    @get:Rule
    val benchmarkRule = MacrobenchmarkRule()

    @Test
    fun startup() = benchmarkRule.measureRepeated(
        packageName = "com.example.app",
        metrics = listOf(StartupTimingMetric()),
        iterations = 5,
        startupMode = StartupMode.COLD,
    ) {
        pressHome()
        startActivityAndWait()
    }
}
```
- Always benchmark with release builds + R8.
- Use Microbenchmark for isolated function performance.

**DON'T:**
- Never benchmark with debug builds — results are meaningless.
- Never optimize without measuring — profile first, then optimize.
- Never rely on subjective "feels fast" — use metrics.

---

## 9. Security

> Source: https://developer.android.com/topic/security/best-practices

### Sensitive Data Storage

> Source: https://developer.android.com/topic/security/best-practices#sensitive-data

**DO:**
- Use `EncryptedSharedPreferences` for sensitive key-value data:
```kotlin
val encryptedPrefs = EncryptedSharedPreferences.create(
    context,
    "secure_prefs",
    MasterKey.Builder(context).setKeyScheme(MasterKey.KeyScheme.AES256_GCM).build(),
    EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
    EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM,
)
```
- Use `EncryptedFile` for sensitive file storage.
- Always store auth tokens in encrypted storage, never in plain SharedPreferences or DataStore.
- Always clear sensitive data when user logs out.

**DON'T:**
- Never store passwords, tokens, or PII in plain SharedPreferences.
- Never store sensitive data in external storage (SD card).
- Never log sensitive data (tokens, passwords, PII) — even in debug builds.
- Never store sensitive data in the app database without encryption.

### Secrets Management

**DO:**
- Store API keys in `local.properties` (git-ignored) and inject via BuildConfig:
```kotlin
// build.gradle.kts
android {
    defaultConfig {
        val apiKey = project.findProperty("API_KEY") as? String ?: ""
        buildConfigField("String", "API_KEY", "\"$apiKey\"")
    }
}
```
- Use environment variables in CI/CD for secrets.
- Use server-side proxy for sensitive API keys when possible (don't ship third-party API keys in APK).

**DON'T:**
- Never hardcode API keys, secrets, or credentials in source code.
- Never commit `local.properties` to version control.
- Never ship production API keys in the APK — they can be extracted via reverse engineering.
- Never use `BuildConfig.DEBUG` as a security gate — it's easily bypassed.

### Network Security

> Source: https://developer.android.com/training/articles/security-config

**DO:**
- Always configure network security in `res/xml/network_security_config.xml`:
```xml
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <base-config cleartextTrafficPermitted="false">
        <trust-anchors>
            <certificates src="system" />
        </trust-anchors>
    </base-config>
</network-security-config>
```
- Reference in `AndroidManifest.xml`:
```xml
<application android:networkSecurityConfig="@xml/network_security_config">
```
- Always use HTTPS for all network communication.
- Implement certificate pinning for high-security apps:
```xml
<domain-config>
    <domain includeSubdomains="true">api.example.com</domain>
    <pin-set>
        <pin digest="SHA-256">base64EncodedPin=</pin>
    </pin-set>
</domain-config>
```

**DON'T:**
- Never allow cleartext (HTTP) traffic in production.
- Never trust user-installed CA certificates in production builds.
- Never disable SSL verification for "convenience".
- Never ship apps without `network_security_config.xml`.

### Input Validation

**DO:**
- Validate all user input at the boundary (before passing to domain/data layer):
```kotlin
fun validateEmail(email: String): ValidationResult {
    return when {
        email.isBlank() -> ValidationResult.Error("Email is required")
        !Patterns.EMAIL_ADDRESS.matcher(email).matches() -> ValidationResult.Error("Invalid email")
        else -> ValidationResult.Valid
    }
}
```
- Use parameterized Room queries (Room does this by default with `@Query`).
- Always sanitize data from deep links and intents before use.

**DON'T:**
- Never trust input from any external source (intents, deep links, content providers).
- Never build SQL queries with string concatenation — use Room's parameterized queries.
- Never pass unsanitized input to WebView's `loadUrl()` or `evaluateJavascript()`.

### Code Obfuscation

**DO:**
- Always enable R8 minification and obfuscation for release builds.
- Add appropriate ProGuard keep rules for reflection-based code.
- Test release builds thoroughly — R8 can remove code it deems unused.

**DON'T:**
- Never ship release builds without R8 — your code is readable with a decompiler.
- Never rely solely on obfuscation for security — it's a deterrent, not a solution.

### WebView Security

**DO:**
- Disable JavaScript unless absolutely needed:
```kotlin
webView.settings.javaScriptEnabled = false // Only enable if required
```
- Validate URLs before loading them.
- Use `WebViewAssetLoader` for loading local assets.
- Override `shouldOverrideUrlLoading` to control navigation.

**DON'T:**
- Never enable `setAllowFileAccess(true)` — disabled by default for good reason.
- Never add `@JavascriptInterface` methods that expose sensitive functionality.
- Never load untrusted content in WebView without validation.

### Permissions

> Source: https://developer.android.com/training/permissions/requesting

**DO:**
- Request only permissions you actually need.
- Always explain to the user why you need a permission before requesting it.
- Handle permission denial gracefully with degraded functionality.
- Use the Activity Result API for permission requests:
```kotlin
val permissionLauncher = rememberLauncherForActivityResult(
    contract = ActivityResultContracts.RequestPermission(),
) { isGranted ->
    if (isGranted) { /* proceed */ }
    else { /* show rationale or degrade gracefully */ }
}
```

**DON'T:**
- Never request permissions at app startup — request when the feature is used.
- Never request `WRITE_EXTERNAL_STORAGE` or `READ_EXTERNAL_STORAGE` on Android 13+ — use MediaStore or SAF.
- Never crash or show empty screen when permission is denied.

---

## 10. Testing

> Source: https://developer.android.com/training/testing

### Testing Strategy

> Source: https://developer.android.com/training/testing/fundamentals

**DO:**
- Follow the testing pyramid:
  - **Unit tests** (70%) — fast, run on JVM, test ViewModels, UseCases, Repositories.
  - **Integration tests** (20%) — test component interaction, navigation flows.
  - **UI/E2E tests** (10%) — test critical user journeys end-to-end.
- Write tests from day one — not as an afterthought.
- Test behavior ("when X happens, Y should result"), not implementation details.

**DON'T:**
- Never skip testing because "it's a small project".
- Never write tests that break when internal implementation changes but behavior stays the same.
- Never aim for 100% coverage at the expense of meaningful tests — focus on critical paths.

### Test Doubles (Fakes over Mocks)

> Source: https://developer.android.com/training/testing (Now in Android pattern)

**DO:**
- Always create fake implementations of interfaces for testing:
```kotlin
class FakeArticleRepository : ArticleRepository {
    private val articles = MutableStateFlow<List<Article>>(emptyList())

    override fun observeArticles(): Flow<List<Article>> = articles

    override suspend fun sync(): Result<Unit> {
        articles.value = listOf(
            Article(id = "1", title = "Test Article", body = "Body"),
        )
        return Result.success(Unit)
    }

    fun setArticles(list: List<Article>) {
        articles.value = list
    }
}
```
- Place fakes in a shared `testing` module so they can be reused across test targets:
```
:core:testing  (shared test utilities and fakes)
```
- Use constructor injection to swap real implementations with fakes in tests.

**DON'T:**
- Never default to Mockito or MockK — use fakes first, mocks only when fakes are impractical.
- Never mock data classes or value objects — construct real instances.
- Never mock final classes or framework classes — create fakes or use Robolectric.

### ViewModel Testing

> Source: https://developer.android.com/training/testing/local-tests

**DO:**
- Test ViewModels as plain Kotlin classes with fake dependencies:
```kotlin
class ArticleListViewModelTest {
    private val fakeRepository = FakeArticleRepository()
    private lateinit var viewModel: ArticleListViewModel

    @Before
    fun setup() {
        viewModel = ArticleListViewModel(
            observeArticlesUseCase = ObserveArticlesUseCase(fakeRepository),
        )
    }

    @Test
    fun `initial state is loading`() = runTest {
        val state = viewModel.uiState.first()
        assertThat(state).isEqualTo(ArticleListUiState.Loading)
    }

    @Test
    fun `shows articles after successful load`() = runTest {
        fakeRepository.setArticles(listOf(testArticle))

        viewModel.uiState.test {
            // Skip loading
            awaitItem()
            // Verify success state
            val state = awaitItem()
            assertThat(state).isInstanceOf(ArticleListUiState.Success::class.java)
        }
    }
}
```
- Use `kotlinx-coroutines-test` with `runTest` for coroutine testing.
- Use Turbine for testing `Flow` and `StateFlow`:
```kotlin
// build.gradle.kts
testImplementation("app.cash.turbine:turbine:<version>")
```
- Set the main dispatcher in tests:
```kotlin
@Before
fun setup() {
    Dispatchers.setMain(UnconfinedTestDispatcher())
}

@After
fun tearDown() {
    Dispatchers.resetMain()
}
```

**DON'T:**
- Never test ViewModel with real network calls — inject fake repositories.
- Never use `Thread.sleep()` in tests — use Turbine's `awaitItem()` or `advanceUntilIdle()`.
- Never test private ViewModel methods — test through public state.

### Compose UI Testing

> Source: https://developer.android.com/develop/ui/compose/testing

**DO:**
- Use `createComposeRule()` for testing composables:
```kotlin
class ProfileScreenTest {
    @get:Rule
    val composeTestRule = createComposeRule()

    @Test
    fun `displays user name when loaded`() {
        composeTestRule.setContent {
            ProfileScreen(
                uiState = ProfileUiState.Success(
                    profile = Profile(name = "Nadeem", email = "test@test.com"),
                ),
                onNavigateBack = {},
            )
        }

        composeTestRule
            .onNodeWithText("Nadeem")
            .assertIsDisplayed()
    }

    @Test
    fun `shows loading indicator`() {
        composeTestRule.setContent {
            ProfileScreen(
                uiState = ProfileUiState.Loading,
                onNavigateBack = {},
            )
        }

        composeTestRule
            .onNodeWithTag("loading_indicator")
            .assertIsDisplayed()
    }
}
```
- Always test the stateless Screen composable, not the Route (no ViewModel in UI tests).
- Use semantics for finding nodes: `onNodeWithText()`, `onNodeWithTag()`, `onNodeWithContentDescription()`.
- Add `testTag` modifier for elements without text:
```kotlin
CircularProgressIndicator(modifier = Modifier.testTag("loading_indicator"))
```

**DON'T:**
- Never test Compose internals (recomposition count, node tree structure).
- Never test with real ViewModels in UI tests — pass state directly.
- Never use `Thread.sleep()` for waiting — use `waitForIdle()` or `waitUntil { }`.

### Repository & DataSource Testing

**DO:**
- Test repositories with fake data sources:
```kotlin
class ArticleRepositoryTest {
    private val fakeRemoteDataSource = FakeArticleRemoteDataSource()
    private val fakeLocalDataSource = FakeArticleLocalDataSource()
    private val repository = ArticleRepository(fakeRemoteDataSource, fakeLocalDataSource)

    @Test
    fun `sync fetches from remote and saves to local`() = runTest {
        fakeRemoteDataSource.setArticles(listOf(networkArticle))

        repository.sync()

        val local = fakeLocalDataSource.getAll()
        assertThat(local).hasSize(1)
    }
}
```
- Test Room DAOs with an in-memory database:
```kotlin
@RunWith(AndroidJUnit4::class)
class ArticleDaoTest {
    private lateinit var db: AppDatabase
    private lateinit var dao: ArticleDao

    @Before
    fun setup() {
        db = Room.inMemoryDatabaseBuilder(
            ApplicationProvider.getApplicationContext(),
            AppDatabase::class.java,
        ).build()
        dao = db.articleDao()
    }

    @After
    fun tearDown() = db.close()
}
```

**DON'T:**
- Never test with real network calls — use fake data sources.
- Never skip DAO tests for complex queries — they catch SQL errors at test time.

### Assertions

**DO:**
- Use Truth (`com.google.common.truth:truth`) for readable assertions:
```kotlin
assertThat(result).isEqualTo(expected)
assertThat(list).containsExactly(item1, item2)
assertThat(result).isInstanceOf(Success::class.java)
```
- Or use kotlin.test assertions for simpler cases:
```kotlin
assertEquals(expected, actual)
assertTrue(condition)
```

**DON'T:**
- Never use JUnit 4 `assertEquals` with unclear parameter order — Truth is more readable.
- Never write assertions that pass for wrong reasons — be specific.
