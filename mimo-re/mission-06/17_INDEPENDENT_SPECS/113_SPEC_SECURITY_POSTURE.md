# Spec 113 — Security Posture (defensive)

## MUST
1. Treat client progress as an unverified assertion; validate server-side.
2. Treat content packs as untrusted input; there is no signature check in the client.
3. Keep two palettes and no secret material in resources (this mission extracted none).
4. Document that the analysed APK is **third-party re-signed**; never cite its integrity behaviour as
   Mimo's.

## MUST NOT
- Describe or enable auth/payment/licence bypass, backend probing, or key extraction.
- Rely on obfuscation for protection.

## GIVEN EVIDENCE
`14_SECURITY/90..93`.
