/**
 * Repository & Data Layer — Before & After AI Rules
 *
 * WITHOUT rules, AI assistants generate:
 * - Direct API calls from ViewModel
 * - No caching or offline support
 * - Mutable data exposed
 * - Single model class for all layers
 *
 * WITH android-ai-skills, AI assistants generate proper offline-first architecture.
 */

// ============================================================
// ❌ WITHOUT RULES — What AI typically generates
// ============================================================

// Single model used everywhere
data class Article(
    @SerializedName("article_id") val id: String,
    val title: String,
    val body: String,
    val author: String,
)

// ViewModel calls API directly
class ArticleListViewModel : ViewModel() {
    val articles = MutableLiveData<List<Article>>()
    val isLoading = MutableLiveData<Boolean>()

    fun loadArticles() {
        isLoading.value = true
        viewModelScope.launch {
            try {
                val response = RetrofitClient.api.getArticles()
                articles.value = response       // no caching, no offline
                isLoading.value = false
            } catch (e: Exception) {
                isLoading.value = false
            }
        }
    }
}


// ============================================================
// ✅ WITH RULES — What AI generates with android-ai-skills
// ============================================================

/**
 * Rules applied:
 * - Separate models per layer: Network, Entity, Domain (data-layer.md)
 * - Room with KSP for local persistence (data-layer.md)
 * - Kotlin Serialization instead of Gson (data-layer.md)
 * - Repository pattern as single data entry point (architecture.md)
 * - Offline-first: local DB is source of truth (data-layer.md)
 * - Flow for reactive data, suspend for one-shot (data-layer.md)
 * - Hilt injection for all classes (dependency-injection.md)
 * - @Upsert for insert-or-update (data-layer.md)
 * - WorkManager for background sync (modern-android.md)
 */

// --- Network Model (API response) ---
@Serializable
data class NetworkArticle(
    @SerialName("article_id") val id: String,
    val title: String,
    val body: String,
    val author: String,
    @SerialName("created_at") val createdAt: String,
)

// --- Database Entity (Room) ---
@Entity(tableName = "articles")
data class ArticleEntity(
    @PrimaryKey val id: String,
    val title: String,
    val body: String,
    val author: String,
    val createdAt: Long,
    val lastSynced: Long = System.currentTimeMillis(),
)

// --- Domain Model (UI consumes this) ---
data class Article(
    val id: String,
    val title: String,
    val body: String,
    val author: String,
    val createdAt: Instant,
)

// --- Mappers ---
fun NetworkArticle.toEntity() = ArticleEntity(
    id = id,
    title = title,
    body = body,
    author = author,
    createdAt = Instant.parse(createdAt).toEpochMilli(),
)

fun ArticleEntity.toDomain() = Article(
    id = id,
    title = title,
    body = body,
    author = author,
    createdAt = Instant.ofEpochMilli(createdAt),
)

// --- DAO (Room) ---
@Dao
interface ArticleDao {
    @Query("SELECT * FROM articles ORDER BY createdAt DESC")
    fun observeArticles(): Flow<List<ArticleEntity>>

    @Query("SELECT * FROM articles WHERE id = :id")
    suspend fun getById(id: String): ArticleEntity?

    @Upsert
    suspend fun upsertAll(articles: List<ArticleEntity>)

    @Query("DELETE FROM articles")
    suspend fun clearAll()
}

// --- Remote Data Source ---
class ArticleRemoteDataSource @Inject constructor(
    private val api: ArticleApi,
) {
    suspend fun fetchArticles(): List<NetworkArticle> = api.getArticles()
}

// --- Local Data Source ---
class ArticleLocalDataSource @Inject constructor(
    private val dao: ArticleDao,
) {
    fun observeArticles(): Flow<List<ArticleEntity>> = dao.observeArticles()

    suspend fun upsertAll(entities: List<ArticleEntity>) = dao.upsertAll(entities)
}

// --- Repository (single entry point) ---
class ArticleRepository @Inject constructor(
    private val remoteDataSource: ArticleRemoteDataSource,
    private val localDataSource: ArticleLocalDataSource,
) {
    /**
     * Observe articles from local database.
     * UI subscribes to this — always reads from local DB.
     */
    fun observeArticles(): Flow<List<Article>> =
        localDataSource.observeArticles()
            .map { entities -> entities.map(ArticleEntity::toDomain) }

    /**
     * Fetch from network and persist to local DB.
     * Called by pull-to-refresh or background sync.
     */
    suspend fun sync(): Result<Unit> = runCatching {
        val remote = remoteDataSource.fetchArticles()
        localDataSource.upsertAll(remote.map(NetworkArticle::toEntity))
    }
}

// --- ViewModel (consumes repository via UseCase) ---
@HiltViewModel
class ArticleListViewModel @Inject constructor(
    private val observeArticlesUseCase: ObserveArticlesUseCase,
    private val syncArticlesUseCase: SyncArticlesUseCase,
) : ViewModel() {

    private val _uiState = MutableStateFlow<ArticleListUiState>(ArticleListUiState.Loading)
    val uiState: StateFlow<ArticleListUiState> = _uiState.asStateFlow()

    init {
        observeArticles()
        sync()
    }

    private fun observeArticles() {
        viewModelScope.launch {
            observeArticlesUseCase()
                .collect { articles ->
                    _uiState.value = if (articles.isEmpty()) {
                        ArticleListUiState.Empty
                    } else {
                        ArticleListUiState.Success(articles = articles)
                    }
                }
        }
    }

    fun sync() {
        viewModelScope.launch {
            _uiState.update { current ->
                when (current) {
                    is ArticleListUiState.Success -> current.copy(isSyncing = true)
                    else -> current
                }
            }
            syncArticlesUseCase()
            _uiState.update { current ->
                when (current) {
                    is ArticleListUiState.Success -> current.copy(isSyncing = false)
                    else -> current
                }
            }
        }
    }
}

sealed interface ArticleListUiState {
    data object Loading : ArticleListUiState
    data object Empty : ArticleListUiState
    data class Success(
        val articles: List<Article>,
        val isSyncing: Boolean = false,
    ) : ArticleListUiState
    data class Error(val message: String) : ArticleListUiState
}
