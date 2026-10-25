# 2023 Subaru Ascent Limited AWD — CarMax Buford, Buford GA

- **Status:** evaluated
- **Dealer/location:** CarMax Buford, Buford GA
- **Listing:** https://www.carmax.com/car/28889551
- **Price:** $26,998 (dealer fees unverified)
- **Mileage:** 52,536
- **Color:** Crystal Black Silica
- **Captain's chairs:** Limited 7-Passenger standard captain's chairs (photo confirmation pending by Claude)
- **Power liftgate:** Power rear gate standard on Limited (confirmation pending)
- **VIN:** 4S4WMASD5P3429465
- **NHTSA vPIC decode:** 2023 SUBARU Ascent LIMITED 7 ES, SMART, DMS | Drive: AWD/All-Wheel Drive | Seats:  | Engine: 2.4L V4
- **NHTSA Recalls (4 campaigns):** 23V258000, 23V392000, 23V647000, 26V436000
- **NHTSA Complaints pattern (45 total):** SERVICE BRAKES (10), UNKNOWN OR OTHER (8), FORWARD COLLISION AVOIDANCE (7), VISIBILITY/WIPER (6), TIRES (5)

## Required listing record (PARETO_GUIDE.md §6)

| Field | Entry |
|---|---|
| Listing URL / dealer / date | [https://www.carmax.com/car/28889551](https://www.carmax.com/car/28889551) / CarMax Buford, Buford GA / 2026-10-24 |
| VIN / year / trim / drivetrain / color | 4S4WMASD5P3429465 / 2023 / Limited / AWD / Crystal Black Silica |
| Captain’s chairs / power liftgate confirmed | Limited 7-Passenger standard captain's chairs (photo confirmation pending by Claude) / Power rear gate standard on Limited (confirmation pending) |
| Mileage / owners / prior use | 52,536 miles / Check pending / Personal / commercial check pending |
| Title, accident, flood, structural history | Adverse history check pending (Muse handoff) |
| Service records and gaps | History report pending (Muse handoff) |
| Open recalls and completion documentation | 4 model-year campaigns (23V258000, 23V392000, 23V647000, 26V436000); VIN-specific completion pending |
| Vehicle price | $26,998 |
| Dealer fees and mandatory packages | Unverified (no API returns dealer fees; written quote required) |
| Taxes / title / registration | Unverified (dealer actual Georgia TAVT calculation required) |
| Transport / travel | Local / within radius (Macon origin) |
| Written OTD total, with financing conditions | Pending written quote from dealer |
| Independent inspection findings | Mandatory gate before deposit (Canton rule) |
| Immediate maintenance estimate | Pending inspection and service history |
| Effective acquisition cost: OTD + immediate work | Pending written OTD + inspection |
| Down payment / retained cash / monthly payment | Default: $17,000 down / $2,000 retained / target $200–250/mo (60 mo @ 6%) |
| Reason it survives against the other candidates | Safety at a discount per PARETO_GUIDE.md §2; Good updated side and Acceptable updated frontal at $26,998. |

## Notes

- Discovered via CLI search tooling on 2026-10-24.
- No API returns dealer fees — fees flagged as unverified rather than estimated.
- Second-row captain's chairs and exterior color require photo verification before travel/evaluation.

## Open gates / next steps

- Dealer call: verify vehicle availability, confirm fees, and request written unconditional OTD quote.
- Muse VIN/recall check and dealer-site CARFAX capture (advances status to `vin-checked`).
- Claude captain's-chair image confirmation at evaluation.
- Independent PPI before any deposit (Canton rule).

## Muse verification — 2026-10-24 (recorded on main 2026-10-25)

- **VIN confirmed, one misquote corrected:** Muse's independent vPIC run (2026-10-24) matches the filed decode — 2023 Ascent Limited, AWD, ErrorCode 0. Recalls API matches the filed 4 campaigns; complaints pattern as filed (45 total). The filed engine quote "2.4L V4" is wrong — the Ascent's engine is a 2.4L turbocharged flat-4 (H4). (Filed line left as-is per append-only convention; this note is the correction.)
- **Listing/price:** CarMax page LIVE 2026-10-24 at **$26,998 — matches the filed price exactly.** The page shows mileage only as "53k miles," so the filed 52,536 mi is consistent but not exactly verified; the page names the color only as "Black."
- Status advanced `lead` → `ready-for-evaluation` on the strength of the 2026-10-24 checks (recorded on main after the branch merge). Remaining gates: captain's-chair photo check (Claude), history report, VIN-specific recall completion, independent PPI.

## Claude evaluation — 2026-10-25

Muse completed its stage and set `ready-for-evaluation`; this is Claude's evaluation-stage verdict and advances the status to `evaluated`. Payments: $17,000 down, 60 mo at 6% (× 0.01933280153), on the dealer's pre-tax total; Georgia TAVT/title not estimated. Stephen decides next.

**Frontier verdict: ON FRONTIER — best safety-per-dollar on the board.**

- **Captain's chairs: PHOTO-CONFIRMED by Claude** (CarMax photo 20: individual second-row captain's chair with armrest and open aisle). CarMax's spec text lists a "60-40 bench" second row — that text is wrong for this car (the bench is the third row). Black confirmed. Power liftgate in CarMax's equipment list.
- **Price:** $26,998 CarMax no-haggle, before tax/title (~$193/mo). CarMax lists the car as **single owner**. Mileage shown as "53k".
- **Safety (IIHS 2023 Ascent):** small overlap G/G, updated side G, **updated frontal A** (better than the Pilot's and Highlander's M), headlights G all trims.
- **Reliability:** CR 2023 Ascent "less reliable" (CVT and electronics are the usual complaints). 2.4L turbo flat-4.
- **Recalls to confirm:** 23V392000 front lower-control-arm ball-joint nut, 23V647000 driveshaft center-support bolts, 23V258000 20-inch tire bead, 26V436000.
- **Versus Wesley Chapel Pilot:** ~$1,260 cheaper, ~33k fewer miles, AWD, ~110 mi away, better frontal rating — for weaker reliability evidence (less vs average).
- **Verdict: evaluated — keep as the safety-at-a-discount pick** (guide §2). Gates: CarMax's AutoCheck/history, recall completion, PPI with CVT fluid/condition check.

## Log

- 2026-10-24 — Filed as `lead` by CLI search tooling.
- 2026-10-25 — Muse: verification recorded on main after the branch merge (checks run 2026-10-24): VIN confirmed, listing live at corrected/confirmed price (CarMax page live 2026-10-24 at $26,998 as filed). Status lead → ready-for-evaluation. Report: history/buford-2023-ascent-limited/vin-check-2026-10-24.md.
- 2026-10-25 — Claude evaluation complete: ON FRONTIER — best safety-per-dollar on the board. Status ready-for-evaluation → evaluated. Awaiting Stephen's decision.
