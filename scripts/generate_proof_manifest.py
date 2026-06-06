#!/usr/bin/env python3
"""Generate proof_manifest.json from real files and test results."""

import json
import sys
import platform
from pathlib import Path
from datetime import datetime, timezone
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PROOF_DIR = ROOT / "artifacts" / "proof" / "current"

def get_pytest_xml_summary(xml_path: Path):
    """Parse JUnit XML and extract test summary."""
    if not xml_path.exists():
        return {"error": "xml not found"}
    
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        # Get testsuite stats
        tests = int(root.get("tests", 0))
        failures = int(root.get("failures", 0))
        errors = int(root.get("errors", 0))
        skipped = int(root.get("skipped", 0))
        
        return {
            "tests": tests,
            "failures": failures,
            "errors": errors,
            "skipped": skipped,
            "passed": tests - failures - errors - skipped,
            "pass": failures == 0 and errors == 0,
        }
    except Exception as e:
        return {"error": str(e)}

def check_file_exists(rel_path: str) -> bool:
    """Check if a proof file exists and has content."""
    path = PROOF_DIR / Path(rel_path).name
    return path.exists() and path.stat().st_size > 0

# Gather environment info
import subprocess

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
        return result.stdout.strip().split('\n')[0]
    except:
        return "unknown"

python_version = f"Python {platform.python_version()}"
node_version = run_cmd("node --version")
npm_version = run_cmd("npm --version")
git_commit = run_cmd("git -C " + str(ROOT) + " rev-parse --short HEAD")

# Check all proof files
backend_pytest_xml = PROOF_DIR / "backend_pytest.xml"
backend_pytest_summary = get_pytest_xml_summary(backend_pytest_xml)

# Build manifest
manifest = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "release_name": "JUDGE_ATLAS-main-final",
    "python_version": python_version,
    "node_version": node_version,
    "npm_version": npm_version,
    "git_commit": git_commit,
    "proof_root": str(PROOF_DIR),
    "required_log_index": "artifacts/proof/current/required_log_index.json",
    "backend_pytest": backend_pytest_summary,
    "backend_compile_pass": check_file_exists("backend_compile.log"),
    "backend_import_pass": check_file_exists("backend_import.log"),
    "frontend_build_pass": check_file_exists("frontend_build.log"),
    "frontend_tests_pass": check_file_exists("frontend_test.log"),
    "frontend_route_smoke_pass": check_file_exists("frontend_route_smoke.log"),
    "docker_runtime_pass": check_file_exists("docker_runtime_preflight.log"),
    "source_registry_proof_pass": check_file_exists("source_registry_proof_pytest.log"),
    "source_registry_status_present": check_file_exists("source_registry_status.json"),
    "proof_consistency_pass": check_file_exists("check_proof_consistency.log"),
    "status_consistency_pass": check_file_exists("status_truth_consistency.log"),
}

# Overall pass criteria
manifest["all_required_logs_present"] = (
    backend_pytest_summary.get("pass", False) and
    manifest["backend_compile_pass"] and
    manifest["backend_import_pass"] and
    manifest["frontend_build_pass"] and
    manifest["frontend_tests_pass"] and
    manifest["docker_runtime_pass"]
)

manifest["overall_pass"] = manifest["all_required_logs_present"]

# Write manifest
dest = PROOF_DIR / "proof_manifest.json"
dest.parent.mkdir(parents=True, exist_ok=True)
dest.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

print(f"Generated: {dest}")
print(f"Backend pytest: {backend_pytest_summary}")
print(f"Overall pass: {manifest['overall_pass']}")

if not manifest["overall_pass"]:
    print("\nERROR: Proof manifest shows failures")
    sys.exit(1)
