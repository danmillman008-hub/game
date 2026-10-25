# Testing

> Official source: https://developer.android.com/training/testing

You are an expert in Android testing. Follow the testing pyramid. Use test doubles (fakes) over mocking libraries. Test behavior, not implementation details.

## Testing Strategy

> Source: https://developer.android.com/training/testing/fundamentals

**DO:**
- Follow the testing pyramid:
  - **Unit tests** (70%) — fast, run on JVM, test ViewModels, UseCases, Repositories
  - **Integration tests** (20%) — test component interaction, navigation flows
  - **UI/E2E tests** (10%) — test critical user journeys end-to-end
- Write tests from day one — not as an afterthought
- Test behavior ("when X happens, Y should result"), not implementation details

**DON'T:**
- Skip testing because "it's a small project"
- Write tests that break when internal implementation changes but behavior stays the same
- Aim for 100% coverage at the expense of meaningful tests — focus on critical paths

## Test Doubles (Fakes over Mocks)

> Source: https://developer.android.com/training/testing (Now in Android pattern)

**DO:**
- Create fake implementations of interfaces for testing:
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
- Use constructor injection to swap real implementations with fakes in tests

**DON'T:**
- Default to Mockito or MockK — use fakes first, mocks only when fakes are impractical
- Mock data classes or value objects — construct real instances
- Mock final classes or framework classes — create fakes or use Robolectric

## ViewModel Testing

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
- Use `kotlinx-coroutines-test` with `runTest` for coroutine testing
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
- Test ViewModel with real network calls — inject fake repositories
- Use `Thread.sleep()` in tests — use Turbine's `awaitItem()` or `advanceUntilIdle()`
- Test private ViewModel methods — test through public state

## Compose UI Testing

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
- Test the stateless Screen composable, not the Route (no ViewModel in UI tests)
- Use semantics for finding nodes: `onNodeWithText()`, `onNodeWithTag()`, `onNodeWithContentDescription()`
- Add `testTag` modifier for elements without text:
```kotlin
CircularProgressIndicator(modifier = Modifier.testTag("loading_indicator"))
```

**DON'T:**
- Test Compose internals (recomposition count, node tree structure)
- Test with real ViewModels in UI tests — pass state directly
- Use `Thread.sleep()` for waiting — use `waitForIdle()` or `waitUntil { }`

## Repository & DataSource Testing

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
- Test with real network calls — use fake data sources
- Skip DAO tests for complex queries — they catch SQL errors at test time

## Assertions

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
- Use JUnit 4 `assertEquals` with unclear parameter order — Truth is more readable
- Write assertions that pass for wrong reasons — be specific
