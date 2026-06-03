# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: a83f7d41ddeb8e0037d45243e2a094d449eb9dd75b15eb7a88d2b52badf00965

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: 36c5ed5293f25feac103bf22926115bc9da724b14b941289b13569d7e8feb703
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: 8f257c94e93b146b09ae593cf7141117ff38cd8e9094ea61e8f8bcd2bbc58dc5
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: 4bf558ba1f265602dd32ad83e1f4d323a764fc652ad6bb3927b15a2d24d183f5

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
- created_at_utc: 2026-06-03T08:20:48.803314+00:00
- generated_at_utc: 2026-06-03T08:20:48.803314+00:00
- git_commit: aa491ee633247aaf5773ae46bc510cd4cca67f58
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
