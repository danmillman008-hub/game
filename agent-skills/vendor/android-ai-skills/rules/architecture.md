# Architecture

> Official source: https://developer.android.com/topic/architecture

You are an expert Android developer. Follow Google's official app architecture guidance strictly. Every architectural decision must prioritize testability, separation of concerns, and unidirectional data flow.

## Layered Architecture

Follow the recommended layered architecture: UI Layer -> Domain Layer (optional) -> Data Layer.

**DO:**
- Separate the app into UI, Domain (optional), and Data layers
- Each layer should only depend on the layer directly below it
- UI layer never accesses data sources directly — always through a repository
- Domain layer is optional — only add it when multiple ViewModels share business logic

**DON'T:**
- Let UI layer call data sources, APIs, or DAOs directly
- Let Data layer reference UI or ViewModel classes
- Create circular dependencies between layers
- Add a Domain layer "just in case" — add it when you need it

```
UI Layer (Compose + ViewModel)
       ↕
Domain Layer (UseCases) — optional
       ↕
Data Layer (Repositories + DataSources)
```

> Source: https://developer.android.com/topic/architecture#recommended-app-arch

## UI Layer & State Management

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
- Expose UI state from ViewModel as `StateFlow`:
```kotlin
private val _uiState = MutableStateFlow(ProfileUiState())
val uiState: StateFlow<ProfileUiState> = _uiState.asStateFlow()
```
- Collect state in Compose with `collectAsStateWithLifecycle()`:
```kotlin
val uiState by viewModel.uiState.collectAsStateWithLifecycle()
```
- Model user actions as events/intents passed to ViewModel via function calls

**DON'T:**
- Expose `MutableStateFlow` or `MutableLiveData` publicly from ViewModel
- Use multiple separate state holders for a single screen (combine into one state class)
- Update ViewModel state directly from Composables — pass callbacks/lambdas instead
- Use `LiveData` in new code — use `StateFlow` with Compose
- Use `collectAsState()` — use `collectAsStateWithLifecycle()` for lifecycle-awareness

## ViewModel

> Source: https://developer.android.com/topic/libraries/architecture/viewmodel

**DO:**
- Annotate with `@HiltViewModel` and use `@Inject constructor` for dependencies
- Use `viewModelScope` for all coroutine launches
- Keep ViewModel focused on UI logic — delegate business logic to UseCases
- Handle `SavedStateHandle` for process death survival when needed:
```kotlin
@HiltViewModel
class ProfileViewModel @Inject constructor(
    private val getProfileUseCase: GetProfileUseCase,
    private val savedStateHandle: SavedStateHandle,
) : ViewModel()
```

**DON'T:**
- Reference `Activity`, `Fragment`, `Context`, or any Android UI class in ViewModel
- Use `GlobalScope` or create unscoped coroutines
- Put heavy business logic directly in ViewModel — extract to UseCases
- Create ViewModel instances manually — use Hilt injection

## Domain Layer (UseCases)

> Source: https://developer.android.com/topic/architecture/domain-layer

**DO:**
- Name use cases as `VerbNounUseCase` (e.g., `GetProfileUseCase`, `SyncOrdersUseCase`)
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
- Keep use cases stateless — no mutable properties
- Make use cases main-safe (move blocking work with `withContext`)
- Use `Result<T>` or a sealed class for return types that can fail
- Each use case should do ONE thing

**DON'T:**
- Store mutable state in use cases
- Call Android framework APIs from use cases — keep them pure Kotlin
- Create use cases that just forward to a repository with no logic — call the repository directly
- Name use cases as `ProfileManager` or `ProfileHelper` — use the `VerbNounUseCase` convention

## Data Layer (Repository Pattern)

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
- Expose data as `Flow<T>` for observable streams or `suspend` functions for one-shot operations
- Return immutable data from repositories — never expose mutable types
- Name repositories by data type: `UserRepository`, `OrderRepository`
- Create separate model classes per layer:
  - `NetworkUser` (API response)
  - `UserEntity` (Room database)
  - `User` (domain/UI model)
- Map between models at layer boundaries

**DON'T:**
- Expose `DataSource` classes to UI or Domain layers — always go through Repository
- Return mutable collections — use `List`, not `MutableList`
- Put UI logic in repositories
- Create a single god repository — split by data type

## Unidirectional Data Flow (UDF)

> Source: https://developer.android.com/topic/architecture/ui-layer#udf

**DO:**
- State flows down from ViewModel to UI
- Events flow up from UI to ViewModel
- ViewModel is the sole producer of UI state
- UI is a pure function of state

```
ViewModel (state producer)
    ↓ StateFlow<UiState>
Composable (state consumer)
    ↓ User events (lambdas)
ViewModel (handles events, updates state)
```

**DON'T:**
- Let Composables modify state directly
- Create bidirectional data flows
- Let multiple sources produce the same state
