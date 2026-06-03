# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: e8c1301749a76e9eb05ab863b657626420dcb173f35c72608dd20dad293cce49

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: bfe944d00050c96af1ffae2993ab255e168442451ca2c6f1b5b9f2aab6c220e8
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: 52b856995edb20a682ae25f97e1f4369053315e21e86ba8804bca49429fbd9f1
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: 7ed76bd5c9d72eb93f6e9185c71c8ae03894eccf7f686749b9657539e5c3f15e

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
- created_at_utc: 2026-06-03T03:18:11.776395+00:00
- generated_at_utc: 2026-06-03T03:18:11.776395+00:00
- git_commit: 98778ed21a662fddd3fd5093021a3dbb233a0ba3
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
