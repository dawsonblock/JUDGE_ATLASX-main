# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: 06295528eb7baeb3a60d0e4a26ac535fc96c2544d4468cc2fd2478e81bf04c9a

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: b6c968beead18decc822c2ca0b343075e772796c50897bf16f322a14a6a66936
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: 093e937196ba56bb26f51cb654e82ad00bf155239797d2fd8adb4757af95ec4c
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: cc1c116c18158718d01526752e1bdfcfc64e262a48039b40cab9c6870723bf42

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
- created_at_utc: 2026-06-02T01:01:27.698679+00:00
- generated_at_utc: 2026-06-02T01:01:27.698679+00:00
- git_commit: unknown
- python: unknown
- node: unknown
- npm: unknown

## Notes
- This is a self-verifying alpha.
- It is not ready for production deployment.
- Ship only the archive listed above.
- Validation must run against a fresh extraction
  of that archive.
- `release_gate.json` is only valid as a proof artifact when every
  log path it references exists inside `artifacts/proof/current/`
  at packaging time. Do not ship manually zipped working trees.
