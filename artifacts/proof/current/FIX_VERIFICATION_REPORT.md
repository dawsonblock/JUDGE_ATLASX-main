# FIX_VERIFICATION_REPORT

- generated_at_utc: 2026-05-31T23:38:06.992298+00:00
- commit_hash: 6a5fd6d4830ac85d675ffd70c38dfef047bca4bd
- alpha_gate_passed: false

## Required Gate Signals

- backend_compile: PASS
- backend_import: PASS
- backend_pytest: FAIL
- verify_evidence_store: PASS
- verify_audit_chain: PASS
- public_api_boundary: PASS
- frontend_node_gate: PASS
- frontend_contracts: PASS
- archive_validation: FAIL
- proof_freshness: PASS

## Release Blockers

- backend_pytest
- docker_runtime_preflight
- docker_smoke
- postgis_proof
- archive_validation
- required_proof_logs
- validation_summary_missing

## Canonical Artifacts

- artifacts/proof/current/release_gate.json
- artifacts/proof/current/proof_manifest.json
- artifacts/proof/current/CURRENT_PROOF.md
- artifacts/proof/current/CURRENT_ALPHA_STATUS.md
- artifacts/proof/current/REPAIR_REPORT.md
