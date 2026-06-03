# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: b1f74171a7a5890d41632e280411cdcbb8dcfc4790061a2b2293b8decfeb244e

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: c50e5dd28573e0e4e693ad6e7de04c6b42b24a66959cfe91fe7f39ab368a8283
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: d578f4b3a711224f46638d85f9d231067382fd486d6dd4b6588a8a50fbabbc15
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: 6b6433389ae1b662ef3e73bff8bc68b543ee9f25ba080a5aa07337060895a7be

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
- created_at_utc: 2026-06-03T04:47:05.566581+00:00
- generated_at_utc: 2026-06-03T04:47:05.566581+00:00
- git_commit: 53a4f1bc553f0b6d2e14ca4b494862b8d0f59785
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
