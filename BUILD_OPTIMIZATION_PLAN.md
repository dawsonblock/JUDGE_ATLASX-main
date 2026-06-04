# Build Optimization Analysis & Recommendations

## Current Build Profile (18 minutes)

Based on analysis of `build_for_upload.sh` and `release_gate.py`:

### Sequential Phases:
1. **check_toolchain_versions** - ~5s
2. **release_gate.py** - ~13-15 minutes
   - Frontend build: ~4-5 min
   - Backend pytest: ~6-7 min (787 tests in batches)
   - Docker proofs: ~1-2 min
   - Other gates: ~1-2 min
3. **package_and_validate_release_archive.sh** - ~2-3 min
4. **verify_upload_ready.sh** - ~30s

### Identified Bottlenecks:

#### 1. Backend Pytest (6-7 minutes, 40% of total)
- 787 tests run sequentially in 8 batches
- Each batch size = 100 tests (configurable)
- Pytest overhead per batch: ~500ms
- **Optimization**: Increase batch size or parallelize

#### 2. Frontend Build (4-5 minutes, 25% of total)
- Full Next.js build from scratch each time
- Includes type checking, linting, build
- No incremental builds or caching
- **Optimization**: Skip build if sources unchanged, parallel tasks

#### 3. Docker Proofs (1-2 minutes, 10% of total)
- docker_smoke: starts full stack, 180s timeout
- postgis_proof: PostGIS container startup
- Both are sequential
- **Optimization**: Parallelize with backend tests or skip in CI

#### 4. Archive Operations (2-3 minutes, 15% of total)
- Full re-extraction and validation each time
- Multiple redundant checks
- **Optimization**: Combine validation passes

## Recommended Optimizations

### HIGH PRIORITY (2-4 min savings)

#### A. Increase Backend Test Batch Size
- Current: batch_size=100, 8 batches
- Proposal: batch_size=200, 4 batches
- Savings: ~1-1.5 min
- Risk: Memory pressure, test isolation issues
- Implementation: Update `release_gate.py` line ~2500

#### B. Skip Docker Proofs in Quick Mode
- Current: docker_smoke + postgis_proof always run
- Proposal: Environment variable JTA_QUICK_BUILD=1 to skip
- Savings: ~1-2 min
- Risk: Missing Docker validation (accept for CI)
- Implementation: Add conditional in release_gate.py

#### C. Parallelize Frontend + Backend
- Current: backend pytest waits for frontend
- Proposal: Launch frontend build in background, run tests in parallel
- Savings: ~0.5-1 min
- Risk: Resource contention, flaky tests
- Implementation: Fork frontend task before backend_pytest

### MEDIUM PRIORITY (1-2 min savings)

#### D. Skip Redundant Archive Validation
- Current: 3 separate extraction/validation passes
- Proposal: Single validation pass with cached results
- Savings: ~0.5-1 min
- Risk: Missing validation edge cases
- Implementation: Combine validation scripts

#### E. Cache Node Dependencies
- Current: npm ci every build
- Proposal: Skip if node_modules hash unchanged
- Savings: ~0.5 min
- Risk: Stale dependencies
- Implementation: Check package-lock.json hash

#### F. Parallel Gate Steps
- Current: gates run sequentially (40+ steps)
- Proposal: Parallelize non-blocking gates
- Savings: ~1-2 min
- Risk: Race conditions, log pollution
- Implementation: Python multiprocessing in release_gate.py

### LOW PRIORITY (30s-1 min savings)

#### G. Skip Linting/Type Checks
- Current: frontend lint + typecheck run
- Proposal: Skip in build-for-upload (faster)
- Savings: ~0.5 min
- Risk: Missing errors
- Implementation: Make skip-checks flag

#### H. Precompile Python
- Current: Python files compiled on first import
- Proposal: Pre-compile .py → .pyc before tests
- Savings: ~0.3 min
- Risk: Obsolete bytecode
- Implementation: compileall on backend dir

## Recommended Implementation Order

### Phase 1: Immediate (5 min → 3-4 min)
1. Add JTA_QUICK_BUILD mode to skip Docker proofs
2. Increase backend batch size to 200
3. Parallelize frontend build with backend pytest

**Expected savings: 3-4 minutes**

### Phase 2: Medium-term (3-4 min → 2-3 min)
4. Parallelize non-blocking gate steps
5. Cache frontend build outputs
6. Combine archive validation passes

**Expected savings: 1-1.5 minutes**

### Phase 3: Long-term (2-3 min → 1-2 min)
7. Refactor release_gate.py for better parallelization
8. Implement incremental proof building
9. Add distributed test running (pytest-xdist)

**Expected savings: 0.5-1 minute**

## Implementation Details

### A. Quick Build Mode
```bash
# Add to release_gate.py
if os.getenv("JTA_QUICK_BUILD") == "1":
    # Skip docker_smoke, postgis_proof, resource-intensive gates
    gate_steps = [g for g in gate_steps if g.name not in [
        "docker_smoke", "postgis_proof", ...
    ]]
```

### B. Larger Batch Size
```bash
# In run_backend_tests_chunked.py
default_batch_size = int(os.getenv("JTA_PYTEST_BATCH_SIZE", "200"))
```

### C. Parallel Frontend Build
```bash
# In build_for_upload.sh or release_gate.py
# Launch frontend build in background
(npm run build --prefix frontend &) 
# Then run backend tests
python -m pytest ...
wait  # Wait for frontend to finish
```

## Testing the Optimizations

### Before/After Timing
```bash
# Baseline (current)
time make build-for-upload

# With JTA_QUICK_BUILD=1 (skip Docker)
time JTA_QUICK_BUILD=1 bash scripts/build_for_upload.sh

# With larger batch size
time JTA_PYTEST_BATCH_SIZE=200 make build-for-upload

# With parallelization
time bash scripts/build_for_upload_parallel.sh
```

## Risk Assessment

| Optimization | Risk Level | Mitigation |
|---|---|---|
| Batch size 200 | MEDIUM | Monitor memory, add fallback |
| Skip Docker | HIGH | Only in CI, use flag |
| Parallelize tests | HIGH | Add serialization lock |
| Cache frontend | MEDIUM | Hash validation, fallback |
| Parallel gates | HIGH | Careful ordering, logging |

## Recommendation

**Start with Phase 1** (Docker skip + batch size):
- Low risk
- 3-4 minute savings
- Minimal code changes
- Can be reverted easily

**Use for CI/CD** (not local development):
- Set `JTA_QUICK_BUILD=1` in CI pipelines
- Keep full build for releases
- Use caching for repeated builds

