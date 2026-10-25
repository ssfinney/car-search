#!/usr/bin/env python3
"""Candidate vehicle markdown file generator.

Produces candidate records conforming strictly to PARETO_GUIDE.md Section 6,
setting status to 'lead' per PROTOCOL.md.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any, Dict, Optional
from tools.dedupe import find_repo_root, is_duplicate
from tools.nhtsa import format_nhtsa_summary, run_nhtsa_chain


def slugify(text: str) -> str:
    """Generate a filename-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")


def generate_candidate_slug(listing: Dict[str, Any]) -> str:
    """Generate a standard candidate filename slug: <dealer-or-city>-<year>-<model>-<trim>."""
    city = listing.get("city") or ""
    dealer = listing.get("dealer") or ""
    prefix = slugify(city) or slugify(dealer) or "dealer"
    year = str(listing.get("year", ""))
    model = slugify(str(listing.get("model", "")))
    trim = slugify(str(listing.get("trim", "")))

    parts = [p for p in [prefix, year, model, trim] if p]
    return "-".join(parts)


def format_currency(val: Any) -> str:
    if val is None or val == "":
        return "Unlisted"
    try:
        num = float(val)
        return f"${num:,.0f}"
    except (ValueError, TypeError):
        return str(val)


def generate_candidate_markdown(
    listing: Dict[str, Any],
    nhtsa_data: Optional[Dict[str, Any]] = None,
    today_str: Optional[str] = None,
) -> str:
    """Generate candidate markdown content with required PARETO_GUIDE.md §6 table."""
    today = today_str or date.today().isoformat()

    vin = listing.get("vin", "").strip().upper()
    year = str(listing.get("year", "")).strip()
    make = str(listing.get("make", "")).strip()
    model = str(listing.get("model", "")).strip()
    trim = str(listing.get("trim", "")).strip()
    drivetrain = str(listing.get("drivetrain") or listing.get("drive_type") or "FWD/AWD").strip()
    dealer = str(listing.get("dealer", "")).strip() or "Dealer"
    city = str(listing.get("city", "")).strip()
    state = str(listing.get("state", "GA")).strip()
    listing_url = str(listing.get("url", "")).strip()
    price = listing.get("price")
    price_str = format_currency(price)
    miles = listing.get("miles") or listing.get("mileage")
    miles_str = f"{int(miles):,}" if miles and str(miles).isdigit() else (str(miles) if miles else "Unlisted")
    color = str(listing.get("color") or listing.get("exterior_color") or "Not recorded").strip()

    captains = listing.get("captains_chairs") or "Configuration match (photo confirmation pending by Claude)"
    liftgate = listing.get("power_liftgate") or "Equipped per trim/options (confirmation pending)"
    owners = listing.get("owners", "Check pending")
    prior_use = listing.get("prior_use", "Personal / commercial check pending")
    reason = listing.get("reason_survives") or (
        f"Fits Pareto search frontier: {year} {make} {model} {trim} within mileage and budget criteria."
    )
    transport = listing.get("transport") or "Local / within radius (Macon origin)"

    location_str = f"{dealer}, {city} {state}".strip(", ")

    # Run NHTSA chain if not provided and VIN is present
    if not nhtsa_data and len(vin) == 17:
        nhtsa_data = run_nhtsa_chain(vin)

    nhtsa_summary = ""
    recalls_summary = "NHTSA check pending"
    if nhtsa_data:
        nhtsa_summary = format_nhtsa_summary(nhtsa_data)
        recalls = nhtsa_data.get("recalls", {})
        if recalls.get("status") == "error" or recalls.get("count") is None:
            recalls_summary = f"NHTSA recalls lookup failed ({recalls.get('error', 'API error')}); re-check required"
        else:
            count = recalls.get("count", 0)
            c_ids = [c.get("campaign_number") for c in recalls.get("campaigns", []) if c.get("campaign_number")]
            if c_ids:
                recalls_summary = f"{count} model-year campaigns ({', '.join(c_ids)}); VIN-specific completion pending"
            else:
                recalls_summary = "0 open campaigns for model year; VIN-specific completion check pending"

    title_header = f"{year} {make} {model} {trim}".strip()
    if drivetrain:
        title_header += f" {drivetrain}"
    title_header += f" — {location_str}"

    reported_fee = listing.get("dealer_fees") or listing.get("fees")
    if reported_fee:
        fee_str = format_currency(reported_fee)
        price_fee_label = f"+{fee_str} fee reported"
        table_fee_label = f"{fee_str} reported by listing source; written quote required for full breakdown"
        notes_fee_label = f"{fee_str} reported by source, but unconditional written quote is required."
    else:
        price_fee_label = "dealer fees unverified"
        table_fee_label = "Unverified (not returned by listing source; written quote required)"
        notes_fee_label = "Unverified; not returned by listing source."

    lines = [
        f"# {title_header}",
        "",
        "- **Status:** lead",
        f"- **Dealer/location:** {location_str}",
        f"- **Listing:** {listing_url if listing_url else 'Direct dealer find'}",
        f"- **Price:** {price_str} ({price_fee_label})",
        f"- **Mileage:** {miles_str}",
        f"- **Color:** {color}",
        f"- **Captain's chairs:** {captains}",
        f"- **Power liftgate:** {liftgate}",
        f"- **VIN:** {vin if vin else 'not recorded'}",
    ]

    if nhtsa_summary:
        lines.append(nhtsa_summary)

    lines.extend([
        "",
        "## Required listing record (PARETO_GUIDE.md §6)",
        "",
        "| Field | Entry |",
        "|---|---|",
        f"| Listing URL / dealer / date | [{listing_url}]({listing_url}) / {location_str} / {today} |",
        f"| VIN / year / trim / drivetrain / color | {vin} / {year} / {trim} / {drivetrain} / {color} |",
        f"| Captain’s chairs / power liftgate confirmed | {captains} / {liftgate} |",
        f"| Mileage / owners / prior use | {miles_str} miles / {owners} / {prior_use} |",
        "| Title, accident, flood, structural history | Adverse history check pending (Muse handoff) |",
        "| Service records and gaps | History report pending (Muse handoff) |",
        f"| Open recalls and completion documentation | {recalls_summary} |",
        f"| Vehicle price | {price_str} |",
        f"| Dealer fees and mandatory packages | {table_fee_label} |",
        "| Taxes / title / registration | Unverified (dealer actual Georgia TAVT calculation required) |",
        f"| Transport / travel | {transport} |",
        "| Written OTD total, with financing conditions | Pending written quote from dealer |",
        "| Independent inspection findings | Mandatory gate before deposit (Canton rule) |",
        "| Immediate maintenance estimate | Pending inspection and service history |",
        "| Effective acquisition cost: OTD + immediate work | Pending written OTD + inspection |",
        "| Down payment / retained cash / monthly payment | Default: $17,000 down / $2,000 retained / target $200–250/mo (60 mo @ 6%) |",
        f"| Reason it survives against the other candidates | {reason} |",
        "",
        "## Notes",
        "",
        f"- Discovered via CLI search tooling on {today}.",
        f"- Dealer fees: {notes_fee_label}",
        "- Second-row captain's chairs and exterior color require photo verification before travel/evaluation.",
        "",
        "## Open gates / next steps",
        "",
        "- Dealer call: verify vehicle availability, confirm fees, and request written unconditional OTD quote.",
        "- Muse VIN/recall check and dealer-site CARFAX capture (advances status to `vin-checked`).",
        "- Claude captain's-chair image confirmation at evaluation.",
        "- Independent PPI before any deposit (Canton rule).",
        "",
        "## Log",
        "",
        f"- {today} — Filed as `lead` by CLI search tooling.",
        "",
    ])

    return "\n".join(lines)


def validate_listing_evidence(listing: Dict[str, Any]) -> None:
    """Validate that real listing evidence is provided.

    Rejects candidate generation when essential listing evidence is missing
    or contains placeholders, per PROTOCOL.md.
    """
    missing = []
    vin = str(listing.get("vin", "")).strip()
    if not vin or len(vin) != 17:
        missing.append("valid 17-character VIN")

    price = listing.get("price")
    if price is None or price == "":
        missing.append("price")
    else:
        try:
            p = float(price)
            if p <= 0:
                missing.append("positive price")
        except (ValueError, TypeError):
            missing.append("numeric price")

    miles = listing.get("miles") or listing.get("mileage")
    if miles is None or miles == "":
        missing.append("mileage")
    else:
        try:
            m = int(miles)
            if m < 0:
                missing.append("valid mileage")
        except (ValueError, TypeError):
            missing.append("numeric mileage")

    dealer = str(listing.get("dealer", "")).strip()
    if not dealer or "example" in dealer.lower():
        missing.append("dealer name (placeholder 'Example Dealer' rejected)")

    color = str(listing.get("color") or listing.get("exterior_color") or "").strip()
    if not color:
        missing.append("exterior color")

    url = str(listing.get("url", "")).strip()
    if not url:
        missing.append("listing URL")

    if missing:
        raise ValueError(
            f"Cannot generate candidate file: Missing verified listing evidence for: {', '.join(missing)}. "
            "Fabricated or placeholder candidate data is strictly prohibited by PROTOCOL.md."
        )


def write_candidate_file(
    listing: Dict[str, Any],
    nhtsa_data: Optional[Dict[str, Any]] = None,
    repo_dir: Optional[Path] = None,
    overwrite: bool = False,
) -> Path:
    """Generate and write a candidate markdown file to candidates/."""
    validate_listing_evidence(listing)

    root = find_repo_root(repo_dir)
    candidates_dir = root / "candidates"
    candidates_dir.mkdir(parents=True, exist_ok=True)

    vin = listing.get("vin", "").strip().upper()
    if vin and len(vin) == 17:
        dup, match = is_duplicate(vin, repo_dir=root)
        if dup and match and not overwrite:
            raise ValueError(f"VIN {vin} already recorded in {match['file']} ({match['dir']})")

    base_slug = generate_candidate_slug(listing)
    target_path = candidates_dir / f"{base_slug}.md"

    # Avoid slug collisions if file exists but has different VIN
    counter = 2
    while target_path.exists() and not overwrite:
        target_path = candidates_dir / f"{base_slug}-{counter}.md"
        counter += 1

    content = generate_candidate_markdown(listing, nhtsa_data)
    target_path.write_text(content, encoding="utf-8")
    return target_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a candidate lead file from verified listing evidence."
    )
    parser.add_argument("vin", help="17-character vehicle VIN")
    parser.add_argument("--dealer", required=True, help="Dealership name (required)")
    parser.add_argument("--city", default="", help="Dealer city")
    parser.add_argument("--state", default="GA", help="Dealer state (default: GA)")
    parser.add_argument("--price", type=float, required=True, help="Listing advertised price (required)")
    parser.add_argument("--miles", type=int, required=True, help="Odometer mileage (required)")
    parser.add_argument("--color", required=True, help="Exterior color (required)")
    parser.add_argument("--url", required=True, help="Listing URL (required)")
    parser.add_argument("--captains-chairs", help="Notes on captain's chair equipment")
    parser.add_argument("--power-liftgate", help="Notes on power liftgate equipment")

    args = parser.parse_args()

    vin = args.vin.strip().upper()
    print(f"Decoding VIN {vin} and running NHTSA safety chain...")
    nhtsa_res = run_nhtsa_chain(vin)
    vpic = nhtsa_res.get("vpic", {})

    listing = {
        "vin": vin,
        "year": vpic.get("year", ""),
        "make": vpic.get("make", ""),
        "model": vpic.get("model", ""),
        "trim": vpic.get("trim", ""),
        "drivetrain": vpic.get("drive_type", ""),
        "dealer": args.dealer,
        "city": args.city,
        "state": args.state,
        "price": args.price,
        "miles": args.miles,
        "color": args.color,
        "url": args.url,
        "captains_chairs": args.captains_chairs,
        "power_liftgate": args.power_liftgate,
    }

    try:
        out_file = write_candidate_file(listing, nhtsa_data=nhtsa_res)
        print(f"Candidate lead filed successfully: {out_file}")
        return 0
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
