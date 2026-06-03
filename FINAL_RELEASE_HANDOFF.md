# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: 1b4ec17b8dbc199931a22fed4e114a71d2c9d8b870a04da61718343ca91ed317

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: 325924516c164624db00a3ca4ffb171656788f09994d0edd31a453d9390d81f8
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: 0c0f0155a08097018a501489850ba506e0290424ed9cb5f3d8825d97e7e6067b
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: 94e94a2f4ef03811414782bbe7714dd284ab7b32913219bc10a7ae762a1e7245

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
- created_at_utc: 2026-06-03T08:10:16.735275+00:00
- generated_at_utc: 2026-06-03T08:10:16.735275+00:00
- git_commit: cb7ab218f33c6c15a3fe6a4074b3f3dff419d478
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
