# 2020 TOYOTA Highlander XLE 4x2 — Volkswagen of Macon, Macon GA

- **Status:** evaluated
- **Dealer/location:** Volkswagen of Macon, Macon GA
- **Listing:** https://www.vwofmacon.com/used/Toyota/2020-Toyota-Highlander-623a7666ac182113dd76063d2389a9c0.htm
- **Price:** $28,969 vehicle price (dealer fees and government charges unverified; implies ~$31.5k+ OTD before negotiation)
- **Mileage:** 60,284
- **Color:** Magnetic Gray Metallic
- **Captain's chairs:** Standard XLE captain's chair configuration (photo confirmation pending by Claude)
- **Power liftgate:** Standard power liftgate confirmed in dealer specifications
- **VIN:** 5TDGZRAH6LS031140
- **NHTSA vPIC decode:** 2020 TOYOTA Highlander XLE | Drive: 4x2 | Seats:  | Engine: 3.5L V6
- **NHTSA Recalls (4 campaigns):** 20V633000, 20V162000, 23V720000, 23V865000
- **NHTSA Complaints pattern (321 total):** POWER TRAIN (126), UNKNOWN OR OTHER (45), SERVICE BRAKES (41), AIR BAGS (32), STRUCTURE (30)

## Required listing record (PARETO_GUIDE.md §6)

| Field | Entry |
|---|---|
| Listing URL / dealer / date | [https://www.vwofmacon.com/used/Toyota/2020-Toyota-Highlander-623a7666ac182113dd76063d2389a9c0.htm](https://www.vwofmacon.com/used/Toyota/2020-Toyota-Highlander-623a7666ac182113dd76063d2389a9c0.htm) / Volkswagen of Macon, Macon GA / 2026-10-24 |
| VIN / year / trim / drivetrain / color | 5TDGZRAH6LS031140 / 2020 / XLE / 4x2 / Magnetic Gray Metallic |
| Captain’s chairs / power liftgate confirmed | Standard XLE captain's chair configuration (photo confirmation pending by Claude) / Standard power liftgate confirmed in dealer specifications |
| Mileage / owners / prior use | 60,284 miles / Check pending / Personal / commercial check pending |
| Title, accident, flood, structural history | Adverse history check pending (Muse handoff) |
| Service records and gaps | History report pending (Muse handoff) |
| Open recalls and completion documentation | 4 model-year campaigns (20V633000, 20V162000, 23V720000, 23V865000); VIN-specific completion pending |
| Vehicle price | $28,969 |
| Dealer fees and mandatory packages | Unverified (no API returns dealer fees; written quote required) |
| Taxes / title / registration | Unverified (dealer actual Georgia TAVT calculation required) |
| Transport / travel | Local / within radius (Macon origin) |
| Written OTD total, with financing conditions | Pending written quote from dealer |
| Independent inspection findings | Mandatory gate before deposit (Canton rule) |
| Immediate maintenance estimate | Pending inspection and service history |
| Effective acquisition cost: OTD + immediate work | Pending written OTD + inspection |
| Down payment / retained cash / monthly payment | Default: $17,000 down / $2,000 retained / target $200–250/mo (60 mo @ 6%) |
| Reason it survives against the other candidates | Located directly at the Macon search origin (0 mi travel); 4th-gen redesign with lowest miles (60,284 mi) among all Highlander leads, 3.5L V6 gas, Magnetic Gray Metallic. Advertised price ($28,969 before fees/tax) implies OTD is likely over the ~$30,000 ceiling without dealer discount; kept as an in-market discovery lead pending written unconditional OTD quote. |

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

- VIN check complete; full report at `history/macon-2020-highlander-xle/vin-check-2026-10-24.md`. vPIC decode clean (ErrorText 0, check digit correct) and matches the filed year/trim/drivetrain/engine exactly. The filed recall list (4 campaigns) and complaints pattern (321 total) match the NHTSA APIs exactly.
- Listing live-verified 2026-10-24: VW of Macon page loads, car marked "On The Lot." Price $28,969 ("VW of Macon Price") matches the filed total, and the page discloses its build: $27,831 list + $988 administrative fee + $150 electronic filing fee. Tax/title is NOT included. Mileage 60,284, VIN, and Magnetic Gray Metallic all match filed.
- 2020-specific safety verified for evaluation (detail in history report): IIHS small overlap G/G, updated side G, front crash prevention Superior, NHTSA 5-star overall — but **XLE headlights are rated P (Poor) for 2020 models only** (2021–22 XLE rate A), and the updated frontal test is not rated for 2020. Reliability: no 2020 row in the guide; secondary Consumer Reports roundups report 4/5 — indicative only, not read from CR directly.
- Still open: adverse history (no CARFAX pulled — owners/accidents/title unverified), VIN-specific recall completion status, captain's-chair photo confirmation (Claude, at evaluation), written OTD, independent PPI.

## Claude evaluation — 2026-10-25

Muse completed its stage and set `ready-for-evaluation`; this is Claude's evaluation-stage verdict and advances the status to `evaluated`. Payments: $17,000 down, 60 mo at 6% (× 0.01933280153), on the dealer's pre-tax total; Georgia TAVT/title not estimated. Stephen decides next.

**Frontier verdict: FAILS REQUIREMENT — second-row bench; recommend elimination.**

- **Second row is a BENCH (8-passenger), photo-confirmed by Claude** (dealer photos 38, 40, 48: continuous second-row bench with a fold-down center armrest/cupholder). Captain's chairs are a firm requirement.
- Also: $28,969 before tax (~$232/mo) at 60,284 mi, 2020 XLE Poor headlights.
- **Verdict: evaluated — recommend Stephen eliminate** (fails the captain's-chair requirement).

## Log

- 2026-10-24 — Filed as `lead` by CLI search tooling.
- 2026-10-24 — Muse: VIN check complete; listing live-verified at the filed price with dealer fees disclosed on the page. Advanced `lead` → `vin-checked` → `ready-for-evaluation`.
- 2026-10-25 — Claude evaluation complete: FAILS REQUIREMENT — second-row bench; recommend elimination. Status ready-for-evaluation → evaluated. Awaiting Stephen's decision.
