# RELEASE_READINESS

- generated_at_utc: 2026-06-01T20:44:55.976113+00:00
- overall_status: blocked
- production_ready: false
- release_recommendation: blocked
- archive_hash: eae0e122efe16d716bf3764bd1ba217b5d850e9e
- platform: macOS-26.2-arm64-arm-64bit
- python_version: 3.11.9
- node_version: v22.22.3
- npm_version: 10.9.8

## Required Proof Gates

| gate | status | exit_code | log | sha256 |
|---|---|---:|---|---|
| check_no_pyc | PASS | 0 | artifacts/proof/current/check_no_pyc.log | a846f2e3cfab43e1b94af70247e6dff79ec62b983961a207185d87595b1b7ff6 |
| check_false_claims | FAIL | 1 | artifacts/proof/current/check_false_claims.log | 6657692ef99f5b5c9be5988947c64ecfac5f80b8c7009dff026ef2096695e9e5 |
| check_source_keys | PASS | 0 | artifacts/proof/current/check_source_keys.log | 5a19cc9f9747d78ac73bb6e54323386b8a32b69079e204630f249748b6ffb39c |
| check_statuses | PASS | 0 | artifacts/proof/current/check_statuses.log | c5a1e374a12383ff2f924e70bd72bb2ba7210c803d1bba658765034a41a5b256 |
| check_no_direct_ingestion_network_clients | PASS | 0 | artifacts/proof/current/check_no_direct_ingestion_network_clients.log | ab01be057c4e3b265f8f9cc13a4ab4a145abca00913b61d7adf7116dbb1dca58 |
| check_external_boundaries | PASS | 0 | artifacts/proof/current/check_external_boundaries.log | da039530a33bf730b0cc264637a3196b2212a42c42e24f50edcb6f1090c41b62 |
| check_dockerfile_copy_paths | PASS | 0 | artifacts/proof/current/check_dockerfile_copy_paths.log | 560dda5ee402fd885f1bb99fe0459cf155bf2b0bc3f986d3ae32c89890628179 |
| check_compose_auth_defaults | PASS | 0 | artifacts/proof/current/check_compose_auth_defaults.log | ce53c858a818dccbbd3685948e8ce1414dddb23714d77e259787b0ce79eceac9 |
| backend_compile | PASS | 0 | artifacts/proof/current/backend_compile.log | ff048fbcb05f4b23e858a813501477214166d826b765b8ca1f6bba526c2b6e9c |
| backend_import | PASS | 0 | artifacts/proof/current/backend_import.log | ef52f5f83bdd965c041c65e22c0119895113e37a9faf0f73842e4ad73fbec2db |
| backend_pytest_collect | PASS | 0 | artifacts/proof/current/backend_pytest_collect.log | 3dcc3a4a892637e437fd103cd9d633815d6d0b75d5f6c1e6ed1a03f3432e77a6 |
| runtime_smoke | PASS | 0 | artifacts/proof/current/runtime_smoke.log | 561261d657b5b6b5bd99f9db4f716948b8a6188d16238c6259018c5ac421a7f3 |
| backend_pytest | FAIL | 1 | artifacts/proof/current/backend_pytest.log | 42e411dcd14518483f6b4307ddc4b5ee534b26d1692b1e507bd628cd08ee847a |
| check_migrations | PASS | 0 | artifacts/proof/current/check_migrations.log | b1a31ef1e482457fd1c47ac213cc98d199e78f8051acc81264a305cf629b66bf |
| docker_runtime_preflight | PASS | 0 | artifacts/proof/current/docker_runtime_preflight.log | c19c3316f8f5e048d452c3379fa6d90822f99eb6c6fcc29d35b077c7e2deb6cb |
| docker_smoke | PASS | 0 | artifacts/proof/current/docker_smoke.log | e6feb328d72d88084804a9167e941191526ece715a7bdf855794dd1a92f74a4f |
| postgis_proof | PASS | 0 | artifacts/proof/current/postgis_proof.log | 6a76ff488d3122d12bac5967fc87ff341e8ef960e8bd917c84686bb3c5440a62 |
| egress_proxy_proof | PASS | 0 | artifacts/proof/current/egress_proxy_proof.log | 3615bb9c70a44af2380c2bc7f39f08ec7babcb4746202fb1ca1c4f5f540706ec |
| demo_proof | PASS | 0 | artifacts/proof/current/demo_proof.log | 5de510ce42797df8e127acf38025711918f2b55854ecaf8f51d8c3d81e29026e |
| validate_sources | PASS | 0 | artifacts/proof/current/validate_sources.log | 4d734d90bf04c25a04d4752d5067c94dc51e963876cfc4f61bbf698de63c27ba |
| check_yaml_duplicate_keys | PASS | 0 | artifacts/proof/current/check_yaml_duplicate_keys.log | 88b52b46f87e415fc01b849aececd79f567ac8ea21f09f1d891a37eca7ddb06d |
| verify_source_registry | PASS | 0 | artifacts/proof/current/verify_source_registry.log | 11297ffd0a4c075cb44887ff11f56d212e109033e10d614a4def1eab46ac01b6 |
| source_registry_status | PASS | 0 | artifacts/proof/current/source_registry_status.log | a627028cae8dc77fd1985e05a14c9eb33197aebcd2791d1824866799fe8c86be |
| check_source_registry_docs | PASS | 0 | artifacts/proof/current/check_source_registry_docs.log | fe1b62e3c0b1bc448549dfe49a124455c9c01b1813f6d4e8effac96e238d35fe |
| prepare_proof_db | PASS | 0 | artifacts/proof/current/prepare_proof_db.log | ef6779db88eeffa32551cb68ca12147f76837d1ef139b9e8d67f668940f260d5 |
| verify_evidence_store | PASS | 0 | artifacts/proof/current/verify_evidence_store.log | 7b693f37394b451d76dd236d9668d34a5e48b67f48dee151954763083deca20f |
| verify_audit_chain | PASS | 0 | artifacts/proof/current/verify_audit_chain.log | fe19f8f6c84b7afc5d25589151b9a62d89728ad6db4a84cfb0cba5057cf8aa60 |
| auth_mutation_route_coverage | PASS | 0 | artifacts/proof/current/auth_mutation_route_coverage.log | 47c07a827704662c4ff8e9e6624363cb35e7c6d6fccd89e15251a30d2b83770e |
| mutation_fail_closed_coverage | PASS | 0 | artifacts/proof/current/mutation_fail_closed_coverage.log | d14f61a853f5d4f2b49932e04bc819a452c3d94029788fe69c2a6cdeb8ed377b |
| check_node_policy | PASS | 0 | artifacts/proof/current/check_node_policy.log | 5a8b2cacbf3c1df63dc8cd6f8a7d3e1769e0683212fc3442cefff374232c5c32 |
| frontend_node_gate | PASS | 0 | artifacts/proof/current/frontend_node_gate.log | 39dc95fbc807439ae0edd07db104299b2a68d401fefe617df96cb835e3585dc9 |
| frontend_install | PASS | 0 | artifacts/proof/current/frontend_install.log | e2519a2eacef2d0e8c4199feca15b029da183408760014cadfd121e6d32e0121 |
| frontend_lint | PASS | 0 | artifacts/proof/current/frontend_lint.log | 9d79910829d5abcf1161f85f3d57cc9c745d1edd5734a88fee634c9913b368e8 |
| frontend_typecheck | PASS | 0 | artifacts/proof/current/frontend_typecheck.log | 701338e1389ab6284419cba533b353099f6b47658b930e128a8627a7a2d6d6e7 |
| frontend_contracts | PASS | 0 | artifacts/proof/current/frontend_contracts.log | a708c183da4738d8e27182aad84226a5c6e3849611ccb8ea3f9de656f7e7c13e |
| frontend_build | PASS | 0 | artifacts/proof/current/frontend_build.log | f5c0fd9e7b5105d1d4b9366169b4026967eb4b0ffee1343822ef7be2c71cd4ea |
| check_api_contracts | PASS | 0 | artifacts/proof/current/check_api_contracts.log | f6750f8d64797a660c9122c245fa0ae38eb689dd8023b7fef1d0481e4ab86216 |
| frontend_backend_route_contract | PASS | 0 | artifacts/proof/current/frontend_backend_route_contract.log | f3563209ec0dcbcbf599836f73236926eee160235914e0fe0e660e945c9042a0 |
| repo_generated_files | PASS | 0 | artifacts/proof/current/repo_generated_files.log | 1f136c767a6ec6bd6d527af249dd34271e19a2e1287eedd33fd8364bb9384137 |
| check_npm_audit_triage | FAIL | 1 | artifacts/proof/current/check_npm_audit_triage.log | 3142fc7b82c65f235e5190f3be3d6a7d04ad4b00c26280a264a5ce714f8671fe |
| map_route_check | PASS | 0 | artifacts/proof/current/map_route_check.log | 3f2c0fb18144134952224494bc6690cde35213914ff5880a8eed0b5ca519e30f |
| public_api_boundary | PASS | 0 | artifacts/proof/current/public_api_boundary.log | 191c0c172a977523c62ec2c1f8b06cc1a5f60e87feb9859437f2f68cebb8ce94 |
| canlii_staging_proof | PASS | 0 | artifacts/proof/current/canlii_staging_proof.log | d7c9393bb589559678b644f26519944ef1a69f81a771fdbd5fce0282bb665ab5 |
| proof_freshness | PASS | 0 | artifacts/proof/current/proof_freshness.log | 319ced60ef85de090a4cacfdec28e6d7b336bf53bb7ec9e53fb11c1086334f10 |
| single_proof_authority | PASS | 0 | artifacts/proof/current/single_proof_authority.log | 67de9d9d555d8a633cccb3b3fd168f55f5975ed306de95965f06666949cc4337 |
| release_readiness_generation | PASS | 0 | artifacts/proof/current/release_readiness.md | aaebbb1aae03601c190bffb0a7a6a9d002211c9ef1a375bddc8d798de3a234ac |
| proof_consistency_pytest | PASS | 0 | artifacts/proof/current/proof_consistency_pytest.log | e229541b306ca52d9ecce9c536c76cbe3da08c272aa8fdd2458d6f31a93e9481 |
| archive_validation | FAIL | 1 | artifacts/proof/current/archive_validation.log | 19afadb38cd0423f6927ddc3e9273d6387ba9875a962bd16ad583fdbe1eaef46 |
| required_proof_logs | FAIL | 1 | artifacts/proof/current/required_proof_logs.log | 5ab5411ea631c2ce8ce7f98b97458347453b87736d0a26b90136c5d934c892ec |
| check_proof_manifest | PASS | 0 | artifacts/proof/current/check_proof_manifest.log | 9229412b512b5a5ddf278981244fefd8c97bf1ac0cd997b58a67b222635e06ab |
| check_no_local_paths_in_release_proof | PASS | 0 | artifacts/proof/current/check_no_local_paths_in_release_proof.log | 7ab4d071c63ecc123622b94a78dda4a32381a788cc2f318f840fe2f9e799c8e4 |
| check_proof_consistency | PASS | 0 | artifacts/proof/current/check_proof_consistency.log | 0a6ed516987c56172c896b5e5e4bae178cd6f9a2b53df2aa17bb118215f63a28 |
| release_gate | PASS | 0 | artifacts/proof/current/release_gate.log | 188e223d9c6e6e29fdcafa5417b56ea3a582da22b9afe00b4eaf7a5c25ba105a |

## Optional Proof Gates

| gate | status | exit_code | log | sha256 |
|---|---|---:|---|---|
| static_guards | PASS | 0 | artifacts/proof/current/static_guards.log | fac94f545e0f6047a2bf1551c45ff8be19e08d822e34a3e3507df5093ed3a624 |

## Remaining Blockers

- check_false_claims
- backend_pytest
- check_npm_audit_triage
- archive_validation
- required_proof_logs
- validation_summary_missing

## Stale Or Misreported Claims

- readiness is blocked due to failed/missing required proof evidence

## Next Repair Action

- Resolve any required failed gate and rerun scripts/release_gate.py.
