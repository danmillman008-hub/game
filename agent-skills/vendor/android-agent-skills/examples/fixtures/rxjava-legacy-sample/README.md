# RxJava Legacy Sample

A lightweight source-only fixture for the `android-rxjava-to-coroutines-migration` skill.

This fixture is intentionally not a full Android app. It exists so the migration scripts can scan:
- `Single`, `Observable`, and `Completable`
- `BehaviorSubject` and `PublishSubject`
- `CompositeDisposable`
- `subscribeOn`, `observeOn`, and `switchMap`

Use it with:

```bash
python3 skills/android-rxjava-to-coroutines-migration/scripts/scan_rxjava_usage.py examples/fixtures/rxjava-legacy-sample
python3 skills/android-rxjava-to-coroutines-migration/scripts/generate_migration_checklist.py examples/fixtures/rxjava-legacy-sample
```
