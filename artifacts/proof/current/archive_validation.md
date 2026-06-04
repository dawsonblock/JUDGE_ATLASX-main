# Archive Validation

- validated_at_utc: 2026-06-04T03:13:51.729153+00:00
- archive: dist/JUDGE_ATLAS-main-final.zip
- archive_sha256: c6ee0138ad467ff670b6c39f436a8549c91709728fc24af3527d2ed921086d4e
- expected_root: JUDGE_ATLAS-main
- actual_root: JUDGE_ATLAS-main
- top_level_roots: JUDGE_ATLAS-main
- root_match: yes
- valid: PASS
- compressed_size_bytes: 2219148
- uncompressed_size_bytes: 8667257

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
| JUDGE_ATLAS-main/artifacts/proof/current/backend_pytest_collect.log | 331169 | 46674 |
| JUDGE_ATLAS-main/scripts/release_gate.py | 128173 | 23713 |
| JUDGE_ATLAS-main/backend/app/models/entities.py | 101799 | 16701 |
| JUDGE_ATLAS-main/artifacts/proof/current/release_gate.json | 99114 | 14565 |
| JUDGE_ATLAS-main/artifacts/proof/current/proof_manifest.json | 59251 | 8034 |
| JUDGE_ATLAS-main/artifacts/proof/current/docker_smoke.log | 48849 | 9303 |
| JUDGE_ATLAS-main/backend/app/memory/contradiction_engine.py | 48640 | 8977 |
| JUDGE_ATLAS-main/backend/app/ingestion/sources/canada_saskatchewan_sources.yaml | 48199 | 6787 |
| JUDGE_ATLAS-main/backend/app/api/routes/admin_sources.py | 46299 | 9283 |
| JUDGE_ATLAS-main/backend/app/tests/test_api.py | 43536 | 7488 |
| JUDGE_ATLAS-main/backend/app/tests/test_admin_ingestion.py | 38695 | 5870 |
| JUDGE_ATLAS-main/backend/app/tests/test_ingestion_runtime.py | 38018 | 5725 |
| JUDGE_ATLAS-main/backend/app/tests/test_phase5_adaptive_retry.py | 35181 | 4174 |
| JUDGE_ATLAS-main/scripts/build_release_archive.py | 34919 | 7164 |
| JUDGE_ATLAS-main/backend/app/tests/test_ai_reasoning.py | 30318 | 4943 |
| JUDGE_ATLAS-main/scripts/check_proof_consistency.py | 30315 | 5929 |
| JUDGE_ATLAS-main/backend/app/ingestion/courtlistener_bulk_normalizer.py | 29758 | 5588 |
| JUDGE_ATLAS-main/artifacts/proof/current/backend_pytest.log | 28861 | 4264 |

## Largest Top-Level Directories

| path | uncompressed |
|---|---:|
| backend | 5615960 |
| scripts | 968798 |
| frontend | 873894 |
| artifacts | 697266 |
| docs | 369096 |
| .github | 50711 |
| demo | 26537 |
| infra | 17264 |
| Makefile | 14518 |
| REPO_REALITY.md | 8240 |
| STUBS_AND_PLACEHOLDERS.md | 4772 |
| STATUS.md | 3471 |
| README.md | 3210 |
| PROOF_STATUS.md | 2976 |
| CURRENT_STATUS.md | 2786 |
| docker-compose.yml | 2518 |
| RELEASE_BLOCKERS.md | 2414 |
| RELEASE_MANIFEST.json | 1547 |
| Dockerfile.proof | 890 |
| deploy | 389 |
