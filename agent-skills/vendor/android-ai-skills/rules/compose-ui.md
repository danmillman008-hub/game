# Jetpack Compose UI

> Official source: https://developer.android.com/develop/ui/compose

You are an expert in Jetpack Compose. Write composables that are stateless, testable, and performant. Follow official Compose guidelines for state management, recomposition, and accessibility.

## Screen Pattern (Route + Screen)

> Source: https://developer.android.com/topic/architecture/ui-layer

**DO:**
- Split every screen into a stateful Route and a stateless Screen composable:
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
- Make Screen composables `internal` — expose only the Route
- Use `@Preview` on the stateless Screen composable with sample data

**DON'T:**
- Pass ViewModel directly to Screen composables — pass state and lambdas
- Pass `NavController` to any composable — use callback lambdas
- Mix ViewModel logic and UI in the same composable

## State Management

> Source: https://developer.android.com/develop/ui/compose/state

**DO:**
- Use `remember { mutableStateOf(...) }` for local composable state
- Use `rememberSaveable` for state that must survive configuration changes:
```kotlin
var text by rememberSaveable { mutableStateOf("") }
```
- Hoist state to the lowest common ancestor that reads or writes it
- Use `derivedStateOf` for values computed from other state:
```kotlin
val hasErrors by remember {
    derivedStateOf { username.isBlank() || email.isBlank() }
}
```
- Collect ViewModel state with `collectAsStateWithLifecycle()`:
```kotlin
val uiState by viewModel.uiState.collectAsStateWithLifecycle()
```
- Use `remember(key)` to recompute cached values when dependencies change

**DON'T:**
- Use `collectAsState()` — always use `collectAsStateWithLifecycle()` for lifecycle awareness
- Store ViewModel-managed state in `remember` — let the ViewModel own it
- Read state inside click handlers without wrapping in lambdas (stale captures)
- Use mutable objects (HashMap, ArrayList) as state — Compose won't detect changes

## Recomposition & Performance

> Source: https://developer.android.com/develop/ui/compose/performance

**DO:**
- Keep composables fast, idempotent, and side-effect free
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
- Defer state reads to the latest possible phase (drawing > layout > composition)
- Extract non-recomposing parameters into lambda wrappers

**DON'T:**
- Pass unstable types (List, Map, data classes with var) as parameters without `@Stable`
- Create new lambda instances in composition for frequently recomposing code — use `remember`
- Benchmark performance in debug builds — always use release + R8
- Use `Modifier.offset(x, y)` for animations — use the lambda version `Modifier.offset { }`
- Write backwards — reading state that was already written in the same composition

## Side Effects

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
- Use `rememberUpdatedState` for values referenced in long-running effects
- Use `SideEffect` for publishing Compose state to non-Compose code

**DON'T:**
- Call suspend functions directly from composable body
- Perform I/O, logging, or shared state writes inside composable functions
- Use `LaunchedEffect(Unit)` unless you truly want it to run once per composition

## Material 3 & Theming

> Source: https://developer.android.com/develop/ui/compose/designsystems/material3

**DO:**
- Use Material 3 components from `androidx.compose.material3`
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
- Use `MaterialTheme.colorScheme`, `.typography`, `.shapes` for all styling
- Support dark mode and dynamic color (Material You)

**DON'T:**
- Hardcode colors, font sizes, or shapes in composables
- Use Material 2 (`androidx.compose.material`) in new projects — use Material 3
- Mix Material 2 and Material 3 components

## Design System

> Source: https://developer.android.com/develop/ui/compose/designsystems

**DO:**
- Create reusable design system composables (AppButton, AppCard, AppTextField)
- Centralize spacing, padding, and elevation values
- Place design system in a `core:designsystem` module for multi-module projects

## Accessibility

> Source: https://developer.android.com/develop/ui/compose/accessibility

**DO:**
- Add `contentDescription` to all images and icons:
```kotlin
Icon(
    imageVector = Icons.Default.Close,
    contentDescription = stringResource(R.string.close),
)
```
- Use `Modifier.semantics` for custom accessibility info
- Ensure minimum touch target size of 48dp:
```kotlin
Modifier.sizeIn(minWidth = 48.dp, minHeight = 48.dp)
```
- Support font scaling — use `sp` for text, never hardcode text size in `dp`
- Group related elements with `Modifier.semantics(mergeDescendants = true)`

**DON'T:**
- Leave `contentDescription = null` on meaningful images (decorative-only is fine)
- Use `dp` for text sizes — use `sp`
- Create touch targets smaller than 48dp

## String Resources

> Source: https://developer.android.com/guide/topics/resources/string-resource

**DO:**
- Always use `stringResource(R.string.xyz)` in composables — never hardcoded strings
- Use parameterized strings for dynamic content:
```kotlin
stringResource(R.string.welcome_message, userName)
```
- Use plurals for countable items

**DON'T:**
- Hardcode user-visible text: `Text("Hello")` — use `Text(stringResource(R.string.hello))`
- Use string concatenation for dynamic messages — use string formatting
