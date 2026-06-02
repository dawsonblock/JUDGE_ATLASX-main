# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: 00bc68af0277abbbebaf4c6643cc5e8b18394260fafabfe79aaeb846afe68cc1

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: c5a1c98866709951c3de8fa7fe481717032d7287add8ab61714fb5f12ab58247
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: 117b590764cb65ce77218c45b77a0f6acb4c3487cc3dac47774c6a90d5f43ab1
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: fbf99eeb0bfa12a727b4edb9ec6cda3c1f77912099d5a2f486361e24c08044e7

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
- created_at_utc: 2026-06-02T21:49:14.728010+00:00
- generated_at_utc: 2026-06-02T21:49:14.728010+00:00
- git_commit: dc3b80d8fbd4902097d51b03f4c6c443d5533d72
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
