/**
 * ViewModel — Before & After AI Rules
 *
 * WITHOUT rules, AI assistants generate ViewModels with:
 * - MutableLiveData exposed directly
 * - GlobalScope for coroutines
 * - No dependency injection
 * - No proper state modeling
 *
 * WITH android-ai-skills, AI assistants generate production-ready code.
 */

// ============================================================
// ❌ WITHOUT RULES — What AI typically generates
// ============================================================

class ProfileViewModel : ViewModel() {
    var name = MutableLiveData<String>()
    var email = MutableLiveData<String>()
    var loading = MutableLiveData<Boolean>()
    var error = MutableLiveData<String?>()

    private val api = RetrofitClient.create() // hardcoded dependency

    fun loadProfile(userId: String) {
        loading.value = true
        GlobalScope.launch {
            try {
                val result = api.getProfile(userId)
                name.postValue(result.name)
                email.postValue(result.email)
                loading.postValue(false)
            } catch (e: Exception) {
                error.postValue(e.message)
                loading.postValue(false)
            }
        }
    }
}


// ============================================================
// ✅ WITH RULES — What AI generates with android-ai-skills
// ============================================================

/**
 * Rules applied:
 * - @HiltViewModel with @Inject constructor (dependency-injection.md)
 * - Sealed interface for mutually exclusive UI states (architecture.md)
 * - StateFlow instead of LiveData (architecture.md)
 * - Private MutableStateFlow, public StateFlow (architecture.md)
 * - UseCase for business logic delegation (architecture.md)
 * - viewModelScope instead of GlobalScope (modern-android.md)
 * - SavedStateHandle for process death survival (modern-android.md)
 */

// --- UI State ---
sealed interface ProfileUiState {
    data object Loading : ProfileUiState
    data class Success(val profile: Profile) : ProfileUiState
    data class Error(val message: String) : ProfileUiState
}

// --- Domain Model ---
data class Profile(
    val id: String,
    val name: String,
    val email: String,
    val avatarUrl: String,
)

// --- UseCase ---
class GetProfileUseCase @Inject constructor(
    private val userRepository: UserRepository,
) {
    suspend operator fun invoke(userId: String): Result<Profile> {
        return userRepository.getProfile(userId)
    }
}

// --- ViewModel ---
@HiltViewModel
class ProfileViewModel @Inject constructor(
    private val getProfileUseCase: GetProfileUseCase,
    savedStateHandle: SavedStateHandle,
) : ViewModel() {

    private val userId: String = checkNotNull(savedStateHandle["userId"])

    private val _uiState = MutableStateFlow<ProfileUiState>(ProfileUiState.Loading)
    val uiState: StateFlow<ProfileUiState> = _uiState.asStateFlow()

    init {
        loadProfile()
    }

    private fun loadProfile() {
        viewModelScope.launch {
            _uiState.value = ProfileUiState.Loading
            _uiState.value = getProfileUseCase(userId).fold(
                onSuccess = { ProfileUiState.Success(it) },
                onFailure = { ProfileUiState.Error(it.message ?: "Unknown error") },
            )
        }
    }

    fun retry() = loadProfile()
}
