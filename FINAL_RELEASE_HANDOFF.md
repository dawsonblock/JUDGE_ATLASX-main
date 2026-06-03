# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: 0db27a29695e6d3a9b36e530ffb9b06db714f6c5c142073f642c0013bda7ea87

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: b0a7996fb963158ef19a64567b7ea576136fdf928a313d3f47410f5a3f1f76e8
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: e8e9acb25d0687ab23d20769770a81d086beacc74cbcbcad17c4c91603804b3a
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: 40f579cc2b664c57de1bd0cf8cd5afde5672774db81a07b3a30402a10bd3f7ea

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
- created_at_utc: 2026-06-02T23:47:43.452017+00:00
- generated_at_utc: 2026-06-02T23:47:43.452017+00:00
- git_commit: 6dc750a786099ea62d30aa89bd8f8e37e76a1c53
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
