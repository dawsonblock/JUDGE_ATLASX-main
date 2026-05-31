# RELEASE_READINESS

- generated_at_utc: 2026-05-31T23:31:49.212063+00:00
- overall_status: blocked
- production_ready: false
- release_recommendation: blocked
- archive_hash: ceb8b7e7d5417d896edc91dd87aef645d2854bca
- platform: macOS-26.2-arm64-arm-64bit
- python_version: 3.11.9
- node_version: v22.22.3
- npm_version: 10.9.8

## Required Proof Gates

| gate | status | exit_code | log | sha256 |
|---|---|---:|---|---|
| check_no_pyc | PASS | 0 | artifacts/proof/current/check_no_pyc.log | a846f2e3cfab43e1b94af70247e6dff79ec62b983961a207185d87595b1b7ff6 |
| check_false_claims | PASS | 0 | artifacts/proof/current/check_false_claims.log | 8c882684eaade150d76d26e289c110f776b307c04d132c6aa33949aff87c7bc1 |
| check_source_keys | PASS | 0 | artifacts/proof/current/check_source_keys.log | 5a19cc9f9747d78ac73bb6e54323386b8a32b69079e204630f249748b6ffb39c |
| check_statuses | PASS | 0 | artifacts/proof/current/check_statuses.log | c5a1e374a12383ff2f924e70bd72bb2ba7210c803d1bba658765034a41a5b256 |
| check_no_direct_ingestion_network_clients | PASS | 0 | artifacts/proof/current/check_no_direct_ingestion_network_clients.log | ab01be057c4e3b265f8f9cc13a4ab4a145abca00913b61d7adf7116dbb1dca58 |
| check_external_boundaries | PASS | 0 | artifacts/proof/current/check_external_boundaries.log | da039530a33bf730b0cc264637a3196b2212a42c42e24f50edcb6f1090c41b62 |
| check_dockerfile_copy_paths | PASS | 0 | artifacts/proof/current/check_dockerfile_copy_paths.log | 9cb5347afde90057ddc1a4fdcecd6ae1318290990ddadf2f5dfaeebf1e92eb2a |
| check_compose_auth_defaults | PASS | 0 | artifacts/proof/current/check_compose_auth_defaults.log | ce53c858a818dccbbd3685948e8ce1414dddb23714d77e259787b0ce79eceac9 |
| backend_compile | PASS | 0 | artifacts/proof/current/backend_compile.log | ff048fbcb05f4b23e858a813501477214166d826b765b8ca1f6bba526c2b6e9c |
| backend_import | PASS | 0 | artifacts/proof/current/backend_import.log | ef52f5f83bdd965c041c65e22c0119895113e37a9faf0f73842e4ad73fbec2db |
| backend_pytest_collect | PASS | 0 | artifacts/proof/current/backend_pytest_collect.log | ad413e4141b5d10aaeb5cfea4e851c6ea0a74e10109ef34ecfabe723a02c625a |
| runtime_smoke | PASS | 0 | artifacts/proof/current/runtime_smoke.log | 561261d657b5b6b5bd99f9db4f716948b8a6188d16238c6259018c5ac421a7f3 |
| backend_pytest | FAIL | 1 | artifacts/proof/current/backend_pytest.log | c10f4f0158a8e2363e65049d57d887ca19a3a42441d55beb8b8a484078b4743e |
| check_migrations | PASS | 0 | artifacts/proof/current/check_migrations.log | b1a31ef1e482457fd1c47ac213cc98d199e78f8051acc81264a305cf629b66bf |
| docker_runtime_preflight | FAIL | 1 | artifacts/proof/current/docker_runtime_preflight.log | 0a733fe45929bf8c174beafea11cc59e37bfef5d5ecd085e27bc0a4caa1cb0bb |
| docker_smoke | BLOCKED | 1 | artifacts/proof/current/docker_smoke.log | c6593ad24f69d3c07a62c0aa26fba3a8e0b9cc02d0fde1d040db17258fd57c2c |
| postgis_proof | BLOCKED | 1 | artifacts/proof/current/postgis_proof.log | 161e3405df71182f2be5bc8d5b88e4558cb8779029700e68c4a76192e027b0c8 |
| egress_proxy_proof | PASS | 0 | artifacts/proof/current/egress_proxy_proof.log | fa81a1dc278abd11ccc85fa2604213ce4bf6b7dca837241f9b5b8c7954e0c308 |
| demo_proof | PASS | 0 | artifacts/proof/current/demo_proof.log | 5de510ce42797df8e127acf38025711918f2b55854ecaf8f51d8c3d81e29026e |
| validate_sources | PASS | 0 | artifacts/proof/current/validate_sources.log | 4d734d90bf04c25a04d4752d5067c94dc51e963876cfc4f61bbf698de63c27ba |
| check_yaml_duplicate_keys | PASS | 0 | artifacts/proof/current/check_yaml_duplicate_keys.log | 88b52b46f87e415fc01b849aececd79f567ac8ea21f09f1d891a37eca7ddb06d |
| verify_source_registry | PASS | 0 | artifacts/proof/current/verify_source_registry.log | 74083aa390ad8adafaa9b6a693573797e4b80cbaf5e926c8cceb8ef355157ca2 |
| source_registry_status | PASS | 0 | artifacts/proof/current/source_registry_status.log | a627028cae8dc77fd1985e05a14c9eb33197aebcd2791d1824866799fe8c86be |
| check_source_registry_docs | PASS | 0 | artifacts/proof/current/check_source_registry_docs.log | fe1b62e3c0b1bc448549dfe49a124455c9c01b1813f6d4e8effac96e238d35fe |
| prepare_proof_db | PASS | 0 | artifacts/proof/current/prepare_proof_db.log | ef6779db88eeffa32551cb68ca12147f76837d1ef139b9e8d67f668940f260d5 |
| verify_evidence_store | PASS | 0 | artifacts/proof/current/verify_evidence_store.log | 7b693f37394b451d76dd236d9668d34a5e48b67f48dee151954763083deca20f |
| verify_audit_chain | PASS | 0 | artifacts/proof/current/verify_audit_chain.log | 0137f8f111298ac7460cd4b4a4b4bdcd099150b488081f86b626a00b22749a2c |
| auth_mutation_route_coverage | PASS | 0 | artifacts/proof/current/auth_mutation_route_coverage.log | 2a7d251874f6b6cfb13fff84ae694c0637e665e4a6f687e4a389d2364b3f9915 |
| mutation_fail_closed_coverage | PASS | 0 | artifacts/proof/current/mutation_fail_closed_coverage.log | 7d9bc4d71748472d398f8b60c4db2744f076fe3e513de51af7d1c0fc90101a56 |
| check_node_policy | PASS | 0 | artifacts/proof/current/check_node_policy.log | 5a8b2cacbf3c1df63dc8cd6f8a7d3e1769e0683212fc3442cefff374232c5c32 |
| frontend_node_gate | PASS | 0 | artifacts/proof/current/frontend_node_gate.log | 39dc95fbc807439ae0edd07db104299b2a68d401fefe617df96cb835e3585dc9 |
| frontend_install | PASS | 0 | artifacts/proof/current/frontend_install.log | 0e127fb272d8bdba2ce1185aece6e40b108ce9e355a124dd147c459301c5cfce |
| frontend_lint | PASS | 0 | artifacts/proof/current/frontend_lint.log | 9d79910829d5abcf1161f85f3d57cc9c745d1edd5734a88fee634c9913b368e8 |
| frontend_typecheck | PASS | 0 | artifacts/proof/current/frontend_typecheck.log | 701338e1389ab6284419cba533b353099f6b47658b930e128a8627a7a2d6d6e7 |
| frontend_contracts | PASS | 0 | artifacts/proof/current/frontend_contracts.log | 73b6d1d5f31f096e0b8a4c115ee9819ebd9f2d5a83b07fdea60037a06f0eb512 |
| frontend_build | PASS | 0 | artifacts/proof/current/frontend_build.log | f5c0fd9e7b5105d1d4b9366169b4026967eb4b0ffee1343822ef7be2c71cd4ea |
| check_api_contracts | PASS | 0 | artifacts/proof/current/check_api_contracts.log | f6750f8d64797a660c9122c245fa0ae38eb689dd8023b7fef1d0481e4ab86216 |
| frontend_backend_route_contract | PASS | 0 | artifacts/proof/current/frontend_backend_route_contract.log | f3563209ec0dcbcbf599836f73236926eee160235914e0fe0e660e945c9042a0 |
| repo_generated_files | PASS | 0 | artifacts/proof/current/repo_generated_files.log | 1f136c767a6ec6bd6d527af249dd34271e19a2e1287eedd33fd8364bb9384137 |
| check_npm_audit_triage | PASS | 0 | artifacts/proof/current/check_npm_audit_triage.log | c9bab79018cc60539b4fa5a6d6b6e291f3138327e6689b409cb60d8087b54092 |
| map_route_check | PASS | 0 | artifacts/proof/current/map_route_check.log | 3f2c0fb18144134952224494bc6690cde35213914ff5880a8eed0b5ca519e30f |
| public_api_boundary | PASS | 0 | artifacts/proof/current/public_api_boundary.log | 9a65c4696b5538d43af073e2a32ac15ff6b5840f4361a14252ede13de3442e41 |
| canlii_staging_proof | PASS | 0 | artifacts/proof/current/canlii_staging_proof.log | d7c9393bb589559678b644f26519944ef1a69f81a771fdbd5fce0282bb665ab5 |
| proof_freshness | PASS | 0 | artifacts/proof/current/proof_freshness.log | 46e130660fd6a93ef498c2e1cdddd68974be4db1567fe15344fd8af46dfe1566 |
| single_proof_authority | PASS | 0 | artifacts/proof/current/single_proof_authority.log | 67de9d9d555d8a633cccb3b3fd168f55f5975ed306de95965f06666949cc4337 |
| release_readiness_generation | PASS | 0 | artifacts/proof/current/release_readiness.md | 65e3c14e6f937b7bfbecf2492b2344fb7cbfa92d0bb7ad38af4b7a5e6e205087 |
| proof_consistency_pytest | PASS | 0 | artifacts/proof/current/proof_consistency_pytest.log | e229541b306ca52d9ecce9c536c76cbe3da08c272aa8fdd2458d6f31a93e9481 |
| archive_validation | FAIL | 1 | artifacts/proof/current/archive_validation.log | 18178aef461f22182320a4ebc05e564dafdc2cf559edc45b15ca56d10a599796 |
| required_proof_logs | FAIL | 1 | artifacts/proof/current/required_proof_logs.log | 91856ce29633b638342aa82457f7b60af6783048ea5b7b4d4d5cebbc0562e4b9 |
| check_proof_manifest | PASS | 0 | artifacts/proof/current/check_proof_manifest.log | 02a5c925c7261eb8bd964a91c6442c19d3346172c9561eeed5476fc616df93d9 |
| check_no_local_paths_in_release_proof | PASS | 0 | artifacts/proof/current/check_no_local_paths_in_release_proof.log | 7ab4d071c63ecc123622b94a78dda4a32381a788cc2f318f840fe2f9e799c8e4 |
| check_proof_consistency | PASS | 0 | artifacts/proof/current/check_proof_consistency.log | 0a6ed516987c56172c896b5e5e4bae178cd6f9a2b53df2aa17bb118215f63a28 |
| release_gate | PASS | 0 | artifacts/proof/current/release_gate.log | eca4614cb1ca1c0aed29edc097cdd4299f95c47638c208cbde168ee9456625c7 |

## Optional Proof Gates

| gate | status | exit_code | log | sha256 |
|---|---|---:|---|---|
| static_guards | PASS | 0 | artifacts/proof/current/static_guards.log | 115a68267999528d3cc712acd354f443bc0db2bd743118066bb8d8f59c01ce65 |

## Remaining Blockers

- backend_pytest
- docker_runtime_preflight
- docker_smoke
- postgis_proof
- archive_validation
- required_proof_logs
- validation_summary_missing

## Stale Or Misreported Claims

- readiness is blocked due to failed/missing required proof evidence

## Next Repair Action

- Resolve any required failed gate and rerun scripts/release_gate.py.
