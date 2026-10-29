This repo is a multi-agent SUV search. Read PROTOCOL.md and PARETO_GUIDE.md before doing anything.
Your role and handoff stage are defined there — CLI agents build tooling in tools/ and file search matches as candidates.
One file per candidate in candidates/; advance only your own workflow stage via the status field.
Append dated log entries; never rewrite another agent's log entries.

## Facebook Marketplace lane (added 2026-10-29)
Run the Facebook lane through the linked facebook-cli connector (`marketplace search`), never the browser — the browser session is login-gated and the 2026-10-29 sweep's FB lane failed for that reason. The connector account is linked and verified. Use trim-specific queries ("Honda Pilot Touring" / "Honda Pilot Elite") with best_match sort; a bare "Honda Pilot" query returns loose category results. Macon origin 32.8407,-83.6324, radius 100 mi (FB's useful cap).
