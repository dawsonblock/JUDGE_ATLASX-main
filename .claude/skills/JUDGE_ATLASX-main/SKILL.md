```markdown
# JUDGE_ATLASX-main Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill provides guidance on contributing to the `JUDGE_ATLASX-main` TypeScript codebase. It covers coding conventions, artifact management workflows, and testing patterns to ensure consistency and maintainability. The repository focuses on proof artifact tracking and verification, with regular maintenance workflows to keep proof status up-to-date.

## Coding Conventions

### File Naming
- Use **snake_case** for all file names.
  - Example: `proof_policy.ts`, `source_registry_status.ts`

### Import Style
- Use **relative imports** for modules within the project.
  ```typescript
  import { verifyProof } from './proof_utils';
  ```

### Export Style
- Use **named exports** for all modules.
  ```typescript
  // In proof_utils.ts
  export function verifyProof() { ... }

  // In another file
  import { verifyProof } from './proof_utils';
  ```

### Commit Message Patterns
- Prefix commits with context such as `fix`, `proof`, etc.
  - Example: `fix: correct proof artifact path resolution`
  - Example: `proof: update verification report generation logic`
- Aim for descriptive commit messages (average ~88 characters).

## Workflows

### Proof Artifact Reset and Cleanup
**Trigger:** When preparing for a new proof cycle, release, or after proof regeneration to ensure only current and relevant proof artifacts are present.  
**Command:** `/reset-proof-artifacts`

1. **Update release configuration**  
   Edit `.releaseignore` (or similar) to exclude unnecessary files from release artifacts.
   ```diff
   # .releaseignore
   artifacts/proof/current/*
   !artifacts/proof/current/CURRENT_PROOF.md
   ```
2. **Truncate or reset in-progress proof artifact stubs**  
   Clear or reset files such as:
   - `artifacts/proof/current/CURRENT_PROOF.md`
   - `artifacts/proof/current/FIX_VERIFICATION_REPORT.md`
   - `artifacts/proof/current/SOURCE_REGISTRY_STATUS.md`
3. **Remove or regenerate completed or stale proof artifacts**  
   Delete or regenerate files like:
   - `artifacts/proof/current/backend_pytest_batch_X.xml`
   - `artifacts/proof/current/PROOF_POLICY.md`
   - `artifacts/proof/current/archive_validation.md`
   - Proof summaries and manifest files
4. **Update documentation and generated status files**  
   Refresh documentation and summary files to reflect the current proof state:
   - `docs/CURRENT_ALPHA_STATUS.md`
   - `docs/PROOF_POLICY.md`
   - `docs/generated/PROOF_SUMMARY.md`
   - `docs/generated/RELEASE_STATUS.md`
   - `docs/source-governance/COVERAGE_MATRIX.md`

**Files Involved:**
- `.releaseignore`
- `artifacts/proof/current/*`
- `docs/*`
- `docs/generated/*`
- `docs/source-governance/COVERAGE_MATRIX.md`

**Frequency:** Approximately 2 times per month.

## Testing Patterns

- **Test Framework:** Unknown (no framework detected).
- **Test File Pattern:** Files named with `.test.` in the filename.
  - Example: `proof_utils.test.ts`
- **Test Example:**
  ```typescript
  // proof_utils.test.ts
  import { verifyProof } from './proof_utils';

  test('verifyProof returns true for valid proof', () => {
    expect(verifyProof(validProof)).toBe(true);
  });
  ```

## Commands

| Command                | Purpose                                                        |
|------------------------|----------------------------------------------------------------|
| /reset-proof-artifacts | Reset and clean up proof artifacts for a new proof cycle/release |

```