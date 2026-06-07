# Archive Validation

- validated_at_utc: 2026-06-07T06:20:36.426201+00:00
- archive: dist/JUDGE_ATLAS-main-final.zip
- archive_sha256: e1f713f4d1ff40bc561d00ae32bb3a3a6fa98b9d85649c42b2babe229f05a651
- expected_root: JUDGE_ATLAS-main
- actual_root: JUDGE_ATLAS-main
- top_level_roots: JUDGE_ATLAS-main
- root_match: yes
- valid: PASS
- compressed_size_bytes: 2237366
- uncompressed_size_bytes: 8722068

## Errors

- none

## Warnings

- release_gate_not_alpha_passed
- release_gate_not_release_candidate

## Largest Files

| path | uncompressed | compressed |
|---|---:|---:|
| JUDGE_ATLAS-main/backend/uv.lock | 769811 | 238625 |
| JUDGE_ATLAS-main/frontend/package-lock.json | 393441 | 85051 |
| JUDGE_ATLAS-main/artifacts/proof/current/backend_pytest_collect.log | 333531 | 46953 |
| JUDGE_ATLAS-main/scripts/release_gate.py | 129205 | 23958 |
| JUDGE_ATLAS-main/backend/app/models/entities.py | 101799 | 16701 |
| JUDGE_ATLAS-main/artifacts/proof/current/release_gate.json | 100367 | 14788 |
| JUDGE_ATLAS-main/artifacts/proof/current/proof_manifest.json | 59331 | 8071 |
| JUDGE_ATLAS-main/backend/app/ingestion/sources/canada_saskatchewan_sources.yaml | 50147 | 7012 |
| JUDGE_ATLAS-main/backend/app/memory/contradiction_engine.py | 48640 | 8977 |
| JUDGE_ATLAS-main/backend/app/api/routes/admin_sources.py | 46299 | 9283 |
| JUDGE_ATLAS-main/backend/app/tests/test_api.py | 43536 | 7488 |
| JUDGE_ATLAS-main/backend/app/tests/test_admin_ingestion.py | 38695 | 5870 |
| JUDGE_ATLAS-main/backend/app/tests/test_ingestion_runtime.py | 38018 | 5725 |
| JUDGE_ATLAS-main/backend/app/tests/test_phase5_adaptive_retry.py | 35181 | 4174 |
| JUDGE_ATLAS-main/scripts/build_release_archive.py | 34797 | 7090 |
| JUDGE_ATLAS-main/backend/app/tests/test_ai_reasoning.py | 30318 | 4943 |
| JUDGE_ATLAS-main/scripts/check_proof_consistency.py | 30315 | 5929 |
| JUDGE_ATLAS-main/backend/app/ingestion/courtlistener_bulk_normalizer.py | 29758 | 5588 |
| JUDGE_ATLAS-main/artifacts/proof/current/backend_pytest.log | 28920 | 4289 |
| JUDGE_ATLAS-main/scripts/validate_release_archive.py | 28274 | 5888 |

## Largest Top-Level Directories

| path | uncompressed |
|---|---:|
| backend | 5647374 |
| scripts | 998115 |
| frontend | 873899 |
| artifacts | 672120 |
| docs | 380342 |
| .github | 57766 |
| demo | 26537 |
| infra | 17264 |
| Makefile | 15098 |
| REPO_REALITY.md | 8240 |
| STUBS_AND_PLACEHOLDERS.md | 4772 |
| STATUS.md | 3471 |
| README.md | 3210 |
| PROOF_STATUS.md | 2976 |
| CURRENT_STATUS.md | 2786 |
| docker-compose.yml | 2518 |
| RELEASE_BLOCKERS.md | 2414 |
| RELEASE_MANIFEST.json | 1887 |
| Dockerfile.proof | 890 |
| deploy | 389 |
