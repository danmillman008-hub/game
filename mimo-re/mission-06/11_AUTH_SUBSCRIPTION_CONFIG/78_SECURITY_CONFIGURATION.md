# Mission 6 — Security Configuration (client surface)

## Scope
Client-side security posture: transport, storage, backup, cleartext, certificate pinning.

## Method
`network_security_config` (decoded), manifest flags, interceptor inspection, Keystore/crypto usage search.

## Findings (VERIFIED_STATIC)
1. `allowBackup=false` and `requestLegacyExternalStorage=true` (manifest).
2. No certificate-pinning `CertificatePinner` call was found in the recovered OkHttp builder (case 20) —
   transport relies on system trust (`VERIFIED_STATIC` for the recovered constructor, subject to `Q-120`).
3. `network_security_config.xml` exists; its content governs cleartext. Whether cleartext is permitted for
   any domain was not fully decoded (`Q-120`) — the API hosts are all HTTPS in code.
4. Token storage: read via `ri.b`/`d(0)`; whether it is EncryptedSharedPreferences/Keystore-backed is
   **NOT_RECOVERED** (`Q-121`).
5. The APK itself is **re-signed by a third party** (`META-INF/YOUAREFINISHED.RSA`) and carries a Mod
   watermark in 11,543 const-strings — so any *integrity* claim about this artifact is void, and injected
   `bin.ghost`/`libyrf.so` code must be treated as foreign (see `00_BASELINE/INTEGRITY_CAVEAT.md`).

## Evidence labels
1, 2, 3, 5 **VERIFIED_STATIC**; 4 **NOT_RECOVERED**.

## Open questions
`Q-120` pinning/cleartext; `Q-121` token storage mechanism; `Q-122` root/emulator detection (only foreign
classes found).

## Reproduction
`grep -c pin /tmp/dad/ae.m.java; cat /tmp/res/res/xml/network_security_config.xml`
