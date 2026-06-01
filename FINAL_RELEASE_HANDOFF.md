# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: e643a0e5d4b7c7b169b817dd2fa99ac6f1d2de6978c12ea97e3b8b223657f9b4

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: 8b39c9ae6ad3fdc4af6beb60fd310fa2d287a3fb3617a14032ec298e4b02701d
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: daad90f6259ec0bdc0d8821e3058068d9a35c20d43bf0e74575595af0c3f141c
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: 1bfe1b071865a38a5685c3ff8aa825b1834e454e4a73345a46fb8ee9b577df1a

## Release Status
- release_classification: proof-blocked alpha proof snapshot
- alpha_candidate: true
- self_verifying_alpha: true
- production_release_candidate: false
- production_ready: false
- public_release_safe: false
- proof_complete: true
- blocked_release_checks: []

## Build Metadata
- created_at_utc: 2026-06-01T21:51:13.749783+00:00
- generated_at_utc: 2026-06-01T21:51:13.749783+00:00
- git_commit: unknown
- python: unknown
- node: unknown
- npm: unknown

## Notes
- This is a proof-blocked alpha proof snapshot.
- It is not ready for production deployment.
- Ship only the archive listed above.
- Validation must run against a fresh extraction
  of that archive.
- `release_gate.json` is only valid as a proof artifact when every
  log path it references exists inside `artifacts/proof/current/`
  at packaging time. Do not ship manually zipped working trees.
