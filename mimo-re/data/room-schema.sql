-- Room schema recovered from DEX string constants (com.getmimo.data.source.local.room.Database)

CREATE TABLE IF NOT EXISTS `chapter_completions` (`chapter_id` INTEGER NOT NULL, `created_at` INTEGER NOT NULL, `track_id` INTEGER NOT NULL, `tutorial_id` INTEGER NOT NULL, PRIMARY KEY(`chapter_id`, `track_id`))

CREATE TABLE IF NOT EXISTS `lesson_progress` (`lesson_id` INTEGER NOT NULL, `completed_at` INTEGER NOT NULL, `started_at` INTEGER NOT NULL, `tries` INTEGER NOT NULL, `tutorial_id` INTEGER NOT NULL, `tutorial_version` INTEGER NOT NULL, `track_id` INTEGER NOT NULL, `publish_set_version` INTEGER NOT NULL, `attempts` INTEGER NOT NULL, `is_practice_progress` INTEGER NOT NULL, `in_queue` INTEGER NOT NULL, PRIMARY KEY(`lesson_id`, `tutorial_id`))

CREATE TABLE IF NOT EXISTS `tutorial_completions` (`tutorial_id` INTEGER NOT NULL, `is_completed` INTEGER NOT NULL, `updated_at` INTEGER NOT NULL, `track_id` INTEGER NOT NULL, PRIMARY KEY(`tutorial_id`, `track_id`))
