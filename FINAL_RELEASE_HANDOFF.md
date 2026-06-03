# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: 71986fe52910688675891d72b309a6c5e1cc135df940dd24042594f56f3bfda9

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: 72514966ccdc0bbe4a5da9c5849a242c2259aefc2d4bfbdb32b083a6024b0c40
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: 3cde3d770d141c0a99a0b35a734b361389dd48bafdd7b0898d0c37fa11815052
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: 701963579b22621f823b81ff162f9f19eac5893b2418bcd03b95e7cf93a6b655

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
- created_at_utc: 2026-06-03T07:51:37.815886+00:00
- generated_at_utc: 2026-06-03T07:51:37.815886+00:00
- git_commit: 243d2cd475f672e3375958d126830b7fb622eb4f
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
