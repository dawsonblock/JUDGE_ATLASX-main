#!/usr/bin/env python3
"""Generate required_log_index.json from actual disk files."""

import hashlib
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
PROOF_DIR = ROOT / "artifacts" / "proof" / "current"

# These must exist after proof generation
REQUIRED = [
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
]

def sha256(path: Path) -> str:
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

entries = []
missing = []

for rel in REQUIRED:
    path = ROOT / rel
    if not path.exists() or not path.is_file():
        missing.append(rel)
        continue
    
    size = path.stat().st_size
    if size <= 0:
        missing.append(rel)
        continue
    
    entries.append({
        "path": rel,
        "exists": True,
        "size_bytes": size,
        "sha256": sha256(path),
    })

output = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "required_count": len(REQUIRED),
    "present_count": len(entries),
    "missing_count": len(missing),
    "missing": missing,
    "entries": entries,
    "pass": len(missing) == 0,
}

dest = PROOF_DIR / "required_log_index.json"
dest.parent.mkdir(parents=True, exist_ok=True)
dest.write_text(json.dumps(output, indent=2), encoding="utf-8")

print(f"Generated: {dest}")
print(f"Present: {len(entries)}/{len(REQUIRED)}")

if missing:
    print(f"\nMISSING REQUIRED LOGS ({len(missing)}):")
    for m in missing:
        print(f"  - {m}")
    sys.exit(1)

print("\nAll required logs present: PASS")
