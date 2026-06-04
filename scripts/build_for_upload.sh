#!/usr/bin/env bash
set -euo pipefail

# Build the canonical archive and place it where the user cannot miss it.
# This script exists because the user repeatedly uploads source snapshots
# instead of the canonical release archive. Make the right file obvious.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CANONICAL_ARCHIVE="${ROOT_DIR}/dist/JUDGE_ATLAS-main-final.zip"
UPLOAD_BASENAME="UPLOAD_THIS_JUDGE_ATLAS-main-final.zip"

# Try Desktop, fall back to repo root
if [[ -d "${HOME}/Desktop" ]]; then
    UPLOAD_TARGET="${HOME}/Desktop/${UPLOAD_BASENAME}"
elif [[ -d "${HOME}/desktop" ]]; then
    UPLOAD_TARGET="${HOME}/desktop/${UPLOAD_BASENAME}"
else
    UPLOAD_TARGET="${ROOT_DIR}/${UPLOAD_BASENAME}"
fi

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

log_pass() { echo -e "${GREEN}[PASS]${NC} $*"; }
log_fail() { echo -e "${RED}[FAIL]${NC} $*" >&2; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $*"; }
log_bold() { echo -e "${BOLD}$*${NC}"; }

cd "${ROOT_DIR}"

# Step 1: ensure canonical archive exists
if [[ ! -f "${CANONICAL_ARCHIVE}" ]]; then
    log_warn "Canonical archive not found. Building it now..."
    bash scripts/package_and_validate_release_archive.sh \
        --archive-path "${CANONICAL_ARCHIVE}" \
        --package-root-name JUDGE_ATLAS-main \
        --skip-release-gate \
        --skip-handoff-check \
        --skip-extracted-validation
fi

if [[ ! -f "${CANONICAL_ARCHIVE}" ]]; then
    log_fail "Failed to build canonical archive: ${CANONICAL_ARCHIVE}"
    exit 1
fi
log_pass "Canonical archive exists: ${CANONICAL_ARCHIVE}"

# Step 2: copy to obvious location
cp -f "${CANONICAL_ARCHIVE}" "${UPLOAD_TARGET}"
log_pass "Copied canonical archive to: ${UPLOAD_TARGET}"

# Step 3: compute SHA-256
ARCHIVE_SHA256=""
if command -v sha256sum >/dev/null 2>&1; then
    ARCHIVE_SHA256=$(sha256sum "${CANONICAL_ARCHIVE}" | awk '{print $1}')
else
    ARCHIVE_SHA256=$(shasum -a 256 "${CANONICAL_ARCHIVE}" | awk '{print $1}')
fi

# Step 4: create symlink in repo root
SYMLINK_PATH="${ROOT_DIR}/UPLOAD_THIS.zip"
rm -f "${SYMLINK_PATH}"
ln -s "${CANONICAL_ARCHIVE}" "${SYMLINK_PATH}"
log_pass "Created symlink: ${SYMLINK_PATH} → ${CANONICAL_ARCHIVE}"

echo ""
echo "========================================"
echo "  UPLOAD FILE READY"
echo "========================================"
echo ""
log_bold "UPLOAD ONLY THIS EXACT FILE:"
echo ""
echo "  ${UPLOAD_TARGET}"
echo ""
log_bold "OR use the symlink in the repo root:"
echo ""
echo "  ${SYMLINK_PATH}"
echo ""
log_bold "Archive SHA-256:"
echo ""
echo "  ${ARCHIVE_SHA256}"
echo ""
echo "========================================"
log_bold "DO NOT UPLOAD:"
echo "  - Any file named JUDGE_ATLASX-main-master*.zip"
echo "  - Any source snapshot or git-export ZIP"
echo "  - Any ZIP containing .env.example files"
echo "  - Any ZIP with root folder other than JUDGE_ATLAS-main/"
echo "========================================"
