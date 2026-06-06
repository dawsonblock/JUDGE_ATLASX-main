#!/usr/bin/env python3
"""Generate release_gate.json last, only if all proof criteria pass."""

import json
import sys
import platform
from pathlib import Path
from datetime import datetime, timezone
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PROOF_DIR = ROOT / "artifacts" / "proof" / "current"

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
        return result.stdout.strip().split('\n')[0]
    except:
        return "unknown"

# Check all required proof files exist
required_files = [
    "backend_compile.log",
    "backend_import.log",
    "backend_pytest_collect.log",
    "backend_pytest.log",
    "backend_pytest.xml",
    "frontend_build.log",
    "frontend_test.log",
    "frontend_route_smoke.log",
    "docker_runtime_preflight.log",
    "source_registry_proof_pytest.log",
    "source_registry_status.json",
    "check_proof_consistency.log",
    "status_truth_consistency.log",
    "required_log_index.json",
    "proof_manifest.json",
]

missing = []
for f in required_files:
    path = PROOF_DIR / f
    if not path.exists() or path.stat().st_size <= 0:
        missing.append(f)

# Check required_log_index.json for completeness
required_log_index_pass = False
if (PROOF_DIR / "required_log_index.json").exists():
    with open(PROOF_DIR / "required_log_index.json") as f:
        idx = json.load(f)
        required_log_index_pass = idx.get("pass", False)

# Check proof_manifest.json
manifest_pass = False
if (PROOF_DIR / "proof_manifest.json").exists():
    with open(PROOF_DIR / "proof_manifest.json") as f:
        manifest = json.load(f)
        manifest_pass = manifest.get("overall_pass", False)

# Gather environment info
python_version = f"Python {platform.python_version()}"
node_version = run_cmd("node --version")
npm_version = run_cmd("npm --version")
git_commit = run_cmd("git -C " + str(ROOT) + " rev-parse --short HEAD")

# Build release gate
release_gate = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "release_name": "JUDGE_ATLAS-main-final",
    "python_version": python_version,
    "node_version": node_version,
    "npm_version": npm_version,
    "git_commit": git_commit,
    "alpha_gate_passed": not missing and required_log_index_pass and manifest_pass,
    "self_verifying_alpha": not missing and required_log_index_pass and manifest_pass,
    "production_ready": False,  # Intentionally false for alpha
    "public_release_safe": False,  # Intentionally false for alpha
    "missing_required_files": missing,
    "required_log_index_pass": required_log_index_pass,
    "proof_manifest_pass": manifest_pass,
    "referenced_logs": [
        "artifacts/proof/current/backend_compile.log",
        "artifacts/proof/current/backend_import.log",
        "artifacts/proof/current/backend_pytest_collect.log",
        "artifacts/proof/current/backend_pytest.log",
        "artifacts/proof/current/backend_pytest.xml",
        "artifacts/proof/current/frontend_build.log",
        "artifacts/proof/current/frontend_test.log",
        "artifacts/proof/current/frontend_route_smoke.log",
        "artifacts/proof/current/docker_runtime_preflight.log",
        "artifacts/proof/current/source_registry_proof_pytest.log",
        "artifacts/proof/current/source_registry_status.json",
        "artifacts/proof/current/check_proof_consistency.log",
        "artifacts/proof/current/status_truth_consistency.log",
    ],
    "required_documents": [
        "artifacts/proof/current/CURRENT_PROOF.md",
        "artifacts/proof/current/CURRENT_ALPHA_STATUS.md",
        "artifacts/proof/current/REPAIR_REPORT.md",
        "artifacts/proof/current/release_readiness.md",
        "FINAL_RELEASE_HANDOFF.md",
    ],
}

# Write release gate
dest = PROOF_DIR / "release_gate.json"
dest.parent.mkdir(parents=True, exist_ok=True)
dest.write_text(json.dumps(release_gate, indent=2), encoding="utf-8")

print(f"Generated: {dest}")
print(f"Alpha gate passed: {release_gate['alpha_gate_passed']}")
print(f"Missing files: {missing}")

if release_gate['alpha_gate_passed']:
    print("\nRelease gate: PASS - Archive is ready for packaging")
else:
    print("\nRelease gate: FAIL - Cannot package")
    sys.exit(1)
