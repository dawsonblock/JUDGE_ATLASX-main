# RELEASE_READINESS

- generated_at_utc: 2026-06-02T01:01:04.685346+00:00
- overall_status: self-verifying-alpha
- alpha_candidate: true
- self_verifying_alpha: true
- production_release_candidate: false
- production_ready: false
- public_release_safe: false
- release_recommendation: self-verifying-alpha
- archive_hash: f2376b6958df606bdd3a351934682bfa088a7092
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
| backend_pytest_collect | PASS | 0 | artifacts/proof/current/backend_pytest_collect.log | 14cb026ccb1c0ea67c8a11014854d70c724c4f45412ff5a2eb0ab023123e3af1 |
| runtime_smoke | PASS | 0 | artifacts/proof/current/runtime_smoke.log | 561261d657b5b6b5bd99f9db4f716948b8a6188d16238c6259018c5ac421a7f3 |
| backend_pytest | PASS | 0 | artifacts/proof/current/backend_pytest.log | 953e87ce8587ae834ae4fde734c7a98aa6090d8342d2e19ed284927d9125502d |
| check_migrations | PASS | 0 | artifacts/proof/current/check_migrations.log | b1a31ef1e482457fd1c47ac213cc98d199e78f8051acc81264a305cf629b66bf |
| docker_runtime_preflight | PASS | 0 | artifacts/proof/current/docker_runtime_preflight.log | c19c3316f8f5e048d452c3379fa6d90822f99eb6c6fcc29d35b077c7e2deb6cb |
| docker_smoke | PASS | 0 | artifacts/proof/current/docker_smoke.log | ad6126583d4868d403a70d9f19d4c09fdd1879d3c3037ba96bfceb450e1409b6 |
| postgis_proof | PASS | 0 | artifacts/proof/current/postgis_proof.log | 8208e296ec625b2be0d84fe9827c910418a4f790064843eff680d4e5b60561dd |
| egress_proxy_proof | PASS | 0 | artifacts/proof/current/egress_proxy_proof.log | 9ed1ba0db7c66e067d6766a16c9283eb9bfe941476ff85683e900331169e6459 |
| demo_proof | PASS | 0 | artifacts/proof/current/demo_proof.log | 5de510ce42797df8e127acf38025711918f2b55854ecaf8f51d8c3d81e29026e |
| validate_sources | PASS | 0 | artifacts/proof/current/validate_sources.log | 4d734d90bf04c25a04d4752d5067c94dc51e963876cfc4f61bbf698de63c27ba |
| check_yaml_duplicate_keys | PASS | 0 | artifacts/proof/current/check_yaml_duplicate_keys.log | 88b52b46f87e415fc01b849aececd79f567ac8ea21f09f1d891a37eca7ddb06d |
| verify_source_registry | PASS | 0 | artifacts/proof/current/verify_source_registry.log | b0e1554b5b1815bddb61ee77b2e0e1cee36efeac8ce679abedd6a00cf2bfaefe |
| source_registry_status | PASS | 0 | artifacts/proof/current/source_registry_status.log | a627028cae8dc77fd1985e05a14c9eb33197aebcd2791d1824866799fe8c86be |
| generate_coverage_matrix | PASS | 0 | artifacts/proof/current/generate_coverage_matrix.log | 3d868e3cbd1d339db9943afaaf81a5a2e3ad66fc852f8f7a5f57ffc063133f23 |
| check_source_registry_docs | PASS | 0 | artifacts/proof/current/check_source_registry_docs.log | fe1b62e3c0b1bc448549dfe49a124455c9c01b1813f6d4e8effac96e238d35fe |
| prepare_proof_db | PASS | 0 | artifacts/proof/current/prepare_proof_db.log | ef6779db88eeffa32551cb68ca12147f76837d1ef139b9e8d67f668940f260d5 |
| verify_evidence_store | PASS | 0 | artifacts/proof/current/verify_evidence_store.log | 7b693f37394b451d76dd236d9668d34a5e48b67f48dee151954763083deca20f |
| verify_audit_chain | PASS | 0 | artifacts/proof/current/verify_audit_chain.log | 617469c6dafe05e51aabac659c9ccafcf45c0683a61da6bee9a872d31b4f7f34 |
| auth_mutation_route_coverage | PASS | 0 | artifacts/proof/current/auth_mutation_route_coverage.log | 2a7d251874f6b6cfb13fff84ae694c0637e665e4a6f687e4a389d2364b3f9915 |
| mutation_fail_closed_coverage | PASS | 0 | artifacts/proof/current/mutation_fail_closed_coverage.log | d14f61a853f5d4f2b49932e04bc819a452c3d94029788fe69c2a6cdeb8ed377b |
| check_node_policy | PASS | 0 | artifacts/proof/current/check_node_policy.log | 5a8b2cacbf3c1df63dc8cd6f8a7d3e1769e0683212fc3442cefff374232c5c32 |
| frontend_node_gate | PASS | 0 | artifacts/proof/current/frontend_node_gate.log | 39dc95fbc807439ae0edd07db104299b2a68d401fefe617df96cb835e3585dc9 |
| frontend_install | PASS | 0 | artifacts/proof/current/frontend_install.log | 95ce38bc6fb19418e34a252dcfb62941cb51ca3c12dbf606909d211192a97dab |
| frontend_lint | PASS | 0 | artifacts/proof/current/frontend_lint.log | 9d79910829d5abcf1161f85f3d57cc9c745d1edd5734a88fee634c9913b368e8 |
| frontend_typecheck | PASS | 0 | artifacts/proof/current/frontend_typecheck.log | 701338e1389ab6284419cba533b353099f6b47658b930e128a8627a7a2d6d6e7 |
| frontend_contracts | PASS | 0 | artifacts/proof/current/frontend_contracts.log | 25121da8a3d34a721d918e60f138fa7e45358e0fb6c286da6cc2c2ff5e82da65 |
| frontend_build | PASS | 0 | artifacts/proof/current/frontend_build.log | f5c0fd9e7b5105d1d4b9366169b4026967eb4b0ffee1343822ef7be2c71cd4ea |
| check_api_contracts | PASS | 0 | artifacts/proof/current/check_api_contracts.log | f6750f8d64797a660c9122c245fa0ae38eb689dd8023b7fef1d0481e4ab86216 |
| frontend_backend_route_contract | PASS | 0 | artifacts/proof/current/frontend_backend_route_contract.log | f3563209ec0dcbcbf599836f73236926eee160235914e0fe0e660e945c9042a0 |
| frontend_route_smoke | PASS | 0 | artifacts/proof/current/frontend_route_smoke.log | 4afbcaf47374fb181a53b0939ce9ef84d5fde94e2028df8eb9e29b1fe9b322f0 |
| repo_generated_files | PASS | 0 | artifacts/proof/current/repo_generated_files.log | 1f136c767a6ec6bd6d527af249dd34271e19a2e1287eedd33fd8364bb9384137 |
| check_npm_audit_triage | PASS | 0 | artifacts/proof/current/check_npm_audit_triage.log | c9bab79018cc60539b4fa5a6d6b6e291f3138327e6689b409cb60d8087b54092 |
| map_route_check | PASS | 0 | artifacts/proof/current/map_route_check.log | 3f2c0fb18144134952224494bc6690cde35213914ff5880a8eed0b5ca519e30f |
| public_api_boundary | PASS | 0 | artifacts/proof/current/public_api_boundary.log | 92e4ec8cf5da0607226699f33cbbb5573f5af5df899868159c302da12b2e603f |
| canlii_staging_proof | PASS | 0 | artifacts/proof/current/canlii_staging_proof.log | d7c9393bb589559678b644f26519944ef1a69f81a771fdbd5fce0282bb665ab5 |
| proof_freshness | PASS | 0 | artifacts/proof/current/proof_freshness.log | ae10f18fec257494a5dd735e921ef3060ede8fbc77352f1dcd9842e3d5e9c7da |
| single_proof_authority | PASS | 0 | artifacts/proof/current/single_proof_authority.log | 67de9d9d555d8a633cccb3b3fd168f55f5975ed306de95965f06666949cc4337 |
| release_readiness_generation | PASS | 0 | artifacts/proof/current/release_readiness.md | 1882dcf4e126904b7c48951245e2d30951b6347a6a11fbe11d7e53a3acaa6ab8 |
| proof_consistency_pytest | PASS | 0 | artifacts/proof/current/proof_consistency_pytest.log | 71b613bcd27213dfff551d96b719001cddd9753def7294194d078f5a3c0dc56a |
| archive_validation | PASS | 0 | artifacts/proof/current/archive_validation.log | 128e95b80c8f77699a73ecb2bcd72d0cbbdfc9f3ea4488a2be9b6ffbad86cf90 |
| check_proof_manifest | PASS | 0 | artifacts/proof/current/check_proof_manifest.log | e63ce35132ca4d582b603680717610f4abe0456f3d6c0f26fde65294e4a21910 |
| check_no_local_paths_in_release_proof | PASS | 0 | artifacts/proof/current/check_no_local_paths_in_release_proof.log | 7ab4d071c63ecc123622b94a78dda4a32381a788cc2f318f840fe2f9e799c8e4 |
| check_proof_consistency | PASS | 0 | artifacts/proof/current/check_proof_consistency.log | 0a6ed516987c56172c896b5e5e4bae178cd6f9a2b53df2aa17bb118215f63a28 |
| required_proof_logs | PASS | 0 | artifacts/proof/current/required_proof_logs.log | a3bb446f2cd83447e8dcc0f301e9458579aaa156f0bcbac9691e805033a503b9 |
| release_gate | PASS | 0 | artifacts/proof/current/release_gate.log | 6bba7546cf29335011877b948fcde1a4db85c29b56982f80ae0a99ea662fa2b1 |

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
