# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: 44ea89c6b65ae730e61fa49bb6e8fa6de92b3103f94bc93924e88d37f22df89b

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: 4ed557383d8f4d3698d76e67743d92621484039425f5189edc96eddd5b959bf6
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: e1f50a8167186957750545a36a75f53ac3ea11f3392d5678a9edfbf9d690d4d8
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: e3bbc51c8c50a502e7c01fa78abb778a365189c8b70544f7abbd50f99bcd28af

## Release Status
- release_classification: proof-blocked alpha proof snapshot
- alpha_candidate: false
- self_verifying_alpha: false
- production_release_candidate: false
- production_ready: false
- public_release_safe: false
- proof_complete: false
- blocked_release_checks: ["archive_validation", "check_proof_consistency"]

## Build Metadata
- created_at_utc: 2026-06-04T05:00:30.368264+00:00
- generated_at_utc: 2026-06-04T05:00:30.368264+00:00
- git_commit: f05f8f471467212412d49125a85476b6ad31af7f
- platform: macOS-26.2-arm64-arm-64bit
- python: 3.11.9
- node: v22.22.3
- npm: 10.9.8

## Notes
- This is a proof-blocked alpha proof snapshot.
- It is not ready for production deployment.
- Ship only the archive listed above.
- Validation must run against a fresh extraction
  of that archive.
- `release_gate.json` is only valid as a proof artifact when
  every log path it references exists inside
  `artifacts/proof/current/`
  at packaging time. Do not ship manually zipped working trees.
