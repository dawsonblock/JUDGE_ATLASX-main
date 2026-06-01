# FIX_VERIFICATION_REPORT

- generated_at_utc: 2026-06-01T20:44:55.976113+00:00
- commit_hash: eae0e122efe16d716bf3764bd1ba217b5d850e9e
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

- check_false_claims
- backend_pytest
- check_npm_audit_triage
- archive_validation
- required_proof_logs
- validation_summary_missing

## Canonical Artifacts

- artifacts/proof/current/release_gate.json
- artifacts/proof/current/proof_manifest.json
- artifacts/proof/current/CURRENT_PROOF.md
- artifacts/proof/current/CURRENT_ALPHA_STATUS.md
- artifacts/proof/current/REPAIR_REPORT.md
