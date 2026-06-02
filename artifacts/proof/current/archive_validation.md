# Archive Validation

- validated_at_utc: 2026-06-02T21:50:32.353030+00:00
- archive: dist/JUDGE_ATLAS-main-final.zip
- archive_sha256: 00bc68af0277abbbebaf4c6643cc5e8b18394260fafabfe79aaeb846afe68cc1
- expected_root: JUDGE_ATLAS-main
- actual_root: JUDGE_ATLAS-main
- top_level_roots: JUDGE_ATLAS-main
- root_match: yes
- valid: PASS
- compressed_size_bytes: 2176929
- uncompressed_size_bytes: 8514449

## Errors

- none

## Warnings

- release_gate_not_release_candidate

## Largest Files

| path | uncompressed | compressed |
|---|---:|---:|
| JUDGE_ATLAS-main/backend/uv.lock | 769811 | 238625 |
| JUDGE_ATLAS-main/frontend/package-lock.json | 393441 | 85051 |
| JUDGE_ATLAS-main/artifacts/proof/current/backend_pytest_collect.log | 322493 | 45744 |
| JUDGE_ATLAS-main/scripts/release_gate.py | 126713 | 23513 |
| JUDGE_ATLAS-main/backend/app/models/entities.py | 101799 | 16701 |
| JUDGE_ATLAS-main/artifacts/proof/current/release_gate.json | 95859 | 14099 |
| JUDGE_ATLAS-main/artifacts/proof/current/proof_manifest.json | 55920 | 7583 |
| JUDGE_ATLAS-main/backend/app/memory/contradiction_engine.py | 48640 | 8977 |
| JUDGE_ATLAS-main/backend/app/ingestion/sources/canada_saskatchewan_sources.yaml | 48453 | 6929 |
| JUDGE_ATLAS-main/artifacts/proof/current/docker_smoke.log | 48363 | 9201 |
| JUDGE_ATLAS-main/backend/app/api/routes/admin_sources.py | 46092 | 9260 |
| JUDGE_ATLAS-main/backend/app/tests/test_api.py | 43536 | 7488 |
| JUDGE_ATLAS-main/backend/app/tests/test_admin_ingestion.py | 38695 | 5870 |
| JUDGE_ATLAS-main/backend/app/tests/test_ingestion_runtime.py | 38018 | 5725 |
| JUDGE_ATLAS-main/backend/app/tests/test_phase5_adaptive_retry.py | 35181 | 4174 |
| JUDGE_ATLAS-main/scripts/build_release_archive.py | 34758 | 7083 |
| JUDGE_ATLAS-main/backend/app/tests/test_ai_reasoning.py | 30318 | 4943 |
| JUDGE_ATLAS-main/scripts/check_proof_consistency.py | 30315 | 5929 |
| JUDGE_ATLAS-main/backend/app/ingestion/courtlistener_bulk_normalizer.py | 29758 | 5588 |
| JUDGE_ATLAS-main/scripts/validate_release_archive.py | 28274 | 5888 |

## Largest Top-Level Directories

| path | uncompressed |
|---|---:|
| backend | 5570207 |
| scripts | 895964 |
| frontend | 873785 |
| artifacts | 678118 |
| docs | 357059 |
| .github | 50671 |
| demo | 26537 |
| infra | 17264 |
| Makefile | 12154 |
| REPO_REALITY.md | 8240 |
| STUBS_AND_PLACEHOLDERS.md | 4768 |
| STATUS.md | 3470 |
| PROOF_STATUS.md | 2972 |
| README.md | 2827 |
| CURRENT_STATUS.md | 2785 |
| docker-compose.yml | 2518 |
| RELEASE_BLOCKERS.md | 2410 |
| RELEASE_MANIFEST.json | 1421 |
| Dockerfile.proof | 890 |
| deploy | 389 |
