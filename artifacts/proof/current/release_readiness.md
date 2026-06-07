# RELEASE_READINESS

- generated_at_utc: 2026-06-07T06:20:13.919225+00:00
- overall_status: blocked
- alpha_candidate: false
- self_verifying_alpha: false
- production_release_candidate: false
- production_ready: false
- public_release_safe: false
- release_recommendation: blocked
- archive_hash: abcd220675f7fb5134519ab88ae303bcab4b70a2
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
| check_no_direct_ingestion_network_clients | PASS | 0 | artifacts/proof/current/check_no_direct_ingestion_network_clients.log | a02b4b7b012d3d75ab6fe8c669cc59c29c9898a597ed6fe747ad1eb35d18b715 |
| check_external_boundaries | PASS | 0 | artifacts/proof/current/check_external_boundaries.log | da039530a33bf730b0cc264637a3196b2212a42c42e24f50edcb6f1090c41b62 |
| check_dockerfile_copy_paths | PASS | 0 | artifacts/proof/current/check_dockerfile_copy_paths.log | 9cb5347afde90057ddc1a4fdcecd6ae1318290990ddadf2f5dfaeebf1e92eb2a |
| check_compose_auth_defaults | PASS | 0 | artifacts/proof/current/check_compose_auth_defaults.log | ce53c858a818dccbbd3685948e8ce1414dddb23714d77e259787b0ce79eceac9 |
| backend_compile | PASS | 0 | artifacts/proof/current/backend_compile.log | ff048fbcb05f4b23e858a813501477214166d826b765b8ca1f6bba526c2b6e9c |
| backend_import | PASS | 0 | artifacts/proof/current/backend_import.log | 6393cbd986957cbe5d40d4556853a5b1c49f25d6898cb7f61eaa8aee496ec4f5 |
| backend_pytest_collect | PASS | 0 | artifacts/proof/current/backend_pytest_collect.log | 8473b5cbd71a9f2225e0692b179c7a06a24e377ebfd13d46e2502da0341edb75 |
| runtime_smoke | PASS | 0 | artifacts/proof/current/runtime_smoke.log | 561261d657b5b6b5bd99f9db4f716948b8a6188d16238c6259018c5ac421a7f3 |
| backend_pytest | PASS | 0 | artifacts/proof/current/backend_pytest.log | 36f92f2bbc7a4f7e06c36ba85a4cd3aa455064402a3cb2ec141caa21cff7e74d |
| check_migrations | FAIL | 1 | artifacts/proof/current/check_migrations.log | d5204c86768992497ca4f7e4270dd842c5074fff0fb92c2612c2047a482f80b7 |
| docker_runtime_preflight | FAIL | 1 | artifacts/proof/current/docker_runtime_preflight.log | d8a5b94b05f00a16c4d18025d8726153fd88b53e15f5b0f3f0c51f3b5c27fdab |
| docker_smoke | BLOCKED | 1 | artifacts/proof/current/docker_smoke.log | c6593ad24f69d3c07a62c0aa26fba3a8e0b9cc02d0fde1d040db17258fd57c2c |
| postgis_proof | BLOCKED | 1 | artifacts/proof/current/postgis_proof.log | 161e3405df71182f2be5bc8d5b88e4558cb8779029700e68c4a76192e027b0c8 |
| egress_proxy_proof | PASS | 0 | artifacts/proof/current/egress_proxy_proof.log | 490a84e30088f031f85e4ed169efc77b63c605e0c4fc833f0de727c0dde0c060 |
| demo_proof | FAIL | 1 | artifacts/proof/current/demo_proof.log | 179220ad0ab14d997ed0dd6c6ac24635b3664141083d705800ea6c98ac394098 |
| validate_sources | PASS | 0 | artifacts/proof/current/validate_sources.log | 3704f047a9579c5906775936cecc4b2bb34deafe905b85d73c69f63c2363b6a9 |
| check_yaml_duplicate_keys | PASS | 0 | artifacts/proof/current/check_yaml_duplicate_keys.log | 88b52b46f87e415fc01b849aececd79f567ac8ea21f09f1d891a37eca7ddb06d |
| verify_source_registry | PASS | 0 | artifacts/proof/current/verify_source_registry.log | 78dd57538d166988c711d48022b38744f7d6a093673bae81ddbba6fb94277996 |
| source_registry_status | PASS | 0 | artifacts/proof/current/source_registry_status.log | de9e0de1944794266771043f45171dd1179979af2e0e408db8fed7b1f56802b8 |
| generate_coverage_matrix | PASS | 0 | artifacts/proof/current/generate_coverage_matrix.log | 3d868e3cbd1d339db9943afaaf81a5a2e3ad66fc852f8f7a5f57ffc063133f23 |
| check_source_registry_docs | FAIL | 1 | artifacts/proof/current/check_source_registry_docs.log | 51bf3c97ed828a33f759c72cdb49f8f77976815d69984d0fc6eac6ecec8805bd |
| prepare_proof_db | FAIL | 1 | artifacts/proof/current/prepare_proof_db.log | 66bafe57c07edf3e005ab5382cf3e96de190eb8af7d0edd8525070307e8ee407 |
| verify_evidence_store | PASS | 0 | artifacts/proof/current/verify_evidence_store.log | 1179d0c8c1c56de20d4f917fd60915207780fa80305d5ffb0e8d31ff25adc9a1 |
| evidence_verification_standard | PASS | 0 | artifacts/proof/current/evidence_verification_standard.log | 135d21e9308aeca27d724d74b34077ea16cb290440c5de5a76e19c3b37604ee9 |
| evidence_verification_standard_pytest | PASS | 0 | artifacts/proof/current/evidence_verification_standard_pytest.log | c492c41580448240d0cd071f0c665f8548d9931c41518b75e86f2e55f4694f2a |
| source_registry_proof_pytest | FAIL | 1 | artifacts/proof/current/source_registry_proof_pytest.log | c2ee0ef51b37cd469bf21553ac8c970e9c998f231faf918cdf32748a6a5b364a |
| verify_audit_chain | PASS | 0 | artifacts/proof/current/verify_audit_chain.log | 01ab2325e8e19ba0c1931aa6934d2f6222d47c828b058e1df0f21d98a6727a16 |
| auth_mutation_route_coverage | PASS | 0 | artifacts/proof/current/auth_mutation_route_coverage.log | c71587ec14dbe44f50f2795b5c7cfd104cb929c9c3d0a4f5dccc87bdf8c4f926 |
| mutation_fail_closed_coverage | PASS | 0 | artifacts/proof/current/mutation_fail_closed_coverage.log | a5827770312079eb477c2e8db85e3e13e8ab42ada37ce886e4a1cb159c9425cb |
| check_node_policy | PASS | 0 | artifacts/proof/current/check_node_policy.log | 20bc4a96240caa5415f01ad0cf2520f483d16aa14bf114ec9e251eab80bfdc4b |
| frontend_node_gate | PASS | 0 | artifacts/proof/current/frontend_node_gate.log | 39dc95fbc807439ae0edd07db104299b2a68d401fefe617df96cb835e3585dc9 |
| frontend_install | PASS | 0 | artifacts/proof/current/frontend_install.log | 3f0309c3b612b6ba51edf2bdb09e0219fb8a84bb9f83ee91fdf051f81d503338 |
| frontend_lint | PASS | 0 | artifacts/proof/current/frontend_lint.log | 9d79910829d5abcf1161f85f3d57cc9c745d1edd5734a88fee634c9913b368e8 |
| frontend_typecheck | PASS | 0 | artifacts/proof/current/frontend_typecheck.log | 701338e1389ab6284419cba533b353099f6b47658b930e128a8627a7a2d6d6e7 |
| frontend_contracts | PASS | 0 | artifacts/proof/current/frontend_contracts.log | 51ff1af5f1aeead073eae6ddf7ac95e7e504a3f777f9a793e0850178d9ddcaa7 |
| frontend_build | PASS | 0 | artifacts/proof/current/frontend_build.log | 39798d23c4446d3d60b08cb30d3115a9baeeeded0f0434dddee9a487463644b0 |
| check_api_contracts | PASS | 0 | artifacts/proof/current/check_api_contracts.log | f6750f8d64797a660c9122c245fa0ae38eb689dd8023b7fef1d0481e4ab86216 |
| frontend_backend_route_contract | PASS | 0 | artifacts/proof/current/frontend_backend_route_contract.log | f3563209ec0dcbcbf599836f73236926eee160235914e0fe0e660e945c9042a0 |
| frontend_route_smoke | PASS | 0 | artifacts/proof/current/frontend_route_smoke.log | 4afbcaf47374fb181a53b0939ce9ef84d5fde94e2028df8eb9e29b1fe9b322f0 |
| repo_generated_files | PASS | 0 | artifacts/proof/current/repo_generated_files.log | 1f136c767a6ec6bd6d527af249dd34271e19a2e1287eedd33fd8364bb9384137 |
| check_npm_audit_triage | PASS | 0 | artifacts/proof/current/check_npm_audit_triage.log | c9bab79018cc60539b4fa5a6d6b6e291f3138327e6689b409cb60d8087b54092 |
| map_route_check | PASS | 0 | artifacts/proof/current/map_route_check.log | 3f2c0fb18144134952224494bc6690cde35213914ff5880a8eed0b5ca519e30f |
| public_api_boundary | PASS | 0 | artifacts/proof/current/public_api_boundary.log | 58a4f3ea1f7d9641a21c429d087a46bd59fe7c3cffee2a55d2f1e5de260732f1 |
| canlii_staging_proof | PASS | 0 | artifacts/proof/current/canlii_staging_proof.log | d7c9393bb589559678b644f26519944ef1a69f81a771fdbd5fce0282bb665ab5 |
| proof_freshness | PASS | 0 | artifacts/proof/current/proof_freshness.log | ac774803d35d19917290268e034ccb253575fb8fbadbe10237afe3900b53094f |
| single_proof_authority | PASS | 0 | artifacts/proof/current/single_proof_authority.log | 67de9d9d555d8a633cccb3b3fd168f55f5975ed306de95965f06666949cc4337 |
| release_readiness_generation | PASS | 0 | artifacts/proof/current/release_readiness.md | bb2b46e789437da435e792de6c2f91eb41b90771eed2795487149807ce410e40 |
| proof_consistency_pytest | PASS | 0 | artifacts/proof/current/proof_consistency_pytest.log | 71b613bcd27213dfff551d96b719001cddd9753def7294194d078f5a3c0dc56a |
| archive_validation | PASS | 0 | artifacts/proof/current/archive_validation.log | 93d7cdaa6fdfe426f6090fdff4d18f33e4cb24e950f225c138b6fd2888b2e208 |
| check_proof_manifest | PASS | 0 | artifacts/proof/current/check_proof_manifest.log | 652b5b93427a7011f67a82d8814c80478e93ba6e531ba15ca3bec2aa8a6d5b01 |
| check_no_local_paths_in_release_proof | PASS | 0 | artifacts/proof/current/check_no_local_paths_in_release_proof.log | 7ab4d071c63ecc123622b94a78dda4a32381a788cc2f318f840fe2f9e799c8e4 |
| check_proof_consistency | PASS | 0 | artifacts/proof/current/check_proof_consistency.log | 0a6ed516987c56172c896b5e5e4bae178cd6f9a2b53df2aa17bb118215f63a28 |
| required_proof_logs | PASS | 0 | artifacts/proof/current/required_proof_logs.log | fe0b1f0baf2755f5edae374bb5d2f57bade7a008916ce2e2c74a0ac951dadf61 |
| release_gate | PASS | 0 | artifacts/proof/current/release_gate.log | 6ff2665745490bc30f7b718473c4b27b2833f544d12be43184e3861af1c8f0f9 |

## Optional Proof Gates

| gate | status | exit_code | log | sha256 |
|---|---|---:|---|---|
| static_guards | PASS | 0 | artifacts/proof/current/static_guards.log | 7ec501e5df91756421494a2236a0591b146d76413a7d5a71be560f54a39898c9 |

## Remaining Blockers

- required_gate_failed:check_migrations
- required_gate_failed:docker_runtime_preflight
- required_gate_failed:docker_smoke
- required_gate_failed:postgis_proof
- required_gate_failed:demo_proof
- required_gate_failed:check_source_registry_docs
- required_gate_failed:prepare_proof_db
- required_gate_failed:source_registry_proof_pytest

## Stale Or Misreported Claims

- readiness is blocked due to failed/missing required proof evidence

## Next Repair Action

- Resolve any required failed gate and rerun scripts/release_gate.py.
