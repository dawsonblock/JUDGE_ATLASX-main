# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: c6ee0138ad467ff670b6c39f436a8549c91709728fc24af3527d2ed921086d4e

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: ad2b809c6b5518ef3bfdd8d9fd70a558dd5987397a03bc07a4be6bbb1df2733c
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: 732b00390f95582c37cbbee3d5c7de148a967885bace8eb16d389f4185b15f2e
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: df3b0231600f80330615e053cb478efc6c88bd36884f3b91362756e4d7833836

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
- created_at_utc: 2026-06-04T03:12:52.581955+00:00
- generated_at_utc: 2026-06-04T03:12:52.581955+00:00
- git_commit: 0eab8c7f016eced49ad0ceb48a3f38fcfda30faa
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
