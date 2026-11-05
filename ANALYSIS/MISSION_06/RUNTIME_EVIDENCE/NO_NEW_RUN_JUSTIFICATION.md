# Why M06 deliberately ran no new emulator experiment

1. **Local capability** — the sandbox has no emulator, ADB, Android SDK, Java or KVM.
   Runtime host facts in this repository come from GitHub Actions (M03/M04/M05).
2. **Hypotheses resolved statically** — the specific M06 questions (which field
   `isSolvedCorrectly` reads; what `createLessonProgress` writes; how each interaction
   validates; whether `solvedContent` suffices; what the offline gate is) are decidable
   from DEX bytecode and were answered `VERIFIED_STATIC`. A screenshot cannot prove a
   register read.
3. **Standing constraint** — M05 established that the only way to reach an answer screen
   is the deterministic exact 24-tap chain of run `42003884423`; a repeat without that
   exact replay was ruled out. Repeating UI screenshots was explicitly excluded.
4. **The one remaining runtime hypothesis** — reading `lesson_progress` after a correct
   answer — requires root / private app-database extraction, which is forbidden.
5. **Backend boundary** — server response bodies, scoring/economy awards and remote code
   execution were deliberately out of scope; no workflow dispatch was made.

Therefore M06 reused M05 runs 001–005 with explicit `VERIFIED_RUNTIME` / `VERIFIED_BOTH`
classification in `M06_HYPOTHESIS_CORRELATION.md` and recorded the correct-answer state,
persisted-progress-after-answer and server responses as `UNKNOWN` in
`../18_OPEN_QUESTIONS.md`. `SERVER CONFIRMED = 0`.
