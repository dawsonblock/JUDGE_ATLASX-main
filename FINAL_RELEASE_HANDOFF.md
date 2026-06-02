# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: 657ec855f26cb30505b915c3611c4705be25aeb1c44684d1a68d032611162c93

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: 2d85780e8b78738e8030e821fd11a2ffa2c87e6d8890b4b6de6b006b3a5eef54
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: 2e5619290ce855fce1fed79e3cc64063d37c2ed5e2e3d822eeeb7d65765691ba
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: 1f8ef35d4ba1ceb45f24d72053a2cd820bab1e9d8e99394d194cff8c5faedee3

## Release Status
- release_classification: self-verifying alpha
- alpha_candidate: true
- self_verifying_alpha: true
- production_release_candidate: false
- production_ready: false
- public_release_safe: false
- proof_complete: true
- blocked_release_checks: []

## Build Metadata
- created_at_utc: 2026-06-02T08:28:00.137782+00:00
- generated_at_utc: 2026-06-02T08:28:00.137782+00:00
- git_commit: 7964167cc38d7b8844adf0d10719de875b774115
- platform: macOS-26.2-arm64-arm-64bit
- python: 3.11.9
- node: v22.22.3
- npm: 10.9.8

## Notes
- This is a self-verifying alpha.
- It is not ready for production deployment.
- Ship only the archive listed above.
- Validation must run against a fresh extraction
  of that archive.
- `release_gate.json` is only valid as a proof artifact when
  every log path it references exists inside
  `artifacts/proof/current/`
  at packaging time. Do not ship manually zipped working trees.
