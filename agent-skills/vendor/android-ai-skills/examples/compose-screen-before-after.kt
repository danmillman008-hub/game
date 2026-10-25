/**
 * Compose Screen — Before & After AI Rules
 *
 * WITHOUT rules, AI assistants generate screens with:
 * - ViewModel passed to composables
 * - NavController threaded through the tree
 * - No state hoisting (stateful composables)
 * - collectAsState instead of collectAsStateWithLifecycle
 *
 * WITH android-ai-skills, AI assistants generate properly structured screens.
 */

// ============================================================
// ❌ WITHOUT RULES — What AI typically generates
// ============================================================

@Composable
fun ProfileScreen(navController: NavController) {
    val viewModel: ProfileViewModel = viewModel()
    val name by viewModel.name.observeAsState("")
    val loading by viewModel.loading.observeAsState(false)

    Column(modifier = Modifier.padding(16.dp)) {
        if (loading) {
            CircularProgressIndicator()
        } else {
            Text(
                text = "Hello, $name",       // hardcoded string
                fontSize = 24.sp,             // inline styling
                color = Color(0xFF333333),    // hardcoded color
            )
            Button(onClick = { navController.navigate("settings") }) {
                Text("Settings")
            }
        }
    }
}


// ============================================================
// ✅ WITH RULES — What AI generates with android-ai-skills
// ============================================================

/**
 * Rules applied:
 * - Route + Screen pattern: stateful Route, stateless Screen (compose-ui.md)
 * - collectAsStateWithLifecycle instead of collectAsState (compose-ui.md)
 * - NavController NOT passed to composables — lambdas instead (navigation.md)
 * - hiltViewModel() for DI (dependency-injection.md)
 * - stringResource() instead of hardcoded strings (compose-ui.md)
 * - MaterialTheme tokens instead of hardcoded colors (compose-ui.md)
 * - Modifier.testTag for testability (testing.md)
 * - Accessibility: contentDescription on icons (compose-ui.md)
 */

// --- Route: Stateful wrapper ---
@Composable
fun ProfileRoute(
    onNavigateToSettings: () -> Unit,
    onNavigateBack: () -> Unit,
    viewModel: ProfileViewModel = hiltViewModel(),
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    ProfileScreen(
        uiState = uiState,
        onNavigateToSettings = onNavigateToSettings,
        onNavigateBack = onNavigateBack,
        onRetry = viewModel::retry,
    )
}

// --- Screen: Stateless, testable, previewable ---
@Composable
internal fun ProfileScreen(
    uiState: ProfileUiState,
    onNavigateToSettings: () -> Unit,
    onNavigateBack: () -> Unit,
    onRetry: () -> Unit,
) {
    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text(stringResource(R.string.profile_title)) },
                navigationIcon = {
                    IconButton(onClick = onNavigateBack) {
                        Icon(
                            imageVector = Icons.AutoMirrored.Filled.ArrowBack,
                            contentDescription = stringResource(R.string.navigate_back),
                        )
                    }
                },
            )
        },
    ) { innerPadding ->
        when (uiState) {
            is ProfileUiState.Loading -> {
                Box(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(innerPadding),
                    contentAlignment = Alignment.Center,
                ) {
                    CircularProgressIndicator(
                        modifier = Modifier.testTag("loading_indicator"),
                    )
                }
            }

            is ProfileUiState.Success -> {
                Column(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(innerPadding)
                        .padding(horizontal = 16.dp),
                ) {
                    Text(
                        text = stringResource(R.string.welcome_message, uiState.profile.name),
                        style = MaterialTheme.typography.headlineMedium,
                        color = MaterialTheme.colorScheme.onSurface,
                    )
                    Spacer(modifier = Modifier.height(16.dp))
                    Button(onClick = onNavigateToSettings) {
                        Text(stringResource(R.string.settings))
                    }
                }
            }

            is ProfileUiState.Error -> {
                ErrorContent(
                    message = uiState.message,
                    onRetry = onRetry,
                    modifier = Modifier.padding(innerPadding),
                )
            }
        }
    }
}

// --- Preview ---
@Preview(showBackground = true)
@Composable
private fun ProfileScreenPreview() {
    AppTheme {
        ProfileScreen(
            uiState = ProfileUiState.Success(
                profile = Profile(
                    id = "1",
                    name = "Nadeem",
                    email = "nadeem@example.com",
                    avatarUrl = "",
                ),
            ),
            onNavigateToSettings = {},
            onNavigateBack = {},
            onRetry = {},
        )
    }
}
