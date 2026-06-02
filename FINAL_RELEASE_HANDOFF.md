# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: 6e527d65157908e0cfc72a4d059bdc70540da01e01c3d10a9d1f89fe89d2ea21

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: caad9d069b0734343d5b00b0a6930458b3a772c078aa0b9d93ded09a2f7f26b6
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: 1f86c5519a0bd22765e715f6604c0c45da47504601f73c674c8b5e942e84d236
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: 63ba2906bf1f62c1942683e7dcf8b7301cd09c76b505db8c715ba6445c4d7331

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
- created_at_utc: 2026-06-02T04:55:43.928641+00:00
- generated_at_utc: 2026-06-02T04:55:43.928641+00:00
- git_commit: 215b7932089cb13bb207934bf2e8662420146831
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
