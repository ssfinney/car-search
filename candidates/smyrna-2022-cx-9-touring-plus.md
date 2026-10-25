# 2022 Mazda CX-9 Touring Plus AWD — Ed Voyles Kia, Smyrna GA

- **Status:** evaluated
- **Dealer/location:** Ed Voyles Kia, Smyrna GA
- **Listing:** https://www.edvoyleskia.com/used-Smyrna-2022-%2B-Mazda%2BCX%2B9-Touring%2BPlus-JM3TCBAY8N0608934
- **Price:** $24,898 (dealer fees unverified)
- **Mileage:** 63,824
- **Color:** Deep Crystal Blue Mica
- **Captain's chairs:** Standard second-row captain's chairs on Touring Plus (photo confirmation pending by Claude)
- **Power liftgate:** Hands-free power liftgate standard on Touring Plus (confirmation pending)
- **VIN:** JM3TCBAY8N0608934
- **NHTSA vPIC decode:** 2022 MAZDA CX-9 Touring Plus | Drive: 4WD/4-Wheel Drive/4x4 | Seats: 7 | Engine: 2.5L V4
- **NHTSA Recalls (0 campaigns):** None
- **NHTSA Complaints pattern (11 total):** ELECTRICAL SYSTEM (2), STRUCTURE (2), EXTERIOR LIGHTING (2), SEATS (1), STEERING (1)

## Required listing record (PARETO_GUIDE.md §6)

| Field | Entry |
|---|---|
| Listing URL / dealer / date | [https://www.edvoyleskia.com/used-Smyrna-2022-%2B-Mazda%2BCX%2B9-Touring%2BPlus-JM3TCBAY8N0608934](https://www.edvoyleskia.com/used-Smyrna-2022-%2B-Mazda%2BCX%2B9-Touring%2BPlus-JM3TCBAY8N0608934) / Ed Voyles Kia, Smyrna GA / 2026-10-24 |
| VIN / year / trim / drivetrain / color | JM3TCBAY8N0608934 / 2022 / Touring Plus / AWD / Deep Crystal Blue Mica |
| Captain’s chairs / power liftgate confirmed | Standard second-row captain's chairs on Touring Plus (photo confirmation pending by Claude) / Hands-free power liftgate standard on Touring Plus (confirmation pending) |
| Mileage / owners / prior use | 63,824 miles / Check pending / Personal / commercial check pending |
| Title, accident, flood, structural history | Adverse history check pending (Muse handoff) |
| Service records and gaps | History report pending (Muse handoff) |
| Open recalls and completion documentation | 0 open campaigns for model year; VIN-specific completion check pending |
| Vehicle price | $24,898 |
| Dealer fees and mandatory packages | Unverified (no API returns dealer fees; written quote required) |
| Taxes / title / registration | Unverified (dealer actual Georgia TAVT calculation required) |
| Transport / travel | Local / within radius (Macon origin) |
| Written OTD total, with financing conditions | Pending written quote from dealer |
| Independent inspection findings | Mandatory gate before deposit (Canton rule) |
| Immediate maintenance estimate | Pending inspection and service history |
| Effective acquisition cost: OTD + immediate work | Pending written OTD + inspection |
| Down payment / retained cash / monthly payment | Default: $17,000 down / $2,000 retained / target $200–250/mo (60 mo @ 6%) |
| Reason it survives against the other candidates | Newer low-cost alternative per PARETO_GUIDE.md §2; $24,898 price with 63,824 miles preserves cash ($116-174/mo net). |

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

- **VIN confirmed, one misquote corrected:** Muse's independent vPIC run (2026-10-24) matches the filed decode — 2022 CX-9 Touring Plus, AWD, 7 seats, ErrorCode 0; 0 recall campaigns confirmed. The filed engine quote "2.5L V4" is wrong — the CX-9's engine is a 2.5L turbocharged inline-4; no V4 exists in this car. (Filed line left as-is per append-only convention; this note is the correction.)
- **Price correction:** dealer page LIVE 2026-10-24 — the filed $24,898 appears nowhere on it. The dealer shows Internet Price $22,000 and its own fee-inclusive price of **$23,097**; use $23,097. Mileage 63,824 matches the page.
- Status advanced `lead` → `ready-for-evaluation` on the strength of the 2026-10-24 checks (recorded on main after the branch merge). Remaining gates: captain's-chair photo check (Claude), written OTD confirming the $23,097 figure, history report, independent PPI.

## Claude evaluation — 2026-10-25

Muse completed its stage and set `ready-for-evaluation`; this is Claude's evaluation-stage verdict and advances the status to `evaluated`. Payments: $17,000 down, 60 mo at 6% (× 0.01933280153), on the dealer's pre-tax total; Georgia TAVT/title not estimated. Stephen decides next.

**Frontier verdict: ON FRONTIER — cheapest newer car; dominates the Duluth CX-9.**

- **Captain's chairs: PHOTO-CONFIRMED by Claude** (photos 14 and 17: two individual second-row seats with an open aisle). Deep Crystal Blue confirmed.
- **Price:** dealer page $22,000 + $898 + $199 = **$23,097** before tax (~$118/mo — lowest of any newer car on the board). 63,824 mi.
- **CARFAX read by Claude** (summary in `history/smyrna-2022-cx-9-touring-plus/`): no accidents, 1 owner (Columbus GA), no recalls — but only 7 service records with **~28k- and ~20k-mile oil gaps on a turbo engine**. Dealer replaced battery, rear brakes, filters.
- **Safety:** small overlap G/G, updated side G, **updated frontal P**, headlights G. **Reliability:** CR 2022 CX-9 "more reliable." Smallest third row on the board.
- **Versus Duluth CX-9 Signature:** ~$2k+ cheaper, no accidents (Duluth has two), open-aisle second row; Duluth's only edge is ~9k fewer miles and Signature trim → Duluth likely dominated.
- **Verdict: evaluated — keep as the newer low-cost alternative.** The trade is clear: lowest payment and good reliability evidence for the weakest rear-occupant frontal rating. Gates: written OTD, PPI focused on turbo/oil condition given the service gaps.

## Log

- 2026-10-24 — Filed as `lead` by CLI search tooling.
- 2026-10-25 — Muse: verification recorded on main after the branch merge (checks run 2026-10-24): VIN confirmed, listing live at corrected/confirmed price (dealer page live 2026-10-24 at $23,097 fee-inclusive). Status lead → ready-for-evaluation. Report: history/smyrna-2022-cx-9-touring-plus/vin-check-2026-10-24.md.
- 2026-10-25 — Claude evaluation complete: ON FRONTIER — cheapest newer car; dominates the Duluth CX-9. Status ready-for-evaluation → evaluated. Awaiting Stephen's decision.
