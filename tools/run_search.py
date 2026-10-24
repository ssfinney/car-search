#!/usr/bin/env python3
"""Main search runner and candidate generator CLI.

Orchestrates:
1. Listing discovery across Auto.dev / MarketCheck / local listing feeds.
2. Screening against criteria (no white exterior, mileage, price, trim).
3. Deduplication against candidates/ and eliminated/.
4. NHTSA chain (vPIC decode, recalls, complaints pattern signals).
5. Generation of candidate markdown files in candidates/ with status 'lead'.
"""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from tools.candidate_generator import write_candidate_file
from tools.dedupe import find_repo_root, is_duplicate, load_existing_vins
from tools.nhtsa import run_nhtsa_chain
from tools.search import (
    DEFAULT_RADIUS,
    MACON_ZIP,
    SEARCH_TARGETS,
    WIDENED_RADIUS,
    TargetSpec,
    load_listings_from_json,
    passes_screening,
    query_autodev,
    query_marketcheck,
)


def process_listing(
    listing: Dict[str, Any],
    spec: Optional[TargetSpec],
    existing_vins: Dict[str, dict],
    repo_root: Path,
    dry_run: bool = False,
) -> Optional[Path]:
    """Process a single listing: screening -> dedupe -> NHTSA chain -> file write."""
    vin = (listing.get("vin") or "").strip().upper()
    title = f"{listing.get('year')} {listing.get('make')} {listing.get('model')} {listing.get('trim')}"

    # 1. Screening
    passed, reason = passes_screening(listing, spec)
    if not passed:
        print(f"  [SCREEN REJECT] {title} (VIN: {vin or 'none'}): {reason}")
        return None

    # 2. Dedupe
    if vin and len(vin) == 17:
        dup, match = is_duplicate(vin, existing_vins=existing_vins, repo_dir=repo_root)
        if dup and match:
            print(f"  [DEDUPE SKIP] {title} (VIN: {vin}): already in {match['file']} ({match['dir']})")
            return None
    elif not vin:
        print(f"  [WARN] Listing missing VIN: {title} ({listing.get('dealer', 'unknown')})")

    # 3. NHTSA Chain
    nhtsa_data = None
    if vin and len(vin) == 17:
        print(f"  [NHTSA] Running chain for VIN: {vin}...")
        nhtsa_data = run_nhtsa_chain(vin)
        vpic = nhtsa_data.get("vpic", {})
        # Enrich listing with decoded details if missing
        if not listing.get("make") and vpic.get("make"):
            listing["make"] = vpic["make"]
        if not listing.get("model") and vpic.get("model"):
            listing["model"] = vpic["model"]
        if not listing.get("year") and vpic.get("year"):
            listing["year"] = vpic["year"]
        if not listing.get("trim") and vpic.get("trim"):
            listing["trim"] = vpic["trim"]
        if not listing.get("drivetrain") and vpic.get("drive_type"):
            listing["drivetrain"] = vpic["drive_type"]

    # 4. Generate candidate file
    if dry_run:
        print(f"  [DRY RUN] Would file candidate: {title} (VIN: {vin})")
        return None

    try:
        out_path = write_candidate_file(listing, nhtsa_data=nhtsa_data, repo_dir=repo_root)
        print(f"  [FILED LEAD] Created candidate file: {out_path.relative_to(repo_root)}")
        # Update in-memory dedupe registry
        if vin and len(vin) == 17:
            existing_vins[vin] = {
                "vin": vin,
                "file": str(out_path.relative_to(repo_root)),
                "dir": "candidates",
                "status": "lead",
                "title": title,
            }
        return out_path
    except Exception as exc:
        print(f"  [ERROR] Failed to write candidate for {title}: {exc}", file=sys.stderr)
        return None


def run_search(
    targets: List[TargetSpec],
    zip_code: str = MACON_ZIP,
    radius: int = DEFAULT_RADIUS,
    max_price: int = 30000,
    max_miles: int = 95000,
    feed_path: Optional[Path] = None,
    dry_run: bool = False,
    repo_dir: Optional[Path] = None,
) -> List[Path]:
    """Run search across configured targets and sources."""
    root = find_repo_root(repo_dir)
    existing_vins = load_existing_vins(root)
    print(f"Loaded {len(existing_vins)} existing VINs for deduplication.")

    autodev_key = os.environ.get("AUTODEV_API_KEY", "").strip()
    marketcheck_key = os.environ.get("MARKETCHECK_API_KEY", "").strip()

    filed_files: List[Path] = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n--- Search Run: {timestamp} ---")
    print(f"Origin: {zip_code} (Macon, GA) | Radius: {radius} mi | Price ceiling: ${max_price:,} | Max miles: {max_miles:,}")
    print(f"APIs configured: Auto.dev: {'YES' if autodev_key else 'NO'}, MarketCheck: {'YES' if marketcheck_key else 'NO'}")

    # Case 1: Ingesting from local feed or scraper export
    if feed_path:
        print(f"\nReading listings from feed: {feed_path}")
        listings = load_listings_from_json(feed_path)
        print(f"Found {len(listings)} raw listing records in feed.")
        for item in listings:
            res = process_listing(item, spec=None, existing_vins=existing_vins, repo_root=root, dry_run=dry_run)
            if res:
                filed_files.append(res)
        return filed_files

    # Case 2: Querying APIs
    if not autodev_key and not marketcheck_key:
        print("\nNotice: Neither AUTODEV_API_KEY nor MARKETCHECK_API_KEY is set in environment.")
        print("To query online listing APIs, set AUTODEV_API_KEY or MARKETCHECK_API_KEY.")
        print("You can also run search with a feed file: python -m tools.run_search --feed <path.json>")
        return []

    for spec in targets:
        print(f"\nSearching for target: {spec.name} ({spec.category})")
        listings: List[Dict[str, Any]] = []

        if autodev_key:
            print(f"  Querying Auto.dev for {spec.make} {spec.model}...")
            ad_results = query_autodev(
                spec,
                api_key=autodev_key,
                zip_code=zip_code,
                radius=radius,
                max_price=max_price,
                max_miles=max_miles,
            )
            print(f"  Received {len(ad_results)} results from Auto.dev.")
            listings.extend(ad_results)

        if marketcheck_key:
            print(f"  Querying MarketCheck for {spec.make} {spec.model}...")
            mc_results = query_marketcheck(
                spec,
                api_key=marketcheck_key,
                zip_code=zip_code,
                radius=radius,
                max_price=max_price,
                max_miles=max_miles,
            )
            print(f"  Received {len(mc_results)} results from MarketCheck.")
            listings.extend(mc_results)

        # Process each result
        for item in listings:
            res = process_listing(item, spec=spec, existing_vins=existing_vins, repo_root=root, dry_run=dry_run)
            if res:
                filed_files.append(res)

    print(f"\nSearch complete: {len(filed_files)} new candidate lead(s) filed.")
    return filed_files


def main() -> int:
    parser = argparse.ArgumentParser(description="Three-row SUV frontier search runner.")
    parser.add_argument("--zip", default=MACON_ZIP, help=f"Origin ZIP code (default: {MACON_ZIP})")
    parser.add_argument("--radius", type=int, default=DEFAULT_RADIUS, help=f"Search radius in miles (default: {DEFAULT_RADIUS})")
    parser.add_argument("--widen", action="store_true", help=f"Widen radius to {WIDENED_RADIUS} miles")
    parser.add_argument("--max-price", type=int, default=30000, help="Max vehicle price (default: 30000)")
    parser.add_argument("--max-miles", type=int, default=95000, help="Max mileage (default: 95000, widen to 110000)")
    parser.add_argument("--feed", type=Path, help="Path to JSON feed of listings to ingest")
    parser.add_argument("--vin", help="Ingest a specific vehicle VIN as a candidate lead")
    parser.add_argument("--dealer", default="", help="Dealer name when ingesting single VIN")
    parser.add_argument("--city", default="", help="Dealer city when ingesting single VIN")
    parser.add_argument("--state", default="GA", help="Dealer state when ingesting single VIN")
    parser.add_argument("--price", type=float, help="Listing price when ingesting single VIN")
    parser.add_argument("--miles", type=int, help="Listing mileage when ingesting single VIN")
    parser.add_argument("--color", default="", help="Listing exterior color when ingesting single VIN")
    parser.add_argument("--url", default="", help="Listing URL when ingesting single VIN")
    parser.add_argument("--dry-run", action="store_true", help="Screen and test without writing files")

    args = parser.parse_args()
    radius = WIDENED_RADIUS if args.widen else args.radius

    if args.vin:
        # Ingest single VIN
        root = find_repo_root()
        existing = load_existing_vins(root)
        listing = {
            "vin": args.vin.strip().upper(),
            "dealer": args.dealer,
            "city": args.city,
            "state": args.state,
            "price": args.price,
            "miles": args.miles,
            "color": args.color,
            "url": args.url,
        }
        res = process_listing(listing, spec=None, existing_vins=existing, repo_root=root, dry_run=args.dry_run)
        return 0 if res or args.dry_run else 1

    run_search(
        targets=SEARCH_TARGETS,
        zip_code=args.zip,
        radius=radius,
        max_price=args.max_price,
        max_miles=args.max_miles,
        feed_path=args.feed,
        dry_run=args.dry_run,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
