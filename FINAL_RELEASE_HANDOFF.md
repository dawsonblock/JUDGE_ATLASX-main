# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: 258a9d4afccf6a5f4f3f1308ff3233302dedda6d46d8da7b7579c2cec15f48c3

## Proof Anchors
- release_gate_path: artifacts/proof/current/release_gate.json
- release_gate_sha256: b23787909bc51619ad955c5889d2af5a99b248c9454dc4a5b9068ee619631316
- proof_manifest_path: artifacts/proof/current/proof_manifest.json
- proof_manifest_sha256: c7ea9717504b81e6c57db3a8b60fa1f4b57dc157bfbfd798e1553e94c2010f06
- required_log_index_path: artifacts/proof/current/required_log_index.json
- required_log_index_sha256: 577aed376bb6b3389178fdc6d96f6f38444513a63cce7282a7cd4228fffd3d28

## Release Status
- release_classification: proof-blocked alpha proof snapshot
- alpha_gate_passed: false
- release_candidate: false
- production_ready: false
- proof_complete: false
- blocked_release_checks:
  - backend_pytest (2 test failures: infrastructure tests)
  - docker_runtime_preflight (Docker daemon unavailable on this machine)
  - docker_smoke (Docker daemon unavailable)
  - postgis_proof (PostGIS not available)

## Build Metadata
- created_at_utc: 2026-05-31T23:41:00.000000+00:00
- generated_at_utc: 2026-05-31T23:41:00.000000+00:00
- git_commit: unknown
- python: 3.11.9
- node: v22.22.3
- npm: 10.9.8

## Notes
- This is a proof-blocked alpha proof snapshot, NOT a release candidate.
- Docker daemon is unavailable on this machine; Docker-related gates are honestly marked as blocked.
- Backend tests: 3482/3484 pass; 2 remaining failures are infrastructure tests (not functional).
- It is not ready for production deployment.
- Ship only the archive listed above.
- Validation must run against a fresh extraction of that archive.
- `release_gate.json` is only valid as a proof artifact when every log path it references exists inside `artifacts/proof/current/` at packaging time. Do not ship manually zipped working trees.
