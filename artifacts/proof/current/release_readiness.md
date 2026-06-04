# RELEASE_READINESS

- generated_at_utc: 2026-06-04T23:25:35.494581+00:00
- overall_status: self-verifying-alpha
- alpha_candidate: true
- self_verifying_alpha: true
- production_release_candidate: false
- production_ready: false
- public_release_safe: false
- release_recommendation: self-verifying-alpha
- archive_hash: 673826a516c4d12a74cbf88b4536eed79580cfaf
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
| backend_import | PASS | 0 | artifacts/proof/current/backend_import.log | 6393cbd986957cbe5d40d4556853a5b1c49f25d6898cb7f61eaa8aee496ec4f5 |
| backend_pytest_collect | PASS | 0 | artifacts/proof/current/backend_pytest_collect.log | fad7f7659f005b14b8b4743536041614300ecb28cff16858abc9a3175087ac58 |
| runtime_smoke | PASS | 0 | artifacts/proof/current/runtime_smoke.log | 561261d657b5b6b5bd99f9db4f716948b8a6188d16238c6259018c5ac421a7f3 |
| backend_pytest | PASS | 0 | artifacts/proof/current/backend_pytest.log | a4aceff39ec1fc8211c70e15776f403be479be6dabb1fe3571554bf57f674afd |
| check_migrations | PASS | 0 | artifacts/proof/current/check_migrations.log | b1a31ef1e482457fd1c47ac213cc98d199e78f8051acc81264a305cf629b66bf |
| docker_runtime_preflight | PASS | 0 | artifacts/proof/current/docker_runtime_preflight.log | a0393fb378b880c888335bac674db5a9a2689e3a264d09acce1a87495915a61c |
| docker_smoke | PASS | 0 | artifacts/proof/current/docker_smoke.log | aecaa0fe5d2dd8374b11b0396beb8c9dae389a9807fba64888d6d367898d4e18 |
| postgis_proof | PASS | 0 | artifacts/proof/current/postgis_proof.log | bed1911b7a4914001ea8b3710884bcaf60872423a2c1511e560bd4da217cd9b7 |
| egress_proxy_proof | PASS | 0 | artifacts/proof/current/egress_proxy_proof.log | c174c99a1d657dfb282d99769dbacbcbf4cb9818fc15ae14b814835f5c0eed0b |
| demo_proof | PASS | 0 | artifacts/proof/current/demo_proof.log | 5de510ce42797df8e127acf38025711918f2b55854ecaf8f51d8c3d81e29026e |
| validate_sources | PASS | 0 | artifacts/proof/current/validate_sources.log | 4d734d90bf04c25a04d4752d5067c94dc51e963876cfc4f61bbf698de63c27ba |
| check_yaml_duplicate_keys | PASS | 0 | artifacts/proof/current/check_yaml_duplicate_keys.log | 88b52b46f87e415fc01b849aececd79f567ac8ea21f09f1d891a37eca7ddb06d |
| verify_source_registry | PASS | 0 | artifacts/proof/current/verify_source_registry.log | 10564ceb6a4ddef00914e51e1ec4a28327de674b1f64887797eeb3a235828098 |
| source_registry_status | PASS | 0 | artifacts/proof/current/source_registry_status.log | a627028cae8dc77fd1985e05a14c9eb33197aebcd2791d1824866799fe8c86be |
| generate_coverage_matrix | PASS | 0 | artifacts/proof/current/generate_coverage_matrix.log | 3d868e3cbd1d339db9943afaaf81a5a2e3ad66fc852f8f7a5f57ffc063133f23 |
| check_source_registry_docs | PASS | 0 | artifacts/proof/current/check_source_registry_docs.log | fe1b62e3c0b1bc448549dfe49a124455c9c01b1813f6d4e8effac96e238d35fe |
| prepare_proof_db | PASS | 0 | artifacts/proof/current/prepare_proof_db.log | ef6779db88eeffa32551cb68ca12147f76837d1ef139b9e8d67f668940f260d5 |
| verify_evidence_store | PASS | 0 | artifacts/proof/current/verify_evidence_store.log | 7b693f37394b451d76dd236d9668d34a5e48b67f48dee151954763083deca20f |
| evidence_verification_standard | PASS | 0 | artifacts/proof/current/evidence_verification_standard.log | 135d21e9308aeca27d724d74b34077ea16cb290440c5de5a76e19c3b37604ee9 |
| evidence_verification_standard_pytest | PASS | 0 | artifacts/proof/current/evidence_verification_standard_pytest.log | 1ce171b82a4488765d25787c5b3e4ffd3cfc97e8d66272e142c6b5e5da4e9fa8 |
| source_registry_proof_pytest | PASS | 0 | artifacts/proof/current/source_registry_proof_pytest.log | a37398ba11abc14d093878beefe2dbd0a5f55f210e1243bfdd90b6b43f4084dc |
| verify_audit_chain | PASS | 0 | artifacts/proof/current/verify_audit_chain.log | f2b1305093f28b8907e9abc59004709990ef0f6d9b1f93707736282a7991cc18 |
| auth_mutation_route_coverage | PASS | 0 | artifacts/proof/current/auth_mutation_route_coverage.log | f28295362c3dc2f38306c652d331f889d27441cec589d65c2cfa68227fde1fc5 |
| mutation_fail_closed_coverage | PASS | 0 | artifacts/proof/current/mutation_fail_closed_coverage.log | 87bdf2d9e17d0d0ab955407988102381870d0e52fac613363453e5641fbe867a |
| check_node_policy | PASS | 0 | artifacts/proof/current/check_node_policy.log | 5a8b2cacbf3c1df63dc8cd6f8a7d3e1769e0683212fc3442cefff374232c5c32 |
| frontend_node_gate | PASS | 0 | artifacts/proof/current/frontend_node_gate.log | 39dc95fbc807439ae0edd07db104299b2a68d401fefe617df96cb835e3585dc9 |
| frontend_install | PASS | 0 | artifacts/proof/current/frontend_install.log | 2854f683cf588efd5f11e26ed51798a8bab8bed52a5a96b64bda0fbeab46df2b |
| frontend_lint | PASS | 0 | artifacts/proof/current/frontend_lint.log | 9d79910829d5abcf1161f85f3d57cc9c745d1edd5734a88fee634c9913b368e8 |
| frontend_typecheck | PASS | 0 | artifacts/proof/current/frontend_typecheck.log | 701338e1389ab6284419cba533b353099f6b47658b930e128a8627a7a2d6d6e7 |
| frontend_contracts | PASS | 0 | artifacts/proof/current/frontend_contracts.log | 1e38c67a5f783bf64bc1eeef3df7936b5a7f9c34130c6ecc3bdad1118ac64960 |
| frontend_build | PASS | 0 | artifacts/proof/current/frontend_build.log | 39798d23c4446d3d60b08cb30d3115a9baeeeded0f0434dddee9a487463644b0 |
| check_api_contracts | PASS | 0 | artifacts/proof/current/check_api_contracts.log | f6750f8d64797a660c9122c245fa0ae38eb689dd8023b7fef1d0481e4ab86216 |
| frontend_backend_route_contract | PASS | 0 | artifacts/proof/current/frontend_backend_route_contract.log | f3563209ec0dcbcbf599836f73236926eee160235914e0fe0e660e945c9042a0 |
| frontend_route_smoke | PASS | 0 | artifacts/proof/current/frontend_route_smoke.log | 4afbcaf47374fb181a53b0939ce9ef84d5fde94e2028df8eb9e29b1fe9b322f0 |
| repo_generated_files | PASS | 0 | artifacts/proof/current/repo_generated_files.log | 1f136c767a6ec6bd6d527af249dd34271e19a2e1287eedd33fd8364bb9384137 |
| check_npm_audit_triage | PASS | 0 | artifacts/proof/current/check_npm_audit_triage.log | c9bab79018cc60539b4fa5a6d6b6e291f3138327e6689b409cb60d8087b54092 |
| map_route_check | PASS | 0 | artifacts/proof/current/map_route_check.log | 3f2c0fb18144134952224494bc6690cde35213914ff5880a8eed0b5ca519e30f |
| public_api_boundary | PASS | 0 | artifacts/proof/current/public_api_boundary.log | 5a46b3cae2808bf2bcec6a3a5b2be8a970fde6e2f46608ee3269e9e47ebf2162 |
| canlii_staging_proof | PASS | 0 | artifacts/proof/current/canlii_staging_proof.log | d7c9393bb589559678b644f26519944ef1a69f81a771fdbd5fce0282bb665ab5 |
| proof_freshness | PASS | 0 | artifacts/proof/current/proof_freshness.log | 143fb5ae67fa65cd042e90941d4a981157baa5d10291a0cb0bd38bc43902d11a |
| single_proof_authority | PASS | 0 | artifacts/proof/current/single_proof_authority.log | 67de9d9d555d8a633cccb3b3fd168f55f5975ed306de95965f06666949cc4337 |
| release_readiness_generation | PASS | 0 | artifacts/proof/current/release_readiness.md | 217d009e7ff5bf799e760cd5580a98ecdc65db6aae7a1a9e698f0d179a7e047c |
| proof_consistency_pytest | PASS | 0 | artifacts/proof/current/proof_consistency_pytest.log | 13c7400ab5e03ad7aecc3bd7fe5d92c1a43f88f7748e0bed622d077cb5d338a0 |
| archive_validation | PASS | 0 | artifacts/proof/current/archive_validation.log | 9229454691b3b47b6251302473fc1c18e4cd8fb43066e522a483f0260083d1f7 |
| check_proof_manifest | PASS | 0 | artifacts/proof/current/check_proof_manifest.log | 652b5b93427a7011f67a82d8814c80478e93ba6e531ba15ca3bec2aa8a6d5b01 |
| check_no_local_paths_in_release_proof | PASS | 0 | artifacts/proof/current/check_no_local_paths_in_release_proof.log | 7ab4d071c63ecc123622b94a78dda4a32381a788cc2f318f840fe2f9e799c8e4 |
| check_proof_consistency | PASS | 0 | artifacts/proof/current/check_proof_consistency.log | 0a6ed516987c56172c896b5e5e4bae178cd6f9a2b53df2aa17bb118215f63a28 |
| required_proof_logs | PASS | 0 | artifacts/proof/current/required_proof_logs.log | fe0b1f0baf2755f5edae374bb5d2f57bade7a008916ce2e2c74a0ac951dadf61 |
| release_gate | PASS | 0 | artifacts/proof/current/release_gate.log | 6e89e87497bbcf40ad52abbf668d4a697971bce5dbeb51d0d6b0bd9c7425f4f4 |

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
