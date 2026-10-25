# 2020 TOYOTA Highlander XLE 4x2 — AutoNation Toyota Mall of Georgia, Buford GA

- **Status:** ready-for-evaluation
- **Dealer/location:** AutoNation Toyota Mall of Georgia, Buford GA
- **Listing:** https://www.autonation.com/cars-for-sale/2020-toyota-highlander-xle-5tdgzrah4ls502413
- **Price:** $26,189 (dealer fees unverified)
- **Mileage:** 107,372
- **Color:** Celestial Silver Metallic
- **Captain's chairs:** Standard XLE captain's chair configuration (photo confirmation pending by Claude)
- **Power liftgate:** Standard power liftgate on XLE (confirmation pending)
- **VIN:** 5TDGZRAH4LS502413
- **NHTSA vPIC decode:** 2020 TOYOTA Highlander XLE | Drive: 4x2 | Seats:  | Engine: 3.5L V6
- **NHTSA Recalls (4 campaigns):** 20V633000, 20V162000, 23V720000, 23V865000
- **NHTSA Complaints pattern (321 total):** POWER TRAIN (126), UNKNOWN OR OTHER (45), SERVICE BRAKES (41), AIR BAGS (32), STRUCTURE (30)

## Required listing record (PARETO_GUIDE.md §6)

| Field | Entry |
|---|---|
| Listing URL / dealer / date | [https://www.autonation.com/cars-for-sale/2020-toyota-highlander-xle-5tdgzrah4ls502413](https://www.autonation.com/cars-for-sale/2020-toyota-highlander-xle-5tdgzrah4ls502413) / AutoNation Toyota Mall of Georgia, Buford GA / 2026-10-24 |
| VIN / year / trim / drivetrain / color | 5TDGZRAH4LS502413 / 2020 / XLE / 4x2 / Celestial Silver Metallic |
| Captain’s chairs / power liftgate confirmed | Standard XLE captain's chair configuration (photo confirmation pending by Claude) / Standard power liftgate on XLE (confirmation pending) |
| Mileage / owners / prior use | 107,372 miles / Check pending / Personal / commercial check pending |
| Title, accident, flood, structural history | Adverse history check pending (Muse handoff) |
| Service records and gaps | History report pending (Muse handoff) |
| Open recalls and completion documentation | 4 model-year campaigns (20V633000, 20V162000, 23V720000, 23V865000); VIN-specific completion pending |
| Vehicle price | $26,189 |
| Dealer fees and mandatory packages | Unverified (no API returns dealer fees; written quote required) |
| Taxes / title / registration | Unverified (dealer actual Georgia TAVT calculation required) |
| Transport / travel | Local / within radius (Macon origin) |
| Written OTD total, with financing conditions | Pending written quote from dealer |
| Independent inspection findings | Mandatory gate before deposit (Canton rule) |
| Immediate maintenance estimate | Pending inspection and service history |
| Effective acquisition cost: OTD + immediate work | Pending written OTD + inspection |
| Down payment / retained cash / monthly payment | Default: $17,000 down / $2,000 retained / target $200–250/mo (60 mo @ 6%) |
| Reason it survives against the other candidates | Bridges the 2018–19 cash preservation band and 2021–22 primary targets; 4th-gen redesign Highlander in the 100–110k discount band ($26,189 with 107,372 miles), offering modern TNGA-K crash structure at lower entry cost. |

## Notes

- Discovered via CLI search tooling on 2026-10-24.
- No API returns dealer fees — fees flagged as unverified rather than estimated.
- Second-row captain's chairs and exterior color require photo verification before travel/evaluation.

## Open gates / next steps

- Dealer call: verify vehicle availability, confirm fees, and request written unconditional OTD quote.
- Muse VIN/recall check and dealer-site CARFAX capture (advances status to `vin-checked`).
- Claude captain's-chair image confirmation at evaluation.
- Independent PPI before any deposit (Canton rule).

## Muse verification — 2026-10-24

- VIN check complete; full report at `history/buford-2020-highlander-xle/vin-check-2026-10-24.md`. vPIC decode clean (ErrorText 0, check digit correct) and matches the filed year/trim/drivetrain/engine exactly. The filed recall list (4 campaigns) and complaints pattern (321 total) match the NHTSA APIs exactly.
- Listing live-verified 2026-10-24: AutoNation detail page shows the car In-Stock, described by the dealer as "Certified" (program/terms undocumented). Price $26,189 (AutoNation 1Price) matches filed; VIN and color on page match. Mileage on page is 107,378 (+6 vs filed 107,372).
- 2020-specific safety verified for evaluation (detail in history report): IIHS small overlap G/G, updated side G, front crash prevention Superior, NHTSA 5-star overall — but **XLE headlights are rated P (Poor) for 2020 models only** (2021–22 XLE rate A), and the updated frontal test is not rated for 2020. Reliability: no 2020 row in the guide; secondary Consumer Reports roundups report 4/5 — indicative only, not read from CR directly.
- Still open: adverse history (no CARFAX pulled — owners/accidents/title unverified), VIN-specific recall completion status, captain's-chair photo confirmation (Claude, at evaluation), written OTD, independent PPI. Mileage is in the 100–110k widening band: documented maintenance plus a meaningful discount have not yet been shown.

## Log

- 2026-10-24 — Filed as `lead` by CLI search tooling.
- 2026-10-24 — Muse: VIN check complete; listing live-verified at the filed price. Advanced `lead` → `vin-checked` → `ready-for-evaluation`.
