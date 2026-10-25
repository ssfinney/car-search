# 2023 Honda Pilot EX-L FWD — UI Autos, Lawrenceville GA

- **Status:** eliminated
- **Dealer/location:** UI Autos, Lawrenceville GA
- **Listing:** https://cargur.us/details/455004096
- **Price:** $26,920 (dealer fees unverified; dropped from $27,418 on 2026-10-25)
- **Mileage:** 103,581
- **Color:** Crystal Black Pearl
- **Captain's chairs:** 7-passenger trim confirmed by NHTSA vPIC (photo confirmation pending by Claude)
- **Power liftgate:** Standard on EX-L (confirmation pending)
- **VIN:** 5FNYG2H53PB009376
- **NHTSA vPIC decode:** 2023 HONDA Pilot EX-L | Drive: 4x2 | Seats: 7 | Engine: 3.5L V6
- **NHTSA Recalls (5 campaigns):** 23V735000, 24V859000, 24V900000, 25V031000, 25V391000
- **NHTSA Complaints pattern (146 total):** SEAT BELTS (34), ELECTRICAL SYSTEM (28), UNKNOWN OR OTHER (23), FORWARD COLLISION AVOIDANCE (20), STEERING (19)

## Required listing record (PARETO_GUIDE.md §6)

| Field | Entry |
|---|---|
| Listing URL / dealer / date | [https://cargur.us/details/455004096](https://cargur.us/details/455004096) / UI Autos, Lawrenceville GA / 2026-10-24 |
| VIN / year / trim / drivetrain / color | 5FNYG2H53PB009376 / 2023 / EX-L / FWD / Crystal Black Pearl |
| Captain’s chairs / power liftgate confirmed | 7-passenger trim confirmed by NHTSA vPIC (photo confirmation pending by Claude) / Standard on EX-L (confirmation pending) |
| Mileage / owners / prior use | 103,581 miles / Check pending / Personal / commercial check pending |
| Title, accident, flood, structural history | Adverse history check pending (Muse handoff) |
| Service records and gaps | History report pending (Muse handoff) |
| Open recalls and completion documentation | 5 model-year campaigns (23V735000, 24V859000, 24V900000, 25V031000, 25V391000); VIN-specific completion pending |
| Vehicle price | $26,920 |
| Dealer fees and mandatory packages | Unverified (no API returns dealer fees; written quote required) |
| Taxes / title / registration | Unverified (dealer actual Georgia TAVT calculation required) |
| Transport / travel | Local / within radius (Macon origin) |
| Written OTD total, with financing conditions | Pending written quote from dealer |
| Independent inspection findings | Mandatory gate before deposit (Canton rule) |
| Immediate maintenance estimate | Pending inspection and service history |
| Effective acquisition cost: OTD + immediate work | Pending written OTD + inspection |
| Down payment / retained cash / monthly payment | Default: $17,000 down / $2,000 retained / target $200–250/mo (60 mo @ 6%) |
| Reason it survives against the other candidates | Primary 2023 Pilot alternative target; FWD 7-passenger EX-L at $26,920 in the 100-110k discount band. |

## Notes

- Discovered via CLI search tooling on 2026-10-24.
- No API returns dealer fees — fees flagged as unverified rather than estimated.
- Second-row captain's chairs and exterior color require photo verification before travel/evaluation.

## Open gates / next steps

- Dealer call: verify vehicle availability, confirm fees, and request written unconditional OTD quote.
- Muse VIN/recall check and dealer-site CARFAX capture (advances status to `vin-checked`).
- Claude captain's-chair image confirmation at evaluation.
- Independent PPI before any deposit (Canton rule).

## Log

- 2026-10-24 — Filed as `lead` by CLI search tooling.
- 2026-10-25 — Price drop observed: reduced from $27,418 to $26,920.
- 2026-10-25 — Muse (merge of feature/cli-search-tooling into main): dealer listing verified GONE on 2026-10-24 by live-browser check (dealer's 'that one got away' page). The 2026-10-25 aggregator price-drop entry above reflects a stale aggregator feed and does not revive the listing — dealer page outranks aggregator. Status lead → eliminated; file moved to eliminated/.
