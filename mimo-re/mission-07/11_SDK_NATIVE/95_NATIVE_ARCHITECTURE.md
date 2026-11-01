# Mission 7 — Native Architecture

## Facts
- Four `.so` files, two ABIs, all 64/32-bit ARM; **no x86**, so the app cannot run on the default emulator image.
- Two libraries are third-party runtimes with Java-side wrappers (Rive, Adjust).
- One is the C++ runtime.
- `libyrf.so` is specific to this build and is paired with the injected base Application.

## What native code does *not* do (evidence-based)
No native crypto for API payloads (no JNI crypto calls in Mimo data code), no native networking, no native
content parsing — the DSL is parsed in Java/Kotlin.

## Limitation
Without `readelf`/`objdump`/`nm` and without disassembly, symbol-level claims are impossible here. This is a
genuine environment limitation, recorded as such, not a claim of non-existence.
