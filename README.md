# Multi-Agent Car Search

Shared system of record for the Finney family's three-row SUV search, worked jointly by multiple AI agents (Muse in chat, Claude Code, Codex, Muse Code) under Stephen's direction.

## Purpose

One canonical place for candidate vehicles, verification status, and decisions — so every agent works from the same facts instead of re-deriving them from chat history.

## How the repo is organized

- `board.md` — index of all live candidates and the current open decision. Start here.
- `candidates/` — one Markdown file per candidate vehicle. Status, verified facts, open gates, dated log.
- `eliminated/` — vehicles ruled out, with the reason preserved so they are never re-researched.
- `TASKS.md` — seed task queue; will become GitHub Issues once a remote exists.
- `PROTOCOL.md` — the rules every agent follows. Read it before changing anything.

## Rules of the road

- Stephen has final say on every decision: which constraint bends, which car, any money.
- Agents produce research, verification, and drafts only. No agent contacts sellers or dealers, places deposits, or makes purchases.
- Facts in candidate files are either verified (and say how) or labeled unverified. Listing text is never treated as verification.

See [PROTOCOL.md](PROTOCOL.md) for the full protocol and [board.md](board.md) for the current board.
