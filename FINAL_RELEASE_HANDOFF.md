# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: d29044923a46aaae38476127595c08f1be961045ac38a8e6e7cb58fe9706e0fe

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: c91be3ffaa2a83051f6aa7dc6bfc7506bd0bc4227211256a55fd9969e3b408e2
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: 08e22d5e3afd0bd506efd38e47956c1ac83e01c18a24592c24a1319786de733d
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: 20196d97e3d7623574f28f757a116747e5cca161b4e671adacc357bfa44a87dc

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
- created_at_utc: 2026-06-04T08:09:50.350929+00:00
- generated_at_utc: 2026-06-04T08:09:50.350929+00:00
- git_commit: 2f3f99abb08402eb49460b9eb8e70b26998b9dad
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
