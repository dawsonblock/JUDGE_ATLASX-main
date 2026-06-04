# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: 1045dd84e569ad38859a056a24f9682610763e56ba1ff6e064b78ce6a53492fb

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: d232f9fa730b64b9ca870b00775bff091e7674bfed139715c60a32f16ff47cd4
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: fbec38ec79e48dc6166ab65ae79be188d6d1b0417b3198fe5edded0dfd4b2090
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: afb2316b76682cda45c305d982d418b3a65e89dbd521fb81d4d1367f7bcb9aa6

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
- created_at_utc: 2026-06-04T04:10:21.614456+00:00
- generated_at_utc: 2026-06-04T04:10:21.614456+00:00
- git_commit: 515238070d3870362d4781d50f818933da0b79f7
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
