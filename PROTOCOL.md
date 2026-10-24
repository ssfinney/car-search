# Protocol

Every agent working this search follows these rules. If a rule conflicts with an ad-hoc instruction, follow the rule and flag the conflict.

## Source of truth

- This repo is the source of truth. Chat history and memory files are not.
- One Markdown file per candidate vehicle in `candidates/`.
- Eliminated vehicles move to `eliminated/` with the reason recorded. Never delete a candidate file outright.

## Requirements (firm)

Per `PARETO_GUIDE.md`, which controls search targets and evaluation criteria where it and this protocol conflict.

- Three-row SUV.
- Second-row captain's chairs **and** power liftgate required.
- No white exterior.
- Search origin: Macon, GA. Start within 200 miles; widen to 300 miles when the delivered total plus inspection logistics justify it.
- Mileage: prefer 60–90k first; widen to 100–110k for documented maintenance plus a meaningful discount.
- Budget framework: $19,000 cash available; default $17,000 down / $2,000 retained; 60 months at 6% APR; preferred payment $200–250/month; default OTD ceiling ~$30,000. The ceiling is permission to compare better vehicles, not a spending goal.

## Verification rules

- Never trust listing text or trim badges for required attributes. Captain's chairs and exterior color require photo confirmation or a dealer call.
- Compute the real out-the-door price from the dealer's own numbers — advertised price + doc/fees + the dealer's actual tax/title calculation — and get it as a written, unconditional quote before any candidate advances. An advertised price that excludes fees or assumes incentives is not a price. Do not estimate taxes as a universal flat markup (per `PARETO_GUIDE.md`).
- History reports are necessary, not sufficient — the **Canton rule**: a clean CARFAX on the Canton 2016 Pilot Elite missed ~$3–4k of damage that only an independent pre-purchase inspection (PPI) found. An independent PPI is a mandatory gate before any deposit on any vehicle.
- Assume undocumented timing-belt service is due: budget +~$1,200 on Honda V6s. A seller claim is not documentation.

## Claiming work

- Tasks live as GitHub Issues in ssfinney/car-search (seed list mirrored in `TASKS.md`).
- Claim by assigning yourself and/or labeling `claimed:<agent-name>`, with a timestamp comment.
- Do not edit a candidate file another agent has claimed in an open issue.
- Append findings as dated sections. Never rewrite or delete another agent's entries.

## Candidate status vocabulary

Use exactly one in each candidate file. The statuses are the workflow stages in the next section:

- `lead` — filed by a search (CLI agents, or Muse for Marketplace finds); not yet VIN-checked.
- `vin-checked` — Muse has completed the VIN/recall/history checks and saved the report under `history/<candidate-slug>/`.
- `ready-for-evaluation` — Muse has handed the candidate to Claude for frontier evaluation.
- `evaluated` — Claude's frontier verdict is logged in the candidate file; awaiting Stephen's decision.
- `finalist` — Stephen's decision: advanced, subject to the PPI gate before any deposit.
- `eliminated` — ruled out; file lives in `eliminated/` with the reason.
- `purchased` — bought. Search over.

(The old `verified` status is retired; files still carrying it predate the workflow below and get restaged as they are worked.)

## Workflow and handoffs

Candidate status flow:

`lead` → `vin-checked` → `ready-for-evaluation` → `evaluated` → Stephen decision (`finalist` / `eliminated` / `purchased`)

- **CLI agents** file candidates as `lead`.
- **Muse** advances `lead` → `vin-checked`: VIN decode, NHTSA recalls/complaints, adverse-history checks on every candidate, plus dealer-site crawl and CARFAX/history report saved under `history/<candidate-slug>/` for shortlist cars. Muse also runs a parallel Facebook Marketplace search and files Marketplace finds the same way (photo-checking the second row when filing them).
- **Muse** advances `vin-checked` → `ready-for-evaluation` by setting the status in the candidate file and opening or updating an evaluation Issue for Claude.
- **Claude** advances `ready-for-evaluation` → `evaluated`: frontier match per `PARETO_GUIDE.md`, brief image review confirming captain's chairs, verdict logged in the candidate file.
- **Stephen** decides: `finalist`, `eliminated`, or `purchased`.
- Each agent only advances its own stage. A handoff is complete only when the status field in the candidate file changes — not when someone says so in chat.

## Commits

- Small commits: one vehicle or one task per commit.
- Message format: `<agent>: <change>` (e.g. `claude-code: verify pristine belt status`).
- Do not commit over another agent's uncommitted claimed work.

## Division of labor

- **Muse (chat agent):** Facebook Marketplace searching; VIN checks on **all** candidates (NHTSA recalls/complaints, adverse history); crawling dealer websites for shortlist cars and saving the CARFAX/history reports into this repo under `history/<candidate-slug>/`.
- **CLI agents (Stephen's local "omp" agents — Gemini, Codex, whatever else):** build the CLI tooling in this repo (MarketCheck/Auto.dev APIs, the NHTSA chain — see `TASKS.md`) and run the searches with it, filing matching vehicles as candidate files.
- **Claude:** owns evaluations — matching candidates to the Pareto frontier in `PARETO_GUIDE.md` and a brief image review confirming captain's chairs.

## Evaluation standard (from `PARETO_GUIDE.md`)

- **Dominance rule:** remove a candidate only when another offers no meaningful disadvantage across price, applicable safety results, reliability evidence, condition, mileage, and required family usability — and improves at least one. Evidence is imperfect, so the standard is **"likely dominated"**, not exact mathematical certainty.
- **Buying rules, in brief:** favor a 2021–22 Highlander when its delivered price and condition are competitive with the 2023 Pilot; favor the 2023 Pilot when family usability or condition is materially better and it fits ~$30k OTD with reserve intact; keep the 2022 CX-9 when savings or lower mileage are substantial; keep the 2023 Telluride and Ascent for their safety advantages without making them the default reliability choices; keep Langdale as a real lower-cost alternative, not the safety winner; never stretch into a poor-history, high-mileage example for a newer badge; no final endorsement before a written unconditional quote, VIN-specific recall review, and independent inspection.
- `PARETO_GUIDE.md` is controlling for search targets and evaluation criteria where it and this protocol conflict.

## Safety

- No agent contacts sellers or dealers on Stephen's behalf. Drafts and analysis only.
- No deposits, holds, or purchases — ever. Stephen makes all calls and all decisions.
- A listing being "text-confirmed" is recorded as exactly that, never upgraded to photo-confirmed.
