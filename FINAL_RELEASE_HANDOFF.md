# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: 2d27ee5ae0c876f5807f4a69336bba3a4c2cb4941f62ea0873e1c12c1f48c230

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: db9a81f81124b7ed21809805bc7b2ee3528f9b320e50c17ead26656b99622ad0
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: 0ccfc4abc0e8a588860f9e3188f52e427ef3cc624df0ff5b9ee2eab87cce569d
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: cd8efa4192d21e0f0abaf0619ee0539d90308d203d60771a8740dbf18cfabda6

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
- created_at_utc: 2026-06-05T01:51:51.382151+00:00
- generated_at_utc: 2026-06-05T01:51:51.382151+00:00
- git_commit: fac262a453e85318535bbe00222971452f24349e
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
