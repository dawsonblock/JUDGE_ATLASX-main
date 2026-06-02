# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: cba7f7aed49fc12992a518ea75b8f6e413496144299e8b9521b43d03bba803f0

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: 0977e210eb68af58fd4de8f9d01ad5065e7d912538cd59ebdaf4ab23b46c28de
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: c68e8f6f76c31b3603b63434f50d6f74dfde1d44f0b4d212ed8c82e5b4ee3705
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: 8c74623a1e08e8eeff06e33728d778c2de507d11e4f3cb90d52be75c718d4862

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
- created_at_utc: 2026-06-02T06:41:39.800297+00:00
- generated_at_utc: 2026-06-02T06:41:39.800297+00:00
- git_commit: d81f5b347d4449c15aa5c4311448730c51f476dd
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
