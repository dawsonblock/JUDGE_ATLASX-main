#!/usr/bin/env python3
"""Aggregate status-consistency checks for release truth alignment."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


CHECKS = (
    (
        "verify_status_consistency",
        ["python3", "scripts/verify_status_consistency.py", "--root", "."],
    ),
    (
        "check_status_truth_consistency",
        [
            "python3",
            "scripts/check_status_truth_consistency.py",
            "--root",
            ".",
        ],
    ),
)


def _run(cmd: list[str], cwd: Path) -> tuple[int, str]:
    cp = subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )
    output = "\n".join(
        part for part in (cp.stdout.strip(), cp.stderr.strip()) if part
    )
    return cp.returncode, output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root")
    args = parser.parse_args()

    repo_root = Path(args.root).resolve()
    failures: list[tuple[str, int, str]] = []

    for name, cmd in CHECKS:
        rc, output = _run(cmd, cwd=repo_root)
        if rc != 0:
            failures.append((name, rc, output))

    if failures:
        print(f"STATUS_CONSISTENCY: FAIL ({len(failures)} checks failed)")
        for name, rc, output in failures:
            print(f"- {name}: rc={rc}")
            if output:
                print(output)
        return 1

    print("STATUS_CONSISTENCY: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
