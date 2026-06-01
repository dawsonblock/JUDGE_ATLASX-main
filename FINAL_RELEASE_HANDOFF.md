# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: e643a0e5d4b7c7b169b817dd2fa99ac6f1d2de6978c12ea97e3b8b223657f9b4

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: b23787909bc51619ad955c5889d2af5a99b248c9454dc4a5b9068ee619631316
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: c7ea9717504b81e6c57db3a8b60fa1f4b57dc157bfbfd798e1553e94c2010f06
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: 577aed376bb6b3389178fdc6d96f6f38444513a63cce7282a7cd4228fffd3d28

## Release Status
- release_classification: proof-blocked alpha proof snapshot
- alpha_gate_passed: false
- release_candidate: false
- production_ready: false
- proof_complete: false
- blocked_release_checks: ["backend_pytest", "docker_runtime_preflight", "docker_smoke", "postgis_proof", "archive_validation", "required_proof_logs", "validation_summary_missing"]

## Build Metadata
- created_at_utc: 2026-06-01T07:31:10.589650+00:00
- generated_at_utc: 2026-06-01T07:31:10.589650+00:00
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
