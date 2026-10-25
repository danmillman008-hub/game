package dev.androidagentskills.fixtures.rxjava

import io.reactivex.Completable
import io.reactivex.Observable
import io.reactivex.Single
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers
import java.util.concurrent.TimeUnit

class LegacyTaskRepository {
    fun refreshTasks(): Single<List<String>> {
        return Single.just(listOf("Prepare beta release notes", "Sync offline edits"))
            .delay(150, TimeUnit.MILLISECONDS)
            .subscribeOn(Schedulers.io())
            .observeOn(AndroidSchedulers.mainThread())
    }

    fun taskTicker(): Observable<Long> {
        return Observable.interval(1, TimeUnit.SECONDS)
            .switchMap { tick -> Observable.just(tick) }
            .subscribeOn(Schedulers.computation())
            .observeOn(AndroidSchedulers.mainThread())
    }

    fun markReminderReviewed(): Completable {
        return Completable.fromAction { println("Reminder reviewed") }
            .subscribeOn(Schedulers.io())
    }
}
