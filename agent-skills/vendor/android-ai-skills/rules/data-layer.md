# Data Layer

> Official source: https://developer.android.com/topic/architecture/data-layer

You are an expert in Android data layer architecture. Follow offline-first principles, use Room for persistence, DataStore for preferences, and maintain strict layer separation with dedicated models per layer.

## Repository Pattern

> Source: https://developer.android.com/topic/architecture/data-layer

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
- Expose `Flow<T>` for data that changes over time
- Expose `suspend` functions for one-shot operations
- Return immutable types only
- One repository per data type (`UserRepository`, `ArticleRepository`)

**DON'T:**
- Expose DataSource classes outside the data layer
- Return mutable collections (`MutableList`, `MutableMap`)
- Create a single repository for the entire app
- Put UI formatting logic in repositories

## Model Separation

> Source: https://developer.android.com/topic/architecture/data-layer

**DO:**
- Create separate model classes for each layer boundary:
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
- Use a single model class across all layers — API changes will break your UI
- Annotate domain models with `@Entity` or `@Serializable`
- Pass network or entity models to UI composables

## Room Database

> Source: https://developer.android.com/training/data-storage/room

**DO:**
- Use Room for all structured local data
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
- Use `@Upsert` for insert-or-update operations
- Use `@AutoMigration` for schema changes when possible
- Export schema for version control using Room Gradle Plugin

**DON'T:**
- Use KAPT for Room — migrate to KSP
- Return `LiveData` from DAOs in new code — use `Flow`
- Perform database operations on the main thread
- Use raw SQL queries when Room annotations suffice

## DataStore (Preferences)

> Source: https://developer.android.com/topic/libraries/architecture/datastore

**DO:**
- Use DataStore instead of SharedPreferences for all key-value storage:
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
- Use Proto DataStore for complex structured preferences
- Always read DataStore via `Flow` — it's async by design

**DON'T:**
- Use `SharedPreferences` in new code — always use DataStore
- Call DataStore synchronously — it's designed for async access
- Use DataStore for large datasets — use Room instead
- Create multiple DataStore instances for the same file

## Offline-First Architecture

> Source: https://developer.android.com/topic/architecture/data-layer/offline-first

**DO:**
- Local database (Room) is the single source of truth
- UI reads from local database via Flow — never directly from network
- Sync pattern: fetch from network -> save to local DB -> UI observes local DB:
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
- Handle conflict resolution (last-write-wins with timestamps)
- Show stale data with a sync indicator rather than empty screens

**DON'T:**
- Show a loading spinner with no data while waiting for network
- Assume the device has network connectivity
- Bypass the local database for "simple" reads

## Networking

> Source: https://developer.android.com/topic/architecture/data-layer

**DO:**
- Use Retrofit or Ktor for HTTP networking
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
- Use OkHttp interceptors for auth tokens, logging, and retry logic
- Handle network errors gracefully with `Result<T>` or sealed error types

**DON'T:**
- Use Gson or Moshi in new code — use Kotlin Serialization
- Call Retrofit APIs directly from ViewModel — go through Repository → DataSource
- Hardcode base URLs — inject via Hilt module

## Image Loading

> Source: https://coil-kt.github.io/coil/compose/

**DO:**
- Use Coil for image loading in Compose (built for Compose, coroutine-native):
```kotlin
AsyncImage(
    model = imageUrl,
    contentDescription = stringResource(R.string.profile_photo),
    modifier = Modifier.size(64.dp),
    contentScale = ContentScale.Crop,
)
```
- Configure caching and placeholder images
- Use `ContentScale.Crop` for consistent image sizing

**DON'T:**
- Use Glide or Picasso in Compose projects — use Coil
- Load images without `contentDescription` for accessibility
- Skip placeholder/error drawables in production code

## Paging

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
- Use `RemoteMediator` for offline-first paging (network + Room)
- Always provide `key` for paged `LazyColumn` items

**DON'T:**
- Load entire datasets into memory for large lists
- Implement manual pagination logic — use Paging 3
