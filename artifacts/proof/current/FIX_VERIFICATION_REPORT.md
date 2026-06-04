# FIX_VERIFICATION_REPORT

- generated_at_utc: 2026-06-04T02:49:54.077015+00:00
- commit_hash: 0eab8c7f016eced49ad0ceb48a3f38fcfda30faa
- alpha_gate_passed: false
- alpha_candidate: false
- self_verifying_alpha: false
- production_release_candidate: false
- production_ready: false
- public_release_safe: false

## Required Gate Signals

- backend_compile: PASS
- backend_import: PASS
- backend_pytest: PASS
- verify_evidence_store: PASS
- verify_audit_chain: PASS
- public_api_boundary: PASS
- frontend_node_gate: PASS
- frontend_contracts: PASS
- archive_validation: FAIL
- proof_freshness: PASS

## Release Blockers

- archive_validation
- check_proof_consistency

## Canonical Artifacts

- artifacts/proof/current/release_gate.json
- artifacts/proof/current/proof_manifest.json
- artifacts/proof/current/CURRENT_PROOF.md
- artifacts/proof/current/CURRENT_ALPHA_STATUS.md
- artifacts/proof/current/REPAIR_REPORT.md
