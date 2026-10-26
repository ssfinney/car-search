# 2022 Toyota Highlander XLE FWD — ALM Hyundai West, Lithia Springs GA

- **Status:** evaluated
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

## Claude evaluation — 2026-10-25

Muse completed its stage and set `ready-for-evaluation`; this is Claude's evaluation-stage verdict and advances the status to `evaluated`. Payments: $17,000 down, 60 mo at 6% (× 0.01933280153), on the dealer's pre-tax total; Georgia TAVT/title not estimated. Stephen decides next.

**Frontier verdict: ON FRONTIER — cheaper Highlander, conditional on seating photo and rental history.**

- **Captain's chairs: UNVERIFIED** — the listing has only two exterior photos. Dealer FAQ text says "captain's seats"; text does not verify. Needs photos or in-person check.
- **Price:** $25,720 + $995 doc + $249 filing = **$26,964** before tax (~$193/mo). 93,573 mi. Magnetic Gray.
- **CARFAX read by Claude** (summary in `history/lithia-springs-2022-highlander-xle/`): no accidents; **ex-rental** for its first ~46.6k mi (NY/NJ), then one Georgia personal owner with regular Toyota-dealer service; was Toyota Gold Certified in 2024. **Open recall 26V128 (second-row seat-back recliner may not lock)**.
- **Safety:** small overlap G/G, updated side G, updated frontal M, headlights A. **Reliability:** CR 2022 "more reliable."
- **Versus Lilburn 2021:** ~$2,360 cheaper, but +22k miles, FWD, rental first owner, seating unconfirmed. **Versus Wesley Chapel:** ~$1,300 cheaper, +8k miles, better reliability evidence, much closer; rental history and A headlights against it.
- **Verdict: evaluated — keep, conditional.** Gates: second-row photo/in-person check, 26V128 completion, written OTD, PPI (rental wear: brakes, suspension, interior).

## Log

- 2026-10-24 — Filed as `lead` by CLI search tooling.
- 2026-10-25 — Muse: verification recorded on main after the branch merge (checks run 2026-10-24): VIN confirmed, listing live at corrected/confirmed price (dealer page live 2026-10-24 at $26,964). Status lead → ready-for-evaluation. Report: history/lithia-springs-2022-highlander-xle/vin-check-2026-10-24.md.
- 2026-10-25 — Claude evaluation complete: ON FRONTIER — cheaper Highlander, conditional on seating photo and rental history. Status ready-for-evaluation → evaluated. Awaiting Stephen's decision.

## Muse verification — 2026-10-25 (evening, at Stephen's request)
- **Listing re-verified live tonight:** dealer page loads for this VIN; structured data shows **price $26,964, availability InStock** — unchanged from the evaluated figure ($25,720 + $995 doc + $249 filing).
- **Captain's chairs STILL UNVERIFIED:** the dealer FAQ text on the page says "Captain seats," which is text, not photo proof — Claude's evaluation flag stands. The listing gallery remains exterior-only, so this needs an in-person check or dealer interior photos.
- **History (Claude's CARFAX read, above):** ex-rental first ~46.6k mi (NY/NJ), then one Georgia owner with regular Toyota-dealer service; Toyota Gold Certified in 2024; no accidents. **Open recall 26V128000.**
- **Gates unchanged:** second-row photo/in-person confirmation, 26V128000 completion, written OTD (est. ~$28.8k with GA TAVT — under ceiling), PPI with rental-wear focus (brakes, suspension, interior).

## Claude frontier update — 2026-10-26

- **Now likely dominated by Lake City 2021 Highlander XLE** (`candidates/lake-city-2021-highlander-xle.md`, evaluated today): $24,305 vs $26,964 before tax (**−$2,659**), ~6.3k fewer miles, captain's chairs photo-confirmed (this car's are still unverified), no rental use. This car's edges are one model year (same structure, same A headlights, same CR rating) and proximity. Those don't offset ~$2k+ after a trip and an out-of-town PPI.
- Holds only if Lake City clears its gates (on-lot confirmation, written OTD with $0 FL sales tax/DR-123). If Lake City falls through, this car's verdict above (keep, conditional) stands again. Status stays `evaluated`; Stephen decides.
