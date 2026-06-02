# RELEASE_READINESS

- generated_at_utc: 2026-06-02T08:27:36.107651+00:00
- overall_status: self-verifying-alpha
- alpha_candidate: true
- self_verifying_alpha: true
- production_release_candidate: false
- production_ready: false
- public_release_safe: false
- release_recommendation: self-verifying-alpha
- archive_hash: 7964167cc38d7b8844adf0d10719de875b774115
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
| check_dockerfile_copy_paths | PASS | 0 | artifacts/proof/current/check_dockerfile_copy_paths.log | 560dda5ee402fd885f1bb99fe0459cf155bf2b0bc3f986d3ae32c89890628179 |
| check_compose_auth_defaults | PASS | 0 | artifacts/proof/current/check_compose_auth_defaults.log | ce53c858a818dccbbd3685948e8ce1414dddb23714d77e259787b0ce79eceac9 |
| backend_compile | PASS | 0 | artifacts/proof/current/backend_compile.log | ff048fbcb05f4b23e858a813501477214166d826b765b8ca1f6bba526c2b6e9c |
| backend_import | PASS | 0 | artifacts/proof/current/backend_import.log | ef52f5f83bdd965c041c65e22c0119895113e37a9faf0f73842e4ad73fbec2db |
| backend_pytest_collect | PASS | 0 | artifacts/proof/current/backend_pytest_collect.log | 6bd3fb5759c784010168a6e07b18a5917d20ed218037eee9050197218f3f9b8f |
| runtime_smoke | PASS | 0 | artifacts/proof/current/runtime_smoke.log | 561261d657b5b6b5bd99f9db4f716948b8a6188d16238c6259018c5ac421a7f3 |
| backend_pytest | PASS | 0 | artifacts/proof/current/backend_pytest.log | c923cd33ec8a12af941022be06ef98b82d4abca4498700fb5a75a7c75ce80e8e |
| check_migrations | PASS | 0 | artifacts/proof/current/check_migrations.log | b1a31ef1e482457fd1c47ac213cc98d199e78f8051acc81264a305cf629b66bf |
| docker_runtime_preflight | PASS | 0 | artifacts/proof/current/docker_runtime_preflight.log | c19c3316f8f5e048d452c3379fa6d90822f99eb6c6fcc29d35b077c7e2deb6cb |
| docker_smoke | PASS | 0 | artifacts/proof/current/docker_smoke.log | 36f08672e58af41a52282d52ba478beec700c3ec897f628f6570ddfa745fc591 |
| postgis_proof | PASS | 0 | artifacts/proof/current/postgis_proof.log | d5f1897b6f7b3b1355e2c9ff60840d7eeb3f9702e118e14609e957054e62b188 |
| egress_proxy_proof | PASS | 0 | artifacts/proof/current/egress_proxy_proof.log | 01c6994b8757197706fd9ec2bced82dc682dec042fe8e1a291eaedbd64b42697 |
| demo_proof | PASS | 0 | artifacts/proof/current/demo_proof.log | 5de510ce42797df8e127acf38025711918f2b55854ecaf8f51d8c3d81e29026e |
| validate_sources | PASS | 0 | artifacts/proof/current/validate_sources.log | 4d734d90bf04c25a04d4752d5067c94dc51e963876cfc4f61bbf698de63c27ba |
| check_yaml_duplicate_keys | PASS | 0 | artifacts/proof/current/check_yaml_duplicate_keys.log | 88b52b46f87e415fc01b849aececd79f567ac8ea21f09f1d891a37eca7ddb06d |
| verify_source_registry | PASS | 0 | artifacts/proof/current/verify_source_registry.log | bff082fdfa1ecb4b5199bf03d5eeddf526672bf075c7bcef589b2ce576aa48b0 |
| source_registry_status | PASS | 0 | artifacts/proof/current/source_registry_status.log | a627028cae8dc77fd1985e05a14c9eb33197aebcd2791d1824866799fe8c86be |
| generate_coverage_matrix | PASS | 0 | artifacts/proof/current/generate_coverage_matrix.log | 3d868e3cbd1d339db9943afaaf81a5a2e3ad66fc852f8f7a5f57ffc063133f23 |
| check_source_registry_docs | PASS | 0 | artifacts/proof/current/check_source_registry_docs.log | fe1b62e3c0b1bc448549dfe49a124455c9c01b1813f6d4e8effac96e238d35fe |
| prepare_proof_db | PASS | 0 | artifacts/proof/current/prepare_proof_db.log | ef6779db88eeffa32551cb68ca12147f76837d1ef139b9e8d67f668940f260d5 |
| verify_evidence_store | PASS | 0 | artifacts/proof/current/verify_evidence_store.log | 7b693f37394b451d76dd236d9668d34a5e48b67f48dee151954763083deca20f |
| verify_audit_chain | PASS | 0 | artifacts/proof/current/verify_audit_chain.log | dd5e1e02185b426b782b59b732d3ea46c355dd70930780d094ee0accaf7a34af |
| auth_mutation_route_coverage | PASS | 0 | artifacts/proof/current/auth_mutation_route_coverage.log | 2a7d251874f6b6cfb13fff84ae694c0637e665e4a6f687e4a389d2364b3f9915 |
| mutation_fail_closed_coverage | PASS | 0 | artifacts/proof/current/mutation_fail_closed_coverage.log | 50109f37efd56aeaacf481752bdd44e351b4101b519ff024c2226c6249e45f32 |
| check_node_policy | PASS | 0 | artifacts/proof/current/check_node_policy.log | 5a8b2cacbf3c1df63dc8cd6f8a7d3e1769e0683212fc3442cefff374232c5c32 |
| frontend_node_gate | PASS | 0 | artifacts/proof/current/frontend_node_gate.log | 39dc95fbc807439ae0edd07db104299b2a68d401fefe617df96cb835e3585dc9 |
| frontend_install | PASS | 0 | artifacts/proof/current/frontend_install.log | 95ce38bc6fb19418e34a252dcfb62941cb51ca3c12dbf606909d211192a97dab |
| frontend_lint | PASS | 0 | artifacts/proof/current/frontend_lint.log | 9d79910829d5abcf1161f85f3d57cc9c745d1edd5734a88fee634c9913b368e8 |
| frontend_typecheck | PASS | 0 | artifacts/proof/current/frontend_typecheck.log | 701338e1389ab6284419cba533b353099f6b47658b930e128a8627a7a2d6d6e7 |
| frontend_contracts | PASS | 0 | artifacts/proof/current/frontend_contracts.log | bbb866522b901c061d4ca0d0b345ff143fa5551032e0343e6461d7524f2a68b0 |
| frontend_build | PASS | 0 | artifacts/proof/current/frontend_build.log | f5c0fd9e7b5105d1d4b9366169b4026967eb4b0ffee1343822ef7be2c71cd4ea |
| check_api_contracts | PASS | 0 | artifacts/proof/current/check_api_contracts.log | f6750f8d64797a660c9122c245fa0ae38eb689dd8023b7fef1d0481e4ab86216 |
| frontend_backend_route_contract | PASS | 0 | artifacts/proof/current/frontend_backend_route_contract.log | f3563209ec0dcbcbf599836f73236926eee160235914e0fe0e660e945c9042a0 |
| frontend_route_smoke | PASS | 0 | artifacts/proof/current/frontend_route_smoke.log | 4afbcaf47374fb181a53b0939ce9ef84d5fde94e2028df8eb9e29b1fe9b322f0 |
| repo_generated_files | PASS | 0 | artifacts/proof/current/repo_generated_files.log | 1f136c767a6ec6bd6d527af249dd34271e19a2e1287eedd33fd8364bb9384137 |
| check_npm_audit_triage | PASS | 0 | artifacts/proof/current/check_npm_audit_triage.log | c9bab79018cc60539b4fa5a6d6b6e291f3138327e6689b409cb60d8087b54092 |
| map_route_check | PASS | 0 | artifacts/proof/current/map_route_check.log | 3f2c0fb18144134952224494bc6690cde35213914ff5880a8eed0b5ca519e30f |
| public_api_boundary | PASS | 0 | artifacts/proof/current/public_api_boundary.log | fc94f2869cb84e91d6ec572dc84697bd61a8a1ba80fc9533118e4a69216927aa |
| canlii_staging_proof | PASS | 0 | artifacts/proof/current/canlii_staging_proof.log | d7c9393bb589559678b644f26519944ef1a69f81a771fdbd5fce0282bb665ab5 |
| proof_freshness | PASS | 0 | artifacts/proof/current/proof_freshness.log | c8faae69c90ce01f3ee234224929710292754f93b993666363c8caed840eadd0 |
| single_proof_authority | PASS | 0 | artifacts/proof/current/single_proof_authority.log | 67de9d9d555d8a633cccb3b3fd168f55f5975ed306de95965f06666949cc4337 |
| release_readiness_generation | PASS | 0 | artifacts/proof/current/release_readiness.md | 63e56c9c40cbdc32400fb4efdb237d0bc53b5c9b174f01068cf5d374314fcf2a |
| proof_consistency_pytest | PASS | 0 | artifacts/proof/current/proof_consistency_pytest.log | 71b613bcd27213dfff551d96b719001cddd9753def7294194d078f5a3c0dc56a |
| archive_validation | PASS | 0 | artifacts/proof/current/archive_validation.log | 623c71baaa9df7cfbc4ce9f086814acbbead7c50dc95d34f7eda7d6be3b2a24a |
| check_proof_manifest | PASS | 0 | artifacts/proof/current/check_proof_manifest.log | e63ce35132ca4d582b603680717610f4abe0456f3d6c0f26fde65294e4a21910 |
| check_no_local_paths_in_release_proof | PASS | 0 | artifacts/proof/current/check_no_local_paths_in_release_proof.log | 7ab4d071c63ecc123622b94a78dda4a32381a788cc2f318f840fe2f9e799c8e4 |
| check_proof_consistency | PASS | 0 | artifacts/proof/current/check_proof_consistency.log | 0a6ed516987c56172c896b5e5e4bae178cd6f9a2b53df2aa17bb118215f63a28 |
| required_proof_logs | PASS | 0 | artifacts/proof/current/required_proof_logs.log | a3bb446f2cd83447e8dcc0f301e9458579aaa156f0bcbac9691e805033a503b9 |
| release_gate | PASS | 0 | artifacts/proof/current/release_gate.log | e1fcfd53b6392a1c1c4c02073a8f64a00b602cc1978efb22fd1d89be4a35fd9e |

## Optional Proof Gates

| gate | status | exit_code | log | sha256 |
|---|---|---:|---|---|
| static_guards | PASS | 0 | artifacts/proof/current/static_guards.log | 115a68267999528d3cc712acd354f443bc0db2bd743118066bb8d8f59c01ce65 |

## Remaining Blockers

- none

## Stale Or Misreported Claims

- none

## Next Repair Action

- Resolve any required failed gate and rerun scripts/release_gate.py.
