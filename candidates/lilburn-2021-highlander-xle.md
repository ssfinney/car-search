# 2021 Toyota Highlander XLE AWD — Automax Atlanta, Lilburn GA

- **Status:** ready-for-evaluation
- **Dealer/location:** Automax Atlanta, Lilburn GA
- **Listing:** https://www.automaxatlanta.com/pre-owned-cars/detail/2021-Toyota-Highlander/1593882
- **Price:** $28,375 (dealer fees unverified)
- **Mileage:** 71,289
- **Color:** Midnight Black Metallic
- **Captain's chairs:** Configuration match with rear-seat mounted armrests (photo confirmation pending by Claude)
- **Power liftgate:** Standard on XLE (confirmation pending)
- **VIN:** 5TDGZRBH0MS552547
- **NHTSA vPIC decode:** 2021 TOYOTA Highlander XLE | Drive: 4WD/4-Wheel Drive/4x4 | Seats:  | Engine: 3.5L V6
- **NHTSA Recalls (4 campaigns):** 23V720000, 23V865000, 24V452000, 26V128000
- **NHTSA Complaints pattern (533 total):** POWER TRAIN (228), SERVICE BRAKES (68), UNKNOWN OR OTHER (67), STRUCTURE (52), ENGINE (47)

## Required listing record (PARETO_GUIDE.md §6)

| Field | Entry |
|---|---|
| Listing URL / dealer / date | [https://www.automaxatlanta.com/pre-owned-cars/detail/2021-Toyota-Highlander/1593882](https://www.automaxatlanta.com/pre-owned-cars/detail/2021-Toyota-Highlander/1593882) / Automax Atlanta, Lilburn GA / 2026-10-24 |
| VIN / year / trim / drivetrain / color | 5TDGZRBH0MS552547 / 2021 / XLE / AWD / Midnight Black Metallic |
| Captain’s chairs / power liftgate confirmed | Configuration match with rear-seat mounted armrests (photo confirmation pending by Claude) / Standard on XLE (confirmation pending) |
| Mileage / owners / prior use | 71,289 miles / Check pending / Personal / commercial check pending |
| Title, accident, flood, structural history | Adverse history check pending (Muse handoff) |
| Service records and gaps | History report pending (Muse handoff) |
| Open recalls and completion documentation | 4 model-year campaigns (23V720000, 23V865000, 24V452000, 26V128000); VIN-specific completion pending |
| Vehicle price | $28,375 |
| Dealer fees and mandatory packages | Unverified (no API returns dealer fees; written quote required) |
| Taxes / title / registration | Unverified (dealer actual Georgia TAVT calculation required) |
| Transport / travel | Local / within radius (Macon origin) |
| Written OTD total, with financing conditions | Pending written quote from dealer |
| Independent inspection findings | Mandatory gate before deposit (Canton rule) |
| Immediate maintenance estimate | Pending inspection and service history |
| Effective acquisition cost: OTD + immediate work | Pending written OTD + inspection |
| Down payment / retained cash / monthly payment | Default: $17,000 down / $2,000 retained / target $200–250/mo (60 mo @ 6%) |
| Reason it survives against the other candidates | Primary reliability/safety balance target per PARETO_GUIDE.md §2; gas V6 AWD under $30k with 71k miles. |

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

- **VIN confirmed:** Muse's independent vPIC run (2026-10-24) matches the filed decode exactly — 2021 Highlander XLE, AWD, 3.5L V6, ErrorCode 0. Recalls API matches the filed 4 campaigns; complaints pattern as filed (533 total).
- **Price correction:** dealer page LIVE 2026-10-24 at **$29,323** — the filed $28,375 is a stale aggregator figure; use $29,323. The dealer page did not display mileage or VIN, so the filed 71,289 mi stands as aggregator-reported, not dealer-verified.
- Status advanced `lead` → `ready-for-evaluation` on the strength of the 2026-10-24 checks (recorded on main after the branch merge). Remaining gates: written OTD, captain's-chair photo check (Claude), history report, VIN-specific recall completion, independent PPI.

## Log

- 2026-10-24 — Filed as `lead` by CLI search tooling.
- 2026-10-25 — Muse: verification recorded on main after the branch merge (checks run 2026-10-24): VIN confirmed, listing live at corrected/confirmed price (dealer page live 2026-10-24 at $29,323). Status lead → ready-for-evaluation. Report: history/lilburn-2021-highlander-xle/vin-check-2026-10-24.md.
