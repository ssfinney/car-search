# 2023 Kia Telluride SX FWD — Gerald Jones Mazda, Augusta GA

- **Status:** evaluated
- **Dealer/location:** Gerald Jones Mazda, Augusta GA
- **Listing:** https://www.geraldjonesmazda.com/auto/used-2023-kia-telluride-sx/121894667/
- **Price:** $27,771 (dealer fees unverified)
- **Mileage:** 78,633
- **Color:** Gravity Gray
- **Captain's chairs:** SX 7-passenger standard captain's chairs (photo confirmation pending by Claude)
- **Power liftgate:** Smart power liftgate standard on SX (confirmation pending)
- **VIN:** 5XYP54GC1PG338129
- **NHTSA vPIC decode:** 2023 KIA Telluride SX, SX X-LINE / X-PRO / PRESTIGE / PRESTIGE X-LINE / PRESTIGE X-PRO | Drive: 4x2 | Seats: 7 | Engine: 3.8L V6
- **NHTSA Recalls (6 campaigns):** 23V035000, 23V298000, 24V214000, 24V407000, 25V494000, 26V430000
- **NHTSA Complaints pattern (209 total):** UNKNOWN OR OTHER (60), ELECTRICAL SYSTEM (50), VISIBILITY/WIPER (29), POWER TRAIN (24), ENGINE (23)

## Required listing record (PARETO_GUIDE.md §6)

| Field | Entry |
|---|---|
| Listing URL / dealer / date | [https://www.geraldjonesmazda.com/auto/used-2023-kia-telluride-sx/121894667/](https://www.geraldjonesmazda.com/auto/used-2023-kia-telluride-sx/121894667/) / Gerald Jones Mazda, Augusta GA / 2026-10-24 |
| VIN / year / trim / drivetrain / color | 5XYP54GC1PG338129 / 2023 / SX / FWD / Gravity Gray |
| Captain’s chairs / power liftgate confirmed | SX 7-passenger standard captain's chairs (photo confirmation pending by Claude) / Smart power liftgate standard on SX (confirmation pending) |
| Mileage / owners / prior use | 78,633 miles / Check pending / Personal / commercial check pending |
| Title, accident, flood, structural history | Adverse history check pending (Muse handoff) |
| Service records and gaps | History report pending (Muse handoff) |
| Open recalls and completion documentation | 6 model-year campaigns (23V035000, 23V298000, 24V214000, 24V407000, 25V494000, 26V430000); VIN-specific completion pending |
| Vehicle price | $27,771 |
| Dealer fees and mandatory packages | Unverified (no API returns dealer fees; written quote required) |
| Taxes / title / registration | Unverified (dealer actual Georgia TAVT calculation required) |
| Transport / travel | Local / within radius (Macon origin) |
| Written OTD total, with financing conditions | Pending written quote from dealer |
| Independent inspection findings | Mandatory gate before deposit (Canton rule) |
| Immediate maintenance estimate | Pending inspection and service history |
| Effective acquisition cost: OTD + immediate work | Pending written OTD + inspection |
| Down payment / retained cash / monthly payment | Default: $17,000 down / $2,000 retained / target $200–250/mo (60 mo @ 6%) |
| Reason it survives against the other candidates | Crash-test-focused alternative per PARETO_GUIDE.md §2; Good across all tests at $27,771 with 78k miles. |

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

- **VIN confirmed:** Muse's independent vPIC run (2026-10-24) matches the filed decode exactly — 2023 Telluride SX, 4x2 FWD, 7 seats, 3.8L V6, ErrorCode 0. Recalls API matches the filed 6 campaigns; complaints pattern as filed (209 total).
- **Price correction:** dealer page LIVE 2026-10-24 at adjusted selling price **$27,569** — the filed $27,771 is a stale aggregator figure; use $27,569. Mileage 78,633 matches the page.
- Guide note: as a second-owner Kia, the powertrain warranty drops to 5 yr / 60k — factor into evaluation.
- Status advanced `lead` → `ready-for-evaluation` on the strength of the 2026-10-24 checks (recorded on main after the branch merge). Remaining gates: written OTD, captain's-chair photo check (Claude), history report, VIN-specific recall completion, independent PPI.

## Claude evaluation — 2026-10-25

Muse completed its stage and set `ready-for-evaluation`; this is Claude's evaluation-stage verdict and advances the status to `evaluated`. Payments: $17,000 down, 60 mo at 6% (× 0.01933280153), on the dealer's pre-tax total; Georgia TAVT/title not estimated. Stephen decides next.

**Frontier verdict: LISTING NOT LIVE — recommend elimination as sold.**

- **The listing URL now redirects to the dealer's general search page**, and a Telluride search of Gerald Jones Mazda's inventory on 2026-10-25 shows only a 2020 EX, 2024 EX, and 2025 SX X-Line — VIN 5XYP54GC1PG338129 is not present. The car appears sold since Muse's 2026-10-24 check.
- For the record, had it been available: 2023 Telluride all-G crash tests, CR "less reliable," $27,569 at 78.6k mi FWD, second-owner powertrain warranty reduced to 5 yr/60k (already exceeded).
- **Verdict: evaluated — recommend eliminate as no longer available**; Muse may re-verify before moving the file.

## Log

- 2026-10-24 — Filed as `lead` by CLI search tooling.
- 2026-10-25 — Muse: verification recorded on main after the branch merge (checks run 2026-10-24): VIN confirmed, listing live at corrected/confirmed price (dealer page live 2026-10-24 at $27,569). Status lead → ready-for-evaluation. Report: history/augusta-2023-telluride-sx/vin-check-2026-10-24.md.
- 2026-10-25 — Claude evaluation complete: LISTING NOT LIVE — recommend elimination as sold. Status ready-for-evaluation → evaluated. Awaiting Stephen's decision.
