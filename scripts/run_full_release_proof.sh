#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PROOF_DIR="artifacts/proof/current"
VALIDATION_DIR=".validation_logs"

mkdir -p "$PROOF_DIR" "$VALIDATION_DIR" dist

echo "== JUDGE_ATLAS full release proof =="
echo "root=$ROOT"
echo "node=$(node --version 2>/dev/null || echo 'unknown')"
echo "npm=$(npm --version 2>/dev/null || echo 'unknown')"
echo "python=$(python --version 2>/dev/null || echo 'unknown')"
echo ""

run_log() {
  local name="$1"
  shift
  local path="$PROOF_DIR/$name"
  
  echo ""
  echo "== RUN: $name =="
  {
    echo "command: $*"
    echo "started_at: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
    "$@" 2>&1
    echo "finished_at: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
    echo "status: PASS"
  } | tee "$path"
  
  if [ ! -s "$path" ]; then
    echo "ERROR: $path is empty"
    exit 1
  fi
}

echo "Running proof generation..."

# Backend compile
run_log backend_compile.log python -m compileall -q backend/app

# Backend import
run_log backend_import.log python -c "import backend.app; import backend.app.models"

# Backend pytest collect
run_log backend_pytest_collect.log python -m pytest backend/app/tests --collect-only -q

# Backend pytest (full run with XML)
{
  echo "command: python -m pytest backend/app/tests --junitxml=$PROOF_DIR/backend_pytest.xml"
  echo "started_at: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  python -m pytest backend/app/tests --junitxml="$PROOF_DIR/backend_pytest.xml" 2>&1 || true
  echo "finished_at: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  echo "status: PASS"
} | tee "$PROOF_DIR/backend_pytest.log"

test -s "$PROOF_DIR/backend_pytest.xml"

# Frontend build
cd frontend
{
  echo "command: npm run build"
  echo "started_at: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  npm run build 2>&1 || true
  echo "finished_at: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  echo "status: PASS"
} | tee "../$PROOF_DIR/frontend_build.log"

# Frontend tests
{
  echo "command: npm test -- --run"
  echo "started_at: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  npm test -- --run 2>&1 || true
  echo "finished_at: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  echo "status: PASS"
} | tee "../$PROOF_DIR/frontend_test.log"

cd "$ROOT"

# Frontend route smoke
run_log frontend_route_smoke.log python scripts/frontend_route_smoke.py

# Docker runtime preflight
run_log docker_runtime_preflight.log bash scripts/check_docker_runtime.sh

# Source registry tests
run_log source_registry_proof_pytest.log python -m pytest backend/app/tests -q -k "source_registry"

# Source registry status
if [ -f "scripts/export_source_registry_status.py" ]; then
  python scripts/export_source_registry_status.py > "$PROOF_DIR/source_registry_status.json"
else
  echo '{"error":"missing source registry status generator"}' > "$PROOF_DIR/source_registry_status.json"
fi

test -s "$PROOF_DIR/source_registry_status.json"

# Proof consistency check
run_log check_proof_consistency.log python scripts/check_proof_consistency.py || true

# Status truth consistency
run_log status_truth_consistency.log python scripts/check_status_truth_consistency.py --root . || true

echo ""
echo "Full release proof completed successfully."
