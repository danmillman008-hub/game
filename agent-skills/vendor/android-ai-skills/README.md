# Android AI Skills

**Production-grade Android rules for AI coding assistants.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

Works with **Cursor** | **Claude Code** | **GitHub Copilot** | **OpenAI Codex** | **Windsurf**

---

## The Problem

AI coding assistants generate Android code that works but isn't production-ready. Without guidance, they default to:

- `GlobalScope.launch` instead of `viewModelScope`
- `MutableLiveData` exposed directly instead of `StateFlow` with sealed UI state
- Hardcoded strings, colors, and inline styling instead of resources and Material theme tokens
- `NavController` passed through the composable tree instead of callback lambdas
- No offline support, no caching — direct API calls from ViewModel
- `SharedPreferences` instead of DataStore, KAPT instead of KSP, Gson instead of Kotlin Serialization
- No test structure, no fakes, no separation of concerns

This compounds fast. By the time you notice, your codebase has architectural debt baked into every file the AI touched.

## What This Solves

**Android AI Skills** is a set of rule files you drop into your Android project. Your AI assistant reads them and generates code that follows official Google/Android architecture guidance — automatically, on every prompt.

**What changes in your project:**

- **Architecture** — Layered architecture with proper UDF. ViewModels expose immutable `StateFlow<UiState>`, business logic lives in UseCases, data flows through Repositories. No shortcuts.
- **Compose UI** — Every screen follows the Route + Screen pattern: stateful Route connects ViewModel, stateless Screen is testable and previewable. State hoisted correctly, `collectAsStateWithLifecycle()` used everywhere.
- **Data layer** — Offline-first by default. Room as source of truth, separate models per layer (Network, Entity, Domain), DataStore for preferences. Your app works without internet.
- **Testing** — Fakes over mocks (the Now in Android way). ViewModels tested with Turbine, Compose screens tested with semantics. Test structure generated alongside feature code.
- **Build quality** — KSP instead of KAPT (2x faster builds), version catalogs, convention plugins for multi-module, R8 enabled, Baseline Profiles for startup.
- **Security** — Encrypted storage for sensitive data, network security config, no secrets in source code, input validation at boundaries.

**Every rule links to official Android documentation.** Nothing opinionated without a source.

---

## Quick Start

Copy one file into your project. Done.

### Cursor (Modern — Recommended)

```bash
cp -r cursor/rules/ your-project/.cursor/rules/
```

### Cursor (Legacy — Single File)

```bash
cp cursor/.cursorrules your-project/.cursorrules
```

### Claude Code

```bash
cp claude/CLAUDE.md your-project/CLAUDE.md
```

### GitHub Copilot

```bash
mkdir -p your-project/.github
cp copilot/.github/copilot-instructions.md your-project/.github/copilot-instructions.md
```

### OpenAI Codex

```bash
cp codex/AGENTS.md your-project/AGENTS.md
```

### Windsurf

```bash
cp windsurf/.windsurfrules your-project/.windsurfrules
```

**That's it.** Your AI assistant now follows Android best practices on every prompt.

---

## What's Inside

| Domain | Key Topics | Rules |
|--------|-----------|-------|
| [Architecture](rules/architecture.md) | Layered architecture, UDF, ViewModel, UseCases, Repository pattern | 25+ |
| [Compose UI](rules/compose-ui.md) | State management, recomposition, Route+Screen pattern, Material 3, accessibility | 30+ |
| [Data Layer](rules/data-layer.md) | Room (KSP), DataStore, offline-first, Kotlin Serialization, Coil, Paging 3 | 30+ |
| [Dependency Injection](rules/dependency-injection.md) | Hilt setup, modules, scoping, Compose integration, testing | 20+ |
| [Navigation](rules/navigation.md) | Type-safe routes, decoupled navigation, arguments, deep links | 15+ |
| [Testing](rules/testing.md) | Fakes over mocks, ViewModel testing, Compose UI testing, Turbine | 20+ |
| [Build & Tooling](rules/build-tooling.md) | Gradle KTS, version catalogs, KSP, modularization, convention plugins, R8 | 20+ |
| [Performance](rules/performance.md) | Recomposition, lazy layouts, app startup, Baseline Profiles, benchmarking | 20+ |
| [Security](rules/security.md) | Encrypted storage, secrets, network security, input validation, permissions | 20+ |
| [Modern Android](rules/modern-android.md) | Edge-to-edge, predictive back, Splash Screen API, WorkManager, coroutines | 25+ |

Every rule is backed by [official Android documentation](https://developer.android.com/topic/architecture) with source links included.

---

## Before & After

### ViewModel — Without vs. With Rules

<details>
<summary>Click to expand</summary>

**Without rules** — AI generates this:

```kotlin
class ProfileViewModel : ViewModel() {
    var name = MutableLiveData<String>()
    var loading = MutableLiveData<Boolean>()

    fun loadProfile() {
        loading.value = true
        GlobalScope.launch {
            val result = api.getProfile()
            name.postValue(result.name)
            loading.postValue(false)
        }
    }
}
```

**With android-ai-skills** — AI generates this:

```kotlin
@HiltViewModel
class ProfileViewModel @Inject constructor(
    private val getProfileUseCase: GetProfileUseCase,
    savedStateHandle: SavedStateHandle,
) : ViewModel() {

    private val userId: String = checkNotNull(savedStateHandle["userId"])

    private val _uiState = MutableStateFlow<ProfileUiState>(ProfileUiState.Loading)
    val uiState: StateFlow<ProfileUiState> = _uiState.asStateFlow()

    init { loadProfile() }

    private fun loadProfile() {
        viewModelScope.launch {
            _uiState.value = getProfileUseCase(userId).fold(
                onSuccess = { ProfileUiState.Success(it) },
                onFailure = { ProfileUiState.Error(it.message ?: "Unknown error") },
            )
        }
    }
}

sealed interface ProfileUiState {
    data object Loading : ProfileUiState
    data class Success(val profile: Profile) : ProfileUiState
    data class Error(val message: String) : ProfileUiState
}
```

</details>

### Compose Screen — Without vs. With Rules

<details>
<summary>Click to expand</summary>

**Without rules:**

```kotlin
@Composable
fun ProfileScreen(navController: NavController) {
    val vm = viewModel<ProfileViewModel>()
    val name by vm.name.observeAsState("")
    Text("Hello, $name", fontSize = 24.sp, color = Color(0xFF333333))
    Button(onClick = { navController.navigate("settings") }) { Text("Settings") }
}
```

**With android-ai-skills:**

```kotlin
// Route: stateful, connects ViewModel
@Composable
fun ProfileRoute(
    onNavigateToSettings: () -> Unit,
    viewModel: ProfileViewModel = hiltViewModel(),
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    ProfileScreen(uiState = uiState, onNavigateToSettings = onNavigateToSettings)
}

// Screen: stateless, testable, previewable
@Composable
internal fun ProfileScreen(
    uiState: ProfileUiState,
    onNavigateToSettings: () -> Unit,
) {
    when (uiState) {
        is ProfileUiState.Loading -> CircularProgressIndicator()
        is ProfileUiState.Success -> {
            Text(
                text = stringResource(R.string.welcome, uiState.profile.name),
                style = MaterialTheme.typography.headlineMedium,
            )
            Button(onClick = onNavigateToSettings) {
                Text(stringResource(R.string.settings))
            }
        }
        is ProfileUiState.Error -> ErrorContent(message = uiState.message)
    }
}
```

</details>

### Data Layer — Without vs. With Rules

<details>
<summary>Click to expand</summary>

**Without rules** — ViewModel calls API directly, no caching:

```kotlin
class ArticleListViewModel : ViewModel() {
    val articles = MutableLiveData<List<Article>>()
    fun load() {
        viewModelScope.launch {
            articles.value = RetrofitClient.api.getArticles() // no offline support
        }
    }
}
```

**With android-ai-skills** — Offline-first with proper layer separation:

```kotlin
// Separate models per layer
@Serializable
data class NetworkArticle(@SerialName("article_id") val id: String, val title: String)

@Entity(tableName = "articles")
data class ArticleEntity(@PrimaryKey val id: String, val title: String)

data class Article(val id: String, val title: String)

// Repository: single entry point, offline-first
class ArticleRepository @Inject constructor(
    private val remote: ArticleRemoteDataSource,
    private val local: ArticleLocalDataSource,
) {
    fun observeArticles(): Flow<List<Article>> =
        local.observeArticles().map { it.map(ArticleEntity::toDomain) }

    suspend fun sync(): Result<Unit> = runCatching {
        val articles = remote.fetchArticles()
        local.upsertAll(articles.map(NetworkArticle::toEntity))
    }
}
```

</details>

See full examples in the [`examples/`](examples/) directory.

---

## Customizing for Your Project

These rules target modern greenfield Android projects. If your project uses a different stack or has legacy code, you can and should customize them.

### How to Customize

The rules files are plain markdown. Edit them directly in your project after copying:

**1. Swap libraries** — If your project uses Koin instead of Hilt, or Moshi instead of Kotlin Serialization, update the relevant rules:

```markdown
// In your project's CLAUDE.md or .cursorrules, change:

**DO:**
- Use Koin for dependency injection
- Define modules with `module { }` DSL
- Use `koinViewModel()` in Compose

**DON'T:**
- Use Hilt annotations in this project
```

**2. Adjust for legacy code** — If parts of your app still use XML Views, LiveData, or Java, add context so the AI understands what to use where:

```markdown
## Project-Specific Context

This is a legacy project being migrated to Compose. Follow these rules:

- New screens: Use Jetpack Compose with the rules below
- Existing screens in `feature/legacy/`: Use XML Views + ViewBinding. Do NOT convert to Compose unless explicitly asked.
- ViewModels in `feature/legacy/`: Use LiveData (existing pattern). New ViewModels: use StateFlow.
- Navigation: This project uses Navigation Component with Fragments. Do NOT use Navigation Compose.
- DI: This project uses Dagger (not Hilt). Follow existing Dagger module patterns in `di/` package.
```

**3. Remove rules you don't need** — Building a small app? Delete the modularization, convention plugins, and Baseline Profile rules. Keep what applies to your scale.

**4. Add project-specific patterns** — Every team has conventions. Add yours:

```markdown
## Project Conventions

- All API response classes live in `data/remote/model/` and are prefixed with `Api` (e.g., `ApiUser`)
- Feature packages follow: `feature/{name}/ui/`, `feature/{name}/data/`, `feature/{name}/domain/`
- All strings use the format `R.string.feature_screen_element` (e.g., `R.string.profile_settings_title`)
- Error handling: Use the project's `AppError` sealed class, not raw exceptions
```

### What to Keep vs. What to Change

| Keep as-is (universal) | Customize per project |
|------------------------|----------------------|
| State hoisting | DI framework (Hilt/Koin/Dagger) |
| Immutable UI state | Networking library (Retrofit/Ktor) |
| Repository pattern | Module structure |
| Fakes over mocks | Naming conventions |
| No hardcoded strings | Legacy code boundaries |
| KSP over KAPT | JSON library |
| Process death handling | Navigation approach |

The architecture principles are universal. The specific libraries and conventions depend on your project.

---

## Supported Tools

| Tool | File | Format | Location |
|------|------|--------|----------|
| **Cursor** (modern) | `.mdc` files | YAML frontmatter + markdown | `.cursor/rules/` |
| **Cursor** (legacy) | `.cursorrules` | Plain markdown | Project root |
| **Claude Code** | `CLAUDE.md` | Markdown | Project root |
| **GitHub Copilot** | `copilot-instructions.md` | Markdown | `.github/` |
| **OpenAI Codex** | `AGENTS.md` | Markdown | Project root |
| **Windsurf** | `.windsurfrules` | Markdown | Project root |

All formats contain the same rules — pick the one matching your tool.

---

## Opinionated Stack

These rules enforce a specific, modern Android stack based on official Google recommendations:

| Choice | Over | Why |
|--------|------|-----|
| **Jetpack Compose** | XML Views | Official recommended UI toolkit |
| **Material 3** | Material 2 | Current design system with dynamic color |
| **StateFlow** | LiveData | Kotlin-native, works with Compose lifecycle |
| **Hilt** | Koin / Manual DI | Compile-time safety, official Google recommendation |
| **KSP** | KAPT | 2x faster, KAPT is in maintenance mode |
| **Room** | SQLite / Realm | Official Jetpack persistence, Flow support |
| **DataStore** | SharedPreferences | Type-safe, async, coroutine-native |
| **Kotlin Serialization** | Gson / Moshi | Kotlin-native, multiplatform, no reflection |
| **Coil** | Glide / Picasso | Built for Compose, coroutine-native |
| **Fakes** | Mockito / MockK | More maintainable (per Now in Android) |
| **Turbine** | Manual Flow testing | Industry standard for StateFlow/Flow testing |

Not using this exact stack? See [Customizing for Your Project](#customizing-for-your-project) above.

---

## Project Structure

```
android-ai-skills/
├── rules/                    # Canonical source — 10 domain files
│   ├── architecture.md
│   ├── compose-ui.md
│   ├── data-layer.md
│   ├── dependency-injection.md
│   ├── navigation.md
│   ├── testing.md
│   ├── build-tooling.md
│   ├── performance.md
│   ├── security.md
│   └── modern-android.md
├── cursor/                   # Cursor formats
│   ├── .cursorrules          # Legacy single-file
│   └── rules/                # Modern .mdc files
├── claude/CLAUDE.md          # Claude Code
├── copilot/.github/          # GitHub Copilot
├── codex/AGENTS.md           # OpenAI Codex
├── windsurf/.windsurfrules   # Windsurf
└── examples/                 # Before/after Kotlin code
```

The `rules/` directory is the single source of truth. Tool-specific files are generated from it using `scripts/generate.sh`.

---

## Contributing

Contributions welcome. Whether it's a new rule, a fix to an existing one, or support for a new AI tool.

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

[MIT](LICENSE)

---

## References

All rules are based on official Android documentation:
- [Android Architecture Guide](https://developer.android.com/topic/architecture)
- [Jetpack Compose](https://developer.android.com/develop/ui/compose)
- [Now in Android](https://github.com/android/nowinandroid) — Google's reference app
- [Android Testing](https://developer.android.com/training/testing)
- [Android Security](https://developer.android.com/topic/security/best-practices)
