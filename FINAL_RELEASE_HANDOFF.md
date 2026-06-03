# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: ca1fb76597f435ef9bdbc7ba9763b4ce5e93263d89b4d359d488d5bbc492c138

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: 72b03e7fde90d00026bd323076cc82034c92bcbde645dce4f2b79b5b7f1bf7d7
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: 0515811ad23b6a8a085a813f151465b2ae8daa0ab0eca9ba708c9d9e8e6688b6
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: ee78e782256c639781b53d86c98f6dce6eb074af8b02ef9664cf8c0793ec09ff

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
- created_at_utc: 2026-06-03T04:19:05.449755+00:00
- generated_at_utc: 2026-06-03T04:19:05.449755+00:00
- git_commit: 13c503bd375cef49a64b0536133f7b302a6d8f02
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
