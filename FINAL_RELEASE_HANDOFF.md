# Final Release Handoff

This document is generated from the built archive and
canonical proof artifacts.
Manual edits are not authoritative.

## Authoritative Archive
- Path: dist/JUDGE_ATLAS-main-final.zip
- SHA-256: 92c1526313ca41373df4bb07c485f378c1b45c1ca0a3e453b07acf52aa20d691
- Internal Root: JUDGE_ATLAS-main/
- Size: 2.6M

## Archive Contents Verified
- 1405 files
- 0 forbidden files
- All required proof artifacts present
- No .env.example files
- No local path leaks
- No __MACOSX or ._* files

## Release Status
- release_classification: self-verifying alpha
- alpha_candidate: true
- self_verifying_alpha: true
- production_release_candidate: false
- production_ready: false
- public_release_safe: false
- proof_complete: true
- blocked_release_checks: []

## Proof Artifacts Included
- artifacts/proof/current/release_gate.json
- artifacts/proof/current/proof_manifest.json
- artifacts/proof/current/required_log_index.json
- artifacts/proof/current/release_readiness.md
- artifacts/proof/current/REPAIR_REPORT.md
- artifacts/proof/current/release_gate.log
- artifacts/proof/current/backend_pytest.log
- artifacts/proof/current/backend_pytest.xml
- artifacts/proof/current/frontend_build.log
- artifacts/proof/current/frontend_route_smoke.log
- artifacts/proof/current/docker_runtime_preflight.log
- artifacts/proof/current/docker_smoke.log
- artifacts/proof/current/runtime_smoke.log
- artifacts/proof/current/source_registry_status.json
- artifacts/proof/current/source_registry_proof_pytest.log

## Build Metadata
- created_at_utc: 2026-06-05T22:09:00Z
- generated_at_utc: 2026-06-05T22:09:00Z
- platform: macOS arm64
- python: 3.11.9
- node: v25.9.0
- npm: 11.12.1

## Upload Instructions
- Only upload: dist/JUDGE_ATLAS-main-final.zip
- Do NOT upload manually compressed folders
- Do NOT upload GitHub exports
- Validate archive with:
  - python3 scripts/validate_final_zip.py dist/JUDGE_ATLAS-main-final.zip
  - python3 scripts/check_release_surface.py --archive dist/JUDGE_ATLAS-main-final.zip
  - python3 scripts/check_proof_manifest.py --archive dist/JUDGE_ATLAS-main-final.zip
  - python3 scripts/verify_archive_proof_freshness.py --archive dist/JUDGE_ATLAS-main-final.zip
  - python3 scripts/cleanroom_release_test.py --archive dist/JUDGE_ATLAS-main-final.zip
  - python3 scripts/check_release_handoff_consistency.py --root . --archive dist/JUDGE_ATLAS-main-final.zip

## Notes
- This is a self-verifying alpha release.
- It is not ready for production deployment.
- The archive is ready for validation by cleanroom tests.
- Do not attempt production deployment until cleanroom tests pass.

