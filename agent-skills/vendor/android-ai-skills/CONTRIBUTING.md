# Contributing to Android AI Skills

Thanks for your interest in contributing! This project aims to be the definitive collection of Android best practices for AI coding assistants.

## How to Contribute

### Adding a New Rule

1. **Find the right file** — Rules are organized by domain in `rules/`. Pick the file that matches your rule's topic.
2. **Follow the format** — Each rule should have:
   - A clear heading
   - Source URL from official Android documentation
   - **DO** section with correct patterns and code examples
   - **DON'T** section with anti-patterns
3. **Include code examples** — Code examples are critical for AI tools to understand the pattern.
4. **Back it with official docs** — Every rule must reference official Android/Google documentation.

### Rule Quality Checklist

Before submitting, ensure your rule:

- [ ] Is backed by official Android documentation (include URL)
- [ ] Has a clear DO and DON'T section
- [ ] Includes Kotlin code examples
- [ ] Is actionable (specific enough for an AI to follow)
- [ ] Doesn't duplicate an existing rule
- [ ] Uses current/modern APIs (no deprecated patterns)

### Fixing an Existing Rule

- Update outdated API references
- Improve code examples
- Fix incorrect recommendations
- Add missing source URLs

### Adding Support for a New AI Tool

If you want to add support for a new AI coding tool:

1. Create a new directory: `toolname/`
2. Add the formatted rules file
3. Update the README with quick start instructions
4. Submit a PR

## Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b add-rule-xyz`
3. Make your changes
4. Ensure your changes follow the existing format
5. Submit a pull request with a clear description

### PR Title Format

- `rule: add [topic] to [domain]` — for new rules
- `fix: update [topic] in [domain]` — for corrections
- `tool: add [tool name] support` — for new tool formats
- `docs: update [section]` — for documentation changes

## What We Don't Accept

- Rules not backed by official documentation
- Subjective style preferences (tabs vs spaces, naming bikeshedding)
- Framework-specific rules for non-standard libraries (unless widely adopted)
- Marketing or promotional content

## Code of Conduct

Be respectful, constructive, and focused on making Android development better for everyone.

## Questions?

Open an issue with the "question" label and we'll help out.
