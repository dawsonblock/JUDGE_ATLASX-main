# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: f3744b2522f37184df9710aff7afe8a4c9f7190076898fadc085d08e89d7a9b9

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: 41e86686aaef387d6ff07e3af3521ccbd5b4444ac62d4221bfcfe99ebfd7cfb3
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: 22f66bbd7da31ab7178c56dc60cf8200a552d16070c1578473dd659e546c7446
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: c399f8341e20d733703b184f3a49669095a5f0186706f56ed92199c028011e2d

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
- created_at_utc: 2026-06-03T02:19:01.267218+00:00
- generated_at_utc: 2026-06-03T02:19:01.267218+00:00
- git_commit: 6d724a0368959d7e7dedb42067250871d12f0046
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
