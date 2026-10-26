# 2021 Toyota Highlander XLE AWD — Automax Atlanta, Lilburn GA

- **Status:** evaluated
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

## Claude evaluation — 2026-10-25

Muse completed its stage and set `ready-for-evaluation`; this is Claude's evaluation-stage verdict and advances the status to `evaluated`. Payments: $17,000 down, 60 mo at 6% (× 0.01933280153), on the dealer's pre-tax total; Georgia TAVT/title not estimated. Stephen decides next.

**Frontier verdict: ON FRONTIER — top-tier contender; may displace Wesley Chapel pending history.**

- **Captain's chairs: PHOTO-CONFIRMED by Claude** (dealer gallery photo 8: individual second-row seat with armrest and a separate opposite seat, open aisle). Midnight Black confirmed. Power liftgate standard on XLE (not separately verified).
- **Dealer page read 2026-10-25:** $28,375 + $699 service fee + $249 ETR = **$29,323** before tax; **71,289 mi and VIN 5TDGZRBH0MS552547 shown on the page** (resolves Muse's "aggregator-only" mileage note). AutoCheck score 92 (range 88–93); report itself not read. ~$239/mo before tax.
- **Safety (IIHS, applies to this car):** small overlap G/G, updated side G (2020–26), headlights **A** (2021+ XLE), updated frontal not rated for 2021 (2022's M applies from 2022 — same structure, no 2021 result). Superior pedestrian AEB; TSS 2.5+.
- **Reliability:** CR 2021 Highlander "more reliable" — the strongest evidence of any car near this price. NHTSA complaints skew powertrain (228 of 533; 8-speed shift quality) — pattern signal only.
- **Recall to confirm:** **26V128000 second-row seat-back recliner may not lock (2021–25)** — directly affects child-seat positions; also 23V720000, 23V865000, 24V452000.
- **Versus Wesley Chapel 2023 Pilot:** ~$1,065 more before tax, but 14k fewer miles, AWD, ~90 mi from Macon instead of ~400, better reliability evidence, equal side protection; gives up G headlights (A) and has no updated-frontal result. This is the guide's preferred matchup (§7: favor a 2021–22 Highlander when price and condition are competitive).
- **Flag:** Automax Atlanta's site has a "Manufacturer Buyback" section — confirm this VIN is **not** a lemon/manufacturer-buyback title before anything else.
- **Verdict: evaluated — recommend as a co-lead with Wesley Chapel.** Gates: title/buyback check and full history (CARFAX or AutoCheck), written OTD (likely ~$31k with TAVT — over ceiling unless the $699 fee or price moves), 26V128000 completion, PPI.

## Muse buyback check — 2026-10-25 (live browser)

- **Question:** is VIN 5TDGZRBH0MS552547 a manufacturer-buyback / lemon-branded title? Claude's flag came from the "MANUFACTURER BUYBACK" item in Automax Atlanta's site navigation.
- **Listing page:** no "lemon," "branded title," or buyback wording anywhere in this vehicle's listing or description. "Manufacturer Buyback" appears only as the site-wide nav link — it is a dealer marketing category, not a label on this car.
- **Dealer's buyback page** (automaxatlanta.com/manufacturer-buyback): informational video page only; it lists no buyback inventory at all. This VIN / stock 28633C appears nowhere on it.
- **AutoCheck report:** the listing's "View Report" link (automaxatlanta.com/autocheck/get/1593882) would not render — "the vehicle history report cannot be displayed at this time. Please ask the dealer for a copy." Reloaded once, same result. Only verified AutoCheck datum: score 92 (similar vehicles 88–93) from the listing widget.
- **Verdict: no evidence this car is a buyback; title brand NOT verified either way.** The document that settles it — the full AutoCheck (or CARFAX) report — has to come from the dealer. Gate stays open until that report is in hand; treat as a routine first ask on this car, not a red flag found.

## Muse CARFAX read — 2026-10-25 (report supplied by Stephen)

Full summary: `history/lilburn-2021-highlander-xle/carfax-summary-2026-10-25.md` (source PDF held by Muse outside the repo). Report run 10/25/2026 by Automax Atlanta.

- **BUYBACK GATE CLOSED — not a buyback.** Title History: Damage Brands (Salvage | Junk | Rebuilt | Fire | Flood | Hail | Lemon) "No Problem" for both owners, CARFAX-guaranteed; Odometer Brands also "No Problem." No DMV-reported brand of any kind.
- **History otherwise strong:** 2 owners (personal lease 2021–24, MD/NY; personal 2024–26, Salisbury MD); **no accidents or damage reported**; no total loss/structural/airbag events; odometer consistent to 71,289. **18 service records, dealer-maintained throughout** (Steet Toyota NY, then Pohanka Toyota MD incl. full brake/tire reconditioning at Owner 2's purchase and oil on schedule to 04/2026 at 67,745 mi).
- **New finding — repossessed:** Owner 2's car was repossessed 08/13/2026, then wholesaled (financial company → Autos Direct, Fredericksburg VA, 09/15/2026) to Automax (offered 09/30/2026). Repossession does not brand the title. Noted for negotiation and PPI context; service currency through 04/2026 limits the deferred-care concern.
- **Open recall on this VIN: 26V128000 (26TA06)** — second-row seat-back recliner may not lock; remedy available, not shown completed. The only open recall on the report. Confirm completion (free at Toyota) — it affects the second row directly.
- Remaining gates: written OTD (ceiling pressure: ~$31k with TAVT per Claude unless the $699 fee/price moves), 26V128 completion, independent PPI.

## Log

- 2026-10-24 — Filed as `lead` by CLI search tooling.
- 2026-10-25 — Muse: verification recorded on main after the branch merge (checks run 2026-10-24): VIN confirmed, listing live at corrected/confirmed price (dealer page live 2026-10-24 at $29,323). Status lead → ready-for-evaluation. Report: history/lilburn-2021-highlander-xle/vin-check-2026-10-24.md.
- 2026-10-25 — Claude evaluation complete: ON FRONTIER — top-tier contender; may displace Wesley Chapel pending history. Status ready-for-evaluation → evaluated. Awaiting Stephen's decision.
- 2026-10-25 — Muse buyback check: listing carries no buyback/lemon branding (nav link only); dealer's buyback page lists no inventory; linked AutoCheck report would not display on the dealer site, so the title brand itself remains unverified — full history report from the dealer is the closing document. No buyback evidence found.
- 2026-10-25 — Muse read the CARFAX Stephen supplied: title brands all clean and CARFAX-guaranteed — NOT a buyback (gate closed). 2 owners, no accidents/damage reported, 18 dealer service records. New findings: repossessed from Owner 2 on 08/13/2026 and wholesaled to Automax; open recall 26V128000 (seat-back recliner) not shown completed. Summary in history/lilburn-2021-highlander-xle/ (source PDF held by Muse; snapshot push is text-only).

## Muse verification — 2026-10-25 (evening, at Stephen's request)
- **Listing re-verified live tonight:** dealer page loads for this VIN/stock; product metadata shows **price $29,323, availability "in stock"** — unchanged from the filed total ($28,375 + $699 + $249).
- **2026-10-25 CARFAX stands** (see the CARFAX section above and `history/lilburn-2021-highlander-xle/carfax-summary-2026-10-25.md`): no title brands, no accidents, 18 service records; repossessed 08/13/2026 (no title brand); **open recall 26V128000** is the only one on the report.
- **Gates unchanged:** written OTD (pre-tax $29,323; GA TAVT puts it ~$31k — over the ~$30,000 ceiling as priced, so the $699 service fee or the selling price has to move), 26V128000 completion (free at any Toyota dealer), independent PPI.
