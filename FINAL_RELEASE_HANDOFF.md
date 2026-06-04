# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: 535a26286aeea40856b8e19a71aa105dc13ff0d7f6440332c4d330b2967bed6e

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: ca4e5453137fcc29f529da298cdc50cab74bd8cb7b606873f739965ee44f8f4d
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: 8b31f3b7db5ef93313c510efc30bbde5db25b64af4eff400b247b9d0ae308f96
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: 04a08cc394ac84285675ffcec6547b7cd88420c639fc3c2eb0ac5ef9c2961492

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
- created_at_utc: 2026-06-04T23:26:41.680923+00:00
- generated_at_utc: 2026-06-04T23:26:41.680923+00:00
- git_commit: 673826a516c4d12a74cbf88b4536eed79580cfaf
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
