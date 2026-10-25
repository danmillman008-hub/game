package dev.androidagentskills.fixtures.rxjava

import io.reactivex.disposables.CompositeDisposable
import io.reactivex.subjects.BehaviorSubject
import io.reactivex.subjects.PublishSubject

class LegacyTaskBoardViewModel(
    private val repository: LegacyTaskRepository = LegacyTaskRepository(),
) {
    private val disposables = CompositeDisposable()
    val uiState = BehaviorSubject.createDefault(TaskBoardState(isLoading = true))
    val events = PublishSubject.create<String>()

    fun load() {
        disposables.add(
            repository.refreshTasks().subscribe(
                { tasks -> uiState.onNext(TaskBoardState(tasks = tasks, isLoading = false)) },
                { error -> events.onNext(error.message ?: "Unknown error") },
            )
        )
    }

    fun clear() {
        disposables.clear()
    }
}

data class TaskBoardState(
    val tasks: List<String> = emptyList(),
    val isLoading: Boolean = false,
)
