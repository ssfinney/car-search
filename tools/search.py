#!/usr/bin/env python3
"""Vehicle listing search across Auto.dev, MarketCheck, and listing feeds.

Implements search filters according to PROTOCOL.md and PARETO_GUIDE.md:
- Macon, GA origin (31201), 200 mi standard / 300 mi widened
- Primary targets: 2021-22 Highlander XLE, 2023 Pilot EX-L 7-passenger
- Alternatives: 2022 CX-9 (Touring Premium/Plus/Grand Touring), 2023 Telluride EX/SX,
  2023 Ascent 7-passenger, 2018-19 Highlander XLE/Limited
- Mileage: 60-90k preferred, 100-110k secondary
- Price ceiling: ~$30,000 OTD screening band
- Exterior: Strict NO WHITE rule
- Features: Power liftgate & 2nd row captain's chairs required
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

WHITE_SPECIFIC_NAMES = {
    "blizzard pearl", "wind chill pearl", "snow white pearl", "crystal white pearl",
    "starfire pearl", "satin white pearl", "white frost tricoat", "white frost",
    "super white", "summit white", "oxford white", "polar white", "glacier white",
    "chalk white", "ceramic white", "pure white", "pearl white", "ivory tri-coat",
}

MACON_ZIP = "31201"
DEFAULT_RADIUS = 200
WIDENED_RADIUS = 300

@dataclass
class TargetSpec:
    name: str
    make: str
    model: str
    years: List[int]
    target_trims: List[str]
    category: str  # "primary", "alternative", "cash-preservation"
    default_seats: int = 7
    notes: str = ""

SEARCH_TARGETS: List[TargetSpec] = [
    # Primary Targets
    TargetSpec(
        name="2020-2022 Highlander XLE",
        make="Toyota",
        model="Highlander",
        years=[2020, 2021, 2022],
        target_trims=["XLE"],
        category="primary",
        notes="V6 gas preferred; captain's configuration required. 2020 redesign bridges 2019 cash preservation and 2021 modern safety."
    ),
    TargetSpec(
        name="2023 Pilot EX-L 7-Passenger",
        make="Honda",
        model="Pilot",
        years=[2023],
        target_trims=["EX-L"],
        category="primary",
        default_seats=7,
        notes="7-passenger configuration (captain's chairs); FWD primary, AWD if competitive."
    ),
    # Alternatives
    TargetSpec(
        name="2022 CX-9 Touring/Grand Touring",
        make="Mazda",
        model="CX-9",
        years=[2022],
        target_trims=["Touring", "Touring Plus", "Grand Touring"],
        category="alternative",
        notes="Captain's chairs required (standard on GT/Touring Plus, optional on Touring Premium)."
    ),
    TargetSpec(
        name="2023 Telluride EX/SX",
        make="Kia",
        model="Telluride",
        years=[2023],
        target_trims=["EX", "SX"],
        category="alternative",
        notes="Verified captain's chairs required."
    ),
    TargetSpec(
        name="2023 Ascent 7-Passenger",
        make="Subaru",
        model="Ascent",
        years=[2023],
        target_trims=["Limited", "Premium", "Touring"],
        category="alternative",
        default_seats=7,
        notes="7-passenger with verified power liftgate."
    ),
    # Cash Preservation
    TargetSpec(
        name="2018-2019 Highlander XLE/Limited",
        make="Toyota",
        model="Highlander",
        years=[2018, 2019],
        target_trims=["XLE", "Limited", "Limited Platinum"],
        category="cash-preservation",
        notes="Favorable model-year reliability evidence; captain's chairs required."
    ),
]


def is_white_exterior(color_text: Optional[str]) -> bool:
    """Return True if color is identified as white exterior."""
    if not color_text:
        return False
    clean = color_text.lower().strip()
    # Explicit non-white colors that may contain the word pearl (e.g. Crystal Black Pearl)
    non_white_cues = ["black", "blue", "red", "gray", "grey", "silver", "green", "brown", "gold", "bronze"]
    if any(cue in clean for cue in non_white_cues) and "white" not in clean:
        return False
    if "white" in clean:
        return True
    if any(name in clean for name in WHITE_SPECIFIC_NAMES):
        return True
    if clean in {"blizzard", "frost", "chalk", "ivory"}:
        return True
    return False


def normalize_autodev_listing(item: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize an Auto.dev v2 listing object."""
    veh = item.get("vehicle", {})
    ret = item.get("retailListing", {})

    vin = (item.get("vin") or veh.get("vin") or "").strip().upper()
    make = (veh.get("make") or "").strip()
    model = (veh.get("model") or "").strip()
    year = veh.get("year")
    trim = (veh.get("trim") or "").strip()
    drivetrain = (veh.get("drivetrain") or veh.get("driveType") or "").strip()
    color = (veh.get("exteriorColor") or ret.get("exteriorColor") or "").strip()

    price = ret.get("price")
    miles = ret.get("miles")
    dealer = (ret.get("dealer") or ret.get("dealerName") or "").strip()
    city = (ret.get("city") or "").strip()
    state = (ret.get("state") or "").strip()
    url = (ret.get("vdp") or ret.get("url") or item.get("link") or "").strip()

    return {
        "vin": vin,
        "year": year,
        "make": make,
        "model": model,
        "trim": trim,
        "drivetrain": drivetrain,
        "dealer": dealer,
        "city": city,
        "state": state,
        "price": price,
        "miles": miles,
        "color": color,
        "url": url,
        "source": "auto.dev",
        "raw": item,
    }


def normalize_marketcheck_listing(item: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize a MarketCheck v2 listing object."""
    build = item.get("build", {})
    dealer_info = item.get("dealer", {})

    vin = (item.get("vin") or "").strip().upper()
    year = build.get("year") or item.get("year")
    make = (build.get("make") or item.get("make") or "").strip()
    model = (build.get("model") or item.get("model") or "").strip()
    trim = (build.get("trim") or item.get("trim") or "").strip()
    drivetrain = (build.get("drivetrain") or "").strip()
    color = (item.get("exterior_color") or "").strip()

    price = item.get("price")
    miles = item.get("miles")
    dealer = (dealer_info.get("name") or "").strip()
    city = (dealer_info.get("city") or "").strip()
    state = (dealer_info.get("state") or "").strip()
    url = (item.get("vdp_url") or "").strip()

    return {
        "vin": vin,
        "year": year,
        "make": make,
        "model": model,
        "trim": trim,
        "drivetrain": drivetrain,
        "dealer": dealer,
        "city": city,
        "state": state,
        "price": price,
        "miles": miles,
        "color": color,
        "url": url,
        "source": "marketcheck",
        "raw": item,
    }


def query_autodev(
    spec: TargetSpec,
    api_key: str,
    zip_code: str = MACON_ZIP,
    radius: int = DEFAULT_RADIUS,
    max_price: int = 30000,
    max_miles: int = 95000,
) -> List[Dict[str, Any]]:
    """Query Auto.dev API for matching vehicles."""
    base_url = "https://api.auto.dev/listings"
    year_param = ",".join(str(y) for y in spec.years)

    params = {
        "vehicle.make": spec.make,
        "vehicle.model": spec.model,
        "vehicle.year": year_param,
        "retailListing.price": f"10000-{max_price}",
        "retailListing.miles": f"20000-{max_miles}",
        "zip": zip_code,
        "distance": str(radius),
        "limit": "50",
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "User-Agent": "SUV-Search-Tooling/1.0",
    }

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            raw_data = data.get("data", [])
            return [normalize_autodev_listing(item) for item in raw_data]
    except Exception as exc:
        print(f"[Auto.dev Error] {exc}", file=sys.stderr)
        return []


def query_marketcheck(
    spec: TargetSpec,
    api_key: str,
    zip_code: str = MACON_ZIP,
    radius: int = DEFAULT_RADIUS,
    max_price: int = 30000,
    max_miles: int = 95000,
) -> List[Dict[str, Any]]:
    """Query MarketCheck API for matching vehicles."""
    base_url = "https://api.marketcheck.com/v2/search/car/active"
    year_param = f"{min(spec.years)}-{max(spec.years)}" if len(spec.years) > 1 else str(spec.years[0])

    params = {
        "api_key": api_key,
        "make": spec.make,
        "model": spec.model,
        "year": year_param,
        "price_range": f"10000-{max_price}",
        "mileage_range": f"20000-{max_miles}",
        "zip": zip_code,
        "radius": str(radius),
        "car_type": "used",
        "rows": "50",
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    headers = {"User-Agent": "SUV-Search-Tooling/1.0"}

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            listings = data.get("listings", [])
            return [normalize_marketcheck_listing(item) for item in listings]
    except Exception as exc:
        print(f"[MarketCheck Error] {exc}", file=sys.stderr)
        return []


def passes_screening(listing: Dict[str, Any], spec: Optional[TargetSpec] = None) -> Tuple[bool, str]:
    """Screen candidate listing against hard requirements."""
    # 1. White exterior hard reject
    color = listing.get("color")
    if is_white_exterior(color):
        return False, f"Rejected: White exterior ({color})"

    # 2. Mileage bounds
    miles = listing.get("miles")
    if miles:
        try:
            m = int(miles)
            if m > 115000:
                return False, f"Rejected: High mileage ({m:,} mi > 115k)"
        except (ValueError, TypeError):
            pass

    # 3. Price bounds
    price = listing.get("price")
    if price:
        try:
            p = float(price)
            if p > 32000:
                return False, f"Rejected: Advertised price ${p:,.0f} far exceeds $30k ceiling"
        except (ValueError, TypeError):
            pass

    # 4. Trim filter if spec given
    if spec and spec.target_trims:
        trim = (listing.get("trim") or "").lower()
        matched = any(t.lower() in trim for t in spec.target_trims)
        # If trim is missing, don't reject outright, let evaluation check it
        if trim and not matched:
            return False, f"Trim mismatch: '{trim}' not in {spec.target_trims}"

    return True, "Passed screening"


def load_listings_from_json(file_path: Path) -> List[Dict[str, Any]]:
    """Load normalized listings from a local JSON file or scraper export."""
    data = json.loads(file_path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return data
    elif isinstance(data, dict):
        if "data" in data and isinstance(data["data"], list):
            return [normalize_autodev_listing(i) for i in data["data"]]
        elif "listings" in data and isinstance(data["listings"], list):
            return [normalize_marketcheck_listing(i) for i in data["listings"]]
        elif "candidates" in data and isinstance(data["candidates"], list):
            return data["candidates"]
    return []
