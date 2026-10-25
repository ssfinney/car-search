# 2022 Toyota Highlander XLE FWD — ALM Hyundai West, Lithia Springs GA

- **Status:** ready-for-evaluation
- **Dealer/location:** ALM Hyundai West, Lithia Springs GA
- **Listing:** https://www.almcars.com/inventory/2022-toyota-highlander-xle-5TDGZRAH2NS094626
- **Price:** $27,164 (dealer fees unverified)
- **Mileage:** 93,573
- **Color:** Magnetic Gray Metallic
- **Captain's chairs:** Standard XLE configuration (photo confirmation pending by Claude)
- **Power liftgate:** Standard on XLE (confirmation pending)
- **VIN:** 5TDGZRAH2NS094626
- **NHTSA vPIC decode:** 2022 TOYOTA Highlander XLE | Drive: 4x2 | Seats: 7 | Engine: 3.5L V6
- **NHTSA Recalls (5 campaigns):** 22V310000, 23V720000, 24V419000, 24V452000, 26V128000
- **NHTSA Complaints pattern (264 total):** POWER TRAIN (55), STRUCTURE (43), SERVICE BRAKES (39), UNKNOWN OR OTHER (39), AIR BAGS (31)

## Required listing record (PARETO_GUIDE.md §6)

| Field | Entry |
|---|---|
| Listing URL / dealer / date | [https://www.almcars.com/inventory/2022-toyota-highlander-xle-5TDGZRAH2NS094626](https://www.almcars.com/inventory/2022-toyota-highlander-xle-5TDGZRAH2NS094626) / ALM Hyundai West, Lithia Springs GA / 2026-10-24 |
| VIN / year / trim / drivetrain / color | 5TDGZRAH2NS094626 / 2022 / XLE / FWD / Magnetic Gray Metallic |
| Captain’s chairs / power liftgate confirmed | Standard XLE configuration (photo confirmation pending by Claude) / Standard on XLE (confirmation pending) |
| Mileage / owners / prior use | 93,573 miles / Check pending / Personal / commercial check pending |
| Title, accident, flood, structural history | Adverse history check pending (Muse handoff) |
| Service records and gaps | History report pending (Muse handoff) |
| Open recalls and completion documentation | 5 model-year campaigns (22V310000, 23V720000, 24V419000, 24V452000, 26V128000); VIN-specific completion pending |
| Vehicle price | $27,164 |
| Dealer fees and mandatory packages | Unverified (no API returns dealer fees; written quote required) |
| Taxes / title / registration | Unverified (dealer actual Georgia TAVT calculation required) |
| Transport / travel | Local / within radius (Macon origin) |
| Written OTD total, with financing conditions | Pending written quote from dealer |
| Independent inspection findings | Mandatory gate before deposit (Canton rule) |
| Immediate maintenance estimate | Pending inspection and service history |
| Effective acquisition cost: OTD + immediate work | Pending written OTD + inspection |
| Down payment / retained cash / monthly payment | Default: $17,000 down / $2,000 retained / target $200–250/mo (60 mo @ 6%) |
| Reason it survives against the other candidates | Primary reliability/safety target; newer 2022 model year at $27,164, inside the 90-100k discount band. |

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

- **VIN confirmed:** Muse's independent vPIC run (2026-10-24) matches the filed decode exactly — 2022 Highlander XLE, 4x2 FWD, 7 seats, 3.5L V6, ErrorCode 0. Recalls API matches the filed 5 campaigns; complaints pattern as filed (264 total).
- **Price correction:** dealer page LIVE 2026-10-24 at **$26,964** — the filed $27,164 is a stale aggregator figure; use $26,964. The page's FAQ text confirms FWD, 7 passengers, captain's seats, and power liftgate (dealer text; the photo check remains Claude's).
- Status advanced `lead` → `ready-for-evaluation` on the strength of the 2026-10-24 checks (recorded on main after the branch merge). Remaining gates: written OTD, captain's-chair photo check (Claude), history report, VIN-specific recall completion, independent PPI.

## Log

- 2026-10-24 — Filed as `lead` by CLI search tooling.
- 2026-10-25 — Muse: verification recorded on main after the branch merge (checks run 2026-10-24): VIN confirmed, listing live at corrected/confirmed price (dealer page live 2026-10-24 at $26,964). Status lead → ready-for-evaluation. Report: history/lithia-springs-2022-highlander-xle/vin-check-2026-10-24.md.
