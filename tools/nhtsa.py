#!/usr/bin/env python3
"""NHTSA API chain utility.

Performs:
1. vPIC VIN decode (vpic.nhtsa.dot.gov)
2. NHTSA Recalls API (api.nhtsa.gov)
3. NHTSA Complaints API (api.nhtsa.gov) for pattern signals
"""

from __future__ import annotations

import json
import re
import sys
import urllib.parse
import urllib.request
from collections import Counter
from typing import Any, Dict, List, Optional

VPIC_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/{vin}?format=json"
RECALLS_URL = "https://api.nhtsa.gov/recalls/recallsByVehicle?make={make}&model={model}&modelYear={year}"
COMPLAINTS_URL = "https://api.nhtsa.gov/complaints/complaintsByVehicle?make={make}&model={model}&modelYear={year}"

HEADERS = {
    "User-Agent": "SUV-Search-Tooling/1.0 (stephenfinney; research/car-search)"
}


def _http_get_json(url: str, timeout: int = 15) -> Optional[Dict[str, Any]]:
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
            return json.loads(data.decode("utf-8"))
    except urllib.error.HTTPError as exc:
        try:
            body = exc.read().decode("utf-8")
            data = json.loads(body)
            # NHTSA returns 400 when Count is 0
            if isinstance(data, dict) and (data.get("Count") == 0 or data.get("count") == 0 or "results" in data):
                return data
        except Exception:
            pass
        print(f"[NHTSA API error] GET {url}: {exc}", file=sys.stderr)
        return None
    except Exception as exc:
        print(f"[NHTSA API error] GET {url}: {exc}", file=sys.stderr)
        return None

def decode_vin(vin: str) -> Dict[str, Any]:
    """Decode a VIN using NHTSA vPIC."""
    clean_vin = vin.strip().upper()
    url = VPIC_URL.format(vin=clean_vin)
    resp = _http_get_json(url)
    if not resp or "Results" not in resp or not resp["Results"]:
        return {"vin": clean_vin, "error": "No vPIC results returned"}

    res = resp["Results"][0]
    return {
        "vin": clean_vin,
        "make": res.get("Make", "").strip(),
        "model": res.get("Model", "").strip(),
        "year": res.get("ModelYear", "").strip(),
        "trim": res.get("Trim", "").strip(),
        "series": res.get("Series", "").strip(),
        "body_class": res.get("BodyClass", "").strip(),
        "doors": res.get("Doors", "").strip(),
        "seats": res.get("Seats", "").strip(),
        "drive_type": res.get("DriveType", "").strip(),
        "engine_cylinders": res.get("EngineCylinders", "").strip(),
        "displacement_l": res.get("DisplacementL", "").strip(),
        "fuel_type": res.get("FuelTypePrimary", "").strip(),
        "plant_country": res.get("PlantCountry", "").strip(),
        "plant_state": res.get("PlantState", "").strip(),
        "plant_city": res.get("PlantCity", "").strip(),
        "error_code": res.get("ErrorCode", ""),
        "error_text": res.get("ErrorText", ""),
    }


def get_recalls(make: str, model: str, year: str | int) -> Dict[str, Any]:
    """Fetch open NHTSA campaigns for make/model/year."""
    safe_make = urllib.parse.quote(str(make).strip().lower())
    safe_model = urllib.parse.quote(str(model).strip().lower())
    safe_year = urllib.parse.quote(str(year).strip())

    url = RECALLS_URL.format(make=safe_make, model=safe_model, year=safe_year)
    resp = _http_get_json(url)
    if (resp is None or "results" not in resp) and ("-" in model or " " in model):
        alt_model = urllib.parse.quote(re.sub(r"[\s-]+", "", str(model).strip().lower()))
        alt_url = RECALLS_URL.format(make=safe_make, model=alt_model, year=safe_year)
        resp = _http_get_json(alt_url)
    if not resp or "results" not in resp or resp["results"] is None:
        return {"count": 0, "campaigns": []}

    results = resp.get("results") or []
    campaigns: List[Dict[str, Any]] = []
    for r in results:
        campaigns.append({
            "campaign_number": r.get("NHTSACampaignNumber", ""),
            "component": r.get("Component", ""),
            "summary": r.get("Summary", ""),
            "consequence": r.get("Conequence", r.get("Consequence", "")),
            "remedy": r.get("Remedy", ""),
        })

    return {
        "count": len(campaigns),
        "campaigns": campaigns,
    }


def get_complaints_pattern(make: str, model: str, year: str | int) -> Dict[str, Any]:
    """Fetch NHTSA complaints and calculate component pattern signals."""
    safe_make = urllib.parse.quote(str(make).strip().lower())
    safe_model = urllib.parse.quote(str(model).strip().lower())
    safe_year = urllib.parse.quote(str(year).strip())

    url = COMPLAINTS_URL.format(make=safe_make, model=safe_model, year=safe_year)
    resp = _http_get_json(url)
    if (resp is None or "results" not in resp) and ("-" in model or " " in model):
        alt_model = urllib.parse.quote(re.sub(r"[\s-]+", "", str(model).strip().lower()))
        alt_url = COMPLAINTS_URL.format(make=safe_make, model=alt_model, year=safe_year)
        resp = _http_get_json(alt_url)
    if not resp or "results" not in resp or resp["results"] is None:
        return {"count": 0, "patterns": {}, "top_issues": []}

    results = resp.get("results") or []
    count = resp.get("count", len(results))

    component_counter: Counter[str] = Counter()
    for item in results:
        comps = item.get("components", "") or item.get("Component", "")
        if comps:
            for c in comps.split(","):
                c_clean = c.strip().upper()
                if c_clean:
                    component_counter[c_clean] += 1

    top_issues = [
        f"{comp} ({cnt})" for comp, cnt in component_counter.most_common(5)
    ]

    return {
        "count": count,
        "patterns": dict(component_counter.most_common(10)),
        "top_issues": top_issues,
    }


def run_nhtsa_chain(vin: str) -> Dict[str, Any]:
    """Run full NHTSA chain: vPIC decode -> Recalls -> Complaints pattern."""
    clean_vin = vin.strip().upper()
    vpic = decode_vin(clean_vin)
    make = vpic.get("make")
    model = vpic.get("model")
    year = vpic.get("year")

    recalls = {"count": 0, "campaigns": []}
    complaints = {"count": 0, "patterns": {}, "top_issues": []}

    if make and model and year:
        recalls = get_recalls(make, model, year)
        complaints = get_complaints_pattern(make, model, year)

    return {
        "vin": clean_vin,
        "vpic": vpic,
        "recalls": recalls,
        "complaints": complaints,
    }


def format_nhtsa_summary(data: Dict[str, Any]) -> str:
    """Format the NHTSA chain findings into a concise markdown text."""
    vpic = data.get("vpic", {})
    recalls = data.get("recalls", {})
    complaints = data.get("complaints", {})

    make = vpic.get("make", "Unknown")
    model = vpic.get("model", "")
    year = vpic.get("year", "")
    trim = vpic.get("trim", "")
    seats = vpic.get("seats", "")
    drive = vpic.get("drive_type", "")
    disp = vpic.get("displacement_l", "")
    cyl = vpic.get("engine_cylinders", "")

    engine_str = f"{disp}L V{cyl}" if disp and cyl else ""

    campaign_ids = [c.get("campaign_number") for c in recalls.get("campaigns", []) if c.get("campaign_number")]
    campaign_str = ", ".join(campaign_ids) if campaign_ids else "None"

    top_complaints = ", ".join(complaints.get("top_issues", [])) or "None reported"

    lines = [
        f"- **NHTSA vPIC decode:** {year} {make} {model} {trim} | Drive: {drive} | Seats: {seats} | Engine: {engine_str}",
        f"- **NHTSA Recalls ({recalls.get('count', 0)} campaigns):** {campaign_str}",
        f"- **NHTSA Complaints pattern ({complaints.get('count', 0)} total):** {top_complaints}",
    ]
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python -m tools.nhtsa <VIN>", file=sys.stderr)
        return 1

    vin = sys.argv[1].strip()
    print(f"Querying NHTSA chain for VIN: {vin}...")
    res = run_nhtsa_chain(vin)
    print("\n--- Summary ---")
    print(format_nhtsa_summary(res))
    print("\n--- Full JSON ---")
    print(json.dumps(res, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
