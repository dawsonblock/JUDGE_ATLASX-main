# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: 486d0b49bab7e9ee44df5055cc4c17bac03a5634fb501a53f5ae4dbc62549bc9

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: ebaad09dd67987bdcc438d2b90d79c9a74b152a4ace6a8a973d9a7bb507303d2
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: 9bf2cb54bb762446cf797d3494ffc60c174bdf64b987d121b0046d978638cb52
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: 2d9ef8c8425b0c318dca246012b810afdc0060a3225b5086ec4b7aee65830ca7

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
- created_at_utc: 2026-06-03T20:01:31.133571+00:00
- generated_at_utc: 2026-06-03T20:01:31.133571+00:00
- git_commit: f9253a4b7585b08c132603b5df9b1aa6a2e8a196
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
