# FIX_VERIFICATION_REPORT

- generated_at_utc: 2026-06-07T06:20:13.919225+00:00
- commit_hash: abcd220675f7fb5134519ab88ae303bcab4b70a2
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
- archive_validation: PASS
- proof_freshness: PASS

## Release Blockers

- check_migrations
- docker_runtime_preflight
- docker_smoke
- postgis_proof
- demo_proof
- check_source_registry_docs
- prepare_proof_db
- source_registry_proof_pytest

## Canonical Artifacts

- artifacts/proof/current/release_gate.json
- artifacts/proof/current/proof_manifest.json
- artifacts/proof/current/CURRENT_PROOF.md
- artifacts/proof/current/CURRENT_ALPHA_STATUS.md
- artifacts/proof/current/REPAIR_REPORT.md
