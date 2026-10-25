#!/usr/bin/env python3
"""Deduplication utility for candidate vehicle VINs.

Scans candidates/ and eliminated/ to extract existing VINs and prevent duplicate filings.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, Optional, Tuple

VIN_REGEX = re.compile(r"\b[A-HJ-NPR-Z0-9]{17}\b", re.IGNORECASE)


def find_repo_root(start_path: Optional[Path] = None) -> Path:
    current = (start_path or Path.cwd()).resolve()
    for parent in [current, *current.parents]:
        if (parent / "PROTOCOL.md").exists() and (parent / "candidates").is_dir():
            return parent
    return current


def extract_vins_from_text(text: str) -> set[str]:
    """Extract all valid 17-character VINs from text."""
    # Match standard 17-character VINs (excluding I, O, Q)
    candidates = VIN_REGEX.findall(text)
    return {c.upper() for c in candidates}


def load_existing_vins(repo_dir: Optional[Path] = None) -> Dict[str, dict]:
    """Scan candidates/ and eliminated/ for recorded VINs.

    Returns a mapping of VIN -> {file, dir, status, title}.
    """
    root = find_repo_root(repo_dir)
    results: Dict[str, dict] = {}

    target_dirs = [root / "candidates", root / "eliminated"]
    for directory in target_dirs:
        if not directory.is_dir():
            continue
        for md_file in directory.glob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8")
            except OSError:
                continue

            # Extract title and status if present
            title = ""
            status = ""
            for line in content.splitlines():
                if line.startswith("# ") and not title:
                    title = line.lstrip("# ").strip()
                elif line.lower().startswith("- **status:**"):
                    status = line.split(":", 1)[1].strip()

            vins = extract_vins_from_text(content)
            for vin in vins:
                # Avoid storing placeholder / non-VIN strings if regex caught them
                if len(vin) == 17:
                    results[vin] = {
                        "vin": vin,
                        "file": str(md_file.relative_to(root)),
                        "dir": directory.name,
                        "status": status,
                        "title": title,
                    }
    return results


def is_duplicate(
    vin: str,
    existing_vins: Optional[Dict[str, dict]] = None,
    repo_dir: Optional[Path] = None,
) -> Tuple[bool, Optional[dict]]:
    """Check if a VIN is already in candidates/ or eliminated/."""
    clean_vin = vin.strip().upper()
    if existing_vins is None:
        existing_vins = load_existing_vins(repo_dir)
    if clean_vin in existing_vins:
        return True, existing_vins[clean_vin]
    return False, None


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python -m tools.dedupe <VIN> [repo_path]", file=sys.stderr)
        existing = load_existing_vins()
        print(f"Loaded {len(existing)} existing VIN(s) from repo:")
        for v, meta in sorted(existing.items()):
            print(f"  {v}: {meta['file']} ({meta['dir']}, status: {meta['status']})")
        return 0

    target_vin = sys.argv[1].strip().upper()
    repo_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    dup, match = is_duplicate(target_vin, repo_dir=repo_path)
    if dup and match:
        print(f"DUPLICATE: VIN {target_vin} already recorded in {match['file']} ({match['dir']})")
        return 1
    else:
        print(f"CLEAN: VIN {target_vin} is new.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
