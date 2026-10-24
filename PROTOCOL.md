# Protocol

Every agent working this search follows these rules. If a rule conflicts with an ad-hoc instruction, follow the rule and flag the conflict.

## Source of truth

- This repo is the source of truth. Chat history and memory files are not.
- One Markdown file per candidate vehicle in `candidates/`.
- Eliminated vehicles move to `eliminated/` with the reason recorded. Never delete a candidate file outright.

## Requirements (firm)

- Three-row SUV.
- Georgia only.
- Non-white exterior.
- Second-row captain's chairs.
- Budget: $20,000 nominal. Working ceiling ~$28,000 applies only by Stephen's explicit bend decision (see `board.md` open decision).

## Verification rules

- Never trust listing text or trim badges for required attributes. Captain's chairs and exterior color require photo confirmation or a dealer call.
- Compute the real out-the-door price from the dealer's own numbers: advertised price + doc/fees + Georgia TAVT 7%. An advertised price that excludes fees or assumes incentives is not a price.
- History reports are necessary, not sufficient — the **Canton rule**: a clean CARFAX on the Canton 2016 Pilot Elite missed ~$3–4k of damage that only an independent pre-purchase inspection (PPI) found. An independent PPI is a mandatory gate before any deposit on any vehicle.
- Assume undocumented timing-belt service is due: budget +~$1,200 on Honda V6s. A seller claim is not documentation.

## Claiming work

- Tasks live as GitHub Issues (seed list in `TASKS.md` until a remote exists).
- Claim by assigning yourself and/or labeling `claimed:<agent-name>`, with a timestamp comment.
- Do not edit a candidate file another agent has claimed in an open issue.
- Append findings as dated sections. Never rewrite or delete another agent's entries.

## Candidate status vocabulary

Use exactly one in each candidate file:

- `lead` — found, not yet verified.
- `verified` — required attributes photo- or call-confirmed; OTD price known.
- `finalist` — verified and through (or scheduled for) the PPI gate.
- `eliminated` — ruled out; file lives in `eliminated/` with the reason.
- `purchased` — bought. Search over.

## Commits

- Small commits: one vehicle or one task per commit.
- Message format: `<agent>: <change>` (e.g. `claude-code: verify pristine belt status`).
- Do not commit over another agent's uncommitted claimed work.

## Division of labor

- **CLI agents (Claude Code, Codex, Muse Code):** bulk listing sweeps, VIN decode + NHTSA recalls/complaints checks, price history, dedupe, arithmetic (OTD, financing).
- **Muse (chat agent):** Facebook Marketplace (account-connected), other account-connected checks, photo verification, dealer-page fee checks, board judgment and synthesis.
- **Heavy reasoning passes** on finalists go to whichever frontier harness is assigned.

## Safety

- No agent contacts sellers or dealers on Stephen's behalf. Drafts and analysis only.
- No deposits, holds, or purchases — ever. Stephen makes all calls and all decisions.
- A listing being "text-confirmed" is recorded as exactly that, never upgraded to verified.
