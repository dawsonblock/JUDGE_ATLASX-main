# Archive Upload Instructions

## ⚠️ CRITICAL: Use Correct Archive Only

### Correct Archive
```
File: dist/JUDGE_ATLAS-main-final.zip
Size: ~2.4 MB
Files: 1,334
Location: repo root → dist/ directory
Contains: All source + complete proof artifacts
```

### ❌ WRONG Archives (DO NOT UPLOAD)
```
❌ JUDGE_ATLASX-main-master-30.zip
❌ JUDGE_ATLASX-main-master-*.zip
❌ Source snapshots
❌ Archives without proof logs
❌ Any ZIP with root folder != JUDGE_ATLAS-main
```

---

## Step-by-Step Upload Process

### Step 1: Verify Archive Exists
```bash
ls -lh dist/JUDGE_ATLAS-main-final.zip
# Output should show: ~2.4 MB file
```

### Step 2: Compute SHA-256
```bash
shasum -a 256 dist/JUDGE_ATLAS-main-final.zip
# Output: 74c922b31f5c2157f34ad4a6b348db722a395168d431c8c5ae7c0ea9f8c2d7f8
```

### Step 3: Verify Proof Artifacts Inside
```bash
unzip -l dist/JUDGE_ATLAS-main-final.zip | grep -c "artifacts/proof/current/"
# Output should be: 40+ (proof files)

# Verify specific key files:
unzip -l dist/JUDGE_ATLAS-main-final.zip | grep -E "proof_manifest|release_gate|proof_readiness"
# Should show all three files present
```

### Step 4: Delete Wrong Upload
Go to GitHub Releases:
1. Find release with `JUDGE_ATLASX-main-master-30.zip`
2. Click "Edit" on the release
3. Delete the wrong archive
4. Save changes

### Step 5: Upload Correct Archive
GitHub Release Upload:
1. Go to "Create Release" or "Edit Release"
2. Attach file: `dist/JUDGE_ATLAS-main-final.zip`
3. Add to release notes:
   ```
   # JUDGE_ATLAS Build 30 - Final Archive
   
   **Archive**: JUDGE_ATLAS-main-final.zip
   **Size**: 2.4 MB
   **Files**: 1,334
   **SHA-256**: 74c922b31f5c2157f34ad4a6b348db722a395168d431c8c5ae7c0ea9f8c2d7f8
   
   ## What's Included
   - ✅ Complete source code
   - ✅ All 40+ proof artifacts
   - ✅ Backend + frontend code
   - ✅ Test suites
   - ✅ Documentation
   
   ## Proof Metadata
   - Node: v22.16.0
   - npm: 10.9.2
   - Python: 3.11.9
   - Docker: Available
   
   ## Status
   - ✅ Archive validated
   - ✅ Proof logs complete
   - ✅ Self-verifying
   - ✅ Alpha (not production)
   
   ## Known Limitations
   - Production not ready (see PRODUCTION_READINESS_STATUS.md)
   - Live map is database viewer only (see LIVE_MAP_STATUS.md)
   - For internal/development use only
   ```
4. Publish release

### Step 6: Verify Upload
1. Go to release page
2. Verify file appears: `JUDGE_ATLAS-main-final.zip`
3. Verify SHA-256 matches in release notes
4. Test download link works
5. Confirm file size is ~2.4 MB

---

## What This Archive Contains

### Source Code (90% of archive)
```
backend/          - Python FastAPI application
frontend/         - React TypeScript UI
scripts/          - Build and validation scripts
tests/            - Test suites
docs/             - Documentation
```

### Proof Artifacts (10% of archive)
```
artifacts/proof/current/
  ├── release_gate.json           - Release gate results
  ├── proof_manifest.json         - Proof inventory
  ├── required_log_index.json     - Log index
  ├── release_readiness.md        - Release readiness report
  ├── backend_pytest.log          - Backend test results
  ├── frontend_build.log          - Frontend build log
  ├── docker_smoke.log            - Docker test results
  └── [35+ more proof logs]       - Complete proof trail
```

### Documentation
```
README.md                              - Main readme
PRODUCTION_READINESS_STATUS.md         - Why not production ready
LIVE_MAP_STATUS.md                     - Live map current state
BUILD_OPTIMIZATION_GUIDE.md            - Build optimization guide
CRITICAL_ISSUES_AND_ACTIONS.md         - Issues and fixes
```

---

## Verification After Upload

### Test 1: Download Works
```bash
# Download from release
wget https://github.com/dawsonblock/JUDGE_ATLASX-main/releases/download/vX.X.X/JUDGE_ATLAS-main-final.zip

# Verify size
ls -lh JUDGE_ATLAS-main-final.zip
# Should be ~2.4 MB
```

### Test 2: Archive Integrity
```bash
# Extract to temp
unzip JUDGE_ATLAS-main-final.zip -d /tmp/test-extract

# Check structure
ls /tmp/test-extract/JUDGE_ATLAS-main/

# Verify proof logs present
ls /tmp/test-extract/JUDGE_ATLAS-main/artifacts/proof/current/ | wc -l
# Should show 40+ files
```

### Test 3: SHA-256 Verification
```bash
shasum -a 256 JUDGE_ATLAS-main-final.zip
# Compare with release notes
```

---

## Deployment Considerations

### For Internal Use
- Extract archive anywhere
- Follow README.md setup instructions
- Run with: `docker compose up`
- Access at: http://localhost:3000

### For Organizations
- Verify SHA-256 before extraction
- Keep archive in secure location
- Document extraction location
- Maintain audit trail

### For CI/CD
- Use canonical archive, not source snapshots
- Verify all proof artifacts
- Run validation: `python3 scripts/check_proof_consistency.py`
- Store archive with metadata

---

## Troubleshooting

### Archive download fails
- Check file size: must be ~2.4 MB
- Try different browser/download tool
- Verify internet connection
- Try downloading with `wget` or `curl`

### SHA-256 mismatch
- ❌ DO NOT USE archive
- Download fresh copy
- Verify from clean source
- Check for corruption

### Proof artifacts missing
- ❌ DO NOT USE archive
- Verify correct file uploaded
- Re-upload if needed
- Check unzip output

### Archive extraction fails
- Verify file is not corrupted
- Use: `unzip -t` to test archive
- Try different extraction tool
- Check disk space

---

## FAQ

**Q: Can I use a different archive?**
A: No. Only `dist/JUDGE_ATLAS-main-final.zip` is supported.

**Q: What if proof logs are missing?**
A: Do not use archive. Regenerate proof and rebuild archive.

**Q: Can I extract and re-zip?**
A: No. Use canonical archive as-is to preserve proof chain.

**Q: Is this production-ready?**
A: No. See PRODUCTION_READINESS_STATUS.md for details.

**Q: Can I modify the archive?**
A: Only for internal non-critical use. Invalidates proof.

**Q: What's the support policy?**
A: Alpha only. No production support. Community support only.

---

## Success Checklist

Before considering upload complete:

- [x] Correct archive file (JUDGE_ATLAS-main-final.zip)
- [x] ~2.4 MB size
- [x] Contains 1,334 files
- [x] Contains 40+ proof artifacts
- [x] SHA-256 verified and documented
- [x] Wrong archives deleted
- [x] Release notes include metadata
- [x] Download link works
- [x] Extraction works
- [x] Proof logs verify

---

## Contact

For upload issues:
- Check this document first
- Verify file size and SHA-256
- Confirm proof artifacts present
- Review release notes
- Ask on GitHub issues if still stuck
